# DECISIONS.md — Entscheidungen Harness

Ownership: Nur Entscheidungen zum Harness — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.
Gilt eine Begründung weiter und ist nur ihre Ausführung überholt, bleibt
der Eintrag stehen und bekommt eine Zeile **Fortgeführt am `<Datum>`**
mit Zeiger auf die geltende Fassung — dann geht die Herleitung nicht ins
Archiv verloren.


## 2026-07-16 — Brainstorm-Modus normal/uni
Was: Jede Brainstorm-Session startet mit der Modus-Abfrage normal oder uni.
Warum: Uni-Modus braucht eigene Regeln — erklären statt bauen, visuell,
Verständnis-Checks, Knowledge-Pflicht.
Verworfen: ein Einheitsmodus für alle Brainstorm-Sessions.
**Fortgeführt am 2026-08-22:** Der Modus heißt jetzt **Lernmodus** und
gilt für **alle** Session-Typen, nicht nur fürs Brainstorming; dazu zwei
einzeln verstellbare Regler. Geltende Fassung: `Kern/WORKFLOW.md`.

## 2026-07-17 — Knowledge als externer Ordner
Was: Wissensarchiv als Ordner `C:\Repos Isor\Knowledge\` mit
Themen-Unterordnern, eine .md pro Konzept, Offline-Kopien der
Artifact-Seiten unter Seiten/.
Warum: Wissen ist projektübergreifend und überlebt das Projekt; eine
einzelne Datei wäre unübersichtlich gewachsen.
Verworfen: einzelne KNOWLEDGE.md im Projekt als Puffer mit Auslagerung.

## 2026-07-17 — CODE_GUIDELINES: Zwei Blöcke + Projekt-Typ
Was: Block 1 = Uni-Pflicht (Stil/Naming), Block 2 = eigene Architektur-
Regeln; `Projekt-Typ: Uni/Privat` im Dateikopf entscheidet den
Konfliktfall, einmalig beim Projekt-Setup gesetzt.
Warum: Uni-Regeln sind Pflicht, sollen aber nach dem Studium sauber
entfernbar sein; Projekt-Typ ändert sich nie mitten im Projekt.
Verworfen: Session-Abfrage des Typs durch den Harness; ein gemischter
Regelblock ohne Herkunfts-Markierung.
**Fortgeführt am 2026-08-22:** Die Zwei-Block-Struktur gilt unverändert.
Abgelöst ist nur die Kopfzeile `Projekt-Typ:` — der Konfliktfall
entscheidet sich heute daran, ob ein Ordner `Uni/` vorhanden ist
(Eintrag „Projekt-Typ wird aus der Schicht abgeleitet", unten).

## 2026-07-17 — Felder: [SerializeField] private statt public
Was: Default `[SerializeField] private`, `_camelCase` überall; public nur
bewusst und dann als Property.
Warum: Inspector-Wiring funktioniert identisch, Compiler schützt vor
Fremdzugriff; Dozenten-public diente nur der Bequemlichkeit seines
Editor-Setup-Scripts. Deckt sich mit Uni-Regel (Member private/protected).
Verworfen: Dozenten-Default „public fürs Wiring"; sein Underscore-Verbot.

## 2026-07-17 — Dozenten-Patterns als Werkzeugkasten, nicht Pflicht
Was: MVP als Default-Denkmodell (mit Pragmatik-Ausnahmen); SO-Identität,
Event-Channels, RuntimeReference nur bei passender Problemform.
Review-Gate übernommen (angepasst: Isor tippt selbst, Claude prüft mit);
ClaudeSetup zurückgestellt.
Warum: Entspricht den Einsatzkriterien des Dozenten selbst; Isor ist in
der Lernphase und will selbst schreiben, um besser zu werden.
Verworfen: Patterns als Pflicht für jedes System; ClaudeSetup jetzt schon.

## 2026-07-17 — Session-Ende-Rituale erweitert
Was: Knowledge-Abfrage in jeder Session (Uni-Modus: Pflicht);
Commit-Vorschlag durch Claude (Titel `Update V <nächste Nummer>` +
Description), Isor committet selbst; TDD_NOTES.md als Stoffsammlung
fürs Uni-TDD — nur echte Uni-Projekt-Arbeit, keine Harness-Arbeit.
Warum: Erkenntnisse und Commit-Historie gingen sonst beim /clear
verloren; Isor will Commit-Texte nicht selbst formulieren; das TDD ist
Uni-Abgabe (ca. 2026-07-28) und braucht laufendes Rohmaterial.
Verworfen: Knowledge-Abfrage nur im Uni-Modus; Commits durch Claude.
**Fortgeführt am 2026-08-22:** Die Doku-Pflicht hängt jetzt am Typ des
Abschnitts und wird von den Befehlen `/sichern`, `/wechsel` und `/ende`
ausgeführt. Geltende Fassung: `Kern/WORKFLOW.md`.

## 2026-07-17 — Minimalistisch zur Einsatzreife
Was: Alle vier Session-Typen nur minimal definiert; ausgearbeitet wird
erst, wenn der Praxisbetrieb es verlangt. Regel-Dateien beschreiben nur
den Ist-Zustand, Begründungen gehören hierher.
Warum: Uni-Projekt startet 2026-07-18 — funktionstüchtig schlägt
vollständig.
Verworfen: volle Ausarbeitung aller Dokumente vor Praxisstart
(alte Roadmap-Reihenfolge).

## 2026-07-18 — Reine statische Utilities erlaubt
Was: MeshBuilder und HeightmapGenerator sind statische Klassen — die
Regel „Keine Singletons/Statics" meint zustandsbehaftete Statics.
Warum: Beide sind reine Funktionen ohne Zustand (Daten rein, Daten raus,
testbar); eine Instanz hätte keinen Mehrwert.
Verworfen: Instanz-Klassen hinter Interface (kein zweiter Use-Case — YAGNI).

## 2026-07-18 — Wertebereiche an der Eingabe statt Laufzeit-Checks
Was: Ungültige Parameter (resolution < 2, noiseScale 0, octaves 0,
lacunarity < 1) verhindern [Min]/[Range] im Inspector; der Generator
prüft nicht selbst. Jedes Feld bekommt zudem einen sinnvollen Default.
Warum: Der falsche Wert soll gar nicht erst entstehen (gleiche Denke wie
int statt Vector2Int); fast alle Grenzen schützen vor Division durch
null. Defaults nötig, weil [Min] still gespeicherte Werte nicht korrigiert.
Verworfen: Guard-Klauseln/Exceptions im Generator.

## 2026-07-19 — Asset-Ordner: Kategorie + FolderTemplate, Shared nur bei mehreren Abnehmern
Was: Bausteine liegen unter `Entities/`, `Environment/` oder `Systems/`
je in eigenem Ordner mit Template-Unterordnern (nur die benötigten);
`Shared/` nur für Querschnitts-Utilities mit mehreren Abnehmern. Regeln
in CODE_GUIDELINES (Ordnerstruktur); Terrain-Pipeline entsprechend nach
`Systems/TerrainGenerator` umgezogen.
Warum: `Shared/MeshBuilder` war zum Feature-Ordner gewachsen — falsches
Etikett; Isors Template-System existierte schon und funktioniert.
Verworfen: alte Guideline-Zeile `Assets/Scripts/{System}/`; MeshBuilder
in Shared lassen (nur ein Abnehmer — Zusammenhalten schlägt
spekulatives Teilen).
**Überholt seit 2026-08-20** („Assets nach Typ statt nach Thema", unten).
Weder `Entities/`, `Environment/`, `Systems/` noch `Shared/` existieren
noch. Geltende Fassung: `Kern/CODE_GUIDELINES.md`, Abschnitt
„Ordnerstruktur — Assets nach Typ".

## 2026-07-19 — Session-Typen: Brainstorm+Design ein Typ, 1:1-Regel
Was: „Brainstorm/Design" ersetzt die zwei getrennten Typen; pro Baustein
gilt: erst eine Brainstorm/Design-Session (was & wie), dann eine
Development-Session (nur Umsetzung). Eine Design-Session darf mehrere
Bausteine vorentscheiden.
Warum: Design ohne Brainstorm-Anteil kam in der Praxis nie vor; die feste
Reihenfolge gibt Isor einen klaren Schnitt zwischen Entscheiden und Bauen.
Verworfen: vier getrennte Typen; freies Mischen von Design und Umsetzung
in einer Session.

## 2026-07-23 — Kommentar-Konventionen geschärft
Was: XML-Docs mehrzeilig (IDE-Standard, auch Properties); Inline-Kommentare
Default = keiner, sonst einzeilig und Warum-only; Debug-Ausgaben in
`#if UNITY_EDITOR`; Felder ohne `<summary>` (serialisiert → `[Tooltip]`).
Festgehalten in CODE_GUIDELINES.
Warum: benotete Abgabe — geschwätzige/AI-riechende Kommentare sind ein Risiko;
Dozenten-Regel „keine Debug-Logs im Build"; das Warum lebt in DECISIONS/Header,
nicht inline. Aus Isors Praxis-Feedback in Session 2026-07-23.
Verworfen: einzeilige XML-Summaries; der „2–3 Zeilen erlaubt"-Inline-Zusatz
(führte zu Über-Kommentierung).

