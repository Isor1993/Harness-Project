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
- 2026-09-13 — M1 Szenen-Zustandsautomat gebaut, zweiter Baustein des
  Tages: enum class mit sieben Zuständen, while-plus-switch in
  `main`, sechs Stub-Szenen im Kreis (Menü → Name → Tutorial → Spiel
  → Endscreen → Menü), Exit über `GS_EXIT`, Symbol-Test als eigener
  Zustand mit Rückweg ins Menü. Architektur als Melde-Muster
  (DECISIONS dieser Schicht); der Umbau dahin lief in acht
  Einzel-Steps auf Isors Wunsch. Console-Baustein um das
  Scrollback-Löschen erweitert (`3J`). Offen in M1: das echte
  Hauptmenü (Linien-Titel, Buttons, Tasten `T`/`ESC`), Namenseingabe
  und Endszene echt. Lern-Rubriken in `Kern/LERNLOG.md`,
  M1-Ist-Zeit per Grindstone: 10:22 h.
- 2026-09-14 — M1 Aufbau-Gespräch Hauptmenü (nachgetragen am 18.09.
  beim Session-Ende): Isors Architektur-Entwurf (Output als reiner
  Zeichner, je Szene eine eigene Einheit) mit dem Bestand abgeglichen;
  Einigung: Ein-Puffer-Frame auch fürs Menü, Marker wandert im Frame,
  `SetCursorPosition` erst zur Namenseingabe, erst statisch bauen und
  die Einblendung danach. Titel gewählt: Figlet „Standard" voll
  ausgelegt (~72 Zeichen), Rohfassung in
  `Sandbox/M1_Titel_LaneDefender.txt`; die Blockschrift (128 Zeichen)
  scheiterte an der Terminalbreite.
- 2026-09-18 — M1 Hauptmenü-Frame gebaut: Isors Solo-Stand
  (`MainMenu.h`/`.cpp` mit Raw-String-Blöcken, eigene
  Start/Exit-Buttons in Linien-Schrift, `BuildEmptyNextline`) plus
  gemeinsamer Feinschliff — Tab-Bug im Titel gefunden (Raw-String
  übernimmt die Editor-Einrückung), alle Blöcke auf `I_SCREEN_WIDTH`
  120 zentriert (skriptgeprüft, mittig um Spalte 60), die Szene nach
  MainMenu umgezogen (Prototyp-Doppel aufgelöst, `PrintMainMenu`
  entfernt — Output wieder generisch), Magic Numbers benannt,
  Köpfe/Summaries nachgezogen; kompiliert warnungsfrei unter /W4.
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-09-18. Offen in M1:
  Auswahl-Schleife, Titel-Einblendung, Namenseingabe, Endszene.
- 2026-09-19 — M1 Auswahl-Schleife, Marker und Sound fertig: Die
  Menü-Schleife läuft als Zahl-Zustand (`iSelection`, Umlauf in beide
  Richtungen, Tasten ↑↓/W/S, Enter je Auswahl, `ESC`, `T`), gedruckt
  je Runde ab Cursor-Home bei konstanter Frame-Höhe. Marker-Optik
  entschieden und gebaut: Balken unter dem gewählten Button plus
  Gelbfärbung, `AddSelectedMarker` als Isors gemeinsame Methode mit
  Balken-Parameter, Putz-Zeile aus 72 Leerzeichen gegen stehen
  gebliebene Balken (DECISIONS dieser Schicht, beide vom 19.09.).
  Scroll-Ursache diagnostiziert und behoben — der Frame füllte mit
  dem PrintMessage-Extra-`\n` exakt die 30 Terminal-Zeilen
  (Extra-`\n` abbestellt, Titel-Luft 6→4, Cursor in InitConsole
  versteckt). Sound-Feedback als eigenes Paar `Sound.h`/`Sound.cpp`
  (Move/Confirm/Error als freie Funktionen, Konstanten im .cpp,
  WinAPI nur dort); MainMenu.cpp beim VS-Encoding-Dialog auf UTF-8
  ohne Signatur gebracht, wie der Bestand. Review-Pass durch Claude
  (Datei-Köpfe, Summaries, Kosmetik, geliehenes `<cstdint>` in
  MainMenu.h behoben), Prüf-Build /W4 grün ohne Warnungen.
  Lern-Rubriken in `Kern/LERNLOG.md` unter 18./19.09. Offen in M1:
  Titel-Einblendung, echte Namenseingabe, echte Endszene.
