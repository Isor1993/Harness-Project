# LOG.md — Chronik Isor's Tower

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste oben.
Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur ergänzt.
Sie kann daher nicht falsch werden und braucht kein Archiv.
Was als Nächstes kommt, steht in `ROADMAP.md`; warum es so entschieden
wurde, in den DECISIONS dieser Schicht.
Format: `- JJJJ-MM-TT — Ereignis (1–3 Sätze: was, und woran es geprüft wurde)`.
Ein Eintrag darf einen Ablageort nennen — er beschreibt den Stand von
damals, nicht den von heute.

- 2026-07-18 — MeshBuilder: statische Klasse im Uni-Repo
  (`Assets/Shared/MeshBuilder/`), baut aus quadratischer float[,]-Heightmap
  ein Unity-Mesh (Vertices, Triangles, Normals). Geprüft per Flach-,
  Random- und Rampen-Test.
- 2026-07-18 — TerrainPreview: Test-MonoBehaviour daneben — erzeugt
  Test-Heightmap, ruft `MeshBuilder.Build`, weist das Mesh dem
  MeshFilter zu.
- 2026-07-18 — HeightmapGenerator: statische Klasse
  (`Assets/Shared/MeshBuilder/`), erzeugt quadratische 0–1-Heightmap aus
  Perlin Noise mit Oktaven (persistence/lacunarity, Seed→Offsets,
  Normalisierung über Amplitudensumme). Geprüft per Determinismus-,
  Seed- und Oktaven-Test.
- 2026-07-18 — TerrainPreview erweitert: TestMode-Enum (Flat/Ramp als
  Regressions-Checks, Noise ruft den Generator), Noise- und
  Mesh-Parameter als Inspector-Felder mit [Min]/[Range]-Guards,
  Tooltips und Headern.
- 2026-07-18 — TerrainConfig: ScriptableObject-Parameter-Object
  (`Assets/Shared/MeshBuilder/`) mit allen Pipeline-Einstellwerten
  (Heightmap/Noise/Mesh) plus neuer heightCurve (AnimationCurve, formt
  das 0–1-Höhenprofil nach der Normalisierung um). Generator nimmt jetzt
  die Config statt sechs Einzelparameter, TerrainPreview hält nur noch
  TestMode + Config-Referenz (mit Null-Guards in Awake und Start).
  Geprüft: alle drei TestModes unverändert, Kurven-Biege-Test (Täler
  sichtbar flacher), Guard-Test.
- 2026-07-18 — Terrain-Editor-Tool (MVP): TerrainToolWindow (EditorWindow,
  Tools → Terrain Generator) + TerrainToolPresenter
  (`Assets/Shared/MeshBuilder/Editor/`) — generiert, ersetzt und löscht
  das Terrain im Edit Mode aus der TerrainConfig; Fehlbedienung per
  DisabledScope + HelpBox abgefangen. Geprüft: 6-Punkte-Testplan inkl.
  Ersetzen bei Seed-Wechsel und Editor-Neustart (Config-Referenz bleibt).
- 2026-07-18 — TerrainConfig um Terrain-Material erweitert (leer =
  Default-Material der aktiven Render-Pipeline); der Presenter weist es
  bei jedem Generate zu, damit Material-Wechsel sofort greifen. Geprüft
  mit eigenem URP-Lit-Material (Smoothness runter gegen Plastik-Look).
- 2026-07-19 — Asset-Ordnerstruktur aufgeräumt: Terrain-Pipeline von
  `Shared/MeshBuilder` nach `Systems/TerrainGenerator` (Scripts/Editor/
  Materials/SO_Settings), Environment/ParticleEffects-Umbenennungen,
  TutorialInfo entfernt. Umzug im Unity-Editor, Referenzen geprüft.
- 2026-07-19 — PlateauModifier: statische Modifier-Stufe zwischen
  HeightmapGenerator und MeshBuilder (`Systems/TerrainGenerator/Scripts/`),
  plättet eine kreisförmige Fläche auf Zielhöhe mit Blend-Ring;
  Radius 0 = aus. Plateau-Parameter als neue Config-Gruppe, im
  Tool-Presenter eingehängt. Geprüft per 7-Punkte-Plan (Regression
  Radius 0, Center-Verschiebung, Height-Extreme, Blend-Kante, Seed-Test).
- 2026-07-19 — Chunk-Umbau der Terrain-Pipeline: Welt 2048 m als 8×8
  Chunks à 129 Vertices (2 m/Quad; 16×16 = 1 m/Quad rein per Inspector).
  TerrainConfig mit chunksPerEdge/chunkResolution statt
  heightmapResolution plus abgeleiteten Properties (MetersPerQuad,
  ChunkSizeInMeters); Generator und PlateauModifier rechnen pro Chunk
  und sampeln nach Weltposition (nahtlos, thread-tauglich); Presenter
  baut pro Generate einen Terrain-Root mit einem Kind-Objekt je Chunk
  komplett neu. Geprüft visuell: keine Geometrie-Nähte im Wireframe und
  Game View, Plateau global korrekt platziert.
- 2026-07-19 — TerrainPreview gelöscht (samt Szenen-Objekt): der
  Test-Treiber ist durch das Editor-Tool abgelöst.
- 2026-07-19 — Terrain-Feinschliff (Scripts/): HeightCurve-Ergebnis auf
  0–1 geclamped (Overshoot konnte unter den Weltboden ziehen); Octave-
  Offsets auf ±10000 begrenzt (benannte Konstante MaxOctaveOffset) gegen
  Float-Präzisions-Terrassen bei feiner Auflösung. Visuell verifiziert:
  glatte Auflösung 129 ohne Riefen.
- 2026-07-19 — Nahtlose Chunk-Normalen: HeightmapGenerator liefert die
  Heightmap mit 1-Vertex-Randring (Weltpositions-Sampling der Nachbarzelle),
  MeshBuilder rechnet Normalen analytisch aus den Nachbarhöhen (zentrale
  Differenz) statt RecalculateNormals — geteilte Chunk-Kanten bekommen
  dieselbe Normale, Beleuchtungsnähte verschwinden. PlateauModifier auf das
  Padding-Mapping nachgezogen, Blend-Ring auf Mathf.SmoothStep umgestellt
  (kein Knick). Visuell im Streiflicht verifiziert: keine Nähte.
