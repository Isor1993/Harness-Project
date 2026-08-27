# CODE_GUIDELINES.md — Code-Konventionen

Ownership: Code-Konventionen — Namen, Kommentare und Datei-Header,
Architektur, Ordnerstruktur, Tests, das Review-Gate und die
Repo-/Git-Regeln des Projekt-Repos.

Herkunft: Entstanden als Rohmaterial aus dem Brainstorm vom 2026-07-17.
Wann sie zuletzt angefasst wurde, sagt `git log` — genauer, als eine
Hand es je nachführt.

## Priorität

Im Konfliktfall gewinnt **Block 1**, solange das Projekt eine
Uni-Schicht hat — also solange ein Ordner `Uni/` neben dieser Datei
liegt. Ohne Uni-Schicht gewinnt **Block 2**.

Das ersetzt die frühere Angabe „Projekt-Typ: Uni/Privat", die von Hand
gesetzt werden musste. Grund: Beim Kopieren des Harness in ein privates
Projekt hätte man daran denken müssen umzustellen — vergisst man es,
gelten dort still die Uni-Regeln. Abgeleitet stellt es sich von selbst
richtig (`Kern/DECISIONS.md`, 2026-08-22).

## Block 1 — Stil & Naming (Uni-Pflicht, SAE-Conventions Stand 12/2024)
1. Code ausschließlich Englisch. Für Kommentare und Ausgaben ließe die
   SAE-Vorgabe auch Deutsch zu — hier gilt die schärfere Fassung, und die
   besitzt `Kern/DOC_RULES.md`, Abschnitt 9.
2. Kommentare erklären das Warum, nicht das Was. XML-`<summary>` für
   Methoden erwünscht.
3. Bezeichner aussagekräftig: nur ASCII, keine unbekannten Abkürzungen,
   kein `__`-Beginn, mehr als ein Buchstabe (Ausnahme: Schleifenzähler).
   Methoden = Verb + Nomen (`CalculateHeight`).
4. camelCase für Parameter und lokale Variablen. Private Felder:
   `_camelCase`. Booleans als Frage (`isRunning`, `hasTarget`, `canJump`).
5. PascalCase für Klassen, Structs, Interfaces, Methoden, Enums,
   Konstanten, Properties. Interfaces mit `I`-Präfix. Enum-Typen Singular,
   geflaggte Enums Plural. Callbacks beginnen mit `On`/`Handle`.
   **Bewusste Abweichung (2026-08-03):** Konstanten schreiben wir
   SCREAMING_SNAKE (`MAX_TRIES`, `WALK_STOP_DISTANCE`) statt PascalCase —
   siehe `Kern/DECISIONS.md`.
6. Format: eine Anweisung pro Zeile (einzeiliger Scope hinter der
   Bedingung erlaubt). Geschweifte Klammern je eigene Zeile (Allman);
   Properties dürfen einzeilig sein.
7. Member-Variablen private oder protected — Zugriff von außen über
   Properties. Keine ungarische Notation.
8. Namespaces und Ordner strukturieren das Projekt.
9. Nicht Spezifiziertes: Microsoft-C#-Konventionen bzw. Unity-Style-Guide.

## Kommentare & Datei-Header (Isors Standard)
Gilt überall, Uni wie privat. **Die Sprache steht nicht hier** — sie
gehört der Tabelle in `Kern/DOC_RULES.md`, Abschnitt 9. Sie ist schärfer
als die SAE-Vorgabe aus Block 1 und erfüllt sie damit mit.

Arbeitsteilung: Isor tippt Code ohne Kommentare; Header, Summaries und
Kommentare ergänzt Claude automatisch beim Review bzw. wenn Code
geschrieben wurde (vereinbart 2026-07-18).

### Datei-Header
Jede .cs-Datei beginnt mit diesem Block:

    /*****************************************************************************
    * Project : <Unity-Projektname>
    * File    : <Dateiname>.cs
    * Date    : <TT.MM.JJJJ — Erstelldatum>
    * Author  : Eric Rosenberg
    *
    * Description :
    * <Was die Klasse macht und wofür sie zuständig ist, 2–5 Zeilen.>
    *
    * History :
    * <TT.MM.JJJJ> ER Created
    ******************************************************************************/

