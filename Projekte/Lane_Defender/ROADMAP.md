# ROADMAP.md — Bauplan Lane Defender

Ownership: Nur was an Lane Defender als Nächstes gelernt oder gebaut
wird — Lern-Vorlauf, Meilensteine, Ausbauten, offene Aufgaben. Warum das
Projekt so geschnitten ist, steht in den DECISIONS dieser Schicht; die
Zeitschätzung je Meilenstein im ZEITPLAN; was passiert ist, im LOG.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

## Lern-Vorlauf — Sandbox, parallel zum Unterrichtsstart

- [x] **L1 · Werkzeug** — VS-2022-C++-Workload prüfen bzw. installieren,
  erstes Projekt anlegen, kompilieren, Debugger starten; Unterschied zu
  C#/Unity (nativ kompiliert, kein Runtime). **Erledigt am 2026-09-09:**
  Workload war seit dem 2026-09-08 verifiziert (VS 2026); Projekt
  `LaneDefender` angelegt, kompiliert, Debugger mit Breakpoint und
  Locals benutzt, Theorie-Happen am eigenen Build (65,5 KB gegen
  119,2 MB Unity). Beleg: Commit `Update V 0.0002` im Code-Repo und
  `Kern/LERNLOG.md`, 2026-09-09.
- [x] **L2 · Syntax-Umzug** — Typen, `if`/`for`/`while`, Funktionen,
  `cin`/`cout` mit Eingabe-Validierung; Mini-Snippets in `Sandbox/`.
  **Stand 2026-09-09:** Ü1 Typen und Ü2 Kontrollfluss erledigt — als
  Runden-Spielschleife mit Guard Clause und SAE-Konstanten direkt in
  `LaneDefender.cpp`, Commit `Update V 0.0003` im Code-Repo. Offen: Ü3
  Funktionen, Ü4 Eingabe-Validierung.
  **Stand 2026-09-11:** Ü3 Funktionen erledigt — PrintMessage-Überladungen
  und LoseLives am Spielcode, Beleg im LOG dieser Schicht und in
  `Kern/LERNLOG.md`; die Verkürzungsfrage aus der PLAN-Übergabe hat Isor
  mit „Ü3/Ü4 voll statt verschmolzen" entschieden. Offen: nur noch Ü4
  Eingabe-Validierung — dort läuft die Testreihe `abc`/`-3`/`0`/`5` am
  eigenen Code.
  **Erledigt am 2026-09-12:** Ü4 Eingabe-Validierung am Spielcode —
  `ReadValueInput` mit fail/clear/ignore und Bereichsprüfung, Testreihe
  `abc`/`-3`/`0`/`5` bestanden. Beleg: LOG dieser Schicht und
  `Kern/LERNLOG.md`, je 2026-09-12. Damit ist L2 komplett.
- [x] **L3 · Werte, Pointer, Speicher** — Wertsemantik gegen
  C#-Referenzen, Stack und Heap, `&`, `*`, `nullptr`, `const&`;
  Adressen als echte Zahlen im Debugger ansehen.
  **Erledigt am 2026-09-12:** Ü1 Adressen im Debugger (Watch,
  Call-Stack-Frames), Ü2 Pointer-Snippet in main (nach Abnahme
  entfernt), Ü3 const-Referenzen an der PrintMessage-Familie. Beleg:
  LOG dieser Schicht und `Kern/LERNLOG.md`, je 2026-09-12. Der
  Lern-Vorlauf L1–L3 ist damit komplett; als Nächstes M1.

## Meilensteine — Schätzung und Ist-Zeiten im ZEITPLAN

