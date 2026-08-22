# DECISIONS.md — Entscheidungen Harness

Ownership: Nur Entscheidungen zum Harness — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.


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

## 2026-07-19 — Session-Typen: Brainstorm+Design ein Typ, 1:1-Regel
Was: „Brainstorm/Design" ersetzt die zwei getrennten Typen; pro Baustein
gilt: erst eine Brainstorm/Design-Session (was & wie), dann eine
Development-Session (nur Umsetzung). Eine Design-Session darf mehrere
Bausteine vorentscheiden.
Warum: Design ohne Brainstorm-Anteil kam in der Praxis nie vor; die feste
Reihenfolge gibt Isor einen klaren Schnitt zwischen Entscheiden und Bauen.
Verworfen: vier getrennte Typen; freies Mischen von Design und Umsetzung
in einer Session.

## 2026-07-17 — Minimalistisch zur Einsatzreife
Was: Alle vier Session-Typen nur minimal definiert; ausgearbeitet wird
erst, wenn der Praxisbetrieb es verlangt. Regel-Dateien beschreiben nur
den Ist-Zustand, Begründungen gehören hierher.
Warum: Uni-Projekt startet 2026-07-18 — funktionstüchtig schlägt
vollständig.
Verworfen: volle Ausarbeitung aller Dokumente vor Praxisstart
(alte Roadmap-Reihenfolge).

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