## 2026-07-29 — GDD als Maßstab, Short-GDD-Ansatz
Was: GDD.md wird als Short GDD angelegt (ein Bildschirm, wächst mit) und ist
der Maßstab, an dem Roadmap und bestehende Entscheidungen geprüft werden.
„Offen" ist ein ausdrücklich gültiger Eintrag. Der Umbau des Bestehenden
Richtung GDD beginnt erst **nach** der Uni-Abgabe (Portfolio 2026-08-21);
bis dahin ändert das GDD an der Uni-Arbeit nichts.
Warum: Die Systeme, die jetzt entstehen, sollen die Basis für kommende
Semester sein — ohne festgehaltene Design-Absicht werden Architektur-
Entscheidungen geraten statt begründet. Ein volles GDD hätte die Zeit bis
zur Abgabe gekostet, ohne dort einen Beitrag zu leisten. Offene Fragen sind
die wertvollste Information: Jede markiert eine Stelle, an der die
Architektur eine Tür offen halten muss; jede beantwortete Frage erlaubt es,
eine Tür zu schließen und einfacher zu bauen.
Verworfen: vollständiges GDD vor der Abgabe; ganz ohne GDD weiterbauen;
das Bestehende sofort am GDD ausrichten (gefährdet die Abgabe).

## 2026-07-29 — Geltungsbereiche dreier Entscheidungen präzisiert
Was: Drei bestehende Einträge sind pauschaler formuliert als gemeint; ihre
Grenze wird benannt, der Inhalt bleibt unverändert.
(1) „Terrain-Mesh komplett im Code" (2026-07-18) gilt für **generierte**
Gebiete — die Tower-Floors. Das Village wird laut GDD ein festes Grundmesh,
prozedural ist dort nur die Objekt-Platzierung darauf.
(2) „Terrain-Tool als MVP mit EditorWindow" (2026-07-18) beschreibt den
Uni-Stand: Die Pipeline wird ausschließlich aus dem Editor aufgerufen. Laut
GDD entsteht ein Floor beim Portal-Eintritt, also zur Laufzeit — die
Pipeline-Stufen brauchen später einen zweiten Aufrufer. Das Tool bleibt der
Editor-Aufrufer für Vorschau und Preset-Tuning.
(3) „Projekt-Typ Uni/Privat … ändert sich nie mitten im Projekt"
(2026-07-17) trifft nicht zu: Isor's Tower ist der Uni-Prototyp, der nach
dem Studium als privates Release-Projekt weiterläuft. Der Typ wechselt genau
einmal, zum Studienende — das ist der geplante Ablauf, kein Sonderfall, und
genau der Moment, in dem Block 1 (Uni-Pflichtregeln) entfernt wird.
Warum: Pauschale Formulierungen werden später als Verbot gelesen und führen
zu Umbauten, die nie nötig waren. Keine der drei Korrekturen verlangt eine
Code-Änderung vor der Abgabe.
Verworfen: die Einträge umschreiben (Historie ginge verloren); sie
unverändert stehen lassen (führen später in die Irre).

