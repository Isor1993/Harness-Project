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
- 2026-09-07 — Semester-2-Bewertungen in Canvas eingesehen (Beurteilung
  Alisa Reiter): 4FSC0PD003.1 Portfolio 74 Punkte (1-) = First (Process
  Sehr gut, Proficiency und Person Gut), 4FSC0PD004.1 Portfolio
  69 Punkte (2.1+) = Upper Second, ein Punkt unter der First-Grenze
  (alle drei Kriterien Gut); beide Module „Alle Lernziele erreicht".
  Kernpunkte der Kommentare: D003 „weniger ist mehr" (Umfang größer als
  nötig, leere Ordner nicht gelöscht), Code „niveauvoll"; D004 durchweg
  positiv bis auf das untexturierte Häuschen („fehl am Platz") und
  „nicht super kreativ" — die kreative Idee „verspricht kommende
  Inhalte".
- 2026-09-08 — C++-Kursstart: die SAE „Coding Conventions C++" (Version
  05.09.2022) eingegangen und im Datenbaum unter `01_Uni\_Regelwerk\`
  als `Coding_Guidelines_Cpp.pdf` abgelegt; das Arbeitsdestillat steht
  seit heute in `Kern/CODE_GUIDELINES.md` (Beleg im Kern-LOG).
- 2026-09-08 — SAE-Versionsvorgaben des Studienjahrs 0925 eingegangen
  (Screenshot in der Session): Unreal Engine 5.6, Unity 6000.0.59f2
  (6000.0.55f1 als veraltet gestrichen), OpenGL-Empfehlung Core 450.
  Daraufhin Unreal 5.6.1 installiert (Quixel Bridge und Fab-Plugin in
  der Warteschlange); offen bleibt der Toolchain-Test gegen VS 2026
  (`PLAN.md`). Die aktuellen Abgabetermine sind noch nicht
  veröffentlicht — die `~`-Schätzungen des Phasenplans gelten weiter.
- 2026-09-08 — C++-Unterricht Chapter 1, Abendblock des deutschen
  Tracks: 1.1 Überblick und Geschichte, 1.2 Nachschlagewerke
  (cppreference.com, cplusplus.com, isocpp.org), 1.3 Struktur —
  Projektmappe, `main` als Funktion samt ihren vier Signaturen,
  Funktionen, Header/Source-Trennung, STL, Namespaces,
  Multiparadigmen. Live-Coding in Visual Studio: `argc`/`argv`
  durchlaufen, Kommandozeilenargumente an der `.exe` testen, danach
  Umbau auf eine Funktion `ExecCmdArgs` mit benannten Konstanten.
  Angekündigt für den 2026-09-10: 1.4 Primitive Datentypen samt
  Systems-Hungarian-Tabelle und `true`/`false`, dazu 1.5 Abstrakte
  Datentypen. Vorgaben des Dozenten: keine Literale im Code, keine
  globalen Variablen (globale Konstanten erlaubt), jede Variable
  vorinitialisiert.
- 2026-09-08 — Drei Fehler im gezeigten Dozentenmaterial gefunden;
  Isor hatte nichts davon selbst getippt, alle Screenshots stammen vom
  Beamer. (1) `a_sArgV[i] == "--debugMode"` vergleicht zwei
  `const char*` und damit Adressen statt Text — im späteren Umbau von
  selbst behoben, weil die Konstante als `std::string` deklariert
  wurde. (2) `ExecCmdArgs` nimmt `bool a_bIsDebugMode` als Kopie, die
  Zuweisung erreicht den Aufrufer nie; nötig wären Referenz oder
  Rückgabewert. (3) Auf der Folie „1.4 true oder false" stehen
  `INT_MAX == true` und `INT_MIN == true` als wahr — beide sind falsch,
  weil `true` zu `int` (1) hochkonvertiert wird; gemeint ist die
  Umwandlung nach `bool`, nicht der Vergleich. Dazu Ungenauigkeiten der
  Datentyp-Folien: `char` mit 0..255 (das ist `unsigned char`; plain
  `char` ist auf MSVC signed), `int` mit „2 oder 4 Byte" (auf Windows
  x64 immer 4), `Bool` statt `bool` und ein `std::string szText`, wo
  `sz` laut derselben Tabelle den nullterminierten C-String meint.
- 2026-09-08 — Offene Rückfrage an den Dozenten, zu stellen am
  2026-09-10: Gilt die SAE-C++-Konvention nur für das Konsolenprojekt
  oder auch für den 3D-Model-Viewer? Anlass war Isors Einwand, der
  Viewer sei doch ebenfalls ein Konsolenprojekt, weil kein Unreal im
  Spiel ist. Dagegen steht, dass der Aufgabentext für Aufgabe 2
  ausdrücklich ein Anwendungsfenster verlangt und „einheitliche
  Coding-Convention" dort nicht als Feedbackelement führt. Die Antwort
  entscheidet den ROADMAP-Punkt „Dritte C++-Umgebung in
  `CODE_GUIDELINES.md` aufnehmen" (`Kern/ROADMAP.md`).
