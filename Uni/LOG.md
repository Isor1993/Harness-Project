# LOG.md — Chronik Studium

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste oben.
Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur ergänzt.
Sie kann daher nicht falsch werden und braucht kein Archiv.
Was als Nächstes kommt, steht in `ROADMAP.md`; warum es so entschieden
wurde, in den DECISIONS dieser Schicht.
Format: `- JJJJ-MM-TT — Ereignis (1–3 Sätze: was, und woran es geprüft wurde)`.
Ein Eintrag darf einen Ablageort nennen — er beschreibt den Stand von
damals, nicht den von heute.

- 2026-08-05 — Messinfrastruktur für die Threading-Abgabe
  (`Systems/TerrainGenerator/Scripts/`): `PlacementMetrics` (struct) trägt die
  Stufenzeiten aus dem Placer heraus, `InstancedRenderer` misst Exclusion,
  Zellenbau und Gesamtzeit und loggt sie in `#if UNITY_EDITOR ||
  DEVELOPMENT_BUILD`; Feld `Measurement Runs` wiederholt den Rebuild für
  Messreihen. Geprüft im Development Build, 4 Läufe je Version.
- 2026-08-08 — Vier UML-Klassendiagramme für den Terrain-Ast erzeugt
  (`01_Uni\Semester_2\Diagramme_Quellen\`): Terrain-Pipeline (5 Klassen),
  Platzierung inkl. Strategy-Muster (14), Gras-Rendering (8) und Editor-Tool
  mit sichtbarem MVP-Aufbau (8). Je ein Skript unter `05_Werkzeuge\Vorlagen\`,
  Prüfer meldet bei allen null Abweichungen gegen den Code.
- 2026-08-09 — Messreihen-Tabelle in TDD-Kapitel 6.5 eingesetzt (Tabelle 8):
  sechs Messpunkte × vier Zeitspalten plus Verbesserung, Werte neu aus den
  sechs Rohlogs gerechnet (Mittel der Läufe 2–4) und mit den Zahlen im
  Fließtext abgeglichen. Aufbau wie die bestehenden Tabellen (9062 dxa,
  Kopfzeile 0070C0), Beschriftung als SEQ-Feld; Schrift 10 pt. Geprüft am
  gerenderten PDF: kein Umbruch mitten im Wort, Abschnitt passt auf eine Seite,
  Feldaktualisierung ergibt Tabelle 8 (neu) und Tabelle 9 (Assets).
- 2026-08-11 — TDD Kapitel 12 vervollständigt: Die drei Texturquellen (3dtextures.me
  „Moon 002", ambientCG „Ground082S", freestylized „Grass 05") als eigene Unterkapitel
  nach dem bestehenden Schema ergänzt, Tabelle 9 von zwei auf fünf Zeilen, vier
  Einträge im Quellenverzeichnis, Vergleichsabsatz und Kennzeichnung der
  KI-erzeugten Grastextur; in Tabelle 1 eine Zeile für ChatGPT. Alle drei
  Lizenzseiten selbst aufgerufen: zweimal CC0, bei freestylized eine Royalty Free
  License, deren Weitergabe-Einschränkung nur auf der About-Seite steht.
  Geprüft am gerenderten PDF (84 Seiten).
- 2026-08-11 — Zustandsdiagramm der Sheep-FSM
  (`Diagramme_Quellen\Zustand_Sheep_FSM.drawio`, Skript `zustand_sheep_fsm.py`):
  elf Zustände, Anfangsknoten, Sammelknoten „aus jedem Zustand" für die vier
  Push-Wechsel, 31 Übergänge. Neu dafür die Sinnbilder `zustand` und `anfang`.
  Jede Kante ist im Skriptkopf mit Klasse und Zeilennummer belegt. Ergänzt
  `Sheep_FSM` (dort die Klassen, hier die Übergänge). Von Isor angeordnet.
- 2026-08-12 — Abgabe-Ordnerstruktur gebaut und befüllt: die beiden
  Portfolio-Ordner nach dem SAE-Schema, Vorlage abgelegt unter
  `05_Werkzeuge\Vorlagen\SAE_Abgabe_Struktur\`.
- 2026-08-20 — Build 0.0.3 abgegeben. Beide Portfolio-ZIPs neu gebaut
  (309,8 MB und 541,5 MB), `release` und `src` in beiden Abgaben auf den
  heutigen Stand gezogen.
