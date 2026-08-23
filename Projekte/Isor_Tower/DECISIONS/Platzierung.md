# Platzierung.md — Entscheidungen Platzierung

Ownership: Nur Entscheidungen zu Platzierung — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Nicht hier: das Gelände, auf dem platziert wird (`Terrain_Mesh.md`), und
was das Gras-Rendering aus den verteilten Büscheln macht (`Gras.md`).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

Gilt eine Begründung weiter und ist nur ihre Ausführung überholt, bleibt
der Eintrag stehen und bekommt eine Zeile **Fortgeführt am `<Datum>`**
mit Zeiger auf die geltende Fassung — dann geht die Herleitung nicht ins
Archiv verloren.



## 2026-07-18 — Platzierungs-Reihenfolge: Formen vor Reagieren
Was: Schichten-Prinzip — erst was das Gelände formt, dann was darauf
reagiert: 1. Plateau-Modifier (Village-Fläche), 2. Wasserspiegel
(waterLevel + Ebene statt gegrabener Flüsse), 3. Haus/Village aufs
Plateau, 4. Bepflanzung mit Regeln (Höhe/Steigung/Wassernähe/nicht auf
Plateau), 5. Kür: echte Flüsse, Wege. Modifier schreiben in die
Heightmap, Platzierung liest nur.
Warum: Regeln wie „Gras am Wasser" brauchen Wasser als Input — von Isor
selbst hergeleitet. Wasserspiegel liefert „wo ist Wasser" für einen
Bruchteil der Kosten von Fluss-Carving; Straßen sind das Schwerste und
stehen nicht in den Pflicht-Features.
Verworfen: Bepflanzung zuerst (alte Empfehlung); Flüsse graben vor der
Abgabe; Straßen als fester Bestandteil.

## 2026-07-21 — Platzierungs-Stufe: reine Stufe, zwei Listen, globales Poisson
Was: ObjectPlacer als reine statische Stufe (Geschwister zu MeshBuilder, liest
nur, fasst die Szene nicht an). Zwei Listen: Placeable (`[Serializable] class`,
Array in TerrainConfig — prefab, min/maxHeight, maxSlope, minSpacing,
scaleMin/Max, alignToGround, DensityStrategy) → Placement (`struct`, tausendfach
— prefab, position, rotation, scale). Der Presenter instanziiert. Verteilung:
globales Poisson-Disc über die ganze Karte, Ergebnis pro Chunk einsortiert.
Warum: hält den Pipeline-Stil (reine Daten-Stufe, nur der Presenter mutiert die
Szene); Poisson garantiert den Mindestabstand (Isors Kernanforderung); global,
weil Poissons Garantie global ist und per-Chunk am Nahtrand wieder Berührungen
erzeugt; struct spart Garbage bei tausenden Einträgen, class nötig für den
Inspector. Konkretisiert DECISIONS 2026-07-18 „Formen vor Reagieren".
Verworfen: per-Chunk-Poisson (Naht-Abstand nur mit Rand-Check, mehr Code);
Raster+Versatz (kein garantierter Abstand); reiner Zufall (klumpt); prefab per
Index statt direkt (YAGNI); gespeicherte Placement-Liste als Asset.

## 2026-07-21 — Höhe/Steigung für die Platzierung: gemeinsame SampleHeight-Funktion
Was: „Höhe an Weltposition" wird als `SampleHeight(config, x, z)` aus dem
HeightmapGenerator herausgezogen (Noise → Curve → Plateau an einem Punkt);
Chunk-Schleife und Placer nutzen dieselbe Funktion. Steigung und Ausrichtungs-
Normale kommen aus vier Nachbar-Samples (zentrale Differenz wie im MeshBuilder)
— eine Rechnung, zwei Zwecke. Der Placer braucht das Mesh nicht.
Warum: eine Quelle der Wahrheit statt Doppel-Logik; Funktion statt gespeichertem
Gitter, weil der Placer nur verstreut abfragt (~9.600 Punkte gegen ~1,05 Mio
Gitterzellen) und ein Cache bei Config-Änderung veraltet; Funktion passt zum
stateless-pure Stil (Generator/MeshBuilder halten keinen Zustand).
Verworfen: eigenes globales Höhen-Gitter für die Platzierung (Doppelrechnung,
Veraltungs-Risiko, einziger dauerhafter Zustand — Fremdkörper); Mesh-Faces
abfragen für die Ausrichtung (Normale gibt es analytisch aus SampleHeight).