## 2026-07-30 — Prompt-Aktualisierung: Vergleich auf den Prompt erweitern
Was: `PlayerInteractor.UpdateTarget` vergleicht künftig Ziel **und**
Prompt-Text; nur wenn beides unverändert ist, bricht es ab.
Warum: Objekte mit wechselndem Prompt bleiben sonst auf dem alten Text
stehen — die Fackel brennt, angezeigt wird weiter „Light torch", weil
`ReferenceEquals` dasselbe Objekt sieht. „Ziel gleich" ist eben nicht
dasselbe wie „Anzeige aktuell". Der erweiterte Vergleich kostet einen
Property-Aufruf und einen String-Vergleich pro Frame und deckt auch
Änderungen ab, die der Spieler gar nicht ausgelöst hat (Fackel geht bei
Sonnenaufgang von selbst aus).
Verworfen: `_currentTarget = null` nach `Interact` (deckt nur selbst
ausgelöste Änderungen ab); ein Änderungs-Event im `IInteractable` (bläht den
Vertrag für jeden Implementierer auf).

## 2026-08-03 — SO als Startwert, Inspector-Feld als Wahrheit
Was: Serialisierte Felder werden in `Awake` einmalig aus dem ScriptableObject
gefüllt; alle Lesestellen greifen danach auf das Feld zu, nicht aufs SO.
Betrifft `Sheep._type`, `SheepSense` (Radien, Layer, Farben, `_useLocalOverrides`)
und `SheepMoveBehaviour` (Speed-/Flee-Werte).
Warum: `Awake` läuft einmal — dadurch lässt sich im laufenden Play Mode am
einzelnen Objekt tunen, ohne das SO für alle Schafe zu ändern, und der Inspector
zeigt beim Start die effektiven Werte als Ausgangspunkt. Verloren geht nur, was
vor dem Play-Start eingetragen wurde; das ist der bewusste Preis.
Verworfen: direkt aus dem SO lesen (kein Einzelobjekt-Test möglich); das Feld gar
nicht füllen (Inspector zeigt dann nicht, womit das Objekt wirklich arbeitet).

## 2026-08-03 — Konstanten SCREAMING_SNAKE statt PascalCase
Was: Konstanten heißen `MAX_TRIES`, `WALK_STOP_DISTANCE` — bewusste Abweichung
von Block-1-Regel 5 (PascalCase für Konstanten), vermerkt in CODE_GUIDELINES.
Warum: Der Code war darin schon durchgängig konsistent (`MAX_TRIES`,
`UPDATE_TIME`), und die Schreibweise trennt Konstanten im Lesefluss sofort von
Properties, die ebenfalls PascalCase tragen. Ein dokumentiertes Abweichen ist
bei einer benoteten Abgabe stärker als eine Regel, der der Code nicht folgt.
Verworfen: sechs bestehende Stellen auf PascalCase umstellen (Aufwand ohne
Lesbarkeitsgewinn); die Abweichung gar nicht dokumentieren (Guideline und Code
würden auseinanderlaufen).

