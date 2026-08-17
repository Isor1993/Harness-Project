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
**Entschieden 2026-08-12:** Es wird zweimal abgegeben. Stand 1 ist
vollständig und benotbar — als hätte es keinen zweiten Termin. Stand 2
bringt nur noch Kleinigkeiten. Frist ist der 21.08.

**Stand 2026-08-17:** Stand 1 ist hochgeladen (einen Tag später als
geplant, siehe unten). Offen für Stand 2 sind das Lernziel S3 (Herde über
den Placer) und zwei TDD-Kleinigkeiten. Danach erneut kopieren, zippen und
hochladen.

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

### Do 13.08. — Ton — ausgefallen, am Fr 14.08. nachgeholt und erledigt
Isor hatte Mi und Do keine Zeit (Isor, 2026-08-14). Entscheidung: Der
Ton-Block wurde nicht verschoben, sondern zusammen mit dem Freitagsprogramm
am 14.08. abgearbeitet. Damit bleibt Stand 1 am Sonntag vollständig und
Stand 2 frei für Kleinigkeiten.
1. [x] **Musik und Soundeffekte eingebaut** (2026-08-14) — Mixer mit drei
   Gruppen, Musik in beiden Szenen, Windböen, Fackelfeuer, Schafe,
   Spielerschritte, Antwortlaut beim Zähmen. Alle Klänge CC0, Quellen in
   `03_AssetLibrary\Extern_Frei\Audio\`. Einzelheiten im FEATURE_LOG,
   Begründungen in DECISIONS 2026-08-14, Stoff fürs TDD in TDD_NOTES.
   Offen daraus: Audio-Zeilen in Tabelle 9 (Kapitel 12) nachtragen —
   nur Quelle und Lizenz je Zeile, keine Attributionsformel nötig. `Village.unity` enthält
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
   **Optik in einem Rutsch über alle drei Menüs** (Isor, 2026-08-14):
   Hauptmenü, Pausenmenü und Options sollen wie ein System aussehen —
   gleiche Schrift, Farben und Abstände. Einzeln aufgehübschte Teile
   wirken zusammengewürfelt. Größter Einzelhebel ist die TMP-Schärfe,
   die alle Texte auf einmal betrifft.
   Offene Frage dabei: Das Options-Panel ist halbtransparent, damit im
   Pausenmenü das Dorf durchscheint. Im Hauptmenü scheint dadurch der
   blaue Hintergrund durch — entweder so lassen oder dort einen eigenen
   Hintergrund hinterlegen. Erst beim Optik-Durchgang entscheiden.
3. [x] **Menü-UI und Options** — fertig (2026-08-14 gebaut, 2026-08-15
   im Dorf zum Laufen gebracht). Ursache des Maus-Problems: Das
   Options-Panel war durch vier Umzüge (Szene → eigenes Prefab →
   VillageUI → PauseMenuRoot) intern beschädigt; eine frische Kopie aus
   dem Hauptmenü funktionierte sofort. Alles andere war ausgeschlossen —
   Raycast traf, Position stimmte, Click-Action feuerte, `timeScale`,
   Cursor, EventSystem und Doppel-Systeme ohne Befund. **Lehre: Bei
   unerklärlichem UI-Verhalten zuerst eine frische Kopie testen, bevor
   man stundenlang misst.**
   Ebenfalls erledigt: `GameController.Pause()` setzt das Menü beim
   Öffnen auf die Button-Seite zurück, damit nach ESC im Options-Fenster
   nicht wieder Options erscheint.

   Alter Stand der Beschreibung:
   Options-Panel gebaut mit vier Reglern (Gesamt, Musik, Effekte,
   Maus-Empfindlichkeit), Prozentanzeige, `GameSettings` mit
   Mixer-Anbindung und `PlayerPrefs`-Speicherung. **Im Hauptmenü läuft
   alles.** Panel liegt als Prefab in `Shared/UI/Prefabs/`.

   **OFFEN — erster Punkt am nächsten Arbeitstag:** Im Pausenmenü des
   Dorfes reagieren die Slider **nicht auf die Maus** — kein Hover, kein
   Klick, kein Ziehen. Tastaturnavigation funktioniert, Buttons lassen
   sich per Enter auslösen. Im Hauptmenü funktioniert dasselbe Prefab
   einwandfrei.

   Bereits ausgeschlossen (2026-08-14, alles gegen die Dateien geprüft):
   - `Time.timeScale = 0` — testweise entfernt, keine Änderung
   - `InGameUI` und `Fps` als Raycast-Blocker — beide deaktiviert, keine
     Änderung
   - `Raycast Target` am `PauseMenuRoot` — ausgeschaltet, keine Änderung
   - fehlender `GraphicRaycaster` — in beiden Canvas vorhanden, gleiche
     Einstellungen
   - `CanvasGroup` mit abgeschaltetem `Interactable` — existiert nirgends
   - zwei EventSystems — es gibt genau eines, korrekt konfiguriert
     (`Point`, `Left Click`, `Navigate`, `Submit` gesetzt)
   - Canvas-Unterschiede — beide Screen Space Overlay, gleicher
     CanvasScaler (1920×1080)
   - Cursor gesperrt — Mauszeiger ist im Pausenmenü sichtbar
   Noch nicht getestet: Game-View-Zoom auf 1x stellen und vorher ins
   Spielfenster klicken (Editor-Artefakt), sowie ein Test im Build.

   Ebenfalls offen: Mit ESC bei offenem Options-Fenster bleibt beim
   nächsten Öffnen Options statt der Pause-Buttons stehen. Zwei Zeilen in
   `GameController.Pause()` — Options aus, Pause-Panel an.

### Sa 15.08. — verbraucht für Punkt 3
Der ganze Samstag ging für das Options-Fenster im Dorf drauf (siehe
Punkt 3). Die unten geplanten Punkte 4 bis 10 sind **nicht** angefangen
und rutschen auf Sonntag bzw. in Stand 2.

**Lage am Sa 15.08., 22:30 — Neuplanung für den Sonntag:**
Fertig sind Ton (Punkt 1) und Menü/Options (Punkt 3). Offen sind alle
Abgabe-Pflichtteile. Sonntag reicht nur, wenn die Politur gestrichen wird.

Sonntag in dieser Reihenfolge — Pflicht zuerst:
1. Punkt 7 (Herde über den Placer, Lernziel S3) — ~1 h
2. Punkt 8 (Abgabe-Build) — ~1 h
3. Punkt 9 (Screenshots) — ~1 h
4. Punkt 10 (Video Engine-Tool) — ~1 h
5. Punkte 11–19 (TDD, READ_ME, Projektkopien, Zippen, Upload) — ~6 h

In Stand 2 (Mo–Do) verschoben, weil sie keine Bewertungskriterien sind:
Punkt 2 (In-Game-UI-Politur), Punkt 4 (Licht und Bepflanzung),
Punkt 5 (Baum-LOD), Punkt 6 (Terrain-Texturen).

### Sa 15.08. — ursprüngliche Planung (nicht abgearbeitet)
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

### So 16.08. — Ablauf nach Isors Vorgabe (2026-08-15, 22:45)
**Vormittag bis 17:00 — Politur, in dieser Reihenfolge:**
1. [x] **Hauptmenü neu gestaltet** (2026-08-16) — Design-Session mit zwei
   Varianten, entschieden wurde die zentrierte Tafel. Dorf-Screenshot als
   Hintergrund (deckt zugleich Punkt 9), Oswald Bold SDF für Titel und
   Buttons, Fackel-Palette, englische Beschriftungen. Werte und
   Begründungen in DECISIONS 2026-08-16.
2. [x] **Options-Fenster aufgehübscht** (2026-08-16) — feste Tafel statt
   Vollbild-Schleier, damit im Dorf das Dorf sichtbar bleibt. Regler in
   Ember-Füllung. Damit ist die offene ROADMAP-Frage vom 14.08. zur
   Halbtransparenz erledigt.
3. [x] **Pausenmenü auf dieselbe Tafel gebracht** (2026-08-16) — Giftgrün
   ersetzt, ein Schleier je Ebene. Einzelheiten im FEATURE_LOG.
4. [x] **In-Game-HUD gebaut** (2026-08-16) — in sieben Bausteinen:
   HUD-Root und Ausblenden beim Pausieren, Zähmzähler, Uhr, Spieler-Kartusche
   mit neuer `Health`-Komponente, Zielzustand getrennt vom Prompt, Politur
   über alles. Einzelheiten im FEATURE_LOG, Begründungen in DECISIONS.
   Zwei Anzeigen zahlen auf **S3** ein, weil sie die vorhandene Simulation
   erstmals sichtbar machen: Tageszeit und der Zustand der Schafe.
Wunschliste dafür (Isor): Tageszeit sichtbar machen, Zustandsbalken am
Schaf, ein umherlaufender Gegner der die Herde verjagt, ggf. Spielerleben.
Zwei davon zahlen auf **S3** ein („Simulation einer gewohnten Umgebung"):
die Tageszeit-Anzeige und der Gegner. Der Rest ist Feature, kein Kriterium.

**Ab 17:00 — harte Grenze, dann nur noch Abgabe:**
Build, Screenshots, Video, TDD, READ_ME, Projektkopien, Zippen, Upload.

**Zeitwarnung (2026-08-15):** Nach 17:00 bleiben etwa sieben Stunden, der
Bedarf liegt bei acht. Entschärfung: Claude legt am Vormittag parallel die
Doku-Vorarbeit vor (siehe unten), das spart rund zwei Stunden. Und die
Frist ist der 21.08. — was am Spielstand hängt (Build, Screenshots, Video,
Projektkopien) muss Sonntag fertig werden, reiner Text kann Montag folgen.

**Punkt 7 (Herde über den Placer)** bleibt drin, aber mit hartem Deckel von
einer Stunde. S3 ist ein benanntes Lernziel der Aufgabenstellung, und die
Placer-Infrastruktur steht bereits. Läuft es nach einer Stunde nicht,
abbrechen.

### Do 17.08. — Abgabe Stand 1 hochgeladen
Beide Portfolios wurden an einem Stück fertiggestellt, Aufgabe für Aufgabe
gegen die Original-Aufgabenstellungen geprüft und **am Abend des 17.08.
vollständig hochgeladen**. Damit liegt ein benotbarer Stand auf dem Server.
Begründungen in DECISIONS 2026-08-17.

Erledigt in dieser Session:
- Beide READ_ME fertig geschrieben, alle Platzhalter und Kommentarblöcke
  raus, Kriterien-Kürzel eingetragen (D004: KI Prototyp K1/K2/K3/S1,
  Simulation K3/S2/S3)
- TDD: Deckblatt korrigiert (Isor), Wortanzahl 21366, sieben Audiopakete
  in Tabelle 9, KI-Kennzeichnung unter Tabelle 1, PDF neu exportiert
- Beide `release`-Ordner mit dem Build gefüllt, beide `src` nachgezogen
  (281,8 MB, `Village.unity` 139,7 MB mit 21.354 platzierten Bäumen)
- Neue Press-Screenshots und Videos für Engine-Tool, KI Prototyp,
  Simulation und Prozedurale Erweiterung; Zweitkopien mit sprechenden
  Namen unter `01_Uni\Semester_2\Abbildungen\`
- `Messreihen_README.md` von 132 auf 33 Zeilen gekürzt, lange Fassung
  gesichert unter `Arbeitsdateien\Messungen\`
- ZIPs erzeugt und geprüft: D003 308,4 MB, D004 540,1 MB

**Offen geblieben aus der 16.08.-Liste:**
- [ ] **Balkendiagramm der sechs Messpunkte** zu Tabelle 8 einsetzen
  (Punkt 13). Neue Abbildung nur über `Verweise → Beschriftung einfügen`.
- [ ] **Zwei Sätze im Fazit** zur fehlenden `namespace`-Gliederung
  (0 von 83 Dateien) als bewusst aufgeschoben (Punkt 14).

### Offen: Lernziel S3 — generierte Bevölkerung
Beim Prüfen gegen die Aufgabenstellungen gefunden (2026-08-17). **S3 steht
in Modul 004 sowohl bei Aufgabe 2 als auch bei Aufgabe 3** und ist nicht
erfüllt: `TerrainConfig_Default.asset` enthält nur zwei Placeables
(`BirchTree_1`, `GrassSingle_x2`). Die Herde sitzt von Hand als
`SheepHerdManager_01.prefab` im `Village.prefab`; in `Village.unity` kommt
„Sheep" kein einziges Mal vor.
- [ ] Herden-Prefab als drittes Placeable eintragen, im Editor-Tool
  platzieren, Szene speichern. Kein Code nötig — das Tool erzeugt die
  Bedienzeile aus der Placeable-Liste.
  **Falle:** `RuntimePlacementSpawner` spawnt zur Laufzeit nur instanced
  Typen. GameObject-Typen wie die Herde müssen im Editor platziert und in
  der Szene gespeichert werden, sonst fehlen sie im Build.
- [ ] Danach zwingend: Kopierskript erneut, neu zippen, erneut hochladen —
  der zweite Upload ersetzt den ersten.

### Alte Punkte der 16.08.-Liste (Belege)
11. [x] **Deckblatt richtiggestellt** (Isor, 2026-08-17): Modulname auf
    „Structured Game Development", Semester auf März 2026, Modulnummer auf
    `4FSC0PD003.1`.
12. **Entfallen** — kurze Quellenliste. Ursprünglich: Bridson, Amdahl und
    Perlin werden namentlich genannt, eine knappe Liste am Dokumentende
    genügt.
    **Korrigiert am 2026-08-16 (Isor):** Keine der drei
    Aufgabenstellungen verlangt Quellenangaben, Zitierweise oder ein
    Literaturverzeichnis; die Feedbackelemente fragen nach Codequalität,
    Serialisierung, Bedienbarkeit und nachvollziehbaren Performancedaten.
    Die frühere Forderung stammte aus dem Kontext der S4-Abgabe
    („Arbeiten nach akademischen Standards"), einem eigenen Dokument.
    Das TDD ist ein technisches Dokument, keine Seminararbeit.
13./14. offen — siehe oben unter „Offen geblieben aus der 16.08.-Liste".
15. [x] **Audio-Quellen in Tabelle 9 nachgetragen** (2026-08-17): sieben
    Pakete, alle CC0. Die Herkunft wurde über die .meta-GUIDs gegen Szenen
    und Prefabs geprüft, nicht aus `Audio_Quellen.txt` übernommen — die
    Notiz war an drei Stellen falsch (siehe TDD_NOTES 2026-08-17).
16. [x] **Abschluss erledigt** (Isor, 2026-08-17): Wortanzahl 21366,
    beide Unterschriften als Bild vorhanden, F9 gelaufen, PDF neu
    exportiert und in `Abgabe_Final` gelegt. Das S4-Dokument hat Isor
    selbst überarbeitet und ebenfalls neu exportiert.
17. [x] **Beide READ_ME fertig** (2026-08-17).
18. [x] **Projektkopien nachgezogen** (2026-08-17, zweimal — zuletzt am
    Abend nach dem Platzieren der Bäume).
19. [x] **Gezippt und hochgeladen** (2026-08-17). Die Upload-Grenze war
    kein Thema. Zippen brachte mehr als erwartet, weil `Village.unity` als
    YAML-Text stark komprimiert: 1,32 GB Ordner → 848,5 MB in zwei ZIPs.

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

### Mo–Do 17.–20.08. — Stand 2
- [ ] **Do 20.08.: Ton-Block** — Inhalt siehe Punkt 1 oben. Der einzige
  große Posten in Stand 2, alles andere sind Kleinigkeiten.

Sonst keine großen Änderungen mehr. In Frage kommen:
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
- Member-Reihenfolge im `TerrainToolPresenter` sortieren — die Regel steht
  seit 2026-08-16 in CODE_GUIDELINES („Member-Reihenfolge"), das Sortieren
  selbst ist vor der Abgabe trotzdem nicht mehr nötig

### Kollision und NavMesh (Isor, 2026-08-16)
- [ ] **Schafe laufen durch Häuser und Bäume.** Es fehlen Collider, und die
  platzierten Bäume sind für das NavMesh unsichtbar. Zu klären: Collider an
  die betroffenen Prefabs, und wie die zur Laufzeit platzierten Objekte ins
  NavMesh kommen — jeder Baum als `NavMeshObstacle` wäre bei mehreren tausend
  Bäumen zu teuer, also eher NavMesh-Carving über die Platzierungsdaten oder
  ein Bake nach dem Placement. Hängt an der Frage, wie viel Welt zur Laufzeit
  entsteht (ROADMAP-Punkt 1) und braucht eine eigene Design-Session.
  Am Abgabetag bewusst nicht angefasst.

### Aus dem ersten Abgabe-Build (2026-08-16)
Der Build lief mit **null Fehlern** durch (77 s). Offen blieben Warnungen:
- [ ] **Neun Shader-Warnungen** im `GrassMesh_Shader`: `pow(f, e) will not work
  for negative f, use abs(f)`. Der Shader funktioniert; ein Eingriff im Shader
  Graph war am Abgabetag unnötiges Risiko. Fix: `abs()` vor die Potenz.
- [ ] **Eine `CS0414`-Warnung** bleibt: `SheepDodgeBehaviour._hasDrawPoint`
  wird in `OnDisable`, `Update` und `StartDodgeMovement` gesetzt, aber nur in
  `OnDrawGizmos` gelesen. Kapseln hieße fünf `#if`-Klammern in der
  Ablauflogik — beim nächsten Anfassen der Klasse sauber lösen, etwa indem
  der Zeichenzustand aus dem Agent abgeleitet statt mitgeführt wird.
  Die anderen sieben Gizmo-Felder wurden am 16.08. gekapselt.

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
10. [ ] **Ladebildschirm** (Isor, 2026-08-16, für die Woche nach der Abgabe):
   Der Szenenwechsel vom Hauptmenü ins Dorf läuft heute ohne Rückmeldung —
   das Bild steht, bis die Szene fertig ist. Gebraucht wird ein Ladebalken
   zwischen den Szenen. Passt zum bereits vorgesehenen Spielablauf
   (Terrain im Editor, alles Placement zur Laufzeit hinter einem Ladebalken)
   und wird spätestens gebraucht, wenn die Laufzeit-Platzierung des Dorfes
   den Start spürbar verlängert. Betrifft `SceneLoader`.
