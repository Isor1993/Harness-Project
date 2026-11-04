# SYSTEME.md — Was gerade im Projekt steckt

Ownership: Nur die erzeugten Listen — System-Ordner unter
`Assets/Scripts/` (plus `Assets/Editor/`), die oberste Assets-Ebene
und die Wurzel-Objekte jeder Szene. Keine Aufgaben (ROADMAP), keine
Ereignisse (LOG), keine Begründungen (DECISIONS).

**Diese Datei wird erzeugt** — die Listen kommen aus dem Projekt, die
Beschreibung je System kommt von Hand und wird bei jedem Lauf
übernommen. Erzeugt mit `Werkzeuge/systeme.py`; den Projektpfad nennt
`Kern/PFADE.md` → `PROJEKT_PATHMAKERS`.

## Spickzettel — die Ordnungs-Regeln

Kurzform; die Regeln besitzt `Kern/CODE_GUIDELINES.md`.

1. **Ordner:** Gewerk oben (`Art/`, `Audio/`, `Scripts/` …), Typ
   darunter, je ein Ordner pro System. Scripts sortieren nach der
   System-Frage (*welches Spielsystem?*), Canvas-Zeug nach Schicht
   (`UI/` Menü, `HUD/` ingame).
2. **Namen:** erst was, dann wie — `Präfix_Name_Variante` (T_, M_,
   SM_, P_, SO_, TL_, Brush_, Music_, SFX_). Englisch, PascalCase,
   nie Leerzeichen.
3. **Szene:** Zonen in Strich-Optik — `--- SYSTEM ---` (Etikett, lose
   Dienste), `--- World ---` und `--- UI ---` (echte Parents auf
   0/0/0, nie bewegen). Prüfsatz: *beschreibt die Position die Welt,
   oder ist sie egal?*

## Scripts — die Systeme

| System | Skripte | Letzte Änderung | Beschreibung |
|---|---|---|---|
| Building | 8 | 2026-11-04 | Pfad-Bausystem: Grid, Ghost, Bau-Queue, Konnektivität, Netz-Briefe (PathGridNet) |
| GameFlow | 4 | 2026-10-31 | Szenenwechsel und Boot: Loader, Ladebalken, Bootstrap, Hauptmenü-Steuerung |
| HUD | 4 | 2026-11-04 | Ingame-Anzeigen: Bau-Leiste und die Info-Panels (Basis + Kachel + Senden) |
| Interfaces | 2 | 2026-11-04 | Alle Verträge, zentral: lose = allgemein (ISessionService), Unterordner je System (UiMode/IUiMode) |
| Monsters | 3 | 2026-11-03 | Gegner: Läufer-Skript, Steckbrief-SOs, Host-Spawner |
| Networking | 5 | 2026-11-03 | Match-Infrastruktur: MatchSetup (Brett), Spawner, Lobby, Relay |
| Player | 4 | 2026-11-03 | Der Avatar selbst: Motor, Kamera, Klick-Eingabe, Marker |
| Sending | 2 | 2026-11-03 | Senden-System: Sendegebäude und Welt-Klick; Sende-Ring folgt mit P-B5 |
| Tools | 1 | 2026-10-30 | Werkzeug-Komponenten in der Szene (Map-Layout-Gizmo), Editor-Teil hinter #if-Zaun |
| UI | 8 | 2026-10-31 | Menü-Kette und generische UI-Helfer (Lobby, Optionen, Auswahl-Wächter) |
| UiMode | 1 | 2026-11-04 | Die Bühne: ActiveUiMode-Registratur — im Bau (Block 2), liegt noch als Unity-Vorlage da |

## Assets — oberste Ebene

| Ordner | Dateien |
|---|---|
| Art | 16 |
| Audio | 2 |
| Fonts | 3 |
| Prefabs | 14 |
| SO_Settings | 2 |
| Scenes | 5 |
| Scripts | 42 |
| Settings | 7 |
| Terrain | 8 |
| TextMesh Pro | 170 |

## Szenen — Wurzel-Objekte

Reihenfolge wie im Hierarchie-Panel; Zahl = direkte Kinder.

### GameWorld

- --- SYSTEM ---
- Main Camera
- Directional Light
- GameNetwork
- PlayerSpawner (4 Kinder)
- NavMesh Surface
- Tool_MapLayout
- BuildMode (1 Kind)
- SceneBootstrap
- --- World --- (11 Kinder)
- --- UI --- (2 Kinder)

### MainMenu

- LoadingCanvas (1 Kind)
- MainMenuUI (7 Kinder)
- EventSystem
- MainMenuController
- Main Camera
- Directional Light
- Music
- GameSettings
- NetworkManager (Prefab)
- LobbyPlayerSpawner

### Testarea

- --- SYSTEM ---
- NavMesh Surface
- BuildMode (1 Kind)
- GameNetwork
- TestareaBootstrap
- Main Camera
- Directional Light
- PlayerSpawner
- --- World --- (5 Kinder)
- --- UI --- (2 Kinder)