- 2026-07-20 — Wasserspiegel: TerrainConfig um Water-Gruppe erweitert
  (isWaterEnabled, waterLevel 0–1, shoreMargin, waterMaterial) plus
  OnValidate-Warnung, wenn ein aktives Plateau auf/unter dem Wasserstand
  läge (Dorf säuft ab). TerrainToolPresenter baut bei aktivem Wasser eine
  Plane als Kind des Terrain-Roots (BuildWaterPlane): auf die Karte
  skaliert, mittig, auf waterLevel × heightMultiplier gehoben, Material
  mit Pipeline-Default-Fallback, MeshCollider entfernt. Visuell verifiziert:
  Seen füllen die Täler, Shader-Schaum zeichnet die Uferlinie sauber nach.
- 2026-07-23 — SampleHeight extrahiert (`Systems/TerrainGenerator/Scripts/`):
  `HeightmapGenerator.SampleHeight(config, offsets, worldX, worldZ)` liefert
  die Höhe (Noise → HeightCurve → Plateau) an beliebiger Weltposition; die
  Chunk-Schleife nutzt sie, der kommende ObjectPlacer kann sie teilen.
  `PlateauModifier` von Array-Stufe (`Apply`) auf Punkt-Funktion (`SampleAt`)
  umgestellt und in `SampleHeight` komponiert; separater Presenter-Aufruf
  entfernt, `BuildOctaveOffsets` als geteilter Helfer. Padding-Konstante
  benannt, Vertex-Index-Namen geschärft. Verhalten im Editor unverändert
  verifiziert (Plateau an gleicher Stelle). Zusätzlich: Kommentierung aller
  Terrain-Scripts auf den geschärften Maßstab gezogen (mehrzeilige XML-Docs,
  schlanke Inline-Kommentare, `#if UNITY_EDITOR` um das OnValidate-Warning).
- 2026-07-23 — Platzierungs-Datentypen (`Systems/TerrainGenerator/Scripts/`):
  `Placeable` (serialisierbare Rezept-Klasse — Prefab, Höhenband, maxSlope,
  minSpacing, scaleMin/Max, alignToGround; als `Placeable[]` in TerrainConfig
  unter „Placement") und `Placement` (unveränderlicher struct — Prefab,
  Position, Rotation, Scale). Kompiliert, Array im Inspector sichtbar. Basis
  für den Placer (Block 3).
- 2026-07-23 — ObjectPlacer (`Systems/TerrainGenerator/Scripts/`): reine
  statische Platzierungs-Stufe (Geschwister zu MeshBuilder, liest nur, fasst
  die Szene nicht an). `Place(config)` läuft pro Placeable-Typ einen globalen
  Poisson-Disc-Durchgang (Bridson, Radius = minSpacing, eigener
  `System.Random(placementSeed + i)` je Typ, deterministisch) und filtert jeden
  Kandidaten billig→teuer: Wasser-Untergrenze (nur bei aktivem Wasser) →
  Höhenband → Steigung (aus `SampleNormal`, zentrale Differenz aus vier
  Nachbarhöhen). Überlebende werden zu `Placement` — Position, zufälliger Yaw,
  optional an die Boden-Normale gekippt, zufällige Scale. `placementSeed` in
  TerrainConfig ergänzt. Kompiliert sauber; noch nicht an den Presenter gehängt
  (kommt im Panel-Block).
- 2026-07-25 — DensityStrategy (`Systems/TerrainGenerator/Scripts/Density/`):
  Strategy-Pattern für die Platzierungsdichte. Abstrakte `DensityStrategy`
  (ScriptableObject) mit `AcceptanceProbability(worldX, worldZ) → 0–1`; drei
  konkrete Assets — `UniformDensity` (immer 1), `ProbabilityDensity` (fester
  Regler 0–1), `NoiseMaskDensity` (Perlin-Wert direkt als Wahrscheinlichkeit,
  eigener Seed→Offset wie BuildOctaveOffsets + Scale, Offset in OnEnable/
  OnValidate gecacht). Feld `Density` in `Placeable` (leer/null = Uniform, kein
  Pflicht-Asset). ObjectPlacer würfelt an genau einer Stelle: neue Filterstufe
  zwischen Höhenband und Steigung (`random.NextDouble() >= acceptance` →
  verworfen). Kompiliert im Editor; Zuweisung ans Placeable kommt mit dem Panel.
- 2026-07-26 — Tool-Panel/Presenter: die Platzierung hängt am Editor-Tool und
  ist erstmals sichtbar. `TerrainToolPresenter` um `PlaceObjects` (alle Typen /
  ein Typ), `ClearObjects` (alle / ein Typ), `ClearTerrain`, `GenerateComplete`
  und die Helfer `TypeName`, `GetOrCreatePlacementRoot`, `SpawnType` erweitert;
  `Clear(string)` als privater Helfer hinter Absichts-Methoden. Hierarchie:
  „Generated Placement" als Kind des Terrain-Roots (Terrain-Regenerieren räumt
  die Platzierung damit automatisch weg), darunter eine Gruppe je Typ
  (`0_GrassSingle`). `ObjectPlacer.Place(config, placeableIndex)` streut jetzt
  einen Typ statt aller; die Typ-Schleife liegt im Presenter.
  `TerrainToolWindow` zeigt Generate Complete, die Einzel-Stufen und eine aus
  dem `Placeables`-Array erzeugte Zeile je Typ mit Place/Clear. Verifiziert:
  Gras platziert (211.000 Objekte bei minSpacing 2,7), Wasser-, Höhen- und
  Steigungs-Filter sowie AlignToGround sichtbar korrekt.
- 2026-07-26 — Platzierung komponiert mit dem Prefab-Transform: Rotation und
  Scale der Instanz werden nicht mehr überschrieben, sondern mit den im Prefab
  hinterlegten Werten multipliziert (`placement.Rotation * prefabRotation`,
  `prefabScale * placement.Scale`), gelesen von der frisch erzeugten Instanz.
  Damit überleben Achsen-Korrekturen aus dem DCC-Tool die Platzierung.
  Verifiziert mit dem Birken-FBX (Prefab-Root X = 90): Bäume stehen aufrecht
  und drehen sich zufällig um die eigene Achse.
- 2026-07-29 — `GDD.md` als Short GDD angelegt: Design-Absicht von Isor's
  Tower und Maßstab für die Zeit nach der Abgabe. Wächst mit; „offen" ist
  ein gültiger Eintrag.
