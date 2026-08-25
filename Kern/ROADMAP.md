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
- [ ] **Der Pflegetag prüft eine Seite inhaltlich, statt alle
  oberflächlich.** Belegt am 2026-08-23: Er meldete drei Funde, eine
  gründliche Durchsicht derselben acht Seiten fand rund dreißig
  (`STOERUNGEN.md`). Der Abgleich sieht heute nur Metadaten — Index
  gegen Änderungen und gegen die Veröffentlichungsliste. Zu entscheiden:
  eine Seite je Woche im Turnus, gegen den Code gehalten. Hängt daran,
  dass `ARTIFACT_RULES.md` den Stand-Stempel nur erlaubt, **weil** der
  Pflegetag ihn kontrolliert.
- [ ] **Regel für parallele Sessions.** `WORKFLOW.md` sagt „höchstens 2–4
  Sessions parallel offen", aber nichts darüber, wer schreiben darf. Am
  2026-08-23 hat sich eine Parallel-Session selbst eine Regel gegeben und
  vorsichtshalber gar nichts ins Repo geschrieben — richtig gehandelt,
  aber geraten. Zu klären: Wer hält den Stift, wenn zwei Sessions
  dieselbe Datei berühren könnten, und wie übergibt man ihn.
- [ ] **Systemliste je Projekt erzeugen** (E14). Skript liest
  `Assets/Systems`, `Entities`, `Shared` und schreibt Name, Anzahl
  Skripte, letzte Änderung; die Kurzbeschreibung je System kommt von
  Hand und wird über Neuerzeugungen übernommen. Beantwortet „was steckt
  gerade im Projekt drin" — das tut heute kein Dokument.
- [ ] **Werkzeug Markdown → `.docx`** (E61b). Der Abgabetext lebt in
  Markdown, die `.docx` wird daraus gefüllt; das vorhandene TDD-Layout
  wird dabei zur Formatvorlage, nicht weggeworfen. Realistisch ein
  voller Arbeitstag, die ersten Läufe sitzen nicht auf Anhieb.
- [ ] **Test-Abschnitt für `CODE_GUIDELINES`** (E56). Die
  Ownership-Zeile nennt „Tests", der Abschnitt fehlt. Zu klären ist
  zuerst, ob automatische Tests (Unity Test Framework) überhaupt gewollt
  sind — bisher wird von Hand über `TestMode`-Schalter geprüft.
- [ ] **Repo- und Git-System neu ordnen** (eigene Design-Session). Die
  Repos wachsen stark, weil Binärdateien mitversioniert werden. Zu
  klären: was gehört ins Repo und was in die Asset-Library, ob Git LFS
  eingesetzt wird, wie `.gitignore` je Repo aussehen muss, wie mit der
  gewachsenen Historie umgegangen wird. Betrifft alle drei Repos.
  Dazu gehört auch das Build-Versionsschema (`Kern/VERSIONIERUNG.md`).
  **Überschneidung beachten:** Für das Harness-Repo nimmt „Struktur
  begradigen" oben einen Teil davon vorweg — `.gitignore` und die Frage,
  was dort überhaupt hineingehört. Dieser Punkt behandelt danach nur noch
  die zwei anderen Repos und die übergreifenden Fragen.
- [x] **Zwei Reste aus dem ARTIFACT_INDEX** (E46) — geschlossen am
  2026-08-25. Die tote ID `0dd96ec7-…` bekommt keinen Nachfolger
  (Isor): Nichts zeigt auf sie, keine Kopie existiert; der Vermerk
  steht in der Gelöscht-Tabelle des Index. Die „Seite →"-Zeilen
  brauchen keinen ROADMAP-Punkt — der Index markiert sie selbst als
  „(noch nicht erfasst)", gefüllt wird beim nächsten Anfassen der
  jeweiligen Seite.

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