History: pro nennenswerter Änderung eine neue Zeile `<Datum> ER <Was>`.

### Summaries
- XML-`<summary>` über jeder Klasse, jedem Enum, jeder Methode und
  jedem public Property/Event.
- Ausnahme: Unitys Standard-Eventmethoden (`Awake`, `Start`, `Update`,
  `OnEnable` …) brauchen keine.
- Methoden mit Parametern oder Rückgabewert: `<param>` / `<returns>`
  ergänzen.
- Format: **mehrzeilig**, wie das IDE bei `///` erzeugt — `<summary>` und
  `</summary>` je eigene Zeile, Text dazwischen; nicht einzeilig
  zusammenziehen (gilt auch für Properties). `<param>`/`<returns>` knapp
  füllen, kein Wort-für-Wort-Wiederholen des Offensichtlichen (sonst
  AI-Geruch, siehe Inline-Kommentare).
- Felder bekommen **kein** `<summary>`: serialisierte Felder tragen ihre
  Erklärung im `[Tooltip]` (siehe Inspector-Felder), nicht-offensichtliche
  `const`/private Felder höchstens eine kurze `//`-Zeile mit dem Warum.
- Property-`<summary>` und Feld-`[Tooltip]` dürfen sich inhaltlich
  überlappen: die Summary erscheint im Code-IntelliSense (wo Aufrufer die
  Property lesen), der Tooltip im Inspector — verschiedene Orte, keine
  verbotene Dopplung. Summary sagt, was der Name nicht trägt (Einheit,
  Bereich).

### Inline-Kommentare
- **Default: kein Kommentar.** Ein Inline-Kommentar rechtfertigt sich nur,
  wenn ein kompetenter C#-Leser ohne ihn in die Irre ginge oder hängen
  bliebe. Das Warum von Designentscheidungen steht in den DECISIONS der Schicht und im
  Datei-Header, nicht inline.
- Wenn nötig, dann **einzeilig**; mehrzeilige Erklärblöcke im
  Methodenkörper vermeiden. Wiederholt der Kommentar den Code nur auf
  Englisch → löschen.
- Kein Nacherzählen des Codes — klingt sonst AI-generiert; bei einer
  benoteten Abgabe ein echtes Risiko.

### Inspector-Felder
- Jedes serialisierte Feld bekommt ein `[Tooltip]` — was es ist und
  wofür es benutzt wird.
- Zusammengehörige Felder mit `[Header("...")]` gruppieren; Wertebereiche
  mit `[Range]` o. Ä. absichern. Ziel: Der Inspector ist ohne Blick in
  den Code verständlich.

## Block 2 — Architektur & Unity-Praxis (eigene Auswahl)
Quelle: Code-Rules des Dozenten (v2.2), gefiltert im Brainstorm 2026-07-17.