- 2026-09-19 — M1 Namenseingabe ausdesignt und statisch gebaut: Am
  Nachmittag Design-Abschnitt nach Isors Paint-Skizze (Dialogfenster,
  freies Fokus-Modell, Eingabe selbst gezeichnet statt getline,
  Farbsprache Gelb/Hellrot — drei DECISIONS-Einträge), am Abend die
  Umsetzung des statischen Screens: `SetCursorPosition` und
  `S_COLOR_RED` in Console, Szenen-Dateien auf `*Scene` umbenannt
  und `NameInputScene.h`/`.cpp` angelegt (Umzug diesmal ohne
  Leih-Fehler), Dialogfenster aus Zeilen-Typ-Bauern mit
  Zeilen-Verteiler über fensterrelative Konstanten, Textzeilen mit
  Auffüll-Rechnung (static_cast/size_t), kurze Trennlinie,
  Balance-Pass, Schreiblinie unter der Tippzeile,
  Back/Confirm-Zeile. Unterwegs verstanden: Escape-Sequenz-Anatomie
  samt VT-Dolmetscher (InitConsole als Einschalter — halbe
  Console.cpp damit erklärt), Byte-Falle (`length()` zählt Bytes),
  Fließband-gegen-Zellen-Gedächtnis. /W4-Build grün; Sichtprüfung
  von Schreiblinie und Button-Zeile steht aus. Lern-Rubriken in
  `Kern/LERNLOG.md` unter 2026-09-19. Offen in M1: Zeichen-Schleife
  (Fokus, Whitelist, Farben), Titel-Einblendung, echte Endszene.