Zielfenster aus der Semester-Roadmap
(`Uni/ROADMAP.md` → „Der Phasenplan — beschlossen am 2026-09-08"),
seit dem 2026-09-14 mit den echten Terminen: **Fertig-Ziel So 27.09.**,
Abgabe **Fr 02.10., 23:59** (`Uni/Semester_3/STUNDENPLAN.md`), die
Abgabewoche ist nur Feinschliff. Isors Streckziel: wenn möglich schon
So 20.09. fertig — dann beginnt der Model-Viewer eine Woche früher.

- [x] **M1 · Gerüst** — Konsolen-Init (Farben, Sonderzeichen,
  Cursor-Home) samt Zeichentest der Symbol-Kandidaten, Hauptmenü mit
  Titel, Start/Exit, Namenseingabe mit Validierung.
  **Ausdesignt am 2026-09-12** (acht Einträge in den DECISIONS dieser
  Schicht): Szenen-Zustandsautomat mit sechs Stationen,
  Steuerungs-Szene vor jedem Spielstart, Endszenen-Hülle, Menü-Buttons
  mit Marker `>`, Titel in Linien-Schrift mit Start-Einblendung,
  VT-Escape-Technik, Zeichentest hinter versteckter Taste `T`.
  **Stand 2026-09-12 (Development):** `Console.h`/`Console.cpp`
  gebaut, eingebunden und nach Verstehens-Runde abgenommen (Umbau auf
  ausgeschriebene Schritte, /W4-warnungsfrei). Nächster Schritt:
  Zeichentest tippen nach `Sandbox/M1_Zeichentest_Aufgabe.txt` samt
  Testreihe in zwei Terminals; danach Zustandsautomat → Menü. Die
  Ist-Zeit läuft über Isors Grindstone-Tracking (~3,5 h inkl. Design).
  **Stand 2026-09-13:** Zeichentest-Szene gebaut und gemessen (26 von
  30 rasterfest; Schachfiguren doppelbreit und als Figuren-Symbole
  gesetzt — DECISIONS dieser Schicht), Ausgabe-Helfer in
  `Output.h`/`Output.cpp`, `/utf-8` gesetzt.
  **Stand 2026-09-13 (Abend):** Szenen-Zustandsautomat fertig —
  Melde-Muster, sechs Stationen im Kreis, Exit, Symbol-Test als
  Zustand (DECISIONS → „Szenen melden die nächste Szene"). Offen in
  M1: das echte Hauptmenü (Linien-Titel, umrahmte Buttons,
  Pfeil/W-S-Auswahl, Tasten `T` und `ESC`), echte Namenseingabe
  (getline samt Namensregeln), echte Endszene mit Name und Level.
  M1-Ist-Zeit: 10:22 h (Grindstone).
  **Stand 2026-09-18:** Hauptmenü-Frame fertig — Titel und
  Start/Exit-Buttons in Linien-Schrift, blockzentriert auf
  `I_SCREEN_WIDTH` 120, Szene in `MainMenu.h`/`.cpp` (drei Einträge
  vom 18.09. in den DECISIONS dieser Schicht), /W4-warnungsfrei.
  Offen in M1: Auswahl-Schleife (Auswahl-Zahl, Marker im Frame,
  Home-Frame-Schleife, Pfeile/W/S, Enter, `ESC`, `T`),
  Titel-Einblendung, echte Namenseingabe, echte Endszene.
  **Stand 2026-09-19:** Auswahl-Schleife fertig — Zahl-Zustand mit
  Umlauf, Home-Frame-Druck bei konstanter Höhe, Balken+Farbe als
  Marker und Sound-Feedback (DECISIONS dieser Schicht →
  „Marker-Optik" und „Sound als freie Funktionen", je 19.09.),
  Review-Pass und /W4-Build grün, Beleg im LOG. Offen in M1:
  Titel-Einblendung, echte Namenseingabe (Design-Abschnitt am
  19.09. begonnen), echte Endszene.
  **Ausdesignt 2026-09-19 (Namenseingabe):** Dialogfenster mit
  Unterstrich-Slots, freies Fokus-Modell, Eingabe selbst gezeichnet
  statt getline, Farbsprache Gelb/Hellrot — drei DECISIONS-Einträge
  vom 19.09. Offen bleibt die Umsetzung, dazu Titel-Einblendung und
  Endszene.
  **Stand 2026-09-19 (Abend):** Statischer Namenseingabe-Screen
  gebaut — Dialogfenster mit Verteiler über fensterrelative
  Konstanten, Regeln, Schreiblinie unter der Tippzeile,
  Back/Confirm-Zeile (DECISIONS → „Namenseingabe-Feinschliff");
  `SetCursorPosition` und `S_COLOR_RED` in Console; /W4 grün.
  **Sichtprüfung von Schreiblinie und Button-Zeile steht aus —
  erster Handgriff der nächsten Session.** Offen in M1: die
  Zeichen-Schleife der Namenseingabe (Fokus-Modell, Whitelist,
  Backspace, Farben, Marker), Titel-Einblendung, echte Endszene.
  **Stand 2026-09-19 (zweite Session):** Sichtprüfung bestanden;
  Steuerungs-Teil der Zeichen-Schleife fertig — Fokus-Verzweigung
  Feld/Buttons mit direkten Übergängen (DECISIONS → „Enter ist der
  einzige Ausgang"), `CPlayer` angelegt und als Referenz verdrahtet
  (DECISIONS → „Mini-Player-Klasse"), `I_SELECTION_CONFIRM`, Header
  entrümpelt; Rundgang-Test bestanden, /W4 grün bis auf die bewusst
  offene C4100 (`a_player` unbenutzt bis zur Zeichen-Aufnahme).
  Offen in M1: Färbung (Buttons und Feld), Zeichen-Aufnahme
  (Whitelist, Backspace, 17. Zeichen, Fehlerzeile),
  Titel-Einblendung, echte Endszene.
  **Erledigt am 2026-09-20:** Zeichen-Aufnahme komplett (Whitelist,
  Backspace, Enter-Übernahme in CPlayer, rote Fehlerzeile,
  Tipp-Cursor), Feld- und Button-Färbung, echte Tutorial- und
  Endszene als eigene Dateipaare (Figlet-Schriftzüge,
  `BuildCenteredText` in Output), Titel-Einblendung gestrichen
  (DECISIONS, 20.09.). Warnstufe real auf /W4 gehoben und
  warnungsfrei (`Kern/STOERUNGEN.md`, 20.09.), voller
  Szenen-Rundlauf getestet. Ist-Zeit im ZEITPLAN (20 h gegen 6 h);
  Doku-Input in `ABGABE_NOTIZEN.md`, Abgabetext folgt am
  Projektende.
- [x] **M2 · Lanes und Spieler** — Spielfeld mit Lanes zeichnen
  (nur rastergeprüfte Zeichen), Player-Klasse, Lane-Wechsel und
  Schießen über die nicht-blockierende Tastenabfrage (gelieferter
  Baustein).
  **Ausdesignt am 2026-09-20** (sieben Einträge in den DECISIONS
  dieser Schicht): Screen „Gerahmt" mit HUD-Kasten oben, Live-Shop
  unten und getrennten Korridoren (innen 8, Lücke 6);
  Sprung-Modell (Position = Lane-Index, geklemmt);
  Lane-Progression 2/3/4 an den Boss-Siegen; Sprite Lauf 2 über
  Sockel 6 in Gelb; Schuss `||` cyan; kbhit-Wächter samt
  Tick-Reihenfolge. Design-Seite:
  https://claude.ai/artifact/FbqHW5wq6Ay2szchXe7R3j — offen ist
  der Bau, Einstieg über den Lauf-Test (Beschluss vom 12.09.).
  **Stand 2026-09-21:** B1 Lauf-Test bestanden — Tick-Schleife mit
  Drain-Eingabe und Ein-Puffer-Zeichnen, von Isor getippt
  (`GameScene.h/.cpp`). Nebenbefund: Schachfiguren rücken nur
  1 Zelle vor, die Glyphe malt ~1,5 Zellen in die Nachbarzelle
  (DECISIONS → Fortführung am Zeichentest-Ergebnis) — der
  B2-Zeilenbauer zählt Figuren als 1 Spalte mit Pflicht-Luftzelle
  rechts. Offen:
  B2 Spielfeld-Zeichner, B3 Spieler, B4 Schießen.
  **Stand 2026-09-25:** B2 Spielfeld-Zeichner fertig — `BuildFrame`
  baut den kompletten Screen als einen String (HUD-Kasten,
  zentrierte Korridore je Lane-Zahl, Spieler-Zeilen, Shop-Kasten),
  von Isor im Schritt-Modus getippt, Sichtprüfung am laufenden
  Spiel bestanden (nichts wandert, Hämmer-Test ruhig, ESC sauber).
  Offen: B3 Spieler (Lane-Index in CPlayer, Sprung-Eingabe, Gelb),
  B4 Schießen.
  **Stand 2026-09-25 (Abend):** B3 Spieler fertig — `CPlayer` um
  `m_iCurrentLane` mit MoveLeft/MoveRight samt Klemm-Wächtern
  erweitert, Referenz-Reise in die Szene, A/D und Pfeile als
  Fall-Stapel im Eingabe-Switch, T-Sprite gelb; Sprung-Test
  bestanden (springt sofort, klemmt beidseitig, Bauer läuft
  ungestört). Offen in M2: nur noch B4 Schießen.
  **Stand 2026-09-26:** B4 Schießen fertig — `CShot` mit
  Konstruktor als eigenes Dateipaar, `std::vector<CShot>` als
  Beutel in der Szene (erster Container des Projekts, als
  C#-List-Übersetzung gelernt), Leertaste spawnt auf der
  Spieler-Lane, Update mit Range-for und Rückwärts-erase,
  Zellen-Frage in BuildFrame als Dreier-Kette, `||` cyan.
  F5-Test bestanden (mehrere Schüsse gleichzeitig, sauberes
  Verschwinden an der Kappe). **M2 ist gebaut und geprüft** —
  offen für den Haken: Kommentar-Nachtrag (Claude) und der
  Doku-Input in `ABGABE_NOTIZEN.md` samt Ist-Zeit (Grindstone).
  **Erledigt am 2026-09-26:** Kommentar-Nachtrag durch (SAE-Köpfe
  und Summaries, Build /W4 grün), Doku-Input steht in
  `ABGABE_NOTIZEN.md` → M2, Ist-Zeit ~7,5 h gegen 7 h im ZEITPLAN
  — gebaut, geprüft und dokumentiert, der Baustein ist fertig.
- [x] **M3 · Gegner** — Basisklasse plus Tank/Runner (Vererbung,
  `virtual`), Spawn-Plan je Lane, Abwärtslauf per Tick, Durchbruch
  kostet Leben; `new`/`delete` für Spawn und Tod.
  **Ausdesignt am 2026-09-27** (vier Einträge in den DECISIONS
  dieser Schicht): Gegner-Hierarchie Normal/Tank/Boss unter
  `CEnemy` — der Runner entfällt als Typ, Tempo wird globaler
  Level-Wert als Schrittintervall in Ticks, nur der Boss
  überschreibt es (Bau in M5, Design steht); Spawn-Plan als
  Level-Budget aus der 15-Zeilen-Tabelle (fester Abstand,
  Lane-Würfel mit Belegt-Wächter, Typ per Rest-Wahrscheinlichkeit,
  Durchbruch = 1 Leben ab); Speicher als `vector<CEnemy*>` mit
  `new` im Spawner und `delete` an den drei Lebensenden samt
  Aufräum-Schleife; Figuren ♟/♜/♚, ♞ Reserve. Design-Seite:
  https://claude.ai/artifact/FMZX3wJ2Lh43GpvpyXccK4 — offen ist
  der Bau: B1 Klassen, B2 Liste und Spawner, B3 Lebensenden.
  **Stand 2026-09-27, gleicher Tag:** B1 Klassen fertig — `CEnemy`
  mit virtual-Destruktor und Tempo-Hook, `CNormalEnemy` (1 Leben,
  ♟) und `CTankEnemy` (2 Leben, ♜) als reine Startwert-Erben, von
  Isor getippt (das CEnemy-Gerüst ungefragt selbst vorgebaut). Der
  Platzhalter-Bauer läuft jetzt als per `new` erzeugtes Objekt:
  Lebenszyklus delete/new am Korridor-Ende, Aufräumen vor dem
  ESC-return, `BuildFrame` liest Lane, Zeile und Figur aus dem
  Objekt. Tank-Tausch-Test bestanden (eine geänderte Zeile — der
  Turm fällt, ohne dass Szene oder Zeichner Türme kennen);
  Kommentar-Pass durch, /W4 grün. Offen: B2, B3.
  **Stand 2026-09-27, weiter:** B2 Liste und Spawner fertig — Gegner
  leben als `vector<CEnemy*>` (Bewegung, Entsorgung mit delete vor
  erase, ESC-Aufräum-Schleife, BuildFrame sucht je Zelle mit dem
  nullptr-Muster), Schrittintervall läuft über den virtual-Hook
  (Tick-Zähler, 0,6 s je Zeile), Spawner nach Tafel 2 mit den
  Zeile-1-Konstanten (Budget 5 · 1 Tank · Abstand 10 Ticks),
  `srand`-Saat einmal in main. Fünf-Punkte-Testbogen bestanden.
  Regler seit Mitte B2 auf Zuruf: Claude tippt, Isor liest gegen
  (Abgabedruck). Offen: B3 Lebensenden — der Durchbruch kostet noch
  kein Leben.
  **Stand 2026-09-28:** Vormittags auf Isors eigenen Befund („jeder
  Block sollte heißen, was er macht") den Tick in fünf benannte
  Helfer zerlegt — MoveEnemies, RemoveFinishedEnemies, RunSpawner
  (drei `int32_t&`-Zähler), MoveShots, RemoveFinishedShots; Isor
  tippt wieder selbst. Danach B3 Lebensenden fertig: `CPlayer` um
  Leben erweitert (Start 20, Untergrenze 0, RemoveLife/AddLife/
  GetLives — AddLife als Isors eigener M4-Shop-Vorgriff), Durchbruch
  kostet `I_BREAKTHROUGH_LIFE_COST` über die neue CPlayer-Tür der
  Entsorgungs-Funktion. Debugger-Abnahme bestanden (Breakpoint 5×,
  Watch 20 → 15), Kommentar-Pass durch, /W4 grün. **M3 ist gebaut
  und geprüft** — offen für den Haken: Doku-Input in
  `ABGABE_NOTIZEN.md` samt Ist-Zeit (Grindstone).
  **Erledigt am 2026-09-28:** Doku-Input steht in
  `ABGABE_NOTIZEN.md` → M3, Ist-Zeit ~6,7 h gegen 10 h im ZEITPLAN
  (erste Unterschreitung einer Schätzung) — gebaut, geprüft und
  dokumentiert, der Meilenstein ist fertig.
- [x] **M4 · Kampf und Upgrades** — Kollision Schuss/Gegner (gleiche
  Lane, gleiche Zeile), Gold, Upgrade-Screen zwischen den Leveln
  (Schaden, Feuerrate).
  **Stand 2026-09-20 (M2-Design):** Der Upgrade-Screen ist durch
  den Live-Shop ersetzt (DECISIONS → „Live-Shop: Kaufen mitten im
  Lauf") — M4 baut Kollision, Gold und die Kauf-Logik im Tick.
  **Ausdesignt am 2026-09-28** (vier Einträge in den DECISIONS
  dieser Schicht): Kollision als eine Prüf-Funktion zweimal je
  Tick (Durchtunnel-Falle beidseitig dicht), Schaden zur
  Trefferzeit vom Spieler; Feuer-Sperre in Ticks (Start 4, Kauf −1
  bis Minimum 1, geschluckt statt bestraft); Gold 20/50 als
  Erben-Startwert, Start-Gold 0, Start-Schaden 1, Preise mit
  Wirkungen, [4] bis M5 gesperrt; HUD-Werte-Zeile nach M4
  vorgezogen. Design-Seite:
  https://claude.ai/artifact/7Dp5vCLrjoh7YCtneSoBut — offen ist
  der Bau: B1 Spieler-Werte und HUD-Zeile, B2 Kollision, B3
  Feuer-Sperre und Shop-Tasten.
  **Stand 2026-09-28 (Abend):** B1 fertig — Gold/Schaden/
  Feuer-Intervall in `CPlayer` (0/1/4), `BuildHudText` live je Tick,
  `BuildFrame` nimmt `const CPlayer&`; Sichtprüfung bestanden,
  Kommentar-Pass durch. B2 gebaut — Belohnung als viertes
  Startwert-Feld (20/50), `TakeDamage`, `AddGold`,
  `HandleCollisions` zweimal je Tick (Index-Suche, Schaden zur
  Trefferzeit, Gold vor delete); ab der Gegner-Suche tippte Claude
  auf Zuruf. /W4 grün. **Offen: B2-Abnahme per F5-Testbogen (Bauer
  +20, Turm zweistufig +50, Doppelschuss, Soll 130 Gold je
  Testlevel, Durchbruch kostet weiter) — erster Handgriff der
  nächsten Session —, danach B3.**
  **Stand 2026-09-29:** B2-Abnahme bestanden — Erklär-Runde zur
  Kollision mit Verstehens-Check (Handy-Seite:
  https://claude.ai/artifact/VavXTzq3k7XjqsaaXm2QD9), dann der
  F5-Testbogen komplett: Bauer +20, Turm zweistufig +50,
  Doppelschuss +50, Soll 130 im HUD, Durchbruch kostet weiter.
  Offen in M4: B3 Feuer-Sperre und Shop-Tasten.
  **Stand 2026-09-29 (weiter):** B3 fertig — Feuer-Sperre (Zähler
  in der Szene, geschluckt statt bestraft) von Isor getippt,
  Shop-Tasten über Isors TryRemoveGold-Muster, dazu Kauf-Sound und
  AtkSpeed als hochzählende Stufe nach Isors Befunden (DECISIONS,
  29.09.); alle F5-Tests bestanden, /W4 grün, Kommentar-Pass durch.
  **M4 ist gebaut und geprüft** — offen für den Haken: Doku-Input
  in `ABGABE_NOTIZEN.md` samt Ist-Zeit (Grindstone).
  **Erledigt am 2026-09-29:** Doku-Input steht in
  `ABGABE_NOTIZEN.md` → M4, Ist-Zeit ~6 h gegen 8 h im ZEITPLAN —
  gebaut, geprüft und dokumentiert, der Meilenstein ist fertig.
- [ ] **M5 · Boss und Skills** — Boss-Klasse (belegt eine Lane, die
  übrigen spawnen normal weiter), Skill-Wahl beim ersten Boss-Sieg,
  Spezialattacken Doppel-Lane und Durchschlag als Klassen am
  polymorphen Skill-Slot, Skill-Stufen durch weitere Boss-Siege.
  **Stand 2026-09-20 (M2-Design):** Erstmal genau ein Skill
  (Multishot), per Shop-Kauf statt Boss-Freischaltung (DECISIONS →
  „Live-Shop"); der polymorphe Slot bleibt M5-Thema, Wirkung und
  Stufen klärt der M5-Design-Moment.
  **Ausdesignt am 2026-09-30** (sechs Einträge in den DECISIONS
  dieser Schicht): Boss mit zufälliger Lane, Durchbruch −5 Leben,
  Verdoppler-Gold 500/1000/2000, die Boss-Runde zählt auch bei
  Durchbruch; Multishot feuert auf der rechten Nachbar-Lane mit
  (rechts außen fällt der Zusatzschuss weg), keine Skill-Stufen;
  der Slot als Entweder-oder — `CSkill` abstrakt mit rein-virtuellem
  `Fire`, `m_pSkill` in `CPlayer`, der Skill besitzt den ganzen
  Schuss; [4]-Kette nach dem Try-Muster samt delete im ersten
  Destruktor (`~CPlayer`); schmale Balance-Datei wird in B1
  angelegt. Design-Seite:
  https://claude.ai/artifact/Gmwkzh85XeR8AEHnFqDrgh — offen ist
  der Bau: B1 Boss, B2 Skill-System; Schnittlinie 1 („Skill fällt,
  Bosse bleiben") liegt exakt zwischen den beiden.
  **Stand 2026-09-30 (Abend):** B1 Boss fertig — CBoss als
  Startwert-Erbe mit dem ersten Override des Projekts (Tempo
  6 Ticks), Boss-Spawn zu Levelbeginn (zufällige Lane,
  Test-Konstante, Sperr-Wächter im Spawner), Durchbruch-Kosten als
  fünftes Startwert-Feld (DECISIONS, 30.09.), Balance.h angelegt;
  F5-Testbogen bestanden, /W4 grün, Kommentar-Pass durch. Offen:
  B2 Skill-System — **Fallbeil Donnerstagabend**, danach greift
  Schnittlinie 1 ohne neue Diskussion.
- [ ] **M6 · Level-Lauf** — 15 Level, Lane-Progression im
  Dreier-Raster, Skalierung je Level, Sieg nach dem dritten Boss,
  Niederlage bei 0 Leben, HUD.
  **Stand 2026-09-20 (M2-Design):** Die Progression läuft 2/3/4 an
  den Boss-Siegen von Level 5 und 10 statt im Dreier-Raster
  (DECISIONS → „Lane-Progression 2/3/4 an den Boss-Siegen").
- [ ] **M7 · Abgabe-Polish** — Eingaben härten, Konventions-Pass,
  Leak-Kontrolle, Build, README.

## Ausbauten — nur bei Zeitreserve, Reihenfolge in den DECISIONS
(„Schnittlinien Lane Defender")

- [ ] **A1 · Dritter Gegnertyp**
- [ ] **A2 · Endlos-Modus mit Highscore-Liste**
- [ ] **A3 · Dritte Skill-Stufe**
- [ ] **A4 · raylib-Anzeige als Kür**
- [ ] **A5 · Leaderboard mit Datei-Speicherung** — Isors Wunsch vom
  2026-09-30; Entscheidung bewusst erst nach dem M7-Polish, weil
  Datei-Schreiben (Streams, Fehlerfälle) ein neues Thema ohne
  Pflichtthema-Bezug ist. Verwandt mit A2, das die Highscore-Liste
  schon führt.

## Aufgaben

- [x] **Code-Ablage festlegen** — beim L1-Setup entscheiden, wo das
  VS-Projekt liegt (eigenes Repo bzw. die Abgabe-Struktur der
  Uni-Schicht); die Sandbox-Snippets liegen wie beim Python-Lesekurs in
  dieser Schicht. **Erledigt am 2026-09-08:** eigenes Repo, Begründung
  in den DECISIONS („2026-09-08 — Eigenes Code-Repo neben den
  anderen"); Repo mit .gitignore und README angelegt, Marke
  `PROJEKT_LANE_DEFENDER` in `Kern/PFADE.md`, L1-Anleitung in
  `Sandbox/L1_Setup_Anleitung.txt`.
- [ ] **Symbole final wählen** — beim Bau von M2/M3, ausschließlich
  Zeichen, die den Raster-Test bestehen (DECISIONS →
  „Raster-Stabilität vor Schmuck"). Kandidaten für den M1-Zeichentest,
  je Rolle in Vorschlagsreihenfolge (Claude, 2026-09-08): Spieler `A`
  `@` `^` · Schuss `|` `*` `!` · Runner `o` `v` `w` · Tank `#` `O` `T`
  · Boss `M` `W` `B` · Rahmen und Lane-Trenner `│` `─` `┌` `┐` `└` `┘`
  mit ASCII-Rückfall `|` `-` `+` · HUD-Balken `█` `▓` `░` mit Rückfall
  `=`. **Ergänzt 2026-09-13 (Isor):** die Schachfiguren als
  Wunsch-Kandidaten vor den ASCII-Rückfällen — Runner `♟` `♞`, Tank
  `♜`, Boss `♚`. **Stand nach dem Zeichentest (2026-09-13):** Die
  Figuren-Symbole sind entschieden — Schachfiguren, fest doppelbreit
  (DECISIONS → „Schachfiguren gesetzt"); ASCII bleibt Rückfall für
  fremde Terminals. Offen wählt M2/M3 nur noch aus den Bestandenen:
  Schuss (`|` `*` `!`), Rahmen (`│ ─ ┌ ┐ └ ┘`), HUD (`█ ▓ ░`, dazu
  `▀ ▄`).
  **Stand 2026-09-20 (M2-Design):** Schuss `||` und die
  Rahmenzeichen sind entschieden (DECISIONS → „Schuss-Symbol: ||
  in Cyan" und „M2-Screen"), `**` als Treffer-Blitz-Kandidat für
  M4 gemerkt. Offen nur noch: Figuren-Zuordnung je Gegnertyp (M3)
  und die HUD-Balken (M6).
  **Stand 2026-09-27 (M3-Design):** Die Figuren-Zuordnung ist final
  — Normal ♟, Tank ♜, Boss ♚, ♞ Reserve für A1 (DECISIONS →
  „Figuren-Zuordnung final"). Offen nur noch die HUD-Balken (M6).
- [x] **Spieler als zusammengesetztes Sprite prüfen** — Isors Idee vom
  2026-09-13: die Spielfigur aus mehreren Einzelzeichen statt einem
  Symbol; Skizze vom selben Tag: T-Form mit breitem Sockel und
  schmalem Lauf oben („sieht aus wie etwas, das schießt" — der Schuss
  startet aus der Lauf-Spalte). Gehört in den M2-Design-Abschnitt
  (Spielfeld und Player-Klasse); die Bausteine — Linien, Ecken,
  Voll- und Halbblöcke `▀` `▄` — laufen als Bewerber im
  M1-Zeichentest mit.
  **Erledigt am 2026-09-20:** T-Form gewählt und ausgemessen —
  Lauf 2 Spalten über Sockel 6, massiv aus `█`, gelb (DECISIONS →
  „Spieler-Sprite: T-Form massiv, Lauf 2, Sockel 6").
- [x] **Lane-Layout für die Doppelbreit-Figuren ausgestalten** — die
  Richtung ist beschlossen (DECISIONS → „Schachfiguren gesetzt",
  2026-09-13): Lane = Wand + vier Leerzellen + Wand, Figur auf fester
  Mittelposition, Schuss zwei Zellen breit. Der M2-Design-Abschnitt
  gestaltet nur noch aus: exakte Zellrechnung je Zeile,
  Sonderbreiten-Logik beim Zeilenbau, Zusammenspiel mit der
  Doppelzellbreite aus dem Tick-Beschluss.
  **Erledigt am 2026-09-20:** Korridore innen 8 mit fester
  Mittelposition, gespeichert wird nur (Lane, Zeile), der
  Zeilenbauer bucht Figuren als 2 Spalten (DECISIONS → „M2-Screen:
  Design ‚Gerahmt' mit getrennten Korridoren").
- [ ] **Auswahl-Mechanik als wiederverwendbaren Baustein prüfen** —
  Isors Gedanke vom 2026-09-13 beim Automaten-Bau: Die Listen-Auswahl
  (Pfeile/W+S, Marker, Enter) so schneiden, dass mehrere Szenen sie
  nutzen können — Hauptmenü, Bestätigung der Namenseingabe, später der
  M4-Upgrade-Screen. Entscheidet der Design-Moment des
  Menü-Bausteins; YAGNI-Regel der CODE_GUIDELINES gilt (Abstraktion
  beim zweiten konkreten Nutzer).
  **Stand 2026-09-19:** Der zweite Nutzer (Back/Confirm der
  Namenseingabe) ist waagerecht und textbasiert — entschieden:
  Kopie, keine Abstraktion (DECISIONS → „Eingabe selbst gezeichnet",
  Verworfen-Teil). Die Frage stellt sich neu beim dritten Nutzer,
  dem M4-Upgrade-Screen.
  **Stand 2026-09-28 (M4-Design):** Der dritte Nutzer ist
  gegenstandslos — der Live-Shop kauft per Zifferntaste, ohne
  Listen-Auswahl. Die Frage ruht, bis ein echter dritter Nutzer
  auftaucht.
- [ ] **Design gegen die Original-Aufgabe halten**, sobald die echten
  Semester-3-Texte vorliegen. Grundlage bisher:
  `Uni/Semester_3/VORJAHR_AUFGABEN.md` → „1 · C++ Konsolenprojekt".
- [ ] **getline-Härtung bei M1/M7 prüfen** — zeilenweises Lesen
  (`getline` plus Parsen) statt `cin >>` für die Menü-Eingaben: fängt
  auch leere und Leerzeichen-Eingaben und räumt das liegengebliebene
  `\n` ab. Anlass und Abwägung: DECISIONS dieser Schicht →
  „2026-09-12 — Leere Eingabe bleibt stilles Warten".
  **Stand 2026-09-12 (M1-Design):** für M1 entschieden — die
  Namenseingabe liest per `getline` (DECISIONS → „Namensregeln der
  Namenseingabe"), und die Menüs brauchen keine `cin >>`-Eingabe mehr
  (Einzeltasten-Bedienung). Offen bleibt der M7-Check, ob im übrigen
  Code formatiertes Lesen übrig ist.
  **Stand 2026-09-19:** Der M1-Teil ist gegenstandslos — die
  Namenseingabe zeichnet selbst statt getline zu lesen (DECISIONS →
  „Eingabe selbst gezeichnet"), im Projekt bleibt damit gar kein
  `cin` übrig. Offen nur noch der M7-Scan als Kontrolle.
- [ ] **Farbsprache der Dozentin vorlegen** — bei Abgabe oder
  Präsentation fragen, ob Gelb/Hellrot für sie passt (Isor, 2026-09-19:
  Gelb bestätigt; Grün verworfen — Rot-Grün-Paar mit der Fehlerfarbe,
  Beleg in der Session). Falls sie anderes will: Umfärben ist eine
  Ein-Zeilen-Änderung an den Bedeutungs-Konstanten; ein Farb-Setting
  im Spiel wäre ein eigener kleiner Ausbau. Kein Handlungsbedarf vorher.
- [ ] **Fenster-Wächter prüfen** — Konsolengröße beim Start abfragen
  und bei zu kleinem Fenster freundlich um Vergrößern bitten; bis
  dahin gilt die Fensterregel „Standardgröße 120×30 oder größer".
  Anlass: der Scroll-Salat vom 2026-09-19 — der Menü-Frame füllte
  mit dem Extra-`\n` exakt die 30 Terminal-Zeilen, und jedes
  Überschreiten des unteren Rands versetzt alle Folge-Frames.
  Gehört ins M7-Umfeld (Härten).
- [ ] **Zeilen-Schleifen in BuildFrame DRY-en** — Isors Befund vom
  2026-09-25 nach der B2-Abnahme: die innere Lane-Schleife steht
  viermal fast identisch da (Kappe, Körper, Barrel, Base).
  Bewusst zurückgestellt (Isor, gleiche Session): B4 bringt
  Schuss+Gegner in derselben Zeile, M3 macht aus der Zellen-Frage
  einen Daten-Lookup — erst wenn das Muster stillsteht, wird
  einmal richtig abstrahiert. Fällig nach M3.
- [ ] **Polish-Liste vom 2026-09-29** — Isors Befunde nach dem
  M4-Spieltest, gehören ins M7-Umfeld: Schuss-Sound und Sterbe-Sound
  ergänzen, alle Sounds aufeinander abstimmen (unterscheidbar
  machen); Tutorial-Szene polieren; HUD-Farben (z. B. Gold gelb,
  Leben eigen — oder nur die Zahlen hervorheben, entscheidet der
  Polish-Moment); Shop-Zeile: nicht bezahlbare Posten rot statt
  weiß.
  **Ergänzt 2026-09-30 (M5-Test):** Nahbereichs-Schüsse sind
  unsichtbar — steht der Gegner nah am Lauf, entsteht der Schuss,
  trifft und verschwindet im selben Tick, bevor er je gezeichnet
  wird; der Schaden stimmt, nur das Auge geht leer aus.
  Gegenmittel-Kandidaten: der seit M4 geparkte Treffer-Blitz `**`
  und der Schuss-Sound aus dieser Liste. Kein Layout-Problem — die
  Korridorlänge ist nicht die Ursache.
  **Ergänzt 2026-09-30 (Zeugnis):** Vokabel-Runde fürs
  Prüfungsgespräch — Zeiger, Referenz, abstrakte Klasse und
  override laut erklären; Befund des Zeugnisses vom 30.09. (die
  Begriffe sind sortiert, aber noch nicht prüfungsfest). Dazu als Abschluss der **Datei-für-Datei-Durchgang**: Isor
  erklärt jede Datei, Claude vertieft, gemeinsames Refactoring auf
  Lesbarkeit — Isor bestimmt, was und wie umgebaut wird; der
  ausführliche Erklärstil bleibt.