### Felder & Kapselung
- Default: `[SerializeField] private` fürs Inspector-Wiring — keine
  public Felder (deckt sich mit der Block-1-Regel „Member-Variablen
  private oder protected").
- **`_camelCase` für private Felder — überall**, auch in privaten
  Projekten. Der Dozent verbietet Underscore-Präfixe; die Uni-Regel
  gewinnt hier bewusst, weil ein einheitliches Muster über alle Projekte
  mehr wert ist als die Vorliebe einer einzelnen Vorgabe.
- Keine Singletons/Statics. Abhängigkeiten über Inspector-Wiring;
  gespawnte Objekte bekommen sie per `Init(...)` injiziert.

### Member-Reihenfolge (Isor, 2026-08-16)
Innerhalb einer Klasse in dieser Folge:
1. `[SerializeField]`-Felder (die Inspector-Oberfläche)
2. rein private Felder (interner Zustand)
3. Properties
4. Unity-Event-Methoden in Lebenszyklus-Reihenfolge — volle Folge in der
   Tabelle unten
5. public Methoden
6. private Methoden

Begründung: Wer die Klasse zum ersten Mal öffnet, sieht zuerst was sie
von außen braucht, dann wann sie etwas tut, dann was sie anbietet.
Die Lebenszyklus-Reihenfolge spiegelt den tatsächlichen Ablauf zur
Laufzeit — Suchen entfällt.

Innerhalb der `[SerializeField]`-Gruppe stehen Szenen-Objekte und Assets
getrennt beieinander, nicht gemischt.

#### Die Unity-Event-Methoden in ihrer Folge

Übernommen aus Unitys „Order of Execution for Event Functions", damit die
Folge nicht bei jeder Datei neu geraten wird. **Geschrieben wird nur, was
die Klasse wirklich benutzt** — das ist eine Reihenfolge, keine
Checkliste. Kommt eine Methode vor, die hier fehlt, entscheidet ihre
Stelle im Unity-Flussdiagramm, und die Zeile wird hier nachgetragen.

| Phase | Methoden, in dieser Folge |
|---|---|
| nur Editor | `Reset` · `OnValidate` |
| Start des Objekts | `Awake` · `OnEnable` · `Start` |
| Physik | `FixedUpdate` · `OnTriggerEnter` / `OnTriggerStay` / `OnTriggerExit` · `OnCollisionEnter` / `OnCollisionStay` / `OnCollisionExit` · `OnControllerColliderHit` · `OnJointBreak` |
| Eingabe am Collider | `OnMouseEnter` · `OnMouseOver` · `OnMouseDown` · `OnMouseDrag` · `OnMouseUp` · `OnMouseUpAsButton` · `OnMouseExit` |
| Spiellogik | `Update` · `LateUpdate` |
| Darstellung | `OnBecameVisible` · `OnBecameInvisible` · `OnPreCull` · `OnWillRenderObject` · `OnPreRender` · `OnRenderObject` · `OnPostRender` · `OnRenderImage` |
| Skizzen und alte GUI | `OnDrawGizmos` · `OnDrawGizmosSelected` · `OnGUI` |
| Anhalten und Ende | `OnApplicationPause` · `OnApplicationFocus` · `OnApplicationQuit` · `OnDisable` · `OnDestroy` |

Was die Tabelle **nicht** ist: eine Aussage darüber, wie oft eine Methode
läuft. `OnEnable` und `OnDisable` feuern bei jedem Ein- und Ausschalten,
nicht nur am Anfang und am Ende — sie stehen hier trotzdem an den Rändern,
weil die Folge das Lesen ordnet und nicht die Laufzeit zählt.

Coroutinen stehen nicht in der Tabelle. Sie sind keine Event-Methoden,
sondern private Methoden, und gehören damit unter Punkt 6.

### Denkmodell: Model-View-Presenter
- Model = plain C# ohne Unity-API (testbar), View = nur Anzeige,
  Presenter = einzige Brücke. View kennt nie das Model, Model nie die View.
- Pragmatik-Ausnahme: kein Parallel-Model, wo Unity den State schon
  besitzt (Rigidbody, Transform) — zwei Wahrheitsquellen vermeiden.
- Kamera nie als Child des Physik-Bodys: Position käme im Physik-Takt,
  Rotation im Input-Takt — die Mischung lässt die Welt stottern.
  Eigener CameraPresenter liest die Spielerposition in `LateUpdate`
  (nach der Rigidbody-Interpolation).

### SOLID — grob angewendet
- **S**: Eine Klasse, ein Job. Splitten erst, wenn sie zwei echte
  Zuständigkeiten hat — nicht vorsorglich.
- **O**: Erweitern durch neuen Code statt Ändern von funktionierendem —
  Ändern riskiert Regressionen in bereits korrektem Code. Praktisch:
  Definitionen/Configs als ScriptableObjects hinter Interfaces.
  Leitfrage: „Müsste ein dritter Typ diese Klasse wieder anfassen?"
- **L**: Entity-Typen über ein gemeinsames Interface, keine tiefen
  Vererbungsketten.
- **I**: Kleine, fokussierte Interfaces (`IShieldSystem`) statt einem
  fetten `IEntitySystem`.
- **D**: Interfaces nur, wo Austauschbarkeit echten Wert hat — nicht
  per Default auf alles.

### Werkzeuge mit Einsatzkriterium (kein Zwang)
- „X passiert, unabhängige Systeme reagieren" → ScriptableObject-
  Event-Channel. Erst einführen, wenn der zweite konkrete Consumer da ist.
- „Member einer wachsenden Content-Menge" (Items, Gegnertypen) →
  SO-Referenz als Identität statt Enum: neue Member sind neue Assets,
  kein Code-Change, nichts verschiebt sich. Enum nur für bekannte,
  geschlossene Mengen. Den Identitätstyp nach seinem Keyspace benennen,
  nicht nach dem häufigsten Member. Feldtyp per Subtyp einengen statt
  `OnValidate`-Guard — Compiler und Inspector-Picker verhindern den
  falschen Wert dann von vornherein.
- „Service über Szenengrenze" → `RuntimeReference<T>`-SO-Asset
  (single-writer, Consumer nur lesend). Gleiche Szene: direkt verdrahten.
- Bespoke-Lösung statt passendem Werkzeug: kurz begründen.

### UI-Wiring
- Presenter halten serialisierte Referenzen (`Image`, `Text`,
  `RectTransform`) und bauen nie UI zur Laufzeit — kein `new GameObject`,
  kein Canvas-Aufbau im Code; sie steuern, was schon existiert.
- Variable Listen (Inventar, Kontextmenü): eine im Prefab gebackene
  Template-Row klonen und poolen, statt Hierarchie ad hoc zu bauen.
- Read-only-Listen (Log, Statusanzeige): ein `TMP_Text` aus einem
  `StringBuilder` — poolen nur, wenn jede Zeile eigene Interaktion braucht.

### Unity-Handwerk
- Enums append-only: serialisiert wird der Integer — Einfügen oder
  Umsortieren verschiebt gespeicherte Werte still. Neue Member ans Ende.
- Lifecycle — die `Awake`/`OnEnable`-Reihenfolge *zwischen* Objekten ist
  undefiniert, darum zählt das Wo: Model im `Awake` des eigenen
  Presenters erzeugen. Fremde Models in `Start` subscriben (alle Awakes
  laufen vor allen Starts) / `OnDestroy` unsubscriben; View beim
  Subscribe mit dem aktuellen Wert seeden, denn Change-Events feuern
  erst bei der nächsten Änderung. SO-Channels in `OnEnable` /
  `OnDisable`. Jede verdrahtete Referenz null-guarden.
- `GetComponent` nur bei `Awake`/`Init`/Spawn, Ergebnis cachen — nie in
  `Update`-artigen Methoden: die Suche kostet sonst jeden Frame.
- Zerstörte Unity-Objekte hinter Interfaces fängt `== null` nicht —
  Unitys überladenes `==` liegt auf `UnityEngine.Object`, nicht auf dem
  Interface. Darum: `(target as UnityEngine.Object) == null`.
- Neues Input System, nie `Input.GetAxis` — dessen internes Smoothing
  erzeugt Joystick-Gefühl auf der Maus. Ein einziger `PlayerInputReader`
  als einzige Naht zum Input-System: kontinuierlicher Input → gepollte
  Property, diskreter Input → `System.Action`-Event.
- Action-Maps in `OnEnable` aktivieren, in `OnDisable` deaktivieren —
  aktiv gelassene Maps auf deaktivierten Objekten empfangen weiter Input.
- Maus-Delta roh lassen; Gamepad-Bindings mit Dead Zone (min. 0.12) +
  Scale. Optionales Smoothing per Lerp im Code, nie im Binding-Processor
  — so bleibt es per Einstellung konfigurierbar.
- Keine Design-Doc-Zitate in Code/Kommentaren (rotten still) —
  Absicht in eigenen Worten hinschreiben.
- Debug-Ausgaben (`Debug.Log`/`LogWarning`/`LogError`) in
  `#if UNITY_EDITOR … #endif` kapseln — Dozenten-Regel: keine Debug-Logs
  im gebauten Spiel. Reine Pipeline-Klassen loggen ohnehin nicht
  (`Kern/DECISIONS.md`, 2026-07-23 — „Kommentar-Konventionen geschärft").
- YAGNI: Abstraktion erst beim zweiten konkreten Use-Case.
- Magic Numbers benennen: ein Literal, das ein externes Faktum kodiert,
  bekommt eine benannte `const` mit Warum-Kommentar. Selbsterklärende
  Arithmetik bleibt roh.
- Unity-6-APIs (`rb.linearVelocity`, nicht `rb.velocity`). 4 Spaces,
  keine Tabs.

### Ordnerstruktur — Assets nach Typ
Grundentscheidung: `Kern/DECISIONS.md`, 2026-08-20. Die folgende Fassung
ist am 2026-08-22 gegen den tatsächlichen Assets-Baum gelesen worden,
nicht aus den Notizen abgeschrieben.

- **Oberste Ebene ist der Typ, darunter je ein Ordner pro System oder
  Wesen.** Vorhanden sind `Scripts/`, `Prefabs/`, `Materials/`,
  `Textures/`, `SO_Settings/`, `Shader/`, `VFX/`, `FBX/`, `Audio/`,
  `Animation/`, `Fonts/`, `Scenes/`, `Settings/`, `License/`.
  Beispiele: `Scripts/WorldGeneration/`, `Prefabs/Sheep/`.
  Nur anlegen, was gebraucht wird — keine leeren Ordner.
- **Editor-Code zentral in `Assets/Editor/`** (Isor, 2026-08-22). Der
  Ordner muss wörtlich `Editor` heißen; Unity kompiliert ihn editor-only
  und strippt ihn aus Builds. Das löst die frühere Angabe ab, Editor-Code
  dürfe auch im System-Ordner liegen.
- **Kein `Shared/` mehr.** Querschnitts-Utilities bekommen einen eigenen
  Scripts-Ordner nach ihrer Sache — im Projekt sind das
  `Scripts/Interfaces/`, `Scripts/Timer/`, `Scripts/Health/` und
  `Scripts/Diagnostic/`.
- **Fremdpakete bleiben unangetastet:** `ThirdParty/` und `TextMesh Pro/`
  behalten ihre innere Struktur — sie ist Teil des Herkunftsnachweises
  im TDD.
- Ordnernamen Englisch, PascalCase. Umbenennen/Verschieben immer im
  Unity-Editor, nie im Explorer — sonst brechen die .meta-GUIDs und
  damit alle Referenzen.
- **Preis der Umstellung, bewusst gezahlt:** Die Systemgrenzen, die am
  2026-08-08 durch die Trennung in vier Systeme sichtbar geworden waren,
  sind im Ordnerbaum nicht mehr zu erkennen.

### Review-Gate (vor dem Coden)
Vor jeder Implementierung den Plan gegen diese Datei prüfen — Claude
prüft mit, wenn er Code zeigt oder reviewt:
1. Fattening-Check: neuer `switch`-Zweig / neue Feldgruppe in einer
   geteilten Klasse? → ab der zweiten Variante Abstraktion erwägen.
2. Enum-/Serialisierungs-Sicherheit verletzt?
3. Gibt es ein passenderes Werkzeug (siehe oben)?
4. Naming-Fix: alle Geschwister des Musters mitfixen, nicht nur die
   eine angezeigte Stelle.
5. Artifact-Check: Steht eines der Skripte, die gleich angefasst werden,
   in einer Skripte-Zeile von ARTIFACT_INDEX.md? Dann veraltet die Seite
   durch die Änderung und wird nach dem Coden nachgezogen.
   **Ausnahme:** Seiten, deren Stand an einer Versionsnummer hängt,
   werden nicht zwischendurch nachgezogen — dort wird die Abweichung
   nur gesammelt (`ARTIFACT_INDEX.md` → „Was ohne neue Versionsnummer
   passiert"). Betrifft heute `⚙️ System · Harness`.

## Repo & Git

Regeln für das Projekt-Repo; Grundentscheidungen vom 2026-08-26,
Begründungen in `Kern/DECISIONS.md`. Nummern und Build-Ablage besitzt
`Kern/VERSIONIERUNG.md`.

- **Ins Repo gehört, was Unity zum Öffnen und Bauen braucht** — auch
  Fremd-Assets (`Assets/ThirdParty/`, innere Struktur unangetastet,
  siehe „Ordnerstruktur"). Originale und Quellformate (`.blend`,
  Download-Pakete, `.unitypackage`-Exporte) gehören in die
  Asset-Library des Datenbaums (`IsorBackup/RULES.md`).
- **Große Binärdateien laufen über Git LFS**, geregelt in der
  `.gitattributes` des Projekts: das Unity-Template (Texturen, Audio,
  Modelle) plus `*.unity` und `NavMesh-*.asset`. Der Bindestrich ist kein
  Tippfehler: `NavMesh*.asset` traf bei der Migration am 2026-08-26 auch
  `ProjectSettings/NavMeshAreas.asset`, eine 1-KB-Einstellungsdatei.
  Kleine YAML-Configs
  (ScriptableObjects) bleiben Text — ihre Diffs sind beim Tuning die
  Lesehilfe.
- **Projekt-Repos mit Fremd-Assets sind privat.** Die
  Asset-Store-Lizenz erlaubt keine Weiterverbreitung, und ein öffentlich
  kopierbares Abgabeprojekt ist ein Plagiatsrisiko.
- **Kein Token in der Remote-URL.** Die Anmeldung übernimmt der
  Credential Manager; eine URL mit eingebettetem Schlüssel macht jede
  Ordnerkopie zum Kontozugang.

## Tests

Geprüft wird **von Hand, nicht durch ein Test-Framework** — entschieden
am 2026-08-25, Begründung in `Kern/DECISIONS.md`; die Verwerfung des
Unity Test Framework steht unten unter „Bewusst nicht übernommen".

- **TestMode-Muster:** Systeme mit sichtbarem Ergebnis bekommen einen
  `TestMode`-Schalter (Enum im Inspector), der bekannte Eingaben
  erzwingt — etwa Flat/Ramp statt Rauschen im Terrain. Gut ist ein
  TestMode, wenn das richtige Ergebnis vorhersagbar ist: bekannte
  Eingabe, bekanntes Bild.
- **Sichtprüfung gehört zum Fertigwerden:** „Geprüft" im Sinne der
  Baustein-Definition (`Kern/WORKFLOW.md`, Begriff „Baustein") heißt,
  dass jeder TestMode des Bausteins einmal angesehen wurde — nach jeder
  Änderung am betroffenen System erneut.
- **Diagnostic-Skripte** (`Scripts/Diagnostic/`) zählen zum selben
  Werkzeugkasten: Sie machen Zahlen sichtbar, die das Auge nicht prüfen
  kann (Timings, Zähler).
- **Zahlenregeln ohne Bild** (Mindestabstände, Wertebereiche): Wo das
  Hinsehen nicht trägt, rechnet eine Editor-Debug-Ausgabe oder ein
  Diagnostic-Skript die Regel nach und meldet Verstöße im Log.

## Bewusst nicht übernommen

Nur echte Verwerfungen — was geprüft und abgelehnt wurde, damit die
Überlegung nicht wieder von vorn beginnt. Aufgeschobene Aufgaben stehen
in der ROADMAP, geltende Regeln in den Blöcken oben.

- **Dozenten-Default „public Felder fürs Inspector-Wiring"** — verworfen
  zugunsten Kapselung (Begründung in `Kern/DECISIONS.md`).
- **Semantic Versioning für die Spiel-Version** — verworfen zugunsten
  eines Schemas nach Reifegrad (`Kern/VERSIONIERUNG.md`).
- **Unity Test Framework** — verworfen am 2026-08-25 zugunsten der
  Hand-Prüfung (Abschnitt „Tests"; Begründung in `Kern/DECISIONS.md`).
  Neu geprüft wird, wenn ein Uni-Modul automatische Tests verlangt oder
  die Lernphase endet.
- **Eine Ordner-Vorlage im Projekt (`Assets/FolderTemplate/`)** —
  verworfen am 2026-08-26 samt `Assets/Sandbox/`. Beide waren leer und
  wurden von nichts referenziert; die Vorlage bündelte zudem neun Typen
  **unter** einem System und bildete damit das Schema ab, das der
  Abschnitt „Ordnerstruktur" abgelöst hat. Begründung in
  `Kern/DECISIONS.md`. Eine neue Vorlage wäre nur dann sinnvoll, wenn
  sie das Typ-Schema abbildet — dann steht sie aber schon als Liste
  oben und braucht keine leeren Ordner.