## 2026-08-06 — UML-Diagramme werden erzeugt statt gezeichnet
Was: Die Diagramme fürs TDD entstehen per Skript als fertige `.drawio`-Datei.
Werkzeuge unter `C:\IsorBackup\05_Werkzeuge\Vorlagen\`: `uml_drawio.py`
(Klassenkästen + UML-Linienstile), `diagramm_<name>.py` je Diagramm,
`pruefer.py` (vergleicht das Ergebnis gegen den Quellcode). Claude bedient die
Skripte, Isor ordnet einmal an; `positionen_lesen()` übernimmt seine Anordnung
bei jeder Neuerzeugung. Erstes erzeugtes Diagramm: Sheep-Komponentensystem,
17 Klassen, 18 Beziehungen, Prüfer meldet null Abweichungen.
Warum: Die alten Diagramme sind veraltet, weil Aktualisieren zu teuer war —
alles von Hand, bei jeder Code-Änderung neu. Die Aufteilung folgt den Stärken:
Die Maschine übernimmt Korrektheit (Namen direkt aus dem Code, Linienarten,
Vollständigkeit), Isor die Optik. Genau die Korrektheit war das Problem
(zwei falsche `HerdManager`-Methodennamen fielen erst beim Testlauf auf), die
Optik nie. Der Prüfer ersetzt das Gegenlesen aller Member durch einen Bericht
von wenigen Zeilen.
Verworfen: Mermaid als Zwischenformat (draw.io importiert es, macht aber aus der
gefüllten Kompositionsraute eine hohle Aggregation — die Bedeutung ändert sich
still); automatische Anordnung (schweres Graph-Problem, Ergebnis wäre schlechter
als 10–15 Minuten Schieben); Diagramme weiter von Hand zeichnen (der Zustand,
der zu den veralteten Diagrammen geführt hat).

## 2026-08-08 — Unity-Ordner folgen den Uni-Systemgrenzen
Was: `Systems/TerrainGenerator/` ist in vier Systeme aufgeteilt — `WorldGeneration/`,
`ObjectPlacement/`, `GrassRendering/` und `TerrainTool/Editor/`. 26 Skripte plus
6 Assets verschoben, keine Code-Änderung nötig.
Warum: Das TDD-Kapitel beschreibt die Architektur, und die Beschreibung soll zur
endgültigen Ablage passen statt zu einer, die kurz danach umgebaut wird. Der Umzug
war zudem kostenlos: Keine der Dateien hat einen `namespace`, es gibt kein `.asmdef`
— nichts konnte brechen. Zieht ROADMAP-Punkt 8 (Gras herauslösen) mit vor.
Verworfen: Threading als eigener Ordner (die Parallelisierung sitzt in `ObjectPlacer`
und `GrassCellBuilder`, also quer über zwei Systeme — ein eigener Ordner hätte sie
auseinandergerissen); Umbau erst nach der Abgabe.
**Fortgeführt am 2026-08-22:** Die vier Systeme gibt es weiter — als
`Scripts/WorldGeneration/`, `Scripts/ObjectPlacement/`, `Scripts/Grass/`
und `Assets/Editor/`. Überholt ist nur die Verschachtelung unter
`Systems/TerrainGenerator/`, seit der Umstellung vom 2026-08-20.

## 2026-08-08 — Diagramm-Werkzeug hält die Handarbeit über Neuerzeugungen
Was: `positionen_lesen` ordnet über den **Klassennamen** zu statt über die Id; neu
sind `kanten_lesen`/`kanten_wiederherstellen` für Linien-Wegpunkte, Andockpunkte und
die Lage der Multiplizitäts-Beschriftungen. Andockpunkte an Member-Zeilen werden auf
den Kasten umgerechnet. Linienstärke zentral als `LINIENSTAERKE = 2`.
Warum: Vier Verlustwege sind im Praxisbetrieb aufgefallen — draw.io vergibt beim
Kopieren neue Ids; es dockt gezogene Enden an einzelne Member-Zeilen an; es lässt
eine Koordinate von 0 weg; und Wegpunkte hielt das Werkzeug gar nicht. Jeder davon
hätte eine Stunde Anordnung lautlos gekostet. Geprüft: zweiter Lauf erzeugt alle
sieben Dateien byte-identisch.
Verworfen: Andockwerte auf 0–1 begrenzen (draw.io lässt sie bewusst überstehen, das
Begrenzen zog Linienenden auf die Kante zurück); Eintrittspunkte automatisch
verteilen (hätte die bereits von Hand angeordneten Kanten verrückt — bleibt als
Kommentar für künftige Diagramme stehen).

## 2026-08-09 — Ablaufpläne über dieselbe Werkzeugkette wie die Klassendiagramme
Was: Sechs Sinnbilder nach DIN 66001 in `uml_drawio.py` (`knoten`/`pfeil`), ein
Skript `ablauf_generate_complete.py` je Plan, Ablage und Bedienregeln unverändert.
Sinnbilder werden über ihre **Id** zugeordnet, nicht über ihren Text.
Warum: Der Text taugt nicht als Schlüssel — „Ende" kommt in einem Plan mehrfach vor,
und bei den Klassendiagrammen ist der Name nur deshalb der richtige Schlüssel, weil
er dort eindeutig ist. Ein zweites Werkzeug wäre die Alternative gewesen; dagegen
sprach, dass Erhalt der Handarbeit, Linienstärke und Datei-Hülle sonst doppelt
gepflegt werden müssten. Nachgewiesen, dass die Klassendiagramme unberührt bleiben:
kein Klassendiagramm hat einen Kasten außerhalb der Swimlanes auf oberster Ebene.
Verworfen: Ein zweiter Plan für das Innere von `SpawnType` — er würde den ersten
verdoppeln; `SpawnType` steht als Unterprogramm-Sinnbild darin. Bei Bedarf
nachziehbar, die Formen sind da.

## 2026-08-11 — Bogensprung an Kreuzungen, und was eine Skript-Vorgabe darf
Was: `jumpStyle=arc` zentral in `uml_drawio.py`, damit sich kreuzende Linien einen
Bogen schlagen. Zweitens: Wo Isor ein Linienende bewusst frei am Kasten gelassen hat,
wird die Andockvorgabe im Skript **entfernt** statt beibehalten.
Warum: Zwei sich kreuzende orthogonale Linien sehen ohne Sprung wie ein T aus — man
sieht nicht, welche wohin führt. Der zweite Punkt ist die wichtigere Lehre: Eine
Vorgabe im Skript wirkt genau dort, wo in der Datei nichts gespeichert ist. Ein frei
gelassenes Ende ist deshalb kein „nichts", sondern eine Entscheidung, die das Skript
respektieren muss. Erkennungsmerkmal: `kanten_lesen` meldet für die Kante keinen
Andockpunkt, obwohl das Skript einen setzt. Fünf Kanten des Zustandsdiagramms waren
betroffen, zwei weitere nach Isors zweiter Überarbeitung.
Nebenbei behoben: `knoten()` schrieb Koordinaten als Ganzzahl und verschob dadurch
Kästen, die auf halben Pixeln sitzen.

## 2026-08-11 — Zeugnis als vierter Session-Typ mit eigener Rules-Datei
Was: „Zeugnis" wird ein Modus im Harness, nicht eine Ausgabeform. WORKFLOW.md führt
ihn als vierten Session-Typ neben Brainstorm/Design, Development und Art; die Regeln
stehen vollständig in ASSESSMENT_RULES.md, die Zeugnisse in ASSESSMENT_LOG.md.
Auslöser ist der Skill `/zeugnis`, der die Rules-Datei lädt statt sie zu doppeln.
Warum: Der erste Entwurf hätte „Zeugnis" als vierten Artifact-Typ in ARTIFACT_RULES
eingehängt. Das war die falsche Ebene — die drei Typen sagen, worauf eine Seite
blickt, ein Zeugnis bewertet dagegen, und der Kern der Sache ist ohnehin die
Session, nicht die Seite. Gleiches Muster wie KNOWLEDGE_RULES und ARTIFACT_RULES:
eigene Datei, kurzer Zeiger von der zuständigen Stelle aus.
Verworfen: vierter Artifact-Typ (falsche Ebene, hätte die Pflegeregel „aktualisieren
statt neu anlegen" stillschweigend gebrochen); alles in WORKFLOW.md unterbringen
(hätte die Datei aufgebläht und die Belegpflicht unauffindbar gemacht); die Regeln
im Skill selbst halten (der Skill liegt außerhalb des Repos und wäre nicht
mitversioniert).
**Fortgeführt am 2026-08-22:** Zwei Angaben des Eintrags sind überholt —
die Zeugnisse liegen nicht mehr in einer Sammeldatei, sondern je Termin
in `Kern/Zeugnisse/<Datum>.md`, und der Auslöser ist kein globaler Skill
mehr, sondern `/harness:zeugnis` unter `.claude\commands\harness\`. Die
Entscheidung selbst — eigener Session-Typ mit eigener Rules-Datei statt
vierter Artifact-Typ — gilt unverändert. Geltende Fassung:
`Kern/ASSESSMENT_RULES.md`.

## 2026-08-11 — Zeugnis-Artifacts behalten je eine eigene URL
Was: Benannte Ausnahme von der Pflegeregel in ARTIFACT_RULES: Ein Zeugnis wird nie
aktualisiert und nie ersetzt, jedes bekommt eine neue URL. Die Ausnahme besitzt
ASSESSMENT_RULES.md; ARTIFACT_RULES verweist nur darauf, geführt werden die Seiten
weiterhin im ARTIFACT_INDEX. Beim Review-Gate werden sie übersprungen.
Warum: Bei Status, System und Lernstück ist der alte Stand wertlos, sobald der neue
existiert — beim Zeugnis ist er der halbe Zweck. Ein Zeugnis ist keine Ansicht auf
einen aktuellen Stand, sondern ein datierter Messpunkt.
Verworfen: eine sammelnde Zeugnis-Seite mit allen Ständen (wäre auf dem Handy
unlesbar geworden und hätte den direkten Vergleich zweier Termine erschwert).

## 2026-08-14 — FolderTemplate um `Audio` ergänzt
Was: `Audio\` ist ein regulärer Baustein-Unterordner neben Scripts,
Prefabs, Textures.
Warum: Klänge gehören zum Baustein (Fackelfeuer zur Fackel, Blöken zum
Schaf); nur Querschnitts-Material liegt in `Shared/Audio/`.
Verworfen: alle Klänge zentral unter `Shared/Audio/`.
**Überholt seit 2026-08-20:** `Audio/` ist heute ein Typordner auf
oberster Ebene, `Shared/Audio/` gibt es nicht mehr. Die Entscheidung
kehrte sich damit um — Klänge liegen jetzt zentral nach Typ, darunter je
ein Ordner pro Wesen. Geltende Fassung: `Kern/CODE_GUIDELINES.md`,
Abschnitt „Ordnerstruktur — Assets nach Typ".

## 2026-08-16 — Versionsschema nach Reifegrad
Was: Die Build-Version (`Player Settings > Version`) folgt dem Reifegrad des
Spiels, nicht dem üblichen Semantic Versioning:

| Form | Bedeutung |
|---|---|
| `0.0.x` | Prototyp — x zählt die Stände hoch |
| `0.x.0` | Early Access |
| `1.x.x` | fertiges Spiel |

Solange die vordere Stelle `0` ist, ist das Spiel nicht fertig; solange die
mittlere `0` ist, ist es nicht einmal Early Access. Stand 2026-08-16: `0.0.2`.
Warum: Isor will an der Versionsnummer den Reifegrad ablesen, nicht die Art
der letzten Änderung. Bei Semantic Versioning stünde die mittlere Stelle für
neue Funktionen und die hintere für Fehlerbehebungen — das sagt nichts
darüber, wie weit das Spiel ist, und genau das ist hier die interessante
Information.
Verworfen: Semantic Versioning (MAJOR.MINOR.PATCH). Aufgefallen war die
Vermischung an `0.1.1`, das nach Isors eigenem Schema bereits Early Access
behauptet hätte.
**Fortgeführt am 2026-08-22:** Die Regel gilt unverändert und steht
ausformuliert in `Kern/VERSIONIERUNG.md`, das sie um die Zeit **nach**
dem Release ergänzt. Der Eintrag war am 2026-08-22 versehentlich als
abgelöst archiviert und ist zurückgeholt worden (Befund A30) — die
Begründung gehört hierher, die Regel dorthin.

## 2026-08-16 — Prompt und Zielzustand getrennt
Was: `IInteractable` bekam neben `InteractionPrompt` eine zweite
Eigenschaft `StatusText`. Der Prompt zeigt nur Taste und Aktion
(`[E] Tame`), der Zustand des Ziels erscheint als eigene Anzeige oben
mittig.
Warum: Ein Interaktions-Prompt beantwortet eine Frage — welche Taste, welche
Aktion (Isor). Beides in einem Textfeld zwang die Box auf 620 Pixel Breite
und ließ den Text umbrechen. Getrennt bleibt der Prompt schmal, und die
Fackel zeigt gar keine Zustandsanzeige, weil sie einen leeren Text liefert.
Verworfen: den Zustand an den Prompt-String anhängen (erste Umsetzung am
selben Tag, wieder zurückgebaut); eine Weltraum-Anzeige über dem Schaf.

## 2026-08-20 — Assets nach Typ statt nach Thema
**Löst ab:** „Asset-Ordner: Kategorie + FolderTemplate" (2026-07-19) und
„FolderTemplate um `Audio` ergänzt" (2026-08-14); präzisiert
„Unity-Ordner folgen den Uni-Systemgrenzen" (2026-08-08).
Was: Der gesamte Assets-Baum wurde von Themenordnern (Entities, Environment,
Systems, Shared) auf Typordner umgestellt (Scripts, Prefabs, Materials,
SO_Settings, Textures, Shader, VFX, FBX, Audio), darunter je ein Ordner pro
System oder Wesen. Editor-Code liegt getrennt in `Assets/Editor/`.
Warum: Vorgabe der Ordnervorlage des Moduls. Isor hat verschoben, ich habe nur
die leeren Ordner vorbereitet und hinterher geprüft — Verschieben gehört in
Unity, sonst reißen die Referenzen.
Bewusst nicht mitgemacht: `ThirdParty/Suriyun` und `TextMesh Pro` blieben
unangetastet. Dort liegen alle FBX, alle Animationen und der einzige
Animator-Controller; die innere Struktur eines gekauften Pakets ist Teil des
Herkunftsnachweises im TDD.
Preis, bewusst gezahlt: Die Systemgrenzen, die am 08.08. durch die Trennung in
vier Systeme sichtbar gemacht wurden, sind im Ordnerbaum nicht mehr zu sehen.
Nachlauf: Die READ_MEs beider Portfolios nannten an fünf Stellen die alten
Pfade zum bewerteten Code (K1, K2, K3, S1, S2, S3). Alle korrigiert und gegen
das Projekt gegengeprüft, bevor neu gezippt wurde.

## 2026-08-21 — Maßstab für den Harness: fünf Grenzen
Was: Der Harness wird auf eine neue Fassung gebracht — besser bedienbar,
stärker automatisiert, weniger Fehler, mehr Möglichkeiten. Zeit ist
**nicht** die Grenze, Gründlichkeit geht vor Tempo. Fünf Grenzen sind
dabei einzuhalten (Isor): nichts kaputtmachen · Zuständigkeiten dürfen
sich nicht überlappen · es darf nicht unübersichtlich werden · es dürfen
nicht zu viele laufende Kosten entstehen · alles, was sinnvoll geht, wird
automatisiert.
Warum: Sie sind der Maßstab, an dem jede spätere Erweiterung gemessen
wird — ohne sie wächst der Harness einfach weiter. Die dritte und die
vierte begrenzen dabei die erste und die fünfte: Struktur und Automatik
haben einen Preis, und der Preis ist Übersicht und Pflegeaufwand.
Verworfen: keine Alternative — es ist die Zielsetzung selbst.
*Nachgetragen am 2026-08-23 aus `_HARNESS_REVIEW.md`, bevor die Datei
archiviert wird (Befund A10). Der Text stand nur dort.*

## 2026-08-22 — Editor-Code liegt zentral in `Assets/Editor/`
**Präzisiert:** „Assets nach Typ statt nach Thema" (2026-08-20), das den
Ordner nur nebenbei nennt.
Was: Editor-Skripte liegen ausschließlich in `Assets/Editor/`, nicht
verstreut in den Systemordnern.
Warum (Isor, 2026-08-22): So ist es seit der Umstellung tatsächlich, und
`CODE_GUIDELINES.md` behauptete zwei Tage lang das Gegenteil („darf im
System-Ordner liegen"). Ein Ordner reicht, weil Unity ohnehin jeden
Ordner namens `Editor` editor-only kompiliert — die Verteilung auf
mehrere brächte nichts als Suchaufwand.
Verworfen: `Editor/` je System (die frühere Guideline-Zeile); beides
erlauben — dann steht in der Regeldatei wieder keine Entscheidung.

## 2026-08-22 — Regeln, die aus der Abnahme kamen
Was: Fünf Schärfungen an bestehenden Regeln, alle aus belegten Befunden
des Schlussdurchgangs (`_HARNESS_ABNAHME.md`).
(1) Eine **Anzahl** in Überschriften ist nur erlaubt, wenn die Aufzählung
abgeschlossen ist und der Text sagt, warum (A4).
(2) Eine **Nummer** darf zitiert werden, wenn sie in der Überschrift des
Ziels steht; nummerierte Listen ohne Überschrift bekommen Kurznamen (A22).
(3) In eine **Chronik** wird nach Datum einsortiert, nicht hinten
angehängt — der Unterschied fällt nur beim Nachtragen auf (A28).
(4) Besitzen mehrere Dateien dieselbe **Art** von Information, gehört ein
Eintrag der Datei, **deren Code er ändert**, und jede trägt eine Zeile
`Nicht hier:` (A29).
(5) `STOERUNGEN.md` führt statt **Behoben** das Feld **Stand** mit `offen`
oder `behoben <Datum>` (A3).
Warum: Jede der fünf hat sich in der Abnahme selbst gezeigt — die
Anzahl-Regel brach sich in der eigenen Überschrift, die Verweisregel
hatte fünf Verstöße in `DIAGRAM_RULES.md`, drei Chroniken waren nach dem
Umzug verdreht, die sieben Projekt-Entscheidungsdateien grenzten sich nur
gegen ROADMAP und LOG ab, und die Zahl der offenen Störungen wurde
dreimal verschieden gezählt.
Verworfen: die Fundstellen einzeln reparieren, ohne die Regel zu ändern —
dann entsteht derselbe Fehler beim nächsten Mal wieder.

## 2026-08-22 — Projekt-Typ wird aus der Schicht abgeleitet
**Löst ab:** den Zusatz „`Projekt-Typ: Uni/Privat` im Dateikopf" aus
„CODE_GUIDELINES: Zwei Blöcke + Projekt-Typ" (2026-07-17). Die
Zwei-Block-Struktur selbst gilt unverändert.
Was: Im Konfliktfall gewinnt Block 1 (Uni-Pflicht), **solange ein Ordner
`Uni/` neben `CODE_GUIDELINES.md` liegt** — sonst Block 2. Die Kopfzeile
`Projekt-Typ:` entfällt ersatzlos.
Warum: Der Typ musste von Hand gesetzt werden. Beim Kopieren des Harness
in ein privates Projekt hätte man daran denken müssen umzustellen;
vergisst man es, gelten dort still die Uni-Regeln — und still falsch ist
der teuerste Fehler. Abgeleitet stellt es sich von selbst richtig, und
die Schicht ist ohnehin die Stelle, an der der Unterschied sitzt: Ohne
Uni-Schicht gibt es keine Uni-Pflicht.
Verworfen: die `Projekt-Typ:`-Zeile beibehalten. Ihre Begründung von
2026-07-17 („ändert sich nie mitten im Projekt") war schon am 2026-07-29
widerlegt — Isor's Tower ist der Uni-Prototyp, der nach dem Studium als
privates Projekt weiterläuft, wechselt den Typ also genau einmal.

## 2026-08-22 — Werkzeuge liegen in der Schicht, deren Dateien sie bearbeiten
Was: `Kern/Werkzeuge/index_bauen.py`, `IsorBackup/Werkzeuge/sichern.ps1`,
`Projekte/Isor_Tower/Werkzeuge/prefab_status.py` — dieselbe Regel wie für
Dokumente. Die Diagramm-Skripte bleiben in `05_Werkzeuge\Vorlagen\`.
Warum: Das INDEX-Skript bearbeitet die Harness-Dateien selbst und muss
deshalb mit der Kern-Auslieferung mitwandern; läge es außerhalb, bekäme ein
neues Projekt den Harness ohne sein wichtigstes Werkzeug.
Verworfen: alle Skripte an einem Ort (`05_Werkzeuge\Vorlagen\`) — einfacher
zu finden, aber das INDEX-Skript wäre nicht mitkopierbar. Ebenso verworfen,
die elf funktionierenden Diagramm-Skripte mit umzuziehen: Ihre Pfade stehen
in DIAGRAM_RULES und in den Skripten selbst, und sie bearbeiten Dateien
außerhalb des Harness.

## 2026-08-22 — Notkern in der obersten CLAUDE.md (Ergebnis von P1)
Was: `Harness Project\CLAUDE.md` behält die Weiterleitung und trägt
zusätzlich vier Regeln als benannte Kopie: Isor entscheidet · nichts in
fremde Dateien · Rückfrage an der Weggabelung · zeigen statt vorstellen
lassen. Dazu Sprache und „Claude committet nicht".
Warum: Prüfung P1, gemessen in einer frischen Session vor dem ersten
Werkzeugaufruf — von den drei `CLAUDE.md` lädt nur die oberste von
selbst. Die im Unity-Root lädt erst beim Zugriff auf eine Datei darunter,
die mit den echten Regeln nie. Ohne Notkern hängt jede Regel daran, dass
dem Verweis gefolgt wird; bei knappem Kontext oder in einem Subagenten
gilt dann gar nichts.
Verworfen: alles so lassen (die Kette hielt im Test, aber aus Gehorsam,
nicht aus Automatik) · die Regeln ganz nach oben ziehen (dann ist
`Claude\` nicht mehr als Ganzes herausnehmbar, gegen die Schichten-Idee).

## 2026-08-22 — Befehle sind Auslöser, ihr Ablauf steht in WORKFLOW
Was: Alle eigenen Befehle liegen in `.claude\commands\harness\` und
heißen dadurch `/harness:sichern`, `:wechsel`, `:ende`, `:sonntag`,
`:zeugnis`. Jede Datei enthält acht Zeilen und zeigt auf
`Kern/WORKFLOW.md` bzw. `Kern/ASSESSMENT_RULES.md`. Der globale Skill
`~\.claude\skills\zeugnis` ist archiviert — er ließe sich nicht in die
Kategorie einordnen.
Warum: Der Projektstamm ist `Harness Project`, das Git-Repo aber
`My Harness Development` — was in `.claude\` liegt, ist nicht versioniert
und ginge nicht mit der Auslieferung mit. So steht alles Inhaltliche im
Repo, und ein verlorener Auslöser ist aus WORKFLOW neu geschrieben. Die
Erkennungsregel, weil das `/`-Menü eingebaute, mitgelieferte und eigene
Einträge ununterscheidbar mischt.
Verworfen: voller Ablauftext in den Befehlsdateien (unversioniert und
eine zweite Fassung der Doku-Pflicht) · das Arbeitsverzeichnis auf
`My Harness Development` umziehen (saubere Trennung, ändert aber den
Start-Ordner und die Pfade in allen Skripten).
Preis, bewusst gezahlt: Die Befehle gibt es nur, wenn `Harness Project`
der geöffnete Ordner ist. Sie schreiben ohnehin alle in dieses Repo.
**Fortgeführt am 2026-08-22:** Der Preis war höher als gedacht. Die
Auslöser standen dadurch weder im Repo noch im INDEX noch in der
Auslieferung — ein neues Projekt hätte den Harness ohne seine
Bedienoberfläche bekommen, ohne dass das irgendwo aufgefallen wäre
(Befunde A6 und A19 der Abnahme). Deshalb liegt das **Original** jetzt
in `Kern/Befehle/`, `.claude\commands\harness\` ist die Arbeitskopie,
und das INDEX-Skript führt beide Gruppen samt der zwei Wegweiser-
`CLAUDE.md` in eigenen Abschnitten. Verworfen: die Ausnahme nur zu
benennen — das hätte ausgerechnet die `CLAUDE.md` mit dem Notkern
außerhalb des Registers gelassen. Geltende Fassung: `Kern/WORKFLOW.md`
→ „Wo die Auslöser liegen".

## 2026-08-22 — Berechtigungen: generische Muster mit ask und deny
Was: `.claude\settings.local.json` von 314 Allow-Einträgen auf 51
generische Muster, dazu 8 `ask` (Löschen, Prozesse beenden, robocopy) und
4 `deny` (`git commit`, `git push`).
Warum: Die alten Einträge waren fast alle Einweg-Kommandos mit
Session-GUIDs im Pfad und trafen nie wieder. `ask` und `deny` setzen
zugleich zwei Hausregeln dort durch, wo sie wirken: „niemals löschen, nur
archivieren" und „Claude committet und pusht nicht".
Verworfen: nur `allow` pflegen — dann steht die Commit-Regel weiter
allein im Dokument. Bewusst drin gelassen: `python:*`, faktisch beliebiger
Code, aber ohne sie fragt jeder Werkzeuglauf nach.
Bekannte Lücke: `deny` greift über den Befehlsanfang; `git -C <Pfad>
commit` liefe daran vorbei.

## 2026-08-23 — Die Übergabe an die nächste Session lebt in PLAN.md
Was: Der Auftrag für die nächste Session steht in `PLAN.md`, Abschnitt
„Für die nächste Session", **ganz oben**. Er wird bei jedem
`/harness:ende` **überschrieben**, nie ergänzt — „gerade nichts offen"
ist ein gültiger Inhalt. Die Leseordnung in `CLAUDE.md` nennt ihn
ausdrücklich, und `/harness:ende` bekommt dafür den Schritt „Plan
nachziehen".
Warum: Eine Übergabe muss drei Dinge zugleich können — gelesen werden,
vergehen, und das Archivieren der Baulisten überleben. `PLAN.md` bringt
zwei davon mit: Es steht in der Leseordnung, und es wird nach jedem
Zeitraum ohnehin geleert. Der Anlass ist gemessen: Am 2026-08-23 stand
die Übergabe am Ende von `_HARNESS_UMSETZUNG.md` und wurde von einer
frischen Session nicht gefunden — die Leseordnung endet bei WORKFLOW,
und `PLAN.md` zeigte nicht dorthin (Befund A34).
Verworfen: eine eigene `UEBERGABE.md` — sauberer in der Zuständigkeit,
aber ein fünfter Punkt in der Leseordnung für fünf Zeilen Inhalt, die
meistens „nichts offen" lauten; und das Vergehen hätte neu geregelt
werden müssen. Ebenfalls verworfen: die ROADMAP — sie ist dauerhaft und
wird erst gelesen, wenn an ihrer Schicht gearbeitet wird.
Hingenommen: `PLAN.md` führt damit zwei Zeitmaßstäbe, eine Session und
ein bis drei Wochen. Der Abschnitt steht deshalb abgesetzt oben.

## 2026-08-23 — Fünfter Session-Typ „Prüfung"
Was: Ein Abschnitt, der **liest und bewertet, aber nicht baut**. Ergebnis
ist eine Befundliste. Der **Gegenstand wird beim Wechsel mitgenannt**
(„Prüfung — Gegenstand: der Harness"), der Typname bleibt generisch.
Doku-Pflicht: Befundliste · ROADMAP der geprüften Schicht · `LOG` der
Schicht mit einem Satz · `STOERUNGEN.md`. Kein eigener Auslöser, der
Wechsel genügt. Eine Befundliste ist **immer temporär**, eine Datei je
Durchgang; was überlebt, ist der ROADMAP-Punkt.
Warum: Die vier bisherigen Typen decken den Fall nicht ab. Gemessen am
2026-08-23: Für den Prüfauftrag aus der Übergabe schlug Claude
„Development" vor, Isor widersprach — es wird nichts gebaut —, und es gab
keine passende Antwort. Auch die Abnahme (Phase 8) lief ohne Typ. Der
Fall wiederholt sich absehbar: Testphase auf `C:\IsorBackup`,
Prefab-Prüfstand, Sonntagsabgleich (Befund A40).
Verworfen: der Name „Harness-Prüfung" — der Kern wandert in jedes Projekt
mit, und drei der nächsten Prüfungen haben einen anderen Gegenstand als
den Harness. Ebenfalls verworfen: eine dauerhafte `BEFUNDE.md` je Schicht
(würde zum Friedhof, gegen die Kostenformel in `DOC_RULES.md`); kein
LOG-Eintrag nach Zeugnis-Vorbild (ein Prüfdurchgang **ist** ein Ereignis,
die Abnahme hat zu Recht einen bekommen).
Offen: Woran der Takt einer Prüfung hängt — Pflegetag, Meilenstein oder
beides. Steht als Punkt in `Kern/ROADMAP.md`; der Typ funktioniert
solange auf Zuruf.

## 2026-08-23 — Artifact-Seiten teilen eine Farbwelt
Was: Alle Seiten benutzen dieselbe warme dunkle Palette (Grund `#17130F`,
Pergament `#EFE4D2`, Ember `#D9762B`) und erscheinen **nur in einer
Fassung**, ohne Hell-Modus. Fest sind Palette, Schriftrollen und der
Aufbau; wie viel visualisiert wird, entscheidet der Inhalt. Der
Altbestand wird beim nächsten inhaltlichen Anfassen mitgezogen, nicht
eigens. Ausformuliert in `Kern/ARTIFACT_RULES.md`, Abschnitt „Gestaltung".
Warum: Die Sammlung hatte zwei Looks — eine kühle helle Sorte (System und
Lernstücke, 06./08.08.) und eine warme dunkle, die für die
UI-Mockup-Seite entstand. Isor erkannte die zweite als deutlich
lebendiger; ohne festgeschriebene Werte wäre sie bei jeder neuen Seite
neu zu erfinden. Eine Familie entsteht über die Palette, nicht über
Einzelentscheidungen.
Verworfen: die kühle helle Fassung als Standard (acht Seiten sähen schon
so aus, gefällt aber weniger); zwei Looks je nach Typ (die Sammlung
bliebe zweigeteilt, und jede neue Seite bräuchte wieder eine
Entscheidung); alle elf Seiten in einem Durchgang nachziehen (ein
Arbeitstag für Optik, während die Inhalte ohnehin überholt sind).

