# ROADMAP.md — Baureihenfolge

Ownership: Nur Baureihenfolge. Was fertig ist, steht im FEATURE_LOG.md,
Begründungen in DECISIONS.md, Design-Absicht in GDD.md — nie hier.

## Grobziel
Generischer Harness für Game-Dev-Projekte und Brainstorm-/Learn-Sessions:
.md-Dateien als Gedächtnis, Sessions als Wegwerf-Arbeitsräume. Wird hier
entwickelt und getestet, später pro Projekt (Isor's Tower) kopiert und
spezialisiert.

## Nahziel (Stand 2026-07-29)
Zwei Phasen, klar getrennt:
1. **Bis zur Uni-Abgabe (Portfolio 2026-08-21):** Das Uni-Projekt zu Ende
   bringen — abgabefähig und benotbar. Keine Umbauten Richtung GDD.
2. **Nach der Abgabe:** Das Bestehende am GDD.md ausrichten und den
   Basiszustand herstellen, auf dem die kommenden Semester aufbauen.
Am Harness wird bis zur Abgabe nur ausgearbeitet, was der Betrieb
verlangt; danach wird er wieder aktiv ausgebaut.

## Erledigt
- [x] Kern: INDEX.md, ROADMAP.md, CLAUDE.md (minimal), Übergabetest
  (2026-07-14)
- [x] WORKFLOW.md: Grundregeln + alle vier Session-Typen (2026-07-17)
- [x] Knowledge-System: externer Ordner `C:\Repos Isor\Knowledge\` +
  KNOWLEDGE_RULES.md (2026-07-17)
- [x] FEATURE_LOG.md + DECISIONS.md angelegt (2026-07-17)
- [x] CODE_GUIDELINES.md als Rohmaterial: Uni-Conventions + gefilterte
  Dozenten-Rules, Zwei-Block-Struktur (2026-07-17)
- [x] Uni-Terrain-Pipeline bis einschließlich Platzierungs-Stufe
  (2026-07-18 bis 2026-07-26) — Einzelheiten im FEATURE_LOG.md
- [x] GDD.md als Short GDD: Design-Absicht Isor's Tower, Maßstab für die
  Phase nach der Abgabe (2026-07-29)
- [x] Gras-Instancing + LOD + PlacementExclusion + Prefab-Painter
  (2026-08-03 bis 2026-08-05) — Einzelheiten im FEATURE_LOG.md
- [x] Threadoptimierung inkl. Messreihe und Laufzeit-Placement
  (2026-08-05) — Einzelheiten im FEATURE_LOG.md

## Als Nächstes — bis zur Uni-Abgabe (2026-08-21)
1. [ ] **Village spielbar aufbauen.** Zerfällt in zwei Hälften, die
   *nicht* zusammenhängen — die zweite hängt an Punkt 2.
   **1a — sofort machbar (unabhängig von Weltgröße und Terrain):**
   - [x] Interaktionssystem in Betrieb (Layer `Interactable`,
     `PlayerInteractor` + `InteractionPromptView` + Prompt-UI verdrahtet) —
     2026-08-02, Einzelheiten im FEATURE_LOG.md
   - [x] Fackel: `Torch` + `TorchInteractable` (+ `TorchMode`-Enum) — 2026-08-02
   - [x] Prompt-Vergleich im Interactor erweitert (Ziel + Prompt) — 2026-08-02
   - [x] Schafe ins Village bringen und zähmbar machen — 2026-08-03,
     Einzelheiten im FEATURE_LOG.md
   - [ ] Schafe schlagbar machen (entschieden 2026-08-03, erweitert die
     „kein Kampf"-Linie aus DECISIONS 2026-07-30 um genau einen Schlag):
     Attack-Action im Input + Raycast auf `IDamageable` (baugleich zu
     `PlayerInteractor.FindTarget`), `DamageType.Physical` bekommt damit
     seinen ersten Nutzer. Mitzufixen: `Sheep.HandleDamage` flieht nur bei
     `Sense.CurrentThreat != null` — der Spieler liegt auf Layer `Player`,
     ein Treffer würde sonst Schaden machen, ohne dass das Schaf wegläuft.
   - [x] Prefab-Pinsel gebaut (2026-08-03, `Systems/PrefabPainter/`) —
     Hilfstool, nicht Abgabe-Umfang; Einzelheiten im FEATURE_LOG.md
   - [x] Placer spart Bebautes aus — gelöst über `PlacementExclusion`
     (Komponente am Objekt statt Plateau-Prüfung im Placer, 2026-08-05,
     DECISIONS 2026-08-05); wirkt auf beiden Spawn-Wegen
   **1b — erst nach Punkt 2, weil jede Terrain-Änderung die NavMesh-Bake
   wegwirft:**
   - `Village`-Prefab aufbauen: Häuser (Asset oder Primitive — **offen**),
     Props, Interactables; auf dem Plateau platzieren
   - `Navigation`-Objekt mit NavMeshSurface neben dem Tool-Ast, backen
   - NPCs: Herde handgesetzt im Prefab, Goblins per Placer im Umland
   - Bestehendes prüfen: zwei aktive Kameras in `Village.unity`,
     Dubletten-Prefab `Torch .prefab`, Birken-Material am Fackel-Mesh
2. [x] **Gras-Rendering und Verteilung finalisiert** (2026-08-04/05,
   Einzelheiten im FEATURE_LOG.md, Begründungen in DECISIONS 2026-08-04/05):
   - [x] GPU-Instancing gebaut — Pipeline `PlaceableRenderMode` →
     `GrassCellBuilder`/`GrassCell` → `InstancedRenderer`, Verzweigung in
     `SpawnType`; damit existiert zur Laufzeit das Messobjekt für Punkt 4
   - [x] Gras-LOD statt „schön ODER schnell": `GrassRenderProfile` am
     Prefab + `GrassLodSelector` je Zelle; Low-Büschel handgebaut —
     507 Mio → ~12 Mio Dreiecke, 4,5 → ~87 FPS
   - [x] Weltgröße bleibt 2048 m, HeightMultiplier 700 (2026-08-05);
     bei Problemen dann neu bewerten
   - [x] Verteilung ungleichmäßig: Kontrastkurve in `NoiseMaskDensity`
   - [x] Blocker-Bedarf gelöst über `PlacementExclusion` (siehe 1a)
3. [ ] **Schriftliche Abgaben:** TDD aus TDD_NOTES.md generieren, plus
   UML-Klassendiagramm und Ablaufdiagramm fürs Tool (Pflicht laut
   ASSIGNMENT_TOOL); akademische Aufgabe — eine zusätzliche Quelle.
   Baseline-Messung ist mit Punkt 4 erledigt (2026-08-05).
4. [x] **Uni: Threadoptimierung** (K2, K3, S3; formativ 2026-08-07) —
   Code und Messreihe fertig (2026-08-05): Gras-Rebuild 122,7 s → 12,4 s
   (−89,9 %) über vier dokumentierte Zwischenstände, Builds und Logs unter
   `C:\Repos Isor\Builds\` mit eigener README. Einzelheiten im FEATURE_LOG,
   Begründungen in DECISIONS, Stoff fürs TDD in TDD_NOTES (alle 2026-08-05).
   Die Annahme „Bridson bleibt sequenziell" hat sich als halb richtig
   erwiesen: innerhalb einer Kachel ja, über Kacheln hinweg nein.
   **Offen:** der TDD-Text selbst (gehört zu Punkt 3).
5. [ ] **Politur mit der Restzeit:** Audio, Post Processing / Volume,
   Menü, Tool-Layout — alles, was die Note hebt. Vorgemerkt aus der
   Interaktions-Session (2026-08-02): TMP-Font-Schärfe (Texte pixelig);
   Fadenkreuz aufwerten + kontextsensitiv (reagiert auf Interactable);
   Prompt-UI-Stil (Box/Fade, Tastensymbol); HUD beim Pausieren ausblenden;
   Menü-Sortierung (Pause über HUD) + Maus/Tastatur-Moduswechsel; Sun Source
   explizit setzen; Kamera-Far-Plane an die finale Weltgröße koppeln
   (Mond-Culling); Raycast-Target-Hygiene bei UI-Bildern. Neu vorgemerkt
   aus den Gras-Sessions (2026-08-04/05): Lichtblitz/Specular-Highlight
   auf dem Terrain (Material-Smoothness bzw. Bloom prüfen);
   `SheepSense.Update` auf `OverlapSphereNonAlloc` (2 KB GC je Frame);
   Herden-Placeable tunen (Höhenband, MaxSlope, ShoreMargin) und
   Boden-Aufsetzen nach dem NavMesh-Bake prüfen; Lightmap-Warnung des
   generierten Terrains (Mesh hat keine UVs — Contribute GI ausschalten).
6. [ ] **Gesamt-Review vor der Abgabe:** Bugs, halbfertige Stellen,
   Testen, Feedback einholen und umsetzen.

## Nach der Uni-Abgabe — Basiszustand für Isor's Tower
Reihenfolge noch offen, wird in einer eigenen Design-Session festgelegt.
1. [ ] **Ausrichtung am GDD:** Pipeline runtime-fähig machen (Editor-Tool
   und Laufzeit als zwei Aufrufer derselben Stufen); Welt-Wahrheit als
   Seed statt Szene festziehen; Village als festes Grundmesh mit
   Placement-Befüllung darauf; Zellen-Struktur, damit ein wachsendes
   Village später streamen kann.
2. [ ] **Platzierungs-Algorithmen neu bewerten:** zellen-lokales Poisson
   ist mit der Kachelung erledigt (2026-08-05); offen bleibt, ob Bridson
   für Gras überhaupt das richtige Verfahren ist (Jitter-Grid wäre ein
   Bruchteil der Arbeit, zeigt aber Raster — für Bäume ungeeignet).
   Ebenfalls offen aus der Threading-Session: Bucketing des Zellenbaus in
   die Kachelschleife ziehen (die Punkte liegen dort schon nach Kachel
   sortiert), Exclusion als Broad Phase je Kachel statt über alle Punkte,
   und der Aufräumpass für die Kachelränder.
3. [ ] **Massen-Bepflanzung als eigenes System:** LOD, Culling und
   Instancing zusammen — welche Objekte überhaupt gezeichnet werden.
   Großprojekt, eigene Design-Session. Das Instancing selbst ist
   vorgezogen (Punkt 2 vor der Abgabe); hier bleiben LOD,
   Entfernungs-Ausblendung und Culling je Halm via `BatchRendererGroup`.
4. [ ] **Save-System:** Weltzustand als Änderungsliste gegenüber dem
   Ausgangszustand (deckt zugleich den späteren Multiplayer-Sync ab).
5. [ ] **Harness wieder ausbauen:** Review der Regeln nach dem
   Praxisbetrieb, DOC_RULES.md, GDD_RULES.md, GLOSSARY.md, CLAUDE.md
   voll ausarbeiten.
   - Dabei **alle .md-Dateien einmal komplett durchgehen**: Doppelungen
     zwischen Dateien finden, überholte Einträge kürzen, Ownership-Grenzen
     prüfen. DECISIONS.md ist auf über 650 Zeilen gewachsen (vorgemerkt
     2026-08-03).
6. [ ] **Spiel-Features aufbauen:** Kampf, Loot, Inventar, Crafting,
   Quests — jeweils eigene Design-Sessions.
7. [ ] **GameObject-/Prefab-Aufbau-Konvention (eigene Design-Session):**
   einheitliches Schema, wie ein Objekt *innen* aufgebaut ist — Root,
   Visual/Mesh-Kind, VFX-Kind, Collider, Logik-Komponenten. Aktuell
   durchgewürfelt (z. B. Torch: Root → Kind „Torch" (Mesh) + Kind „Torch Fire"
   (VFX)); ein festes Muster für alle Objekte fehlt. Ergänzt die
   Ordnerstruktur-Regeln in CODE_GUIDELINES um die Innen-Struktur der Prefabs.
   Idealerweise *vor* dem Bau vieler Village-Prefabs (1b) — Aufwand gegen
   Abgabe-Zeit abwägen.
8. [ ] **Gras-Rendering aus `Systems/TerrainGenerator/` herauslösen:**
   eigener System-Ordner (Umzug im Unity-Editor, macht Isor manuell —
   .meta-GUIDs); dabei LOD-Fade zwischen den Stufen und Laufzeit-Spawn
   der Herden (statt Prefab-Verdrahtung; löst auch das Aufsetzen aufs
   Gelände) mitdenken.

## Später (nur bei Bedarf)
- Knowledge-Archivierung automatisieren
- ClaudeSetup-artiges Editor-Setup-Script — erst wenn Isor sicher
  programmiert (Lernphase: Isor tippt selbst)
- Harness-Dokumente auf Englisch umstellen — prüfen, ob das in der
  Praxis besser funktioniert (Unterhaltung darf deutsch bleiben)
- Development-Session „automatisierter Modus" (Claude baut, Isor
  reviewt) — erst nach der Lernphase
- Kür fürs Uni-Terrain: echte Flüsse (Spline-Mesh), Insel via
  Falloff-Map, höhen-/steigungsabhängige Texturierung
- Multiplayer (Koop 4–5) — sehr spät, siehe GDD.md