- 2026-08-02 — Interaktionssystem in Betrieb + Fackel: Layer `Interactable`,
  `PlayerInteractor` (Raycast aus der Kamera) + `InteractionPromptView` samt
  Prompt-UI im HUD verdrahtet (Code existierte seit 27.07., war nirgends
  angeschlossen). `Torch` (Fähigkeit: `IsLit`, schaltet VFX + Light,
  `IDayNightListener`) + `TorchInteractable` (Adapter, liefert Prompt, leitet an
  `Toggle`) unter `Environment/Torch/Scripts/`; `TorchMode`-Enum
  (FollowDayNight/StartLit/StartUnlit) macht die Zyklus-Kopplung pro Fackel
  wählbar, Prompt-Texte serialisiert. `PlayerInteractor.UpdateTarget` vergleicht
  jetzt Ziel UND Prompt (Text springt bei gleichem Objekt um). Tag/Nacht-System
  (DayNightCycle-Prefab + eigener `ClestialPivot` mit Sonne/Mond) in
  `Viallage.unity` gebracht. Pause-Menü bedienbar: EventSystem-Startauswahl in
  `GameController.Pause()` + `SelectOnHover` (`Shared/UI/`, Hover setzt Selection)
  für Maus/Tastatur; freistehende `Main Camera` gelöscht (zwei Kameras/Listener),
  Raycast-Target am HUD-Container aus. Verifiziert im Play Mode: zielen → E →
  Fackel an/aus + Prompt, Debug-Zeit 18 → Fackel selbst an, Pause klick- und
  tastaturbedienbar.
- 2026-08-02 — Schaf-Herde als platzierbares Prefab + FSM-Feinschliff:
  `HerdManager` (`Systems/HerdManager/Scripts/`) injiziert sich selbst und den
  Graveyard-Marker per `Sheep.Init(herd, graveyard)` in alle Pool-Mitglieder —
  die Schafe brauchen keine serialisierten Szenen-Referenzen mehr, die Herde ist
  als Ganzes platzierbar. Commander als Herdenführer: nur sein Zähmen setzt
  `SetAllSheepHerdMoving(true)`; `avoidancePriority` 0 für ihn, `Random.Range(30, 70)`
  für Normal-Schafe. `SheepDodgeBehaviour` (`Entities/Sheep/Scripts/`) um
  Dodge-Cooldown und EntityId-Tie-Break erweitert (nur das höhere Schaf weicht
  aus), `TryEnterDodge` nur noch aus `PatrolState`; `DodgeState` kehrt generisch
  in den gemerkten State zurück, `SheepFSM.ChangeState(SheepStateBase)` dafür
  public.
- 2026-08-03 — Zähmen als Umschalter + Cleanup des Schaf-/Herden-/FSM-Codes:
  `Sheep.Tame()` → `ToggleTame()`, `SheepInteractable` hält die Prompts „Tame"
  und „Release" als serialisierte Felder und wechselt sie live; `CanInteract`
  prüft nur noch, ob das Schaf lebt. Neue Datei `SheepAnimatorParameters`
  (`Systems/SheepFSM/Scripts/`) ersetzt 25 Animator-Magic-Strings in den elf
  States. Kapselung: `IsHerdMoving` und `Animator` in `Sheep`, die
  Erkennungsergebnisse in `SheepSense`, `TryGetBestFleeTarget` in
  `SheepMoveBehaviour`. Behoben: fehlendes `</summary>` in `SheepFSM`,
  Test-Killschalter in `SheepHealth` hinter `#if UNITY_EDITOR`, fünf
  `[Range]`-Paare an die Settings-Assets angeglichen, Tippfehler
  `TransitionDeadState` und `_hasHandledDeath`; `ValidateHerd` warnt beim Start,
  wenn Slot-Offsets für die Formation fehlen. Verifiziert im Play Mode: Zähmen
  und Freilassen inklusive Prompt-Wechsel.
- 2026-08-03 — Nur ein Schaf gleichzeitig zähmbar: `TamedSheepReference`
  (ScriptableObject, `Entities/Sheep/SO_Settings/`) hält den Zeiger auf das
  aktuell gezähmte Schaf, projektweit statt pro Herde. `SheepInteractable`
  verweigert den Prompt an allen anderen Schafen, solange der Zeiger belegt ist;
  das gezähmte Schaf selbst bleibt immer freilassbar. Der Zeiger wird beim Lesen
  gegen `IsAlive` und `IsTamed` geprüft und kann darum nicht veralten — ein
  sterbendes Schaf gibt die Sperre frei, sobald es tot ist. Asset an beiden
  Sheep-Prefabs verdrahtet, fehlende Zuweisung meldet eine Warnung in `Awake`.
  Verifiziert im Play Mode: zweites Schaf ohne Prompt, nach dem Freilassen wieder
  zähmbar.
- 2026-08-03 — Prefab-Painter (`Systems/PrefabPainter/Editor/`, MVP wie das
  Terrain-Tool): Fenster + Presenter + `PainterPalette`-Asset mit
  `PaintBrush`-Rezepten (Single/Scatter/Line, Radius, MinSpacing, Zufalls-
  Yaw/Tilt/Scale, Bottom-Snap, Kategorie-Gruppen), malt Prefabs per Raycast
  auf beliebigen Untergrund, Objekte darüber blocken den Platz, Erase im
  Radius, Drop-to-Ground für die Selektion, alles Undo-registriert.
  Editor-Hilfstool, ausdrücklich nicht Abgabe-Umfang. (Doku nachgetragen
  2026-08-05 — die Bau-Session hatte die Pflicht ausgelassen.)
- 2026-08-04 — Gras-Rendering per GPU-Instancing
  (`Systems/TerrainGenerator/Scripts/`): `PlaceableRenderMode` je Placeable
  (GameObjects/Instanced, GameObjects bleibt 0), `GrassCellBuilder` zerlegt
  die Placement-Liste in Zellen (`GrassCell`-struct: `Matrix4x4[]` +
  `Bounds`), `InstancedRenderer` (`[ExecuteAlways]`, sitzt auf der
  Typ-Gruppe) baut die Zellen bei OnEnable/Init aus dem `placementSeed` neu
  — Matrizen werden nie serialisiert — und zeichnet je Zelle in
  ≤1023er-Batches per `Graphics.RenderMeshInstanced`, Schatten aus;
  `SpawnType` im Presenter verzweigt nach RenderMode. Verifiziert: Gras
  zeichnet ohne GameObjects, Zell-Culling greift sichtbar.
