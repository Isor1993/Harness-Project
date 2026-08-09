# ARTIFACT_INDEX.md — Bestand der Artifact-Seiten

Ownership: Welche Artifact-Seiten es gibt, woran jede hängt und wer auf
sie zeigt. Regeln zu Typen, Benennung und Aufbau stehen in
ARTIFACT_RULES.md — hier steht nur der Bestand.

Wofür der Index gut ist: Beim Review-Gate (CODE_GUIDELINES.md) wird
geprüft, ob ein Skript, das gleich angefasst wird, in einer der
Skripte-Zeilen unten steht. Steht es dort, veraltet die Seite durch die
Änderung und muss nachgezogen werden.

Zeilen je Eintrag:
- **URL** — die Seite selbst. Nie eine zweite Seite zum selben Thema anlegen.
- **Stand** — Datum, gegen das die Seite zuletzt geprüft wurde.
- **Quelle** — die führende .md-Datei im Repo.
- **Skripte** — bei System-Seiten: was die Seite beschreibt. Ändert sich
  eines davon, ist die Seite veraltet. Bei Lernstücken heißt die Zeile
  **Beispiel** — die Seite erklärt ein übertragbares Konzept und nutzt
  diese Klassen nur als Beleg.
- **Seite →** — wohin die Seite selbst verlinkt.
- **Seite ←** — welche Knowledge-Notizen auf sie zeigen.

---

## 📍 Status

### 📍 Status · Wo das Projekt steht
```
URL      https://claude.ai/code/artifact/d5e30d97-fafd-4f9e-be83-e727df4d0405
Stand    2026-08-05
Quelle   ROADMAP.md
Skripte  keine — die Seite beschreibt den Projektstand, nicht Code
Seite →  (noch nicht erfasst)
Seite ←  keine
```

---

## ⚙️ System

### ⚙️ System · Terrain & Gras
```
URL      https://claude.ai/code/artifact/14256389-ed13-4e83-9fe1-e590b96b56d4
Stand    2026-08-06, Werkzeug-Abschnitt 2026-08-08
Quelle   FEATURE_LOG.md, DECISIONS.md
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
Stand    2026-08-06
Quelle   FEATURE_LOG.md, DECISIONS.md
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
Quelle   FEATURE_LOG.md, DECISIONS.md
Skripte  TamedSheepReference (SO), SheepInteractable, Sheep, PlayerInteractor,
         IInteractable, FollowPlayerState
Seite →  (noch nicht erfasst)
Seite ←  Patterns/validierung-beim-lesen.md
```

---

## 💡 Lernstück

### 💡 Lernstück · Multithreading in Unity
```
URL      https://claude.ai/code/artifact/f9d2635f-431b-4f60-90fc-dca3151cd51f
Stand    2026-08-05
Quelle   TDD_NOTES.md, Knowledge-Ordner
Beispiel ObjectPlacer, CurveLookup, ExclusionArea, PlacementExclusionFilter,
         GrassCellBuilder
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · Poisson-Disc-Sampling
```
URL      https://claude.ai/code/artifact/2a5340fb-b4de-4326-be1a-c330767d8fdb
Stand    2026-08-06
Quelle   TDD_NOTES.md, Knowledge-Ordner
Beispiel ObjectPlacer
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/poisson-disc-verteilung.md
         (dort auch Offline-Kopie Seiten/2026-07-23-poisson-disc.html)
```

### 💡 Lernstück · GPU-Instancing
```
URL      https://claude.ai/code/artifact/0183966d-3132-4804-af82-83591ffe5f09
Stand    2026-08-06
Quelle   TDD_NOTES.md, Knowledge-Ordner
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
Quelle   TDD_NOTES.md, Knowledge-Ordner
Beispiel MeshBuilder, HeightmapGenerator
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/chunk-nahtlose-normalen.md
```

### 💡 Lernstück · Input-Reader
```
URL      https://claude.ai/code/artifact/20be8fc5-f9bf-4d49-8af5-bab3247bb6e3
Stand    2026-08-06
Quelle   TDD_NOTES.md, Knowledge-Ordner
Beispiel PlayerInputReader, PlayerControls (.inputactions), GameController
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · EditorWindow & MVP
```
URL      https://claude.ai/code/artifact/415afd2f-e1f4-4e9d-9517-0b8585f74ac6
Stand    2026-08-08
Quelle   TDD_NOTES.md, Knowledge-Ordner
Beispiel TerrainToolWindow, TerrainToolPresenter,
         PrefabPainterWindow, PrefabPainterPresenter
Seite →  System · Terrain & Gras
Seite ←  Patterns/mvp-model-view-presenter.md,
         Unity/editor-scripting-editorwindow.md
```

---

## Gelöschte Seiten

Damit nachvollziehbar bleibt, warum eine ID ins Leere zeigt.

| ID | war | gelöscht | Rest |
|---|---|---|---|
| `cd2c6331-…` | Village spielbar | 2026-08-09 | Offline-Kopie `Seiten/2026-07-30-village-spielbar.html` |
| `0dd96ec7-…` | große Uni-Seite der Session 2026-07-16/17 | unbekannt | keine Kopie; Nachfolger nicht festgelegt |

---

## Offene Punkte

- Die Zeile **Seite →** ist erst bei drei Seiten gefüllt. Der Rest wird
  nachgetragen, wenn die jeweilige Seite das nächste Mal angefasst wird —
  nicht in einem eigenen Durchgang.
- Für `0dd96ec7-…` ist nicht entschieden, welche heutige Seite sie
  beerbt. Die zwölf Knowledge-Notizen tragen deshalb nur noch die
  Session-Angabe ohne Link.

Stand dieses Index: 2026-08-09.
