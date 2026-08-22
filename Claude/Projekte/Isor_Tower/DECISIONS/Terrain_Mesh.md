# Terrain_Mesh.md — Entscheidungen Terrain und Mesh

Ownership: Nur Entscheidungen zu Terrain und Mesh — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Nicht hier: was auf dem Terrain platziert wird (`Platzierung.md`) und die
Szene drumherum (`Welt.md`). **Alles, was das Terrain-Tool baut, gehört
hierher** — auch Wasserspiegel und Weltbegrenzung, die thematisch nach
Welt klingen.
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

Gilt eine Begründung weiter und ist nur ihre Ausführung überholt, bleibt
der Eintrag stehen und bekommt eine Zeile **Fortgeführt am `<Datum>`**
mit Zeiger auf die geltende Fassung — dann geht die Herleitung nicht ins
Archiv verloren.



## 2026-07-18 — Terrain-Mesh komplett im Code
Was: Kein Unity-Terrain und kein vormodelliertes Mesh-Asset — MeshBuilder
erzeugt das Mesh vollständig aus der Heightmap.
Warum: Höhen ändern sich pro Seed, Größe/Auflösung kommen aus der Config —
ein Asset müsste trotzdem per Code verformt werden; MeshCollider braucht
passende Geometrie; Mesh-Generierung ist Kern der Uni-Aufgabe.
Verworfen: Unity-Terrain; unterteilte Plane als Basis-Asset.

## 2026-07-18 — Heightmap-Konvention: [x, z], quadratisch, ein int
Was: Erster Index = x, zweiter = z — projektweit für alle Heightmap-Zugriffe;
Auflösung als einzelner int statt Vector2Int.
Warum: Rampen-Test zeigte 90°-gedrehtes Terrain, weil Schreiber [z, x] und
Leser [x, z] benutzten; MeshBuilder setzt Quadrate voraus — ungültige
Rechteck-Auflösungen sollen gar nicht erst einstellbar sein.
Verworfen: freie Index-Reihenfolge pro Klasse; Vector2Int-Resolution.

## 2026-07-18 — TerrainConfig flach, nur lesbar, Guard beim Aufrufer
Was: TerrainConfig als ein flaches SO ([Header]-Gruppen, kein Nesting),
Zugriff nur über Get-only-Properties (`=> _feld`); die Null-Prüfung der
Referenz macht der Aufrufer (TerrainPreview in Awake und Start),
nicht der Generator. MeshBuilder bleibt config-agnostisch (Primitive).
Warum: Nesting/Setter ohne aktuellen Nutzen (YAGNI); Schreibzugriffe
würden im Editor das Asset dauerhaft ändern; ein Guard im Generator käme
nach dem ersten Zugriff zu spät und ein Ersatz-Array würde den Fehler
verstecken — beim Aufrufer sitzt die vergessbare Inspector-Verdrahtung.
Verworfen: verschachtelte [Serializable]-Unterklassen (Skizze vom
16.07.), public Felder/Setter, Guard mit 1×1-Fallback im Generator.

## 2026-07-18 — Editor-Tool vor Platzierungs-Stufe
Was: Reihenfolge bis Ende Juli: 1. minimales Editor-Tool, 2. Platzierung
(Bäume/Gras → Village → Partikel), 3. Texturierung (erster
Streichkandidat), 4. TDD + UML. Große Bausteine liegen auf Isors
Wochenend-Fenstern.
Warum: Das Tool beschleunigt jede spätere Iteration (Generieren im Edit
Mode statt Play Mode), die Tool-Aufgabe ist formativ schon überfällig
(Feedback einholbar), und es wächst mit jeder Stufe mit.
Verworfen: erst Platzierung fertig bauen, dann das Tool drumherum.

## 2026-07-18 — Terrain-Tool als MVP mit EditorWindow (IMGUI)
Was: View `TerrainToolWindow` (EditorWindow, OnGUI/IMGUI), Presenter
`TerrainToolPresenter` (einzige Tool-Logik: prüfen, Pipeline rufen,
Terrain-Objekt besitzen), Model = bestehende Pipeline unverändert.
Beides in `Assets/Shared/MeshBuilder/Editor/`. Fehlbedienung:
DisabledScope + HelpBox ohne Config; Neu-Generieren ersetzt das Objekt.
Warum: Aufgabe verlangt ein MV-Pattern an echter Stelle; Einbahnstraßen-
Abhängigkeit hält das Model testbar; IMGUI ist für ein kleines Fenster
der einfachste Weg.
Verworfen: UI Toolkit (mehr Boilerplate ohne Nutzen bei dieser Größe);
Logik direkt im Fenster (Pattern wäre nur Etikett).