## 2026-07-21 — Platzierung: ein Poisson-Durchgang pro Typ, Reihenfolge=Priorität, Regel-Filter
Was: ein Poisson-Durchgang je Placeable-Typ (eigener minSpacing-Radius);
Reihenfolge in Liste 1 = Priorität. Jeder Durchgang nimmt eine Blocker-Liste
entgegen (jetzt leer → Bäume/Gras unabhängig; später legt der Dorf-Schritt die
Haus-Grundrisse hinein → Gras/Bäume meiden Häuser, ohne Umbau). Regel-Filter je
Kandidat, billig→teuer: Wasser-Untergrenze (global, nur wenn isWaterEnabled,
height ≥ waterLevel + shoreMargin) → Höhenband (max(Wasser, minHeight)…maxHeight)
→ Steigung (≤ maxSlope). Alle bestanden → Placement.
Warum: derselbe Poisson-Abstandsmechanismus deckt auch den Inter-Typ-Ausschluss
(Blocker als Fremd-Punkte) — kein Sonderfall; Reihenfolge billig→teuer spart die
teure Steigungsrechnung bei früh abgelehnten Punkten; Wasser-Regel global, weil
die Uferlinie eine Welt-Eigenschaft ist. Nutzt shoreMargin aus DECISIONS
2026-07-19 „Wasserspiegel".
Verworfen: fest verdrahtete Inter-Typ-Ausschlüsse / Ausschluss-Matrix jetzt
(YAGNI); Wasser-Regel pro Placeable-Zeile.

## 2026-07-21 — Dichte-Steuerung als austauschbare DensityStrategy (Strategy-Pattern)
Was: „wo viel/wenig" als Wahrscheinlichkeits-Ausdünnung statt variablem Poisson-
Radius. Abstrakte `DensityStrategy` (ScriptableObject) mit
`AcceptanceProbability(x, z) → 0–1`; drei Start-Assets: Uniform (immer 1),
NoiseMask (Rausch-Wert, eigener Seed/Scale), Probability (feste Zahl). Feld pro
Placeable, leer = Uniform. Der Würfel-Wurf (`random < p`) lebt einmal im Placer,
die Strategie liefert nur p.
Warum: fester-Radius-Poisson + Ausdünnung ist eine simple 4. Filterstufe;
variabler-Radius-Poisson bricht die Gitter-Beschleunigung (fummelig); Strategy
ist offen für neue Arten ohne Placer-Änderung; NoiseMask als eigenes Asset →
mehrere Masken frei kombinierbar. Erfüllt zugleich das Design-Pattern-Kriterium
der Tool-Aufgabe (zweites Muster neben MVP).
Verworfen: variabler-Radius-Poisson; enum + switch (nicht ohne Code
erweiterbar); Strategie global statt pro Typ.

## 2026-07-21 — Tool-Panel, Prefabs, placementSeed
Was: reiches Editor-Panel — „Generate Complete" (alles in Prioritätsordnung),
Einzel-Stufen (Terrain / Wasser / Place Objects), plus pro-Typ „Place"/„Clear"
**aus Liste 1 erzeugt** (nicht fest verdrahtet). Eigene „Generated Placement"-
Wurzel unter dem Terrain-Root; „Place Objects" läuft ohne Terrain-Rebuild
(schnelles Tunen), Terrain-Regenerieren räumt die Platzierung als veraltet weg.
Prefabs kunst-blind (Referenz in Placeable; Platzhalter-Primitive jetzt, echte
Assets später ohne Code-Change). Gras-Masse-Rendering im Presenter kapselbar
(GameObjects jetzt → GPU-Instancing/Details später), aufgeschoben inkl.
Praxis-Test Prefab-Gras vs. Detail. Eigener `placementSeed` (getrennt vom
Terrain-Seed → Verteilung neu würfeln ohne Rebuild), pro Typ abgeleitet, alles
Zufällige deterministisch.
Warum: Aufgabe belohnt umfangreiche Tools; Einzel-Stufen helfen beim Bauen/
Debuggen; pro-Typ aus der Liste bleibt datengetrieben (neuer Typ = automatisch
Buttons); getrennter Seed löst die vorgemerkte „inkrementell generieren"-Frage;
Rendering-Tausch hinter dem Presenter hält die Platzierungs-Logik unberührt.
Verworfen: Tree/Grass fest verdrahtete Buttons; Auto-Platzierung bei jedem
Terrain-Generate; Platzierung an den Terrain-Seed gekoppelt.

