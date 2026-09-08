# ROADMAP.md — Bauplan Lane Defender

Ownership: Nur was an Lane Defender als Nächstes gelernt oder gebaut
wird — Lern-Vorlauf, Meilensteine, Ausbauten, offene Aufgaben. Warum das
Projekt so geschnitten ist, steht in den DECISIONS dieser Schicht; die
Zeitschätzung je Meilenstein im ZEITPLAN; was passiert ist, im LOG.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

## Lern-Vorlauf — Sandbox, parallel zum Unterrichtsstart

- [ ] **L1 · Werkzeug** — VS-2022-C++-Workload prüfen bzw. installieren,
  erstes Projekt anlegen, kompilieren, Debugger starten; Unterschied zu
  C#/Unity (nativ kompiliert, kein Runtime).
- [ ] **L2 · Syntax-Umzug** — Typen, `if`/`for`/`while`, Funktionen,
  `cin`/`cout` mit Eingabe-Validierung; Mini-Snippets in `Sandbox/`.
- [ ] **L3 · Werte, Pointer, Speicher** — Wertsemantik gegen
  C#-Referenzen, Stack und Heap, `&`, `*`, `nullptr`, `const&`;
  Adressen als echte Zahlen im Debugger ansehen.

## Meilensteine — Schätzung und Ist-Zeiten im ZEITPLAN

Zielfenster aus der Semester-Roadmap, beschlossen am 2026-09-08:
abgabefertig bis ~05.10., vor dem geschätzten Uni-Termin ~15.10.
(`Uni/ROADMAP.md` → „Der Phasenplan — beschlossen am 2026-09-08").

- [ ] **M1 · Gerüst** — Konsolen-Init (Farben, Sonderzeichen,
  Cursor-Home) samt Zeichentest der Symbol-Kandidaten, Hauptmenü mit
  Titel, Start/Exit, Namenseingabe mit Validierung.
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
