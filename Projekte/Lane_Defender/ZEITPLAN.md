# ZEITPLAN.md — Zeitplan Lane Defender

Ownership: Nur die Dreispalten-Zeitplantabelle des C++-Konsolenprojekts —
Meilensteine, geschätzte Dauer, tatsächlich gebrauchte Dauer. Sie ist
der von der Aufgabe verlangte Abgabeteil (Vorjahrestext:
`Uni/Semester_3/VORJAHR_AUFGABEN.md` → „1 · C++ Konsolenprojekt") und
wird zur Abgabe als PDF ausgeleitet. Was die Meilensteine enthalten,
besitzt die ROADMAP dieser Schicht; warum sie so geschnitten sind, die
DECISIONS.
Format: eine Tabellenzeile je Meilenstein. Die Ist-Spalte wird während
der Arbeit gemessen und gefüllt, nie geschätzt; bis dahin steht `—`.

Schätzung vom 2026-09-07 (36 h, nach dem Umschwenk auf den
Lane-Shooter), vor Baustart am 2026-09-12 auf 50 h angehoben —
Begründung in den DECISIONS dieser Schicht („Zeitschätzung vor
Baustart auf 50 Stunden angehoben"). Lernzeit ist eingerechnet, weil
das Projekt zugleich der C++-Kurs ist (DECISIONS → „Das Projekt ist
der Kurs").

| Meilenstein | geschätzt | tatsächlich |
|---|---|---|
| M1 · Gerüst: Konsolen-Init, Zeichentest, Hauptmenü, Namenseingabe | 6 h | 20 h |
| M2 · Lanes und Spieler: Spielfeld, Bewegung, Live-Tasten | 7 h | ~7,5 h |
| M3 · Gegner: Klassenhierarchie, Spawn-Plan, Tick-Lauf | 10 h | ~6,7 h |
| M4 · Kampf und Upgrades: Kollision, Gold, Upgrade-Screen | 8 h | ~6 h |
| M5 · Boss und Skills: Boss, Skill-Wahl, Spezialattacken | 8 h | ~5,2 h |
| M6 · Level-Lauf: 15 Level, Progression, Sieg/Niederlage, HUD | 6 h | ~5 h |
| M7 · Abgabe-Polish: Härten, Konventionen, Leaks, Build | 5 h | ~3 h |
| Summe | 50 h | ~53,4 h |

M1 gemessen am 2026-09-20 (Grindstone): Projekt gesamt 20:50 h, davon
~0:46 h Anfangs-Design; die M1-Zeile enthält den Lern-Vorlauf L1–L3
und alle Design-Runden. Einordnung der Differenz zur Schätzung:
`ABGABE_NOTIZEN.md` → M1.

M2 gemessen am 2026-09-26 (Grindstone): Projekt gesamt 28,37 h; die
M2-Zeile ist die Differenz zum M1-Stand von 20:50 h (~7,5 h) und
enthält den M2-Design-Abschnitt vom 20.09. Einordnung:
`ABGABE_NOTIZEN.md` → M2.

M3 gemessen am 2026-09-28 (Grindstone): Projekt gesamt 35:04 h; die
M3-Zeile ist die Differenz zum M2-Stand von 28,37 h (~6,7 h) und
enthält den M3-Design-Abschnitt vom 27.09. Quersumme der sechs
M3-Einzeleinträge: 6:30 h — die ~0,2 h Rest sind unzugeordnete
Kleinstücke. Einordnung: `ABGABE_NOTIZEN.md` → M3.

M4 gemessen am 2026-09-29 (Grindstone): Projekt gesamt 41:27 h; die
zwei M4-Arbeitsblöcke messen 3:53 h (28.09.) + 2:00 h (29.09.) =
~5,9 h, die Differenz zum M3-Stand von 35:04 h ergibt ~6,4 h — der
Rest sind wieder unzugeordnete Kleinstücke. Die M4-Zeile enthält
den M4-Design-Abschnitt vom 28.09. Einordnung:
`ABGABE_NOTIZEN.md` → M4.

M5 gemessen am 2026-10-03 (Grindstone): 5,22 h über die M5-Blöcke
(30.09. Design-Abschnitt und B1 Boss, 02./03.10. B2 Skill-System);
zwischen den Blöcken lagen zwei Krankheitstage. Einordnung:
`ABGABE_NOTIZEN.md` → M5.

M6 gemessen am 2026-10-03 (Grindstone): 5 h über die M6-Blöcke des
03.10. — Design-Moment und Bau am selben Tag. Einordnung:
`ABGABE_NOTIZEN.md` → M6.

M7 gemessen am 2026-10-03 (Grindstone): 3 h — Leak-Kontrolle,
cin-Scan, Konventions-Pass, Datei-für-Datei-Review aller Klassen,
Balance-Finaltuning samt Voll-Spieltest, Release-Build, README und
Abgabe-Paket. Summe des Projekts: ~53,4 h gegen 50 h Schätzung.
Einordnung: `ABGABE_NOTIZEN.md` → M7.
