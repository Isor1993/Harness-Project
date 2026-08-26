# ALTSTAND.md — Bestand aus Semester 2

Ownership: Nur was am Ende von Semester 2 dastand und was dabei auffiel —
die Befunde, die bei einer Übernahme-Entscheidung zählen. **Kein
Auftrag.** Was gebaut wird, steht in `ROADMAP.md`; warum etwas so ist, in
`DECISIONS/`; was existiert, in `SYSTEME.md` und `PREFAB_STATUS.md`.

Wozu diese Datei da ist: Semester 3 ist ein Neustart desselben Projekts
(`DECISIONS/Multiplayer.md` → „Semester 3 ist ein Neustart desselben
Projekts"). Nach der **Übernahme-Regel** wird jeder Baustein aus Semester
2 einzeln entschieden, wenn er gebraucht wird — **mitnehmen**,
**anpassen** oder **neu**. Diese Liste ist das, was man dabei aufschlägt:
Sie sagt, was an dem Baustein bekannt ist, bevor man ihn anfasst.

Format: `- **Titel** — was bekannt ist.` Danach, wo es hilft, eine Zeile
*Bei Übernahme:* mit dem, was zuerst zu prüfen wäre. Punkte, die im neuen
Bauplan aufgegangen sind, tragen stattdessen *Aufgegangen in:* mit dem
Zeiger dorthin.

**Diese Datei wird nicht abgearbeitet.** Sie hat keine Haken, weil sie
keine Aufgaben führt — ein offener Haken behauptet sonst dauerhaft, hier
läge Arbeit (`Kern/DOC_RULES.md`, Abschnitt 11).

Herkunft: Der gesamte Inhalt stand bis zum 2026-08-26 in `ROADMAP.md`,
die mit dem Neustart geleert wurde. Übernommen wurden alle 31 Punkte des
Abgabestands, unverändert im Inhalt und nur in der Rolle geändert. **Nicht
hier**, weil kein Altstand: der Punkt „Portfolio-Präsentation", den eine
Parallel-Session am selben Tag ergänzte — er blieb in der `ROADMAP.md`.

---

## Pipeline, Platzierung und Gras

- **Ausrichtung am GDD** — Pipeline runtime-fähig machen (Editor-Tool und
  Laufzeit als zwei Aufrufer derselben Stufen); Welt-Wahrheit als Seed
  statt Szene festziehen; Village als festes Grundmesh mit
  Placement-Befüllung darauf; Zellen-Struktur, damit ein wachsendes
  Village später streamen kann. Hängt an der offenen Frage im `GDD.md` →
  „Village-Terrain".
  *Aufgegangen in:* `ROADMAP.md` → „Phase 3 · Floor_1 und das Portal"
  (Seed als Welt-Wahrheit) — der Rest bleibt offen.
- **Platzierungs-Algorithmen neu bewerten** — Zellen-lokales Poisson ist
  mit der Kachelung erledigt; offen bleibt, ob Bridson für Gras das
  richtige Verfahren ist (Jitter-Grid wäre ein Bruchteil der Arbeit,
  zeigt aber Raster — für Bäume ungeeignet). Ebenfalls offen: Bucketing
  des Zellenbaus in die Kachelschleife ziehen, Exclusion als Broad Phase
  je Kachel, Aufräumpass für die Kachelränder.
  *Bei Übernahme:* Die Platzierung muss auf zwei Rechnern dasselbe
  liefern — das ist die härtere Anforderung als die Verfahrenswahl.
- **Massen-Bepflanzung als eigenes System** — LOD, Culling und Instancing
  zusammen. Das Instancing ist vorgezogen; hier bleiben LOD,
  Entfernungs-Ausblendung und Culling je Halm via `BatchRendererGroup`.
  Großprojekt, eigene Design-Session.
- **Gras-Rendering aus `Systems/TerrainGenerator/` herauslösen** — eigener
  System-Ordner (Umzug im Unity-Editor wegen der .meta-GUIDs). Dabei
  LOD-Fade zwischen den Stufen und Laufzeit-Spawn der Herden mitdenken
  (löst auch das Aufsetzen aufs Gelände).
- **Save-System** — Weltzustand als Änderungsliste gegenüber dem
  Ausgangszustand.
  *Aufgegangen in:* `ROADMAP.md` → „Phase 2 · Datenskelett und
  Schnittstelle" und „Phase 6 · StarterVillage und Speichern". Die
  Vermutung von damals, das decke zugleich den Multiplayer-Sync ab, hat
  sich bestätigt.
- **Spiel-Features aufbauen** — Kampf, Loot, Inventar, Crafting, Quests.
  *Aufgegangen in:* `ROADMAP.md` → „Phase 4 · Kampf" und „Phase 5 · Beute
  und Inventar". Crafting und Quests sind aus dem Semesterschnitt heraus
  (`DECISIONS/Multiplayer.md` → „Semesterschnitt").

## Aufräumen und Konventionen

- **Wasserspiegel bekommt keinen Collider** — der Spieler läuft heute in
  den See und weiter auf dem Grund. Offene Frage aus
  `DECISIONS/Terrain_Mesh.md` → „Welt-Begrenzung gehört ins Terrain-Tool"
  (2026-08-19).
- **Ordnerstruktur im Unity-Projekt gegen die Vorlage prüfen** — Maßstab
  ist `05_Werkzeuge\Vorlagen\Unity_Ordnerstruktur`. Übernommen aus dem
  README des Datenbaums (2026-08-22).
  *Bei Übernahme:* Beim Neustart ohnehin fällig — neue Szenen kommen in
  eine Struktur, und die sollte die richtige sein.
- **GameObject-/Prefab-Aufbau-Konvention** — einheitliches Schema, wie ein
  Objekt *innen* aufgebaut ist: Root, Visual/Mesh-Kind, VFX-Kind,
  Collider, Logik-Komponenten. Am Ende von Semester 2 durchgewürfelt.
  Eigene Design-Session.
  *Bei Übernahme:* Betrifft das Spieler-Prefab, das in Phase 1 zum
  Netzobjekt wird — dort entsteht die erste Gelegenheit, es richtig zu
  machen.
- **Prefab-Struktur prüfen und aufräumen** — die Menü-Prefabs sind
  verschachtelt: `MainMenuPanel` und `OptionsPanel` liegen *innerhalb* von
  `MainMenuUI`. Zu klären: welche Prefabs verschachtelt sein sollen, wo
  Instanzen umbenannt wurden, ob angesammelte Overrides zurück in die
  Vorlagen gehören. Arbeitsstand je Prefab in `PREFAB_STATUS.md`.
  *Bei Übernahme:* Das Menü kommt gesetzt mit und wird in Phase 1
  erweitert — dabei fällt diese Struktur zwangsläufig auf.
- **`SheepHealth` auf die `Health`-Komponente umstellen** —
  `Shared/Health/Health.cs` ist die allgemeine Komponente; `SheepHealth`
  macht dasselbe ein zweites Mal. Zu tun: prüfen, was wirklich
  schaf-spezifisch ist (`SheepSettings`, Testschalter, `Die()` mit
  Graveyard und FSM), den Rest ersetzen, Aufrufer nachziehen. Vor der
  Abgabe bewusst nicht gemacht, weil `SheepHealth` im TDD beschrieben ist.
- **Ordner-Restliste nach dem Umzug** — `Terrain_Village.asset` liegt lose
  in `Assets/`; `SO_Settings/SceneLoader/` hält eine einzige Datei,
  `SO_Settings/GameFlow/` steht leer; die Input-Dateien liegen in
  `Scripts/Player/`, `Scripts/Input/` ist leer; `Scripts/Grass/` und
  `Scripts/Grass/GrassRendering/` liegen ineinander. Dazu leere Ordner und
  `FolderTemplate/` löschen.
- **Lizenzordner anlegen** — `Assets/Licenses/` mit
  `Quaternius_UltimatePlatformerPack_CC0.txt`. Pakete mit eigener Lizenz
  behalten sie.
  *Bei Übernahme:* Gilt unabhängig vom Neustart, sobald fremde Assets
  wieder ins Projekt kommen.

## HUD und UI

- **`HudController` und HUD-Einstellungen** — ein Skript auf dem
  `InGameUI`-Objekt, das die HUD-Teile nach gespeicherten Einstellungen
  ein- und ausblendet (FPS, Fadenkreuz, Uhr, Zähmzähler), dazu die
  Schalter im Options-Fenster nach dem Muster von `GameSettings`.
  Abgrenzung, die schon gilt: Der `GameController` fasst beim Pausieren
  **nur das Root-Objekt** an, nie die einzelnen Teile — sonst schaltet er
  beim Fortsetzen Anzeigen wieder ein, die der Spieler ausgeschaltet hat.
- **Ladebild nach der Aktivierung** — sobald das Dorf aktiv ist, ist das
  Ladebild weg. Für die Laufzeit-Platzierung braucht es ein Canvas mit
  `DontDestroyOnLoad`. Betrifft `SceneLoader`.
  *Bei Übernahme:* Der Ladebalken wird in Phase 1 ohnehin angefasst — er
  muss dann auf mehrere Spieler warten.

## Beobachtungen vom Abgabetag (2026-08-20)

Keine Aufgaben, sondern Dinge, die auffielen und beim ersten Anzeichen von
Problemen als Erstes zu prüfen sind.

- **3.023 Glühwürmchen-Instanzen** — `MinSpacing` steht bei diesem Typ auf
  13 statt der besprochenen 150. Auf Isors Rechner läuft es; jede
  VFX-Instanz ist aber ein eigener Effekt mit eigener Simulation, und die
  Dozentin lädt dieselbe Szene in 90 statt 8 Sekunden. Kommt Rückmeldung
  zu Rucklern bei Nacht, ist `MinSpacing` der erste Regler.
- **`SheepSense` fordert je Bild Speicher an** — vier
  `Physics.OverlapSphere` pro Schaf und Frame, jeder legt ein neues
  `Collider[]` an; bei 19 Herden rund 2 KB je Frame. Der Fix ist
  mechanisch: wiederverwendeter Puffer, `OverlapSphereNonAlloc`,
  Trefferzahl als zweiter Parameter in `TryGetClosest`.
  *Bei Übernahme:* Das ist der Befund, der zählt, wenn entschieden wird,
  ob die Schafe mitkommen — im Koop rechnet der Host **alle** Herden.
- **Wasserspiegel steht 0,01 unter der Plateauhöhe** — im
  `TerrainConfig_Default.asset` ist die Plateauhöhe `0,15`, der
  Wasserspiegel `0,14`. `TerrainConfig.OnValidate` warnt, sobald das
  Wasser **auf oder über** der Plateauhöhe liegt — die Warnung greift also
  gerade eben nicht. Ob der geringe Abstand Absicht ist oder aus dem
  Tuning stammt, ist offen. *(Aufgefallen am 2026-08-23 bei der
  Artifact-Bestandsaufnahme, nicht beim Spielen.)*

## Politur

Aus der Interaktions-Session (2026-08-02) und den Gras-Sessions
(2026-08-04/05). Ton und Menü standen ebenfalls auf dieser Liste und sind
gebaut.

- **TMP-Font-Schärfe** — Texte wirken pixelig.
- **Fadenkreuz** aufwerten und kontextsensitiv machen.
- **Prompt-UI-Stil** — Box/Fade, Tastensymbol.
- **HUD beim Pausieren ausblenden** — Menü-Sortierung (Pause über HUD) und
  Maus-/Tastatur-Moduswechsel.
- **Sun Source explizit setzen.**
- **Kamera-Far-Plane an die finale Weltgröße koppeln** (Mond-Culling).
- **Raycast-Target-Hygiene bei UI-Bildern.**
- **Lichtblitz/Specular-Highlight auf dem Terrain** — Material-Smoothness
  bzw. Bloom prüfen.
- **Herden-Placeable tunen** — Höhenband, MaxSlope, ShoreMargin.
- **Lightmap-Warnung des generierten Terrains** — Mesh hat keine UVs,
  Contribute GI ausschalten.
- **Magic Numbers im `MeshBuilder` benennen** — `INDICES_PER_QUAD = 6`,
  `PADDING_RING = 1`, `NEIGHBOUR_SPAN = 2f`. Rein mechanisch. Isors
  Maßstab: keine Zahl im Code, deren Bedeutung er im Prüfungsgespräch erst
  herleiten muss.

## Was damals „sehr spät" hieß

- **Kür fürs Terrain** — echte Flüsse (Spline-Mesh), Insel via
  Falloff-Map, höhen- und steigungsabhängige Texturierung.
- **Multiplayer, Koop für 4–5 Spieler.**
  *Aufgegangen in:* die gesamte `ROADMAP.md` — mit der Design-Session vom
  2026-08-25/26 ist daraus der Rahmen von Semester 3 geworden.
