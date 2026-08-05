# TDD_NOTES.md — Stoffsammlung fürs Technical Design Document

Ownership: Grobe Einträge für das Uni-TDD (Terrain-/Mesh-Generation,
Abgabe ca. 2026-07-28). Kein fertiger Text — nur Rohmaterial, aus dem
das TDD am Ende generiert wird. Nur echte Arbeit am Uni-Projekt —
Harness-Entwicklung gehört nicht hierher.
Format: `- JJJJ-MM-TT — [Themenblock] Stichpunkt (1–3 Zeilen)`.
Themenblöcke frei wählen (z. B. Architektur, Terrain, Mesh, Input,
Tools); neue Einträge einfach anhängen — sortiert wird beim Generieren.

## Einträge
- 2026-07-18 — [Mesh] MeshBuilder als statischer Übersetzer Heightmap→Mesh.
  Kernformeln: res² Vertices, (res−1)²·6 Triangle-Indizes, i = z·res + x;
  zwei Dreiecke pro Gitterquadrat, Winding im Uhrzeigersinn (von oben).
- 2026-07-18 — [Mesh] Verifikation über drei Tests: flach (Kette steht),
  random (Höhen kommen an; Stachel-Chaos motiviert Perlin Noise), Rampe
  (Richtung stimmt). Rampen-Test deckte [z,x]/[x,z]-Mismatch zwischen
  Schreiber und Leser auf → Konvention festgelegt.
- 2026-07-18 — [Mesh] Praxisgrenzen: 16-Bit-Indexpuffer max. 65.535
  Vertices (res ≤ 255 oder IndexFormat.UInt32); SerializeField-Typwechsel
  resettet den Inspector-Wert.
- 2026-07-18 — [Architektur] Mesh komplett im Code statt Unity-Terrain
  oder Mesh-Asset (Begründung in DECISIONS 2026-07-18).
- 2026-07-18 — [Terrain] HeightmapGenerator: statisch, oktavierter Perlin
  Noise. Kernformeln: Amplitude = persistence^o, Frequenz = lacunarity^o
  (per `*=` in der Schleife), Summe / Amplitudensumme → Ergebnis bleibt
  0–1. Seed → System.Random → ein Offset pro Oktave
  (Mathf.PerlinNoise ist seedlos).
- 2026-07-18 — [Terrain] Verifikation über drei Tests: Determinismus
  (gleicher Seed = gleiches Terrain), Seed-Variation (anderes Terrain),
  Oktaven 1 vs. 6 (mehr Detail, gleiche Höhe — Beweis der Normalisierung).
- 2026-07-18 — [Terrain] Parameter-Guards per [Min]/[Range] im Inspector:
  resolution ≥ 2, noiseScale > 0, octaves ≥ 1 (alle drei verhindern
  Division durch null), lacunarity ≥ 1 (sonst kehren sich Oktaven um).
  Oktaven über ~6 bringen keinen sichtbaren Mehrwert (0.5⁹ ≈ 0,2 %),
  kosten aber linear Rechenzeit.
- 2026-07-18 — [Architektur] TerrainConfig als ScriptableObject-Parameter-
  Object: alle Pipeline-Einstellwerte in einem Asset, Konsumenten lesen
  dieselbe Quelle (Get-only-Properties); mehrere Assets = tauschbare
  Presets ohne Code-Change. Generator-Signatur: Generate(TerrainConfig).
- 2026-07-18 — [Terrain] heightCurve (AnimationCurve): remappt das
  normalisierte 0–1-Profil per Evaluate — nach der Oktaven-Normalisierung,
  vor der Meter-Skalierung im MeshBuilder. x²-Intuition: jeder Wert „mal
  sich selbst" → Täler sacken ab (0,2→0,04), Gipfel bleiben (0,9→0,81),
  Terrain wird dramatischer. Verifiziert per Kurven-Biege-Test.
- 2026-07-18 — [Planung] Ziel-Bild des kombinierten Tools (PCG + Engine-
  Tool, siehe DECISIONS 2026-07-18): Terrain mit Bergen und Tälern,
  später evtl. Straßen/Wege; Start-Village mit Haus-Asset am Spawnpunkt;
  Bäume und Gras platzieren, an Flüssen passender Shader/Material;
  vorhandene Partikeleffekte (Glühwürmchen, Fackeln) an ausgewählten
  Stellen. Abgabe braucht zusätzlich: Tool-Beschreibung im TDD, UML-
  Klassendiagramm, Ablaufdiagramm, mind. ein Design Pattern, Fehlbedienung
  ausgeschlossen oder mit Nutzer-Feedback.
