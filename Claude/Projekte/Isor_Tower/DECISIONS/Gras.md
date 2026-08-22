# DECISIONS.md — Entscheidungen Gras und Instancing

Ownership: Nur Entscheidungen zu Gras und Instancing — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

## 2026-07-26 — Gras-Rendering: GPU-Instancing statt GameObjects (Tür B)
Was: Masse-Deko (Gras, Steine, Blumen) wird nicht per Instantiate als
GameObject platziert, sondern als reine Transform-Daten (`Matrix4x4`-Liste, vom
ObjectPlacer erzeugt) per `Graphics.DrawMeshInstanced` gezeichnet (Material mit
„Enable GPU Instancing"). Der Rendering-Weg wird eine eigene, pro Placeable
wählbare `RenderStrategy` (GameObject vs. Instanced). Bäume/Häuser bleiben
GameObjects (wenige, interaktiv). Gras-Verformen zum Spieler bleibt der
Shader-Bend über eine globale Spielerposition — GPU-Sache, braucht kein
GameObject, mit Instancing voll kompatibel.
Warum: Ein GameObject je Halm skaliert nicht — Millionen Halme = GB Overhead,
Millionen Draw Calls, CPU-Tod pro Frame (bestätigt: Editor-Ruckeln und
Crash bei ~1 Mio Objekten Gras+Bäume). Kernsatz: Zeichnen braucht kein GameObject; Platzierung ist Daten,
Rendering ein getrennter Schritt. Instancing ist Unitys empfohlener Weg für
viele Kopien desselben Meshes. Der RenderStrategy-Split hält die Platzierungs-
Logik unberührt (wie schon DensityStrategy) und liefert fürs TDD ein zweites
sichtbares Pattern. Konkretisiert DECISIONS 2026-07-21 „Tool-Panel" (dort als
„Gras-Masse-Rendering später kapselbar" vorgemerkt).
Verworfen: nur das Material-Häkchen setzen (senkt Draw Calls, lässt aber die
GameObjects und damit CPU/RAM/Crash bestehen); ein großes gebackenes Mesh wie
Minecraft-Chunks (lohnt bei unterschiedlicher Geometrie, nicht bei tausenden
identischen Halmen); Bäume jetzt auch instancieren (wenige, sollen anklickbar
bleiben — erst bei echter Masse nötig).
## 2026-08-04 — Gras-Instancing: nachrechnen, eigenes Gras-Gitter, kein Schatten
Was: Die Umsetzung von DECISIONS 2026-07-26 wird festgezurrt und aus dem
Nach-Abgabe-Block vorgezogen. (1) Die Matrizen werden nicht serialisiert, sondern
beim Laden aus dem `placementSeed` neu berechnet — gespeichert wird nur der Seed.
(2) Gras bekommt ein eigenes Zellgitter, unabhängig von den Terrain-Chunks: eine
Matrizenliste je Zelle mit eigener `worldBounds`, Unity cullt die Zellen selbst.
Kantenlänge als Config-Feld `grassCellSize`, Default 128 m. (3) Gras wirft keine
Schatten (`ShadowCastingMode.Off`). (4) Der Aufruf ist `Graphics.RenderMeshInstanced`
statt des 2026-07-26 genannten `Graphics.DrawMeshInstanced` — Unity 6000.5.
Warum: Serialisiert wären es rund 40–50 MB Text je Platzierungslauf, die bei jedem
Seed-Tuning neu ins Repo wandern; Nachrechnen kostet nur Ladezeit — und genau diese
Ladezeit ist das Messobjekt der Threading-Abgabe (ROADMAP Punkt 4), das es bei
editor-seitigem Ausrechnen gar nicht gäbe. Das Terrain-Chunkgitter hängt an der
65.535-Vertex-Grenze eines Meshes, das Gras-Gitter an der 1023-Instanzen-Grenze eines
Batches — zwei verschiedene Zwänge, also zwei Gitter; gekoppelt würde ein Wechsel der
Terrain-Auflösung ungefragt das Culling mitverändern. 128 m ist bei heutiger Dichte
(0,05 Halme/m²) die Kante, die eine volle Zelle in genau ein Batch legt (~820 Halme);
Feld statt Konstante, weil ein halbierter minSpacing die Dichte vervierfacht und die
optimale Kante halbiert. Schatten von hunderttausenden Halmen kosten einen zweiten
Render-Durchgang ohne sichtbaren Gewinn.
Verworfen: Matrizen in Szene oder Asset serialisieren (40–50 MB je Lauf, bläht Repo
und Editor, und nimmt der Threading-Abgabe ihren Gegenstand); Culling an die
Terrain-Chunks koppeln (256 m sind zu grob — 34 % statt 27 % gezeichnet bei zugleich
88 statt 70 Batches, und die Chunkzahl ist eine Auflösungs-Entscheidung);
64-m-Zellen (2 % weniger Gras für 186 zusätzliche Draw Calls); GPU Resident Drawer
(braucht weiterhin GameObjects, löst also weder Speicher noch Editor-Absturz);
Unitys Terrain-Detail-System (setzt Unitys `Terrain`-Komponente voraus, das Terrain
ist selbst gebaut); `BatchRendererGroup` mit Culling je Halm (großes Gerät, bleibt im
Nach-Abgabe-Block); Entfernungs-Abschneider jetzt schon bauen (bleibt
Ein-Zeilen-Reserve, falls das Frustum-Culling allein nicht reicht).
## 2026-08-04 — Gras-Render-Settings am Prefab, LOD-Wahl als eigene Stufe
Was: Die Rendering-Einstellungen (LowDetailMesh, LodDistance, RenderDistance,
CellSize) liegen als reine Datenkomponente `GrassRenderProfile` am Gras-Prefab,
nicht in der TerrainConfig. Die Distanz-Entscheidung je Zelle (None/High/Low)
trifft `GrassLodSelector` als eigene statische Stufe; der `InstancedRenderer`
holt Daten und zeichnet nur noch.
Warum: Die TerrainConfig begann alles Mögliche aufzusammeln (Fattening-Check
aus den CODE_GUIDELINES schlug an — ein Render-Abstand ist keine
Terrain-Generierung); am Prefab stehen die Werte da, wo das Gras ist, und
jeder Typ bringt seine eigenen mit. Die Selector-Stufe ist getrennt, damit
Fade o. Ä. später dazukommen kann, ohne den Zeichencode anzufassen — gleicher
Schnitt wie die kommerzielle Referenz (GPU Instancer: LODGroup als
Datenquelle, Umschaltung im eigenen Renderer).
Verworfen: `grassCellSize`/`grassRenderDistance` in der TerrainConfig (gebaut
04.08., wieder ausgebaut); ScriptableObject statt Komponente (lohnt erst,
wenn mehrere Prefabs dieselben Werte teilen); Unitys LODGroup (arbeitet auf
Renderer-Komponenten — beim Instancing existieren keine); Unity-6 Mesh LOD /
`forceMeshLod` (automatische Vereinfachung, verzieht dünne Halme wie
Decimate); reines Distanz-Culling als Kugel um die Kamera (gebaut 04.08.,
wieder raus — zeichnet auch hinter dem Rücken und löste das eigentliche
Dreiecks-Problem nicht).
## 2026-08-04 — Gras-Detailproblem: LOD-Meshpaar von Hand statt Automatik
Was: Das Detail-Büschel (2.664 Dreiecke, ~110 Halme) bleibt für die Nähe; für
die Ferne ein handgebautes Low-Büschel (~30 Halme à 7 Dreiecke), aus dem
Original abgeleitet: Kopie → Halme ausdünnen → Kantenringe per Dissolve
auflösen (nie Delete — Löcher) → Normals per Normal-Edit-Modifier senkrecht
(stylized Flächenlicht) → FBX-Export mit Apply Modifiers, Unity-Import
„Normals: Import".
Warum: Instancing senkt Draw Calls, nicht Dreiecke — 190k Büschel × 2.664 =
507 Mio Tris = 4,5 FPS, GPU-limitiert; Budget liegt bei ~15–20 Mio. Referenz-
Grassysteme nutzen 1–9 Tris je Halm-LOD. Ableiten statt Neubauen hält
Silhouette und Proportionen identisch → kein sichtbarer Sprung beim
LOD-Wechsel.
Verworfen: Decimate/automatisches Vereinfachen (hat das erste LowPoly
verzogen — legt Dreiecke frei zusammen, Form kippt); Grass-Cards mit
Alpha-Textur (Shader-Bend/Bewegung auf Flächen sichtbar schlechter — bewusste
Design-Entscheidung für echte 3D-Halme); fertiges Asset-Pack (Stil-Bruch,
das Paar war schneller selbst abgeleitet).
## 2026-08-08 — Gras-Verteilung bleibt auf Uniform
Was: Das Gras-Placeable nutzt `UniformDensity`, nicht die gebaute `NoiseMaskDensity`.
Warum: Isors Entscheidung beim Tunen — gleichmäßig sieht in der noch leeren Welt
besser aus. Für das TDD zusätzlich wertvoll: Uniform ist der Worst Case der
Laufzeitmessung, jede Maske dünnt aus. Die gemessenen 12,4 s sind damit eine obere
Grenze, kein geschönter Wert. Im Text steht die Maske als gebaut und begründet
abgeschaltet.
