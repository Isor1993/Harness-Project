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

## 2026-08-02 — Interaction-Prompt: statisch serialisiert, dynamisch berechnet, Interface minimal
Was: `IInteractable.InteractionPrompt` bleibt ein reiner Getter; wie ein
Implementierer den Text herstellt, ist seine Sache. Statische Prompts aus einem
serialisierten Feld (Inspector, kein Hardcoding), dynamische aus einer berechneten
Property. Die Fackel hält zwei serialisierte Texte (`_promptWhenLit`/
`_promptWhenUnlit`) und wählt live nach `IsLit`.
Warum: Ein einzelnes serialisiertes Feld kann einen zustandsabhängigen Prompt nicht
abbilden (fror den Text ein — derselbe „gespeicherter Wert veraltet"-Fehler). Das
Interface schlank zu halten erlaubt beide Wege ohne Vertrags-Aufblähung.
Verworfen: Prompt-Pflichtserialisierung im Interface (unmöglich, erzwingt statisch);
ein einzelnes serialisiertes Feld auch für dynamische Prompts.

## 2026-08-02 — TorchMode-Enum statt zwei Bools
Was: Zyklus-Kopplung + Startzustand der Fackel als ein Enum `TorchMode`
(FollowDayNight / StartLit / StartUnlit), nicht zwei unabhängige Bools.
Warum: Zwei Bools erlauben vier Kombinationen, eine widersprüchlich (folgt +
Startzustand). Das Enum macht den ungültigen Zustand undarstellbar — der
Inspector-Picker bietet nur die drei gültigen Modi. Folgt der Projekt-Linie
„falschen Wert an der Eingabe verhindern" (DECISIONS 2026-07-18) statt Runtime-Guard.
Verworfen: zwei Bools + OnValidate-Guard; reiner Runtime-Check.

## 2026-08-02 — Pause-Menü-Navigation: Hover setzt Selection, Startauswahl im Controller
Was: Maus-Hover setzt die EventSystem-Selection (`SelectOnHover`, `Shared/UI/`),
damit Maus und Tastatur einen Zustand teilen; die Startauswahl beim Öffnen setzt
`GameController.Pause()` per Code. Voller Maus/Tastatur-Moduswechsel (Cursor +
Highlight je Gerät) = Polish.
Warum: Hover-Highlight und Selection sind getrennte Zustände, die auseinanderdriften;
ein Leer-Klick löscht die Selection. Das Inspector-Feld „First Selected" wirkt nur
beim Szenenstart, nicht bei später aktiviertem Menü — die Startauswahl gehört dem
Menü-Besitzer und muss beim Öffnen per Code gesetzt werden. `SelectOnHover` als
eigenes Shared-UI-Script, weil Hover-Verhalten pro Element in Unity auf dem Element
wohnt (kein Smell).
Verworfen: klebrige Re-Selection im GameController-Update als Hauptlösung
(Hover-Sync ist sauberer); Voll-Moduswechsel jetzt (Aufwand → Polish).

## 2026-08-02 — Celestial-Rig getrennt vom Logik-Objekt; Aufräum-Funde
Was: Sonne + Mond hängen unter einem eigenen `ClestialPivot` (den `SkyController`
dreht), getrennt vom DayNightCycle-Logik-Prefab. Nebenbei behoben: freistehende
Szenen-`Main Camera` gelöscht (Player-Prefab bringt Kamera + AudioListener mit —
sonst zwei aktive Kameras/Listener), Raycast-Target am unsichtbaren HUD-Container aus.
Warum: SRP — Logik-Objekt macht Logik, Pivot ist die physische Rig; Sonne/Mond müssen
unter dem gedrehten Objekt hängen (ein Elternteil dreht sich nicht mit dem Pivot).
Deckt den Aufräumpunkt „zwei Kameras" aus DECISIONS 2026-07-30.
Verworfen: Sonne/Mond direkt unters Logik-Objekt (funktioniert, vermischt aber das
wiederverwendbare Logik-Prefab mit szenen-spezifischen Lichtern).

## 2026-08-03 — SO als Startwert, Inspector-Feld als Wahrheit
Was: Serialisierte Felder werden in `Awake` einmalig aus dem ScriptableObject
gefüllt; alle Lesestellen greifen danach auf das Feld zu, nicht aufs SO.
Betrifft `Sheep._type`, `SheepSense` (Radien, Layer, Farben, `_useLocalOverrides`)
und `SheepMoveBehaviour` (Speed-/Flee-Werte).
Warum: `Awake` läuft einmal — dadurch lässt sich im laufenden Play Mode am
einzelnen Objekt tunen, ohne das SO für alle Schafe zu ändern, und der Inspector
zeigt beim Start die effektiven Werte als Ausgangspunkt. Verloren geht nur, was
vor dem Play-Start eingetragen wurde; das ist der bewusste Preis.
Verworfen: direkt aus dem SO lesen (kein Einzelobjekt-Test möglich); das Feld gar
nicht füllen (Inspector zeigt dann nicht, womit das Objekt wirklich arbeitet).

## 2026-08-03 — Konstanten SCREAMING_SNAKE statt PascalCase
Was: Konstanten heißen `MAX_TRIES`, `WALK_STOP_DISTANCE` — bewusste Abweichung
von Block-1-Regel 5 (PascalCase für Konstanten), vermerkt in CODE_GUIDELINES.
Warum: Der Code war darin schon durchgängig konsistent (`MAX_TRIES`,
`UPDATE_TIME`), und die Schreibweise trennt Konstanten im Lesefluss sofort von
Properties, die ebenfalls PascalCase tragen. Ein dokumentiertes Abweichen ist
bei einer benoteten Abgabe stärker als eine Regel, der der Code nicht folgt.
Verworfen: sechs bestehende Stellen auf PascalCase umstellen (Aufwand ohne
Lesbarkeitsgewinn); die Abweichung gar nicht dokumentieren (Guideline und Code
würden auseinanderlaufen).

## 2026-08-02 — Herde als platzierbares Prefab: Injektion statt Szenen-Referenzen
Was: `HerdManager.Awake` injiziert sich selbst und den Graveyard-Marker per
`Sheep.Init(herd, graveyard)` in alle Pool-Mitglieder; die Schafe halten keine
serialisierten Referenzen auf HerdManager oder Graveyard mehr. Der Graveyard ist
ein eigener Marker im Prefab jeder Herde, kein geteiltes Szenen-Objekt.
Warum: Die Herde soll wie das Village ein platzierbares Prefab sein —
serialisierte Referenzen auf Szenen-Objekte überleben das Instanziieren nicht.
Ein geteilter Graveyard hätte genau die Szenen-Abhängigkeit zurückgebracht, die
das Prefab vermeiden soll; die geteilte Variante bräuchte ein
`RuntimeReference<T>`-SO (Werkzeug-Kriterium „Service über Szenengrenze").
Verworfen: geteilter Graveyard für alle Herden; Szenen-Verdrahtung von
HerdManager und Graveyard an jedem einzelnen Schaf.

## 2026-08-02 — Commander als Herdenführer, RVO-Priorität nach Rolle
Was: Nur das Zähmen des Commanders löst `SetAllSheepHerdMoving(true)` aus —
ein gezähmtes Normal-Schaf folgt dem Spieler allein, ohne die Herde in Bewegung
zu setzen. Der Commander bekommt `avoidancePriority = 0`, Normal-Schafe
`Random.Range(30, 70)`.
Warum: Die Herde braucht einen Anker, der sich nicht wegschieben lässt — in
Unitys RVO gewinnt die niedrigere Zahl. Gestreute Prioritäten für die
Normal-Schafe verhindern, dass zwei gleichrangige sich gegenseitig blockieren.
Ein einzelner Herdenführer macht das Zähmen zur Entscheidung statt zur
Sammelaktion.
Verworfen: jedes gezähmte Schaf startet die Herdenbewegung (die Herde wäre nicht
mehr gezielt steuerbar); gleiche Priorität für alle (Deadlocks zwischen Schafen).

## 2026-08-02 — Dodge nur im Patrol, Tie-Break per EntityId
Was: `TryEnterDodge` wird nur noch aus `PatrolState` gerufen (aus Regroup,
HerdMoving und FollowPlayer entfernt). Treffen zwei Schafe aufeinander, weicht
nur das mit der höheren `EntityId` aus; dazu ein Cooldown nach jedem Dodge und
ein `HasReachedDestination`-Guard. `SheepFSM.ChangeState(SheepStateBase)` ist
public, `DodgeState` kehrt über den gemerkten `_returnState` zurück statt über
einen Typ-Switch.
Warum: Ohne Tie-Break weichen beide Schafe gleichzeitig aus und spiegeln sich
endlos. Schaf-gegen-Schaf löst Unitys RVO ohnehin schon; der eigene Dodge ist
für feste Hindernisse da und stört in Formation mehr, als er hilft. Die
generische Rückkehr macht `DodgeState` unabhängig davon, welche States es gibt —
ein neuer Bewegungs-State braucht dort keine Änderung.
Verworfen: Dodge in allen Bewegungs-States; Typ-Switch in `DodgeState`; elegante
Crowd-Avoidance jetzt bauen (vorgemerkt für nach der Abgabe).

## 2026-08-03 — Nur ein gezähmtes Schaf, gemerkt in einem SO-Asset
Was: Der Spieler kann projektweit nur ein Schaf zugleich führen.
`TamedSheepReference` (ScriptableObject in `Entities/Sheep/SO_Settings/`) hält den
Zeiger auf das gezähmte Schaf; `SheepInteractable.CanInteract` verweigert das
Zähmen, solange der Zeiger belegt ist — ein bereits gezähmtes Schaf lässt sich
dagegen immer freilassen. Der Zeiger wird beim Lesen validiert
(`!= null && IsAlive && IsTamed`) statt von außen aufgeräumt.
Warum: Die Herdenformation ist um einen Anker gebaut, zwei folgende Schafe
streiten sich um dieselben Slots — die Sperre verhindert den Fehler, statt ihn
später zu reparieren. Vom Spielgefühl gehört „mein Schaf" zum Spieler, technisch
geht das nicht: Schafe sind Prefabs und können keine Szenen-Referenz halten, und
`IInteractable.CanInteract` bekommt den Interactor nicht — eine rein
spielerseitige Regel hätte den Tastendruck blockiert und den Prompt trotzdem
stehen gelassen. Auf ein Asset darf ein Prefab zeigen. Die Prüfung beim Lesen
macht einen Zähler überflüssig, der bei Zähmen, Freilassen, Tod und Respawn
mitgepflegt werden müsste; der Merkzettel bleibt ein Zeiger auf `Sheep._isTamed`,
keine zweite Wahrheit.
Verworfen: Zähler im HerdManager (vier Pflegepfade, bei einem vergessenen still
falsch); Regel pro Herde (heute identisch, bräche still bei der zweiten Herde);
`CanInteract` um den Interactor erweitern (änderte den Vertrag für alle
Implementierer, gegen DECISIONS 2026-08-02 „Interface minimal").

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

## 2026-08-06 — Zähmen wirkt sofort, schlafende Schafe sind nicht zähmbar
Was: `Sheep.ToggleTame()` schaltet das Flag um und erzwingt beim Zähmen den
Wechsel in `FollowPlayerState`; das Freilassen bleibt ungezwungen.
`SheepInteractable.CanInteract` liefert für ein schlafendes, ungezähmtes Schaf
`false` — der Interactor verwirft das Ziel, der Prompt erscheint gar nicht.
Dreht die Absicht vom 27.07.2026 um, den Zeitpunkt bewusst der FSM zu überlassen.
Warum: Nur `PatrolState` und `OnAlertState` prüfen das Tame-Flag von sich aus;
`Eating`, `Sleeping`, `Idle`, `Regroup`, `HerdMoving` und `Dodge` gar nicht. Ein
fressendes Schaf reagierte erst beim Sattwerden, ein patrouillierendes erst am
Wegpunkt, und in `OnAlert` kam die Reaktionszeit obendrauf — der Spieler wartete
auf seinen eigenen Tastendruck. Das Freilassen braucht keinen Zwang, weil
`FollowPlayerState.Tick()` `!IsTamed` ohnehin je Frame prüft; damit bleibt die
ziehende FSM erhalten und nur der Eintritt wird gedrückt.
Tragend ist die Reihenfolge in `CanInteract`: Die Schlafprüfung steht **hinter**
dem `IsTamed`-Early-Return. Das Schlaf-Flag folgt der Tageszeit, nicht dem
Zustand des Schafs — stünde die Prüfung davor, hinge ein gezähmtes Schaf bei
Einbruch der Nacht bis zum Morgen am Spieler fest.
Verworfen (Zähmen): Zähmen weckt ein schlafendes Schaf (berührte `_isSleeping`,
`SleepingState` und die Hunger-Pause — drei Stellen für einen seltenen Fall);
jedem State eine eigene Tame-Prüfung geben (verteilt dieselbe Logik auf sechs
Dateien und muss bei jedem neuen State mitgepflegt werden); zusätzliche
`IsCurrentState<DeadState>()`-Absicherung (`IsAlive` fängt es bereits zweifach
ab, in `CanInteract` und in `ToggleTame`).

## 2026-08-06 — UML-Diagramme werden erzeugt statt gezeichnet
Was: Die Diagramme fürs TDD entstehen per Skript als fertige `.drawio`-Datei.
Werkzeuge unter `C:\IsorBackup\05_Werkzeuge\Vorlagen\`: `uml_drawio.py`
(Klassenkästen + UML-Linienstile), `diagramm_<name>.py` je Diagramm,
`pruefer.py` (vergleicht das Ergebnis gegen den Quellcode). Claude bedient die
Skripte, Isor ordnet einmal an; `positionen_lesen()` übernimmt seine Anordnung
bei jeder Neuerzeugung. Erstes erzeugtes Diagramm: Sheep-Komponentensystem,
17 Klassen, 18 Beziehungen, Prüfer meldet null Abweichungen.
Warum: Die alten Diagramme sind veraltet, weil Aktualisieren zu teuer war —
alles von Hand, bei jeder Code-Änderung neu. Die Aufteilung folgt den Stärken:
Die Maschine übernimmt Korrektheit (Namen direkt aus dem Code, Linienarten,
Vollständigkeit), Isor die Optik. Genau die Korrektheit war das Problem
(zwei falsche `HerdManager`-Methodennamen fielen erst beim Testlauf auf), die
Optik nie. Der Prüfer ersetzt das Gegenlesen aller Member durch einen Bericht
von wenigen Zeilen.
Verworfen: Mermaid als Zwischenformat (draw.io importiert es, macht aber aus der
gefüllten Kompositionsraute eine hohle Aggregation — die Bedeutung ändert sich
still); automatische Anordnung (schweres Graph-Problem, Ergebnis wäre schlechter
als 10–15 Minuten Schieben); Diagramme weiter von Hand zeichnen (der Zustand,
der zu den veralteten Diagrammen geführt hat).

## 2026-08-07 — Claude bearbeitet die TDD-Datei direkt
Was: Änderungen am TDD schreibt Claude selbst in
`01_Uni\Semester_2\Arbeitsdateien\TDD Softwareplanung.docx`, nicht mehr als
Textblock zum Kopieren. Technisch wird nur `word/document.xml` als Text
verändert, alle übrigen Archivteile werden unverändert übernommen — Bilder,
Formatvorlagen und Beziehungen werden nicht angefasst. Vor jeder Änderung
entsteht eine Kopie unter `Arbeitsdateien\Sicherung\` mit Zeitstempel; nach
jeder Änderung wird geprüft, dass die Teilezahl gleich blieb und außer
`document.xml` nichts abweicht. Bedingung: Die Datei darf in Word nicht offen
sein. Bilder einfügen, Verzeichnisse erzeugen und Seitenumbrüche bleiben bei
Isor. Neue Aufzählungspunkte werden aus einem bestehenden Punkt derselben
Liste geklont, damit Nummerierung und Einrückung sicher stimmen.
Warum: Der Weg über Textblöcke kostete pro Kapitel zweimal Arbeit — Isor musste
einfügen, und Claude musste anschließend das ganze Dokument neu einlesen, um zu
sehen, was angekommen ist. Diese Volldumps waren der mit Abstand teuerste Posten
der Session. Direktes Schreiben spart sie vollständig. Dazu kommt Isors
Lese-Rechtschreib-Schwäche: Abtippen erzeugt Fehler, Kopieren aus dem Chat
schleppt Formatierung nach Word.
Die frühere Zurückhaltung („Claude fasst die .docx nicht an") bezog sich auf den
Verlust der 16 Abbildungen — der entstand aber durch Words Formatwechsel
zwischen `.odt` und `.docx`, nicht durch XML-Bearbeitung.
Verworfen: Textbausteine als `.txt` neben der Arbeitsdatei (ein Umweg mehr statt
weniger, von Isor nach einem Versuch abgelehnt); Blöcke im Chat mit
`Strg+Umschalt+V` (funktioniert, löst aber weder die Nacharbeit noch das
Wiedereinlesen).

## 2026-08-07 — Zeiterfassung im TDD tageweise, ohne Schätzspalte
Was: Die neuen Zeitkapitel 5.3 bis 5.6 führen eine Zeile pro Arbeitstag statt
pro Arbeitsschritt und haben nur noch vier Spalten — die Spalte „Geschätzte
Zeit" entfällt. Die Gliederung folgt den vier Work Items aus Grindstone
(`Semester2_PCG` 37:41, `Semester 2_Isor Tower` 27:24, `Thread Optimierung`
9:56, `SoftwarePlanung` 7:44, zusammen 82:45). PCG und Engine-Tool stehen in
einem gemeinsamen Kapitel.
Warum: Feiner aufzuteilen als gemessen wurde hieße, die Stunden innerhalb eines
Tages zu schätzen — erfundene Zahlen in einer Zeiterfassungstabelle. Die
Tagessumme ist gemessen, und was an dem Tag entstand, steht datiert im
FEATURE_LOG; damit ist jede Angabe belegt. Geschätzt wurde für diese Module
nichts, also steht dort auch nichts; die Methodenänderung wird im Fließtext
benannt statt kaschiert. PCG und Tool gemeinsam, weil das Tool die
Bedienoberfläche der Pipeline ist und jede Pipeline-Stufe ihre Bedienung sofort
mitbekam — eine getrennte Erfassung wäre nachträglich konstruiert.
Festgehalten wird außerdem, dass die Werte eine Untergrenze sind: Tutorials in
der Freizeit wurden nicht getrackt, und rund zehn Stunden Gras-Arbeit vom
04./05.08. liegen unter „Isor Tower", gehören fachlich aber zur PCG-Aufgabe.
Verworfen: Stunden nachträglich auf Einzelaufgaben verteilen; die Schätzspalte
mit nachgereichten Werten füllen; die Gras-Stunden ins PCG-Kapitel umbuchen
(hätte die Messung frisiert).

## 2026-08-08 — Beschriftungen und Verweise im TDD sind Word-Felder
Was: Alle 48 Beschriftungen wurden auf Zählfelder (`SEQ`) umgestellt und mit
einer Textmarke umschlossen; alle 39 Verweise im Fließtext („siehe Abbildung
19") wurden zu Verweisfeldern (`REF`) auf diese Marken. Vorher enthielt das
Dokument kein einziges Feld, alle Nummern waren getippt. Kontrolle: sichtbarer
Text vorher und nachher zeichengleich (85.453 Zeichen), kein Verweis ohne
Textmarke, Archivteile 56 → 56.
Warum: Die neuen Diagramme gehören in die Kapitel UML und Programmablaufplan,
die **vor** dem Shader-Kapitel stehen. Jedes eingefügte Diagramm hätte von Hand
31 Beschriftungen und 31 Verweise verschoben — bei jeder Einfügung neu. Zweiter
Grund: Abbildungs- und Tabellenverzeichnis lassen sich ohne Felder überhaupt
nicht erzeugen, und beide sind laut Formatierungsvorgaben Pflicht.
Isors eigener Versuch scheiterte an der Alles-oder-nichts-Eigenschaft: Ein
`SEQ`-Feld zählt nur andere `SEQ`-Felder, nie getippten Text. Eine einzelne
automatische Beschriftung zwischen 47 getippten wird deshalb korrekt als
„Abbildung 1" ausgewiesen und sieht dadurch kaputt aus.
Merkposten für die Bedienung: `Alt+F9` schaltet zwischen Feldfunktion und Wert
um — steht die Anzeige auf Feldfunktion, erscheinen alle Felder als Code,
inklusive der Seitenzahl in der Fußzeile. `Strg+A` und `F9` aktualisiert die
Werte.
Verworfen: nur die Beschriftungen umstellen und die 39 Verweise am Ende von Hand
prüfen (billiger, aber die Handarbeit fällt bei jeder Einfügung erneut an);
Umstellung erst nach dem Einfügen der Diagramme (dann käme die Umnummerierung
von Hand obendrauf).

## 2026-08-08 — Unity-Ordner folgen den Uni-Systemgrenzen
Was: `Systems/TerrainGenerator/` ist in vier Systeme aufgeteilt — `WorldGeneration/`,
`ObjectPlacement/`, `GrassRendering/` und `TerrainTool/Editor/`. 26 Skripte plus
6 Assets verschoben, keine Code-Änderung nötig.
Warum: Das TDD-Kapitel beschreibt die Architektur, und die Beschreibung soll zur
endgültigen Ablage passen statt zu einer, die kurz danach umgebaut wird. Der Umzug
war zudem kostenlos: Keine der Dateien hat einen `namespace`, es gibt kein `.asmdef`
— nichts konnte brechen. Zieht ROADMAP-Punkt 8 (Gras herauslösen) mit vor.
Verworfen: Threading als eigener Ordner (die Parallelisierung sitzt in `ObjectPlacer`
und `GrassCellBuilder`, also quer über zwei Systeme — ein eigener Ordner hätte sie
auseinandergerissen); Umbau erst nach der Abgabe.

## 2026-08-08 — TDD-Kapitel 6.3 nach Pipeline-Stufen statt nach Klassen
Was: Kapitel 6.3 ist in sieben Unterkapitel entlang der Pipeline gegliedert
(Überblick, Config, Heightmap, Plateau, Mesh, Placer, Gras-Rendering) statt in eine
Überschrift je Klasse wie in 6.1 und 6.2.
Warum: Eine Überschrift je Klasse hätte 24 Unterkapitel ergeben, und der Ablauf der
Pipeline — das eigentlich Erklärungsbedürftige — wäre in der Liste untergegangen.
Klassen werden innerhalb ihres Abschnitts genannt und erklärt.
Verworfen: 24 Einzelkapitel (konsistent zum Rest, aber unlesbar); drei getrennte
Hauptkapitel je Ordner (hätte die Pipeline als Zusammenhang zerschnitten).

## 2026-08-08 — Vier neue Diagramme für den Terrain-Ast, Sheep-System braucht keins
Was: Erzeugt wurden Terrain-Pipeline (5 Klassen), Platzierung (14, mit vollständig
dargestelltem Strategy-Muster), Gras-Rendering (8) und Editor-Tool (8, MVP von links
nach rechts lesbar). DayNightSystem und Sheep-FSM wurden neu erzeugt, die
handgezeichneten Vorgänger archiviert.
Warum: Die Tool-Aufgabe verlangt Klassendiagramm und Ablaufdiagramm, und für den
gesamten Terrain-Ast existierte keines. Vier statt zwei Diagramme, weil ein einzelnes
mit 25 Klassen unlesbar würde — das Sheep-Diagramm hat 17 und ist bereits voll.
`Sheep_System_UML` wurde ersatzlos archiviert: `Sheep_Komponenten` deckt es
vollständig ab und enthält sechs Klassen mehr.
Verworfen: alle alten Diagramme sofort neu erzeugen (Prüfung zeigte nur einen harten
Fehler; die Zeit gehört in die fehlenden Pflichtdiagramme).

## 2026-08-08 — Diagramm-Werkzeug hält die Handarbeit über Neuerzeugungen
Was: `positionen_lesen` ordnet über den **Klassennamen** zu statt über die Id; neu
sind `kanten_lesen`/`kanten_wiederherstellen` für Linien-Wegpunkte, Andockpunkte und
die Lage der Multiplizitäts-Beschriftungen. Andockpunkte an Member-Zeilen werden auf
den Kasten umgerechnet. Linienstärke zentral als `LINIENSTAERKE = 2`.
Warum: Vier Verlustwege sind im Praxisbetrieb aufgefallen — draw.io vergibt beim
Kopieren neue Ids; es dockt gezogene Enden an einzelne Member-Zeilen an; es lässt
eine Koordinate von 0 weg; und Wegpunkte hielt das Werkzeug gar nicht. Jeder davon
hätte eine Stunde Anordnung lautlos gekostet. Geprüft: zweiter Lauf erzeugt alle
sieben Dateien byte-identisch.
Verworfen: Andockwerte auf 0–1 begrenzen (draw.io lässt sie bewusst überstehen, das
Begrenzen zog Linienenden auf die Kante zurück); Eintrittspunkte automatisch
verteilen (hätte die bereits von Hand angeordneten Kanten verrückt — bleibt als
Kommentar für künftige Diagramme stehen).

## 2026-08-08 — Gras-Verteilung bleibt auf Uniform
Was: Das Gras-Placeable nutzt `UniformDensity`, nicht die gebaute `NoiseMaskDensity`.
Warum: Isors Entscheidung beim Tunen — gleichmäßig sieht in der noch leeren Welt
besser aus. Für das TDD zusätzlich wertvoll: Uniform ist der Worst Case der
Laufzeitmessung, jede Maske dünnt aus. Die gemessenen 12,4 s sind damit eine obere
Grenze, kein geschönter Wert. Im Text steht die Maske als gebaut und begründet
abgeschaltet.

## 2026-08-09 — Ablaufpläne über dieselbe Werkzeugkette wie die Klassendiagramme
Was: Sechs Sinnbilder nach DIN 66001 in `uml_drawio.py` (`knoten`/`pfeil`), ein
Skript `ablauf_generate_complete.py` je Plan, Ablage und Bedienregeln unverändert.
Sinnbilder werden über ihre **Id** zugeordnet, nicht über ihren Text.
Warum: Der Text taugt nicht als Schlüssel — „Ende" kommt in einem Plan mehrfach vor,
und bei den Klassendiagrammen ist der Name nur deshalb der richtige Schlüssel, weil
er dort eindeutig ist. Ein zweites Werkzeug wäre die Alternative gewesen; dagegen
sprach, dass Erhalt der Handarbeit, Linienstärke und Datei-Hülle sonst doppelt
gepflegt werden müssten. Nachgewiesen, dass die Klassendiagramme unberührt bleiben:
kein Klassendiagramm hat einen Kasten außerhalb der Swimlanes auf oberster Ebene.
Verworfen: Ein zweiter Plan für das Innere von `SpawnType` — er würde den ersten
verdoppeln; `SpawnType` steht als Unterprogramm-Sinnbild darin. Bei Bedarf
nachziehbar, die Formen sind da.

## 2026-08-09 — Messreihe als Tabelle mit 10-pt-Schrift
Was: Die Messreihe in TDD 6.5 steht zusätzlich als Tabelle (sechs Messpunkte,
Spalten Erzeugen/Filtern, Ausschluss, Zellbau, Gesamt, Verbesserung). Tabellenschrift
10 pt statt der 12 pt des Fließtextes.
Warum: Bei 12 pt passen sechs Spalten nicht auf die Satzbreite — Word trennt dann
mitten im Wort („Ausschlussfilte r"). Weiche Trennzeichen halfen nicht, Word zeigt
sie in dieser Datei durchgehend an. Spalten zu streichen hätte die Aussage gekostet:
Erst die Abschnittsspalten zeigen, dass der Gewinn zwischen den Messpunkten die
Stelle wechselt. Die Formatvorgaben regeln Fließtext (11–12 pt) und Beschriftungen
(9–11 pt), nicht den Tabelleninhalt.
Nebenwirkung: Die Tabelle steht vor der Asset-Tabelle und wird damit Tabelle 8; die
Asset-Tabelle rückt auf 9. Beide Nummern sind SEQ-Felder und rechnen beim
Aktualisieren selbst nach.

## 2026-08-11 — Bogensprung an Kreuzungen, und was eine Skript-Vorgabe darf
Was: `jumpStyle=arc` zentral in `uml_drawio.py`, damit sich kreuzende Linien einen
Bogen schlagen. Zweitens: Wo Isor ein Linienende bewusst frei am Kasten gelassen hat,
wird die Andockvorgabe im Skript **entfernt** statt beibehalten.
Warum: Zwei sich kreuzende orthogonale Linien sehen ohne Sprung wie ein T aus — man
sieht nicht, welche wohin führt. Der zweite Punkt ist die wichtigere Lehre: Eine
Vorgabe im Skript wirkt genau dort, wo in der Datei nichts gespeichert ist. Ein frei
gelassenes Ende ist deshalb kein „nichts", sondern eine Entscheidung, die das Skript
respektieren muss. Erkennungsmerkmal: `kanten_lesen` meldet für die Kante keinen
Andockpunkt, obwohl das Skript einen setzt. Fünf Kanten des Zustandsdiagramms waren
betroffen, zwei weitere nach Isors zweiter Überarbeitung.
Nebenbei behoben: `knoten()` schrieb Koordinaten als Ganzzahl und verschob dadurch
Kästen, die auf halben Pixeln sitzen.

## 2026-08-11 — Fazit dreiteilig statt als Mängelliste
Was: Kapitel 13 des TDD gliedert sich in erreichten Stand, tragfähige Ergebnisse und
offene Punkte nach Bereichen. Der Aufwand von 51 Stunden Dokumentation wird benannt
und mit der mehrsemestrigen Nutzung begründet.
Warum: Isors Sammlung offener Punkte war vollständig, aber zu 95 % eine Mängelliste.
Die stärksten Ergebnisse des Semesters sind gedanklich — Amdahl als Auswahlkriterium,
die Zwischenmessung, der dokumentierte gescheiterte Versuch. Ein Fazit, das nur
Restarbeit aufzählt, verschenkt sie. Die offenen Punkte stehen weiterhin vollständig
drin, aber als Reihenfolge-Entscheidung statt als Versäumnis.

## 2026-08-11 — Lizenzkapitel: Quellen selbst nachlesen statt Notizen glauben
Was: Vor dem Schreiben von TDD 12.4 bis 12.6 wurden alle drei Anbieterseiten
aufgerufen. Ergebnis: zwei Korrekturen an dem, was in unseren Notizen stand.
Warum: In `_Nachladen.md` stand pauschal „alle genannten Quellen sind CC0". Für
freestylized stimmt das nicht — dort gilt eine Royalty Free License, und die
Einschränkung zur Weitergabe steht nur auf der About-Seite, nicht bei der Textur.
Zweitens war der Verdacht, die Bäume stammten aus dem falschen Quaternius-Pack, ein
Fehlalarm: Die beigelegte `License.txt` ist bei allen Packs dieselbe. Lehre: Eine
Lizenzanalyse ist genau die Stelle, an der eine übernommene Angabe nichts wert ist.

## 2026-08-11 — S4-Abgabe aus dem TDD als Formatvorlagen-Spender gebaut
Was: Die verlorene Word-Fassung der S4-Aufgabe wurde neu erzeugt, indem alle Teile des
TDD-Pakets außer `document.xml` übernommen wurden — Formatvorlagen, Schrift, Fußzeile,
Nummerierung. Der Text kam wortgetreu aus der abgegebenen PDF.
Warum: So sieht die Abgabe ohne Nacharbeit aus wie das TDD, und es entsteht keine
zweite Formatwelt. Inhaltlich geändert wurden nur die Quellenangaben: Das Sekundärzitat
Shaker et al. wurde zum Direktbeleg, die Calgary-Quelle stand mit Vornamen statt
Nachnamen und mit fremdem Titel im Verzeichnis, und die Einleitung von Übungstext 4
hatte gar keinen Beleg. Damit ist das Feedback der Fachbetreuung („1–2 mehr Quellen")
erfüllt, ohne den Text umzuschreiben.

## 2026-08-11 — Zeugnis als vierter Session-Typ mit eigener Rules-Datei
Was: „Zeugnis" wird ein Modus im Harness, nicht eine Ausgabeform. WORKFLOW.md führt
ihn als vierten Session-Typ neben Brainstorm/Design, Development und Art; die Regeln
stehen vollständig in ASSESSMENT_RULES.md, die Zeugnisse in ASSESSMENT_LOG.md.
Auslöser ist der Skill `/zeugnis`, der die Rules-Datei lädt statt sie zu doppeln.
Warum: Der erste Entwurf hätte „Zeugnis" als vierten Artifact-Typ in ARTIFACT_RULES
eingehängt. Das war die falsche Ebene — die drei Typen sagen, worauf eine Seite
blickt, ein Zeugnis bewertet dagegen, und der Kern der Sache ist ohnehin die
Session, nicht die Seite. Gleiches Muster wie KNOWLEDGE_RULES und ARTIFACT_RULES:
eigene Datei, kurzer Zeiger von der zuständigen Stelle aus.
Verworfen: vierter Artifact-Typ (falsche Ebene, hätte die Pflegeregel „aktualisieren
statt neu anlegen" stillschweigend gebrochen); alles in WORKFLOW.md unterbringen
(hätte die Datei aufgebläht und die Belegpflicht unauffindbar gemacht); die Regeln
im Skill selbst halten (der Skill liegt außerhalb des Repos und wäre nicht
mitversioniert).

## 2026-08-11 — Zeugnis-Artifacts behalten je eine eigene URL
Was: Benannte Ausnahme von der Pflegeregel in ARTIFACT_RULES: Ein Zeugnis wird nie
aktualisiert und nie ersetzt, jedes bekommt eine neue URL. Die Ausnahme besitzt
ASSESSMENT_RULES.md; ARTIFACT_RULES verweist nur darauf, geführt werden die Seiten
weiterhin im ARTIFACT_INDEX. Beim Review-Gate werden sie übersprungen.
Warum: Bei Status, System und Lernstück ist der alte Stand wertlos, sobald der neue
existiert — beim Zeugnis ist er der halbe Zweck. Ein Zeugnis ist keine Ansicht auf
einen aktuellen Stand, sondern ein datierter Messpunkt.
Verworfen: eine sammelnde Zeugnis-Seite mit allen Ständen (wäre auf dem Handy
unlesbar geworden und hätte den direkten Vergleich zweier Termine erschwert).

## 2026-08-12 — Abgabe in zwei Ständen
Was: Es wird zweimal abgegeben. Stand 1 am So 16.08. ist vollständig und
benotbar, als gäbe es keinen zweiten Termin; Stand 2 am Mi/Do 19./20.08.
bringt nur noch Kleinigkeiten. Frist bleibt der 21.08.
Warum: Ein vollständiger früher Stand nimmt das Risiko aus der letzten Woche —
was am Sonntag liegt, kann nicht mehr schiefgehen. In der Woche darauf ist
ohnehin kaum Zeit, dort passen nur kleine Korrekturen.
Verworfen: einmal abgeben kurz vor der Frist (setzt alles auf einen Tag).

## 2026-08-12 — Spiel vor Dokumentation
Was: Do Ton, Fr UI, Sa Welt beleben und Abgabe-Material, So die gesamte
TDD-Restarbeit an einem Stück. Der frühere Plan hatte es umgekehrt.
Warum: Bis Samstag kommen Ton, UI und Beleuchtung dazu, die im Text stehen
müssen — ein früher Textstand beschreibt einen Stand, den es Sonntag nicht
mehr gibt. Zweitens ist der sichtbare Eindruck der schwächste Punkt des
Projekts (Zeugnis 2026-08-11: „die Systeme sind gut, aber sie zeigen sich
nicht"), und der Build entscheidet laut Vorgabe über die Funktionalitätsnote.
Verworfen: Textarbeit in die kurzen Abende legen und das Spiel ans Wochenende
(hätte doppelte Textarbeit erzeugt).

## 2026-08-12 — Neuer Abgabe-Satz statt Umbau des alten
Was: Der Endstand wird als eigener Ordner `Semester_2\Abgabe_Final\` nach
SAE-Vorgabe aufgebaut; die bestehenden Portfolio-Ordner unter `Abgabe\`
bleiben unangetastet. Die Unity-Projektkopie liegt einmal je Portfolio, nicht
je Aufgabe — die übrigen Aufgabenordner verweisen über den READ_ME-Baustein
„Folgende Aufgaben sind in anderen Ordnern zu finden".
Warum: Die alte Struktur ist der Beleg der formativen Abgaben und weicht in
drei Punkten von der Vorgabe ab (`Other` statt `other`, README je Aufgabe
statt einem READ_ME, keine Nummerierung). Getrennt aufbauen kostet nichts und
kann nichts zerstören. Die Kopie einmal je Portfolio spart 2 × 198 MB und hält
nur einen Stand nachziehbar.
Verworfen: die bestehenden Ordner an Ort und Stelle umbenennen; Projektkopie
je Aufgabenordner.

## 2026-08-12 — READ_ME knapp, Lizenzen als Tabellenzeile
Was: READ_ME der Abgaben sind Stichpunkte mit einem Ordnerbaum und den
Kriterien-Kürzeln je Aufgabe — kein Fließtext wie im ersten Semester. Neue
Audio-Quellen kommen als Zeilen in die Asset-Tabelle (Tabelle 9), nicht als
eigenes Unterkapitel.
Warum: Für die Bewertung zählt, dass der Prüfer die geforderten Punkte findet,
nicht wie ausführlich sie beschrieben sind. Eine Tabellenzeile mit Quelle und
Lizenz erfüllt den Nachweis vollständig; ein Unterkapitel je Sound würde den
Text doppeln.
Verworfen: Feature-Beschreibungen als Fließtext; Audio-Lizenzen als eigenes
Kapitel wie die Texturquellen in 12.1 bis 12.3.

## 2026-08-12 — Village-Prefab nicht neu aufbauen
Was: Der geplante Neuaufbau des Village-Prefabs (Häuser, Props, NavMesh) fällt
vor der Abgabe weg. Stattdessen Ton, UI und Beleuchtung.
Warum: Der bestehende Aufbau trägt und der NavMesh-Bake ist aktuell (geprüft
2026-08-12: `Village.unity` enthält null Kamera-Komponenten, die Notiz vom
2026-08-02 war überholt). Ein umgebautes Prefab sieht man im Build nicht,
fehlender Ton hört man sofort.
Verworfen: Village-Neuaufbau am Freitag als großen Block.

## 2026-08-14 — AudioMixer mit drei Gruppen statt Lautstärke je Quelle
Was: Ein `MainMixer`-Asset mit Master → Music/SFX; jede AudioSource wählt
ihre Gruppe. Die Optionen setzen später drei exponierte Parameter.
Warum: Ein Regler, der jede Quelle einzeln kennen müsste, vergisst jede
neu hinzugefügte. Über die Gruppe folgt alles automatisch.
Verworfen: Regler greift direkt auf `AudioSource.volume` zu; Sub-Mixer je
Kategorie (versehentlich zuerst gebaut — für drei Regler überdimensioniert).

## 2026-08-14 — Kein AudioManager
Was: Es gibt keine zentrale Audio-Klasse. Der Mixer ist ein Asset und wird
dort per `[SerializeField]` verdrahtet, wo er gebraucht wird.
Warum: Ein AudioManager wäre ein Singleton, und die sind in
CODE_GUIDELINES ausgeschlossen. Das Asset erfüllt denselben Zweck über
Inspector-Wiring — dasselbe Muster wie `PlayerInputReader` und `SceneLoader`.
Verworfen: die auf der Artifact-Seite „System · Grundgerüst" vorgemerkten
Klassen `AudioManager` und `SceneMusic`.

## 2026-08-14 — Wer den Klang auswählt, hält ihn auch
Was: Gibt es nichts auszuwählen, liegt der Clip in der AudioSource (Musik,
Fackel). Wählt ein Skript aus mehreren, liegen die Clips im Skript und das
Feld der Quelle bleibt leer (Schritte, Schafe, Wind).
Warum: Zwei gefüllte Stellen für dieselbe Sache — man weiß später nicht
mehr, welche gilt.
Verworfen: Clips grundsätzlich in der Quelle halten und im Skript nur
umschalten.

## 2026-08-14 — Der Interaktionsklang gehört zum Interactable
Was: Kein gemeinsamer Klang im `PlayerInteractor`. Jedes `IInteractable`
bringt seine eigene Rückmeldung mit — die Fackel über das startende Feuer,
das Schaf über einen Antwortlaut.
Warum: Der Interactor weiß bewusst nicht, was er vor sich hat; ein Klang
dort wäre für jedes Ziel derselbe. So bringt jedes neue Interactable seinen
Klang mit, ohne dass der Interactor angefasst wird.
Verworfen: ein generischer Interaktionslaut am Spieler. Die Quelle
`Audio_Interaction` bleibt bestehen, aber für Menügeräusche.

## 2026-08-14 — Eigener Timer je Quelle statt Event-Channel
Was: `RandomIntervalSound` hängt an jedem Objekt und zählt selbst.
Warum: Ein zentraler Sender, der tickt und Events verteilt, ließe alle
Schafe gleichzeitig blöken — aus einer Herde würde ein Chor. Die
Einsatzregel für Event-Channels („X passiert, unabhängige Systeme
reagieren") trifft nicht zu: Es gibt kein gemeinsames X.
Verworfen: Observer/Event-Channel mit zentralem Taktgeber.

## 2026-08-14 — Schrittfrequenz über Strecke statt Zeit
Was: `FootstepPlayer` addiert zurückgelegte Meter und löst bei 2 m aus,
statt einen Zeittakt zu verwenden.
Warum: Die Schrittfrequenz hängt damit ohne Umrechnung am Tempo — wer
langsamer läuft, legt langsamer 2 m zurück. Ein Zeittakt müsste die
Geschwindigkeit erst umrechnen, sobald es Sprinten gibt.
Verworfen: fester Zeitabstand; Tonhöhe an die Geschwindigkeit koppeln
(falsch — Tempo ändert die Frequenz der Schritte, nicht ihre Tonhöhe).

## 2026-08-14 — Alle verwendeten Klänge unter CC0
Was: Nur CC0-Material im Projekt. Das einzige CC-BY-Paket (Yo Frankie!,
Blender Foundation) wurde zurückgestellt; sein Ordner trägt `_CC-BY` im
Namen, die Belegzeile liegt fertig in seiner `_Quelle.txt`.
Warum: Es liegt ohnehin nur als FLAC vor, das Unity nicht importiert, und
der Wind wird von einem CC0-Paket abgedeckt. Damit braucht Tabelle 9 im TDD
keine Attributionsformel, nur Quelle und Lizenz je Zeile.
Verworfen: FLAC umwandeln und die Nennungspflicht in Kauf nehmen.

## 2026-08-14 — Audio-Library zweistufig
Was: `_Pakete\` hält die Originalpakete vollständig mit `_Quelle.txt`,
`Sortiert\` die nach Zweck einsortierten Kopien mit dem Paketnamen als
Dateipräfix. `_Katalog.md` verbindet beide.
Warum: Ein Paket deckt viele Zwecke ab (95 Dateien für Kampf, Inventar,
Interface). Nach Zweck zerlegt geht die Herkunft verloren, als Paket
belassen findet man nichts. Das Präfix macht jede sortierte Datei
rückverfolgbar.
Verworfen: nur nach Zweck sortieren; nur Pakete belassen; nach Lizenz
sortieren (man sucht einen Schritt-Sound, nicht „alle CC0-Dateien").

## 2026-08-14 — AudioSource.Priority gesetzt statt Voice-Limit erhöht
Was: Musik 0, Ambience 32, Schritte 100, Schafe 150, Fackeln 200.
Warum: Unity spielt nur 32 Quellen wirklich ab (`Max Real Voices`) und
virtualisiert den Rest nach Lautstärke und Priorität. Bei vielen Fackeln
fiel die leise Musik aus. Prioritäten opfern im Zweifel eine von zwanzig
Fackeln, was niemand merkt.
Verworfen: `Max Real Voices` hochsetzen — kostet Rechenzeit und behebt die
Rangfolge nicht.

## 2026-08-14 — FolderTemplate um `Audio` ergänzt
Was: `Audio\` ist ein regulärer Baustein-Unterordner neben Scripts,
Prefabs, Textures.
Warum: Klänge gehören zum Baustein (Fackelfeuer zur Fackel, Blöken zum
Schaf); nur Querschnitts-Material liegt in `Shared/Audio/`.
Verworfen: alle Klänge zentral unter `Shared/Audio/`.
