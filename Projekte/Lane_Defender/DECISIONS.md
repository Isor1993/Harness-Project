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
**Fortgeführt am 2026-09-20:** Spielgerüst und Pflichtthemen gelten;
abgelöst sind drei Teile — der Upgrade-Screen zwischen den Leveln
(„Live-Shop: Kaufen mitten im Lauf"), die Lane-Staffel „Start 1,
alle drei Level +1" („Lane-Progression 2/3/4 an den Boss-Siegen")
und die Skill-Freischaltung durch den Boss-Sieg (ebenfalls
Live-Shop-Eintrag).
**Fortgeführt am 2026-09-27:** Der Gegner-Zuschnitt ist abgelöst —
der Runner entfällt als Typ, das Tempo wird globaler Level-Wert; neu
sind Normal/Tank/Boss (Eintrag „Gegner-Hierarchie: Normal, Tank,
Boss", 2026-09-27).

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
**Fortgeführt am 2026-09-13:** Der Grundsatz bleibt — nichts verschiebt
sich —, aber der Weg dorthin ist für die Figuren-Symbole präzisiert:
Nach der Messung des Zeichentests plant das Spielfeld die
Schachfiguren als **fest doppelbreite** Zeichen ein, statt sie
auszuschließen („Schachfiguren gesetzt", unten). Einzelbreite bleibt
Pflicht für alles, was im Raster neben Unbekanntem steht (Rahmen,
HUD, Schuss).

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
**Fortgeführt am 2026-09-13:** Dazu kommt das Compiler-Flag `/utf-8`
(alle Konfigurationen der .vcxproj): Quelldateien und String-Literale
gelten als UTF-8 — die Rahmenzeichen-Literale tragen damit genau die
Bytes, die die per `SetConsoleOutputCP(CP_UTF8)` umgestellte Konsole
erwartet. Ohne das Flag hinge Quell-Lesart und Ausgabe an der
zufälligen System-Codepage.

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
**Fortgeführt am 2026-09-13:** „Mehr Dateien erst ab M2" ist für die
Ausgabe-Helfer abgelöst — die PrintMessage-Familie zieht sofort in
`Output.h`/`Output.cpp` („Ausgabe-Helfer ziehen in Output.h/Output.cpp",
unten). Der Rest des Eintrags gilt unverändert.

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

## 2026-09-13 — Szenen melden die nächste Szene (Melde-Muster)
Was: Der M1-Zustandsautomat läuft als Melde-Muster: Jede
Szenen-Funktion gibt `E_GAME_SCENES` zurück, `main` hält den Zustand
als lokale Variable, wischt je Runde (ClearScreen samt Scrollback)
und weist im switch zu; `GS_EXIT` beendet `main` direkt. Der
Szenen-Typ und die Prototypen wohnen in `LaneDefender.h` — nur
Zusagen, keine Variablen. Der Symbol-Test bleibt eigener Zustand und
meldet selbst „danach Hauptmenü".
Warum: Isors Architektur-Anforderung vom 2026-09-13 — main clean,
Szenen später als eigene Controller auslagerbar, ohne
Automat-Innereien zu kennen; sein Merksatz „Funktionen melden,
Aufrufer entscheiden" als Bauform. Der erste Wurf (ChangeScene plus
geteilte Variable) brach genau an der Auslagerung: Eine Variable im
Header wird per Include-Textkopie mehrfach definiert.
Verworfen: ChangeScene mit Variable auf Datei-Ebene (funktionierte,
koppelt aber jede ausgelagerte Szene an den Automaten); die
Zustandsvariable im Header; ein `RunEndProgramm` (nur main kann main
beenden — der GS_EXIT-case returnt selbst); ein Pointer auf die
aktuelle Szene (der Inhalt wechselt im selben Karton, kein
Ziel-Wechsel zwischen Objekten).

## 2026-09-13 — Zeichentest-Ergebnis: 26 rasterfest, Schach doppelbreit
Was: Erster Lauf der Zeichentest-Szene (VS-Konsole und Windows
Terminal — beide rendern identisch, VS nutzt inzwischen die
Windows-Terminal-Engine). Bestanden mit bündigem rechten Rand: alle
15 ASCII-Kandidaten, die Linien `│ ─`, die Ecken `┌ ┐ └ ┘`, die
Blöcke `█ ▓ ░`, die Halbblöcke `▀ ▄` — 26 Zeichen. Die vier
Schachfiguren `♟ ♜ ♞ ♚` belegen in beiden Terminals zwei Zellen
(Glyphe ≈1,5 Zellen breit), und der Bauer rendert als farbiges Emoji,
dessen Farbe kein VT-Code ändert. Eine Textform mit angehängtem
U+FE0E („als Text rendern") wurde mitgemessen, änderte nichts und ist
wieder aus der Kandidatenliste entfernt; die Schachfiguren bleiben
als Bewerber für die Doppelbreit-Route drin.
Warum: Abnahme mit dem Auge gegen die Lineal-Zeile (Isor,
2026-09-13); zwei Terminals als zwei Brillen, wie im Test-Design
vorgesehen.
Verworfen: die Schachfiguren als Einzelzell-Symbole (gemessen
doppelbreit); der U+FE0E-Trick (gemessen wirkungslos). Offen bleibt
die Doppelbreit-Route über das Lane-Layout (ROADMAP → „Lane-Layout
für Doppelbreit-Symbole prüfen") — das entscheidet der
M2-Design-Abschnitt.
**Fortgeführt am 2026-09-21:** Der B1-Lauf-Test misst feiner — es
gibt zwei Breiten je Zeichen: das **Vorrücken** des Cursors und die
**Glyphen-Breite**. Der Bauer rückt im Spiel-Terminal nur **eine**
Zelle vor, die Glyphe malt ~1,5 Zellen — eine voll, die Nachbarzelle
etwa zur Hälfte (Isors Diagnose „zählt als 1, benutzt heimlich 2",
per Zoom am Zellraster nachgemessen; Beleg: sein
Wandbündigkeits-Fix in B1 plus T-Szenen-Gegenprobe im selben Lauf —
Ränder bündig, Figuren überlappt). Die Glyphen-Breite ≈1,5 stand
schon im Messprotokoll vom 13.09. — neu ist nur die Vorrück-Lesart
(damals als 2 gelesen, warum, bleibt offen). Fürs Zeilenbauen zählt
eine Figur damit **1 Spalte** und braucht eine **Leerzelle rechts**
als Überzeichnungs-Raum — die feste Mittelposition mit Luft liefert
den ohnehin. Das Messgerät bleibt die T-Szene; Breite bleibt
Messfrage je Terminal.

## 2026-09-13 — Schachfiguren gesetzt, Lanes werden dafür ausgelegt
Was: Die Schachfiguren `♟ ♜ ♞ ♚` sind als Figuren-Symbole des Spiels
gesetzt (Zuordnung je Gegnertyp final beim Bau von M3, Favoriten nach
ROADMAP-Reihenfolge: Runner `♟`, Tank `♜`, Boss `♚`). Das Spielfeld
wird dafür ausgelegt: Figuren belegen fest zwei Zellen; Isors
Lane-Entwurf (Wand + vier Leerzellen + Wand, Figur auf fester
Mittelposition, Schuss zwei Zellen breit) ist die Bauvorlage für den
M2-Design-Abschnitt.
Warum: Isors Entscheid vom 2026-09-13 nach dem Zeichentest — die
Optik ist ihm den Preis wert, und die Messung trägt die Entscheidung:
Beide Brillen (VS-Konsole und Windows Terminal, gleiche
Terminal-Engine) rendern die Figuren identisch doppelbreit, es braucht
also keine zwei Druck-Logiken auf diesem Rechner. Der Preis ist
benannt: Sonderbreiten-Logik beim Zeilenbau, die Bauern-Farbe gehört
dem Terminal (Emoji, kein VT-Code greift), und ein fremdes
Prüfer-Terminal bleibt Restrisiko — dagegen steht der Zeichentest als
eingebaute Szene (Taste `T`) für den Nachweis vor Ort.
Verworfen: ASCII-Einzelzeichen als Figuren-Symbole (rasterfest
gemessen, aber „sieht grausam aus" — sie bleiben Rückfall, falls ein
fremdes Terminal die Figuren zerlegt); die Doppelbreit-Route wieder
aufzumachen — entschieden ist entschieden, M2 gestaltet nur noch aus.
**Fortgeführt am 2026-09-20:** ausgestaltet — der M2-Screen-Eintrag
(„Design ‚Gerahmt'") legt die Korridore auf innen 8 statt „Wand +
vier Leerzellen + Wand"; Doppelbreite, feste Mittelposition und
ASCII-Rückfall gelten unverändert.
**Fortgeführt am 2026-09-27:** Die Zuordnung ist final — Normal `♟`,
Tank `♜`, Boss `♚`, `♞` bleibt Reserve für den A1-Ausbau (Eintrag
„Figuren-Zuordnung final", 2026-09-27).

## 2026-09-13 — Ausgabe-Helfer ziehen in Output.h/Output.cpp
Was: Die PrintMessage-Familie (fünf Überladungen) zieht aus
`LaneDefender.cpp` in ein eigenes Datei-Paar `Output.h`/`Output.cpp` —
Zuständigkeit: formatierte Konsolen-Ausgabe. Freie Funktionen wie
bisher, keine Klasse. `LoseLives` wandert **nicht** mit (Spiellogik,
keine Ausgabe) und wurde im selben Zug komplett entfernt: kein
Aufrufer mehr — es kommt wie `ReadValueInput` aus der Sicherung
zurück, sobald ein Aufrufer existiert (M6-Umfeld), und landet dann
gleich in der Klassenstruktur, die es bis dahin gibt. In Output kommt
nur, was zur benannten Zuständigkeit gehört — die Datei ist kein
Sammelort für Helfer aller Art.
Warum: Isors Entscheid vom 2026-09-13 — von Anfang an nach
Zuständigkeit trennen statt bei M2 zwischen frischem Klassen-Code
aufzuräumen; die Trennung kostet jetzt Minuten und ist selbst Lernziel.
C#-Übersetzung dahinter: Die Zuständigkeit einer C#-Klasse trägt in C++
das .h/.cpp-Paar; eine Klasse entsteht nur, wo Zustand und Verhalten
zusammengehören (M1-Ablauf-Eintrag). Erster selbst angelegter Header.
Verworfen: Aufteilung erst ab M2 (Freitag-Stand — vom Kostenargument
geschlagen); eine Printer-Klasse (kein Zustand, Klasse als
Selbstzweck); eine Sammel-Datei „Utils/Helpers" (genau der Müllsack,
gegen den die Trennung schützt); `LoseLives` ohne Aufrufer in
`LaneDefender.cpp` stehen lassen (erste Fassung dieses Eintrags —
noch am selben Tag vom Toter-Code-Argument geschlagen, das schon
`ReadValueInput` entfernt hat).

## 2026-09-18 — Zielbreite 120, Zentrierung als eingebautes Padding
Was: Alle Bildschirme sind auf `I_SCREEN_WIDTH = 120` Spalten
ausgelegt (Konstante in Console.h, der Windows-Terminal-Standard).
ASCII-Blöcke werden **blockweise** zentriert: ein gemeinsames Padding
je Block nach seiner breitesten Zeile, als Leerzeichen direkt im
Raw-String — nie Tabs, die Konsole springt damit aufs Achter-Raster
(der Versatz-Bug vom 18.09.).
Warum: Zentrieren ist ausgerechnetes Padding und braucht weder
SetCursor noch Laufzeit-Parsing; blockweise, weil zeilenweises
Zentrieren die Linien-Schrift zerreißt (Zeilen von 61 bis 72 Zeichen
bekämen verschiedene Ränder).
Verworfen: Zentrierung per SetCursor je Zeile (bricht das
Ein-Puffer-Rendering); eine Laufzeit-Zentrierfunktion (Parsing ohne
Not — kommt erst, wenn variable Inhalte sie brauchen); 80 Spalten als
Zielbreite (der 72er-Titel ließe nur 4 Spalten Rand).

## 2026-09-18 — Auswahl-Marker wandert im Frame, SetCursor erst zur Namenseingabe
Was: Auch die Menü-Auswahl bleibt im Ein-Puffer-Muster: Der Zustand
ist die Auswahl-Zahl, jeder Tastendruck baut den Frame neu, der
Marker steht in der Button-Zeile, deren Nummer die Zahl ist; die
Menü-Schleife sendet ab Cursor-Home und überschreibt — ClearScreen
läuft nur beim Szenenwechsel in main. `SetCursorPosition` wird erst
mit ihrem ersten echten Nutzer gebaut, der Namenseingabe.
Warum: Flackern ist das leere Zwischenbild beim Löschen, nicht das
Neuschreiben — Home-statt-Löschen deckt Isors Flacker-Sorge bereits
(Beschluss vom Zeichentest); eine auf Vorrat gebaute
SetCursor-Funktion läge ungenutzt und ungetestet in der Abgabe.
Verworfen: das Auswahl-Symbol einzeln per SetCursor nachzeichnen
(zweite Druck-Logik neben dem Puffer, Optimierung ohne gemessene
Not — Isors Vorschlag vom 14./18.09., am eigenen
Home-statt-Löschen-Beschluss entschieden); SetCursorPosition auf
Vorrat bauen.

## 2026-09-18 — Der Titel: Figlet „Standard" voll ausgelegt statt Blockschrift
Was: Der Menü-Titel ist der Figlet-Font „Standard" in voller
Buchstabenbreite (patorjk-Generator, Isors Link als Quelle), fünf
Zeilen, breiteste 72 Zeichen; die Rohfassung liegt in
`Sandbox/M1_Titel_LaneDefender.txt`. Start und Exit tragen dieselbe
Schrift als Buttons (Isors eigene Blöcke vom 14.–18.09.).
Warum: Reines ASCII — rasterfest ohne Sonderfälle und ohne den
Zeichentest zu bemühen; passt mit 24 Spalten Rand in die
120er-Breite; die Linien-Schrift-Entscheidung vom 12.09. bleibt
erfüllt.
Verworfen: die gefüllte Blockschrift (Isors Favorit, ~128 Zeichen —
läuft in jedem Standard-Terminal über und schied an der Breite aus);
die kursiven Fassungen (das L las sich als Z — „Zane Defender").

## 2026-09-19 — Marker-Optik: Balken unter dem Button plus Gelbfärbung
Was: Der gewählte Menü-Button trägt einen Unterstrich-Balken in
Blockbreite direkt unter der Schrift (Start 47 Leerzeichen + 25
Striche, Exit 51 + 18) und wird samt Balken gelb gefärbt (VT-Farben
aus Console.h). Der nicht gewählte Button schreibt statt des Balkens
eine Putz-Zeile aus 72 Leerzeichen — eine Leerzeile aus bloßem `\n`
beschreibt null Zellen, und das Terminal behält, was niemand
überschreibt. Umgesetzt in Isors gemeinsamer Methode
`AddSelectedMarker(bool, Block, Balken-Zeile)`; was sich je Aufrufer
unterscheidet, kommt als Parameter.
Warum: Das einzelne `>` vom 12.09. stammt aus der Zeit einzeilig
gedachter Buttons; neben den fünf Zeilen hohen
Linien-Schrift-Blöcken vom 18.09. wirkte es verloren (Isor,
2026-09-19). Balken war Isors eigener Vorschlag, die Farbe kam als
Kombination dazu — billigster Bau der vier Kandidaten, und Form plus
Farbe tragen die Auswahl doppelt.
Verworfen: das einzelne `>` (von der Linien-Schrift überholt); der
fünfzeilige Pfeil (Isors zweiter Kandidat — Fünf-Platzhalter-Bau,
Zeitkosten vor dem Streckziel); der Rahmen um den Button (teuerster
Umbau, bleibt Polish-Kandidat fürs M7-Umfeld); das
find-Platzhalter-Verfahren für ein Einzelzeichen (mit der
Balken-Entscheidung gegenstandslos).

## 2026-09-19 — Sound als freie Funktionen, benannt nach Bedeutung
Was: Audio-Feedback wohnt im Paar `Sound.h`/`Sound.cpp`:
`PlayMenuMoveSound`, `PlayMenuConfirmSound`, `PlayErrorSound` (zwei
fallende Beeps, Isors „dü-dü") — freie Funktionen, alle Frequenzen
und Dauern als benannte Konstanten im .cpp, `windows.h` nur dort.
Aufrufer sagen, was passiert ist; wie es klingt, weiß allein
Sound.cpp. Der default-Fall des Menüs meldet unbelegte Tasten über
den Error-Sound.
Warum: Isors eigener Schnitt nach seinem Output-Muster vom 13.09. —
kein Zustand, also keine Klasse; die Beep-Literale des Erstwurfs in
den cases waren Magic Numbers, und die Benennung nach Bedeutung
macht das Umstimmen zur Ein-Datei-Änderung. WinAPI-`Beep` blockiert
für die Ton-Dauer — Frequenzen und Dauern bleiben deshalb
ausdrücklich Regler (Feintuning offen, 80/60 Hz sind auf kleinen
Lautsprechern ein Restrisiko).
Verworfen: Beep-Aufrufe mit Literalen direkt in den cases (Isors
Erstwurf, an der eigenen Magic-Number-Regel gescheitert); eine
Sound-Klasse (kein Zustand, Klasse als Selbstzweck); das
Klingel-Zeichen `\a` (ein Ton für vier Bedeutungen); `windows.h` im
Aufrufer MainMenu (WinAPI wohnt im .cpp der Technik-Schicht,
Console macht es vor).

## 2026-09-19 — Namenseingabe: Dialogfenster, Slots und Fokus-Modell
Was: Die Szene zeigt ein zentriertes Dialogfenster (62 Spalten,
Zeilen 7–20 der 120×30): Aufforderung, drei Regel-Zeilen (bis 16
Zeichen · A–Z a–z 0–9 · leer wird „Player"), das Eingabefeld als 16
Unterstrich-Slots, die sich beim Tippen füllen, die Fehlerzeile
direkt unter dem Feld; unten links Back, unten rechts Confirm als
Textzeilen mit dem Unterstrich-Marker des Hauptmenüs. Spieltexte
Englisch. Fokus-Modell: ↓/↑ wechseln zwischen Feld und Button-Zeile,
←/→ (+A/D) wechseln Back/Confirm, Enter im Feld prüft und springt
bei gültigem Namen auf Confirm (Schnellweg Enter–Enter), Enter auf
dem Button führt aus, ESC ist von überall der Rückweg ins Menü.
Warum: Isors Skizze vom 2026-09-19 — Message-Fenster-Metapher,
Regeln vor dem Fehler zeigen, Fehler am Feld melden; das freie
Fokus-Modell ersetzt den zweiphasigen Zwang, der sich in der
Design-Runde als unnatürlich erwies: Der Spieler wählt selbst, wo
er ist.
Verworfen: der zweiphasige Pflicht-Ablauf (erst Name, dann Buttons —
so der Plan vom 12.09., vom Fokus-Modell abgelöst); der
Eingabekasten mit eigenem Rahmen (Isors erste Skizze — die Slots
zeigen die Restlänge und sind eine Zeile statt drei);
gemischtsprachige Bildschirmtexte (Sprachregel: Ausgaben Englisch).

## 2026-09-19 — Eingabe selbst gezeichnet — löst den getline-Beschluss ab
Was: Die Namenseingabe liest keine Zeile über `getline`, sondern
läuft als Zeichen-Schleife im Home-Frame-Muster des Hauptmenüs:
`ReadKey` liefert jede Taste, eine Whitelist (`A–Z`, `a–z`, `0–9`)
hängt erlaubte Zeichen an den Namen an, Backspace löscht (Wächter
gegen leeren Namen), das 17. Zeichen und jedes fremde Zeichen enden
im Error-Sound. Enter prüft: leer → „Player", sonst übernehmen.
Unverändert bleiben Prüfung nach Enter für den Leer-Fall, der
Default, die 16er-Grenze und die Meldung, die die Regel nennt.
Löst ab: „Namensregeln der Namenseingabe" vom 2026-09-12, dessen
Lese-Werkzeug getline war.
Warum: getline ist modal — solange getippt wird, gehört die
Tastatur der Konsole, ein Fokuswechsel auf die Buttons ist
unmöglich. Das Selbst-Zeichnen macht den Fokus frei, hält die Slots
formstabil (kein Echo-Überlauf), erlaubt die Färbung des Getippten
und tilgt das letzte `cin` aus dem Projekt — der Problemraum des
liegengebliebenen `\n` entfällt, der M7-Check „formatiertes Lesen
übrig?" wird trivial. Die 12.09.-Ablehnung der eigenen
Eingabeschleife („ohne Mehrwert") ist damit überholt: Der Mehrwert
existiert jetzt und ist benannt. Preis, ebenfalls benannt: nur
Backspace statt getlines Zeilen-Editing — bei 16 Zeichen ein
Radiergummi statt eines Texteditors, das reicht.
Verworfen: getline (modal; Echo läuft bei Überlänge übers Feld);
die sofortige Generalisierung der Auswahl-Mechanik zum
wiederverwendbaren Baustein (der zweite Nutzer ist waagerecht und
textbasiert — die Abstraktions-Entscheidung fällt beim dritten
Nutzer, dem M4-Upgrade-Screen).

## 2026-09-19 — Farbsprache: Gelb heißt „hier bist du", Hellrot heißt Fehler
Was: Es gibt genau eine Aktiv-Farbe im Spiel: Gelb trägt das
fokussierte Element — im Menü den gewählten Button samt Balken, in
der Namenseingabe das Feld samt getipptem Namen bzw. den gewählten
Button. Fehlermeldungen sind hellrot (neue Konstante `S_COLOR_RED`,
VT-Code 91); die Fehlerzeile nennt weiterhin die Regel im Text.
Löst ab: die Verwerfung „Rot als Fehlerfarbe" vom 2026-09-12.
Warum: Isors Argument aus der Design-Runde — das Getippte braucht
eine eigene Kennzeichnung, damit man sieht, wo man ist; damit sind
zwei Signale zu vergeben, und zwei Signale brauchen zwei Farben.
Die 12.09.-Verwerfung fiel, als es nur ein Signal gab. Hellrot
statt Dunkelrot wegen des Kontrasts auf Schwarz; der Text bleibt
der zweite Träger neben der Farbe.
Verworfen: Gelb für beides (Aktiv und Fehler wären
ununterscheidbar); Dunkelrot (VT-Code 31, kontrastschwach auf
Schwarz); ein Fehlertext ohne Regelnennung („Invalid input" allein
sagt nicht, was zu tun ist).

## 2026-09-19 — Namenseingabe-Feinschliff: Balance, kurze Linie, Schreiblinie
Was: Drei Nachbesserungen am Fenster-Layout aus der Sichtprüfung des
gebauten Screens. Erstens die Zeilen-Balance: Regeln auf die
Fensterzeilen 6–8, Name auf 10 — der Inhalt klumpte sonst oben und
ließ vier tote Zeilen unter sich. Zweitens die Trennlinie: 40 Spalten
bündig unter dem Aufforderungstext statt Wand zu Wand (der Bauer
rechnet die Ränder selbst und zählt Spalten per Schleife, nie Bytes).
Drittens die Schreiblinie: Die 16 Unterstrich-Slots wandern eine
Zeile UNTER die Tippzeile (Fensterzeile 11, Fehlerzeile rückt auf
12) — getippt wird auf leeren Zellen über der Linie, wie auf einem
Formular. Dazu die Back/Confirm-Zeile als Bildschirmzeile 28
(Beschriftung „Confirm", nicht „Start Game"); Marker-Linie und
Farben folgen erst mit der Eingabe-Schleife.
Warum: Isors Optik-Urteil am laufenden Programm (kopflastige
Aufteilung — die zufällige Luftigkeit des Verteiler-Bugs hatte ihm
besser gefallen und wurde zum bewussten Regler); die Schreiblinie
ist Isors eigener Einwand: Der echte Konsolen-Cursor ist je nach
Terminal-Einstellung selbst ein Unterstrich und bliebe auf einem
Slot unsichtbar — auf leerer Zelle über der Linie blinkt er bei
jeder Cursor-Form, und die Linie bleibt als Längen-Budget lesbar.
Verworfen: Slots in der Tippzeile (Cursor-Form-Restrisiko —
dieselbe Sorge wie beim fremden Prüfer-Terminal); die
Wand-zu-Wand-Trennlinie (erschlug die Aufforderung); das
kopflastige Erst-Layout; eine Strich-Konstante durch den
Textzeilen-Bauer (Byte-Falle — Striche wiegen drei); die
Beschriftung „Start Game" (nach Confirm kommt erst die
Steuerungs-Szene, der Knopf würde mehr versprechen als kommt).

## 2026-09-19 — Enter ist der einzige Ausgang aus dem Eingabefeld
Was: Die Steuerung der Namenseingabe verzweigt zuerst nach Fokus
(Feld gegen Button-Zeile), dann nach Taste — zwei kleine switches
statt einem großen. Im Feld führt nur Enter hinunter (Sprung auf
Confirm) und ESC hinaus; auf der Button-Zeile wechseln ←/→ (+A/D)
zwischen Back und Confirm per direkter Zuweisung statt
Zahlen-Arithmetik, ↑/W führt zurück ins Feld, Enter führt aus, der
default meldet unbelegte Tasten mit dem Fehlerton. Der Feld-default
bleibt bewusst lautlos — dort landen später die getippten Zeichen.
Löst ab: den ↓/↑-Freiwechsel aus „Namenseingabe: Dialogfenster,
Slots und Fokus-Modell" (2026-09-19, Vormittag); Fenster, Slots,
Schnellweg Enter–Enter und ESC-Rückweg gelten unverändert.
Warum: Isors Vorschlag beim Bau — Enter ist der natürliche
„fertig getippt"-Moment, und der Einwand gegen den
Zwei-Phasen-Zwang trifft nicht, weil der Rückweg (↑/W) offen
bleibt. Nebengewinn: Der Feld-Zweig bleibt klein (Enter, ESC,
später das Tippen), und die Button-Zeile hat nur zwei Stationen —
zuweisen statt zählen, keine Klemm-Arithmetik.
Verworfen: ↓ als zweiter Ausgang aus dem Feld (ein Weg reicht;
W/A/S/D müssen im Feld tippbar bleiben — nur echte Pfeile könnten
dort navigieren); die Drei-Stationen-Zahlenlinie mit +1/−1 und
Klemmen (ließ ←/→ aus dem Feld hinauswandern — Isors erster
Wurf, am Bild „Dreieck gegen Zahlenlinie" verworfen).

## 2026-09-19 — Spielername wohnt sofort in einer Mini-Player-Klasse
Was: Der Name lebt in `CPlayer` (`Player.h`/`Player.cpp`): privater
Member `m_sName{}`, Zugriff über `SetName(const std::string&)` und
`std::string GetName() const` (Kopie-Rückgabe). Das Objekt lebt als
Wert in main und reist als `CPlayer&`-Referenz in die Szene —
`RunNameInputScreen(CPlayer&)`. Kein Pointer. M2 baut die Klasse
aus (Lanes, Leben, Position), der Name ist dann schon zu Hause.
Warum: Isors Entscheidung gegen Claudes String-in-main-Empfehlung —
einmal richtig angehen statt späterer Umzugsarbeit; die Klasse
kommt mit M2 ohnehin, und der Bau war zugleich die erste eigene
C++-Klasse (Lernwert eingepreist).
Verworfen: nackter `std::string` in main mit Referenz-Durchreichung
(Claudes Empfehlung — nur zwei Zeilen Umzug später, aber eben
Umzug); ein Pointer (die Referenz reicht, das Objekt lebt in main);
`GetName` als const-Referenz-Rückgabe (Kopie ist bei 16 Zeichen
gratis und in der Abgabe leichter zu verteidigen).

## 2026-09-19 — Grün als Fokusfarbe geprüft und verworfen
Was: Gelb bleibt die einzige Aktiv-Farbe; die „Farbsprache" vom
2026-09-19 steht unverändert. Anlass war ein Grün-Vorschlag aus
Isors Umfeld; geprüft wurde mit Leuchtdichte-Zahlen und
Deuteranopie-Simulation statt nach Gefühl.
Warum: Zwei Signale (Fokus und Fehler) mit Grün und Hellrot wären
ein Rot-Grün-Paar — für Isor selbst und etwa jeden zwölften
männlichen Spieler kollabieren beide zu ähnlichem Oliv (Simulation:
Grün 92 und Hellrot 91 werden oliv, Gelb 93 bleibt nahezu
unverändert). Helligkeit trägt als zweiter Kanal: Kontrast auf
Schwarz Gelb ~18:1, Grün ~9:1, Hellrot ~5,5:1 — Gelb/Rot trennt
rund 3,8-fach in der Leuchtdichte, Grün/Rot nur 1,8-fach. Dazu
Bedeutungsballast: Grün hieße „gültig", bevor geprüft ist. Und
einen Grün-Bau könnte Isor selbst nicht abnehmen.
Verworfen: Grün (VT 92) als Fokusfarbe. Offen gehalten: Cyan
(VT 96, liegt in Console.h) als farbfehlsichtig-sichere
Ausweichfarbe, falls Gelb je stört; die Dozentin-Frage steht als
Merkpunkt in der ROADMAP dieser Schicht.

## 2026-09-20 — Titel-Einblendung gestrichen
Was: Es gibt keine Start-Einblendung des Titels — das Menü steht
sofort. Löst ab: den Einblendungs-Teil aus „Menü-Bedienung und
Titel-Optik" (2026-09-12); Buttons, Marker, Farben und Linien-Schrift
gelten unverändert.
Warum: Isors Schnitt am 2026-09-20 unter Zeitdruck — reiner Zierrat
ohne Lern- oder Bewertungswert, die Abgabe verlangt ihn nicht. Der
Verzicht sparte zwei Console-Werkzeuge (Tasten-Warteschlange,
Warten), die nur die Einblendung gebraucht hätte.
Verworfen: die zeilenweise Einblendung mit Tasten-Skip (fertig
entworfen und als Vorschau gezeigt — bleibt Polish-Kandidat, falls
M7 Luft hat).

## 2026-09-20 — Doku-Input je Baustein statt Abgabetext sofort
Was: Der Abgabetext entsteht am Projektende in einem Zug; nach jedem
Meilenstein wird nur Roh-Input festgehalten — in `ABGABE_NOTIZEN.md`
dieser Schicht (Zeit, Gebautes, Begründungen, Besonderheiten). Für
Lane Defender gilt die Baustein-Bedingung „dokumentiert" damit als
erfüllt, sobald der Input des Meilensteins dort steht.
Warum: Isor am 2026-09-20 — Doku-Aufwand bündeln, solange offen ist,
wie ausführlich die Abgabe-Doku überhaupt wird (womöglich nur Tabelle
plus README); der Input direkt nach dem Baustein hält die Fakten
frisch, ohne Form-Arbeit vor der Form-Entscheidung.
Verworfen: der ausformulierte Abgabe-Abschnitt je Baustein
(Form-Arbeit vor Klarheit über die Form); gar kein Zwischenstand
(am Projektende wären die Begründungen aus dem Kopf).

## 2026-09-20 — M2-Screen: Design „Gerahmt" mit getrennten Korridoren
Was: Der Spielbildschirm (120×30) ist dreigeteilt: HUD-Kasten oben
(Zeilen 1–3: Player, Gold, Damage, Atk Speed, Skill, Level),
Shop-Kasten unten (Zeilen 25–28), dazwischen das Feld — Lanes als
getrennte Korridore mit eigenen Wänden, Kappe oben (Zeile 4) und
offenem Ende unten; innen 8 Spalten, Lücke 6. Gegnerlauf Zeilen 5–22
(18 Zeilen ≈ 3,6 s bei 200-ms-Tick), Spielerzone Zeilen 23–24 unter
dem offenen Ende, Zeile 29 Luft, Zeile 30 bleibt frei
(Scroll-Wächter aus M1). Feldbreite zentriert je Stufe: 2 Lanes 26,
3 Lanes 42, 4 Lanes 58 Spalten; nicht freigeschaltete Lanes werden
nicht gezeichnet.
Warum: Isors Grobziel-Skizze vom 2026-09-20 (HUD oben, Shop unten,
Korridore), gewählt aus drei voll gerenderten Design-Beispielen —
die Kasten-Optik der Skizze war ihm die drei Feldzeilen und zwei
Rahmenbauer wert. Logisch gespeichert wird nur (Lane, Zeile); die
Doppelbreite der Figuren lebt allein im Zeichnen weiter, ein Treffer
bleibt „gleiche Lane, gleiche Zeile".
Verworfen: das Brett mit geteilten Wänden (dichtestes Bild, aber am
weitesten weg von der Skizze); Korridore mit Trennlinien statt
Kästen (Claudes Empfehlung — mehr Feldhöhe, Isor wählte die
Skizzen-Nähe); Innenbreiten 4 und 6 (zu gedrungen für die
120er-Breite).

## 2026-09-20 — Live-Shop: Kaufen mitten im Lauf
Was: Der Shop ist der Kasten unten am Spielbildschirm und immer
offen: [1] Damage 100G · [2] Atk Speed 120G · [3] Life 500G ·
[4] Multishot 2000G — Kauf per Zifferntaste während der
Tick-Schleife, zu wenig Gold meldet der Error-Sound. Es gibt erstmal
genau einen Skill (Multishot), gekauft statt beim Boss-Sieg
freigeschaltet; was er tut und wie der Slot ihn trägt, klärt das
M5-Design — der polymorphe Skill-Slot bleibt (Zeiger startet leer,
der Kauf belegt ihn). Löst ab: den Upgrade-Screen zwischen den
Leveln und die Skill-Freischaltung durch den ersten Boss-Sieg
(„Umschwenk auf den Lane-Shooter", 2026-09-07).
Warum: Isors Entscheid vom 2026-09-20 — Kaufen unter Druck macht das
Spiel spaßiger; und es ist billiger als der alte Plan: Die
nicht-blockierende Tastenabfrage liest ohnehin jede Taste pro Tick,
ein Kauf ist ein weiterer case mit Gold-Prüfung, die eigene
Shop-Szene entfällt komplett.
Verworfen: der Upgrade-Screen als eigene Szene zwischen den Leveln
(eine Szene mehr ohne Spielgefühl-Gewinn); Kauf nur zwischen den
Wellen (der Live-Reiz wäre weg).
**Fortgeführt am 2026-09-28:** Wirkungen, Startwerte und die
[4]-Sperre bis M5 stehen (Eintrag „Gold, Preise und
Kauf-Wirkungen"), die Feuerrate hat ihre Mechanik (Eintrag
„Feuerrate: Sperre in Ticks").

## 2026-09-20 — Lane-Progression 2/3/4 an den Boss-Siegen
Was: Gestartet wird mit 2 Lanes; der Boss-Sieg von Level 5 öffnet
die dritte, der von Level 10 die vierte — testweise, Feinjustierung
nach dem ersten Spielgefühl. Löst ab: „alle drei Level kommt eine
Lane dazu (Start: eine, Maximum: vier)" aus dem Umschwenk-Eintrag.
Warum: Isors Entscheid vom 2026-09-20 — eine einzelne Start-Lane
hätte kein Lane-Wechsel-Gameplay, und die Öffnung am Boss-Sieg macht
den Sieg zum sichtbaren Meilenstein. Schnittlinie gleich mitbenannt:
Wird die Zeit knapp, bleibt es bei 3 Lanes — mit fester
Korridor-Geometrie ist das ein Tabellenwert, keine Logikänderung.
Verworfen: Start mit 1 Lane (nichts zu wechseln); der feste
Drei-Level-Takt (entkoppelt vom Boss-Erlebnis).

## 2026-09-20 — Sprung-Modell: Die Position ist der Lane-Index
Was: Der Spieler steht immer auf der festen Mittelposition unter
genau einer Lane; A/D und ←/→ springen eine Lane weiter, am Rand
wird geklemmt (kein Umlauf). Bei 3 offenen Lanes gibt es exakt
3 Positionen — gespeichert wird nur der Lane-Index, gezeichnet wird
an dessen Mittelspalten.
Warum: Isors eigener Entwurf samt Begründung vom 2026-09-20: keine
Zwischenzustände, nichts kann überdruckt werden, deutlich simpler zu
programmieren. Klemmen statt Umlauf, weil ein Fehlsprung quer übers
Feld hier Leben kostet — anders als im Menü, wo der Umlauf richtig
war.
Verworfen: Gleiten über die Lücke (Zwischenpositionen plus eine
Regel fürs Schießen unterwegs); Umlauf wie im Hauptmenü.

## 2026-09-20 — Spieler-Sprite: T-Form massiv, Lauf 2, Sockel 6
Was: Isors T-Form vom 13.09. wird gebaut als Lauf von 2 Spalten auf
der Korridor-Mitte (Zeile 23) über einem Sockel von 6 Spalten
(Zeile 24), beides massiv aus `█`, gefärbt in Gelb nach der
Farbsprache („Gelb heißt: hier bist du"). Der Schuss startet aus der
Lauf-Spalte.
Warum: Proportionen wie die Skizze (breiter Sockel, schmaler Lauf),
füllt den 8er-Korridor, ohne ihn zu berühren; nur rasterfest
gemessene Zeichen.
Verworfen: Sockel 4 (wirkt verloren unter dem 8er-Korridor); der
Sockel als Halbblock `▀` (Podest-Optik, Isor wählte massiv).

## 2026-09-20 — Schuss-Symbol: || in Cyan
Was: Der Schuss ist `||` — zwei Pipes, 2 Spalten breit auf der
Korridor-Mitte, cyan (`S_COLOR_CYAN` liegt in Console.h). Gemerkt:
`**` bleibt Kandidat für den Treffer-Blitz der M4-Kollision.
Warum: Ruhiger, eindeutig aufwärts gerichteter Strahl; gewählt aus
den drei rasterfest bestandenen Kandidaten.
Verworfen: `**` als Schuss (wirkt wie ein Einschlag, nicht wie ein
Flug); `!!` (liest sich als Warnmeldung).

## 2026-09-20 — Tastenabfrage-Baustein und Tick-Reihenfolge
Was: Der gelieferte Baustein ist ein Wächter vor dem vorhandenen
ReadKey: `ReadKeyNonBlocking` fragt `_kbhit()` und liefert ohne
wartende Taste sofort das neue `I_KEY_NONE` (−2; −1 ist als
`I_KEY_UNKNOWN` vergeben — „nichts da" ist nicht „unbekannt"). Dazu
`WaitMilliseconds` als Sleep-Kapsel, WinAPI bleibt im .cpp. Die
Tick-Schleife läuft: Eingabe (alle wartenden Tasten, Schleife bis
`I_KEY_NONE`) → Update (bewegen, Kollision, aufräumen) → einmal
zeichnen ab Cursor-Home → `WaitMilliseconds(200)`. Löst endgültig
ab: „Eingabe nur zwischen den Wellen" aus dem Tick-Beschluss vom
2026-09-07 — dessen Fortführungs-Vermerk das bereits ankündigte.
Warum: Der Zwei-Schritt-Code der Pfeiltasten bleibt gefahrlos, weil
beide Bytes zusammen im Puffer liegen — der Wächter macht das
getestete ReadKey nicht-blockierend, statt ein zweites Lese-Muster
zu bauen. Alle Tasten je Tick, weil bei 200 ms und schnellem Tippen
2–3 Tasten pro Tick anfallen — eine pro Tick ließe die Eingabe bis
zu einer halben Sekunde nachziehen.
Verworfen: eine Taste pro Tick (schwammige Eingabe durch Rückstau);
ein eigenes nicht-blockierendes Lese-Muster neben ReadKey (doppelte
Pfeiltasten-Logik).

## 2026-09-27 — Gegner-Hierarchie: Normal, Tank, Boss
Was: Drei Klassen unter der Basis `CEnemy` (Daten: Lane, Zeile,
Leben, Figur; Können: fallen, Treffer nehmen): `CNormalEnemy`
(normales Leben, `♟`) und `CTankEnemy` (hohes Leben, `♜`) setzen nur
Startwerte und werden in M3 gebaut; `CBoss` (`♚`, extrem viel Leben,
belegt eine Lane) ist ab jetzt designt und wird in M5 gebaut. Der
Runner entfällt als Typ: Tempo ist kein Klassen-Merkmal mehr,
sondern ein globaler Level-Wert — als Schrittintervall in Ticks in
der Basis (Kurve füllt M6), das allein der Boss überschreibt. Tank
und Normal laufen gleich schnell. `virtual` zeigt sich am Destruktor
(Pflicht bei `delete` über den Basis-Zeiger) und an diesem
Tempo-Hook.
Warum: Isors Zuschnitt vom 2026-09-27. Die Schnittlinie „nie unter
zwei Gegnertypen" bleibt erfüllt, und das Vererbungs-Pflichtthema
wird stärker: Tank/Runner unterschieden sich nur in Zahlen, der Boss
verhält sich anders. Ohne Typ-Tempo braucht M3 keine Takte je Sorte.
Da 1 Zeile/Tick bereits das Maximum ist, heißt „schneller je Level"
praktisch: langsamer starten (Intervall 3 → 1; 18 Zeilen in 10,8 s
bis 3,6 s, Boss darüber). Die Schach-Metapher passt besser: der
Bauer ist der Normale.
Verworfen: der Runner als eigene Klasse (nur ein weiterer
Zahlenunterschied); eine zusätzliche virtual-Methode je Typ schon in
M3 (künstlich, solange Normal und Tank sich gleich verhalten);
Schach-Klassennamen CPawn/CRook/CKing (koppeln die Logik an die
Anzeige — tauscht man eine Figur, lügt der Klassenname).

## 2026-09-27 — Spawn-Plan: Level-Budget aus der Tabelle
Was: Jedes Level ist ein Budget — eine feste Gesamtzahl Gegner,
davon ein festes Tank-Kontingent; Budget verbraucht und Feld leer
heißt Level geschafft. Die Werte stehen in einer 15-Zeilen-Tabelle
(je Level: Gesamt · Tanks · Spawn-Abstand); M3 baut den Spawner und
nutzt Zeile 1 als Testlevel, Tabelle füllen und Level-Wechsel sind
M6. Gespawnt wird im Tick: fester Abstand-Zähler → Lane würfeln
(oberste Zelle belegt → ein Tick warten) → Typ würfeln (Tank-Chance
= Rest-Tanks ÷ Rest-Budget) → Gegner oben einsetzen. Durchbruch
unten: Gegner verschwindet, 1 Leben ab — mehr nicht. Die Boss-Runde
(jedes 5. Level) bleibt die einzige Ausnahme: Der Boss belegt seine
Lane allein, die übrigen spawnen normal weiter (Bau in M5).
Warum: Isors Budget-Ansatz vom 2026-09-27 (Max-Zahl je Level, dann
nächstes Level), dazu vier Vereinfachungen auf Empfehlung: fester
Abstand statt Zufallsspanne (ein Zähler, ein Tabellenwert); Tabelle
statt Zuwachs-Formel (reproduzierbares Balancing); reiner
Lane-Zufall; Rest-Wahrscheinlichkeit lässt das Kontingent immer
exakt aufgehen, ohne Listen zu mischen.
Verworfen: Zufallsspanne beim Spawn-Abstand; „je Level +2 bis +5
zufällig" (jede Balancing-Runde liefe anders); Wiederhol-Sperre bei
der Lane-Wahl (Merk-Zustand ohne echtes Problem bei 2 Lanes); feste
Tank-Positionen wie „jeder vierte Spawn" (vorhersehbares Muster).

## 2026-09-27 — Speicher: Zeiger-Liste, delete an drei Lebensenden
Was: Die GameScene hält die Gegner als `std::vector<CEnemy*>` neben
dem Schuss-Beutel; `new` im Spawn-Schritt, `delete` an den drei
Lebensenden: Durchbruch unten (M3), Tod durch Schuss (M4),
Szenen-Ende mit Aufräum-Schleife vor jedem `return` (M3). Regel:
erst `delete`, dann `erase` — erase wirft nur die Adresse weg, und
die Adresse ist der einzige Zugang zum Objekt. Die Schüsse bleiben
Werte (`vector<CShot>`), sie haben keine Erben.
Warum: Vererbung wirkt nur durch einen Zeiger hindurch — in einer
Werte-Kiste (`vector<CEnemy>`) würde ein `CBoss` beim Einpacken auf
Basisklassen-Maß zurechtgesägt (Slicing) und der Tempo-Override wäre
still weg. Dazu ist laufendes `new`/`delete` das Pflichtthema Memory
Management der Aufgabe. Isors Verständnis-Check bestanden
(delete-vor-erase selbst begründet).
Verworfen: `vector<CEnemy>` mit Werten (Slicing); Smart Pointer wie
`unique_ptr` (über Semesterniveau, und sie automatisierten genau das
Pflichtthema weg, das die Aufgabe sehen will).

## 2026-09-27 — Figuren-Zuordnung final
Was: Normal `♟` · Tank `♜` · Boss `♚`; `♞` bleibt Reserve für den
A1-Ausbau (dritter Gegnertyp). Löst den Favoriten-Vermerk vom
2026-09-13 ein — nur die `♟`-Rolle wandert vom Runner zum Normal.
Warum: Alle vier haben den M1-Zeichentest bestanden; der häufige
Bauer als Normaler, der zähe Turm als Tank, der König als Boss.
Verworfen: die Zuordnung bis zum Bau offenlassen (kein Gewinn — die
Kandidaten stehen seit dem Zeichentest fest).

## 2026-09-28 — Kollision: eine Prüfung, zweimal je Tick
Was: `HandleCollisions` prüft Treffer als „gleiche Lane, gleiche
Zeile" (Beschluss vom 07.09., wörtlich) und wird zweimal je Tick
gerufen — nach dem Gegner-Zug und nach dem Schuss-Zug. Beim Treffer
nimmt der Gegner Schaden in Höhe des Spieler-Schadens (gelesen zur
Trefferzeit, der Schuss trägt kein eigenes Schadensfeld), der Schuss
verschwindet immer; fällt das Leben auf 0, wird Gold gutgeschrieben
und der Gegner mit delete-vor-erase entfernt.
Warum: Isors Kern-Instinkt „im Bewegungs-Moment prüfen",
verallgemeinert gegen die Durchtunnel-Falle: Bewegen sich Schuss und
Gegner im selben Tick aufeinander zu, tauschen sie die Plätze, ohne
je auf derselben Zeile zu stehen — nur die Prüfung nach **jedem**
Bewegungs-Zug fängt beide Richtungen. Schaden zur Trefferzeit, weil
ein Upgrade so sofort auf fliegende Schüsse wirkt und kein neues
Feld braucht.
Verworfen: Look-ahead je Beweger (gleicher Effekt, aber die
Trefferlogik steckt doppelt in zwei Bewegungs-Funktionen); Schaden
als Abschuss-Schnappschuss im Schuss; der Treffer-Blitz `**` jetzt
(Ein-Tick-Anzeigen brauchen Merk-Zustand — bleibt M7-Kandidat);
Schuss-Geschwindigkeit als Upgrade (2 Zeilen je Sprung wäre die
selbstgebaute Tunnel-Falle, und am Schaden je Sekunde ändert das
Flugtempo nichts — Isors eigene Diagnose).

## 2026-09-28 — Feuerrate: Sperre in Ticks, geschluckt statt bestraft
Was: Feuern hat eine Sperre in Ticks — Start 4 (1 Schuss je 0,8 s),
der Kauf `[2]` senkt sie um 1 bis Minimum 1 (5 Schüsse je Sekunde).
Die Leertaste während der Sperre wird still geschluckt: kein Error,
kein Blockier-Gefühl — beim Hämmern feuert die Waffe von selbst im
Takt. Der Sperr-Wert wohnt als Stat in `CPlayer`, der Rest-Zähler in
der Szene — das dritte „alle N Ticks"-Muster nach Schrittintervall
und Spawn-Abstand. Zahlen sind Beispielwerte.
Warum: Isors Spielgefühl-Einwand („nur manchmal drücken dürfen fühlt
sich komisch an") trifft nur bestrafte Cooldowns — stilles Schlucken
ist das Arcade-Muster: Die Sperre fühlt sich als Feuerrate an, nicht
als Verbot.
Verworfen: Schuss-Geschwindigkeit statt Feuerrate (Isors erste Idee,
von ihm selbst angezweifelt — Begründung im Kollisions-Eintrag);
Error-Sound beim Drücken in der Sperre (bestraft Normalverhalten).

## 2026-09-28 — Gold, Preise und Kauf-Wirkungen
Was: Gold wohnt in `CPlayer` (Start 0), die Belohnung je Typ als
drittes Startwert-Feld im `CEnemy`-Konstruktor neben Leben und
Figur — Bauer 20 G, Turm 50 G (Level 1 bringt 130 G).
Start-Schaden 1 (Bauer stirbt an 1 Treffer, Turm an 2). Käufe
jederzeit per Zifferntaste im Eingabe-Drain: [1] Damage 100 G →
Schaden +1 · [2] Atk Speed 120 G → Sperre −1 · [3] Life 500 G →
+1 Leben (ruft das wartende AddLife) · zu wenig Gold → Error-Sound.
[4] Multishot bleibt bis M5 gesperrt — Error-Sound, kein Kauf.
Warum: Belohnung als Konstruktor-Startwert folgt dem „setzt nur
Startwerte"-Muster der Erben; Schaden 1 passt exakt zur
Leben-Staffel 1/2; 130 G Beute je Level gegen 100 G Erstpreis ergibt
das erste Upgrade nach gut einem Level. [4] gesperrt, weil 2000 G
für einen Skill ohne Wirkung ein Geld-Grab wäre.
Verworfen: [4] stumm ignorieren (die Taste wirkte kaputt); die
Zahlen als finale Werte lesen (sie sind Tuning-Masse für M6).

## 2026-09-28 — HUD-Werte vorgezogen nach M4
Was: Die bestehende HUD-Zeile wird schon in M4 live aus den
Spieler-Werten zusammengesetzt (Name, Gold, Schaden, Feuerrate,
Leben) statt aus der statischen Konstante. Das gestaltete HUD
(Balken, Layout, Level-Anzeige) bleibt M6.
Warum: Ohne sichtbares Gold wäre der Live-Shop bis M6 nur im
Debugger testbar; der Vorzug kostet fast nichts, weil
`BuildBoxTextLine` beliebigen Text längst zentriert.
Verworfen: das HUD komplett erst in M6 (blinder Shop); ein eigenes
Zwischen-HUD-Design (doppelte Arbeit für einen Übergang).

## 2026-09-29 — Kauf-Kette: ein Try, die billigen Fragen zuerst
Was: Gold-Prüfung und -Abzug stecken zusammen in `TryRemoveGold` —
das bool sagt, ob der Kauf klappte, der Aufrufer spielt danach
Wirkung oder Error-Sound. Je Kauf-Kette gibt es genau ein Try (das,
das Geld bewegt); alle billigen Fragen stehen davor: Der [2]-Kauf
fragt erst „schon am Minimum?" und wird dort **abgelehnt**, statt
Gold ohne Wirkung zu schlucken. `ReduceFireInterval` bleibt void mit
Klemme bei `I_MIN_FIRE_INTERVAL_TICKS`.
Warum: Isors eigene Idee (Try-Muster, aus C#-TryParse bekannt) — die
Prüfung wohnt an der einen Stelle, an der das Gold wohnt, kein
Aufrufer kann sie vergessen. Ein zweites Try nach dem Abzug müsste
bei Fehlschlag Gold zurückbuchen, und Rückbuchen ist die Fehlerquelle.
Verworfen: GetGold-Prüfung in der Szene (Claudes erster Vorschlag —
vergessbar, Wissen doppelt); `TryReduceFireInterval`
(Rückbuchungs-Falle); ein Kauf am Minimum, der Geld schluckt (sähe
für den Spieler wie ein Bug aus).

## 2026-09-29 — Shop-Feedback: Kauf-Sound und Stufen-Anzeige
Was: Jeder gelungene Kauf spielt `PlayPurchaseSound` — zwei steigende
Töne, das Gegenstück zum fallenden Error-Sound. Die HUD-Zeile zeigt
AtkSpeed als Stufe, die hochzählt (Startwert − Intervall + 1: Start
Stufe 1, Vollausbau 4); intern bleibt die Sperre unverändert ein
Tick-Intervall.
Warum: Beide Befunde von Isor am laufenden Spiel — Käufe ohne
Feedback fühlen sich nach nichts an, und eine Zahl, die beim
Schneller-Werden sinkt, erzählt dem Spieler das Falsche. Übersetzt
wird in der Anzeige, nicht in der Mechanik: Die Sperre ist das
dritte „alle N Ticks"-Muster und bleibt es.
Verworfen: MenuConfirm als Kauf-Sound (verwischt die Bedeutung);
Schüsse pro Sekunde im HUD (Kommazahlen in der Konsole); internes
Umdrehen auf einen Speed-Wert (Umbau an Stat, Klemme und Sperre für
reine Anzeige-Kosmetik).
