# ROADMAP.md — Baureihenfolge Isor's Tower

Ownership: Nur was am Projekt als Nächstes gebaut wird. Was gerade dran
ist, steht in `PLAN.md`; was fertig ist, in `LOG.md`; warum es so
entschieden wurde, in `DECISIONS/`; was das Spiel sein soll, in `GDD.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`
Reihenfolge innerhalb eines Abschnitts ist noch nicht festgelegt; das
geschieht in einer eigenen Design-Session.

## Basiszustand nach der Abgabe

- [ ] **Ausrichtung am GDD.** Pipeline runtime-fähig machen (Editor-Tool
  und Laufzeit als zwei Aufrufer derselben Stufen); Welt-Wahrheit als
  Seed statt Szene festziehen; Village als festes Grundmesh mit
  Placement-Befüllung darauf; Zellen-Struktur, damit ein wachsendes
  Village später streamen kann.
  Hängt an der offenen Design-Frage im `GDD.md` → „Wird das
  Village-Terrain handgebaut, mit einem Tool erweitert, oder einmalig
  generiert und eingefroren?"
- [ ] **Platzierungs-Algorithmen neu bewerten.** Zellen-lokales Poisson
  ist mit der Kachelung erledigt; offen bleibt, ob Bridson für Gras das
  richtige Verfahren ist (Jitter-Grid wäre ein Bruchteil der Arbeit,
  zeigt aber Raster — für Bäume ungeeignet). Ebenfalls offen: Bucketing
  des Zellenbaus in die Kachelschleife ziehen, Exclusion als Broad Phase
  je Kachel, Aufräumpass für die Kachelränder.
- [ ] **Massen-Bepflanzung als eigenes System.** LOD, Culling und
  Instancing zusammen. Das Instancing ist vorgezogen; hier bleiben LOD,
  Entfernungs-Ausblendung und Culling je Halm via `BatchRendererGroup`.
  Großprojekt, eigene Design-Session.
- [ ] **Gras-Rendering aus `Systems/TerrainGenerator/` herauslösen** —
  eigener System-Ordner (Umzug im Unity-Editor wegen der .meta-GUIDs).
  Dabei LOD-Fade zwischen den Stufen und Laufzeit-Spawn der Herden
  mitdenken (löst auch das Aufsetzen aufs Gelände).
- [ ] **Save-System.** Weltzustand als Änderungsliste gegenüber dem
  Ausgangszustand — deckt zugleich den späteren Multiplayer-Sync ab.
- [ ] **Spiel-Features aufbauen:** Kampf, Loot, Inventar, Crafting,
  Quests — jeweils eigene Design-Sessions.

## Aufräumen und Konventionen

- [ ] **Wasserspiegel bekommt keinen Collider — entscheiden, ob das so
  bleibt.** Der Spieler läuft heute in den See und weiter auf dem Grund.
  Offene Frage aus `DECISIONS/Terrain_Mesh.md` → „Welt-Begrenzung gehört
  ins Terrain-Tool" (2026-08-19); dort steht die Begründung, hier nur die
  Aufgabe.
- [ ] **Ordnerstruktur im Unity-Projekt gegen die Vorlage prüfen.**
  Maßstab ist `05_Werkzeuge\Vorlagen\Unity_Ordnerstruktur`. Zwischendurch
  mitziehen, nicht erst ganz am Schluss — sonst wird daraus ein eigener
  Arbeitstag. Übernommen aus dem README des Datenbaums (2026-08-22);
  die Aufgabe betrifft das Projekt, nicht den Datenbaum.
- [ ] **GameObject-/Prefab-Aufbau-Konvention** (eigene Design-Session).
  Einheitliches Schema, wie ein Objekt *innen* aufgebaut ist: Root,
  Visual/Mesh-Kind, VFX-Kind, Collider, Logik-Komponenten. Aktuell
  durchgewürfelt. Ergänzt die Ordnerstruktur-Regeln in CODE_GUIDELINES
  um die Innen-Struktur der Prefabs.
- [ ] **Prefab-Struktur prüfen und aufräumen.** Die Menü-Prefabs sind
  verschachtelt — `MainMenuPanel` und `OptionsPanel` liegen *innerhalb*
  von `MainMenuUI`. Zu klären: welche Prefabs überhaupt verschachtelt
  sein sollen, wo Instanzen umbenannt wurden, ob angesammelte Overrides
  zurück in die Vorlagen gehören. Arbeitsstand je Prefab in
  `PREFAB_STATUS.md`. Gehört thematisch zur Aufbau-Konvention.
- [ ] **`SheepHealth` auf die `Health`-Komponente umstellen.**
  `Shared/Health/Health.cs` ist die allgemeine Komponente; `SheepHealth`
  macht dasselbe ein zweites Mal. Zu tun: prüfen, was wirklich
  schaf-spezifisch ist (`SheepSettings`, Testschalter, `Die()` mit
  Graveyard und FSM), den Rest ersetzen, Aufrufer nachziehen.
  Vor der Abgabe bewusst nicht gemacht, weil `SheepHealth` im TDD
  beschrieben ist.
- [ ] **Ordner-Restliste nach dem Umzug.** `Terrain_Village.asset` liegt
  lose in `Assets/`; `SO_Settings/SceneLoader/` hält eine einzige Datei,
  `SO_Settings/GameFlow/` steht leer; die Input-Dateien liegen in
  `Scripts/Player/`, `Scripts/Input/` ist leer; `Scripts/Grass/` und
  `Scripts/Grass/GrassRendering/` liegen ineinander. Dazu leere Ordner
  und `FolderTemplate/` löschen.
