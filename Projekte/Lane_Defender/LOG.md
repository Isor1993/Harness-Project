# LOG.md — Chronik und Kurs-Log Lane Defender

Ownership: Nur was wann passiert ist — datierte Ereignisse und die
Kurs-Einträge des Lernens am Projekt, älteste oben. Eine **Chronik**:
Einträge werden nie geändert oder gekürzt, nur ergänzt. Was als
Nächstes kommt, steht in der ROADMAP dieser Schicht; warum das Projekt
so gebaut ist, in den DECISIONS. Zeugnisse lesen aus dieser Datei und
aus `Kern/LERNLOG.md`.
Format: Ereignisse als `- JJJJ-MM-TT — Ereignis (1–3 Sätze)`.
Kurs-Einträge wie im Python-Lesekurs als
`- JJJJ-MM-TT — <Baustein> · <Thema>` mit den Zeilen `Selbst:` (was
Isor ohne Hilfe gelang), `Hilfe:` (wo ein Hinweis nötig war) und
`Fehler:` (Verwechslungen, wörtlich genug zum Wiederfinden); eine
leere Rubrik schreibt `—`.

- 2026-09-07 — Projekt entworfen und angelegt: Konsolen-Tower-Defense
  „Grid Defense" als eigenständiges C++-Konsolenprojekt für Modul
  5-101. Design, Lernpfad und Schnittlinien in den DECISIONS dieser
  Schicht, Meilensteine in ROADMAP und ZEITPLAN. Machbarkeit des
  Tick-Modells in der Session per interaktiver Demo gezeigt; Grundlage
  ist die Vorjahres-Vorschau, Isors Originaltexte stehen noch aus.
- 2026-09-07 — Umschwenk auf den Lane-Shooter „Lane Defender"
  (Tapper-Vorbild), Schicht von `Grid_Defense` zu `Lane_Defender`
  umbenannt: Die Artefakte der Tick-Demo zeigten die Fehlerfläche der
  2D-Geometrie, Isors Lane-Idee streicht sie strukturell; dazu die
  Regel „Raster-Stabilität vor Schmuck". Design in den DECISIONS,
  Meilensteine und Schätzung (36 h) neu in ROADMAP und ZEITPLAN.
- 2026-09-08 — Baustart vorbereitet: eigenes Code-Repo `Lane-Defender`
  angelegt (Entscheidung in den DECISIONS), Symbol-Kandidaten für den
  M1-Zeichentest in die ROADMAP-Aufgabe gelegt, L1-Anleitung nach
  `Sandbox/`. VS 2026 samt C++-Workload und cl.exe am Rechner
  verifiziert — vor der ersten Kursstunde ist nichts zu installieren.
  Zielfenster aus der Semester-Roadmap: abgabefertig bis ~05.10.
- 2026-09-09 — Lern-Vorlauf gestartet: L1 komplett (VS-Projekt
  `LaneDefender` im Code-Repo angelegt, kompiliert, Debugger benutzt;
  Commit `Update V 0.0002`) und L2 zur Hälfte — Ü1 Typen und Ü2
  Kontrollfluss samt Guard Clause und SAE-Konstanten (Commit
  `Update V 0.0003`). Die Lern-Rubriken der drei Einheiten stehen in
  `Kern/LERNLOG.md` unter 2026-09-09. Isors Einschätzung zum Schluss:
  bisher „recht leicht, nur Syntax-Gewöhnung", Respekt vor den
  Pointern (L3). Session nach rund zwei Stunden bewusst an der
  Baustein-Grenze geschnitten.
