# DECISIONS.md — Entscheidungen

Ownership: Entscheidungen: was, warum, verworfene Alternativen.
Format: `## JJJJ-MM-TT — Titel` mit Was / Warum / Verworfen, je 1–2 Zeilen.

## 2026-07-16 — Brainstorm-Modus normal/uni
Was: Jede Brainstorm-Session startet mit der Modus-Abfrage normal oder uni.
Warum: Uni-Modus braucht eigene Regeln — erklären statt bauen, visuell,
Verständnis-Checks, Knowledge-Pflicht.
Verworfen: ein Einheitsmodus für alle Brainstorm-Sessions.

## 2026-07-17 — Knowledge als externer Ordner
Was: Wissensarchiv als Ordner `C:\Repos Isor\Knowledge\` mit
Themen-Unterordnern, eine .md pro Konzept, Offline-Kopien der
Artifact-Seiten unter Seiten/.
Warum: Wissen ist projektübergreifend und überlebt das Projekt; eine
einzelne Datei wäre unübersichtlich gewachsen.
Verworfen: einzelne KNOWLEDGE.md im Projekt als Puffer mit Auslagerung.

## 2026-07-17 — CODE_GUIDELINES: Zwei Blöcke + Projekt-Typ
Was: Block 1 = Uni-Pflicht (Stil/Naming), Block 2 = eigene Architektur-
Regeln; `Projekt-Typ: Uni/Privat` im Dateikopf entscheidet den
Konfliktfall, einmalig beim Projekt-Setup gesetzt.
Warum: Uni-Regeln sind Pflicht, sollen aber nach dem Studium sauber
entfernbar sein; Projekt-Typ ändert sich nie mitten im Projekt.
Verworfen: Session-Abfrage des Typs durch den Harness; ein gemischter
Regelblock ohne Herkunfts-Markierung.

## 2026-07-17 — Felder: [SerializeField] private statt public
Was: Default `[SerializeField] private`, `_camelCase` überall; public nur
bewusst und dann als Property.
Warum: Inspector-Wiring funktioniert identisch, Compiler schützt vor
Fremdzugriff; Dozenten-public diente nur der Bequemlichkeit seines
Editor-Setup-Scripts. Deckt sich mit Uni-Regel (Member private/protected).
Verworfen: Dozenten-Default „public fürs Wiring"; sein Underscore-Verbot.

## 2026-07-17 — Dozenten-Patterns als Werkzeugkasten, nicht Pflicht
Was: MVP als Default-Denkmodell (mit Pragmatik-Ausnahmen); SO-Identität,
Event-Channels, RuntimeReference nur bei passender Problemform.
Review-Gate übernommen (angepasst: Isor tippt selbst, Claude prüft mit);
ClaudeSetup zurückgestellt.
Warum: Entspricht den Einsatzkriterien des Dozenten selbst; Isor ist in
der Lernphase und will selbst schreiben, um besser zu werden.
Verworfen: Patterns als Pflicht für jedes System; ClaudeSetup jetzt schon.

## 2026-07-17 — Session-Ende-Rituale erweitert
Was: Knowledge-Abfrage in jeder Session (Uni-Modus: Pflicht);
Commit-Vorschlag durch Claude (Titel `Update V <nächste Nummer>` +
Description), Isor committet selbst; TDD_NOTES.md als Stoffsammlung
fürs Uni-TDD — nur echte Uni-Projekt-Arbeit, keine Harness-Arbeit.
Warum: Erkenntnisse und Commit-Historie gingen sonst beim /clear
verloren; Isor will Commit-Texte nicht selbst formulieren; das TDD ist
Uni-Abgabe (ca. 2026-07-28) und braucht laufendes Rohmaterial.
Verworfen: Knowledge-Abfrage nur im Uni-Modus; Commits durch Claude.

## 2026-07-17 — Sprache: Code englisch, Unterhaltung deutsch
Was: Code, Kommentare, Debug-Ausgaben und Commit-Messages ausnahmslos
Englisch; Harness-Doku und Unterhaltung mit Claude vorerst Deutsch.
Warum: GitHub-Repo ist englischsprachig, Fachbegriffe bleiben konsistent
mit der Unity-/C#-Welt; Deutsch hilft beim Lernen.
Verworfen: Sprachwahl je Situation; sofortige Englisch-Umstellung des
Harness (geparkt in ROADMAP „Später").

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

## 2026-07-18 — Reine statische Utilities erlaubt
Was: MeshBuilder und HeightmapGenerator sind statische Klassen — die
Regel „Keine Singletons/Statics" meint zustandsbehaftete Statics.
Warum: Beide sind reine Funktionen ohne Zustand (Daten rein, Daten raus,
testbar); eine Instanz hätte keinen Mehrwert.
Verworfen: Instanz-Klassen hinter Interface (kein zweiter Use-Case — YAGNI).

## 2026-07-18 — Wertebereiche an der Eingabe statt Laufzeit-Checks
Was: Ungültige Parameter (resolution < 2, noiseScale 0, octaves 0,
lacunarity < 1) verhindern [Min]/[Range] im Inspector; der Generator
prüft nicht selbst. Jedes Feld bekommt zudem einen sinnvollen Default.
Warum: Der falsche Wert soll gar nicht erst entstehen (gleiche Denke wie
int statt Vector2Int); fast alle Grenzen schützen vor Division durch
null. Defaults nötig, weil [Min] still gespeicherte Werte nicht korrigiert.
Verworfen: Guard-Klauseln/Exceptions im Generator.

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

## 2026-07-18 — PCG- und Engine-Tool-Aufgabe kombiniert
Was: Beide Uni-Aufgaben (ASSIGNMENT_PCG.md + ASSIGNMENT_TOOL.md) werden
mit einem Projekt erfüllt: die Terrain-Pipeline als prozedurale
Level-Generierung (PCG) plus ein Editor-Tool mit UI und mindestens einem
Design Pattern obendrauf (Engine-Tool). Bestückung nutzt vorhandene
Inhalte aus früheren Abgaben (Shader, Partikeleffekte wie
Glühwürmchen/Fackeln, vorhandene KI) und leicht beschaffbare Assets
(Haus fürs Start-Village, Bäume, Gras).
Warum: Spart Zeit, ergibt ein zusammenhängendes Spielprojekt; die
Aufgabenstellung erlaubt eigene Anwendungsfälle, Spawn-Inhalte sind frei
wählbar.
Verworfen: zwei getrennte Tools/Abgaben ohne gemeinsame Basis.

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

## 2026-07-19 — Asset-Ordner: Kategorie + FolderTemplate, Shared nur bei mehreren Abnehmern
Was: Bausteine liegen unter `Entities/`, `Environment/` oder `Systems/`
je in eigenem Ordner mit Template-Unterordnern (nur die benötigten);
`Shared/` nur für Querschnitts-Utilities mit mehreren Abnehmern. Regeln
in CODE_GUIDELINES (Ordnerstruktur); Terrain-Pipeline entsprechend nach
`Systems/TerrainGenerator` umgezogen.
Warum: `Shared/MeshBuilder` war zum Feature-Ordner gewachsen — falsches
Etikett; Isors Template-System existierte schon und funktioniert.
Verworfen: alte Guideline-Zeile `Assets/Scripts/{System}/`; MeshBuilder
in Shared lassen (nur ein Abnehmer — Zusammenhalten schlägt
spekulatives Teilen).

## 2026-07-19 — Pipeline-Klassen loggen nicht
Was: Reine Pipeline-Funktionen (Generator, Modifier, MeshBuilder)
bleiben still — kein Debug.Log, keine Warnings; Nutzer-Feedback ist
Sache der Presenter-Schicht (StatusMessage im Tool).
Warum: Radius 0 ist gewollter Aus-Schalter, kein Fehler; Logs in
Zellen-Schleifen wären Spam; was nie geloggt wird, muss für die
Uni-Abgabe nie entfernt werden.
Verworfen: Warning bei Radius 0; Debug.Logs mit späterem Ausbau.

## 2026-07-19 — Session-Typen: Brainstorm+Design ein Typ, 1:1-Regel
Was: „Brainstorm/Design" ersetzt die zwei getrennten Typen; pro Baustein
gilt: erst eine Brainstorm/Design-Session (was & wie), dann eine
Development-Session (nur Umsetzung). Eine Design-Session darf mehrere
Bausteine vorentscheiden.
Warum: Design ohne Brainstorm-Anteil kam in der Praxis nie vor; die feste
Reihenfolge gibt Isor einen klaren Schnitt zwischen Entscheiden und Bauen.
Verworfen: vier getrennte Typen; freies Mischen von Design und Umsetzung
in einer Session.

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

## 2026-07-17 — Minimalistisch zur Einsatzreife
Was: Alle vier Session-Typen nur minimal definiert; ausgearbeitet wird
erst, wenn der Praxisbetrieb es verlangt. Regel-Dateien beschreiben nur
den Ist-Zustand, Begründungen gehören hierher.
Warum: Uni-Projekt startet 2026-07-18 — funktionstüchtig schlägt
vollständig.
Verworfen: volle Ausarbeitung aller Dokumente vor Praxisstart
(alte Roadmap-Reihenfolge).

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

## 2026-07-23 — Kommentar-Konventionen geschärft
Was: XML-Docs mehrzeilig (IDE-Standard, auch Properties); Inline-Kommentare
Default = keiner, sonst einzeilig und Warum-only; Debug-Ausgaben in
`#if UNITY_EDITOR`; Felder ohne `<summary>` (serialisiert → `[Tooltip]`).
Festgehalten in CODE_GUIDELINES.
Warum: benotete Abgabe — geschwätzige/AI-riechende Kommentare sind ein Risiko;
Dozenten-Regel „keine Debug-Logs im Build"; das Warum lebt in DECISIONS/Header,
nicht inline. Aus Isors Praxis-Feedback in Session 2026-07-23.
Verworfen: einzeilige XML-Summaries; der „2–3 Zeilen erlaubt"-Inline-Zusatz
(führte zu Über-Kommentierung).

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

