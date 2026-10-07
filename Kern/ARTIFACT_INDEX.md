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
- **Ruht** — die Seite beschreibt den ruhenden Unity-Altstand und steht
  bis zum Kontrollpunkt der Stack-Entscheidung außerhalb der gründlichen
  Prüfung (`ARTIFACT_RULES.md` → „Wann geschaut wird"). Die Zeile nennt
  nur das Datum.
- **Geprüft** — Datum der letzten gründlichen Prüfung am Pflegetag.
  Fehlt die Zeile, wurde die Seite nie gründlich geprüft und ist als
  Nächstes dran (`ARTIFACT_RULES.md` → „Wann geschaut wird"). Bei
  `Ruht`- und `Abgeschlossen`-Seiten entfällt sie.
- **Bekannt** — eine Abweichung zwischen Index und veröffentlichter
  Seite, die Isor bewusst liegen lässt. Der Abgleich meldet sie nicht
  erneut.
- **Abgeschlossen** — die Seite gehört zu einem abgegebenen Projekt und
  steht dauerhaft außerhalb der gründlichen Prüfung, wird nicht
  nachgezogen (`ARTIFACT_RULES.md` → „Wann geschaut wird"). Die Zeile
  nennt das Abgabedatum.

---

## 📍 Status  — Schicht: Uni

### 📍 Status · Semester 3
```
URL      https://claude.ai/code/artifact/990b0be5-f2ec-42e2-affe-858d1cc92208
Stand    2026-10-07 — nachgezogen am Pflegetag: Neuausrichtung vom
         01.10. als eigener Abschnitt (vier Karten: nur Spielprojekt
         benotet, Viewer minimal, Engine-Entscheidung bis 02.11.,
         eigenständiges Spiel), Zeitstrahl um Game Jam, frühe
         Viewer-Abgabe, Hands-on und Entscheidungstermin ergänzt,
         Kontrollpunkt vom 22.11. auf den 02.11. verlegt, Lane Defender
         als abgegeben (03.10.) markiert, Kacheln neu, Phasen 1–3
         nachgezogen. Termine darüber hinaus unverändert vom 14.09.
Löst ab  `📍 Status · Wo das Projekt steht` (seit 2026-09-11; die Seite
         ist inzwischen gelöscht — Tabelle unten)
Geprüft  2026-10-07 — gegen Uni/ROADMAP.md, die vier DECISIONS vom
         01.10. und STUNDENPLAN.md
Quelle   Uni/ROADMAP.md (Phasenplan), Uni/DECISIONS.md,
         Uni/Semester_3/STUNDENPLAN.md
Skripte  keine — die Seite zeigt Termine und Plan, nicht Code
Seite →  keine
Seite ←  keine
```

---

## 📍 Status  — Schicht: Projekt (Lane Defender)

Alle vier Seiten sind **abgeschlossen** — Lane Defender ist am
2026-10-03 abgegeben (Entscheidung `DECISIONS.md`, 2026-10-07).

### 📍 Status · Lane Defender M2-Design
```
URL      https://claude.ai/artifact/FbqHW5wq6Ay2szchXe7R3j
Stand    2026-09-20 — neu, gebaut im M2-Design-Abschnitt: Screen
         „Gerahmt" mit beiden Spielstufen als Render, Zeilenbudget,
         Feldbreiten je Stufe, Sprite, Schuss-Symbol und der
         kbhit-Baustein samt Tick-Reihenfolge
Abgeschlossen 2026-10-03
Bekannt  Titel draußen „Lane Defender M2" (ohne Symbol, Typwort und
         „-Design"), zuletzt veröffentlicht am 21.09. statt 20.09. —
         Abgleich 2026-10-07, bleibt so
Quelle   Projekte/Lane_Defender/DECISIONS.md (sieben Einträge vom
         2026-09-20), Projekte/Lane_Defender/ROADMAP.md (M2)
Skripte  keine — die Seite zeigt den Design-Stand, nicht Code
Seite →  keine
Seite ←  📍 Status · Lane Defender M3-Design (Fußzeile); die
         M2-Stand-Zeile der Lane-Defender-ROADMAP nennt die URL
```

### 📍 Status · Lane Defender M3-Design
```
URL      https://claude.ai/artifact/FMZX3wJ2Lh43GpvpyXccK4
Stand    2026-09-27 — neu, gebaut im M3-Design-Abschnitt: Klassenbaum
         der Gegner (Tafel 1), Spawn-Schritt im Tick (Tafel 2),
         delete-vor-erase-Merksatz, Figuren-Zuordnung und die
         Bausteine B1–B3
Abgeschlossen 2026-10-03
Quelle   Projekte/Lane_Defender/DECISIONS.md (vier Einträge vom
         2026-09-27), Projekte/Lane_Defender/ROADMAP.md (M3)
Skripte  keine — die Seite zeigt den Design-Stand, nicht Code
Seite →  📍 Status · Lane Defender M2-Design (Fußzeile)
Seite ←  📍 Status · Lane Defender M4-Design (Fußzeile); die
         M3-Stand-Zeile der Lane-Defender-ROADMAP nennt die URL
```

### 📍 Status · Lane Defender M4-Design
```
URL      https://claude.ai/artifact/7Dp5vCLrjoh7YCtneSoBut
Stand    2026-09-28 — neu, gebaut im M4-Design-Abschnitt: Tick mit
         beiden Kollisions-Prüfungen (Tafel 1), Feuerraten-Tabelle,
         Shop-Preise samt Wirkungen, Startwert-Kacheln, HUD-Vorzug
         und die Bausteine B1–B3
Abgeschlossen 2026-10-03
Quelle   Projekte/Lane_Defender/DECISIONS.md (vier Einträge vom
         2026-09-28), Projekte/Lane_Defender/ROADMAP.md (M4)
Skripte  keine — die Seite zeigt den Design-Stand, nicht Code
Seite →  📍 Status · Lane Defender M3-Design (Fußzeile)
Seite ←  📍 Status · Lane Defender M5-Design (Fußzeile) und
         💡 Lernstück · Tick-Kollision (Fußzeile); die M4-Stand-Zeile
         der Lane-Defender-ROADMAP nennt die URL
```

### 📍 Status · Lane Defender M5-Design
```
URL      https://claude.ai/artifact/Gmwkzh85XeR8AEHnFqDrgh
Stand    2026-09-30 — neu, gebaut im M5-Design-Abschnitt:
         Boss-Werte-Tabelle samt Durchbruch-Regel, Slot-Diagramm
         (Zeiger und Heap), Entweder-oder-Feuer-Ablauf,
         [4]-Kauf-Kette, das vierte delete, Balance-Datei-Schnitt
         und die Bausteine B1–B2
Abgeschlossen 2026-10-03
Bekannt  Titel draußen „Lane Defender M5" — wie M2, Abgleich
         2026-10-07, bleibt so
Quelle   Projekte/Lane_Defender/DECISIONS.md (sechs Einträge vom
         2026-09-30), Projekte/Lane_Defender/ROADMAP.md (M5)
Skripte  keine — die Seite zeigt den Design-Stand, nicht Code
Seite →  📍 Status · Lane Defender M4-Design (Fußzeile)
Seite ←  die M5-Stand-Zeile der Lane-Defender-ROADMAP nennt die URL
```

---

## 🎓 Zeugnis  — Schicht: Kern

**Kein vierter Typ** — die Seiten gehören zum Session-Typ „Zeugnis"
(WORKFLOW.md) und werden von ASSESSMENT_RULES.md geregelt. Hier stehen
sie nur, damit keine URL unerklärt bleibt. Abweichend vom übrigen
Bestand: Jedes Zeugnis behält seine eigene URL und wird **nie
nachgezogen** — der alte Stand ist der halbe Zweck. Beim Review-Gate
sind diese Seiten deshalb zu überspringen.

### 🎓 Zeugnis · 2026-09-30, Lane Defender
```
URL      https://claude.ai/artifact/2PCvp9a5HBxQQvEXYStJBZ
Datum    2026-09-30 — zwei Tage vor der Abgabe, Gegenstand Lane
         Defender (Isors Zuruf); viertes Zeugnis, wird nie
         nachgezogen
Quelle   Kern/Zeugnisse/2026-09-30.md
Seite →  keine
Seite ←  keine
```

### 🎓 Zeugnis · 2026-09-04, Semesterstart
```
URL      https://claude.ai/code/artifact/90fec556-66a8-41ef-90ec-fa959bd5ad6b
Datum    2026-09-04 — nach Phase 0 und Baustein B, Schritt 4; drittes
         Zeugnis, wird nie nachgezogen
Quelle   Kern/Zeugnisse/2026-09-04.md
Seite →  keine
Seite ←  keine
```

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
Stand    2026-08-24 — nachgezogen, im Paar mit GPU-Instancing:
         Hausfarbwelt (Neubau aus der blaugrauen Fassung), die
         OnEnable-Aussage durch EnsureHeightCurveLookup ersetzt,
         Gras-Zellen-Zeile auf 32 m / LOD-Einheit korrigiert,
         GrassInteraction und GrassLodLevel ergänzt, Ladebalken als
         gebaut markiert, ShoreMargin-0-Hinweis, 190.000 als Messstand
         datiert und gegen die 211.000-Baseline abgegrenzt.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
Skripte  TerrainConfig, HeightmapGenerator, PlateauModifier, MeshBuilder,
         CurveLookup, Placeable, ObjectPlacer, Placement, PlacementMetrics,
         DensityStrategy, PlacementExclusion, ExclusionArea,
         PlacementExclusionFilter, PlaceableRenderMode,
         RuntimePlacementSpawner, GrassCellBuilder, GrassCell,
         GrassRenderProfile, GrassLodSelector, GrassLodLevel,
         GrassInteraction, InstancedRenderer,
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
Stand    2026-08-24 — Neubau nach der Teilung: behält Spielablauf,
         Szenen, Input und Interaktion; Tag-Nacht, Herde und Kampf
         wohnen jetzt auf „Welt & Überleben". Alle Pfade und Klassen
         gegen den Code gebaut; Player.cs ist ehrlich als leere Hülle
         ausgewiesen, der Audio-Plan (AudioManager/SceneMusic) ist
         raus — gebaut wurde Audio anders (FootstepPlayer u.a.).
Überholt Schritt 5 (2026-09-06) erweitert den Menüfluss: MainMenuController
         füttert jetzt LobbyPanel (Zähler, Rollen, Gast-Name); neu sind
         LobbyPlayer, LobbyPlayerSpawner, LobbyPlayerRow, LobbyPanel und
         ISessionService.MaxPlayers. Beim Nachziehen mit aufnehmen.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
Skripte  SceneLoader, LoadingScreenController, GameController,
         MainMenuController, Player, PlayerMotor, PlayerLook,
         PlayerInteractor, PlayerControls (.inputactions),
         PlayerInputReader, FootstepPlayer, RigidbodyPusher,
         IInteractable, SheepInteractable, TorchInteractable, Torch,
         GameSettings, SelectOnHover, InteractionPromptView,
         TargetStatusDisplay
Seite →  System · Welt & Überleben, System · Nur ein Schaf zähmbar,
         System · Terrain & Gras, Lernstück Input-Reader
Seite ←  keine
```

### ⚙️ System · Welt & Überleben
```
URL      https://claude.ai/code/artifact/2efff1de-8063-4824-9a96-4589e2e82899
Stand    2026-08-24 — neu, abgespalten aus „Grundgerüst" (Entscheidung
         Kern/DECISIONS.md, 2026-08-24). Ehrlich ausgewiesen: Goblin
         ist Platzhalter, das Schadenssystem hat Verträge, aber noch
         keinen Angreifer; Verhungern ist der einzige laufende
         Schadensweg.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
         (Entities.md, Welt.md)
Skripte  IngameTime, DayNightCycle, DayNightCycleEventManager,
         SkyController, TimeFastForward, NightVfx, IDayNightListener,
         Sheep, SheepSense, SheepHunger, SheepHealth,
         SheepMoveBehaviour, SheepDodgeBehaviour, DodgeBehaviourBase,
         SheepFSM, SheepStateBase, SheepStateSettings,
         SheepAnimatorParameters, die elf Zustands-Klassen unter
         SheepFSM/States, HerdManager, Health, IDamageable, DamageType,
         HealthBarDisplay, Goblin, Timer, IResumeTargetState,
         RandomIntervalSound, DayTimeDisplay, TamedSheepDisplay,
         FpsDisplay, Torch
Seite →  System · Grundgerüst, System · Nur ein Schaf zähmbar
Seite ←  keine
```

### ⚙️ System · Nur ein Schaf zähmbar
```
URL      https://claude.ai/code/artifact/12ef2f34-c7f5-4e79-9798-a60edab85c02
Stand    2026-08-24 — nachgezogen: Hausfarbwelt (Neubau aus der
         moosgrünen Fassung), vierte Frage (IsAsleep) in Flow, Code und
         Durchspiel-Tabelle samt der Nacht-Zeile, die belegt, warum die
         Reihenfolge trägt; FSM-Lesestellen auf vier korrigiert;
         neu StatusText/Zähm-Laut und der Commander als Herdenanker
         (HerdManager); Fußzeilen-Pfade auf die echten Orte.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/LOG.md und .../DECISIONS/
Skripte  TamedSheepReference (SO), SheepInteractable, Sheep, PlayerInteractor,
         IInteractable, FollowPlayerState, HerdManager
Seite →  (noch nicht erfasst)
Seite ←  Patterns/validierung-beim-lesen.md
```

### ⚙️ System · Multiplayer
```
URL      https://claude.ai/code/artifact/cc012a9e-ec18-46ba-a4b3-14d294bbbdee
Stand    2026-08-26 — neu aus der Design-Session vom 25./26.08.
Zustand  **geplant** — die Seite beschreibt Absicht, nicht Zustand;
         gebaut ist davon nichts. Seit dem 2026-08-26 ist das kein
         Behelf mehr, sondern geregelt: `(geplant)` ist ein Zustand,
         kein eigener Typ (`ARTIFACT_RULES.md` → „Die Typen"). Im
         Turnus würde sie gegen die führende Quelle geprüft statt gegen
         Code. Pflegetag 2026-09-11: Die Absicht ist von der
         Stack-Entscheidung überholt (`Uni/DECISIONS.md`, 2026-09-07) —
         sie plant NGO in Unity; die engine-neutralen Design-Fragen
         daraus stehen in `Projekte/Isor_Tower/ROADMAP.md`.
Ruht     seit 2026-09-11
Titel    Draußen steht nur `Multiplayer` — ohne Symbol, Typwort und
         Klammer (Abgleich 2026-09-11; der frühere Vermerk nannte
         `⚙️ System · Multiplayer`, das stimmte nicht). Nachgezogen beim
         nächsten inhaltlichen Anfassen: Ein Neubau der ganzen Seite
         allein für den Titel lohnt nicht.
Quelle   Projekte/Isor_Tower/DECISIONS/Multiplayer.md, .../ROADMAP.md,
         .../GDD.md
Skripte  beschreibt keinen gebauten Code. Gemessen wurde gegen den
         Bestand: PlayerInputReader, PlayerMotor, PlayerLook,
         PlayerInteractor, GameController, TimeFastForward,
         RuntimePlacementSpawner, InstancedRenderer, TerrainConfig
Seite →  Lernstück Netzwerkgrundlagen, Lernstück NGO-Bausteine
Seite ←  keine
```

### ⚙️ System · Lobby-Tafel
```
URL      https://claude.ai/code/artifact/c57234c7-9e7c-4e9c-b49d-1ced0ccbf5b9
Stand    2026-09-04 — gebaut am 01.09. für die Layout-Entscheidung der
         Lobby, am 04.09. um den Maßstabsvergleich gegen 1920×1080
         ergänzt. Offline-Kopie: Knowledge/Seiten/2026-09-01-lobby-tafel.html
Zustand  **teils geplant** — die Host-Optionen-Tafel ist seit dem 04.09.
         gebaut und getestet; die Lobby-Ansicht (Spielerliste, Chat mit
         Scroll-Verlauf) ist Entwurf und Bauvorlage für Schritt 5.
Überholt Schritt 5 ist am 2026-09-06 gebaut (LOG.md) — die Spielerliste
         existiert jetzt als Code und weicht im Detail ab (Host-Zeile,
         Haken per Sichtbarkeit, Rollen-Knopfpaar); der Chat bleibt
         Entwurf. Nachziehen beim nächsten Anfassen bzw. Pflegetag.
Titel    Draußen heißt sie „Die Lobby-Tafel" — benannt, bevor die Seite
         ins Register kam. Nachgezogen beim nächsten inhaltlichen
         Anfassen (Schritt 5), wie beim Multiplayer-Präzedenzfall.
Bekannt  Die Veröffentlichungsliste nennt den 01.09. als letzten Stand,
         nicht den 04.09. Der Maßstabsvergleich gegen 1920×1080 steht
         trotzdem auf der Seite (abgerufen 2026-10-07) — nur das Datum
         weicht ab, der Inhalt nicht. Bleibt so.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/DECISIONS/UI.md (Einträge vom 29.08. und
         01.09.)
Skripte  beschreibt UI-Entwurf, keinen Code. Die Maße sind gegen
         HostOptionsPanel.cs und die Szene geprüft (szene_pruefen.py).
Seite →  keine
Seite ←  keine
```

### ⚙️ System · Szenenwechsel & Lobby
```
URL      https://claude.ai/code/artifact/19033944-8b4c-4308-a19d-f59c169df3bf
Stand    2026-08-30 — Baustand des Kerns von Baustein B (Design am
         29.08., gebaut und getestet am 30.08.). Nachgetragen am
         2026-09-11: Beim Abgleich stand die Seite in keinem Register.
Titel    Draußen heißt sie „Szenenwechsel & Lobby" — ohne Symbol und
         Typwort. Nachgezogen beim nächsten inhaltlichen Anfassen, wie
         bei der Lobby-Tafel.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/DECISIONS/UI.md, .../DECISIONS/Multiplayer.md
Skripte  laut Seite: MultiPlayerPanel, JoinPanel, LobbyPanel, LobbyPlayer,
         ISessionService, LoadingScreenController, SelectOnHover
Seite →  keine
Seite ←  keine direkt; Unity/ngo-szenenwechsel-ladebalken.md und
         Unity/ngo-lobby-objekt-je-spieler.md nennen die Design-Session
         vom 2026-08-29 ohne Link
```

---

## 💡 Lernstück  — Schicht: Kern (übertragbar)

### 💡 Lernstück · Multithreading in Unity
```
URL      https://claude.ai/code/artifact/f9d2635f-431b-4f60-90fc-dca3151cd51f
Stand    2026-08-24 — nachgezogen: Hausfarbwelt (Neubau aus der hellen
         Fassung, jetzt eine Fassung ohne Hell-Modus), fünfte Falle
         (SO-OnEnable-Reihenfolge, gegen TerrainConfig.cs und
         ObjectPlacer.cs verifiziert) samt geschärftem Merksatz,
         Anzahl aus der Fallen-Überschrift entfernt, Fußzeile nennt
         LOG.md statt FEATURE_LOG und die führende Quelle.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel ObjectPlacer, CurveLookup, ExclusionArea, PlacementExclusionFilter,
         GrassCellBuilder
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · Poisson-Disc-Sampling
```
URL      https://claude.ai/code/artifact/2a5340fb-b4de-4326-be1a-c330767d8fdb
Stand    2026-10-07 — gründliche Prüfung des Pflegetags, vier Befunde
         nachgezogen: Gras-Radius 0,6 → 0,5 m samt Gitter (5793², 134 MB;
         je Kachel 725², 2,1 MB — die Korrektur aus TDD_NOTES vom 08.08.
         war am 24.08. nicht übernommen worden), Messtabelle als Spalte
         „Erzeugen + Filtern" benannt und um die 10,1-s-Zeile ergänzt
         (die 8,8 s enthalten den entschärften Ausschlussfilter), Kopf-
         Kacheln auf Birke 9,47 m je 256-m-Kachel statt 5 m global,
         Seed-Satz auf „je Kachel ein Generator" geschärft.
         Vorher: 2026-08-24, Hausfarbwelt und Projekt-Kasten.
Geprüft  2026-10-07 — gegen ObjectPlacer.cs, TerrainConfig_Default.asset,
         TDD_NOTES.md und TDD.md (Messreihe)
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel ObjectPlacer
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/poisson-disc-verteilung.md
         (dort auch Offline-Kopie Seiten/2026-07-23-poisson-disc.html)
```

### 💡 Lernstück · GPU-Instancing
```
URL      https://claude.ai/code/artifact/0183966d-3132-4804-af82-83591ffe5f09
Stand    2026-08-24 — nachgezogen, im Paar mit Terrain & Gras: beide
         Widersprüche aufgelöst. Die 143-m-Herleitung bleibt als
         datierte Rechnung stehen, ein neuer Kasten erklärt die
         gebauten 32 m über den Engpass-Wechsel zu Dreiecken
         (TDD_NOTES 04.08.) und die Zelle als LOD-Einheit; 211.000 und
         190.000 sind als verschiedene Messstände ausgewiesen. LOD- und
         Render-Distanz stehen jetzt auf der Seite. Hausfarbwelt, die
         vier Diagramme über Klassen-Variablen mitgefärbt; Quellenzeile
         ergänzt.
Geprüft  2026-08-24 — Durchsicht des Altbestands vom 23.08., Befunde am
         24.08. nachgezogen. Beispiel-Code seitdem unverändert (git,
         Abgleich 2026-10-07)
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
Stand    2026-08-24 — nachgezogen: Hausfarbwelt (Palettentausch, SVGs
         über CSS-Variablen mitgefärbt), Regel-Kopf mit Stand-Stempel,
         Überholt-Kasten trägt die heutigen Asset-Werte samt der
         Wasser-Absicht (DECISIONS/Terrain_Mesh.md), Fußzeile nennt die
         führende Quelle. Erste Altbestand-Seite im Hausstil.
Geprüft  2026-08-24 — wie GPU-Instancing; Beispiel-Code seitdem
         unverändert (git, Abgleich 2026-10-07)
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel MeshBuilder, HeightmapGenerator
Seite →  (noch nicht erfasst)
Seite ←  ProcGen/chunk-nahtlose-normalen.md
```

### 💡 Lernstück · Input-Reader
```
URL      https://claude.ai/code/artifact/20be8fc5-f9bf-4d49-8af5-bab3247bb6e3
Stand    2026-08-24 — nachgezogen: Hausfarbwelt (Neubau aus der hellen
         Fassung), die canceled-Aussage umgedreht und als Korrektur-
         Kasten mit dem echten EnableUI-Code belegt, Kette zeigt beide
         Maps, neu die gehaltene Taste (ReadValueAsButton) und der
         Beleg des normalized-Beispiels in PlayerMotor.Move().
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel PlayerInputReader, PlayerControls (.inputactions), GameController
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · EditorWindow & MVP
```
URL      https://claude.ai/code/artifact/415afd2f-e1f4-4e9d-9517-0b8585f74ac6
Stand    2026-09-11 — erste gründliche Prüfung des Pflegetags, danach
         Neubau im Hausstil: „niemals `using UnityEditor`" auf „nur
         hinter `#if UNITY_EDITOR`" korrigiert (Beleg
         `GameController.QuitGame`), der direkte Blick der View aufs
         Model in Tafel und Text, der Prefab-Painter als lockerer
         gesetzter Schnitt ausgewiesen, die Model-Zeile um ObjectPlacer,
         PlacementExclusionFilter und InstancedRenderer ergänzt.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/TDD_NOTES.md, Knowledge-Ordner
Beispiel TerrainToolWindow, TerrainToolPresenter,
         PrefabPainterWindow, PrefabPainterPresenter, GameController
Seite →  System · Terrain & Gras
Seite ←  Patterns/mvp-model-view-presenter.md,
         Unity/editor-scripting-editorwindow.md
```

### 💡 Lernstück · Netzwerkgrundlagen
```
URL      https://claude.ai/code/artifact/1cb76a6f-f73f-420b-9781-35135354eb16
Stand    2026-08-26 — umbenannt (hieß „Multiplayer von Null") und um
         einen Nachtrag-Kasten ergänzt. Inhalt vom 2026-08-23,
         ungeprüft geblieben.
Herkunft Entstand am 2026-08-23 in einem Vorlauf **ohne Harness** und
         war deshalb bis heute in keinem Register. Titel und Nachtrag
         nachgezogen, der Lehrstoff unverändert.
Überholt Zwei Punkte, im Nachtrag-Kasten benannt: die Annahme eines neu
         aufgesetzten Projekts (entschieden wurde: gleiches Repo) und
         die Zeitschätzung, die nur die Netzwerkschicht rechnet.
Stil     Steht weiter in ihrer eigenen blaugrauen Fassung, nicht in der
         Hausfarbwelt — bewusste Abweichung von ARTIFACT_RULES →
         „Der Altbestand": Ein Neubau von 100 KB Lehrtext war der
         Umbenennung nicht angemessen. Fällig beim nächsten
         inhaltlichen Anfassen.
Bekannt  Gründlich geprüft am 2026-10-07, nicht nachgezogen (Isor: ruht
         wie NGO-Bausteine). Der Lehrstoff hält (UDP/TCP, Authority,
         Topologien, Relay, die meisten Zahlen). Offen:
         - Rechenfehler: „40 Objekte mehr, die Verbindung bricht" —
           tatsächlich ≈ 3,7 Mbit/s, 37 % von 10 Mbit/s.
         - Fall A ohne die 30 B Verpackung gerechnet (≈ 0,09 statt
           0,06 Mbit/s).
         - Der Nachtrag-Kasten nennt Punkte der NGO-Seite und die Seite
           `⚙️ Multiplayer` als führend.
         - Prediction, Determinismus, async-Backend und öffentliche
           Lobby sind vom Design 25.–28.08. überholt.
         - Unity/NGO ist von der Stack-Entscheidung überholt.
         Am Kontrollpunkt 02.11. mitentscheiden.
Ruht     seit 2026-10-07
Quelle   Projekte/Isor_Tower/DECISIONS/Multiplayer.md → „Verhältnis zum
         Vorlauf vom 2026-08-23/24"
Beispiel erklärt Netzwerktechnik allgemein: Latenz, Tick, UDP gegen TCP,
         Authority, Topologien, Relay und Lobby
Seite →  (noch nicht erfasst)
Seite ←  keine
```

### 💡 Lernstück · NGO-Bausteine
```
URL      https://claude.ai/code/artifact/7fa5f368-d3ee-4635-8e08-f87ce1b230a9
Stand    2026-08-26 — umbenannt (hieß „Multiplayer bauen") und um einen
         Nachtrag-Kasten ergänzt. Inhalt vom 2026-08-24, ungeprüft
         geblieben.
Herkunft wie die Seite darüber: Vorlauf ohne Harness, bis heute in
         keinem Register.
Überholt Der Umbauplan in Etappe 14 geht von einem neu aufgesetzten
         Projekt aus; entschieden wurde ein Neustart **im selben Repo**.
         Im Nachtrag-Kasten benannt.
Stil     wie die Seite darüber — eigene Fassung, nicht Hausfarbwelt.
Ruht     seit 2026-09-11
Quelle   Projekte/Isor_Tower/DECISIONS/Multiplayer.md → „Verhältnis zum
         Vorlauf vom 2026-08-23/24"
Beispiel vierzehn Etappen durch die NGO-Bausteine: NetworkObject,
         Ownership, NetworkVariable, RPC, Session, Determinismus
Seite →  Lernstück Netzwerkgrundlagen
Seite ←  keine
```

---

## 💡 Lernstück  — Schicht: Uni

### 💡 Lernstück · SAE-C++-Konventionen
```
URL      https://claude.ai/code/artifact/5ea67ac8-e377-46ba-8920-d21ef5508131
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-09-08 — neu, gebaut im Zug der Guidelines-Einpflege; Inhalt
         aus dem SAE-PDF (Version 05.09.2022) und den C++-Abschnitten
         der CODE_GUIDELINES vom selben Tag. Geltung am 2026-09-11
         nachgezogen (Pflegetag): auch der 3D-Model-Viewer
         (Dozenten-Auskunft vom 10.09.); der L1-Kasten „Heute Abend" ist
         durch eine Geltungstafel ersetzt.
Quelle   Kern/CODE_GUIDELINES.md → „C++ — welche Konvention wo gilt" und
         „C++ · Konsolenprojekt — SAE-Konvention (Pflicht)"; Original-PDF
         im Datenbaum unter 01_Uni\_Regelwerk\ (Kern/PFADE.md → DATENBAUM)
Beispiel keine Projekt-Klassen — die Code-Beispiele der Seite (CPlayer)
         sind synthetisch nach SAE-Muster. Angewandt: Lane Defender,
         Abgabestand (Release-Build 1.0.0, Repo V 0.0014), und Model-Viewer
Geprüft  2026-10-07 — gegen CODE_GUIDELINES, das SAE-PDF und Stichproben
         im Code; nachgezogen: Englisch gilt auch für Ausgaben,
         Debug-Kachel abgeschwächt (0xCC oder 0)
Seite →  keine
Seite ←  Cpp/sae-cpp-konventionen.md
         (dort auch Offline-Kopie Seiten/2026-09-08-sae-cpp-konventionen.html)
```

### 💡 Lernstück · Pointer & Referenzen
```
URL      https://claude.ai/code/artifact/38a61247-8221-4115-a5af-79822f94c5e9
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-09-13 — neu, gebaut nach Abschluss des Lern-Vorlaufs L3
         (Lane Defender): zwei Tafeln — Zettel tauschen gegen Haus
         besuchen, by value gegen const-Referenz — dazu nullptr-Wächter,
         die drei Pointer-Einsatzfälle und die Kostenregel als Tabelle.
         Offline-Kopie: Seiten/2026-09-13-cpp-pointer-referenzen.html
Quelle   Knowledge-Ordner: Cpp/pointer-hat-nie-den-wert.md und
         Cpp/referenz-reicht-die-hausnummer-durch.md
Beispiel Lane Defender, Abgabestand (Release-Build 1.0.0, Repo V 0.0014)
         — Output.h (PrintMessage auf const std::string&), Player.h
         (CSkill* m_pSkill), GameScene.cpp (vector<CEnemy*>, Wächter im
         Feuer-Zweig); dazu die L3-Übungen vom 12./13.09.
Geprüft  2026-10-07 — acht Befunde nachgezogen, darunter einer falsch:
         Der Skill-Slot hieß SpecialAttack* und galt als „vor dem ersten
         Boss-Sieg leer"; tatsächlich CSkill*, gefüllt per [4]-Kauf
Seite →  Lernstück C++-Funktionen & Überladung,
         Lernstück SAE-C++-Konventionen
Seite ←  Cpp/pointer-hat-nie-den-wert.md,
         Cpp/referenz-reicht-die-hausnummer-durch.md
```

### 💡 Lernstück · C++-Funktionen & Überladung
```
URL      https://claude.ai/code/artifact/1a3f534c-2b97-4f84-a81e-13ca4211f227
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-09-11 — neu, gebaut beim Abschluss von L2 Ü3 (Lane
         Defender): drei Tafeln — Wertübergabe by value, Prototyp gegen
         Definition (Semikolon), Überladungswahl mit der bool→1-Falle;
         dazu Default-Argumente und die double-Literal-Falle.
         Offline-Kopie: Seiten/2026-09-11-cpp-funktionen-ueberladung.html
Quelle   Knowledge-Ordner: Cpp/funktionen-bekommen-kopien.md und
         Cpp/ueberladung-nimmt-den-billigsten-weg.md
Beispiel Lane Defender, Abgabestand (Release-Build 1.0.0, Repo V 0.0014)
         — Output.h/Output.cpp; der LoseLives-Kasten und Tafel 3 als
         historischer Ü3-Stand (Commit e822709, 11.09.) gekennzeichnet
Geprüft  2026-10-07 — sieben Befunde nachgezogen: Code-Ort, Referenz-
         Ausnahme bei by value, Ränge nach dem Standard (Exact Match /
         Promotion / Conversion), Default-Argumente zählen bei der
         Anzahl mit. Der Überholt-Vermerk vom 13.09. ist damit erledigt
Seite →  Lernstück SAE-C++-Konventionen
Seite ←  Cpp/funktionen-bekommen-kopien.md,
         Cpp/ueberladung-nimmt-den-billigsten-weg.md
```

### 💡 Lernstück · Tick-Kollision
```
URL      https://claude.ai/artifact/VavXTzq3k7XjqsaaXm2QD9
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-09-29 — neu, gebaut als Erklär-Runde vor der
         M4-B2-Abnahme (Lane Defender): Tick-Reihenfolge mit beiden
         Prüfungen (Tafel 1), HandleCollisions als Treffer-Kette
         samt echtem Code (Tafel 2), die Platztausch-Falle gefangen
         gegen durchgetunnelt (Tafeln 3a/3b), Zahlen-Kacheln und
         der F5-Testbogen der Abnahme
Quelle   Knowledge-Ordner: Cpp/in-ticks-tunnelt-die-kollision.md
Beispiel Lane Defender, Abgabestand (Release-Build 1.0.0, Repo V 0.0014)
         — GameScene.cpp (HandleCollisions, Tick-Doppelruf) und Balance.h
Geprüft  2026-10-07 — Tafel 1 auf zwölf Stationen, Durchbruch-Preis je
         Gegner (Boss 5), Takt aus der Level-Tabelle, Tafel 3b neu: Sie
         zeigte einen Fall, den Prüfung 2 fängt, statt des echten
         Platztauschs, den nur Prüfung 1 fängt. Knowledge-Notiz: das
         Stepper-Versprechen auf feste Tafeln korrigiert
Seite →  📍 Status · Lane Defender M4-Design (Fußzeile)
Seite ←  Cpp/in-ticks-tunnelt-die-kollision.md
```

### 💡 Lernstück · Kompiliervorgang & Präprozessor
```
URL      https://claude.ai/artifact/2uiZN5dDKHy7qBzV1HEX1g
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-10-05 — neu, gebaut im Kurz-Konsult zu C++-Unterricht 2
         (Folien 4.1/4.2): Pipeline-Tafel mit Fehlerpräfixen (C…
         gegen LNK…, Anker LNK4098 aus Model-Viewer V1), die drei
         #define-Formen, Include-Schutz, MULTIPLY-Klammer-Falle als
         Zahlenbeispiel (2,67 gegen 0,67), drei Folien-Korrekturen
         (#elif, #pragma once, Leerzeichen-Regel), Unreal-Ausblick
         (UPROPERTY & Co. als Macros) und die Parken-Liste
         (Lexer/Parser/AST, .obj-Hexdump, STRINGIFY, Engine-DLL)
Quelle   Kern/LERNLOG.md (Eintrag vom 2026-10-05); Stoffgrundlage
         sind die SAE-Folien von Unterricht 2 — eine Knowledge-Notiz
         gibt es nicht (Knowledge-Frage am 2026-10-06 gestellt,
         Auswahl fiel auf die zwei OpenGL-Themen; der Stoff lebt auf
         der Seite und im LERNLOG)
Beispiel Model-Viewer V1 (LNK4098, GLFW als DLL) — Commit c5bcf1c,
         Update V 0.0001, 2026-10-04; Unterrichts-Code CppLesson2 liegt
         nicht im Bestand (gesucht 2026-10-07)
Geprüft  2026-10-07 — LNK4098 ist eine Warnung (LNK4xxx), kein Fehler;
         UHT und TOWER_API im Unreal-Ausblick ergänzt, #elseif
         präzisiert, Dateinamen main.cpp / Window.cpp
Seite →  💡 Lernstück · SAE-C++-Konventionen (Fußzeile)
Seite ←  💡 Marken statt Zeiger und
         💡 Shader-Pipeline & Fehlertexte (beide Fußzeile)
```

### 💡 Lernstück · Marken statt Zeiger
```
URL      https://claude.ai/artifact/HvvNAzt3vEW4KeGjsk5DNj
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-10-06 — neu, gebaut beim Sichern der V2-Session des
         Model-Viewers: Grenz-Tafel RAM gegen GPU, Marken-Kacheln
         (uint32_t, 0 als Flagge), Plural-API-Tabelle, Tafel „Weg
         der 36 Bytes" (Anschluss und Bind), RAII-Tabelle
         CShader/CMesh
Quelle   Knowledge/Grafik/opengl-zwei-welten-und-marken.md
Beispiel Model-Viewer V2 (Commit e428f94) — CShader und CMesh; V3
         (Commit 44302a5) ergänzt CTexture und die Kugel (8 floats je Ecke)
Geprüft  2026-10-07 — zwei Aussagen falsch: „immer im Plural" (Shader
         und Programme entstehen per Rückgabewert) und „eine Ressource je
         Klasse" (CMesh hat zwei). Dazu 36 Bytes als V2-Beispiel, keine
         Lücken-Garantie, CTexture. Knowledge-Notiz mitkorrigiert
Seite →  💡 Shader-Pipeline & Fehlertexte und
         💡 Kompiliervorgang & Präprozessor (Fußzeile)
Seite ←  Grafik/opengl-zwei-welten-und-marken.md
```

### 💡 Lernstück · Shader-Pipeline & Fehlertexte
```
URL      https://claude.ai/artifact/WsY2ratacwT59ZQp2Ux4xE
Stand    2026-10-07 — gründlich geprüft und nachgezogen (Zeile Geprüft).
         Vorher 2026-10-06 — neu, gebaut beim Sichern der V2-Session des
         Model-Viewers: Pipeline-Tafel mit fünf Stationen und den
         Läufe-Kacheln (3 gegen ~115.000), beide triangle-Dateien
         als Rezept, Compiler-Tabelle MSBuild gegen Treiber,
         Anatomie-Tafel „0(5)" samt Stolperzeilen-Merksatz,
         Wächterkette bis exit −1
Quelle   Knowledge/Grafik/shader-pipeline-und-fehlertexte.md
Beispiel Model-Viewer V2 (Commit e428f94) — CShader und
         Shaders/triangle.vert|.frag; ein Kasten zeigt, was V3 (Commit
         44302a5) am Rezept ändert
Geprüft  2026-10-07 — Rezept als V2-Stand gekennzeichnet, w-Division vor
         dem Rasterizer, Fragments statt Pixel samt Per-Fragment-Tests.
         Knowledge-Notiz: aPos → a_Position
Seite →  💡 Marken statt Zeiger und
         💡 Kompiliervorgang & Präprozessor (Fußzeile)
Seite ←  Grafik/shader-pipeline-und-fehlertexte.md
```

---

## ⚙️ System  — Schicht: Kern (der Harness selbst)

### ⚙️ System · Harness
```
URL      https://claude.ai/code/artifact/42f2b4ac-aacb-45eb-8911-55eb7769c459
Stand    2026-09-11 — nachgezogen auf Version 2.1.0 (Pflegetag, fällig
         seit dem 2026-08-27): Erststart, Prüfung 9 samt Hinweisen,
         sechster Befehl, Auslieferung ohne fremde Geschichte,
         Revier-Regel, Zahlen neu gezählt; dazu ein Abschnitt, was seit
         2.1.0 ohne neue Nummer dazukam.
Überholt Sammelstelle bis zur nächsten Harness-Version (Regel unten):
         - 2026-10-07, Pflegetag: Die gründliche Prüfung wählt nicht
           mehr nach ältestem Stand, sondern nie geprüfte Seiten oder
           solche mit geänderter Quelle.
         - Neue Index-Zeilen `Geprüft`, `Bekannt` und `Abgeschlossen`.
         - Lernstücke nennen ihren Beispiel-Code mit Versionsstand.
         - Der Kontrollpunkt für die ruhenden Seiten liegt am 02.11.
         Quelle: DECISIONS 2026-10-07.
Quelle   CLAUDE.md, Kern/WORKFLOW.md, DOC_RULES.md, VERSIONIERUNG.md,
         DECISIONS.md
Skripte  keine Unity-Skripte; die Seite beschreibt die Harness-Dateien,
         die Befehle unter Kern/Befehle/ und Kern/Werkzeuge/pruefen.py
Bilder   Tafel 5 gibt Kern/Bilder/hook_sessionstart.svg wieder —
         hochkant und in der Hausfarbwelt neu gezeichnet, weil die
         Originalskizze quer und hell ist. Original bleibt die Datei.
Seite →  keine
Seite ←  keine
```
Die Seite beschreibt den Harness in seinem **aktuellen** Zustand und wird
**bei jeder neuen Harness-Version nachgezogen** — sie ist damit die
einzige Seite, deren Stand an der Versionsnummer hängt statt am
Sonntagsabgleich (`Kern/VERSIONIERUNG.md`). Gebaut wird sie erst, wenn
der Kern nach der Abnahme steht; vorher beschriebe sie eine Baustelle.

**Was ohne neue Versionsnummer passiert** *(ergänzt 2026-08-26)*: Der
Harness ändert sich auch, ohne dass die Versionsnummer steigt — sie misst
Verträglichkeit, nicht Umfang. Die Seite wird dafür **nicht** neu gebaut;
stattdessen sammelt die Zeile `Überholt` oben jede bekannte Abweichung,
sobald sie entsteht. Die nächste Nachziehung bekommt so eine Liste statt
einer Suche. Ausgelöst wird der Eintrag vom Review-Gate
(`CODE_GUIDELINES.md` → Artifact-Check), das beim Anfassen eines Skripts
ohnehin fragt, welche Seite dadurch veraltet. Anlass: Prüfung 8 am
2026-08-26 — das Review-Gate verlangte Nachziehen, die Regel darüber
verbot es, und für den Zwischenfall gab es keinen Weg.

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

## Nicht geführte Seiten

Veröffentlicht, aber kein Teil des Harness. Sie stehen hier nur, damit
der Abgleich gegen die Veröffentlichungsliste sie nicht jede Woche neu
meldet — ein Register muss vollständig sein (`DOC_RULES.md`,
Abschnitt 8).

| ID | Titel | seit | Grund |
|---|---|---|---|
| `fc15275b-…` | Fenominal Duftliste | 2026-08-31 | privat, ohne Projektbezug — beim Abgleich am 2026-09-11 aufgefallen |
| `aa76bbca-…` | R50 Rogue Layout | 2026-10-05 | privat, Aufstellung in einem Handyspiel — beim Abgleich am 2026-10-07 aufgefallen |

---

## Gelöschte Seiten

Damit nachvollziehbar bleibt, warum eine ID ins Leere zeigt.

| ID | war | gelöscht | Rest |
|---|---|---|---|
| `cd2c6331-…` | Village spielbar | 2026-08-09 | Offline-Kopie `Seiten/2026-07-30-village-spielbar.html` |
| `0dd96ec7-…` | große Uni-Seite der Session 2026-07-16/17 | unbekannt | keine Kopie; kein Nachfolger (Isor, 2026-08-25) — nichts zeigt auf die ID, der Stoff lebt in den Lernstück-Seiten |
| `d5e30d97-…` | 🗑 Löschen · Wo das Projekt steht (Stand 2026-08-23, seit 2026-09-11 auf 🗑) | zwischen 2026-09-11 und 2026-10-07 | keine Kopie; Nachfolger `📍 Status · Semester 3`. Beim Abgleich am 2026-10-07 nicht mehr erreichbar, nichts im Knowledge zeigt auf die ID |

---

Offene Punkte zu diesem Bestand stehen in `Kern/ROADMAP.md` — ein
Verzeichnis besitzt den Bestand, nicht die Arbeit daran.

Kein Stand-Stempel für den Index als Ganzes: Er hätte keine Prüfung, die
ihn kontrolliert, und war zuletzt zehn Tage falsch (`DOC_RULES.md`,
Abschnitt 7). Die Stempel der einzelnen Seiten bleiben — die prüft der
Sonntagsabgleich.
