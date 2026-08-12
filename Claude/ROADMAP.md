# ROADMAP.md — Baureihenfolge

Ownership: Nur Baureihenfolge. Was fertig ist, steht im FEATURE_LOG.md,
Begründungen in DECISIONS.md, Design-Absicht in GDD.md — nie hier.

## Grobziel
Generischer Harness für Game-Dev-Projekte und Brainstorm-/Learn-Sessions:
.md-Dateien als Gedächtnis, Sessions als Wegwerf-Arbeitsräume. Wird hier
entwickelt und getestet, später pro Projekt (Isor's Tower) kopiert und
spezialisiert.

## Nahziel (Stand 2026-08-12)
Zwei Phasen, klar getrennt:
1. **Bis zur Uni-Abgabe (Frist 2026-08-21):** Das Uni-Projekt zu Ende
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
  (2026-08-05) — Gras-Rebuild 122,7 s → 12,4 s (−89,9 %). Einzelheiten im
  FEATURE_LOG.md, Stoff fürs TDD in TDD_NOTES.md
- [x] Gras-Rendering und Verteilung finalisiert (2026-08-04/05):
  GPU-Instancing, Gras-LOD (507 Mio → ~12 Mio Dreiecke, 4,5 → ~87 FPS),
  Weltgröße bleibt 2048 m bei HeightMultiplier 700, Kontrastkurve in
  `NoiseMaskDensity`, Blocker über `PlacementExclusion`
- [x] Neun Diagramme erzeugt und angeordnet (2026-08-08 bis 2026-08-11) —
  Terrain-Pipeline, Platzierung, Gras-Rendering, Editor-Tool,
  DayNightSystem, Sheep-FSM, Sheep-Komponenten, Ablauf Generate Complete,
  Zustand Sheep-FSM. Skripte unter `05_Werkzeuge\Vorlagen\`, Quellen unter
  `01_Uni\Semester_2\Diagramme_Quellen\`. Regeln in DIAGRAM_RULES.md
- [x] Session-Typ „Zeugnis" gebaut (2026-08-11): vierter Typ in
  WORKFLOW.md, Regeln in ASSESSMENT_RULES.md, Zeugnisse in
  ASSESSMENT_LOG.md, Auslöser `/zeugnis`; erstes Zeugnis am selben Tag.
  Begründungen in DECISIONS 2026-08-11
- [x] Artifact-Seiten nach den drei Typen sortiert (2026-08-05 bis
  2026-08-08): zehn Seiten mit Symbol, Kind-Badge und Favicon. Regeln in
  ARTIFACT_RULES.md
- [x] **TDD inhaltlich fertig** (2026-08-11): Kapitel 1 bis 8, 12, 13, 14
  durch, 149.948 Zeichen, alle Zahlen gegen Code und Rohlogs geprüft.
  Verlauf und Einzelheiten im FEATURE_LOG.md, Begründungen in DECISIONS.
  S4-Abgabe („Arbeiten nach akademischen Standards") neu erstellt.
- [x] **TDD-Layout** (Isor, 2026-08-11): Abschnittsumbruch und
  Seitennummerierung, Seitenumbrüche, Zeilenabstände, Verzeichnisse
  erzeugt, Strg+A / F9 durchgelaufen
- [x] **Abgabe-Ordnerstruktur gebaut und befüllt** (2026-08-12):
  `01_Uni\Semester_2\Abgabe_Final\` nach SAE-Vorgabe, Vorlage für kommende
  Semester unter `05_Werkzeuge\Vorlagen\SAE_Abgabe_Struktur\`, Kopierskript
  `05_Werkzeuge\Abgabe_Projektkopie.ps1`. Beide Projektkopien, alle
  Diagramme, Videos, Bilder, Logs und PDFs liegen drin. Restliste in
  `01_Uni\Semester_2\Arbeitsdateien\Abgabe_Packliste.txt`

## Als Nächstes — Abgabe in zwei Ständen
**Entschieden 2026-08-12:** Es wird zweimal abgegeben. **Stand 1 am
Sonntag 16.08.** ist vollständig und benotbar — als hätte es keinen
zweiten Termin. **Stand 2 am Mi/Do 19./20.08.** bringt nur noch
Kleinigkeiten. Frist ist der 21.08.

Grund: Ein vollständiger früher Stand nimmt das Risiko aus der Woche.
Was am Sonntag steht, kann nicht mehr schiefgehen.

**Zeitbudget:** Mi 4 h, Do 4 h, Fr bis So zusammen rund 17 h — gut 25 h.
Der Bedarf unten liegt bei 15 bis 18 h. Der Puffer ist Absicht.

**Reihenfolge nach Isors Vorgabe (2026-08-12):** Zuerst das, was das
Spiel lebendig macht — Ton, UI, Licht, Bepflanzung. Die Dokumentation
kommt bewusst zuletzt an einem Stück (Sonntag), weil bis dahin noch
Dinge dazukommen, die im Text stehen müssen. Ein früher Textstand wäre
doppelte Arbeit. Das Dokument ist ohnehin schon einmal zum Feedback
eingereicht.

### Mi 12.08. — entfällt
Planungssession. Isor geht früher schlafen, um Donnerstag mit voller
Energie zu starten — bewusste Entscheidung, kein Verzug: die tragenden
Tage sind Fr bis So.

### Do 13.08. — Ton (4 h)
1. [ ] **Musik und Soundeffekte einbauen.** `Village.unity` enthält
   derzeit **null AudioSource und null AudioListener** — es gibt keinen
   Ton. Größter einzelner Eindrucks-Hebel und ein abgeschlossener Block,
   der in einen 4-Stunden-Abend passt. Reihenfolge: Listener am Spieler
   prüfen, Umgebungsmusik, dann Einzeleffekte (Schritte, Fackel, Schafe,
   Interaktion).
   Lizenzen: Die Quellen kommen als **Zeilen in die Asset-Tabelle
   (Tabelle 9, Kapitel 12)** — kurze Nennung mit Quelle und Lizenz, kein
   eigenes Unterkapitel (Isor 2026-08-12: sonst doppelt sich der Text).
   Beim Herunterladen gleich Quelle und Lizenz mitnotieren, sonst muss
   das am Sonntag rekonstruiert werden.

### Fr 14.08. — UI (langer Block)
2. [ ] **In-Game-UI aufwerten:** Fadenkreuz kontextsensitiv auf
   Interactable, Prompt-Stil (Box, Fade, Tastensymbol), HUD beim
   Pausieren ausblenden, TMP-Font-Schärfe (Texte sind pixelig).
3. [ ] **Menü-UI und Options:** Pause über HUD sortieren, Maus-/
   Tastatur-Moduswechsel, Options-Fenster mit **Lautstärkeregler**
   (hängt an Punkt 1).

### Sa 15.08. — Welt beleben, dann Abgabe-Material
4. [ ] **Licht und Bepflanzung:** Fackeln setzen, Glühwürmchen setzen,
   mehrere Herden verteilen.
5. [ ] **Baum-LOD nachziehen** — die Stufen kommen aus Blender mit, die
   Umschaltabstände passen nicht.
6. [ ] **Terrain-Texturen ansehen** — Umfang bewusst offen, erst schauen
   was mit wenig Aufwand deutlich besser aussieht.
7. [ ] **Mindestens eine Herde über den Placer** statt von Hand (~1 h).
   Lernziel **S3** („generierte Bevölkerung") und damit ein
   Bewertungskriterium, kein Polish — kleinster Punkt des Tages mit der
   größten Notenwirkung. Optional daneben ein einfacher Feind (Goblin)
   über denselben Weg.
8. [ ] **Abgabe-Build erstellen und durchspielen** (~1 h): kein
   Development Build. Kommt in beide `release`-Ordner. Die Funktionalität
   wird laut Vorgabe am Build bewertet.
9. [ ] **Screenshots** (~1 h): drei je Projektordner, ab 1024x768,
   `Press1.png`, `Press2.png`, `Press3.png`. Betrifft Engine-Tool, KI
   Prototyp, Simulation, Prozedurale Erweiterung. Die vorhandenen Bilder
   sind Shader-Graphen aus dem TDD, keine Spielbilder.
10. [ ] **Video für Engine-Tool-Entwicklung** (~1 h): 30 bis 90 Sekunden.
    Der einzige Projektordner ohne Video.

### So 16.08. — Dokumentation und Abgabe (Stand 1)
Alles am TDD an einem Stück, weil der Text erst dann den fertigen Stand
beschreibt. Claude legt bis Samstagabend vor (siehe unten), sodass hier
nur noch eingesetzt und geprüft wird.
11. [ ] **Deckblatt richtigstellen** (~15 min): steht auf `Semester:
    März 2025` und `Modulname: Game Development Basics` — beides falsch.
    Richtig: laufendes Studienjahr und „Structured Game Development"
    (ASSIGNMENT_TOOL, Modul 4FSC0PD003.1). Vorher gegen Canvas prüfen.
12. [ ] **Quellenangaben in 6.3 und 6.5 + Literaturverzeichnis** (~2 h):
    Bridson, Amdahl und Perlin werden namentlich genannt, aber nicht
    belegt; ein Literaturverzeichnis existiert bisher nicht. Belegtechnik
    aus dem S4-Text übernehmen.
13. [ ] **Balkendiagramm der sechs Messpunkte** zu Tabelle 8 einsetzen.
    Neue Abbildung nur über `Verweise → Beschriftung einfügen`.
14. [ ] **Zwei Sätze im Fazit** zur fehlenden `namespace`-Gliederung
    (0 von 83 Dateien) als bewusst aufgeschoben.
15. [ ] **Audio-Quellen in Tabelle 9 nachtragen** — knapp, Quelle und
    Lizenz je Zeile, kein eigenes Unterkapitel.
16. [ ] **Abschluss** (~40 min): Wortanzahl auf der Titelseite
    eintragen, Unterschrift auf beiden Erklärungen prüfen, Strg+A / F9,
    beide PDFs exportieren und die Fassungen in `Abgabe_Final`
    überschreiben.
17. [ ] **Beide READ_ME fertig schreiben** (~1 h): Platzhalter ersetzen,
    Kriterien-Kürzel für KI Prototyp und Simulation aus der
    Aufgabenstellung nachtragen, Kommentarblöcke entfernen, leer
    gebliebene Ordner löschen.
18. [ ] **Projektkopien nachziehen** (~5 min): `powershell -File
    "C:\IsorBackup\05_Werkzeuge\Abgabe_Projektkopie.ps1"`. Zwingend, bevor
    gezippt wird — die Kopien in `Abgabe_Final` sind sonst der Stand vom
    12.08. und enthalten weder Ton noch UI noch die Beleuchtung vom
    Wochenende. Das Skript spiegelt, also werden auch gelöschte und
    verschobene Dateien nachgezogen.
19. [ ] **Zippen und hochladen** (~30 min): eine ZIP je Portfolio. Vorher
    die Upload-Grenze auf Canvas prüfen — 619 MB gesamt, davon 2 × 198 MB
    Projektkopie und rund 204 MB Videos. Wenn es klemmt, sind die Videos
    der Hebel: die Vorgabe verlangt nur *ein* Video je Projektordner.

### Was Claude bis Samstagabend vorlegt (kostet Isor keine Zeit)
Damit der Sonntag nicht überläuft, liegt vorbereitet bereit:
- [ ] Balkendiagramm der sechs Messpunkte als fertige Bilddatei
- [ ] Quellenangaben für Bridson, Amdahl und Perlin, formatiert nach der
  Belegtechnik des S4-Texts, plus die Einträge fürs Literaturverzeichnis
- [ ] Formulierungsvorschlag für die zwei Fazit-Sätze
- [ ] Beide READ_ME so weit gefüllt, wie es ohne den fertigen Stand geht

### Geprüft am 2026-08-12 — Village-Altlasten
- `Village.unity` enthält **null Kamera-Komponenten** direkt in der
  Szene. Die Notiz „zwei aktive Kameras" vom 2026-08-02 ist erledigt.
- NavMesh-Bake ist auf dem aktuellen Aufbau, `Environment/Village/` hat
  genau ein Prefab, `Environment/Terrain/` nur Texturen (Isor).
- Die zwei Dateien unter `Environment/Torch/Prefab/` (`Torch .prefab` und
  `Torch.prefab`) sind **Absicht** — zwei Fackeln mit unterschiedlichen
  Einstellungen (Isor, 2026-08-12). Keine Dublette, nichts zu tun.
  Die frühere Notiz „Dubletten-Prefab" vom 2026-08-02 war ein Fehlschluss.

Damit sind alle drei Village-Altlasten aus der Notiz vom 2026-08-02
erledigt oder als Absicht geklärt.

### Nicht mehr geplant
Das Village-Prefab neu aufbauen (früherer Punkt 1b). Der bestehende
Aufbau trägt; die Zeit geht stattdessen in Ton, UI und Beleuchtung —
das ist am Bildschirm sichtbar, ein umgebautes Prefab nicht.

### Mo–Do 17.–20.08. — Stand 2, nur Kleinigkeiten
Keine großen Änderungen mehr. In Frage kommen:
- [ ] Politur aus Punkt „Restliste" unten, soweit sie abends passt
- [ ] Falls es Rückmeldungen zur formativen Abgabe gab: zwei Zeilen im
  Änderungsverlauf, was zurückkam und was geändert wurde (Feedbackelement
  *Person* in beiden Aufgabenstellungen)
- [ ] Was beim Durchspielen am Sonntag auffiel
- [ ] Die beiden Fackel-Prefabs sprechend umbenennen (heute `Torch .prefab`
  und `Torch.prefab`, Unterschied nur ein Leerzeichen). Die eine brennt
  ruhig, die andere aggressiver mit mehr Funken (Isor, 2026-08-12).
  Vorschlag: `Torch_Calm` und `Torch_Blazing` — oder die Bezeichner des
  `TorchMode`-Enums, falls die beiden dort schon Werte haben.
  Passiert im Unity-Editor, wenn ohnehin an den Fackeln gearbeitet wird.

### Bewusst nicht mehr vor der Abgabe
- Kapitel 9/10 (Shader/VFX) von Screenshots auf erklärenden Text umbauen
- `namespace`-Umbau über die 83 Dateien
- `ObjectPlacer.PlaceType` zerlegen — die Methode ist das Messobjekt der
  Threading-Abgabe, ein Umbau entwertet die Messreihe
- Schafe schlagbar machen (war ROADMAP 1a): Feature, kein Bewertungspunkt
- Member-Reihenfolge im `TerrainToolPresenter` sortieren — dazu fehlt die
  Regel in CODE_GUIDELINES, sonst ist es Gefühl statt Maßstab

### Restliste Politur (nur wenn Zeit bleibt)
Aus der Interaktions-Session (2026-08-02): TMP-Font-Schärfe (Texte
pixelig); Fadenkreuz aufwerten + kontextsensitiv; Prompt-UI-Stil
(Box/Fade, Tastensymbol); HUD beim Pausieren ausblenden; Menü-Sortierung
(Pause über HUD) + Maus/Tastatur-Moduswechsel; Sun Source explizit
setzen; Kamera-Far-Plane an die finale Weltgröße koppeln (Mond-Culling);
Raycast-Target-Hygiene bei UI-Bildern.
Aus den Gras-Sessions (2026-08-04/05): Lichtblitz/Specular-Highlight auf
dem Terrain (Material-Smoothness bzw. Bloom prüfen); `SheepSense.Update`
auf `OverlapSphereNonAlloc` (2 KB GC je Frame); Herden-Placeable tunen
(Höhenband, MaxSlope, ShoreMargin); Lightmap-Warnung des generierten
Terrains (Mesh hat keine UVs — Contribute GI ausschalten).
Beim TDD-Schreiben gefunden (Isor, 2026-08-08): Magic Numbers im
`MeshBuilder` benennen — `INDICES_PER_QUAD = 6`, `PADDING_RING = 1`,
`NEIGHBOUR_SPAN = 2f`. Rein mechanisch. Isors Maßstab: keine Zahl im
Code, deren Bedeutung er im Prüfungsgespräch erst herleiten muss.
Fehlender Ton und fehlendes Menü sind der größte sichtbare Mangel
(Zeugnis 2026-08-11) — aber vor der Abgabe nicht mehr realistisch.

### Arbeitsregeln, die weiter gelten
- **Arbeitsdatei TDD:** `01_Uni\Semester_2\Arbeitsdateien\TDD
  Softwareplanung.docx` — nur diese anfassen. Sicherungen unter
  `Arbeitsdateien\Sicherung\`. Regeln in DOCX_RULES.md.
- **Arbeitsteilung am Text** (Isor, 2026-08-08): Korrekturen an
  bestehendem Text schreibt Claude direkt in die Datei. Neue Fachkapitel
  formuliert Isor selbst, Claude liefert Struktur, geprüfte Fakten und
  Zahlen und glättet hinterher. Grund: Der Text soll von ihm kommen, und
  das Durchgehen ist zugleich das Lernen des Stoffs.
- **Word-Felder:** Beschriftungen und Verweise sind Felder — neue
  Abbildungen nur über `Verweise → Beschriftung einfügen`.
- **Prefab-Painter** wird im TDD nicht erwähnt (Isor, 2026-08-07), bleibt
  aber in der Projektkopie (2026-08-11).
- **Unity-Version:** Das Projekt läuft auf `6000.5.2f1` und weicht damit
  von den beiden in der Vorgabe genannten Versionen ab. Die Dozentin hat
  persönlich freigegeben, dass eine eigene Version gewählt werden darf
  (Isor, 2026-08-12). Kein Handlungsbedarf — hier notiert, falls die
  Abweichung später jemandem auffällt.
- **Abgabe-Restliste:** `01_Uni\Semester_2\Arbeitsdateien\
  Abgabe_Packliste.txt` — dort steht, was in welchem Ordner liegt und was
  noch fehlt. Diese ROADMAP sagt *wann*, die Packliste sagt *was wohin*.

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
   vorgezogen; hier bleiben LOD, Entfernungs-Ausblendung und Culling je
   Halm via `BatchRendererGroup`.
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
8. [ ] **Gras-Rendering aus `Systems/TerrainGenerator/` herauslösen:**
   eigener System-Ordner (Umzug im Unity-Editor, macht Isor manuell —
   .meta-GUIDs); dabei LOD-Fade zwischen den Stufen und Laufzeit-Spawn
   der Herden (statt Prefab-Verdrahtung; löst auch das Aufsetzen aufs
   Gelände) mitdenken.
9. [ ] **Repo- und GitHub-System neu ordnen (eigene Design-Session):** Die Repos
   wachsen stark, weil Texturen und andere Binärdateien mitversioniert werden —
   Git legt jede Fassung vollständig ab, Binärdateien lassen sich nicht
   deltakomprimieren, und gelöschte Dateien bleiben in der Historie. Zu klären:
   was gehört überhaupt ins Repo und was in die Asset-Library unter
   `C:\IsorBackup\03_AssetLibrary\`, ob Git LFS eingesetzt wird, wie `.gitignore`
   je Repo aussehen muss, und wie mit der bereits gewachsenen Historie umgegangen
   wird. Betrifft alle drei Repos. Erst nach der vollständigen Uni-Abgabe
   (vorgemerkt 2026-08-06).
10. [ ] **Studien-Aufbau der Abgabe wiederverwenden:** Die Vorlage unter
   `05_Werkzeuge\Vorlagen\SAE_Abgabe_Struktur\` beim nächsten Semester
   gleich zu Beginn kopieren, statt am Ende zu sortieren.

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
