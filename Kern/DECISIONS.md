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
**Fortgeführt am 2026-08-23:** Die **Begründung** oben ist mit dem
Struktur-Umbau weggefallen, die **Entscheidung** nicht. `.claude\` liegt
seit 2.0.0 in der Repo-Wurzel und ist versioniert — „was dort liegt, ist
nicht im Repo" stimmt nicht mehr. Die Doppelung Original/Arbeitskopie
bleibt, jetzt weil Claude Code Befehle ausschließlich in
`.claude\commands\` findet, die Auslieferung aber `Kern/` packt. Auch
der Preis von Zeile 515 ist bezahlt: Der geöffnete Ordner **ist** jetzt
das Repo. Die zwei Wegweiser-`CLAUDE.md` aus dem letzten Absatz gibt es
nicht mehr; der INDEX führt nur noch die Befehle gesondert. Geltende
Fassung unverändert: `Kern/WORKFLOW.md` → „Wo die Auslöser liegen".

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

## 2026-08-23 — Die Testphase beginnt auf Zuruf, nicht nach der Prüfung
Was: Wann der Harness in anderen Räumen (`C:\IsorBackup`, Isor's Tower)
in Betrieb genommen wird, entscheidet **Isor durch Ansage**. Kein Datum,
keine Bedingung, die Claude selbst feststellen könnte. Bis dahin wird am
Harness gearbeitet: prüfen, was nicht trägt, und es verbessern. Claude
meldet die Testphase nicht als fällig. Festgehalten in `PLAN.md`.
Warum: „Nach der Prüfung" klingt nach einem Termin, ist aber keiner — ob
der Harness so weit ist, kann nur Isor beurteilen, und niemand sonst
sieht, wie viel Arbeit er noch will. Aufgefallen am 2026-08-23: Claude
las den alten Plansatz vor, als wäre er noch gültig, obwohl Isor längst
anders entschieden hatte. Gleiche Bauart wie beim Backup (Eintrag oben):
Eine Bedingung, die Claude nicht messen kann, wird zur Ansage.
Verworfen: die Testphase an das Ende der Befund-Behebung hängen (Befunde
werden nachwachsen, solange geprüft wird — das Ende wäre willkürlich);
ein Datum setzen (dasselbe Problem, nur früher sichtbar).

## 2026-08-23 — Der laufende Typ steht in der Klammer des Session-Titels
Was: Der Session-Titel folgt dem Schema `<Thema> (<Typ>)`; der Modus
kommt nur dazu, wenn er vom Lernmodus abweicht. **Das Thema gehört Isor,
die Klammer gehört Claude**, der sie bei jedem `/harness:wechsel`
umschreibt. Der Titel ist **Anzeige, kein Beleg** — er lebt in der App,
nicht im Repo. Ausformuliert in `Kern/WORKFLOW.md`.
Warum (Isor, 2026-08-23): Der Typ entscheidet, was die Doku-Pflicht
schreibt — und stand bis heute an **keiner** Stelle. Weder während der
Session noch hinterher war zu sehen, worin man steckt; wer es wissen
wollte, musste zurückscrollen. Isors Fassung hält den Thementeil stabil
und bewegt nur die Klammer, sodass die Session über den Tag
wiedererkennbar bleibt. Dass Claude den Titel selbst setzen kann, ist
der Grund, warum es trägt: Es hängt nicht an Isors Disziplin, und
Verhaltensregeln, die am Erinnern hängen, sind am selben Tag mehrfach
gerissen.
Verworfen: den Typ in eine Kopfzeile von `PLAN.md` schreiben (die Datei
wird nach jedem Zeitraum geleert, und man müsste sie öffnen, statt zu
sehen); den Titel bei jedem Wechsel komplett neu bauen (dann springt der
Name, und die Session ist in der Liste nicht wiederzuerkennen); den
Modus immer mitschreiben (er wechselt seltener als der Typ und stünde
meist nur im Weg). Hingenommen: Der Titel trägt immer nur den letzten
Abschnitt — die Abfolge steht im LOG.
**Ergänzt am selben Tag (Isor):** Die Klammer trägt außerdem die zwei
Ruhezustände — `zu` nach `/harness:ende` und `aufgehoben` für eine
absichtlich offen gelassene Session. Grund: Eine beendete Session zeigte
sonst weiter einen Typ und behauptete Arbeit, die niemand mehr tut; und
eine geparkte Session (Isor hält eine offen, um Inhalte darin zu
behalten) wäre beim Aufräumen entweder als tot oder als laufend gelesen
worden. Bekannte Grenze: Bei `/clear` kann Claude nichts mehr setzen —
der Handgriff sitzt deshalb in `/harness:ende`, dem letzten Moment davor.

## 2026-08-23 — `pruefen.py` läuft beim Sichern, nicht am Pflegetag
Was: Das Prüfskript wird bei jedem `/harness:sichern` aufgerufen — also
auch bei `/wechsel` und `/ende` — und **meldet nur**, es ändert nichts.
Der Pflegetag bekommt es ausdrücklich **nicht** als zweiten Punkt; dort
bleibt allein die Artifact-Durchsicht.
Warum: Die beiden Sorten Arbeit haben verschiedene Preise. Ein Lauf über
46 Dateien dauert Sekunden, das Abrufen und Gegenlesen der
Artifact-Seiten eine halbe Session. Nur das Teure braucht einen Termin.
Dazu entstehen die Fehler, die das Skript findet — tote Verweise,
Zahlwörter, abweichende Glossar-Zeilen — genau **beim Schreiben**;
wöchentlich zu prüfen hieße, sie bis zu sechs Tage stehen zu lassen. Die
drei falschen Glossar-Zeilen sind in zwei Tagen entstanden.
Verworfen: nur sonntags (Befunde stünden tagelang, und am Sonntag fehlt
der Anlass im Kopf); beides parallel (zwei Betriebsarten, die
auseinanderlaufen); das Skript Triviales selbst reparieren lassen (es
schriebe unbeaufsichtigt in Regeldateien — gegen „Isor baut und
entscheidet").
Gemessen beim Bau: Der erste Lauf meldete **45 Funde, davon rund 40
Fehlalarme** — geplante Dateien, Verweise auf fremde Bäume, ein
Gegenbeispiel im Regeltext, Zeitangaben statt Listenanzahlen. Nach zwei
Runden Schärfung: 4 Funde, davon einer echt. Daraus die Bauregel für
jeden weiteren Prüfer: **Ein Fund, den niemand prüfen kann, ist Rauschen,
und Rauschen macht den Prüfer wertlos** — dieselbe Mechanik, aus der das
Backup aus dem Pflegetag geflogen ist.

## 2026-08-23 — Die Repo-Wurzel bleibt `Harness Project`, nicht `Harness`
Was: Beim Umbau auf 2.0.0 wandert `.git` eine Ebene hoch, sodass
`C:\Repos Isor\Harness Project\` die Wurzel wird. Der kürzere,
sauberere Name `C:\Repos Isor\Harness\` wurde **nicht** genommen.
Warum: Claude Code schlüsselt Session-Historie und Memory am **geöffneten
Ordner**, nicht am Repo. Bleibt der Pfad derselbe, bleiben rund dreißig
Memory-Einträge und die gesamte Session-Historie liegen, wo sie sind —
Handgriff 8 des Bauplans entfällt ersatzlos. Derselbe Grund macht
`.claude\` gratis: Der Ordner lag bereits in `Harness Project\` und war
damit schon auf der Zielebene.
Verworfen: `C:\Repos Isor\Harness\` (kürzester Name, aber neuer
Ordnerschlüssel — Memory und Historie hätten mit umziehen müssen, und
ein Umzug, der beim Aufräumen Erinnerungen kostet, zahlt den falschen
Preis) · die Wurzel bei `My Harness Development\` lassen (dann bliebe
`Harness Project\` eine Hülle mit genau einem Unterordner, und `.claude\`
hätte eine Ebene **runter** gemusst — das Problem wäre verschoben, nicht
gelöst).
Preis, bewusst gezahlt: Der Ordnername `Harness Project` und der
GitHub-Name `My-Harness-Development` laufen auseinander. Das taten sie
vorher schon; das Umbenennen des Remotes ist als eigener Punkt in der
ROADMAP notiert und wird nachgeholt, wenn der Umbau committet ist.

## 2026-08-23 — Der Umbau ist 2.0.0, nicht 1.1.0
Was: Der Struktur-Umbau hebt die Harness-Version auf **2.0.0**.
Warum: Nach `VERSIONIERUNG.md` ändert sich die vordere Stelle, wenn ein
bestehendes Projekt **umziehen muss**. Genau das trifft zu: Die Wurzel
verschiebt sich, der Notkern und die Wegweiser-`CLAUDE.md` entfallen,
und die Auslieferung sieht dadurch anders aus — wer 1.0.0 ausgepackt
hat, kann 2.0.0 nicht darüberkopieren.
Verworfen: `1.1.0` mit dem Argument, die Schichten `Kern/`, `Uni/` und
`Projekte/` blieben unverändert und nur die Ebene darüber ändere sich.
Stimmt für den Inhalt, verfehlt aber die Frage, die diese Nummer
beantwortet — sie misst Verträglichkeit, nicht Umfang.
Folge, noch offen: Nach `VERSIONIERUNG.md` wird bei jeder Änderung von
`X` eine Auslieferung abgelegt. `Harness_2.0.0` steht in der ROADMAP.

## 2026-08-23 — Der Hook feuert auch bei `clear`, nicht nur bei `startup`
Was: Der `SessionStart`-Hook trägt die Auslöser
`startup|resume|clear|compact`. `fork` bleibt draußen.
Warum: Isors Ablauf endet mit `/harness:ende` und dann `/clear`. Das
erzeugt den Auslöser `clear`; `startup` feuert nur beim frischen Öffnen
von Claude Code. Ein Hook allein auf `startup` hätte im tatsächlichen
Arbeitsrhythmus fast nie gegriffen — also genau dort nicht, wofür er
gebaut wurde. `compact` ist dabei, weil beim Zusammenfassen das
Prüfergebnis aus dem Kontext fallen kann.
Verworfen: `fork`. Eine abgezweigte Session erbt den Kontext, das
Ergebnis steht dort schon; ein zweiter Lauf wäre reine Wiederholung.
Verworfen außerdem: ein zweiter Hook auf `.md`-Änderungen (Kandidat 2 des
Bauplans). Bei einem `/harness:sichern` werden fünf bis acht Dateien
nacheinander geschrieben, und die Zwischenstände sind zu Recht
unvollständig — ein Verweis auf eine Datei, die zwei Schritte später
entsteht, wäre ein Fund, der keiner ist. Die Begründung steht schon im
Skript selbst: Rauschen killt den Prüfer.

## 2026-08-23 — Die Hook-Vorlage liegt im Kern, nicht nur im Text
Was: `Kern/Vorlagen/settings.json` ist das Original, `.claude\settings.json`
die Arbeitskopie. Die Auslieferung bekommt einen vierten
Einrichtungs-Handgriff, der kopiert. `pruefen.py` gleicht beide als
**Prüfung 6** ab — je Hook-Eintrag, nicht als ganze Datei.
Warum: Dieselbe Bauart wie bei `Kern/Befehle/`. Ohne Original im Kern
wäre der Hook in einem ausgelieferten Harness weg, denn die Auslieferung
packt `Kern/` und `.claude\` ist Konfiguration des Programms. Und ohne
Prüfung 6 wäre der Hook das einzige Stück des Harness, das seinen eigenen
Ausfall nicht melden kann: Verschwindet er aus der Arbeitskopie, läuft
nichts mehr, und niemand sagt etwas.
Warum je Eintrag statt ganzer Datei: Die Arbeitskopie trägt zusätzlich
`permissions.additionalDirectories` mit einem rechnerabhängigen Pfad. Ein
Gleichheitsvergleich wie bei den Befehlen hätte dauerhaft angeschlagen.
Verworfen: nur ein Handgriff im Text von `VERSIONIERUNG.md`, ohne Datei —
dann wäre der Hook-Block abzutippen, könnte abweichen, und niemand
prüfte es. Verworfen außerdem: gar keine Auslieferung des Hooks — das
hätte die ausgelieferte Fassung dauerhaft schwächer gemacht als das
Original.

## 2026-08-23 — Das Prüfskript kennzeichnet seine Herkunft
Was: `pruefen.py --hook` stellt der Ausgabe die Zeile
`[SessionStart-Hook]` voran. Nur der Hook übergibt diesen Schalter.
Warum: Die Ausgabe sieht identisch aus, gleich ob der Harness sie erzeugt
hat oder Claude das Skript von Hand gestartet hat (Isor, 2026-08-23).
Ohne Kennzeichen ist der Unterschied zwischen Automatik und Erinnerung
nicht nachprüfbar — und dieser Unterschied war der ganze Zweck. Zweiter
Dienst derselben Zeile: Sie sagt der Session, dass der Einstiegslauf
schon stattgefunden hat, damit er nicht wiederholt wird.
Ausdrücklich begrenzt auf den Einstieg: Die Läufe bei `/harness:sichern`
bleiben unberührt. Eine pauschale Formulierung hätte die wichtigere
Prüfebene stillgelegt — die nämlich, die findet, was das Schreiben selbst
kaputt gemacht hat. (Isors Einwand, noch vor der ersten Veröffentlichung
der Zeile.)
Verworfen: Herkunft an einer Umgebungsvariablen erkennen. Ob Claude Code
`CLAUDE_PROJECT_DIR` auch außerhalb von Hooks setzt, ist ungeprüft; ein
eigener Schalter ist eindeutig.

## 2026-08-23 — Erklärskizzen bekommen einen Ort: `Kern/Bilder/`
Was: Von Hand gebaute `.svg`-Skizzen zu Harness-Mechanismen liegen unter
`Kern/Bilder/`, mit einer `README.md`, die den Ordner in den INDEX trägt.
Warum: `DIAGRAM_RULES.md` gilt ausdrücklich nur für die skriptgenerierten
`.drawio`-Dateien, und ein Artifact ist eine Ausgabeform, keine Ablage.
Die erste solche Skizze — das Hook-Bild — lag im Sitzungs-Zwischenspeicher
und wäre mit der Session verschwunden.
Warum eine `README.md` dazu: `index_bauen.py` sammelt nur `.md`-Dateien.
Eine `.svg` oder `.json` erscheint im INDEX weder als Eintrag noch als
Warnung — sie wäre eine Datei außerhalb des Registers, gegen
`DOC_RULES.md` Abschnitt 8. Dieselbe Lösung trägt `Kern/Vorlagen/`.
Verworfen: `index_bauen.py` um eine Nicht-`.md`-Gattung erweitern. Das
Skript bekäme eine zweite Sammellogik samt der Frage, woher die
Beschreibung einer Datei ohne Ownership-Zeile kommen soll; eine
`README.md` je Ordner beantwortet das ohne Code.

## 2026-08-23 — Skizzen wandern nachgezeichnet in Artifact-Seiten, nicht eingebettet
Was: Wandert eine Skizze aus `Kern/Bilder/` in eine Artifact-Seite, wird
sie dort in der Hausfarbwelt und hochkant **neu gezeichnet**. Die Datei
bleibt das Original, die Tafel ist eine zweite Darstellung derselben
Sache. Der Eintrag im `ARTIFACT_INDEX.md` nennt beide.
Warum: Die zwei Formen haben verschiedene Maße, und keine kann beide
bedienen. Eine Artifact-Seite ist die Handy-Fassung — `ARTIFACT_RULES.md`
verlangt hochkant, höchstens 460 px breit und die dunkle Palette. Die
Skizze `hook_sessionstart.svg` ist quer, hell und 980 px breit, weil sie
im Repo, im Browser und in Abgaben gelesen wird. Eingebettet schrumpft
sie auf dem Handy unter die Lesbarkeit ihrer Beschriftung.
Verworfen: **1:1 einbetten** — spart die Doppelung, kostet aber genau
das, wofür die Seite da ist. **Die Skizze selbst hochkant und dunkel
umbauen** — dann passt sie in die Seite und nirgends sonst mehr; ein
helles Querformat ist für Repo und Abgabe die richtige Form.
Preis, offen benannt: zwei Stellen zum Pflegen. Die Richtung dagegen
steht fest und ist dieselbe wie bei `Kern/Befehle/` und `Kern/Vorlagen/` —
geändert wird das Original, danach wird die Seite nachgezogen.

## 2026-08-24 — Pfade bekommen einen Besitzer: `Kern/PFADE.md`
Was: Absolute Pfade stehen nur noch in `Kern/PFADE.md`, als Tabelle mit
Marken (`DATENBAUM`, `KNOWLEDGE`, `PROJEKT`). Regeldateien nennen die
Marke und verweisen dorthin; Chroniken bleiben ausgenommen. Erzwungen
durch Prüfung 7 in `pruefen.py`.
Warum: Beim Packen der Auslieferung 2.0.0 fanden sich absolute Pfade an
sieben Stellen im Kern — jede davon wandert in fremde Projekte mit. Der
laute Fehlerfall (Ordner fehlt) ist harmlos; der stille nicht: Liegen
zwei Harness-Bäume auf demselben Rechner, findet der Pfad eine Datei,
nur die falsche. Das ist der Ownership-Kernsatz, angewandt auf Pfade —
sie waren die letzte Informationsart ohne Besitzer. Idee von Isor
(2026-08-24), als die Alternative war, die Befehlsdateien einzeln zu
flicken.
Verworfen: **Platzhalter in den .md-Dateien** (`{{DATENBAUM}}`) — Markdown
hat keine Variablen; ich müsste beim Lesen an die Ersetzung denken, das
wäre wieder eine Bitte statt einer Tatsache. **Pfade beim Einrichten fest
in die Dateien schreiben** — Massen-Ersetzen ist fehleranfällig (Beleg:
die BOM-Störung vom 2026-08-23), und ein Umzug hieße nochmal ersetzen
statt eine Zeile ändern.

## 2026-08-24 — Einrichten wird ein Befehl, keine Handgriff-Liste
Was: `/harness:einrichten` ersetzt die vier Einrichtungs-Handgriffe aus
`VERSIONIERUNG.md`. Er fragt die Pfade für `Kern/PFADE.md` einzeln ab
und führt dann aus: Befehle in die Arbeitskopie, `PLAN.md` anlegen, Hook
eintragen, INDEX erzeugen, Prüflauf samt `--glossar-ok`. Ablauf in
`WORKFLOW.md`, Auslöser in `Kern/Befehle/`.
Warum: Die Handgriff-Liste ist dreimal gewachsen (zwei Punkte nach dem
Probelauf von 1.0.0, einer mit dem Hook) — eine Liste zum Abarbeiten
wird mit jeder Version länger und unvollständiger. Ein Befehl führt aus
statt zu erinnern; dieselbe Richtung wie beim SessionStart-Hook. Idee
von Isor (2026-08-24).
Verworfen: die Liste behalten und nur um die Pfad-Abfrage ergänzen —
fünf Handgriffe von Hand sind nicht besser als vier.

## 2026-08-24 — Die Packliste steht in VERSIONIERUNG.md, nicht im Ermessen
Was: Welche Datei beim Packen einer Auslieferung vollständig bleibt,
geleert wird oder wegfällt, steht als Tabelle in `VERSIONIERUNG.md` →
„Die Packliste". Eine neue Kern-Datei wird beim Anlegen einer der drei
Zeilen zugeordnet.
Warum: Die Frage stellte sich beim Packen von 2.0.0 zum zweiten Mal
(ROADMAP voll mitgeben oder leeren?), und zweimal verschieden zu
antworten wäre schlimmer als jede der Antworten. Isors Einwand
(2026-08-24): Das darf nicht jedes Mal neu gefragt werden. Entschieden:
ROADMAP bleibt vollständig — sie zeigt an echten Einträgen, wie eine
geführt wird; `PFADE.md` wird auf `(nicht eingerichtet)` geleert.
Verworfen: je Auslieferung neu entscheiden (genau der Zustand, der die
Regel nötig machte) · eine Muster-ROADMAP mit erfundenem Beispieleintrag
(erfundene Einträge altern schlechter als echte).

## 2026-08-24 — Die Seite „Grundgerüst" wird in zwei geteilt
Was: Beim Nachziehen des Altbestands entsteht aus `⚙️ System ·
Grundgerüst` ein Paar: „Grundgerüst" behält Spielablauf, Szenen, Input
und Interaktion; neu dazu kommt eine Seite „Welt & Überleben" mit
Tag-Nacht-System, Herde/FSM und Kampf/Gesundheit. Die neue Seite bekommt
eine neue URL und einen eigenen Indexeintrag.
Warum: `ARTIFACT_RULES.md` verlangt eine Frage je Seite; die geprüfte
Fassung beantwortet mindestens drei (Befundliste vom 2026-08-23). Zwei
Seiten statt drei, weil jede weitere URL dauerhaft Pflege am
Sonntagsabgleich kostet — Isors Grenze „keine zu hohen laufenden
Kosten".
Verworfen: Teilen in drei (sauberster Schnitt, aber dreifache Pflege) ·
eine Seite lassen (bräuchte eine benannte Ausnahme von der eigenen
Regel).

## 2026-08-24 — Gras-Zellgröße: 32 m ist der geltende Wert für die Seiten
Was: Die Seiten übernehmen beim Nachziehen 32 m als Zellgröße. Das
GPU-Lernstück rechnet seine Herleitung mit der heutigen Dichte neu,
statt die alte 128-m-Empfehlung fortzuschreiben; die Terrain-Seite nennt
den gemessenen Wert statt „≈ 36 m".
Warum: 32 m ist der gebaute Stand — am 2026-08-24 am echten Prefab
gemessen (`GrassSingle_x2.prefab`, `_cellSize: 32`), deckungsgleich mit
dem Skript-Default. Der Widerspruch zur 128-m-Herleitung löst sich, weil
sich das **Optimierungsziel** verschoben hat, nicht nur die Dichte: Die
128er-Rechnung optimierte Batch-Füllung, als Draw Calls der Engpass
waren. Am 04.08. zeigte die Messung, dass Dreiecke der Engpass sind
(190.000 Büschel × 2.664 Tris = 507 Mio → 4,5 FPS; `TDD_NOTES.md`), der
Fix war ein LOD-Meshpaar mit **Distanzwahl je Zelle** — seither ist die
Zelle die Cull- und LOD-Einheit und muss klein gegen die LOD-Distanz
(60 m) sein. Der Tooltip am Feld trägt die Abwägung wörtlich: „Smaller
cells cull more precisely but cost more draw calls." *(Präzisiert noch
am selben Tag: Die erste Fassung dieses Eintrags erklärte den
Unterschied allein über die Dichte-Faustregel — zu kurz gegriffen, die
TDD_NOTES belegen den Zielwechsel.)*
Verworfen: 128 m in den Code umsetzen (wäre ein Projekt-Eingriff samt
Messlauf und gehört nicht in die Seitenpflege) · offen lassen (der
veröffentlichte Widerspruch bliebe stehen und sperrte zwei Seiten).

## 2026-08-25 — Archiv-Verweise tragen „(im Archiv)", Prüfung 1 erzwingt es
Was: Ein Verweis auf eine temporäre Befundliste (`_HARNESS_*.md`), die
schon im Archiv liegt, trägt in lebendem Text den Zusatz „(im Archiv)"
— auf derselben oder der unmittelbar folgenden Zeile. `pruefen.py`
(Prüfung 1) schlägt `_HARNESS_`-Verweise jetzt nach und meldet jeden
ungekennzeichneten, dessen Ziel fehlt; die Befundlisten selbst
überspringt sie wie Chroniken. Kennzeichen gewählt von Isor
(2026-08-25).
Warum: Die Befundlisten sind die einzige Dateiart, die planmäßig
verschwindet, und genau sie sah die Verweisprüfung nicht — belegt am
2026-08-23, als nach dem Archivieren drei Verweise ins Leere zeigten
und das Skript null meldete. Alles zu melden ginge auch nicht: Ein Teil
der Verweise ist Absicht (Beleg einer Regel, Herkunft eines
Ereignisses) und würde als Dauer-Fehlalarm den Prüfer entwerten. Das
Kennzeichen trennt Absicht von Versehen, mechanisch prüfbar; der Zusatz
stand an zwei Stellen schon von Hand im Bestand.
Warum das Fenster über beide Zeilen reicht: Der 72-Zeichen-Umbruch
schiebt den Zusatz real auf die Folgezeile — der erste scharfe Lauf
fand genau diesen Fall (`Kern/ROADMAP.md`, Eintrag zum
Artifact-Altbestand). Eine zeilengenaue Regel wäre eine Falle für jeden
künftigen Umbruch.
Verworfen: gar nicht prüfen (das belegte Loch bliebe) · alle
verschwundenen Befundlisten-Verweise melden (Dauer-Fehlalarm —
„Rauschen killt den Prüfer") · die Existenz im Datenbaum-Archiv
nachschlagen (der Archivbestand liegt außerhalb des Repos und variiert
je Rechner; das Skript wäre auf fremden Rechnern stumm oder falsch).

## 2026-08-25 — Die tote ID `0dd96ec7-…` bekommt keinen Nachfolger
Was: Die gelöschte „große Uni-Seite" der Session 2026-07-16/17 wird von
keiner heutigen Seite beerbt; die Gelöscht-Tabelle im
`ARTIFACT_INDEX.md` vermerkt das als abschließenden Zustand (Isor,
2026-08-25).
Warum: Ein Erbe hat nur Zweck, wenn ein Verweis umzubiegen ist —
geprüft am 2026-08-25: Weder im Knowledge-Ordner noch im Harness zeigt
etwas auf die ID, eine Offline-Kopie existiert nicht. Der Uni-Lernstoff
von damals lebt verteilt in den Lernstück-Seiten.
Verworfen: eine Lernstück-Seite als formalen Erben eintragen — ein Erbe
ohne einen einzigen Verweis, der ihn braucht, wäre Pflege ohne Leser.

## 2026-08-25 — Keine automatischen Tests; die Hand-Prüfung wird Regel (E56)
Was: Das Unity Test Framework wird nicht eingeführt. Der bisherige Weg —
TestMode-Schalter mit bekannter Eingabe, Sichtprüfung im Editor,
Diagnostic-Skripte — steht jetzt als Abschnitt „Tests" in
`CODE_GUIDELINES.md`, die Verwerfung samt Wiederprüf-Anlass dort unter
„Bewusst nicht übernommen" (Isor, 2026-08-25).
Warum: Kein Uni-Aufgabentext verlangt automatische Tests (geprüft am
2026-08-25 in den sechs Assignments von Semester 2 — verlangt sind nur
Playtests durch Mitstudenten); die Abgabe-Regel „jede Zeile auf
Semesterniveau verteidigen" verträgt keine NUnit-Attribute und Assembly
Definitions; und das Zeitbudget soll in Fertigstellung fließen, woran
das First-Ziel zuletzt scheiterte — nicht in Testpflege. Die
Architektur bleibt testbar (Model = plain C# ohne Unity-API), die Tür
also offen.
Verworfen: UTF nur für EditMode-Zahlenlogik (gleicher Einrichtungs- und
Lernaufwand bei kleinerem Nutzen) · UTF vollständig mit PlayMode (am
weitesten über Semesterniveau, laufende Pflegekosten).

## 2026-08-25 — Pflegetag: eine Seite gründlich, Auswahl nach ältestem Stand
Was: Der Sonntagsabgleich behält den Metadaten-Abgleich und prüft
zusätzlich genau eine Seite inhaltlich gegen Code und führende Quelle.
Dran ist die lebendige Seite mit dem ältesten Stand-Datum im
ARTIFACT_INDEX; außerhalb stehen die dort als nicht-nachziehbar
geführten Seiten (Zeugnisse, Muster-Seite, Harness-Seite). Regel in
`Kern/ARTIFACT_RULES.md` und `Kern/WORKFLOW.md` (Isor, 2026-08-25).
Warum: Der Abgleich allein sieht nur Metadaten — am 2026-08-23 meldete
er drei Funde, eine gründliche Durchsicht derselben acht Seiten fand
rund dreißig. Ganz ersetzen darf die Ein-Seiten-Prüfung ihn nicht: Er
ist die Prüfung, die die Stand-Stempel der Seiten erlaubt macht
(`DOC_RULES.md`, Abschnitt 7). „Ältester Stand" statt fester Liste,
weil der Turnus so keinen pflegbaren Zeiger braucht und sich selbst
heilt — beim Coden nachgezogene Seiten rücken von allein ans Ende. Bei
elf lebendigen Seiten (Stand heute) ist jede etwa alle elf Wochen dran;
die erste Verteidigungslinie bleibt das Review-Gate.
Verworfen: die Ein-Seiten-Prüfung ersetzt den Abgleich (die
Stempel-Erlaubnis bräche) · eine feste Turnusliste (ein Zeiger, der
verfallen kann) · alles lassen wie bisher (der belegte blinde Fleck
bliebe).

## 2026-08-25 — Parallele Sessions: das Revier-Modell
Was: Bei parallelen Sessions schreibt jede frei nur in die Schicht
ihres Fokus (das Revier); die Gemeinschaftsdateien (`STOERUNGEN.md`,
`GLOSSARY.md`, INDEX, `PLAN.md`) werden nur innerhalb der Befehle
beschrieben; ein Revier wird frei durch Abschnittsende. Fremde Schicht
nötig → melden statt schreiben. Regel in `Kern/WORKFLOW.md`, Abschnitt
„Parallele Sessions" (Isor, 2026-08-25).
Warum: `WORKFLOW.md` erlaubte 2–4 parallele Sessions, sagte aber nicht,
wer schreiben darf — am 2026-08-23 musste sich eine Parallel-Session
selbst eine Regel geben und schrieb vorsichtshalber gar nichts. Das
Revier folgt der Aufteilung, die ohnehin existiert (Isor öffnet
Sessions je Thema, der Abschnitt trägt den Fokus); der
Gemeinschaftsboden ist konfliktfrei, weil Isor die Befehle nur
nacheinander anstoßen kann — er spricht immer nur mit einer Session
zugleich. Eine Sperre oder ein Titel-Abgleich wäre Verwaltung für einen
Konflikt, den der Ablauf schon ausschließt; der Titel bleibt ohnehin
Anzeige, kein Beleg.
Verworfen: global nur eine Schreib-Session (die Doku-Pflicht der
übrigen bliebe liegen und lebte nur im Kontext) · vor jedem Schreiben
fragen (Reibung bei jedem sichern für meist eindeutige Fälle).

## 2026-08-25 — Systemliste (E14): Zuschnitt des Werkzeugs
Was: `systeme.py` erzeugt `SYSTEME.md` in der Projektschicht — eine
Tabellenzeile je Ordner unter `Assets/Scripts/` plus eine für
`Assets/Editor/`: Name, Anzahl .cs (rekursiv), letzte Änderung,
Beschreibung. Schlüssel ist der Ordnername; Beschreibungen kommen von
Hand und überleben jeden Lauf (`⚠ fehlt` / `⚠ nicht mehr vorhanden`,
wie beim Prefab-Prüfstand). Den Projektpfad liest das Skript aus
`Kern/PFADE.md` → `PROJEKT` (Isor, 2026-08-25).
Warum: Der ROADMAP-Wortlaut nannte noch `Assets/Systems`, `Entities`
und `Shared` — die Struktur ist seit der Grundentscheidung vom
2026-08-20 „Typ oben, ein Ordner je System darunter"
(`CODE_GUIDELINES.md`). Gelistet wird, was wirklich da ist: 16
System-Ordner mit 86 Skripten plus 7 Editor-Skripte (gemessen
2026-08-25). Die Marke statt eines harten Pfads, damit beim Umzug eine
Zeile reicht — `prefab_status.py` trägt den Pfad noch hart, es entstand
vor `PFADE.md`.
Verworfen: `Sandbox/` und `FolderTemplate/` mitlisten (beide sind eine
offene Projekt-Aufgabe „Ordnerstruktur prüfen" — erst klären, dann
listen) · Fremdcode (`ThirdParty/`, `TextMesh Pro/`) listen (kein
Projektwissen) · die letzte Änderung aus `git log` ziehen (teurer; das
Dateisystem-Datum trägt im Ein-Rechner-Betrieb).

## 2026-08-25 — Markdown→docx (E61b): Zuschnitt des Werkzeugs
Was: Vollgenerierung — jeder Lauf erzeugt die Abgabe-`.docx` komplett
neu aus dem Markdown-Manuskript plus einer Referenz-`.docx` mit den
Styles des bestehenden TDD-Layouts. Gebaut wird generisch als
Kern-Werkzeug (das TDD ist der erste Fall); Motor ist Pandoc mit
Referenz-Dokument — eine Vorentscheidung, die der Bautag im Probelauf
bestätigt. Pflichtteile: Sperrdatei-Check und Zeitstempel-Sicherung vor
dem Schreiben, `validate.py` danach, Seitenumbruch je Hauptkapitel und
SEQ-Felder für Beschriftungen aus dem Werkzeug (Isor, 2026-08-25).
Warum: Nur die Vollgenerierung macht das Manuskript wirklich führend —
bei Teilersetzung bliebe die `.docx` halbe Quelle, und genau deren
XML-Handarbeit soll das Werkzeug ablösen. Der Preis ist benannt:
Layout-Feinschliff von Hand wird bei jedem Lauf überschrieben und
wandert deshalb als letzter Schritt vor die Abgabe („Bilder zuletzt"
aus `Uni/DOCX_RULES.md`, verallgemeinert). Generisch im Kern, weil der
ROADMAP-Punkt dort lebt und jede künftige Abgabe denselben Weg geht.
Pandoc, weil Referenz-Styles sein Standardfall sind; die Felder-Frage
(SEQ) ist das benannte Risiko und entscheidet der Probelauf. Der
Sperr-Check gehört ins Werkzeug, weil die Handregel nachweislich reißt
— beim Design-Termin stand die Abgabedatei tatsächlich offen in Word.
Verworfen: kapitelweise Ersetzung in der bestehenden Datei (fummelig,
Quelle bliebe geteilt) · Spezialskript nur fürs TDD (der zweite Fall
käme sicher) · Eigenbau mit python-docx als Erstweg (eigener
Markdown-Parser nötig; bleibt Rückfallebene, falls der Pandoc-Probelauf
die Felder nicht sauber liefert).

## 2026-08-25 — Abgabe-Bau: Layout-Teile fix, Fließtext generiert
Was: Die Vollgenerierung (Eintrag oben) gilt nur für den Fließtext ab
Kapitel 1. Titelblatt, Erklärungen und die Verzeichnis-Felder leben als
fixe Datei `TDD Titelteil.docx`, die das Werkzeug unverändert
voranstellt; die Formatvorlage trägt Seitenumbruch- und Tabellen-Style.
Ein Nachlauf stellt Beschriftungen als SEQ-Felder samt Sprungmarken
und Querverweise als REF-Felder wieder her; die Seitenzählung läuft
durchgehend arabisch ab der ersten Seite (Isor, 2026-08-25).
Warum: Der erste Sichttest fiel durch — Markdown kann kein Layout:
Tabulator-Spalten und Zentrierung der Titelseite gingen verloren, die
extrahierten Verzeichnisse wurden Textmüll und ihre Überschriften
zählten als Kapitel (jede Kapitelnummer um drei verschoben), Tabellen
verloren ihren Style. Felder sind Words Sache — also bleiben sie in
Words Obhut (Titelteil) oder werden als echte Felder erzeugt (SEQ,
REF), statt als Text zu erstarren. Durchgehend arabisch, weil es Isors
Wunsch (Zählung ab Seite 1 wie in der Abgabe vom 21.08.) und die
Formatvorgabe zugleich erfüllt — das Original zeigte durchgehend
römische Ziffern, was keiner der zwei erlaubten Varianten entsprach.
Verworfen: die Titelseite als rohes OOXML im Manuskript (die
Unterschrift-Bilder hängen an Beziehungs-IDs, die ein Neubau nicht
kennt) · Zählung mit Neustart ab Kapitel 1 (die Zählung begänne nicht
auf Seite 1) · wortwörtlich römische Anzeige wie das Original
(entspricht keiner erlaubten Variante der Formatvorgabe).

## 2026-08-26 — Szenen wandern nach LFS, die Historie wird migriert
Was: Im Unity-Repo laufen `*.unity` und die gebackene NavMesh
(`NavMesh*.asset`) künftig über Git LFS; die kleinen Config-Assets
bleiben Text. Die gewachsene Historie wird am Wochenende mit
`git lfs migrate` umgeschrieben — vorher eine Sicherung als Bundle in
den Datenbaum. Ablauf als Punkt in `Kern/ROADMAP.md` (Isor, 2026-08-26).
Warum: Gemessen am 2026-08-26: Die Historie trägt 1.269 MB rohe
Szenen-Stände (75 Blobs, 92 % aller Bytes des Repos), `Village.unity`
wiegt 73 MB je Stand — GitHub sperrt normale Dateien ab 100 MB, und
die Grenze rückt mit jedem Terrain-Wachstum näher. Texturen, Audio und
Modelle laufen seit dem ersten Commit über LFS; nur die Szenen fehlten,
weil das Standard-Template auf Text-Merges für Teams setzt — bei einer
73-MB-Szene solo wertlos. Die GitHub-Quote (10 GB LFS-Speicher) lässt
auch die migrierte Historie (~1,4 GB) bequem zu.
Verworfen: alle `*.asset` pauschal nach LFS (die Tuning-Configs
verlören ihre lesbaren Diffs) · die Historie lassen (119 MB Pack für
immer in jedem Clone) · ein frisches Repo vom heutigen Stand (verwirft
die Commit-Geschichte — gegen „niemals löschen, nur archivieren").

## 2026-08-26 — Sichtbarkeit und Zugang der Repos
Was: `Isor-Tower-ProtoTyp-2026` wird privat gestellt, `Harness-Project`
bleibt bewusst öffentlich, `Knowledge` ist privat. Das GitHub-Token,
das im Klartext in der Remote-URL des Unity-Repos stand, ist entfernt;
das Widerrufen und das Privatstellen sind Isors Handgriffe auf
github.com (`Kern/ROADMAP.md`). Die Anmeldung übernimmt der
Credential Manager (Isor, 2026-08-26).
Warum: Das öffentliche Unity-Repo verteilte Asset-Store-Pakete weiter
(gegen deren Lizenz) und machte das Uni-Abgabeprojekt frei kopierbar —
ein Plagiatsrisiko in beide Richtungen. Beim Harness kennt Isor die
Gegenseite (Uni-Originaltexte und Zeugnisse bleiben öffentlich lesbar)
und wählt die Sichtbarkeit. Ein Token in der URL macht jede Kopie des
Ordners zu einem gültigen Kontoschlüssel; auf GitHub lag es nie, denn
`.git/config` wird nicht gepusht.
Verworfen: beide Repos privat (Isor behält den Harness bewusst
sichtbar) · das Token nur entfernen, ohne Widerruf (der Schlüssel
bliebe in älteren Kopien gültig).
**Ergänzt im selben Zug (Isor):** Das Unity-Repo bleibt **dauerhaft**
privat — es ist als Hauptprojekt für Bewerbungen gedacht, und gezeigt
wird über Builds, Videos und gezielte Lese-Einladungen auf GitHub,
bei Bedarf später über ein kuratiertes Showcase-Repo mit nur eigenen
Skripten. Ein öffentliches Arbeits-Repo ist dafür weder nötig noch
wegen der Asset-Store-Lizenzen möglich; ein Bereinigungs-Umbau
entfällt damit ersatzlos.

## 2026-08-26 — Repo-Grenze zur Asset-Library
Was: Ins Projekt-Repo gehört alles, was Unity zum Öffnen und Bauen
braucht — auch Fremd-Assets unter `Assets/ThirdParty/`; LFS trägt die
Last. In die Asset-Library des Datenbaums gehören Originale und
Quellformate (.blend, Download-Pakete, `.unitypackage`-Exporte) samt
`_Quelle.txt`. Regel in `Kern/CODE_GUIDELINES.md` → „Repo & Git"; die
zwei `ThirdAssets`-Zeilen der Unity-`.gitignore` entfallen — der
Ordner, den sie ignorieren, hat nie existiert (Isor, 2026-08-26).
Warum: Ein frischer Clone soll ohne Handarbeit öffnen — fehlende
Fremd-Pakete wären eine Bitte an das Gedächtnis. Die Library löst die
andere Hälfte: Lizenznachweis und Wiederverwendung über Projektgrenzen
(`IsorBackup/RULES.md`). Gelebt wurde die Grenze schon so; sie stand
nur nirgends als Regel.
Verworfen: Fremd-Packs nur in der Library halten (jeder Clone bräuchte
Handarbeit, bis das Projekt öffnet) · die toten Ignore-Zeilen behalten
(eine Regel über einen Ordner, den es nie gab, ist Rauschen).

## 2026-08-26 — Nummern-Klarstellungen: Build-Ablage und V-Nummer
Was: Spiel-Builds liegen im Datenbaum unter
`02_Projekte\<Projekt>\Builds\<Spielversion>_<JJJJ-MM-TT>\`
(`Kern/PFADE.md` → `DATENBAUM`); die Schema-Zeile steht in
`Kern/VERSIONIERUNG.md`. Dort steht jetzt außerdem: Die V-Nummer zählt
**Sessions** — der Commit-Vorschlag bei `/harness:ende` trägt sie,
Zwischenstände von Hand tragen freie Titel (Isor, 2026-08-26).
Warum: `Build/` ist im Repo zu Recht ignoriert — ohne benannten
Ablageort landet jeder Build woanders; das Datum unterscheidet zwei
Prototyp-Stände derselben Spielversion. Die Commit-Titel des
Unity-Repos mischten Schema und Zuruf („Update V 0.0023" neben „save
point") — keine Disziplinfrage, sondern eine Lücke in der Lesart: Die
Nummer hat nie jeden Commit gezählt, nur sagte das keine Regel.
Verworfen: das Schema für jeden Zwischenstand (Mehraufwand bei jedem
schnellen Sichern, ohne Gewinn) · die V-Nummer im Build-Namen (sie sagt
nichts über den Reifegrad — genau davor warnt `VERSIONIERUNG.md`).
