# PREFAB_STATUS.md — Prüfstand der Prefabs

Ownership: Nur der Prüfstand jedes Prefabs — welche schon durchgesehen
sind und was dabei auffiel. **Keine Aufgabenplanung** (das ist ROADMAP
Punkt 10), **keine Begründungen** (DECISIONS.md), **kein Fertiges**
(FEATURE_LOG.md).

Zweck: Beim Aufräumen nach der Abgabe soll kein Prefab zweimal angefasst
werden. Isor entscheidet den Status, Claude trägt Befunde ein.

Status-Werte:
- `offen` — noch nicht angesehen
- `berührt` — inhaltlich geändert, Struktur aber nicht geprüft
- `geprüft` — Aufbau und Ablage angesehen, Befund notiert, nichts offen
- `Befund` — angesehen, etwas stimmt nicht (steht in der Spalte)

Stand: 2026-08-16. 33 Prefabs, ohne den TextMesh-Pro-Ordner.

## Shared/UI

| Prefab | Status | Befund |
|---|---|---|
| MainMenuUI | geprüft | Äußeres Prefab, `MainMenuPanel` und `OptionsPanel` liegen **darin** verschachtelt. 2026-08-16 aufgeräumt: `Apply All` an der Szenen-Instanz hatte alles hierher geschrieben statt in die inneren Vorlagen (595 → 1924 Zeilen). Über den Prefab-Modus dieses Prefabs an die inneren appliziert, danach 511 Zeilen — schlanker als zuvor, weil Unity dabei auch alte Abweichungen abgeräumt hat. **Lehre: An verschachtelte Prefabs kommt man nur über den Prefab-Modus des äußeren.** |
| MainMenuPanel | berührt | 2026-08-16 umgebaut (Tafel, Oswald, Fackel-Palette), Werte in der Vorlage angekommen (1054 → 1158 Zeilen). Ob es ein eigenes Prefab bleiben soll oder in MainMenuUI aufgehen kann: offen. |
| OptionsPanel | geprüft | 2026-08-16 umgebaut, Werte in der Vorlage angekommen (3437 → 3477 Zeilen). Wird von **beiden** Szenen genutzt. Die Dorf-Instanz hieß `OptionsPanel2` und wurde am selben Tag auf `OptionsPanel` zurückbenannt — Quelle unverändert `c121d007…`. Gewollte Abweichung im Dorf: Schleier auf Alpha 0, weil dort `PauseMenuRoot` die blockierende Ebene ist. |
| BackgroundPanel | berührt | 2026-08-16 vom blauen Farbfeld auf Dorf-Screenshot mit Aspect Ratio Fitter (Envelope Parent) umgestellt, in der Vorlage angekommen (77 → 92 Zeilen). |
| PausedMenuPanel | Befund | Vorlage selbst **unverändert** (1352 Zeilen, 0 Oswald). Der Umbau vom 2026-08-16 liegt als Abweichung in `PauseMenuRoot.prefab`, weil es dort als Kind hinzugefügt wurde. Funktioniert, weil das Dorf `PauseMenuRoot` lädt und das Hauptmenü dieses Panel nicht benutzt. Beim Aufräumen entscheiden, ob die Werte hierher gehören. Hat als einziges Panel `SelectOnHover` von Anfang an an allen vier Buttons. |
| PauseMenuRoot | berührt | 2026-08-16: 287 → 1264 Zeilen. Enthielt ursprünglich **nur ein Image** (den Schleier); `PausedMenuPanel` und `OptionsPanel` wurden erst in der Dorf-Instanz als Kinder hinzugefügt und sind durch das Apply hierher gewandert. Schleier steht auf Alpha 120. |
| VillageHud (ehem. VillageUI) | berührt | 2026-08-16 umbenannt und stark erweitert. Nach dem ersten Apply von 1407 auf 774 Zeilen geschrumpft, danach kam das komplette HUD dazu. Enthält `HudRoot`, `PauseMenuRoot` und `OptionsPanel` als verschachtelte Instanzen. |
| InGameUI | Befund | Das Objekt in der Szene heißt seit 2026-08-16 `HudRoot` und trägt das gesamte HUD (Fps, Crosshair, PlayerCard, ClockDisplay, TamedDisplay, TargetStatus, InteractablePromptRoot). **Das Prefab `InGameUI.prefab` heißt noch alt** — beim Aufräumen prüfen, ob es überhaupt noch benutzt wird oder verwaist ist. |
| EventSystem | offen | |

## Entities

| Prefab | Status | Befund |
|---|---|---|
| Player | offen | |
| SheepC | offen | Namensschema `C`/`N` ohne erkennbare Bedeutung — beim Durchgang klären. |
| SheepN | offen | siehe oben |
| Goblin | offen | Existiert bereits. Relevant für ROADMAP-Punkt 7 (Gegner über den Placer). |

## Environment

| Prefab | Status | Befund |
|---|---|---|
| Torch | Befund | Zwei Dateien, Unterschied nur ein Leerzeichen: `Torch .prefab` und `Torch.prefab`. Absicht laut Isor (2026-08-12) — eine ruhig, eine mit mehr Funken. Umbenennen steht in der ROADMAP. |
| Village | offen | |
| House | offen | |
| Graveyard | offen | |
| Moon | offen | |
| BirchTree_1 | offen | |
| GrassClumb_2Plane_Cross 1 | Befund | Leerzeichen und angehängte `1` im Namen. Zudem `Clumb` statt `Clump`. |
| GrassBush LOD_0 | Befund | Leerzeichen im Namen. |
| GrassSingle | offen | |
| GrassSingle_x2 | offen | |
| WaterPond | Befund | Drei Dateien: `WaterPond`, `WaterPond (1)`, `WaterPond (2)`. Klammer-Namen deuten auf Kopien — ob alle drei gebraucht werden, ist offen. |

## Systems

| Prefab | Status | Befund |
|---|---|---|
| ClestialPivot | Befund | Tippfehler im Namen — richtig wäre `CelestialPivot`. Umbenennen zieht die .meta-GUID mit, muss im Unity-Editor passieren. |
| DayNightCycle | offen | |
| GameController | offen | |
| MainMenuController | offen | |
| SheepHerdManager_01 | offen | Angehängte `_01` ohne zweite Fassung — Nummerierung prüfen. |
| NavMesh Water CutOut | Befund | Leerzeichen im Namen. |