## 2026-08-23 — Das Backup fällt aus dem Pflegetag heraus
Was: Die Sicherung auf die externe Platte ist **kein Punkt des
Pflegetags** mehr. Das Skript `IsorBackup/Werkzeuge/sichern.ps1` bleibt
gebaut und unangetastet; Isor fährt die Sicherung von Hand. Claude
erinnert nicht daran und meldet sie nicht als offenen Punkt. Bedingung
fürs Wiederaufnehmen: Die Testphase ist durch und der Harness hat sich
im laufenden Betrieb bewährt — kein Datum.
Warum: Am Harness steht noch viel Arbeit an, die erst im Betrieb
auffallen wird; die Sicherung trägt zur Funktion des Harness nichts bei
und lässt sich ohne ihn erledigen. Ein Punkt, der bei jedem Pflegetag
„offen" meldet, ohne dass ihn jemand angehen will, wird nach dem dritten
Mal überlesen — und dann fällt auch der Punkt daneben durch. Belegt am
ersten Pflegetag (2026-08-23): Er lief, und genau dieser Punkt blieb als
einziger offen stehen.
Verworfen: als Erinnerung im Pflegetag belassen und einfach nicht
ausführen (erzeugt eine Liste, in der ein Eintrag dauerhaft rot steht);
das Skript löschen (es ist fertig und geprüft, Löschen wäre Verlust —
`niemals löschen, nur archivieren`).

## 2026-08-23 — Eine Auslieferung ist eine Vorlage, keine Kopie
Was: Beim Packen einer Kern-Auslieferung wird entfernt, was unter `Kern/`
liegt, aber nur Isor betrifft — die Zeugnisse, die Einträge im
`ARTIFACT_INDEX.md` und die Zeilen in `index_geplant.txt`. Regel steht in
`Kern/VERSIONIERUNG.md`.
Warum: Aufgefallen beim Packen von `Harness_1.0.0`: Nach dem Buchstaben
der Regel („nur `Kern/`") wären zwei Zeugnisse über Isors Leistungsstand
und seine Artifact-URLs mitgegangen — 1.020 von 3.995 Zeilen, in einem
fremden Projekt wertlos. Dem Sinn nach sagte die Regel schon „keine Uni,
kein Projekt"; sie war nur nicht scharf genug.
Verworfen: alles mitliefern (die gefüllten Dateien als Formatbeispiel —
zu teuer erkauft); ein Zeugnis als Muster behalten (eine Bewertung von
Isors Person geht ein fremdes Projekt nichts an). `LOG.md`,
`DECISIONS.md` und `_ARCHIV.md` bleiben bewusst drin: Sie erklären, warum
die Regeln so aussehen.