## 2026-07-18 — Terrain-Material wohnt in der Config
Was: TerrainConfig hält das Terrain-Material (leer = Default der aktiven
Render-Pipeline); der Presenter weist es bei jedem Generate zu, nicht
nur beim Anlegen des Objekts.
Warum: Material ist eine Preset-Eigenschaft wie Seed/Größe — Config-
Tausch wechselt Terrain und Look gemeinsam; Zuweisung pro Generate,
damit Änderungen ohne Clear sichtbar werden. Built-in-Default-Diffuse
rendert unter URP magenta (Signalfarbe für inkompatiblen Shader).
Verworfen: Material-Feld im Tool-Fenster (zweite Quelle neben der
Config); hartes Default-Diffuse; Auto-Regenerieren bei Config-Änderung
(geparkt als spätere Checkbox — Performance beim Slider-Ziehen,
Absichtsprinzip).

## 2026-07-19 — Pipeline-Klassen loggen nicht
Was: Reine Pipeline-Funktionen (Generator, Modifier, MeshBuilder)
bleiben still — kein Debug.Log, keine Warnings; Nutzer-Feedback ist
Sache der Presenter-Schicht (StatusMessage im Tool).
Warum: Radius 0 ist gewollter Aus-Schalter, kein Fehler; Logs in
Zellen-Schleifen wären Spam; was nie geloggt wird, muss für die
Uni-Abgabe nie entfernt werden.
Verworfen: Warning bei Radius 0; Debug.Logs mit späterem Ausbau.

## 2026-07-19 — Chunk-Terrain: 2048 m, Start 2 m/Quad, 8×8 à 129
Was: Terrain wird in Chunks gebaut; Config bekommt chunksPerEdge +
chunkResolution statt heightmapResolution. Welt 2048 m Kante, Start-
Detail 2 m/Quad (8×8 Chunks à 129 Vertices); 1 m/Quad (16×16) bleibt
reiner Inspector-Wechsel und wird visuell entschieden. Noise wird nach
Weltposition gesampelt (nahtlose Chunks); Chunks rechnen unabhängig
(thread-tauglich), optimiert wird erst am Schluss — die langsame Version
ist die Baseline-Messung für die Threading-Abgabe (formativ 2026-08-07).
Warum: 16-Bit-Meshes enden bei 65.535 Vertices — ein Einzelmesh kann
2 km nicht in Gameplay-Detail (1–2 m/Quad) darstellen; Chunks liefern
zudem Culling-Granularität. Platzierung erzwingt kein feines Raster:
Objekte stehen in Weltkoordinaten, die Heightmap wird interpoliert
abgefragt.
Verworfen: Einzelmesh mit 32-Bit-Indizes (kein Culling, alles-oder-
nichts-Regenerierung); 1 m/Quad sofort (4× Kosten bei jedem Tuning-
Klick ohne sichtbaren Mehrwert); Threading jetzt (Messdaten fehlten).

## 2026-07-19 — Wasserspiegel: Einheit, Schalter, Darstellung
Was: waterLevel normalisiert 0–1 (verglichen nach der HeightCurve),
_waterEnabled als explizites Bool, Darstellung als eine Plane auf
waterLevel × heightMultiplier mit Isors vorhandenem Shader-Graph-
Wassershader (_waterMaterial), OnValidate-Warnung wenn
PlateauHeight <= WaterLevel, Uferstreifen-Margin kommt mit in die
Config (visuell bewertet erst mit der Platzierungs-Stufe). Ergänzt
DECISIONS 2026-07-18 „Formen vor Reagieren".
Warum: 0–1 hält das Wasser im Verhältnis zur Karte — Multiplier-
Änderungen verschieben die Uferlinie nicht; das Bool erhält den
eingestellten Level beim Ausschalten; der eigene Shader existiert und
passt (Schaum zeichnet die Uferlinie).
Verworfen: Meter-Wert (Seen schrumpfen beim Hochskalieren); 0-als-Aus-
Konvention wie beim Plateau (Wert ginge beim Ausschalten verloren);
gekaufte Fluss-Assets für die Abgabe (bewertet wird eigener Code;
Flüsse sind eine eigene Pipeline-Stufe → Kür nach dem Portfolio).