## 2026-07-23 — SampleHeight komponiert, PlateauModifier bleibt eigener Job
Was: Die geteilte Höhen-Funktion `SampleHeight` ist ein dünner Komponist
(Noise+Curve, dann `PlateauModifier.SampleAt`); die Plateau-Logik bleibt in
`PlateauModifier` (jetzt per-Punkt statt Array), nicht inline in `SampleHeight`
gefaltet. Setzt DECISIONS 2026-07-21 „gemeinsame SampleHeight-Funktion" um.
Warum: DRY (eine Wahrheit, ein Einstiegspunkt) und SRP (ein Job je Klasse)
beißen sich nur bei Inline-Faltung; Trennung nach Job + Teilen durch Komposition
erfüllt beide, kein Gott-Objekt. Von Isor selbst als Spannung erkannt.
Verworfen: Plateau-Rechnung inline in `SampleHeight` (SRP-Verstoß);
`PlateauModifier` löschen; ihn behalten UND Plateau in `SampleHeight`
duplizieren (DRY-Verstoß).

## 2026-07-25 — Dichte-Filter vor der Steigung; Würfel an einer Stelle
Was: Umsetzung der DensityStrategy (2026-07-21). Der Dichte-Filter läuft im
ObjectPlacer zwischen Höhenband und Steigung — nicht als letzte Stufe wie im
Design-Text („4. Filterstufe") skizziert. Der Würfel lebt an genau einer Stelle
(`random.NextDouble() >= p`), die Strategie liefert nur p (float, nicht bool).
Fehlende Maske (`_density == null`) = Uniform, deshalb ist ein Uniform-Asset
optional. NoiseMask cacht den Seed→Offset in OnEnable/OnValidate.
Warum: billig→teuer. Die Maske kostet höchstens einen Perlin-Aufruf (NoiseMask)
oder gar nichts (Uniform/Probability), die Steigung vier SampleHeight-Aufrufe
(~20 Perlin bei 5 Oktaven) — früh per Maske verworfene Kandidaten sparen die
teure Rechnung. float trägt die Gewichtung (bool verwürfe die Abstufung); ein
Würfel-Ort + ein Seed-Strom hält die Platzierung deterministisch. Der Offset-
Cache ist abgeleiteter Zustand (Antwort bleibt reine Funktion von x,z), kein
veränderlicher Zustand. Setzt DECISIONS 2026-07-21 „Dichte-Steuerung als
DensityStrategy" um.
Verworfen: Dichte als letzte Stufe (Text-Reihenfolge, teurer); bool `Accepts`
mit Würfel in der Strategie (Abstufung weg, Zufall im zustandslosen Asset);
Uniform als Pflicht-Asset (null genügt).

## 2026-07-26 — Placer-Einstieg pro Typ, eine Hierarchie-Gruppe je Placeable
Was: `ObjectPlacer.Place(config, placeableIndex)` streut genau einen Typ; die
Schleife über alle Typen liegt im Presenter, der pro Typ eine eigene Gruppe
(`{index}_{Prefabname}`) unter „Generated Placement" anlegt. Seed-Ableitung
bleibt `placementSeed + index`. Setzt DECISIONS 2026-07-21 „Tool-Panel" um.
Warum: Der Presenter muss ohnehin pro Typ gruppieren — so gibt es die Schleife
nur einmal (DRY), und das alte `Place(config)` entfällt statt als toter Code
zu bleiben. Der Index im Namen hält ihn eindeutig (zwei Typen dürfen dasselbe
Prefab nutzen) und macht die Prioritätsreihenfolge in der Hierarchie sichtbar.
Unveränderte Seed-Ableitung heißt: ein einzeln platzierter Typ sieht identisch
aus wie derselbe Typ im Komplettlauf — Voraussetzung fürs Tunen. Nebenwirkung:
Umsortieren der Placeables ändert die Indizes und damit alle Verteilungen.
Verworfen: `Place(config)` zusätzlich behalten (toter Code); Typ-Zugehörigkeit
als Feld im `Placement`-struct (bläht den tausendfachen Wert auf); eine flache
Wurzel ohne Typ-Gruppen (Einzel-Clear nicht möglich).

## 2026-07-26 — Platzierung komponiert mit dem Prefab-Transform
Was: Der Presenter überschreibt Rotation und Scale der Instanz nicht mehr,
sondern multipliziert sie mit den im Prefab hinterlegten Werten
(`placement.Rotation * prefabRotation`, `prefabScale * placement.Scale`),
gelesen von der frisch erzeugten Instanz statt vom Prefab-Asset.
Warum: Modelle aus Blender brauchen oft eine Achsen-Korrektur am Prefab-Root;
absolutes Setzen der Rotation löschte sie und legte alle Bäume um. Reihenfolge
`placement * prefab` ist zwingend — Quaternionen wirken von rechts nach links,
also erst aufrichten, dann drehen/neigen. Von der Instanz gelesen, weil das
Prefab-Asset seine Transform-Werte nicht zuverlässig herausgibt.
Verworfen: Korrektur-Rotation strukturell an ein Kind-Objekt auslagern
(Wrapper-Prefab — funktioniert, kostet aber einen Transform je Instanz bei
hunderttausenden Objekten); Achsen-Korrektur nur über den Import erzwingen
(`Bake Axis Conversion` dreht bereits konvertierte Blender-Dateien ein
zweites Mal und legt sie damit erst um).

## 2026-07-29 — Globales Poisson: bekannte Grenze, keine Lösung vorentschieden
Was: Der globale Poisson-Disc-Durchgang (2026-07-21) bleibt bis zur Abgabe
unverändert. Festgehalten wird nur die Grenze: „global" verlangt, die ganze
Karte auf einmal zu berechnen — das trägt bei ~2 km, aber nicht bei einem
Village, das laut GDD um ein Vielfaches wachsen kann, und nicht bei
zellenweise nachgeladener Welt. Wie ersetzt wird, ist **offen** und wird
nach der Abgabe neu bewertet; zellen-lokales Poisson ist eine Möglichkeit
unter mehreren, kein gesetzter Weg.
Warum: Die Grenze jetzt zu kennen verhindert, dass darauf aufgebaut wird;
sie jetzt zu lösen wäre verfrüht, weil sich Anforderungen und verfügbare
Verfahren bis dahin ändern können. Für die Abgabe hat die Grenze keine
Auswirkung — die Abgabe-Welt wird ohnehin verkleinert.
Verworfen: jetzt auf zellen-lokales Poisson festlegen (verfrüht); die
Grenze nicht dokumentieren (würde später als Überraschung auftauchen).

## 2026-08-03 — Prefab Painter: Aufbau und Bedienung
Was: Editor-Tool `Tools > Isor Tower > Prefab Painter` in
`Assets/Systems/PrefabPainter/Editor/`, MVP wie das Terrain-Tool:
`PrefabPainterWindow` (View + SceneView-Input), `PrefabPainterPresenter`
(alle Szenenänderungen inkl. Undo), `BrushSampler` (reine Mathe, fasst die
Szene nie an), `PainterPalette`/`PaintBrush` als Einstellungs-Asset.
Gemalt wird unter eine frei gewählte Ziel-Wurzel; die Hierarchie darunter ist
`<Kategorie>/<Prefabname>/<Prefabname>_001`. Die Kategorie kommt aus dem
Asset-Pfad des Prefabs (`Assets/Environment/...` → `Environment`),
überschreibbar pro Pinsel. Drei Pinselformen (Single, Scatter, Line) plus
Continuous-Schalter; ein Pinsel hält mehrere Prefabs und würfelt pro Objekt
eins aus. Löschen liegt auf Strg+Klick, ein ganzer Strich ist ein Undo-Schritt.
Höhe und Normale kommen aus einem Raycast gegen die Collider, nicht aus
`HeightmapGenerator.SampleHeight`. Das Terrain-Tool zieht mit ins Menü
`Tools > Isor Tower`. Das Tool ist ausdrücklich nicht Teil der Uni-Abgabe.
Warum: Der Raycast macht den Painter unabhängig von der Terrain-Pipeline — er
läuft in jeder Szene auf jedem Collider, liefert die Normale gratis und findet
auch Bauwerke, die die Heightmap nicht kennt. Der Strahl ignoriert dabei alles
unter der Ziel-Wurzel, sonst würde ein frisch gesetztes Grasbüschel zum Boden
für das nächste. Löschen wird mitgebaut, weil Undo nur chronologisch zurück-
spult und beim Scatter-Malen zwangsläufig übermalt wird. Die Kategorie aus dem
Pfad zu lesen kostet keine Pflege und deckt sich mit der Ordnerkonvention aus
CODE_GUIDELINES. Nummeriert wird selbst, weil Unity nur Duplikate nummeriert,
nicht frische Prefab-Instanzen. Neue Pinsel entstehen als echte `PaintBrush`-
Instanz statt über die serialisierte Array-Größe — nur so laufen die
Feld-Initialisierer, sonst startet ein Pinsel mit Radius und Scale 0.
Verworfen: `SampleHeight` als Höhenquelle (kennt nur die prozedurale Heightmap,
band das Tool an `TerrainConfig`); Löschen weglassen und auf Undo/Entf setzen;
eine Pinselform statt drei; Malen im Prefab-Isolationsmodus (dort gibt es kein
Terrain zum Anpeilen); Determinismus per Seed wie im `ObjectPlacer` (das
Ergebnis sind gespeicherte Objekte, keine reproduzierbare Generierung).

## 2026-08-05 — PlacementExclusion: Freiflächen als Komponente am Objekt
Was: `PlacementExclusion` (Kreis oder Box, Center-Offset, dreht mit dem
Objekt, Gizmo immer sichtbar) markiert Flächen, in die der Placer nichts
setzt. `PlacementExclusionFilter` als eigene Stufe zwischen `ObjectPlacer`
und beiden Konsumenten (InstancedRenderer und SpawnType). Die Formprüfung
lebt in der Komponente (`Contains`); der Rand wächst um die halbe
Objektbreite aus den Mesh-Bounds.
Warum: Jedes Objekt bringt seine Freifläche selbst mit — Haus hinsetzen
genügt, keine zentral gepflegte Liste, die vom Szenenstand abdriftet
(gleiche Linie wie GrassRenderProfile: Daten ans Objekt). Filter
formunabhängig → neue Form ändert ihn nicht (wie DensityStrategy). Der Rand
ist nötig, weil der Placer Fußpunkte prüft: „Mittelpunkt draußen" hieße
sonst „Halme ragen trotzdem rein". Ersetzt die geplante Blocker-Liste und
die angedachte Plateau-Sonderprüfung im Placer.
Verworfen: Blocker-Liste im Placer (zentrale Pflege); Dorfkreis-Prüfung
gegen PlateauCenter/Radius (deckt nur das Plateau, nicht einzelne Objekte);
Laufzeit-Spawn der Schafe als Fix fürs Aufsetzen (Umbau der ganzen
Herden-Verdrahtung — nach der Abgabe, mit „Pipeline runtime-fähig"); Name
`GrassExclusion` (galt nach dem Anschluss an SpawnType nicht mehr nur für
Gras — umbenannt, die eine gesetzte Zone neu verdrahtet).

## 2026-08-05 — NoiseMask bekommt eine Kontrastkurve
Was: `NoiseMaskDensity` schickt den Perlin-Wert durch eine AnimationCurve
(Default: bis 0,42 → 0, ab 0,58 → 1, dazwischen Anstieg); erst das Ergebnis
ist die Annahme-Wahrscheinlichkeit.
Warum: Perlin liegt fast vollständig bei ~0,35–0,65 — als Wahrscheinlichkeit
heißt das „überall ≈ 50 %": gleichmäßiges Ausdünnen statt Flecken, und Scale
hatte sichtbar keinen Effekt (Beleg: 266k/265k/276k Objekte bei Scale
5/100/600). Die Kurve erzeugt echte Kahl- und Dichtflächen; erst dadurch
steuert Scale die Fleckengröße. Weniger Objekte bei lebendigerem Bild —
und dasselbe Werkzeug wie die HeightCurve (Konsistenz, live tunebar).
Verworfen: festes Formel-Remap (SmoothStep o. Ä. — unsichtbar und nicht pro
Asset tunebar); minSpacing vergrößern (dünnt gleichmäßig aus, erzeugt keine
Flecken).

## 2026-08-05 — Placement kachelweise statt punktweise parallelisiert
Was: Die Welt wird für die Platzierung in `PlacementTilesPerAxis`² Kacheln
geteilt (Default 8×8 = 64, wie das Terrain-Chunk-Gitter); jede Kachel sampelt
und filtert eigenständig mit eigenem `System.Random`, `Parallel.For` läuft über
die Kacheln. 1 stellt das alte Verhalten wieder her.
Warum: Der erste Versuch parallelisierte nur den Regel-Filter (ein Arbeitspaket
je Punkt) und brachte 3,7 %, weil der sequenzielle Poisson-Pass 84 % der Zeit
hielt. Die Kachelung macht den teuren Teil selbst parallelisierbar und schrumpft
nebenbei das Poisson-Gitter von ~94 MB auf ~1,5 MB je Kachel (Cache) — allein
das brachte 19,4 % ohne jeden Thread, mit Threads zusammen 86,6 %. Der Code wurde
dabei kürzer: kein 126-MB-Zufallsarray und kein `Parallel.For` mit
thread-lokalen Sammlern mehr.
Verworfen: punktweise Parallelisierung (Deckel bei 16,6 % laut Amdahl); Unity
Job System + Burst (Pipeline hängt an ScriptableObjects, virtuellen Aufrufen und
`Mathf.PerlinNoise` — Umbau hätte länger gedauert als die Aufgabe wert ist, und
die Aufgabe nennt Threadpools ausdrücklich); Padding an den Kachelrändern nach
Vorbild der Mesh-Normalen (funktioniert dort, weil die Höhe eine Funktion der
Position ist — ein Poisson-Punkt ist dagegen ein Verlauf und lässt sich vom
Nachbarn nicht nachrechnen).

## 2026-08-05 — Kachelgrenzen-Ungenauigkeit bewusst akzeptiert
Was: An den Kachelrändern kann der Poisson-Mindestabstand verletzt werden, weil
Kacheln einander nicht kennen. Bleibt so, dokumentiert als bekannte Grenze.
Warum: Bei 8×8 Kacheln entstehen ~28 km Nahtlänge auf 7,4 Mio Halme — optisch
nicht wahrnehmbar. Die Alternativen kosten spürbar: ein Aufräumpass über die
Randstreifen (machbar, ~0,5 % der Punkte) oder ein Schachbrett-Verfahren in zwei
Phasen (halbiert die Parallelität). Bei Bäumen, wo einzelne Abstände auffallen,
wäre der Aufräumpass nachzuholen.
Verworfen: feinere Kachelung (verdoppelt die Nahtlänge je Halbierung und bringt
bei gleichmäßiger Grasdichte keine bessere Lastverteilung).

## 2026-08-05 — Laufzeit-Spawner für instanziertes Placement
Was: `RuntimePlacementSpawner` auf dem Placement-Root erzeugt beim Szenenstart je
instanziertem Placeable-Typ ein Kind mit `InstancedRenderer`; `Init` nimmt die
Anzahl der Messläufe mit. Das Editor-Tool bleibt unverändert daneben bestehen.
Warum: Der Gras-Renderer entstand bisher nur durch den Tool-Klick — im Build gab
es das Objekt nicht, also lief kein Placement und es war nichts zu messen. Der
gesamte Placement-Code lag ohnehin schon in `Scripts/`, nur der Auslöser fehlte.
Zieht damit den Roadmap-Punkt „Editor-Tool und Laufzeit als zwei Aufrufer
derselben Stufen" für Gras vor.
Verworfen: die vom Tool erzeugten Objekte in der Szene speichern (macht
generierten Inhalt zum Szeneninhalt und widerspricht dem Szenen-Vertrag);
GameObject-Typen gleich mitziehen (eigener Baustein, Millionen Objekte).

## 2026-08-19 — Bäume mit NavMeshObstacle statt NavMesh-Rebake
Was: Jeder Baum trägt `NavMeshObstacle` mit `Carve` und
`CarveOnlyStationary` plus einen `CapsuleCollider`. Kein neuer NavMesh-Bake,
keine Navigation-Static-Markierung.
Warum: Isor hat es gebaut und im Spiel gemessen — bei 21.354 Bäumen kein
spürbarer Einbruch. Der Weg braucht keine Änderung an der Szene und keinen
Bake-Durchlauf zwei Tage vor der Frist.
Verworfen: Bäume als Navigation Static markieren und das NavMesh neu backen
(sauberer, weil dann zur Laufzeit gar nichts mehr passiert — aber ein
Bake-Durchlauf über 21.354 Objekte am Abgabeabend); `Carve` abschalten und
nur lokal ausweichen lassen.
Richtigstellung zum Verständnis: Der NavMesh-Bake und das Carving sind
getrennte Vorgänge. Der Bake liegt als Daten im Build, das Carving eines
Obstacle ist dagegen reine Laufzeit und läuft bei **jedem** Spielstart neu.
Beim Testen am fremden Rechner darauf achten, ob direkt nach dem Ladescreen
ein Hänger auftritt; Gegenmittel wäre `Carve` aus.

## 2026-08-20 — Bäume stehen senkrecht statt hangparallel
Was: `AlignToGround` am Baum-Placeable ausgeschaltet, `MaxSlope` bleibt bei 90.
Bäume stehen damit überall senkrecht; an Steilhängen steht der Stammfuß frei.
Warum: Mit `AlignToGround: 1` und `MaxSlope: 90` wurde jeder Baum auf die
Bodennormale gedreht — an einer fast senkrechten Wand liegt die Normale
waagerecht, der Baum legte sich also flach hin. Bodenausrichtung ist für Gras
und Steine richtig, für Bäume nicht: Bäume wachsen senkrecht.
`MaxSlope` blieb bewusst unangetastet, weil der Placer seine Zufallszahlen pro
angenommenem Punkt zieht — eine andere Hanggrenze verschiebt die Zufallsfolge
und hätte am Abgabetag eine komplett neue Waldverteilung ergeben. So blieben
Positionen, Drehwinkel und Größen identisch, die Bäume stehen nur auf.
Verworfen für heute, richtig für später (Isors eigene Einschätzung, das sei
"für ein richtiges Spiel" nicht gut genug): `MaxSlope` auf 25–30 senken, damit
an Steilhängen gar nichts steht; den Baum hangabhängig einsinken lassen, damit
der Fuß nicht frei steht; oder per `Quaternion.Slerp` mit etwa 0,2–0,3
zwischen Senkrechter und Normale mischen, sodass der Baum sich leicht neigt.

## 2026-08-20 — Glühwürmchen über den Placer, nicht von Hand gemalt
Was: Die Schwärme sind ein dritter Placeable-Typ in `TerrainConfig_Default`,
begrenzt über Höhenband und Hangneigung, Render Mode GameObjects.
Warum: Isors Einwand gegen meinen Vorschlag. Ich hatte zum Prefab Painter
geraten, weil der Placer über die ganzen 2048 × 2048 Meter streut und ein
Schwarm-Effekt (`capacity: 30`) teurer ist als ein Baum-Mesh. Der Einwand
zieht aber nicht, weil sich die Menge über `MinSpacing` und die Regeln
steuern lässt — und der Placer ist zugleich der in der ROADMAP ohnehin
gewünschte Zielzustand und das prozedurale statt des händischen Verfahrens.
Merkposten für später: VFX-Instanzen sind teurer als statische Meshes; wenn
die Bildrate bei Nacht einbricht, ist `MinSpacing` der Regler.
Verworfen: von Hand mit dem Prefab Painter malen (mein Vorschlag);
`Instanced` als Render Mode — das zeichnet nur Meshes und führt keine
VFX-Komponente aus.

## 2026-08-20 — Der Placer setzt Herden, nicht einzelne Schafe
Was: Vierter Placeable-Typ ist `SheepHerdManager_01`, nicht das Schaf-Prefab.
19 Instanzen, Hangneigung bis 8,4°, Höhenband 0,14–0,30.
Warum: Isors Lösung, und sie ist besser als das, was gestern besprochen war.
Der Placer streut damit Herden statt Einzeltiere — das umgeht die Sorge, dass
verstreute NavMeshAgents nicht sauber auf dem NavMesh aufsetzen, hält die Zahl
klein (19 statt hunderter Einzelschafe) und ergibt trotzdem eine belebte Welt.
Die flache Hanggrenze sorgt dafür, dass die Herden auf begehbarem Weideland
landen.
Folge für die Bewertung: Lernziel S3 ("generierte Bevölkerung") gilt damit als
erfüllt. Es stand am 19.08. noch als geschoben in der ROADMAP.
Verworfen: einzelne Schafe streuen; von Hand setzen (Isors Plan vom 19.08.).