## 2026-07-29 — GDD als Maßstab, Short-GDD-Ansatz
Was: GDD.md wird als Short GDD angelegt (ein Bildschirm, wächst mit) und ist
der Maßstab, an dem Roadmap und bestehende Entscheidungen geprüft werden.
„Offen" ist ein ausdrücklich gültiger Eintrag. Der Umbau des Bestehenden
Richtung GDD beginnt erst **nach** der Uni-Abgabe (Portfolio 2026-08-21);
bis dahin ändert das GDD an der Uni-Arbeit nichts.
Warum: Die Systeme, die jetzt entstehen, sollen die Basis für kommende
Semester sein — ohne festgehaltene Design-Absicht werden Architektur-
Entscheidungen geraten statt begründet. Ein volles GDD hätte die Zeit bis
zur Abgabe gekostet, ohne dort einen Beitrag zu leisten. Offene Fragen sind
die wertvollste Information: Jede markiert eine Stelle, an der die
Architektur eine Tür offen halten muss; jede beantwortete Frage erlaubt es,
eine Tür zu schließen und einfacher zu bauen.
Verworfen: vollständiges GDD vor der Abgabe; ganz ohne GDD weiterbauen;
das Bestehende sofort am GDD ausrichten (gefährdet die Abgabe).

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

