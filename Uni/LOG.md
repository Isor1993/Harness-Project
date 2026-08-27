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
- 2026-08-24 — Die vier fehlenden Aufgabentexte nachgetragen (E62 —
  Fehlende Aufgabentexte nachtragen): vier ASSIGNMENT-Dateien in
  `Uni/Semester_2/` (Softwareplanung, KI-Prototyp, Simulation,
  Akademisch), wortgetreu aus den heute abgerufenen Canvas-Aufgaben der
  Kurse 23111 und 23112; die S4-Aufgabe erwies sich als Verweiskette ins
  Modul 4GST1XD001 (Kurs 21787) und wurde samt der zwei abgegebenen
  Übungstexte übernommen. Damit liegen die Originaltexte aller sieben
  Teilabgaben vor; INDEX neu erzeugt (52 Dateien, alle mit
  Ownership-Zeile).
- 2026-08-25 — Semester-2-Abschluss nachgezogen (Isor: Abgabe ist final
  raus). Der ROADMAP-Punkt „Akademische Texte gegen den Harvard-Leitfaden
  prüfen" ging als überholt mit Ablöse-Vermerk ins Archiv der Schicht;
  `Abgabe_Final` im Datenbaum aufgeräumt: die zwei Portfolio-Ordner
  (2.474 Dateien, 1.420.522.200 Bytes — Dateizahl und Byte-Summe vor dem
  Verschieben gegen `Abgabe\` geprüft, identisch) nach
  `99_Archiv\_Zu_Loeschen\2026-08-25_Abgabe_Final_Duplikate\`; es
  bleiben die zwei Abgabe-ZIPs.
- 2026-08-26 — Uni-Schicht geprüft, erster Prüfbogen für diese Schicht:
  sechs Befunde auf zwölf Dateien (1.663 Zeilen), geprüft gegen den
  Prüfbogen aus `Kern/WORKFLOW.md`, den INDEX und die Regeldateien des
  Kerns. Alle sechs stammen aus den zwei echten Regeldateien; Chroniken,
  Archiv und die sieben Aufgabentexte waren ohne Befund.
- 2026-08-26 — Fünf der sechs Befunde behoben, in eigener Session nach
  Isors Revier-Freigabe: `Uni/DOCX_RULES.md` (U1 Ownership-Zeile auf
  `Projekte/Isor_Tower/TDD.md`, U2 Prüfliste umgestellt — `validate.py`
  ist jetzt Schritt 4 und läuft nur nach Handarbeit am XML, U3 Marke
  `DATENBAUM` beim ersten Pfad) und `Uni/ROADMAP.md` (U4 relative
  Zeitangabe aus der Überschrift, U5 „Abgeschlossenes" → „Überholtes").
  U6 bleibt bewusst stehen, bis der nächste Textstand gebaut ist. Bei U2
  wurden die zwei Rückverweise im Abschnitt „Werkzeuge" auf die neue
  Nummerierung nachgezogen; geprüft mit `pruefen.py` und
  `index_bauen.py`.
