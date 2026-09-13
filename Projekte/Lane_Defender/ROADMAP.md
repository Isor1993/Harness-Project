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

Zielfenster aus der Semester-Roadmap, beschlossen am 2026-09-08:
abgabefertig bis ~05.10., vor dem geschätzten Uni-Termin ~15.10.
(`Uni/ROADMAP.md` → „Der Phasenplan — beschlossen am 2026-09-08").

- [ ] **M1 · Gerüst** — Konsolen-Init (Farben, Sonderzeichen,
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
- [ ] **M2 · Lanes und Spieler** — Spielfeld mit Lanes zeichnen
  (nur rastergeprüfte Zeichen), Player-Klasse, Lane-Wechsel und
  Schießen über die nicht-blockierende Tastenabfrage (gelieferter
  Baustein).
- [ ] **M3 · Gegner** — Basisklasse plus Tank/Runner (Vererbung,
  `virtual`), Spawn-Plan je Lane, Abwärtslauf per Tick, Durchbruch
  kostet Leben; `new`/`delete` für Spawn und Tod.
- [ ] **M4 · Kampf und Upgrades** — Kollision Schuss/Gegner (gleiche
  Lane, gleiche Zeile), Gold, Upgrade-Screen zwischen den Leveln
  (Schaden, Feuerrate).
- [ ] **M5 · Boss und Skills** — Boss-Klasse (belegt eine Lane, die
  übrigen spawnen normal weiter), Skill-Wahl beim ersten Boss-Sieg,
  Spezialattacken Doppel-Lane und Durchschlag als Klassen am
  polymorphen Skill-Slot, Skill-Stufen durch weitere Boss-Siege.
- [ ] **M6 · Level-Lauf** — 15 Level, Lane-Progression im
  Dreier-Raster, Skalierung je Level, Sieg nach dem dritten Boss,
  Niederlage bei 0 Leben, HUD.
- [ ] **M7 · Abgabe-Polish** — Eingaben härten, Konventions-Pass,
  Leak-Kontrolle, Build, README.

## Ausbauten — nur bei Zeitreserve, Reihenfolge in den DECISIONS
(„Schnittlinien Lane Defender")

- [ ] **A1 · Dritter Gegnertyp**
- [ ] **A2 · Endlos-Modus mit Highscore-Liste**
- [ ] **A3 · Dritte Skill-Stufe**
- [ ] **A4 · raylib-Anzeige als Kür**

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
  `=`.
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
