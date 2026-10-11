# LOG.md — Chronik Game Jam Semester 3

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste
oben. Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur
ergänzt. Was als Nächstes kommt, steht in der ROADMAP dieser Schicht;
warum es so gebaut ist, in den DECISIONS; die Lern-Rubriken stehen in
`Kern/LERNLOG.md`.
Format: Ereignisse als `- JJJJ-MM-TT — Ereignis (1–3 Sätze)`.

- 2026-10-10 — Schicht angelegt, J1 und J2 gebaut: Isor schrieb
  `IInteractable` selbst (Fix `class` → `interface`, Parameter nach
  Review in `interactor` umbenannt) und den `ColorBucket` mit
  TODO-Gerüst für `CanInteract`; im Review fiel `Destroy(this)` statt
  `Destroy(gameObject)` auf und ein überflüssiges Inspector-Feld auf
  den Spieler. Header und Summaries durch Claude, beides von Isor
  gepusht bzw. zum Push bereit.
- 2026-10-10 — J3 und J5a gebaut, J5b/J5c durch Claude: Portalpaar im
  Gespräch ausdesignt und das Portal von Isor getippt; `IDamageable` und
  der Gegner-Tod mit Portalen ebenfalls von Isor (Review fand Min statt
  Max, Spawn ohne Position, Ziele nicht über Kreuz). Patrol, Sicht und
  Attack schrieb Claude auf Isors Wunsch wegen Erkältung; Kompilier-Probe
  per `dotnet build` ohne Fehler. Am selben Tag `Kern/CODE_GUIDELINES.md`
  wieder für C# in Kraft gesetzt (`Kern/DECISIONS.md`).
- 2026-10-11 — J4 und J6 gebaut, alles in der Sandbox getestet: Isor
  tippte SceneLoader und Paintable selbst, Claude legte die lokale
  Sandbox an (Test-Spieler, Test-Kamera, Test-Sprites; Ausschluss per
  `.git/info/exclude`, per `git status` geprüft). Isors Testlauf in
  Unity bestand alle sechs Stationen — Eimer, Gegner-Sicht und -Schaden,
  Tod mit Portalpaar, Teleport hin und zurück, Überblenden. Layer Player
  und Enemy sowie das Paket *2D Sprite* gepusht; Isors Jam-Anteil ist
  damit bis auf den Inventar-Anschluss fertig.