## 2026-07-19 — HeightCurve clampen, Octave-Offsets begrenzen
Was: Generator wickelt Evaluate in Mathf.Clamp01; Octave-Offsets laufen nur
noch ±10000 (benannte Konstante MaxOctaveOffset) statt ±100000.
Warum: Weiche Kurven-Tangenten schwingen zwischen Keys unter 0/über 1 durch —
per Attribut nicht begrenzbar (bewusste Ausnahme zu „Wertebereiche an der
Eingabe", 2026-07-18), daher Laufzeit-Clamp. Große Offsets sampeln Perlin bei
~100000, wo float gröber auflöst als der 2-m-Vertexschritt → identische
Nachbarwerte → Terrassen bei Auflösung 129 (nicht bei 40).
Verworfen: Kurve ungeclampt lassen; Offsets bei ±100000 (Terracing).

## 2026-07-19 — Nahtlose Normalen über Padding-Ring statt RecalculateNormals
Was: HeightmapGenerator gibt die Heightmap um 1 Vertex gepaddet zurück (Ring =
Nachbarhöhen, nicht im Mesh); MeshBuilder baut nur das Innere und rechnet
Normalen analytisch aus Nachbarhöhen (zentrale Differenz). Mapping: Array-/
Schleifengröße = ChunkResolution+2, Weltmapping bleibt ChunkResolution−1 mit
(index−1)-Versatz.
Warum: RecalculateNormals kennt nur das eigene Chunk-Mesh → doppelte Rand-
Vertices bekommen verschiedene Normalen → Beleuchtungsnaht. Der Ring liefert
beiden Chunks identische Nachbarhöhen an der geteilten Kante → identische
Normale, deterministisch, lokal (kein Cross-Chunk-Nachbearbeiten). Ergänzt
DECISIONS 2026-07-19 „Chunk-Nahtlosigkeit" (Geometrie war schon nahtlos, jetzt
auch die Beleuchtung).
Verworfen: Rand-Normalen nachträglich über alle Meshes mitteln (Cross-Chunk-
Pass, Float-Positionsabgleich, fehleranfällig); Einzelmesh mit 32-Bit-Indizes
(kein Culling).

## 2026-07-29 — Welt-Wahrheit (Seed oder Szene): vertagt, Befund festgehalten
Was: **Keine Entscheidung.** Festgehalten wird nur die Herleitung, damit sie
nicht verloren geht: Aus dem Koop-Modell (GDD — Gast joint in die Welt des
Hosts) folgt, dass beim Join entweder die fertige Welt oder ihre Anleitung
übertragen werden muss; Anleitung (Seed für Floors, Änderungsliste gegenüber
dem Ausgangszustand fürs Village) ist um Größenordnungen kleiner als
Weltdaten. Save-System und Multiplayer-Sync beantworten dieselbe Frage.
Entschieden wird nach der Uni-Abgabe, in einer eigenen Design-Session.
Warum: Die Frage ist noch nicht entscheidungsreif — Multiplayer liegt weit
hinten, und bis dahin können sich Anforderungen und Möglichkeiten ändern.
Bis zur Abgabe hat sie keine Auswirkung. Die bestehenden Entscheidungen
(deterministischer `placementSeed`, keine gespeicherte Placement-Liste,
zustandslose Pipeline) halten die Tür ohnehin offen, ohne Mehrarbeit.
Verworfen: jetzt auf „Seed ist die Wahrheit" festlegen (nicht
entscheidungsreif); den Befund gar nicht festhalten (Herleitung ginge
verloren und müsste neu erarbeitet werden).

## 2026-08-19 — Welt-Begrenzung gehört ins Terrain-Tool, nicht in ein Laufzeit-Skript
Was: Die vier Wände baut der `TerrainToolPresenter` wie den Wasserspiegel,
als Kinder des Terrain-Roots. Kein `MonoBehaviour`, kein Objekt in der Szene,
das jemand verdrahten muss, keine Laufzeitkosten. Zusätzlich ein eigener
Knopf, der nur die Wände neu baut.
Warum (Isors Vorschlag, 2026-08-19): Die Wände gehören zur generierten Welt,
also baut sie der Generator — dasselbe Muster wie `BuildWaterPlane`, und die
Maße kommen aus derselben Config wie das Terrain statt abgetippt zu werden.
Der eigene Knopf ist nötig, weil `ClearGeneratedChildren` beim `Generate`
auch `Generated Placement` löscht: Ohne ihn hätte das Nachrüsten der Wände
die 21.354 platzierten Bäume mitgenommen und einen kompletten Neuaufbau der
139,7-MB-Szene zwei Tage vor der Frist erzwungen.
Verworfen: ein `WorldBounds`-MonoBehaviour, das die Wände in `Awake` erzeugt
(mein erster Vorschlag — mehr Teile, Laufzeitkosten, und ein Objekt mehr, das
in der Szene hängen muss); vier von Hand gesetzte Würfel (Weltgröße abgetippt).
Offen geblieben: Der Wasserspiegel hat bewusst keinen Collider, der Spieler
läuft also in den See und weiter auf dem Grund. Am 19.08. nicht angefasst.