- 2026-08-04 — Gras-LOD + Render-Settings am Prefab: `GrassRenderProfile`
  (Datenkomponente am Gras-Prefab — LowDetailMesh, LodDistance,
  RenderDistance, CellSize), `GrassLodSelector` entscheidet je Zelle
  None/High/Low nach Kamera-Distanz, der Renderer zeichnet nur noch.
  Low-Büschel in Blender aus dem Original abgeleitet (Halm 20 → 7 Tris via
  Dissolve, Normals per Normal-Edit-Modifier nach oben, Unity-Import
  „Normals: Import"). Von 507 Mio auf ~12 Mio Dreiecke, 4,5 → ~87 FPS im
  Editor; 27k Gras-Instanzen in 138 Draw Calls.
- 2026-08-05 — PlacementExclusion (`Systems/TerrainGenerator/Scripts/`):
  Komponente markiert Freiflächen (Kreis/Box, Center-Offset, dreht mit dem
  Objekt, Gizmo immer sichtbar); `PlacementExclusionFilter` als eigene Stufe
  zwischen Placer und beiden Spawn-Wegen (Instanced und GameObjects) wirft
  Platzierungen darin raus, Rand = halbe Objektbreite aus den Mesh-Bounds.
  Formprüfung lebt in der Komponente (`Contains`), der Filter kennt keine
  Formen. Verifiziert am Haus: Gras- und Baumkante folgen der Zone.
- 2026-08-05 — NoiseMask-Kontrastkurve + Instancing-Transform-Fix:
  `NoiseMaskDensity` remappt den Perlin-Wert per AnimationCurve zu echten
  Kahl-/Dichtflächen (roh lag alles bei ~0,5 → gleichmäßiges Ausdünnen);
  `GrassCellBuilder` komponiert jetzt Prefab-Root-Scale und -Rotation in die
  Matrix (`prefabScale * placement.Scale`) wie der GameObject-Weg — vorher
  wurde Gras bei Root-Scale 0,3 um Faktor 3,3 zu groß gezeichnet.
- 2026-08-05 — `RuntimePlacementSpawner` (`Systems/TerrainGenerator/Scripts/`):
  erzeugt beim Szenenstart je instanziertem Typ eine Gruppe mit
  `InstancedRenderer`, sodass Gras auch ohne Editor-Tool im Build entsteht.
  Sitzt auf „Generated Placement", überspringt Gruppen, die das Tool schon
  angelegt hat. Geprüft: Play-Mode und Build zeigen Gras, Stacktrace bestätigt
  den Laufzeit-Pfad.
- 2026-08-05 — Placement kachelweise parallelisiert: `ObjectPlacer` teilt die
  Welt in `PlacementTilesPerAxis`² Kacheln, jede sampelt und filtert mit eigenem
  Generator, `Parallel.For` über die Kacheln; `GrassCellBuilder` baut Matrizen
  und Bounds ebenfalls parallel. Neu dafür `CurveLookup` (AnimationCurve als
  thread-sichere Tabelle, genutzt von `TerrainConfig` und `NoiseMaskDensity`).
  Ladezeit des Gras-Rebuilds 122,7 s → 16,5 s, Punktzahl praktisch unverändert
  (+0,17 %). Einzelheiten in DECISIONS und TDD_NOTES 2026-08-05.
- 2026-08-05 — `ExclusionArea` (`Systems/TerrainGenerator/Scripts/`):
  Exclusion-Zone als reine Zahlen, einmal per `PlacementExclusion.ToArea` aus dem
  Transform aufgelöst; der Filter testet danach ohne Unity-Zugriff. Vorher wurde
  `transform` je geprüftem Punkt gelesen (~15 Mio Zugriffe). Stufe 2,57 s →
  0,97 s, Gesamtladezeit 12,4 s. `PlacementExclusion.Contains` entfällt.
- 2026-08-05 — `FpsDisplay` (`Systems/Diagnostics/Scripts/`): schreibt Frame-Rate
  und Frametime gemittelt über ein Intervall in ein HUD-Label; misst ungeskalierte
  Zeit, damit Pause die Anzeige nicht verfälscht.
- 2026-08-06 — Zähmen reagiert sofort: `Sheep.ToggleTame()` wechselt beim Zähmen
  direkt in `FollowPlayerState` (Freilassen bleibt ungezwungen — `FollowPlayerState`
  steigt über `!IsTamed` selbst aus); `SheepInteractable.CanInteract` blendet den
  Prompt für schlafende, ungezähmte Schafe aus, die `IsAsleep`-Prüfung sitzt hinter
  dem `IsTamed`-Early-Return. Geprüft an sechs Fällen: fressendes und
  patrouillierendes Schaf folgen sofort, schlafendes zeigt keinen Prompt, gezähmtes
  bleibt bei Einbruch der Nacht freilassbar, Freilassen geht ohne Flackern nach
  Regroup, Commander startet die Herdenbewegung wie zuvor. Begründung in
  DECISIONS 2026-08-06.
- 2026-08-08 — Unity-Ordnerstruktur nach Uni-Systemgrenzen getrennt:
  `Systems/TerrainGenerator/` in vier Systeme aufgeteilt — `WorldGeneration/`
  (TerrainConfig, HeightmapGenerator, PlateauModifier, MeshBuilder, CurveLookup),
  `ObjectPlacement/` (Placer, Placeable, Placement, Exclusion-Kette, `Density/`,
  RuntimePlacementSpawner), `GrassRendering/` (Cell, CellBuilder, LodLevel,
  LodSelector, RenderProfile, InstancedRenderer) und `TerrainTool/Editor/`
  (Window, Presenter). 26 Skripte plus 6 Assets, keine Code-Änderung nötig —
  die Dateien haben weder `namespace` noch `.asmdef`. Zieht ROADMAP-Punkt 8
  (Gras herauslösen) mit vor.
- 2026-08-08 — DayNightSystem (5 Klassen) und Sheep-FSM (14 Klassen) als
  erzeugte Diagramme neu gebaut; die handgezeichneten Vorgänger sind archiviert.
  `Sheep_System_UML` braucht keinen Ersatz — `Sheep_Komponenten` deckt es
  vollständig ab und enthält sechs Klassen mehr.
- 2026-08-09 — Programmablaufplan „Generate Complete" erzeugt
  (`Diagramme_Quellen\Ablauf_Generate_Complete.drawio`, Skript
  `05_Werkzeuge\Vorlagen\ablauf_generate_complete.py`): 29 Sinnbilder, 32
  Linien, beide Hälften des Befehls (Generate links, PlaceObjects rechts),
  vier Abbruchzweige, zwei Schleifen. Damit ist die letzte Pflichtanforderung
  der Tool-Aufgabe erzeugbar. Geprüft: keine Überlappung, zweiter Lauf
  byte-identisch, von Hand verschobener Kasten und gesetzter Wegpunkt
  überleben einen Lauf.
- 2026-08-14 — Ton-System aufgebaut. `Village.unity` und `MainMenu.unity`
  hatten vorher **null AudioSource**. Jetzt: `MainMixer` (`Shared/Audio/`)
  mit den Gruppen Master → Music/SFX und den exponierten Parametern
  `MasterVolume`, `MusicVolume`, `SfxVolume`; Musik im Hauptmenü
  (TownTheme) und im Dorf (The Wind), Windböen und Fackelfeuer als
  Umgebung, Schafe, Spielerschritte und ein Antwortlaut beim Zähmen.
  Alle verwendeten Klänge stehen unter CC0.
- 2026-08-14 — `RandomIntervalSound` (`Shared/Audio/Scripts/`): spielt nach
  gewürfelter Wartezeit einen zufälligen Clip mit zufälliger Tonhöhe. Jede
  Instanz zählt ihren eigenen Timer, damit eine Herde verstreut blökt statt
  im Chor. Fällt auf die AudioSource am eigenen Objekt zurück, wenn keine
  verdrahtet ist — nötig für massenhaft gesetzte Objekte. Läuft an neun
  Schafen und am Wind.
- 2026-08-14 — `FootstepPlayer` (`Entities/Player/Scripts/`): zählt die
  zurückgelegte Strecke statt der Zeit, sodass die Schrittfrequenz ohne
  Umrechnung am Tempo hängt (2 m je Schritt, bei 5 m/s alle 0,4 s).
  Nur bei Bodenkontakt und über einer Mindestgeschwindigkeit; beim Anhalten
  parkt der Zähler auf der Schwelle, damit kurzes Antippen hörbar bleibt
  und eine Landung aufsetzt. Geprüft im Spiel.
- 2026-08-14 — `Torch.SetLit` schaltet jetzt auch den Feuerklang, neben
  Flammen-VFX und Licht. `TorchInteractable` braucht deshalb keinen eigenen
  Interaktionslaut — das an- und ausgehende Feuer ist die Rückmeldung.
  `SheepInteractable` spielt beim Zähmen und Freilassen einen Antwortlaut
  über die vorhandene Schaf-Stimme.
- 2026-08-14 — Audio-Bestand in der Asset-Library geordnet
  (`03_AssetLibrary\Extern_Frei\Audio\`): elf Pakete unter `_Pakete\` mit je
  einer `_Quelle.txt`, daneben `Sortiert\` mit 214 nach Zweck einsortierten
  Dateien (Ambience, Combat, Creatures, Doors, Fire, Footsteps, Items,
  Music, UI). `_Katalog.md` verbindet beide Ebenen.
- 2026-08-14 — Options-Fenster gebaut: `OptionsPanel` als Prefab
  (`Shared/UI/Prefabs/`) mit vier Reglern — Gesamtlautstärke, Musik,
  Effekte, Maus-Empfindlichkeit — je mit Beschriftung und Prozentanzeige,
  dazu ein Zurück-Knopf. Aufbau wie das Hauptmenü: Vollbild-Panel für den
  Hintergrund, darin ein mittig verankerter `Content`-Container mit
  Vertical Layout Group und Content Size Fitter, der die Anordnung rechnet.
  Im Hauptmenü vollständig in Betrieb; im Pausenmenü des Dorfes reagieren
  die Slider noch nicht auf die Maus (offener Punkt in der ROADMAP).
- 2026-08-14 — `GameSettings` (`Shared/UI/Scripts/`): rechnet Reglerwerte
  in Dezibel um (`Log10(max(v, 0.0001)) * 20`, damit `Log10(0)` nie
  auftritt), setzt sie am `MainMixer`, schreibt die Prozentanzeige und
  legt alles in `PlayerPrefs` ab. Liegt bewusst auf einem immer aktiven
  Objekt statt auf dem Options-Panel, weil ein deaktiviertes Panel sein
  `Awake` nie ausführt und gespeicherte Werte dann erst nach dem ersten
  Öffnen greifen würden.
- 2026-08-14 — `PlayerLook` nimmt die Maus-Empfindlichkeit jetzt von außen
  an (`SetSensitivity`) und liest den gespeicherten Wert in `Awake` selbst
  aus `PlayerPrefs` — nötig, weil die Einstellung im Hauptmenü vorgenommen
  wird, wo es keinen Spieler gibt, der sie entgegennehmen könnte.
- 2026-08-15 — Options-Fenster auch im Dorf in Betrieb. Das Panel reagierte
  dort nicht auf die Maus, obwohl Tastaturbedienung ging; eine frische Kopie
  aus dem Hauptmenü funktionierte sofort. Das alte Panel war durch mehrfaches
  Umhängen zwischen Prefabs beschädigt. `GameController.Pause()` setzt das
  Menü beim Öffnen jetzt auf die Button-Seite zurück, damit nach ESC im
  Options-Fenster nicht wieder Options erscheint.
- 2026-08-16 — Menü-Optik über alle drei Fenster vereinheitlicht. Eine
  Tafel (760 breit, `17130F` Alpha 224, `UISprite` sliced mit PPU-Faktor
  0.5) trägt Hauptmenü, Pausenmenü und Options; Titel und Buttons in
  `Oswald Bold SDF`, Beschriftungen englisch. Der Auswahlzustand läuft
  über eine Ember-Tönung im ColorBlock statt über das vorherige Giftgrün;
  `SelectOnHover` hängt jetzt auch an den drei Hauptmenü-Buttons, damit
  nie zwei Einträge gleichzeitig markiert sind.
- 2026-08-16 — Hauptmenü-Hintergrund: Dorf-Standbild statt Farbfeld, über
  die Image-Farbe abgedunkelt, mit `Aspect Ratio Fitter` im Modus
  `Envelope Parent` — füllt jedes Seitenverhältnis ohne Verzerrung.
- 2026-08-16 — Options-Fenster als feste Tafel statt Vollbild-Schleier;
  Regler mit Ember-Füllung. Damit bleibt im Dorf das Dorf sichtbar, was
  vorher nicht der Fall war (zwei Schleier übereinander).
- 2026-08-16 — In-Game-HUD gebaut. `InGameUI` wurde zu `HudRoot` und ist
  jetzt der gemeinsame Schalter: `GameController` blendet beim Pausieren nur
  dieses eine Objekt aus. Vier Ecken plus Mitte — Spieler-Kartusche oben
  links, Uhr oben rechts, FPS unten links, Zähmzähler unten rechts,
  Fadenkreuz und Prompt in der Mitte, Ziel-Zustand oben mittig. Alle Tafeln
  aus demselben Material wie die Menüs.
- 2026-08-16 — `Health` als allgemeine Komponente
  (`Assets/Shared/Health/Scripts/`), implementiert `IDamageable`: Leben,
  Schaden, Heilung, `Normalized` für Balkenanzeigen. Hängt am Spieler und ist
  für Goblin und Mobs ohne Änderung wiederverwendbar. `SheepHealth` blieb
  unberührt, weil es im TDD beschrieben ist.
- 2026-08-16 — Vier HUD-Anzeigen nach einheitlicher Bauart
  (`Shared/UI/Scripts/`): `TamedSheepDisplay` (Einzelschaf oder Herde folgt),
  `DayTimeDisplay` (Tag, Uhrzeit, Tagesphase), `HealthBarDisplay` (gefüllte
  Leiste zu beliebiger `Health`), `TargetStatusDisplay` (Zustand des
  anvisierten Objekts). Alle vier merken sich den angezeigten Wert, prüfen ihn
  in `Update` und schreiben nur bei Änderung — TextMeshPro baut sein Mesh sonst
  in jedem Frame neu auf.
- 2026-08-16 — `IInteractable` um `StatusText` erweitert: Der
  Interaktions-Prompt sagt, was ein Tastendruck tut, `StatusText` sagt, was das
  Objekt ist. Beim Schaf sind das Leben und Hunger, bei der Fackel bleibt es
  leer. `PlayerInteractor` reicht beides getrennt weiter.
- 2026-08-19 — Ladescreen beim Szenenwechsel Hauptmenü → Dorf.
  `SceneLoader` bekam `LoadAsync(SceneId)`, das den Ladevorgang startet, mit
  `allowSceneActivation = false` zurückhält und die `AsyncOperation`
  zurückgibt; die doppelte Namensprüfung liegt jetzt in `TryGetSceneName`.
  Neu ist `LoadingScreenController` (`Systems/GameFlow/Scripts/`): hält die
  Operation, rechnet `progress / 0.9` auf 0–1 hoch, zieht den angezeigten
  Wert mit `Mathf.MoveTowards` nach und schaltet die Szene erst um, wenn der
  **angezeigte** Wert 1 erreicht hat. `MainMenuController.StartGame()` blendet
  nur noch das Menü-Panel aus und übergibt. Das Ladepanel liegt als viertes
  Kind in `MainMenuUI.prefab` (Backdrop, BarTrack mit BarFill, ProgressLabel,
  LoadingTitle) in der Menü-Palette. Dazu ein selbst erzeugtes 8×8-Sprite
  `Shared/UI/Textures/UI_WhitePixel.png`. Im Editor geprüft.
- 2026-08-19 — Welt-Begrenzung: vier unsichtbare Wände am Kartenrand, gebaut
  vom Terrain-Tool. `TerrainToolPresenter.BuildWorldBounds` erzeugt unter
  `Generated World Bounds` vier leere Objekte mit BoxCollider, Maße aus
  `SizeInMeters` und `HeightMultiplier`: 10 m dick, von Y −50 bis Y 850,
  Innenkante bündig mit der Weltkante bei 0 und 2048. Wird aus `Generate`
  mitgerufen und liegt zusätzlich als eigener Knopf „Build World Bounds" im
  Tool-Fenster, damit eine bereits bepflanzte Welt die Wände ohne
  Neugenerierung bekommt. Wirkt auf den Spieler, weil `PlayerMotor` über
  `CharacterController.Move` läuft; die Schafe hält schon die NavMesh-Kante.
- 2026-08-19 — Bäume sind jetzt fest: `BirchTree_1.prefab` bekam einen
  `CapsuleCollider` (Radius 0,21, Höhe 5,68, Achse Z wegen der 90°-Drehung
  des Modells) und einen `NavMeshObstacle` mit `Carve` und
  `CarveOnlyStationary`. Damit stoppt der Collider den Spieler und der
  Obstacle die Schafe — zwei Systeme, zwei Lösungen. Von Isor im Spiel
  geprüft: kein spürbarer Einbruch bei 21.354 Bäumen.
- 2026-08-19 — Fackeln bekommen Licht und Körper. Beide Prefabs unter
  `Environment/Torch/Prefab/` tragen jetzt je ein Point Light in warmem
  Feuerton (RGB rund 147/100/41, Intensität 0,66 bzw. 0,68, Reichweite
  10,88 m) und je zwei CapsuleCollider (Schaft r 0,19 / h 1,24, Korb
  r 0,50 / h 2,00). Damit leuchten sie und lassen sich nicht mehr durchlaufen.
- 2026-08-20 — Zeit-Vorspulen auf gehaltener Taste `T`. Neue Action
  `FastForward` in `PlayerControls.inputactions`, im `PlayerInputReader` als
  abgefragte Eigenschaft `IsFastForwarding` (gehaltene Taste ist
  kontinuierliche Eingabe, kein Event) und in `EnableUI` mit zurückgesetzt.
  Neu ist `TimeFastForward` (`Systems/DayNightCycle/Scripts/`) auf dem
  `ClockDisplay`: setzt `IngameTime.TimeScale` auf das 60-fache, solange die
  Taste hält, und schreibt `[T] Fast Forward` bzw. `Fast Forward x60` in eine
  Zeile unter der Uhr. Betroffen ist nur die Ingame-Uhr — `IngameTime` hat
  einen eigenen Multiplikator, Unitys `Time.timeScale` bleibt unberührt, also
  laufen Physik, Animationen und Schafe normal weiter.
- 2026-08-20 — Tageslänge von 24 echten Stunden auf 20 Minuten gesenkt
  (`_realSecondsPerIngameSecond` von 1 auf 0,0139 im `DayNightCycle`-Prefab).
- 2026-08-20 — Bäume stehen senkrecht: `AlignToGround` am Baum-Placeable aus,
  Baumgruppe über die Typ-Zeile neu gesetzt. Vorher lagen Bäume an steilen
  Hängen flach, weil sie auf die Bodennormale gedreht wurden.
- 2026-08-20 — Glühwürmchen: `VFX_FireFly`-Prefab aus `FireFly.vfx`
  (`ParticleEffects/FireFly/Prefabs/`) mit neuer `NightVfx`-Komponente
  (`Systems/DayNightCycle/Scripts/`). Sie meldet sich wie `Torch` beim
  `DayNightCycleEventManager` an und lässt den Effekt bei Abend und Nacht
  laufen; bleibt das Manager-Feld leer, sucht sie ihn beim Start selbst —
  nötig, weil platzierte Kopien keine Szenenreferenz tragen können. Gesetzt
  wurden die Schwärme als dritter Placeable-Typ über den Terrain-Placer,
  begrenzt auf das Höhenband knapp über dem Wasserspiegel und flaches Gelände.
- 2026-08-20 — Schafherden prozedural gesetzt: `SheepHerdManager_01` als
  vierter Placeable-Typ, 19 Instanzen, Höhenband 0,14–0,30 und Hangneigung
  bis 8,4° (nur flaches Weideland, damit die NavMeshAgents sauber aufsetzen).
  Gesetzt wird der Herdenverwalter, nicht das einzelne Schaf — die Herde
  entsteht daraus. Damit ist die Bevölkerung des Dorfes generiert und nicht
  von Hand verteilt.
- 2026-08-20 — Roter Ball als Bedrohungs-Attrappe auf Layer `Enemy`, dazu
  `RigidbodyPusher` (`Scripts/Player/`): Ein `CharacterController` gibt beim
  Bewegen keinen Impuls weiter, deshalb schiebt die Komponente leichte
  Rigidbodies aus `OnControllerColliderHit` von Hand an. Damit lässt sich das
  Fluchtverhalten der Schafe vorführen, solange es keinen Gegner gibt.
- 2026-08-20 — Assets von Themen- auf Typsortierung umgestellt: `Scripts/`,
  `Prefabs/`, `Materials/`, `SO_Settings/`, `Textures/`, `Shader/`, `VFX/`,
  `FBX/`, `Audio/`, darunter je ein Ordner pro System oder Wesen. Editor-Code
  getrennt in `Assets/Editor/`, Fremdpakete unverändert in `ThirdParty/`.
- 2026-08-25 — Systemliste eingerichtet: `Werkzeuge/systeme.py` erzeugt
  `SYSTEME.md` — je Ordner unter `Assets/Scripts/` plus `Assets/Editor/`
  eine Zeile mit Skriptzahl und letzter Änderung; Beschreibungen kommen
  von Hand und überleben jeden Lauf, den Projektpfad liefert
  `Kern/PFADE.md` → `PROJEKT`. Geprüft: Zählung gegen Handmessung
  (17 Ordner, 93 Skripte) und Beschreibungs-Erhalt über einen zweiten
  Lauf.
- 2026-08-26 — Repo-Hygiene aus der Harness-Design-Session: das
  GitHub-Token aus der Remote-URL entfernt (von Isor widerrufen), das
  Repo privat gestellt, die `.gitattributes` routet `*.unity` und
  `NavMesh*.asset` jetzt über LFS, die toten `ThirdAssets`-Zeilen sind
  aus der `.gitignore`. Die LFS-Migration der Historie steht als Punkt
  in `Kern/ROADMAP.md`. Geprüft: `git ls-remote` liefert `main`
  weiterhin; Sichtbarkeit per API-Abruf ohne Anmeldung (404).
- 2026-08-28 — Phase 0 begonnen, Arbeit über den 27. und 28. verteilt.
  Netzwerk-Pakete über das Multiplayer Center installiert: Netcode for
  GameObjects 2.13.2, Multiplayer Services 2.3.1, Multiplayer Play Mode
  2.0.2, Multiplayer Tools 2.2.11. Vivox und das Dedicated Server
  Package abgewählt. Der Assistent empfahl dabei zweimal etwas anderes
  als am 2026-08-25 entschieden — erst einen Dedicated Server (Folge von
  „Cheating: very important"), dann Distributed Authority (Folge von
  „geringste Kosten"); beides von Hand auf Client Server und Client
  Hosted gestellt. Relay und Player Authentication im
  Unity-Cloud-Dashboard freigeschaltet; das Cloud-Projekt war bereits
  verknüpft. Beleg: Der Quickstart meldet „This project is correctly
  setup to use Unity services."
- 2026-08-28 — `NetTestbed.unity` gebaut: Boden als Plane (Scale 3, also
  30 × 30 m), NetworkManager mit Unity Transport, Spieler-Prefab
  `NetTestPlayer` mit `NetworkObject` und `NetworkTransform` auf
  `Authority Mode: Owner` (Scale-Synchronisation abgeschaltet, weil sich
  die Größe nie ändert), Behelfs-UI mit zwei Knöpfen sowie die Skripte
  `SessionStarter` und `NetTestPlayerMover` in
  `Assets/Scripts/Networking/`. Geprüft mit zwei Spielern über
  Multiplayer Play Mode auf einem Rechner: Beide Kapseln erscheinen,
  jeder steuert nur seine eigene. Damit ist Abnahmepunkt 2 von Phase 0
  (Besitz) erledigt; die übrigen vier stehen aus.
- 2026-08-28 — Join-Code über die Sessions-API gebaut: anonyme Anmeldung,
  `CreateSessionAsync` mit `WithRelayNetwork`, Code in der Behelfs-UI,
  Beitritt über `JoinSessionByCodeAsync`. Geprüft mit zwei Prozessen auf
  einem Rechner, aber **über Relay statt über `127.0.0.1`** — beide sahen
  einander laufen, das Ownership-Overlay zeigte zwei Besitzer (Client 0
  und 1). Damit ist Abnahmepunkt 1 erledigt. Die Syntax wurde vorher in
  Unitys Doku nachgeschlagen statt aus dem Gedächtnis geschrieben; drei
  von drei Annahmen wären falsch gewesen.
- 2026-08-28 — `NetTestPing` gebaut: Leertaste beim Besitzer →
  `[Rpc(SendTo.Server)]` zum Host → Zähler → `[Rpc(SendTo.Everyone)]`
  zurück an alle. Geprüft: In der Konsole des Gastes erschienen beide
  Meldungen, auch die für die Kapsel des Hosts — damit ist der Rückweg
  belegt und Abnahmepunkt 3 erledigt. Es fehlen noch Punkt 4
  (Vergleichstest) und Punkt 5 (Build auf dem Laptop); beide brauchen das
  zweite Gerät.
- 2026-08-28 — Der Regler „Wer schreibt" wurde im Lauf der Session
  geändert: Bibliotheks-Anbindung und Wegwerf-Code schreibt Claude, alles
  Entscheidungstragende und selbst Entworfene tippt Isor. Als Ersatz für
  das Abtippen kamen Verständnisfragen zum Code. Erster Durchgang: Von
  drei Fragen saß eine sofort, eine war halb, eine nicht — nach der
  Auflösung konnte Isor alle drei in eigenen Worten herleiten.
- 2026-08-28 — `NetTestPing` auf `NetworkVariable` umgebaut: Der Zähler ist
  jetzt ein Zustand statt eines Ereignisses. `int` → `readonly
  NetworkVariable<int>` als Feldinitialisierer, Abonnement in
  `OnNetworkSpawn`, Abbestellung in `OnNetworkDespawn`, und der Rückweg-RPC
  `AnnouncePingRpc` ersatzlos gelöscht — die Variable verteilt den Wert
  selbst. Geprüft im Multiplayer Play Mode mit drei Spielern: Ein nach zwei
  Pings beigetretener Gast schrieb **keine** Ping-Zeile für die Vergangenheit,
  meldete danach aber `Ping 2` für die fremden Kapseln statt `Ping 1`. Damit
  ist belegt, dass der Wert beim Spawnen nachgeliefert wird und
  `OnValueChanged` dafür nicht feuert.
- 2026-08-28 — `SessionStarter` um zwei Behelfe erweitert: `IsAlreadyConnected`
  lehnt einen zweiten Start ab (`NetworkManager.Singleton.IsListening`) und
  loggt eine Warnung, statt die SDK vierzig Zeilen tief scheitern zu lassen;
  dazu `OnClientConnectedCallback` mit An- und Abmeldung in `Start` und
  `OnDestroy`. Geprüft mit drei Prozessen: Der Host meldete `Client 0`, `1`
  und `2`, jeder Gast nur sich selbst — der Rückruf feuert beim Host für alle,
  beim Gast nur für die eigene Verbindung. Vorarbeit für den Ladebalken aus
  Phase 1, der auf mehrere Spieler warten muss.
- 2026-08-28 — Verbindungsaufbau scheiterte zwischendurch mit
  `SessionException: Failed to start the network manager`. Ursache war eine
  Skript-Neukompilierung bei laufendem Play Mode, nicht der Code: Ein
  vollständiger Editor-Neustart behob es ohne jede Änderung. Der Stacktrace
  wies den Weg — der Beitritt lief bis zur Relay-Zuteilung durch und
  scheiterte erst am lokalen `StartClient()`.
- 2026-08-28 — `GenerationFingerprint` gebaut (`Assets/Scripts/Diagnostic/`),
  dazu die neue Szene `Fingerprint.unity` mit nur diesem einen Objekt. Ein
  MonoBehaviour statt eines EditorWindow, weil die Messung auch im Build
  laufen muss. Es tastet 128 × 128 = 16.384 Höhen auf festem Raster ab, läuft
  den `ObjectPlacer` je Typ und faltet Position, Drehung und Skalierung als
  rohe Bitmuster in einen FNV-1a-Hash; das Ergebnis geht als Textdatei nach
  `Application.persistentDataPath`, getrennt nach Editor- und Build-Lauf.
- 2026-08-28 — Erste Messreihe des Vergleichstests mit
  `TerrainConfig_Default`, Seed 2376 und placementSeed 154: 16.384 Höhen,
  13.021 Birken, 4.689.011 Grasbüschel, 958 Glühwürmchen-Schwärme, 7
  Schafherden. Zwei Läufe derselben .exe (15:02 und 15:23) sowie ein
  Editor-Lauf (15:14) ergaben **dieselben fünf Prüfsummen bis aufs letzte
  Bit**. Damit ist die Nebenläufigkeit im `ObjectPlacer` als Fehlerquelle
  ausgeschlossen: Die Kachel-Parallelisierung liefert reproduzierbar
  dasselbe. Offen bleibt allein der Hardware-Vergleich gegen den Laptop.
- 2026-08-28 — Nicht gemessen wird der `PlacementExclusionFilter`: Der
  Prüfstand misst die Ausgabe des `ObjectPlacer`, die Ausschlusszonen laufen
  als eigene Stufe danach. Bewusst so, weil die riskante Stelle die
  Poisson-Streuung ist — festgehalten, damit ein grüner Test nicht mehr
  behauptet, als er geprüft hat.
- 2026-08-28 — Vergleichstest auf zwei Maschinen bestanden: Der Laptop
  (Intel Core i9-14900HX) lieferte gegen den PC (AMD Ryzen 7 8700G) bei
  gleichem Seed 2376 **exakt dieselben fünf Prüfsummen** — 16.384 Höhen,
  13.021 Birken, 4.689.011 Grasbüschel, 958 Glühwürmchen-Schwärme, 7
  Schafherden. Verschiedene Hersteller, verschiedene Mikroarchitekturen.
  Damit ist die ungeprüfte Bedingung aus `DECISIONS/Multiplayer.md`
  („Der Floor kommt gemischt herüber", 2026-08-25) erfüllt: Gelände und
  Bewuchs dürfen als Seed übertragen werden. Nicht abgedeckt bleiben
  ARM-Prozessoren und IL2CPP-Builds — beide Geräte fahren x86-64 und Mono.
- 2026-08-28 — Erster Verbindungstest über echtes Internet: eine Lobby mit
  drei Teilnehmern — PC und Laptop in Deutschland, dazu ein dritter Rechner
  auf den Philippinen (rund 10.000 km). Beitritt über Join-Code und Relay,
  ohne dass jemand Ports freigeben musste. Damit ist die in den DECISIONS
  vom 2026-08-27 ausdrücklich benannte Lücke geschlossen („Nicht abgedeckt
  bleibt echte Internet-Verzögerung: Beide Geräte hängen am selben Router").
  Beobachtet: fremde Kapseln liefen flüssig, die Ping-Meldung erschien ohne
  wahrnehmbare Verzögerung, keine Aussetzer über die Testdauer. Das sind
  Eindrücke, keine Messung — eine Zahl für die Umlaufzeit fehlt weiterhin.
- 2026-08-28 — **Phase 0 abgeschlossen**, vor dem Semesterstart wie geplant.
  Alle fünf Abnahmepunkte stehen: Verbindung über Join-Code, Besitz,
  Nachrichten in beide Richtungen, gelaufener Vergleichstest und ein
  Windows-Build auf dem Laptop. `NetTestbed.unity` bleibt als
  Diagnose-Szene stehen, `Fingerprint.unity` daneben als Prüfstand der
  Weltgleichheit.