11. [ ] **`SheepHealth` auf die `Health`-Komponente umstellen** (Isor,
   2026-08-16): Am 16.08. wurde `Assets/Shared/Health/Health.cs` als
   allgemeine Komponente angelegt — jedes Wesen, das Leben hat, bekommt sie
   angehängt (Spieler, später Goblin und Mobs). `SheepHealth` blieb dabei
   unberührt und macht dasselbe ein zweites Mal.
   Zu tun: prüfen, was in `SheepHealth` wirklich schaf-spezifisch ist
   (`SheepSettings`, der Testschalter, `Die()` mit Graveyard und FSM), den
   Rest durch die `Health`-Komponente ersetzen und die Aufrufer nachziehen.
   Nicht vor der Abgabe gemacht, weil **`SheepHealth` im TDD beschrieben ist**
   (Isor, 2026-08-16) — ein Umbau hätte den Text falsch gemacht, und das
   Nachziehen kostet mehr als der Umbau selbst. Dazu hängt die Klasse an FSM,
   Hungersystem und Graveyard.
   Entscheidung für Komposition statt Vererbung: Isor, 2026-08-16.
12. [ ] **`HudController` und HUD-Einstellungen** (vorgemerkt 2026-08-16):
   Ein Skript auf dem `InGameUI`-Objekt, das die einzelnen HUD-Teile nach
   gespeicherten Spielereinstellungen ein- und ausblendet (FPS-Anzeige,
   Fadenkreuz, Uhr, Zähmzähler) — dazu die passenden Schalter im
   Options-Fenster, nach dem Muster von `GameSettings`.
   Abgrenzung, die dafür schon gilt (Isor, 2026-08-16): Der
   `GameController` fasst beim Pausieren **nur das Root-Objekt** an, nie
   die einzelnen Teile. Sonst würde er beim Fortsetzen Anzeigen wieder
   einschalten, die der Spieler bewusst ausgeschaltet hat. Damit ist der
   Controller später ein Aufsatz und kein Umbau.
