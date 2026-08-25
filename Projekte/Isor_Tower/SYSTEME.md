# SYSTEME.md — Was gerade im Projekt steckt

Ownership: Nur die erzeugte Systemliste — welche System-Ordner es unter
`Assets/Scripts/` gibt (plus `Assets/Editor/`), wie viele Skripte jeder
trägt und wozu er da ist. Keine Aufgaben (die ROADMAP der Schicht),
keine Ereignisse (das LOG), keine Begründungen (die DECISIONS).

**Diese Datei wird erzeugt** — die Liste kommt aus dem Projekt, die
Beschreibung je System kommt von Hand und wird bei jedem Lauf
übernommen. Erzeugt mit `Werkzeuge/systeme.py`; den Projektpfad nennt
`Kern/PFADE.md` → `PROJEKT`.

| System | Skripte | Letzte Änderung | Beschreibung |
|---|---|---|---|
| DayNightCycle | 6 | 2026-08-20 | Ingame-Uhr und Tag-Nacht-Wechsel: Himmel, Nachteffekte, Zeitraffer; andere Systeme hören über den EventManager zu. |
| Diagnostic | 1 | 2026-08-05 | Messwert-Anzeigen fürs laufende Spiel — bisher die FPS-Anzeige. |
| Editor | 7 | 2026-08-19 | Editor-Werkzeuge, nicht im Build: Terrain-Generator und Prefab-Painter, je als Window mit Presenter. |
| Enemies | 1 | 2026-08-20 | Gegner — bisher nur der Goblin als Platzhalter. |
| GameFlow | 4 | 2026-08-20 | Spielablauf vom Hauptmenü ins Spiel: Szenenwechsel mit Ladebalken, zentraler GameController. |
| Grass | 7 | 2026-08-05 | Gras per GPU-Instancing: Zellen als LOD-Einheit, Render-Profile, Interaktion mit dem Spieler. |
| Health | 1 | 2026-08-16 | Wiederverwendbare Lebenspunkte-Komponente für alles, was Schaden nehmen kann. |
| HerdManager | 1 | 2026-08-16 | Herdenverwalter: wird platziert statt einzelner Schafe, erzeugt und führt die Herde. |
| Interfaces | 5 | 2026-08-16 | Die systemeübergreifenden Interfaces des Projekts. |
| ObjectPlacement | 13 | 2026-08-20 | Prozedurale Platzierung per Poisson-Disc: Dichte-Strategien, Ausschlusszonen, Spawnen zur Laufzeit hinter dem Ladebalken. |
| Player | 9 | 2026-08-20 | First-Person-Spieler: Input-Reader als einzige Naht zum Input-System, Bewegung, Kamera, Interaktion, Schritte. |
| Sheep | 8 | 2026-08-16 | Das Schaf als Wesen: Sinne, Hunger, Leben, Bewegung, Zähm-Interaktion — die Zustandslogik liegt in SheepFSM. |
| SheepFSM | 15 | 2026-08-03 | Zustandsmaschine des Schafs: elf Zustände von Idle bis Dead, gemeinsame Basis und Einstellwerte je Zustand. |
| Timer | 1 | 2026-07-03 | Wiederverwendbarer Countdown-Baustein für zeitgesteuerte Abläufe. |
| Torch | 2 | 2026-08-16 | Die Fackel als interagierbares Licht-Objekt. |
| UI | 7 | 2026-08-16 | HUD-Anzeigen (Uhrzeit, Lebensbalken, Zähm-Status), Menü-Bausteine und GameSettings. |
| WorldGeneration | 5 | 2026-08-20 | Terrain-Pipeline: Heightmap aus Perlin-Rauschen, Höhenkurve, Plateaus, Mesh-Bau — konfiguriert über das TerrainConfig-SO. |