## 2026-07-29 — Geltungsbereiche dreier Entscheidungen präzisiert
Was: Drei bestehende Einträge sind pauschaler formuliert als gemeint; ihre
Grenze wird benannt, der Inhalt bleibt unverändert.
(1) „Terrain-Mesh komplett im Code" (2026-07-18) gilt für **generierte**
Gebiete — die Tower-Floors. Das Village wird laut GDD ein festes Grundmesh,
prozedural ist dort nur die Objekt-Platzierung darauf.
(2) „Terrain-Tool als MVP mit EditorWindow" (2026-07-18) beschreibt den
Uni-Stand: Die Pipeline wird ausschließlich aus dem Editor aufgerufen. Laut
GDD entsteht ein Floor beim Portal-Eintritt, also zur Laufzeit — die
Pipeline-Stufen brauchen später einen zweiten Aufrufer. Das Tool bleibt der
Editor-Aufrufer für Vorschau und Preset-Tuning.
(3) „Projekt-Typ Uni/Privat … ändert sich nie mitten im Projekt"
(2026-07-17) trifft nicht zu: Isor's Tower ist der Uni-Prototyp, der nach
dem Studium als privates Release-Projekt weiterläuft. Der Typ wechselt genau
einmal, zum Studienende — das ist der geplante Ablauf, kein Sonderfall, und
genau der Moment, in dem Block 1 (Uni-Pflichtregeln) entfernt wird.
Warum: Pauschale Formulierungen werden später als Verbot gelesen und führen
zu Umbauten, die nie nötig waren. Keine der drei Korrekturen verlangt eine
Code-Änderung vor der Abgabe.
Verworfen: die Einträge umschreiben (Historie ginge verloren); sie
unverändert stehen lassen (führen später in die Irre).

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