13. [ ] **Prefab-Struktur prüfen und aufräumen** (vorgemerkt 2026-08-16):
   Beim UI-Umbau kam heraus, dass die Menü-Prefabs **verschachtelt** sind —
   `MainMenuPanel` und `OptionsPanel` liegen *innerhalb* von `MainMenuUI`.
   Folge: `Apply All` an der Szenen-Instanz schreibt alles ins äußere
   Prefab (`MainMenuUI.prefab` wuchs von 595 auf 1924 Zeilen), die inneren
   Vorlagen bleiben leer, und das Dorf zeigt weiter den alten Stand. An die
   inneren kommt man nur über den Prefab-Modus des äußeren.
   Zu klären: welche Prefabs überhaupt verschachtelt sein sollen, wo
   Instanzen umbenannt wurden (`OptionsPanel2` im Dorf ist dieselbe
   Vorlage wie `OptionsPanel`), und ob angesammelte Overrides zurück in
   die Vorlagen gehören. Betrifft alle Prefabs, nicht nur die UI —
   Isor will jedes einzelne einmal durchgehen und prüfen, ob es sinnvoll
   geschnitten ist. Gehört thematisch zu Punkt 7 (Aufbau-Konvention).
14. [ ] **Studien-Aufbau der Abgabe wiederverwenden:** Die Vorlage unter
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
