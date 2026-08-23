# ARTIFACT_INDEX.md — Bestand der Artifact-Seiten

Ownership: Welche Artifact-Seiten es gibt, woran jede hängt und wer auf
sie zeigt. Regeln zu Typen, Benennung und Aufbau stehen in
ARTIFACT_RULES.md — hier steht nur der Bestand.

Wofür der Index gut ist: Er wird beim Review-Gate abgefragt
(`CODE_GUIDELINES.md` → „Artifact-Check") und beim Sonntagsabgleich
(`ARTIFACT_RULES.md`).

**Benannte Ausnahme von der Schichten-Regel:** Dieser Index bleibt **eine
Datei im Kern**, obwohl er Seiten aus Projekt, Uni und Kern führt. Grund:
Seine Hauptzusage steht gleich unten — „nie eine zweite Seite zum selben
Thema anlegen". Die kann nur eine ungeteilte Liste geben; drei Teillisten
hießen dreimal nachsehen. Ein Verzeichnis fremder Adressen ist kein
Inhalt, den man nach Schichten ordnet (`DOC_RULES.md`, Abschnitt 8).
Die Schicht steht je Abschnitt dabei.

Zeilen je Eintrag:
- **URL** — die Seite selbst. Nie eine zweite Seite zum selben Thema anlegen.
- **Stand** — Datum, gegen das die Seite zuletzt geprüft wurde. Bei
  Zeugnis-Seiten heißt die Zeile **Datum**: Dort ist kein Prüfstand
  gemeint, sondern der Inhalt selbst (`ASSESSMENT_RULES.md`).
- **Quelle** — die führende .md-Datei im Repo.
- **Skripte** — bei System-Seiten: was die Seite beschreibt. Ändert sich
  eines davon, ist die Seite veraltet. Bei Lernstücken heißt die Zeile
  **Beispiel** — die Seite erklärt ein übertragbares Konzept und nutzt
  diese Klassen nur als Beleg.
- **Seite →** — wohin die Seite selbst verlinkt.
- **Seite ←** — welche Knowledge-Notizen auf sie zeigen.

---

## 📍 Status  — Schicht: Projekt

### 📍 Status · Wo das Projekt steht
```
URL      https://claude.ai/code/artifact/d5e30d97-fafd-4f9e-be83-e727df4d0405
Stand    2026-08-23 — nach dem Umbau neu gebaut, erste Seite im neuen
         Hausstil (ARTIFACT_RULES → „Gestaltung")
Quelle   PLAN.md, Kern/ROADMAP.md, Projekte/Isor_Tower/ROADMAP.md,
         Uni/ROADMAP.md, Projekte/Isor_Tower/GDD.md
Skripte  keine — die Seite beschreibt den Projektstand, nicht Code
Seite →  System · Harness
Seite ←  keine
```

---

## 🎓 Zeugnis  — Schicht: Kern

**Kein vierter Typ** — die Seiten gehören zum Session-Typ „Zeugnis"
(WORKFLOW.md) und werden von ASSESSMENT_RULES.md geregelt. Hier stehen
sie nur, damit keine URL unerklärt bleibt. Abweichend vom übrigen
Bestand: Jedes Zeugnis behält seine eigene URL und wird **nie
nachgezogen** — der alte Stand ist der halbe Zweck. Beim Review-Gate
sind diese Seiten deshalb zu überspringen.

### 🎓 Zeugnis · 2026-08-16, Politur-Wochenende
```
URL      https://claude.ai/code/artifact/dfb56399-a0ac-467c-8efb-feb88940678e
Datum    2026-08-16 — Zeugnis-Datum, kein Prüfstand; wird nicht nachgezogen
Quelle   Kern/Zeugnisse/<Datum>.md, Kern/ASSESSMENT_RULES.md
Skripte  keine — die Seite bewertet den Projektstand, nicht Code
Seite →  keine
Seite ←  keine
```

### 🎓 Zwischenzeugnis 11.08.2026
```
URL      https://claude.ai/code/artifact/b9f54327-8f46-4d25-b667-ff66852adc6f
Datum    2026-08-11 — Zeugnis-Datum, kein Prüfstand; wird nicht nachgezogen
Titel    weicht vom Namensschema ab und bleibt so: Die Seite entstand vor
         dem Schema, und ein Zeugnis wird nie neu veröffentlicht
         (ASSESSMENT_RULES). Hier steht der Titel, der tatsächlich
         draußen steht — Abgleich am Pflegetag 2026-08-23.
Quelle   Kern/Zeugnisse/<Datum>.md, Kern/ASSESSMENT_RULES.md
Skripte  keine — die Seite bewertet den Projektstand, nicht Code
Seite →  keine
Seite ←  keine
```

---

## ⚙️ System  — Schicht: Projekt (Isor's Tower)

### ⚙️ System · Terrain & Gras
```
URL      https://claude.ai/code/artifact/14256389-ed13-4e83-9fe1-e590b96b56d4
Stand    2026-08-06, Werkzeug-Abschnitt 2026-08-08
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
Skripte  TerrainConfig, HeightmapGenerator, PlateauModifier, MeshBuilder,
         CurveLookup, Placeable, ObjectPlacer, Placement, PlacementMetrics,
         DensityStrategy, PlacementExclusion, ExclusionArea,
         PlacementExclusionFilter, PlaceableRenderMode,
         RuntimePlacementSpawner, GrassCellBuilder, GrassCell,
         GrassRenderProfile, GrassLodSelector, InstancedRenderer,
         FpsDisplay, TerrainToolWindow, TerrainToolPresenter
Seite →  Lernstück Multithreading, Poisson-Disc-Sampling, GPU-Instancing,
         EditorWindow & MVP
Seite ←  keine direkt; terrain-pipeline.md und prozedurales-mesh-grundlagen.md
         zeigen auf die Offline-Kopie des Vorgängers
         (Seiten/2026-07-18-terrain-architektur.html)
```

### ⚙️ System · Grundgerüst
```
URL      https://claude.ai/code/artifact/761467e7-ed2e-48a9-a237-e208526fae48
Stand    2026-08-06 — **die Seite wurde am 2026-08-07 noch einmal
         veröffentlicht, also nach ihrer letzten Prüfung.** Beim nächsten
         Anfassen gegen den Code prüfen und den Stempel nachziehen
         (Fund des Pflegetags 2026-08-23).
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
Skripte  SceneLoader, GameController, MainMenuController, PauseMenuController,
         Player, PlayerMotor, PlayerLook, PlayerInteractor,
         PlayerControls (.inputactions), PlayerInputReader,
         IInteractable, SheepInteractable, TorchInteractable;
         geplant, noch nicht gebaut: AudioManager, SceneMusic
Seite →  System · Terrain & Gras; nennt das Lernstück „Der Input-Reader"
         im Text (noch ohne Link)
Seite ←  keine
```

### ⚙️ System · Nur ein Schaf zähmbar
```
URL      https://claude.ai/code/artifact/12ef2f34-c7f5-4e79-9798-a60edab85c02
Stand    2026-08-07
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
Skripte  TamedSheepReference (SO), SheepInteractable, Sheep, PlayerInteractor,
         IInteractable, FollowPlayerState
Seite →  (noch nicht erfasst)
Seite ←  Patterns/validierung-beim-lesen.md
```

---

## 💡 Lernstück  — Schicht: Kern (übertragbar)

### 💡 Lernstück · Multithreading in Unity
```
URL      https://claude.ai/code/artifact/f9d2635f-431b-4f60-90fc-dca3151cd51f
Stand    2026-08-05
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel ObjectPlacer, CurveLookup, ExclusionArea, PlacementExclusionFilter,
         GrassCellBuilder
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · Poisson-Disc-Sampling
```
URL      https://claude.ai/code/artifact/2a5340fb-b4de-4326-be1a-c330767d8fdb
Stand    2026-08-06
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel ObjectPlacer
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/poisson-disc-verteilung.md
         (dort auch Offline-Kopie Seiten/2026-07-23-poisson-disc.html)
```

### 💡 Lernstück · GPU-Instancing
```
URL      https://claude.ai/code/artifact/0183966d-3132-4804-af82-83591ffe5f09
Stand    2026-08-06
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel InstancedRenderer, GrassCellBuilder, GrassCell, GrassRenderProfile,
         GrassLodSelector, PlaceableRenderMode
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/seed-statt-serialisieren.md,
         Unity/instancing-culling-zellengroesse.md
         (beide über die Offline-Kopie Seiten/2026-08-04-gras-instancing.html)
```

### 💡 Lernstück · Terrain-Fallen
```
URL      https://claude.ai/code/artifact/6241c560-1893-45ab-9f4f-aa71dbc01da6
Stand    2026-08-06
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel MeshBuilder, HeightmapGenerator
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/chunk-nahtlose-normalen.md
```

### 💡 Lernstück · Input-Reader
```
URL      https://claude.ai/code/artifact/20be8fc5-f9bf-4d49-8af5-bab3247bb6e3
Stand    2026-08-06
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel PlayerInputReader, PlayerControls (.inputactions), GameController
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · EditorWindow & MVP
```
URL      https://claude.ai/code/artifact/415afd2f-e1f4-4e9d-9517-0b8585f74ac6
Stand    2026-08-08
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel TerrainToolWindow, TerrainToolPresenter,
         PrefabPainterWindow, PrefabPainterPresenter
Seite →  System · Terrain & Gras
Seite ←  Patterns/mvp-model-view-presenter.md,
         Unity/editor-scripting-editorwindow.md
```

---

## ⚙️ System  — Schicht: Kern (der Harness selbst)

### ⚙️ System · Harness
```
URL      https://claude.ai/code/artifact/42f2b4ac-aacb-45eb-8911-55eb7769c459
Stand    2026-08-23 — gebaut zur Version 1.0.0
Quelle   CLAUDE.md, Kern/WORKFLOW.md, DOC_RULES.md, VERSIONIERUNG.md,
         DECISIONS.md
Skripte  keine Unity-Skripte; die Seite beschreibt die Harness-Dateien
         und die Befehle unter Kern/Befehle/
Seite →  keine
Seite ←  keine
```
Die Seite beschreibt den Harness in seinem **aktuellen** Zustand und wird
**bei jeder neuen Harness-Version nachgezogen** — sie ist damit die
einzige Seite, deren Stand an der Versionsnummer hängt statt am
Sonntagsabgleich (`Kern/VERSIONIERUNG.md`). Gebaut wird sie erst, wenn
der Kern nach der Abnahme steht; vorher beschriebe sie eine Baustelle.

---

## 🎨 Muster  — Schicht: Kern

Keine eigene Gattung, sondern eine Seite, die zufällig als Beleg dient:
`ARTIFACT_RULES.md` → „Gestaltung" verweist auf sie als Herkunft der
Farbwelt. Sie wird deshalb **nicht** nachgezogen und bleibt als Stand vom
2026-08-16 stehen.

### Isor's Tower Menü-Politur
```
URL      https://claude.ai/code/artifact/5d644461-e354-41e5-be11-9bfbed6c6f7d
Stand    2026-08-16 — Entwurfsstand, wird nicht nachgezogen
Quelle   Projekte/Isor_Tower/DECISIONS/UI.md, .../LOG.md
Skripte  MainMenuController, PauseMenuController, GameSettings, HudRoot
Seite →  keine
Seite ←  Kern/ARTIFACT_RULES.md, Abschnitt „Gestaltung"
```

---

## Gelöschte Seiten

Damit nachvollziehbar bleibt, warum eine ID ins Leere zeigt.

| ID | war | gelöscht | Rest |
|---|---|---|---|
| `cd2c6331-…` | Village spielbar | 2026-08-09 | Offline-Kopie `Seiten/2026-07-30-village-spielbar.html` |
| `0dd96ec7-…` | große Uni-Seite der Session 2026-07-16/17 | unbekannt | keine Kopie; Nachfolger nicht festgelegt |

---

Offene Punkte zu diesem Bestand stehen in `Kern/ROADMAP.md` — ein
Verzeichnis besitzt den Bestand, nicht die Arbeit daran.

Kein Stand-Stempel für den Index als Ganzes: Er hätte keine Prüfung, die
ihn kontrolliert, und war zuletzt zehn Tage falsch (`DOC_RULES.md`,
Abschnitt 7). Die Stempel der einzelnen Seiten bleiben — die prüft der
Sonntagsabgleich.
