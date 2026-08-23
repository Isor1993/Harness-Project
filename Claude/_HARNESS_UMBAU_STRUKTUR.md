# _HARNESS_UMBAU_STRUKTUR.md — Bauplan: Struktur begradigen, dann Hooks

Ownership: Nur die Handgriffe **dieser einen Umbau-Folge** — der Harness
wird sein eigenes Repo, danach werden die Skript-Prüfungen als Hooks
erzwungen. Temporär: Was überlebt, sind die zwei Punkte in
`Kern/ROADMAP.md`, nicht diese Datei. Danach ins Archiv.
Format: je Baustein **Ausgangslage** / **Ziel** / **Handgriffe** /
**vorher wissen**. Entschieden wird hier nichts — die Begründungen
stehen in `Kern/DECISIONS.md`.

Entstanden am 2026-08-23 aus einem Gespräch mit Isor, in dem er die
Ordnerstruktur zum ersten Mal ganz durchgesehen hat. Beide Bausteine
gehören in **eigene Sessions**, in dieser Reihenfolge.

---

## Baustein 1 — Struktur begradigen

### Ausgangslage, gemessen am 2026-08-23

Bis zu den Regeln führen **zwei Weiterleitungen** über drei `CLAUDE.md`:

| Ebene | was dort liegt | im Repo? |
|---|---|---|
| `Harness Project\` | `.claude\`, `CLAUDE.md` (Notkern) | **nein** |
| `My Harness Development\` | `CLAUDE.md` (Wegweiser), Unity-Kram, `Claude\` | ja, hier beginnt `.git` |
| `My Harness Development\Claude\` | die echten Regeln | ja |

Das mittlere Ordnerpaar ist ein **Unity-Projekt, dessen `Assets\` 14
Dateien enthält — alle aus der Unity-Vorlage** (SampleScene,
TutorialInfo, Renderer-Settings). Kein eigenes Skript, kein eigenes
Asset. Die Unity-Ebene trägt nichts bei und schleppt `Library\`,
`Logs\`, zwei `.csproj`, `.slnx` und je eine `.meta` pro Datei mit.

### Ziel

Ein Repo, dessen **Wurzel der Harness selbst ist**:

    <Repo>\
    ├── .claude\                 Befehle, Rechte, später Hooks
    ├── CLAUDE.md                die echten Regeln — lädt von selbst
    ├── INDEX.md · PLAN.md
    ├── Kern\ · Uni\ · IsorBackup\ · Projekte\

**Null Weiterleitungen.** Was dabei **ersatzlos entfällt**: der
**Notkern** (er existiert nur, weil die automatisch ladende Datei heute
nicht die Regeldatei ist), die INDEX-Kategorie **Wegweiser** samt der
Liste `WEGWEISER` in `index_bauen.py`, und zwei der drei `CLAUDE.md`.

### Handgriffe

1. Unity-Anteile **archivieren statt löschen**: `Assets\`, `Library\`,
   `Logs\`, `ProjectSettings\`, `Packages\`, `*.csproj`, `*.slnx`,
   `.vsconfig`.
2. Inhalt von `Claude\` eine Ebene hoch in die Repo-Wurzel.
3. `.claude\` in dieselbe Wurzel — **nicht** in einen Unterordner. Der
   Ordner mit Punkt muss ganz oben im geöffneten Ordner liegen, sonst
   findet Claude Code ihn nicht. *(Namensfalle: `.claude\` ist die
   Konfiguration des Programms, `Claude\` war Isors Harness-Ordner.
   Genau diese Ähnlichkeit hat am 2026-08-23 für Verwirrung gesorgt.)*
4. `.gitignore` neu: Unity-Zeilen raus, `/.claude/settings.local.json`
   rein — die Datei ist maschinen- und nutzerspezifisch. Geprüft:
   `.claude` selbst wird heute **nicht** ausgeschlossen, es würde also
   sofort mitversioniert.
5. Notkern-Datei und Wegweiser-`CLAUDE.md` archivieren; ihre gültigen
   Teile — vor allem die Liste der nie zu durchsuchenden Unity-Ordner —
   in die neue Wurzel-`CLAUDE.md` übernehmen.
6. Skripte nachziehen: in `pruefen.py` den Pfad `ARBEITSKOPIE`, in
   `index_bauen.py` die Liste `WEGWEISER` und den Wegweiser-Abschnitt.
7. `WORKFLOW.md` → „Wo die Auslöser liegen" neu begründen: Dort steht
   heute, `.claude\` sei nicht versioniert — danach ist es das. Die
   Doppelung Original/Arbeitskopie bleibt nötig, aber nur noch, weil
   Claude Code die Befehle ausschließlich in `.claude\commands\` findet.
8. Memory- und Session-Ordner unter `~\.claude\projects\` mitnehmen.

### Vorher wissen

- **Nach den Umzugsregeln arbeiten** (`DOC_RULES.md`, Abschnitt 11):
  Commit des Ist-Standes **vor** dem ersten Schnitt, verschieben per
  Skript statt von Hand, vorher und nachher zählen, Originale nach
  `99_Archiv\_Zu_Loeschen\`. Erster echter Anwendungsfall dieser Regel.
- **Claude Code führt Sessions und Erinnerungen je geöffnetem Ordner.**
  Ein anderer Ordner heißt ein anderer Schlüssel — die Session-Historie
  und rund dreißig Memory-Einträge sind sonst nicht mehr zur Hand
  (Handgriff 8).
- Soll das Repo am Ende woanders liegen, braucht **GitHub Desktop** den
  neuen Pfad. Die Historie bleibt vollständig: verschoben wird innerhalb
  desselben Repos.
- **Zu entscheiden ist die Versionsnummer.** Nach `VERSIONIERUNG.md`
  bedeutet ein Wechsel von `X`, dass die Struktur sich ändert und ein
  Projekt umziehen muss — das trifft hier zu. Ob daraus **2.0.0** wird,
  entscheidet Isor.

### Die betroffenen Zeiger — vollständig durchsucht am 2026-08-23

Gesucht wurde nach `My Harness Development`, `Harness Project`, dem
Ordner `Claude\` und `.claude\` über alle `.md`, `.py` und `.ps1` des
Bestands **und** über den Datenbaum. Ergebnis in drei Gruppen.

**Gruppe 1 — muss geändert werden:**

| Stelle | was dort steht |
|---|---|
| `Kern/Befehle/` — **alle fünf** | absoluter Pfad `C:\Repos Isor\Harness Project\My Harness Development\Claude\Kern\…` |
| `.claude\commands\harness\` — **alle fünf** | dieselbe Zeile in der Arbeitskopie; zusammen **zehn** Dateien |
| `Kern/WORKFLOW.md` → „Wo die Auslöser liegen" | Tabelle und Begründung, dass `.claude\` nicht versioniert sei |
| `Kern/WORKFLOW.md` → „Prüfung" | „liegt oben in `Claude\`" — heißt danach: in der Repo-Wurzel |
| `Kern/VERSIONIERUNG.md` → Auslieferung | der Handgriff „`Kern/Befehle/*.md` nach `.claude\commands\harness\` kopieren" — bleibt gültig, Pfad prüfen |
| `Kern/Werkzeuge/pruefen.py` | `ARBEITSKOPIE`, eine Ebene zu tief |
| `Kern/Werkzeuge/index_bauen.py` | `WEGWEISER` entfällt ganz; dazu der Hinweistext im INDEX-Kopf |
| **`C:\IsorBackup\README.md`** | zeigt mit vollem Pfad auf `…\Claude\IsorBackup\` — **liegt außerhalb des Repos** und wird sonst übersehen |
| **`C:\Repos Isor\Knowledge\README.md`** | zeigt mit vollem Pfad auf `…\Claude\Kern\KNOWLEDGE_RULES.md` — ebenfalls außerhalb, im dritten Repo |

**Gruppe 2 — bleibt stehen, wird nicht angefasst:** Die Treffer in
`Kern/DECISIONS.md` und `Kern/LOG.md` sind **Chronik**; was geschrieben
ist, bleibt (`DOC_RULES.md`, Abschnitt 6). **Aber:** Der Eintrag vom
2026-08-22 über die Befehls-Doppelung wird durch den Umbau inhaltlich
überholt — er bekommt eine Zeile **Fortgeführt am `<Datum>`** mit Zeiger
auf die neue Fassung, statt geändert oder archiviert zu werden. Ebenso
zu prüfen: der Eintrag „Der Notkern in der obersten `CLAUDE.md`" — seine
Begründung entfällt vollständig, das ist ein Fall fürs `_ARCHIV.md`.

**Gruppe 3 — erledigt sich selbst:** `INDEX.md` wird erzeugt.
`Kern/GLOSSARY.md` → „Auslöser" nennt `.claude\commands\harness\` ohne
absoluten Pfad und bleibt richtig. `_HARNESS_PRUEFUNG_1_0_0.md` ist
temporär und geht ohnehin ins Archiv.

**Nicht anfassen:** die abgelegte Auslieferung `Harness_1.0.0` unter
`C:\IsorBackup\05_Werkzeuge\` — sie trägt die alten Pfade, und eine
abgelegte Auslieferung wird nie bearbeitet (`VERSIONIERUNG.md`). Die
nächste entsteht korrekt.

**Zum Prüfen hinterher:** `pruefen.py` findet tote Verweise auf Dateien
dieses Baums von allein — Prüfung 1. Die absoluten Pfade in den
Befehlsdateien sieht es **nicht**, weil sie außerhalb liegen. Die zehn
Dateien gehören deshalb von Hand gegengelesen, und Prüfung 3 bestätigt
danach nur noch, dass Original und Arbeitskopie gleich sind.

### Geklärt, nicht mehr zu diskutieren *(Isor, 2026-08-23)*

Der Harness muss **nie** in einem Projekt-Repo liegen, um mit dessen Code
zu arbeiten. Die Freigabe über `additionalDirectories` genügt — belegt am
selben Tag: Eine Session las 89 Skripte und die Asset-Werte des
Tower-Repos, während dort kein einziges Harness-Dokument liegt und der
`.claude`-Ordner leer ist. Ins Projekt gehört der Harness nur, wenn das
Projekt **ohne Isor** weitergegeben wird; dafür gibt es die Auslieferung.

---

## Baustein 2 — Hooks: erzwingen statt erinnern

Erst **nach** Baustein 1. Grund: Hooks leben in
`.claude\settings.json`; solange die Datei außerhalb des Repos liegt,
wäre jeder Hook unversioniert und nach einem Rechnerwechsel weg.

### Ausgangslage

`.claude\settings.json` enthält heute nur die Berechtigungsliste, keine
Hooks. Ein Hook führt bei einem Ereignis ein Kommando aus — **der
Harness tut das, nicht Claude**. Er greift also auch dann, wenn eine
Regel überlesen wird. Genau dort liegt die Schwachstelle: Von den sieben
Prüfebenen in `WORKFLOW.md` hängen die vier Urteils-Ebenen zu Recht am
Menschen, die drei Skript-Ebenen aber unnötigerweise an Claudes
Erinnerung. Am 2026-08-23 ist das dreimal gerissen — die Anzahl-Regel
wurde am Tag nach ihrer Einführung viermal gebrochen, das Glossar
sammelte drei falsche Zeilen, ein überholter Planabschnitt wurde als
gültig vorgelesen.

### Kandidaten

1. **Session-Start ruft `pruefen.py`.** Die Zeile steht seit dem
   2026-08-23 in der Leseordnung (`CLAUDE.md`, Punkt 5) und wäre als
   Hook eine Tatsache statt einer Bitte.
2. **Ein Lauf nach Änderungen an `.md`-Dateien.**

### Vor dem Bauen zu klären

Welche Ereignisse es tatsächlich gibt, was ein Hook zurückgeben darf, wie
er sich verhält, wenn das Skript fehlschlägt, und ob er in die
Auslieferung mitwandert.

**Nicht mehr offen** *(Isor, 2026-08-23)*: ob ein Hook auf Dateien im
**freigegebenen** Ordner zugreifen kann. Kann er — er startet ein
Kommando, und ein Prozess kennt keine Projektgrenze, nur Dateirechte.
Offen bleibt allein die kleinere Frage, ob ein Ereignis auch dann
**feuert**, wenn die geschriebene Datei außerhalb des geöffneten Ordners
liegt. Für Kandidat 1 ist beides ohne Belang.

**Nicht erwarten:** dass Hooks die Urteils-Ebenen ersetzen. Sie führen
Kommandos aus, sie beurteilen keine Aussagen.