- 2026-07-18 — [Tools] Terrain-Editor-Tool als MVP: View TerrainToolWindow
  (EditorWindow, IMGUI), Presenter TerrainToolPresenter (prüft Config,
  ruft Pipeline, besitzt „Generated Terrain"-Objekt), Model = bestehende
  Pipeline unverändert. Fehlbedienung: Button-DisabledScope + HelpBox;
  Edit-Mode-Fallen: sharedMesh statt mesh, DestroyImmediate,
  [SerializeField] am Config-Feld (Serialisierungs-Bewertungspunkt).
  Liefert fürs TDD: Tool-Beschreibung + Stoff für UML-/Ablaufdiagramm.
- 2026-07-18 — [Tools] Tool fertig und getestet (6-Punkte-Plan inkl.
  Editor-Neustart). IMGUI-Kernmuster fürs TDD: Felder geben ihren neuen
  Wert zurück (`_config = ObjectField(...)`), Buttons feuern nur im
  Klick-Frame, DisabledScope sperrt per using-Klammer garantiert nur
  seinen Bereich. typeof als Typ-Filter des ObjectFields.
- 2026-07-18 — [Tools] URP-Lektion: Magenta = Shader inkompatibel mit
  aktiver Pipeline; Built-in-Materials (Default-Diffuse) funktionieren
  unter URP nicht → GraphicsSettings.currentRenderPipeline.defaultMaterial
  als Fallback, eigentliches Material kommt aus der Config.
- 2026-07-18 — [Tools] Bewusste Grenzen v1 (TDD-Kapitel „Erweiterungen"):
  kein Undo für Generate/Clear; GameObject.Find sieht nur aktive Objekte;
  Auto-Regenerate als Checkbox geparkt (Performance/Absichtsprinzip —
  siehe DECISIONS 2026-07-18).
- 2026-07-19 — [Terrain/Shader] Bekannte Grenze Wasser-Shader (TDD-Kapitel
  „Erweiterungen"): aktueller Shader läuft auf einer flachen Ebene in
  eine Richtung — passend für den geplanten globalen Wasserspiegel
  (Seen/Talwasser, siehe DECISIONS 2026-07-18), nicht für echte Flüsse
  mit Flussbett-Kurven. Für Flüsse bräuchte es ein eigenes, entlang eines
  Splines gebautes Mesh (Mesh-Baustein vor der Shader-Anpassung) — bleibt
  Kür nach der formativen Abgabe, kein Shader-Nachbessern.
- 2026-07-19 — [Terrain] PlateauModifier: Modifier-Stufe zwischen
  Generator und MeshBuilder, schreibt in-place in die Heightmap.
  Kernformeln: Position normiert auf 0–1 (x/(res−1), Cast Pflicht gegen
  Integer-Division), Distanz zum Center via Vector2.Distance; drei Fälle:
  innen → Zielhöhe, Ring → Lerp(PlateauHeight, original, t) mit
  t = (dist − radius)/blend, außen → unangetastet. Lerp-Richtung: t=0 an
  der Plateau-Kante = volle Plateauhöhe.
- 2026-07-19 — [Architektur] Nicht-destruktive Pipeline: Modifier
  schreiben vor dem Mesh-Build, danach ist die Heightmap read-only —
  das Mesh ist ein Schnappschuss, keine Live-Verbindung (zwei
  Wahrheitsquellen vermeiden). Änderungen gehen in die Quelldaten
  (Config/Modifier), dann läuft die Pipeline komplett neu; Determinismus
  (Seed) macht das Original jederzeit reproduzierbar — Löschen eines
  Modifiers = Eintrag streichen + neu generieren.
- 2026-07-19 — [Terrain] Plateau-Guards: radius Min(0) mit 0 als
  gewolltem Aus-Schalter (kein Extra-Bool); blend Min(0.001) sichert die
  Division in t ab — statt sich auf die Zweig-Reihenfolge zu verlassen
  (gleiche Linie wie noiseScale: falscher Wert entsteht gar nicht erst).
  Pipeline-Klassen loggen nicht (siehe DECISIONS 2026-07-19).
- 2026-07-19 — [Terrain] Chunk-Entscheidung: Welt 2048 m Kante, Start
  2 m/Quad → 8×8 Chunks à 129 Vertices (16.641/Chunk, ~1,06 Mio gesamt);
  1 m/Quad = 16×16 Chunks per Inspector. Begründung: 16-Bit-Limit
  65.535 Verts/Mesh (max. 255×255) hieße ~8 m/Quad bei 2 km — zu grob;
  Chunks liefern Culling + Thread-Granularität. Threading bewusst ans
  Ende: langsame Version = Baseline-Messdaten für die Threading-Abgabe.
- 2026-07-19 — [Terrain] Chunk-Nahtlosigkeit: Noise nach Weltposition
  sampeln, nie nach lokalem Chunk-Index — Nachbarränder fragen identische
  Weltkoordinaten ab → identische Höhen, Naht gratis. Bekannte Baustelle:
  RecalculateNormals kennt nur das eigene Chunk-Mesh → Beleuchtungsnaht;
  Lösung: Normalen aus der Heightmap rechnen, eine Reihe Überlappung.
- 2026-07-19 — [Terrain] Wasserspiegel-Design: waterLevel 0–1 (Vergleich
  nach der HeightCurve), Plane auf waterLevel × heightMultiplier mit
  eigenem Shader-Graph-Material; _waterEnabled-Bool; OnValidate-Warnung
  bei PlateauHeight <= WaterLevel; Margin für kahlen Uferstreifen als
  Platzierungs-Input (platzieren erst ab height > waterLevel + margin).
  0–1 statt Meter: Wasser skaliert mit der Karte, Uferlinie bleibt bei
  Multiplier-Änderungen exakt gleich.
- 2026-07-19 — [Terrain] Chunk-Umbau umgesetzt und visuell verifiziert
  (keine Geometrie-Nähte). Kernformeln: globaler Vertex-Index =
  chunk × (chunkRes − 1) + lokal (Nachbarn teilen die Randreihe),
  Weltposition = Index × MetersPerQuad; abgeleitete Config-Properties
  (MetersPerQuad, ChunkSizeInMeters) halten die Formeln an einer Stelle.
  Presenter: pro Generate kompletter Rebuild des Terrain-Roots — Reuse
  hinterließe bei Chunk-Zahl-Wechsel verwaiste Kinder. ~1,06 Mio Verts
  blockierend in einem Rutsch = Baseline-Messung für Threading-Abgabe.
- 2026-07-19 — [Terrain] Platzierung entkoppelt von Auflösung: Objekte
  stehen in Weltkoordinaten (beliebige floats), die Heightmap ist nur
  das interpolierte Höhen-Nachschlagewerk (Mischung der Nachbarpunkte,
  gewichtet nach Nähe). Auflösung bestimmt Bodenform-Detail und
  Steigungs-Glättung, nicht die Platzierungs-Präzision.
- 2026-07-19 — [Terrain] Float-Präzisions-Terracing: Perlin bei Sample-
  Koordinaten ~100000 löst float nur in ~0.008er-Schritten auf; bei 2 m/Quad
  ist der Sample-Schritt 2/NoiseScale ≈ 0.004 < 0.008 → Nachbarvertices runden
  auf denselben Wert → Terrassen (nur bei feiner Auflösung, nicht bei grober).
  Fix: Octave-Offsets klein halten (±10000). Lektion: großer Zahlenbereich +
  kleiner Abstand = Präzisionsverlust.
- 2026-07-19 — [Terrain/Mesh] Nahtlose Beleuchtung: RecalculateNormals ist pro
  Mesh lokal → Chunk-Kanten unterschiedlich beleuchtet. Lösung: Heightmap mit
  1-Vertex-Randring (Nachbar-Weltpositionen), Normalen analytisch per zentraler
  Differenz normal = normalize(hL−hR, 2·spacing, hD−hU); geteilte Kante rechnet
  in beiden Chunks identisch. Padding-Mapping: Arraygröße res+2, Weltindex =
  chunk·(res−1)+(lokal−1). Erledigt die Baustelle aus dem Chunk-Eintrag.
- 2026-07-19 — [Terrain] HeightCurve-Clamp: AnimationCurve kann zwischen
  gültigen Keys über-/unterschwingen (Attribut greift nicht) → Laufzeit
  Mathf.Clamp01 nach Evaluate. Bewusste Ausnahme zur Inspector-Guard-Linie.
- 2026-07-19 — [Terrain] Finaler Tuning-Look „ein bis mehrere Bergmassive":
  NoiseScale ~460–600, HeightMultiplier 700, Octaves 5, Persistence ~0.28–0.36,
  HeightCurve mit flacher Basis + spätem Anstieg, Seed durchprobieren.
  Verhältnis Höhe:Breite ~25 % (wie das Referenz-Terrain); Seed steuert die
  Lage der Massive, gezielte Platzierung bräuchte einen Mask-Modifier (Kür).
- 2026-07-21 — [Platzierung] Design der Platzierungs-Stufe: ObjectPlacer reine
  statische Stufe (Geschwister zu MeshBuilder), zwei Datentypen — Placeable
  (class, Config-Array: prefab, min/maxHeight, maxSlope, minSpacing,
  scaleMin/Max, alignToGround, DensityStrategy) → Placement (struct: prefab,
  position, rotation, scale); Presenter instanziiert. Verteilung: globales
  Poisson-Disc (garantierter Mindestabstand), Ergebnis pro Chunk einsortiert.
- 2026-07-21 — [Platzierung] SampleHeight(config, x, z) als gemeinsame Höhen-
  Funktion (Noise→Curve→Plateau an einem Punkt) für Chunk-Schleife und Placer;
  Steigung/Ausrichtungs-Normale aus 4 Nachbar-Samples (zentrale Differenz, wie
  MeshBuilder) — eine Rechnung, zwei Zwecke. Funktion statt Cache: Placer fragt
  nur ~9.600 Punkte (gegen ~1,05 Mio Gitterzellen), ein Cache veraltet.
- 2026-07-21 — [Platzierung] Ein Poisson-Durchgang pro Typ (eigener Radius),
  Reihenfolge=Priorität, Blocker-Liste für späteren Inter-Typ-Ausschluss (jetzt
  leer). Regel-Filter je Kandidat billig→teuer: Wasser-Untergrenze (global,
  height ≥ waterLevel + shoreMargin, nur bei isWaterEnabled) → Höhenband
  (max(Wasser, minHeight)…maxHeight) → Steigung (≤ maxSlope).
- 2026-07-21 — [Pattern] Zweites Design-Pattern fürs TDD: Strategy —
  DensityStrategy (ScriptableObject, AcceptanceProbability(x,z)→0–1) mit
  Uniform/NoiseMask/Probability. Dichte-Variation als Wahrscheinlichkeits-
  Ausdünnung statt variablem Poisson-Radius; offen/geschlossen: neue Art = neues
  Asset, Placer unberührt.
- 2026-07-21 — [Tools] Panel-Ausbau: Generate Complete + Einzel-Stufen (Terrain/
  Wasser/Place) + pro-Typ Place/Clear aus Liste 1 erzeugt (datengetrieben, nicht
  fest verdrahtet); „Place Objects" ohne Terrain-Rebuild (inkrementelles
  Generieren), eigene „Generated Placement"-Wurzel; eigener placementSeed
  getrennt vom Terrain-Seed → Verteilung neu würfeln ohne Rebuild.
- 2026-07-23 — [Platzierung/Architektur] SampleHeight umgesetzt: aus dem
  HeightmapGenerator herausgezogen als geteilte reine Funktion
  SampleHeight(config, offsets, worldX, worldZ) → Höhe an beliebiger Welt-
  position. Schlüssel für die Teilbarkeit: worldX/worldZ als Parameter (nicht
  Gitter-Index) — nur so kann sowohl die Chunk-Schleife (rechnet Index→Welt)
  als auch der Placer (freie Weltkoordinaten) dieselbe Funktion rufen. Offsets
  einmal gebaut (seed-abhängig, für alle Punkte gleich), als Parameter gereicht;
  kein Klassen-Zustand (thread-tauglich, pure).
- 2026-07-23 — [Architektur/Pattern] DRY vs. SRP aufgelöst per Komposition:
  SampleHeight ist ein dünner Dirigent (Noise+Curve, dann PlateauModifier.
  SampleAt); die Plateau-Rechnung bleibt in PlateauModifier (von Array-Stufe
  Apply zu Punkt-Funktion SampleAt umgebaut). Trennung nach Job (SRP) + Teilen
  über einen Einstiegspunkt (DRY) — kein Gott-Objekt, keine Doppel-Logik.
- 2026-07-23 — [Platzierung] Datentypen gebaut: Placeable (class, [Serializable],
  Array in TerrainConfig, [SerializeField]+Tooltip+[Range]/[Min], Get-only-
  Properties) als Rezept; Placement (struct, unveränderlich per Konstruktor +
  Get-only) als Ergebnis. class für Inspector-Serialisierung, struct gegen
  Garbage bei tausenden Instanzen. DensityStrategy-Feld bewusst aufgeschoben
  bis zum Strategy-Baustein (kein Verweis auf noch nicht existierenden Typ).
- 2026-07-23 — [Platzierung] ObjectPlacer gebaut: reine statische Stufe,
  `Place(config)` → List<Placement>. Pro Typ ein globaler Poisson-Durchgang,
  Reihenfolge = Priorität, eigener `System.Random(placementSeed + i)`
  (deterministisch, getrennt vom Terrain-Seed).
- 2026-07-23 — [Platzierung/Algorithmus] Poisson-Disc nach Bridson: Beschleunigungs-
  Gitter Zellgröße r/√2 (Diagonale = r → max. 1 Punkt/Zelle), Zelle speichert
  sampleIndex+1 (0 = leer). Active-Liste als Front: zufälligen Punkt greifen, bis
  zu 30 Würfe im Annulus [r, 2r] (Winkel + Abstand), ersten gültigen setzen, sonst
  pensionieren. Kandidat gültig = in der Karte UND kein Nachbar < r; Nachbar-Check
  nur im 5×5-Zellblock (Konflikt sitzt höchstens 2 Zellen weit) → O(n) statt O(n²).
- 2026-07-23 — [Platzierung] Regel-Filter billig→teuer je Kandidat: Wasser-
  Untergrenze (nur bei isWaterEnabled, height ≥ waterLevel + shoreMargin) →
  Höhenband (minHeight…maxHeight) → Steigung (≤ maxSlope). Steigung zuletzt, weil
  sie über SampleNormal vier weitere SampleHeight-Aufrufe kostet.
- 2026-07-23 — [Platzierung] SampleNormal: Normale per zentraler Differenz aus vier
  Nachbarhöhen (in Meter, × heightMultiplier), normal = normalize(hL−hR, 2·spacing,
  hD−hU); Steigung = Vector3.Angle(normal, up). Placement-Rotation: zufälliger Yaw;
  optional FromToRotation(up, normal) * Euler(yaw) — Tilt links, Yaw rechts, denn
  Quaternion-Multiplikation ist nicht vertauschbar (falsche Reihenfolge schwenkt die
  Achse von der Normale weg). Scale = Lerp(min, max, rand).
- 2026-07-25 — [Pattern] Strategy umgesetzt: DensityStrategy (abstract SO,
  AcceptanceProbability(x,z)→0–1) + UniformDensity/ProbabilityDensity/
  NoiseMaskDensity. Der Placer ruft nur die Basis, kennt die Konkreten nicht →
  neue Dichte-Art = neues Asset, ObjectPlacer unberührt (Open/Closed; zweites
  Muster fürs TDD neben MVP). float statt bool: die Gewichtung braucht die
  Abstufung, der Würfel sitzt an einer Stelle im Placer (Determinismus über
  einen Seed-Strom, feste Ziehungsreihenfolge). NoiseMask: Perlin liefert von
  Haus aus ~0–1 = fertige Wahrscheinlichkeit; Seed→Offset (wie
  BuildOctaveOffsets, ±10000 gegen Float-Terracing), Scale zoomt die Wolken;
  Offset in OnEnable/OnValidate gecacht — abgeleiteter Cache, kein
  veränderlicher Zustand. Dichte-Stufe billig→teuer vor der Steigung.
- 2026-07-26 — [Tools] Panel fertig: MVP bleibt tragend — die View zeichnet nur
  und kennt keine Objektnamen, der Presenter besitzt die Szenen-Objekte. Vier
  Absichts-Methoden als Überladungspaare (PlaceObjects/ClearObjects je alle bzw.
  ein Typ) statt eines öffentlichen `Clear(string)`: der Aufrufer nennt die
  Absicht, nie den Namen — der Tippfehler kann gar nicht entstehen. Pro-Typ-
  Zeilen werden aus dem `Placeables`-Array erzeugt (datengetrieben: neuer Typ =
  neue Zeile ohne Code-Change). Fürs UML: TerrainToolWindow → TerrainToolPresenter
  → {HeightmapGenerator, MeshBuilder, ObjectPlacer}; Einbahnstraße, das Model
  kennt weder View noch Presenter.
- 2026-07-26 — [Tools] Hierarchie als Aufräum-Mechanismus: „Generated Placement"
  ist Kind des Terrain-Roots, darunter eine Gruppe je Typ. Terrain-Regenerieren
  zerstört den Root und nimmt die veraltete Platzierung automatisch mit — kein
  eigener Invalidierungs-Code. Einzel-Typ-Place leert nur seine Gruppe (kein
  Clear der Wurzel), damit Tunen eines Typs die anderen stehen lässt.
  `transform.Find` statt `GameObject.Find` für Kinder: sucht nur im Teilbaum,
  immun gegen gleichnamige Objekte anderswo.
- 2026-07-26 — [Platzierung] Prefab-Transform komponieren statt ersetzen:
  Instanz-Rotation = placement.Rotation * prefabRotation, Scale = prefabScale *
  placement.Scale. Quaternion-Reihenfolge ist nicht vertauschbar — rechts steht,
  was zuerst wirkt (Achsen-Korrektur aufrichten), links das Nachträgliche (Yaw,
  Boden-Neigung). Umgekehrt kippt die Korrektur die bereits zufällig gedrehte
  Achse. Gleiche Lektion wie bei FromToRotation × Euler(yaw) vom 23.07.
- 2026-07-26 — [Assets] Blender→Unity Achsen-Falle (TDD-Kapitel „Erweiterungen"/
  Lessons Learned): Blender ist Z-up, Unity Y-up. Blenders FBX-Exporter
  konvertiert bereits; Unitys Import-Option „Bake Axis Conversion" ist für
  *nicht* konvertierte Dateien gedacht und dreht eine korrekte Datei ein zweites
  Mal um −90° → Modell liegt. Zweite Falle: eine Korrektur-Rotation am Prefab-
  Root wird von jedem prozeduralen Placer überschrieben, der Rotation absolut
  setzt. Prüfreihenfolge: Modell in Blender bei Rotation 0 aufrecht (Stamm
  entlang +Z, Ursprung am Fuß) → Import-Optionen → erst dann den Code verdächtigen.
- 2026-07-26 — [Performance] Baseline für die Threading-Abgabe: 211.000
  Gras-GameObjects bei minSpacing 2,7 auf 2048 m machen den Editor zäh. Anzahl
  wächst quadratisch zum Abstand (~Fläche/(1,3·r²)): 2,7 m ≈ 211.000, 8 m
  ≈ 25.000, 12 m ≈ 11.000. Kostentreiber ist nicht primär das Rendering, sondern
  die Objektanzahl selbst (Hierarchie-Fenster, Transforms, Undo, Serialisierung)
  — GPU Instancing adressiert nur die Draw Calls und greift unter URP oft gar
  nicht, weil der SRP Batcher Vorrang hat. Struktureller Weg: die Placement-Liste
  direkt instanziert zeichnen, ohne GameObjects; hinter dem Presenter kapselbar.
- 2026-07-30 — [Interaktion] Aufbau des Systems (TDD-Kapitel Architektur):
  `IInteractable` (Prompt / CanInteract / Interact) ist die einzige Berührungs-
  linie zwischen Spieler- und Objektseite — der Spieler kennt keine Schafe, die
  UI kennt nur einen string. Vier Teile: Vertrag (Interface), Sucher
  (`PlayerInteractor`, Raycast aus der Kamera, Reichweite + LayerMask), Anzeige
  (`InteractionPromptView`, Event-Abonnent), Adapter (`SheepInteractable`,
  delegiert an `Sheep`). Alternative Bauform Trigger-Collider beantwortet „was ist
  nah", der Strahl „was schaue ich an" — für First Person mit Fadenkreuz richtig.
- 2026-07-30 — [Interaktion] Drei Fallen mit Beleg im eigenen Code:
  (1) `GetComponentInParent` sucht nur **aufwärts** — der Collider darf tiefer
  sitzen als das Script, nie höher; sonst kein Treffer, keine Fehlermeldung.
  (2) Unitys `==`-Überschreibung für zerstörte Objekte sitzt auf
  `UnityEngine.Object`, nicht auf dem Interface → Cast vor dem Null-Check.
  (3) Event-Abonnent muss den Startwert selbst nachziehen, weil Events erst bei
  der nächsten Änderung feuern; jedes `+=` braucht sein `-=` im Gegenstück.
- 2026-07-30 — [Interaktion] Prompt-Aktualisierung: `ReferenceEquals(target,
  _currentTarget)` als Abbruchbedingung reicht nur, solange ein Objekt seinen
  Prompt nie ändert. Fackel an/aus ändert ihn bei gleichbleibendem Ziel → Text
  friert ein. Fix: Ziel **und** Prompt vergleichen (ein String-Vergleich/Frame).
  Lektion fürs TDD: „Quelle unverändert" ist nicht dasselbe wie „Ergebnis
  unverändert" — dieselbe Cache-Invalidierungs-Frage wie beim Höhen-Cache.
- 2026-07-30 — [Tools/Navigation] NavMesh gegen generierte Welt (TDD-Kapitel
  Erweiterungen/Lessons Learned): Der `NavMeshSurface` lag auf „Generated
  Terrain" — dem Objekt, das der Presenter bei jedem Generate per
  `DestroyImmediate` ersetzt. Folge: Bake-Asset bleibt auf der Platte, ist aber
  an nichts mehr angeschlossen; Agents verlieren den Boden ohne Konsolenfehler.
  Bake-Kosten skalieren quadratisch mit der Kantenlänge (Voxel 0,1667 m:
  2048 m ≈ 151 Mio Spalten, 1024 m ≈ 38 Mio, 512 m ≈ 9,4 Mio). Daraus die
  Reihenfolge Weltgröße final → backen → NPCs. Tool-Kandidaten, die echte
  Handarbeit sparen (Bewertungspunkt der Tool-Aufgabe): „Bake NavMesh" und
  „Village aufs Plateau setzen".
- 2026-07-30 — [Architektur] Szenen-Vertrag: generierter Ast (Tool-Eigentum,
  wegwerfbar) gegen handgebauten Ast (Village-Prefab, Navigation, Player, Game).
  Nebenregel mit Konsequenz fürs Design: Ein Prefab darf keine Referenz in die
  Szene halten (nur Szene → Prefab). Alles, was aus dem Village-Prefab heraus auf
  Spieler oder GameController zeigen müsste, braucht ein ScriptableObject als
  Treffpunkt oder eine Laufzeit-Suche.
- 2026-08-04 — [Rendering] Gras ohne GameObjects: `Graphics.RenderMeshInstanced`
  (Unity 6; `DrawMeshInstanced` überholt) zeichnet max. 1023 Instanzen je
  Aufruf → Schleife in 1023er-Fenstern über das Matrix-Array (start/count als
  Parameter, Array bleibt ganz). Material braucht „Enable GPU Instancing",
  sonst `InvalidOperationException`. Aufruf gilt nur einen Frame → `Update` +
  `[ExecuteAlways]` für den Editor.
- 2026-08-04 — [Rendering] Culling je Zelle statt je Instanz:
  `RenderParams.worldBounds` ist die Einheit, die Unity prüft. Eigenes
  Zellgitter, nicht das Chunk-Gitter (1023er-Batchgrenze vs.
  65.535-Vertexgrenze — zwei Zwänge, zwei Gitter; optimale Kante =
  √(1023 / Dichte je m²)). Bounds aus den Fußpunkten wachsen lassen
  (Encapsulate) + Halmhöhe als Padding (`mesh.bounds.size.y ×
  prefabScale.y × ScaleMax`), sonst cullt die Box Halmspitzen weg.
  Zellgröße als Regler: kleiner = präziseres Culling (auch hinter der
  Kamera), mehr Draw Calls.
- 2026-08-04 — [Performance] Dreiecks-Budget schlägt Draw Calls: Instancing
  senkte die Aufrufe (138 Draw Calls für 27k Instanzen vs. 770 für 770
  GameObjects), aber 190k Büschel × 2.664 Tris = 507 Mio Dreiecke → 4,5 FPS,
  GPU-limitiert. Fix: LOD-Meshpaar (Halm 20/7 Tris, Referenzsysteme nutzen
  1–9) + Distanzwahl je Zelle → ~12 Mio Tris, 87+ FPS. Lektion: zwei Regler
  multiplizieren sich (Halme je Büschel × Büschelzahl); Editor-Stats waren
  der Beweis, Profiler-Zahlen im Editor dagegen von EditorLoop/Deep Profile
  dominiert — echte Messung nur im Development Build.
- 2026-08-04 — [Architektur] Rendering-Zerlegung wie die Platzierung:
  Settings als Datenkomponente am Prefab (`GrassRenderProfile`), Entscheidung
  als eigene statische Stufe (`GrassLodSelector`: Zelle+Kamera+Profil →
  None/High/Low), Renderer zeichnet nur. Unitys LODGroup unbrauchbar ohne
  Renderer-Komponenten; Mesh LOD (forceMeshLod) verworfen wegen
  Auto-Vereinfachung. Gleicher Schnitt wie GPU Instancer (LODGroup als
  Datenquelle, eigene Umschaltung).
- 2026-08-05 — [Platzierung] PlacementExclusion als Filterstufe zwischen
  Placer und Konsumenten: Komponente am Objekt bringt die Freifläche mit
  (Kreis/Box; `Contains` in der Komponente — neue Form ändert den Filter
  nicht, gleiche Offen/Geschlossen-Linie wie DensityStrategy). Rand = halbe
  Objektbreite, sonst gilt nur „Mittelpunkt frei", nicht „Fläche frei" —
  breite Büschel ragen sichtbar über die Kante.
- 2026-08-05 — [Platzierung] Perlin braucht Kontrast: roh liegen die Werte
  bei ~0,35–0,65 → als Annahme-Wahrscheinlichkeit „überall ≈ 50 %",
  gleichmäßiges Rauschen statt Flecken; Scale ohne sichtbaren Effekt
  (Beleg: 266k/265k/276k Objekte bei Scale 5/100/600). Remap-Kurve
  (0,42→0, 0,58→1) erzeugt echte Kahl-/Dichtflächen, erst dann steuert
  Scale die Fleckengröße.
- 2026-08-05 — [Platzierung] Instancing-Parität mit dem GameObject-Weg:
  Prefab-Root-Scale und -Rotation in die Matrix komponieren
  (`prefabScale * placement.Scale`) — vergessen = Gras 3,3× zu groß bei
  Root-Scale 0,3. Dritte Stelle derselben Lektion „komponieren statt
  ersetzen" (nach FromToRotation×Yaw und SpawnType); Konsequenz: abgeleitete
  Größen (Halmhöhe fürs Bounds-Padding, Exclusion-Rand) müssen die
  Prefab-Scale mitrechnen.
- 2026-08-05 — [Performance] Messmethodik der Threading-Abgabe: Messobjekt ist
  der Gras-Rebuild beim Szenenstart (`InstancedRenderer.Rebuild`), Stoppuhren je
  Stufe, Ausgabe per `Debug.Log` in `#if UNITY_EDITOR || DEVELOPMENT_BUILD`
  (Dozenten-Regel „keine Logs im Release" bleibt erfüllt, Messung im Development
  Build trotzdem möglich). Vier Läufe je Build, erster verworfen (JIT + kalte
  Caches, im ersten Lauf durchweg der langsamste `cellbuild`), Mittel aus 2–4.
  Konstanten mitloggen — Kernzahl, Kachelanzahl, Punktzahl —, sonst sind die
  Logs zweier Builds hinterher nicht mehr auseinanderzuhalten.
- 2026-08-05 — [Performance] Messreihe Threading (RTX 4060, 8 Kerne/16 Threads,
  Unity 6000.5.2f1), Ladezeit je Rebuild: Baseline 122,7 s → punktweise
  parallelisierter Filter 118,1 s (−3,7 %) → Kachelung ohne Threads 98,9 s
  (−19,4 %) → Kachelung mit `Parallel.For` 16,5 s (−86,6 %) → plus entschärfter
  Exclusion-Filter 12,4 s (−89,9 %). Die getrennte Zwischenmessung „gekachelt,
  aber sequenziell" trennt den Cache-Effekt (−19,4 %) vom Thread-Effekt
  (Kachel-Durchgang 9,2× schneller) — ohne sie wäre beides nicht auseinander-
  zuhalten.
- 2026-08-05 — [Performance] Amdahl als Leitfaden statt als Nachwort: Die erste
  Optimierung (Filter punktweise über den Thread-Pool) scheiterte nicht am
  Threading, sondern daran, dass der sequenzielle Poisson-Pass 84 % der Laufzeit
  hielt — der maximal mögliche Gewinn lag damit bei 16,6 %, gemessen wurden
  3,7 %. Konsequenz: nicht die parallelisierbare Stelle suchen, sondern die
  teure Stelle parallelisierbar *machen*.
- 2026-08-05 — [Platzierung/Algorithmus] Poisson kachelweise statt global: Die
  Welt wird in 8×8 Kacheln geteilt (`PlacementTilesPerAxis`, 1 = altes
  Verhalten), jede Kachel sampelt und filtert für sich, `Parallel.For` läuft über
  die Kacheln. Zwei Effekte: das Poisson-Beschleunigungsgitter schrumpft von
  ~94 MB (4860²) auf ~1,5 MB je Kachel (610²) und passt in den Prozessor-Cache;
  und der bis dahin unantastbar sequenzielle Teil wird parallelisierbar, weil
  Kacheln einander nicht lesen. Preis: an Kachelgrenzen kann der Mindestabstand
  verletzt werden (~28 km Nahtlänge bei 8×8, bei 7,4 Mio Halmen unsichtbar);
  Lösung wäre ein Aufräumpass nur über die Randstreifen. Kachelzahl 64 begründet
  über drei Größen: Lastverteilung (4 Pakete je Thread reichen), Cache-Größe,
  Nahtlänge (verdoppelt sich mit jeder Halbierung der Kachelgröße).
- 2026-08-05 — [Performance/Threading] Vier Fallen, alle im eigenen Code belegt:
  (1) `AnimationCurve.Evaluate` cacht intern den zuletzt getroffenen Keyframe →
  zwei Threads liefern sich falsche Werte, ohne Fehlermeldung. Lösung
  `CurveLookup`: Kurve einmal auf dem Main Thread in ein `float[]` abtasten,
  danach nur noch lesen. (2) Ein geteiltes `System.Random` ist nicht thread-sicher
  *und* macht die Reihenfolge ergebnisrelevant → je Kachel ein eigener Generator,
  Seeds vorab gezogen. (3) Unitys `==`-Überladung auf Assets greift in nativen
  Code → `Density != null` vor der Schleife auswerten. (4) `transform.position`
  ist kein Feldzugriff: der Exclusion-Filter fragte ihn 7,4 Mio mal für einen
  Wert ab, der sich nie ändert (2,57 s → 0,97 s nach dem Auflösen in
  `ExclusionArea`). Gemeinsames Muster aller vier: was sich nicht ändert, einmal
  auf dem Main Thread auflösen, danach nur noch rechnen.
- 2026-08-05 — [Performance] Verworfener Versuch (gehört ins TDD, weil er die
  Methodik zeigt): Ergebnisliste des Placers vorab auf Endgröße setzen
  (`Capacity`). Gemessen 12,2 s gegen 12,4 s — 1,8 %, innerhalb der Streuung,
  zwei von drei Stufen sogar langsamer. Ursache: Die Liste wird per `AddRange`
  gefüllt, nicht per einzelnem `Add`; `AddRange` kennt die Elementzahl vorher und
  wächst in einem Schritt. Änderung zurückgenommen. Beim Exclusion-Filter griff
  dasselbe Argument dagegen, weil dort einzeln angehängt wird.