## 2026-07-30 — Abgabe-Szene, Spielbar-Definition, Village als eigenes Prefab
Was: `Village.unity` (die generierte Szene) ist die Abgabe-Szene;
`Scene_StartEntry_Village` wird nur noch Fundgrube (VFX, Global Volume,
HerdManager). „Spielbar" heißt für die Abgabe: Menü → Village → laufen →
bevölkerte Welt → einige Dinge reagieren → Pause/Quit, Konsole fehlerfrei —
kein Kampf, keine Quests. Alles Handgebaute im Dorf wird **ein** `Village`-
Prefab, das neben dem Tool-Ast in der Szene liegt.
Warum: Die generierte Szene zeigt Tool und Pipeline im echten Einsatz — das
ist der benotete Teil; die alte Szene aufzuwerten hieße, das generierte
Terrain gegen handgebautes zu tauschen (Doppelarbeit). Kampf steht in keinem
Feedbackelement beider Aufgaben. Ein Prefab ist eine Wahrheit, überlebt Szene
und Terrain-Rebuild, erlaubt verschachtelte Haus-Prefabs und Varianten
(„Village klein" für die Abgabe) und trifft die GDD-Trennung „festes Dorf,
prozedurale Bepflanzung darauf".
Verworfen: alte Szene als Abgabe; beide Szenen pflegen (zwei NavMesh-Bakes,
zwei Bug-Quellen); volle Gameplay-Schleife; reine Tech-Demo ohne Player
(verschenkt Lernziel S3); Dorf als lose Objektsammlung in der Szene.

## 2026-07-30 — Hierarchie-Vertrag: generierter Ast gegen handgebauten Ast
Was: Was unter „Generated …" liegt, gehört dem Tool und ist jederzeit
wegwerfbar; Handgesetztes liegt **daneben, nie darunter**. Szenen-Wurzeln:
`Generated Terrain` (Tool), `Village` (Prefab), `Navigation`, `Player`, `Game`.
Warum: `TerrainToolPresenter` sucht den Terrain-Root, löscht ihn per
`DestroyImmediate` und legt ihn neu an (Zeile 74–79) — bewusst so, damit
veraltete Platzierung automatisch verschwindet. Genau deshalb löscht ein
einziger Generate-Klick alles, was versehentlich darunter liegt.
Verworfen: Häuser/NPCs unter dem Terrain-Root; Aufräumen statt Neuanlegen im
Presenter (der Rebuild ist gewollt, siehe DECISIONS 2026-07-19).

## 2026-07-30 — NavMeshSurface raus aus dem generierten Ast
Was: Der `NavMeshSurface` zieht von „Generated Terrain" auf ein eigenes
Szenen-Objekt `Navigation` (kein Prefab). Reihenfolge festgezurrt:
Weltgröße/Verteilung final → NavMesh backen → NPCs setzen.
Warum: Fund dieser Session — der Surface sitzt heute auf genau dem Objekt,
das jedes Generate zerstört; danach ist die gebackene NavMesh an niemanden
mehr angeschlossen und jeder `NavMeshAgent` steht auf nichts, ohne Fehler in
der Konsole. Backen ist zudem teuer und skaliert quadratisch: bei Voxelgröße
0,1667 m sind es auf 2048 m Kante ~151 Mio Voxelspalten, auf 512 m nur
~9,4 Mio (16×) — jede spätere Terrain-Änderung wirft die Bake weg. Ins
Village-Prefab kann der Surface nicht, weil der begehbare Boden (das
generierte Terrain) außerhalb des Prefabs liegt.
Verworfen: Surface im Village-Prefab; NPCs vor der finalen Weltgröße setzen;
NavMesh-Bake nach jedem Generate automatisch mitlaufen lassen (Minuten pro
Klick beim Tunen).

## 2026-07-30 — NPC-Platzierung: die Ortsbindung entscheidet, nicht die Gattung
Was: Was an einem **bestimmten** Ort stehen muss (Herde beim Dorf, später
Händler), wird von Hand ins Village-Prefab gesetzt. Was nur **irgendwo
passend** stehen muss (Goblins im Umland), streut der ObjectPlacer als
`Placeable`-Zeile. Für NPC-Placeables gilt: `alignToGround` aus, Scale fix
(1,0), sonst kippen und stauchen sie wie Deko.
Warum: Lernziel S3 der PCG-Aufgabe verlangt ausdrücklich eine „generierte
Bevölkerung"; der Placer ist prefab-blind, ein Goblin kostet ihn keine Zeile
neuen Code. Handgesetzt bleibt, was Komposition braucht — dafür ist ein
Zufallsstreuer das falsche Werkzeug. Ein Kriterium („muss es dort stehen?")
statt zweier Gewohnheiten hält die Grenze überprüfbar.
Verworfen: alles per Placer (Dorfbild dem Zufall überlassen); alles von Hand
(S3 ungenutzt); Trennung nach Gattung (Schafe hier, Goblins dort).

## 2026-07-30 — Erster Baustein: Interaktion anschließen, Fackel als zwei Klassen
Was: Nächster Baustein ist nicht das Dorf, sondern das Interaktionssystem in
Betrieb nehmen: Layer `Interactable` anlegen, `PlayerInteractor` und
`InteractionPromptView` samt Prompt-UI ins Player-Prefab, dann `Torch`
(Fähigkeit: `IsLit`, schaltet VFX und Light) + `TorchInteractable` (Adapter,
liefert den Prompt und leitet weiter), danach die Schafe.
Warum: `IInteractable`, `PlayerInteractor`, `InteractionPromptView` und
`SheepInteractable` existieren seit 27.07., sind aber **nirgends verdrahtet** —
die Script-GUIDs kommen weder im Player-Prefab noch in `Village.unity` vor.
Es fehlt kein Code, sondern der Anschluss. Zwei Klassen für die Fackel, weil
der `DayNightCycleEventManager` sie abends schalten muss, ohne dass jemand
auf sie zielt: zwei Aufrufer für dieselbe Fähigkeit = Fähigkeit und Adapter
trennen, genau wie `Sheep` / `SheepInteractable`.
Verworfen: eine Klasse für Fackel und Interaktion zugleich; das bestehende
System zum Lernen neu schreiben (es läuft, und die Zeit bis 2026-08-21 ist
knapp — gelernt wird am neuen Stück).

## 2026-07-30 — Prompt-Aktualisierung: Vergleich auf den Prompt erweitern
Was: `PlayerInteractor.UpdateTarget` vergleicht künftig Ziel **und**
Prompt-Text; nur wenn beides unverändert ist, bricht es ab.
Warum: Objekte mit wechselndem Prompt bleiben sonst auf dem alten Text
stehen — die Fackel brennt, angezeigt wird weiter „Light torch", weil
`ReferenceEquals` dasselbe Objekt sieht. „Ziel gleich" ist eben nicht
dasselbe wie „Anzeige aktuell". Der erweiterte Vergleich kostet einen
Property-Aufruf und einen String-Vergleich pro Frame und deckt auch
Änderungen ab, die der Spieler gar nicht ausgelöst hat (Fackel geht bei
Sonnenaufgang von selbst aus).
Verworfen: `_currentTarget = null` nach `Interact` (deckt nur selbst
ausgelöste Änderungen ab); ein Änderungs-Event im `IInteractable` (bläht den
Vertrag für jeden Implementierer auf).

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
