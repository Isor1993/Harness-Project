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
- 2026-09-11 — L2 Ü3 Funktionen erledigt, am Spielcode: `main` in die
  Überladungsfamilie `PrintMessage` (string-/int32_t-/float-Wege,
  Default `a_bNextLine = true`) und `LoseLives` zerlegt, Prototypen
  oben, Definitionen unter `main`; die Datei konsequent auf `int32_t`
  umgestellt (Entscheidung in den DECISIONS dieser Schicht).
  Regressionslauf gegen die Ü2-Ausgabe bestanden: speed 1.5,
  Round status true, Leben 5→0, Game Over in Round 2. Die
  Lern-Rubriken stehen in `Kern/LERNLOG.md` unter 2026-09-11; die
  Verkürzungsfrage aus `PLAN.md` hat Isor mit „voll machen"
  entschieden — offen bleibt nur Ü4 Eingabe-Validierung.
- 2026-09-12 — L2 Ü4 Eingabe-Validierung erledigt, am Spielcode: neue
  Funktion `ReadValueInput` (fail/clear/ignore samt `continue`,
  Bereichsprüfung gegen `I_MIN_LIVES`) ersetzt das feste `iLives = 5`;
  Aufgabenzettel in `Sandbox/U4_Aufgabe.txt`. Testreihe
  `abc`/`-3`/`0`/`5` bestanden, im Gegenlauf belegt (warnungsfrei
  unter /W4, je Fehleingabe genau eine Meldung, 5 startet das Spiel).
  Damit ist L2 komplett, der Lern-Vorlauf steht vor L3; die leere
  Eingabe bleibt stilles Warten (DECISIONS dieser Schicht),
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-09-12.
- 2026-09-12 — L3 Werte, Pointer, Speicher erledigt, am Spielcode und
  im Debugger: Ü1 Adressen (Watch mit `&`, Call-Stack-Frames, die zwei
  Kartons von `LoseLives` an echten Adressen belegt), Ü2 erster Pointer
  als Wegwerf-Snippet in main (nullptr-Start, Wächter, Schreiben über
  `*`; nach der Abnahme wieder entfernt), Ü3 die string-Parameter der
  PrintMessage-Familie auf const-Referenzen (drei Überladungen, je
  Prototyp und Definition; Regressionslauf bestanden, /W4
  warnungsfrei). Damit ist der Lern-Vorlauf L1–L3 komplett — nächster
  Baustein ist M1. Aufgabenzettel in `Sandbox/L3_Aufgabe.txt`,
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-09-12.
- 2026-09-12 — M1-Design-Abschnitt, die erste Design-Session des
  Projekts: Ablauf als Szenen-Zustandsautomat mit sechs Stationen nach
  Isors Szenen-Modell, dazu Menü-Buttons mit Rahmen, Titel in
  Linien-Schrift mit Start-Einblendung, Namensregeln, VT-Technik,
  Zeichentest hinter versteckter Taste T und die M1-Struktur — acht
  Einträge in den DECISIONS dieser Schicht. ZEITPLAN vor Baustart von
  36 auf 50 h angehoben (Isor); der Übungsstand liegt gesichert als
  `Sandbox/L2_L3_Uebungsstand.cpp`.
- 2026-09-12 — M1-Development gestartet: gelieferter Baustein
  `Console.h`/`Console.cpp` (VT-Init mit UTF-8, Farb-Konstanten,
  Cursor-Steuerung, Einzeltasten-Abfrage) gebaut, von Isor eingebunden
  und in einer langen Verstehens-Runde komplett abgenommen —
  Compiler/Linker, Bit-Oder, Ausgabe-Puffer, Tastatur-Warteschlange;
  Lern-Rubriken in `Kern/LERNLOG.md`. Auf Isors Stilentscheid auf
  ausgeschriebene Schritte umgebaut, /W4-warnungsfrei. Aufgabenzettel
  für den Zeichentest in `Sandbox/M1_Zeichentest_Aufgabe.txt`; die
  M1-Ist-Zeit trackt Isor ab jetzt mit Grindstone (Stand ~3,5 h inkl.
  Design). Session am Abend geschnitten — das Zeichentest-Tippen steht
  aus.
- 2026-09-13 — M1 Zeichentest gebaut, gemessen und entschieden: main
  aufgeräumt (Übungsschleife und `ReadValueInput` raus), die
  PrintMessage-Familie in das neue Paar `Output.h`/`Output.cpp`
  umgezogen (erster von Isor selbst angelegter Header; `LoseLives`
  komplett entfernt), Compiler-Flag `/utf-8` in allen Konfigurationen
  gesetzt und die Zeichentest-Szene `RunSymbolTest` gebaut — 30
  Bewerber, Testreihe in VS-Konsole und Windows Terminal (identisches
  Rendering, gleiche Terminal-Engine). Ergebnis und Folge-Entscheid in
  den DECISIONS dieser Schicht: 26 rasterfest, Schachfiguren
  doppelbreit — von Isor als Figuren-Symbole gesetzt, das Lane-Layout
  wird dafür ausgelegt. Lern-Rubriken in `Kern/LERNLOG.md` unter
  2026-09-13. Nachtrag vom Abschnittsende: Die Test-Szene hat Isor
  unaufgefordert selbst nach `SymbolTest.h`/`SymbolTest.cpp`
  ausgelagert; Review-Pass (Exit-Konstante zurück zu main, eigener
  Header zuerst, Datei-Köpfe) durch Claude, Build warnungsfrei.