- 2026-09-19 — M1 Zeichen-Schleife, Teil 1 — Steuerung und
  Player-Klasse: Sichtprüfung des statischen Screens bestanden
  (gestrichelte Underscore-Optik bewusst gelassen — zählbare Slots);
  Gelb nach Zahlen- und Bildvergleich bestätigt (DECISIONS → „Grün
  als Fokusfarbe geprüft und verworfen", Dozentin-Merkpunkt in der
  ROADMAP). Steuerungs-Schleife der Namenseingabe in Schritten
  gebaut: Fokus-Verzweigung Feld/Buttons mit direkten Übergängen
  (Isors Modell — DECISIONS → „Enter ist der einzige Ausgang"),
  Sounds je Fall, ESC überall; erste eigene C++-Klasse `CPlayer`
  (`Player.h`/`.cpp`) und als Referenz durch main verdrahtet
  (DECISIONS → „Mini-Player-Klasse"); `I_SELECTION_CONFIRM`
  umbenannt, tote Versprechen InputIsValid/ClearNameInput aus dem
  Header entfernt. Rundgang-Test bestanden — die Sounds belegen den
  Fokuswechsel. /W4 grün bis auf die bewusst offene C4100
  (`a_player` unbenutzt bis zur Zeichen-Aufnahme). Drei
  Knowledge-Seiten (Nachname, break-Tür, Zustand-trägt-Wissen);
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-09-19. Offen in M1:
  Färbung, Zeichen-Aufnahme, Titel-Einblendung, echte Endszene.
- 2026-09-20 — M1 fertig: Färbung, Zeichen-Aufnahme, End- und
  Tutorial-Szene: Button-Färbung nach Isors Eigenversuch als
  Zuruf-Umbau (gemeinsames Zeilen-Skelett 3+4+103+7, AddFocusColor,
  GetButtonRow/GetMarkerRow — die Marker-Zeile putzt sich selbst);
  dabei der W4-Befund: Projekt stand seit Anlage auf /W3, alle
  „/W4 grün"-Angaben waren ungemessen — Warnstufe real auf Level4,
  totes Doppel-return in InitConsole entfernt (Störung in
  `Kern/STOERUNGEN.md`). Feld-Gelb über Farb-Parameter des
  Zeilen-Bauers (färben nach der Füllungs-Rechnung); Header nach dem
  Schaufenster-Prinzip entrümpelt. Zeichen-Aufnahme komplett:
  Whitelist-Bereiche im default-Fall, 16er-Grenze, Backspace
  (I_KEY_BACKSPACE in Console), Enter-Übernahme in CPlayer samt
  „Player"-Default, rote Fehlerzeile, Tipp-Cursor (ClearScreen
  versteckt den Cursor jetzt beim Szenenwechsel). Danach auf Zuruf:
  echte Tutorial- und Endszene als neue Dateipaare (Vorschau erst im
  Chat, Figlet-Schriftzüge — Kerning von Isor selbst gerichtet),
  `BuildCenteredText` in Output (zweiter Nutzer), Stubs aus main
  ausgezogen, .vcxproj um die vier Dateien ergänzt;
  Titel-Einblendung auf Isors Schnitt gestrichen (DECISIONS).
  Kommentar-Kürzungs-Pass auf Isors Urteil („sieht KI-generiert
  aus") — neue Stilregel: Inline-Kommentare höchstens zwei Zeilen.
  Voller Szenen-Rundlauf getestet, Build warnungsfrei. M1 abgehakt;
  Ist-Zeit 20 h → ZEITPLAN, Doku-Input → `ABGABE_NOTIZEN.md` (neue
  Datei, DECISIONS → „Doku-Input je Baustein"). Zwei
  Knowledge-Erweiterungen (Escape-Byte-Falle, Blacklist-Kipper).
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-09-20. Offen: M2
  beginnt mit einem Design-Abschnitt.
- 2026-09-21 — M2 B1 Lauf-Test fertig (begonnen am 20.09. abends nach
  dem Design-Abschnitt): gelieferter Baustein `ReadKeyNonBlocking` +
  `I_KEY_NONE` + `WaitMilliseconds` in Console, neues Paar
  `GameScene.h/.cpp`; Isors erste Tick-Schleife mit Drain-Eingabe
  (Flag-Muster), Wrap und Ein-Puffer-Zeichnen ab Home. Nebenbefund
  beim Test: Schachfiguren rücken nur 1 Zelle vor, die Glyphe malt
  ~1,5 (Isors Diagnose samt T-Szenen-Gegenprobe) — Zeilenbau-Regel
  gekippt, DECISIONS-Fortführung am Zeichentest-Ergebnis.
- 2026-09-25 — M2 B2 Spielfeld-Zeichner fertig (gebaut 23.–25.09. im
  Schritt-Modus): `BuildBoxBorder`/`BuildBoxTextLine` als
  Kasten-Helfer, `BuildFrame` baut den ganzen Screen als einen
  String — HUD-Kasten, zentrierte Korridore (jede Zeile schneidet
  durch alle Lanes), Spieler-Zeilen, Shop-Kasten; Sichtprüfung am
  laufenden Spiel bestanden. Isors DRY-Befund zur vierfachen
  Lane-Schleife samt eigener Begründung fürs Warten →
  ROADMAP-Aufgabe „nach M3".
- 2026-09-25 — M2 B3 Spieler fertig: `CPlayer` um den geklemmten
  Lane-Index erweitert (MoveLeft/MoveRight als Spiegel-Wächter),
  Referenz-Reise in die Szene, A/D und Pfeile als Fall-Stapel im
  Eingabe-Switch, T-Sprite gelb; Sprung-Test bestanden.
- 2026-09-26 — M2 B4 Schießen fertig und M2 abgeschlossen: `CShot`
  mit erstem eigenen Konstruktor, `std::vector` als Schuss-Beutel
  (erster Container des Projekts, als C#-List-Übersetzung gelernt),
  Leertaste spawnt auf der Spieler-Lane, Range-for-Update,
  Rückwärts-erase; `||` cyan in der Dreier-Kette der Zellen-Frage.
  Kommentar-Pass (SAE-Köpfe fürs Shot-Paar, Summaries, Header
  aktualisiert), Build /W4 grün. Ist-Zeit ~7,5 h gegen 7 geschätzt
  (Grindstone gesamt 28,37 h) → ZEITPLAN; Doku-Input →
  `ABGABE_NOTIZEN.md` → M2; M2 in der ROADMAP abgehakt. Offen: M3
  beginnt mit einem Design-Abschnitt (Gegner-Hierarchie, Spawn-Plan
  — Frage aus dem M2-Design geparkt —, new/delete,
  Figuren-Zuordnung).
- 2026-09-27 — M3 B1 Klassen fertig (nach dem M3-Design-Abschnitt vom
  selben Tag: vier DECISIONS-Einträge, Design-Seite im
  ARTIFACT_INDEX): `CEnemy` mit virtual-Destruktor und Tempo-Hook,
  `CNormalEnemy`/`CTankEnemy` als reine Startwert-Erben — das
  CEnemy-Gerüst hat Isor ungefragt selbst vorgebaut, SAE fehlerfrei.
  Platzhalter-Bauer durch ein per `new` erzeugtes Objekt ersetzt:
  Lebenszyklus delete/new am Korridor-Ende, Aufräumen vor dem
  ESC-return, `BuildFrame` liest Lane, Zeile und Figur aus dem
  Objekt. Tank-Tausch-Test bestanden — nach einer geänderten Zeile
  fiel einen Durchgang lang ein Turm, danach wieder Bauer, weil der
  zweite Geburtsort (Respawn) unverändert war: derselbe Zeiger trug
  nacheinander zwei Typen, ungeplantes Polymorphie-Experiment.
  Kommentar-Pass (SAE-Köpfe der drei neuen Paare, Summaries,
  GameScene-History), Build /W4 grün. Lern-Rubriken in
  `Kern/LERNLOG.md`. Offen in M3: B2 Liste und Spawner, B3
  Lebensenden.
- 2026-09-28 — M3 abgeschlossen (B2-Rest, Tick-Aufräumen, B3):
  Vormittag Pointer-Klärung (Wohnungs-Bild: Lebensdauer wählt den
  Wohnort; Beutel-Beschriftung in den spitzen Klammern, F12-Reflex),
  dann auf Isors eigenen Lesbarkeits-Befund den Tick in fünf
  benannte Helfer zerlegt — Isor tippte alle Extraktionen selbst,
  Königsrunde `RunSpawner` mit drei `int32_t&`-Zählern. B3
  Lebensenden: `CPlayer` um Leben erweitert (Start 20, Untergrenze
  0, RemoveLife/AddLife/GetLives — AddLife als Isors eigener
  M4-Vorgriff), Durchbruch kostet `I_BREAKTHROUGH_LIFE_COST`;
  Debugger-Abnahme bestanden (Breakpoint fünfmal, Watch 20 → 15).
  Kommentar-Pass, /W4 grün. Ist ~6,7 h gegen 10 geschätzt
  (Grindstone gesamt 35:04 h) → ZEITPLAN; Doku-Input →
  `ABGABE_NOTIZEN.md` → M3; M3 in der ROADMAP abgehakt — erste
  Unterschreitung einer Schätzung. Lern-Rubriken in
  `Kern/LERNLOG.md`. Offen: M4 beginnt mit einem Design-Abschnitt
  (Kollision, Gold, Live-Shop-Kauflogik im Tick).
- 2026-09-28 — M4 B1 und B2 gebaut (nach dem M4-Design vom selben
  Tag): B1 Spieler-Werte und HUD-Zeile — `CPlayer` um Gold, Schaden
  und Feuer-Intervall erweitert (Startwerte 0/1/4 als Konstanten,
  Getter nach dem Lives-Muster), `BuildHudText` setzt die HUD-Zeile
  je Tick live aus den Gettern zusammen (`std::to_string`),
  `BuildFrame` nimmt `const CPlayer&` statt der nackten Lane. Isor
  tippte; das Review fand die `+= int`-Doppelzeilen (char-Überladung
  hängt Steuerzeichen an → Knowledge) und den gebauten, aber nicht
  eingehängten Aufruf. Sichtprüfung bestanden, Kommentar-Pass durch.
  B2 Kollision — Belohnung als viertes Startwert-Feld im
  CEnemy-Konstruktor (Bauer 20, Turm 50; C4100 fand die vergessene
  Zuweisung), `TakeDamage`, `AddGold`; `HandleCollisions` prüft
  rückwärts über die Schüsse mit Index-Suche (−1 statt nullptr),
  Schaden zur Trefferzeit, Gold vor delete-vor-erase, Schuss immer
  verbraucht — zweimal je Tick gegen die Platztausch-Falle.
  Regler-Wechsel ab der Gegner-Suche: Claude tippte auf Zuruf
  (Energie aufgebraucht). Build /W4 grün. **Offen: B2-Abnahme
  (F5-Testbogen, Soll 130 Gold je Testlevel) und B3 Feuer-Sperre
  plus Shop-Tasten.** Lern-Rubriken in `Kern/LERNLOG.md`. Dazu
  Projektstand-Analyse: ~55 % nach Schätzgewichten, Rest realistisch
  14–18 h gegen ~8 h Regulärzeit bis Fr — Schnitt-Kontrollpunkt
  Mittwochabend (Schnittlinie 1: Skill-System).
- 2026-09-29 — M4 abgeschlossen (B2-Abnahme, B3, Feinschliff):
  Erklär-Runde zur Kollision mit Verstehens-Check (Tick-Bild,
  Treffer-Kette, klickbarer Platztausch-Stepper; Handy-Seite
  „💡 Lernstück · Tick-Kollision" im ARTIFACT_INDEX), dann
  B2-Abnahme per F5-Testbogen bestanden (Bauer +20, Turm zweistufig
  +50, Doppelschuss, Soll 130 Gold, Durchbruch kostet weiter). B3:
  Feuer-Sperre von Isor getippt (Rest-Zähler in der Szene;
  Fehlerbild unbewachter Runterzähler, Fix nach dem eigenen
  Spawner-Muster), Shop-Käufe über Isors TryRemoveGold-Idee
  (DECISIONS → „Kauf-Kette: ein Try"), dazu auf Isors Spieltest-
  Befunde Kauf-Sound und AtkSpeed als hochzählende Stufe
  (DECISIONS → „Shop-Feedback"). Zweimal die VS-Puffer-Falle in
  Gegenrichtung (alter Puffer überschrieb frische Platte) —
  Knowledge-Seite erweitert. Builds über MSBuild, /W4 grün,
  Kommentar-Pass durch. Ist ~6 h gegen 8 h geschätzt (Grindstone
  gesamt 41:27 h) → ZEITPLAN; Doku-Input → `ABGABE_NOTIZEN.md` →
  M4; M4 in der ROADMAP abgehakt — zweite Unterschreitung in Folge.
  Lern-Rubriken in `Kern/LERNLOG.md`. Drei Knowledge-Seiten
  (Try-Muster neu, Tick-Kollision und Editor-Wahrheit erweitert).
  Offen: M5 beginnt mit einem Design-Abschnitt (Boss,
  Multishot-Wirkung, polymorpher Skill-Slot); Polish-Liste vom
  29.09. als ROADMAP-Aufgabe (Sounds, HUD-Farben, Tutorial,
  Datei-für-Datei-Durchgang mit Refactoring).
