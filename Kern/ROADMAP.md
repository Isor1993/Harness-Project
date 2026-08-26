# ROADMAP.md — Baureihenfolge Harness

Ownership: Nur was am Harness als Nächstes gebaut wird. Was gerade dran
ist, steht in `PLAN.md`; was fertig ist, in `Kern/LOG.md`; warum es so
entschieden wurde, in `Kern/DECISIONS.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`
Kein Datum, keine Tagesplanung — das ist Sache von `PLAN.md`.

## Läuft gerade
- [x] **Überholung auf Version 1.0.0** — abgeschlossen am 2026-08-23.
  Acht Phasen, die achte war die Abnahme, danach ein Gegenlese-Durchgang
  aus eigener Session. Ausgeliefert nach
  `05_Werkzeuge\Harness_Auslieferungen\Harness_1.0.0\` im Datenbaum;
  die drei Arbeitsdateien sind archiviert, was aus ihnen dauerhaft gilt,
  steht in den Regeldateien. Ereignis im `LOG.md`.

## Als Nächstes
- [x] **Nachlese zum Bau vom 2026-08-23** — gelaufen am 2026-08-23 als
  Prüfung in frischer Session. Ergebnis: vierzehn Befunde in
  `_HARNESS_PRUEFUNG_1_0_0.md`, acht davon `muss`. Behoben ist nichts.
- [x] **Die Befunde der Prüfung 1.0.0 beheben** — am 2026-08-23 in einem
  eigenen Abschnitt erledigt, alle vierzehn. Wo jede Änderung steht,
  zeigt die Tabelle „Behebung" in `_HARNESS_PRUEFUNG_1_0_0.md`. Offen
  bleibt allein die Automatisierung zu P4 und P13; sie steht als Punkt
  beim Prüfskript unten. Betroffen waren:
  **P2 — „Plan nachziehen" prüft nur den Übergabe-Abschnitt** (ein
  vierter Handgriff fehlt) · **P3 — diese ROADMAP widerspricht
  `PLAN.md`** (Testphase ohne Zuruf-Vorbehalt, Reihenfolge verdreht) ·
  **P4 — die Anzahl-Regel ist an sechs Stellen gebrochen** ·
  **P7 — die Regel „Befunde sofort eintragen" wurde beim Archivieren
  übersehen** · **P10 bis P12 — drei falsche Zeilen im `GLOSSARY.md`**
  (der fünfte Session-Typ fehlt, „Chronik" sagt das Gegenteil der Regel,
  „Auslieferung" heißt dort Kopie statt Vorlage) · **P13 — das Glossar
  steht in keiner Doku-Pflicht**, was die drei erklärt. Danach ist die
  Befundliste archivierbar.
- [x] **Prüfskripte in den Kern übernehmen** — gebaut am 2026-08-23 als
  `Kern/Werkzeuge/pruefen.py`, fünf Prüfungen, Aufruf bei jedem
  `/harness:sichern` statt am Pflegetag (die Fehler entstehen beim
  Schreiben). Erster scharfer Lauf: ein echter Fund, drei Sammelhinweise;
  der Weg von 45 auf 4 Funde steht im `Kern/LOG.md`. Offen bleibt nichts.
Die ersten beiden Punkte hängen voneinander ab und stehen vor allem
anderen: Solange die Pfade sich noch ändern, erzeugt jede weitere
Arbeit Zeiger, die hinterher noch einmal angefasst werden müssen.

- [x] **Struktur begradigen: der Harness wird sein eigenes Repo** —
  erledigt am 2026-08-23 als Harness 2.0.0. Wurzel ist das Repo selbst,
  null Weiterleitungen, eine einzige
  `CLAUDE.md`; Notkern und die INDEX-Kategorie Wegweiser sind entfallen.
  Getrackt statt 123 nur noch 58 Dateien. Was beim Ausführen vom Plan
  abwich, steht in `_HARNESS_UMBAU_STRUKTUR.md` (im Archiv), Baustein 1;
  das Ereignis im `Kern/LOG.md`, die Entscheidungen in
  `Kern/DECISIONS.md`.

- [x] **Auslieferung `Harness_2.0.0` abgelegt** — am 2026-08-24, nach der
  neuen Packliste in `VERSIONIERUNG.md`, mit Probelauf des
  Einrichten-Ablaufs vor dem Ablegen. 31 Dateien, 269.233 Bytes, Quelle
  wie Ziel. Neu gegenüber 1.0.0 im Paket: `PFADE.md` (geleert),
  `Vorlagen/`, `Bilder/`, `pruefen.py`, der sechste Befehl
  `einrichten.md`.

- [x] **GitHub-Repo umbenannt** — erledigt am 2026-08-25 durch Isor:
  heißt jetzt `Isor1993/Harness-Project`, passend zum Ordner
  `Harness Project`. GitHub leitet den alten Namen weiter; die lokale
  Remote-URL ist nachgezogen und gegen den letzten Commit geprüft
  (`git ls-remote`). Der alte Name steht nur noch in datierten
  Chronik-Einträgen.
- [x] **Hooks: erzwingen statt erinnern** — gebaut am 2026-08-23,
  scharf belegt beim ersten Session-Start danach: Die Zeile
  `[SessionStart-Hook]` stand ohne sichtbaren Werkzeugaufruf im Kontext,
  Ergebnis 0 Funde bei 49 Dateien. Damit ist zugleich belegt, dass
  Claude Code den Platzhalter `${CLAUDE_PROJECT_DIR}` ersetzt und
  `python` im Hook-Prozess erreichbar ist. Gebaut wurden `SessionStart`,
  die Vorlage, Prüfung 6 und der Schalter `--hook` (Einzelheiten im
  `Kern/LOG.md`). `_HARNESS_UMBAU_STRUKTUR.md` (im Archiv) ist
  daraufhin archiviert.
- [x] **`pruefen.py` sieht jetzt auch die temporären Wurzeldateien** —
  gebaut am 2026-08-25. Prüfung 1 schlägt Verweise auf `_HARNESS_*.md`
  nach: Datei in der Wurzel → still; verschwunden → Fund, außer die
  Zeile oder die unmittelbar folgende trägt den Zusatz „(im Archiv)" —
  das Kennzeichen hat Isor entschieden, die Regel steht in
  `Kern/DOC_RULES.md`, Abschnitt 6. Der erste scharfe Lauf fand sechs
  Stellen: fünf ohne Kennzeichen (nachgezogen), eine mit dem Zusatz auf
  der Folgezeile — daher das Zwei-Zeilen-Fenster. Die Befundlisten
  selbst überspringt die Prüfung wie Chroniken; ihre Verweise sind
  Bericht von damals.
- [x] **Artifact-Seite `⚙️ System · Harness` auf 2.0.0 nachziehen** —
  erledigt am 2026-08-23, gleiche URL. Nachgezogen wurden die
  Versionszeile, alle gemessenen Zahlen (Leseordnung, Bestand,
  Kopfzeile), die Nummern-Tabelle, der Pflegetag ohne Backup und der
  Stand-Abschnitt; neu sind Punkt 5 der Leseordnung, die Prüfebenen als
  Tabelle und **Tafel 5** aus `Kern/Bilder/hook_sessionstart.svg`. Zwei
  inhaltliche Fehler der alten Fassung sind mit weg: Sie kündigte die
  Testphase als automatische Folge an (sie beginnt auf Zuruf) und nannte
  ein Commit-Format, das es nicht gibt.
- [x] **Den Artifact-Altbestand nachziehen** — abgeschlossen am
  2026-08-24, alle acht Seiten an einem Tag, in der geplanten
  Reihenfolge (Terrain-Fallen → Multithreading → Input-Reader → Schaf →
  Poisson → GPU + Terrain & Gras als Paar → Grundgerüst). Das
  Grundgerüst wurde dabei wie entschieden **geteilt**: Die neue Seite
  „Welt & Überleben" trägt Tag-Nacht, Herde/FSM und den
  Schadens-Unterbau. Jede Seite wurde vor dem Umbau abgerufen und gegen
  den echten Code geprüft; die Stände je Seite stehen im
  `ARTIFACT_INDEX.md`. Die Befundliste `_HARNESS_ARTIFACTS_1_0_0.md`
  (im Archiv) ist damit abgearbeitet und archiviert.
- [x] **Der Pflegetag prüft eine Seite inhaltlich, statt alle
  oberflächlich** — entschieden und geregelt am 2026-08-25: Der
  Metadaten-Abgleich bleibt (er kontrolliert die Stand-Stempel), dazu
  prüft jeder Pflegetag genau eine Seite gegen Code und führende
  Quelle — dran ist die lebendige Seite mit dem ältesten Stand im
  ARTIFACT_INDEX. Regeln in `Kern/ARTIFACT_RULES.md` („Wann geschaut
  wird") und `Kern/WORKFLOW.md` (Pflegetag), Begründung in
  `Kern/DECISIONS.md`.
- [x] **Regel für parallele Sessions** — entschieden und geregelt am
  2026-08-25 als Revier-Modell: frei geschrieben wird nur in der Schicht
  des eigenen Fokus, die Gemeinschaftsdateien nur innerhalb der Befehle
  (die Isor nacheinander anstößt), das Revier wird frei durch
  Abschnittsende; fremde Schicht → melden statt schreiben. Regel in
  `Kern/WORKFLOW.md` („Parallele Sessions"), Begründung in
  `Kern/DECISIONS.md`.
- [x] **Systemliste je Projekt erzeugen** (E14) — gebaut am 2026-08-25
  als `Projekte/Isor_Tower/Werkzeuge/systeme.py`, erzeugt `SYSTEME.md`
  (17 Ordner, 93 Skripte beim ersten Lauf). Anders als der alte Wortlaut
  hier liest es die heutige Typ-Struktur (`Assets/Scripts/<System>/`
  plus `Assets/Editor/`) und den Projektpfad aus `Kern/PFADE.md` →
  `PROJEKT`; Zuschnitt in `Kern/DECISIONS.md`. Die Beschreibungen je
  System füllt Isor — bis dahin stehen sie als „⚠ fehlt".
- [x] **Werkzeug Markdown → `.docx`** (E61b) — gebaut, nach dem ersten
  Sichttest umgebaut und am 2026-08-25 von Isor abgenommen:
  `Kern/Werkzeuge/abgabe_bauen.py` baut den Fließtext per Pandoc und
  setzt ihn hinter den fixen Titelteil (Sperr-Check, Sicherung,
  SEQ/REF-Nachlauf, Zusammenbau über Word). Dazu im Datenbaum
  `TDD Titelteil.docx` und `TDD Formatvorlage.docx`, im Repo das
  Manuskript `Projekte/Isor_Tower/TDD.md`. **Seit heute führt das
  Markdown** (`Uni/DOCX_RULES.md`); Architektur in `Kern/DECISIONS.md`,
  Ereignisse im `Kern/LOG.md`.
- [x] **SEQ-Felder für Abbildungs-Beschriftungen** (Rest aus E61b) —
  miterledigt am 2026-08-25 beim Umbau: Der Nachlauf in
  `abgabe_bauen.py` erzeugt SEQ-Felder samt Sprungmarken (im ersten
  Lauf 10 Tabellen, 43 Abbildungen) und baut Querverweise zu
  REF-Feldern um; Abbildungs- und Tabellenverzeichnis füllen sich
  bei F9.
- [x] **Test-Abschnitt für `CODE_GUIDELINES`** (E56) — entschieden und
  geschrieben am 2026-08-25: kein Unity Test Framework, die Hand-Prüfung
  (TestMode-Muster, Sichtprüfung, Diagnostic-Skripte) steht als
  Abschnitt „Tests" in `CODE_GUIDELINES.md`, die Verwerfung samt
  Wiederprüf-Anlass unter „Bewusst nicht übernommen", die Begründung in
  `Kern/DECISIONS.md`.
- [x] **Repo- und Git-System neu ordnen** — Design-Session am
  2026-08-26, alle Fragen entschieden (`Kern/DECISIONS.md`, vier
  Einträge vom selben Tag). Gemessen: Harness (3,2 MB) und Knowledge
  (0,2 MB) sind gesund; im Unity-Repo stammen 92 % der Historien-Bytes
  aus Szenen-Ständen (1.269 MB roh, `Village.unity` 73 MB je Stand).
  Beschlossen: Szenen und NavMesh künftig über LFS, Historie-Migration
  als eigener Punkt unten; Isor Tower wird privat, der Harness bleibt
  bewusst öffentlich; Repo-Grenze zur Asset-Library, Build-Ablage und
  V-Nummer-Lesart geregelt (`Kern/CODE_GUIDELINES.md` → „Repo & Git",
  `Kern/VERSIONIERUNG.md`). Das GitHub-Token in der Remote-URL des
  Unity-Repos wurde dabei gefunden und noch in der Session entfernt.
- [x] **LFS-Migration des Unity-Repos** — am 2026-08-26 vorgezogen und
  durchgeführt statt am Wochenende. **Git-Pack 117 MB → 2,2 MB**,
  Rohbytes der Historie 1.372 MB → 32,6 MB; größte Datei darin jetzt
  ein 2,26-MB-Font statt einer 73-MB-Szene. Gesichert vorher als
  `git bundle` (118,7 MB, verifiziert) im Datenbaum unter
  `02_Projekte\IsorsTower\Repo_Sicherungen\` (`Kern/PFADE.md` →
  `DATENBAUM`). Isor hat committet und force-gepusht; lokal und GitHub
  stimmen überein, die Szene liegt dort als Zeiger, Unity öffnet das
  Projekt normal. Zwei Nacharbeiten waren nötig: 36 Dateien lagen nach
  der Migration nur als Zeiger im Arbeitsverzeichnis (`git lfs
  checkout`), und das Muster `NavMesh*.asset` traf auch
  `ProjectSettings/NavMeshAreas.asset` — es heißt jetzt `NavMesh-*`.
- [x] **GitHub-Handgriffe, nur Isor** — erledigt am 2026-08-26: das
  alte `gho_`-Token widerrufen und `Isor-Tower-ProtoTyp-2026` privat
  gestellt. Geprüft per API-Abruf ohne Anmeldung: Das Repo antwortet
  jetzt mit 404, der Harness wie gewollt mit 200. Begründung:
  `Kern/DECISIONS.md`, „Sichtbarkeit und Zugang der Repos".
- [x] **Zwei Reste aus dem ARTIFACT_INDEX** (E46) — geschlossen am
  2026-08-25. Die tote ID `0dd96ec7-…` bekommt keinen Nachfolger
  (Isor): Nichts zeigt auf sie, keine Kopie existiert; der Vermerk
  steht in der Gelöscht-Tabelle des Index. Die „Seite →"-Zeilen
  brauchen keinen ROADMAP-Punkt — der Index markiert sie selbst als
  „(noch nicht erfasst)", gefüllt wird beim nächsten Anfassen der
  jeweiligen Seite.

- [ ] **Ein Artifact-Typ für Design-Absicht fehlt.** `ARTIFACT_RULES.md`
  kennt drei Typen: Status (wo steht das Projekt), System (wie funktioniert
  *mein* System X) und Lernstück (übertragbares Konzept). Eine Seite, die
  ein noch **ungebautes** System entwirft, passt in keinen: Sie beschreibt
  Absicht, nicht Zustand. Aufgefallen am 2026-08-26 beim Bau von
  `⚙️ System · Multiplayer`, die deshalb behelfsweise als System geführt
  wird und im Vorspann ausdrücklich sagt, dass sie Absicht beschreibt.
  Zu entscheiden: vierter Typ, oder die System-Definition so weiten, dass
  sie „geplant" einschließt — beides hat Folgen für den Pflegetag, denn
  eine Absichtsseite lässt sich nicht gegen Code prüfen.

- [ ] **Testphase beginnen — erst auf Isors Zuruf.** Der Harness wird
  benutzt statt gebaut. Steht bewusst am Ende dieser Liste: Der Beginn
  hängt an keiner Bedingung, die Claude feststellen könnte, sondern an
  Isors Ansage (`Kern/DECISIONS.md`, 2026-08-23). Erste Aufgabe dann:
  den Datenbaum aufräumen, in Viererpaketen (`IsorBackup/ROADMAP.md`).
  Zugleich die erste Belastungsprobe — was dabei nicht trägt, kommt in
  `STOERUNGEN.md`.

## Später, nur bei Bedarf
- [ ] **Knowledge-Archivierung automatisieren.**
- [ ] **ClaudeSetup** — ein Editor-Skript, das Szenen baut und
  verdrahtet. Zurückgestellt, solange Isor in der Lernphase selbst
  tippt; wieder prüfen, wenn er sicher programmiert.
- [ ] **Development-Modus „Claude baut, Isor reviewt"** — der Regler
  „Wer schreibt" sieht ihn bereits vor (E21); ausgearbeitet wird er erst
  nach der Lernphase.
- [ ] **Harness-Dokumente auf Englisch** — **erst prüfen, wenn der
  Harness tatsächlich an jemanden weitergegeben werden soll** (E83).
  Solange das nicht ansteht, gilt die Sprachtabelle in `DOC_RULES.md`:
  Harness-Dokumente sind deutsch.
- [ ] **Artifact-Seite für die Weitergabe** (Isor, 2026-08-23) — eine
  zweite Harness-Seite, die **nur** das Verfahren erklärt: Schichten,
  Ownership, Session-Ablauf, Befehle. Ohne Isors Projektstand, ohne
  Befundzahlen, ohne Beispiele aus Isor's Tower. Grund: Die bestehende
  Seite `⚙️ System · Harness` beschreibt den Harness **in Benutzung** und
  ist als Erklärung für Fremde ungeeignet. Hängt an derselben Bedingung
  wie der Punkt darüber — gebaut wird sie, wenn eine Weitergabe ansteht,
  nicht vorher.
