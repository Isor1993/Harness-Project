# FEATURE_LOG.md — Gebautes

Ownership: Nur fertig Gebautes und Geprüftes — nichts Geplantes.
Nur Projekt-/Spiel-Features; Harness-Bauten stehen in ROADMAP.md
unter Erledigt.
Format: `- JJJJ-MM-TT — Feature (1–2 Sätze: was und wo)`

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
