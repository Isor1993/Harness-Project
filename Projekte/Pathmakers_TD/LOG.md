# LOG.md — Chronik Pathmakers TD

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste
oben. Begründungen gehören in die DECISIONS der Schicht, Pläne in die
ROADMAP.
Format: `- JJJJ-MM-TT — Ereignis.` Ein bis drei Zeilen je Eintrag.

- 2026-10-20 — P1-Brainstorm-Runde: Prototyp-Vorgehen entschieden und
  der Prototyp in die Bausteine P-B1 bis P-B8 geschnitten (DECISIONS,
  Einträge vom 2026-10-20; Bausteine in der ROADMAP). Abends Repo
  `Pathmakers-TD` mit Unity-Projekt `PathmakersTD` (6.3, URP)
  angelegt; .gitignore-Anker-Falle vor dem ersten Projekt-Commit
  behoben (Commit „Update V 0.0001").
- 2026-10-21 — P-B1-Übernahme: Netz-Pakete, eigenes UGS-Cloud-Projekt,
  Menü- und Netz-Grundlage per Export/Import aus Its-DOT geholt und
  nachbereinigt (Testkram, Alt-Szenen, tote Verweise; Commit „Update
  V 0.0002"); Menü-Kette im Play-Test lauffähig. Steuerungsmodell
  korrigiert: Befehlsklick statt Direktsteuerung (DECISIONS →
  „2026-10-21 — Steuerung: Befehlsklick statt Direktsteuerung").
- 2026-10-21/22 — P-B1 fertiggebaut: Figur-Paket (PlayerSpawner,
  PlayerMotor, ClickCommandInput samt Klick-Ring, StrategyCamera mit
  Start-Snap, Action-Map „Gameplay", Multiplayer Play Mode) und der
  Zwei-Instanzen-Test über Relay bestanden — nur die eigene Figur
  steuerbar, Positions-Sync auf der Kopie, Ring bleibt lokal.
  8:05 h getrackt (`ABGABE_NOTIZEN.md` → „P-B1").