- [ ] **Lizenzordner anlegen:** `Assets/Licenses/` mit
  `Quaternius_UltimatePlatformerPack_CC0.txt`. Pakete mit eigener Lizenz
  behalten sie.

## HUD und UI

- [ ] **`HudController` und HUD-Einstellungen.** Ein Skript auf dem
  `InGameUI`-Objekt, das die HUD-Teile nach gespeicherten Einstellungen
  ein- und ausblendet (FPS, Fadenkreuz, Uhr, Zähmzähler), dazu die
  Schalter im Options-Fenster nach dem Muster von `GameSettings`.
  Abgrenzung, die schon gilt: Der `GameController` fasst beim Pausieren
  **nur das Root-Objekt** an, nie die einzelnen Teile — sonst schaltet er
  beim Fortsetzen Anzeigen wieder ein, die der Spieler ausgeschaltet hat.
- [ ] **Ladebild nach der Aktivierung.** Sobald das Dorf aktiv ist, ist
  das Ladebild weg. Wenn die Laufzeit-Platzierung kommt, braucht es dafür
  ein Canvas mit `DontDestroyOnLoad`. Betrifft `SceneLoader`.

## Beobachtungspunkte vom Abgabetag (2026-08-20)

Keine Aufgaben — Dinge, die auffielen und beim ersten Anzeichen von
Problemen als Erstes zu prüfen sind.

- [ ] **3.023 Glühwürmchen-Instanzen.** `MinSpacing` steht bei diesem Typ
  auf 13 statt der besprochenen 150. Auf Isors Rechner läuft es; jede
  VFX-Instanz ist aber ein eigener Effekt mit eigener Simulation, und die
  Dozentin lädt dieselbe Szene in 90 statt 8 Sekunden. Kommt Rückmeldung
  zu Rucklern bei Nacht, ist `MinSpacing` der erste Regler.
- [ ] **`SheepSense` fordert je Bild Speicher an.** Vier
  `Physics.OverlapSphere` pro Schaf und Frame, jeder legt ein neues
  `Collider[]` an; bei 19 Herden summiert sich das auf rund 2 KB je Frame.
  Der Fix ist mechanisch: wiederverwendeter Puffer,
  `OverlapSphereNonAlloc`, Trefferzahl als zweiter Parameter in
  `TryGetClosest`. Am Abgabetag bewusst nicht gemacht.
- [ ] **Wasserspiegel steht 0,01 unter der Plateauhöhe.** Im
  `TerrainConfig_Default.asset` ist die Plateauhöhe `0,15`, der
  Wasserspiegel `0,14`. `TerrainConfig.OnValidate` warnt, sobald das
  Wasser **auf oder über** der Plateauhöhe liegt („das Dorf würde
  absaufen") — die Warnung greift also gerade eben nicht. Ob der geringe
  Abstand Absicht ist oder aus dem Tuning stammt, entscheidet Isor; beim
  nächsten Anfassen der Terrain-Werte mit ansehen. *(Aufgefallen am
  2026-08-23 bei der Artifact-Bestandsaufnahme, nicht beim Spielen.)*

## Politur (nur wenn Zeit bleibt)

Aus der Interaktions-Session (2026-08-02) und den Gras-Sessions
(2026-08-04/05). Ton und Menü standen ebenfalls auf dieser Liste und sind
inzwischen gebaut.

- [ ] TMP-Font-Schärfe — Texte wirken pixelig
- [ ] Fadenkreuz aufwerten und kontextsensitiv machen
- [ ] Prompt-UI-Stil: Box/Fade, Tastensymbol
- [ ] HUD beim Pausieren ausblenden; Menü-Sortierung (Pause über HUD) und
  Maus-/Tastatur-Moduswechsel
- [ ] Sun Source explizit setzen
- [ ] Kamera-Far-Plane an die finale Weltgröße koppeln (Mond-Culling)
- [ ] Raycast-Target-Hygiene bei UI-Bildern
- [ ] Lichtblitz/Specular-Highlight auf dem Terrain — Material-Smoothness
  bzw. Bloom prüfen
- [ ] Herden-Placeable tunen: Höhenband, MaxSlope, ShoreMargin
- [ ] Lightmap-Warnung des generierten Terrains — Mesh hat keine UVs,
  Contribute GI ausschalten
- [ ] Magic Numbers im `MeshBuilder` benennen: `INDICES_PER_QUAD = 6`,
  `PADDING_RING = 1`, `NEIGHBOUR_SPAN = 2f`. Rein mechanisch. Isors
  Maßstab: keine Zahl im Code, deren Bedeutung er im Prüfungsgespräch
  erst herleiten muss.

## Sehr spät

- [ ] **Portfolio-Präsentation** (erst wenn eine Bewerbung ansteht):
  spielbarer Build aus der Build-Ablage (`Kern/VERSIONIERUNG.md` →
  „Ablage der Builds"), Video oder GIFs, gezielte Lese-Einladung ins
  private Repo; bei Bedarf ein kuratiertes Showcase-Repo mit nur
  eigenen Skripten. Das Projekt-Repo selbst bleibt dauerhaft privat
  (`Kern/DECISIONS.md` → „Sichtbarkeit und Zugang der Repos").
- [ ] **Kür fürs Terrain:** echte Flüsse (Spline-Mesh), Insel via
  Falloff-Map, höhen- und steigungsabhängige Texturierung.
- [ ] **Multiplayer**, Koop für 4–5 Spieler. Laut `GDD.md` gesetzt, nicht
  optional — wird nicht vorgebaut, aber bei Architekturentscheidungen
  mitgedacht.
