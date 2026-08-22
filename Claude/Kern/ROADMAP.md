# ROADMAP.md — Baureihenfolge Harness

Ownership: Nur was am Harness als Nächstes gebaut wird. Was gerade dran
ist, steht in `PLAN.md`; was fertig ist, in `Kern/LOG.md`; warum es so
entschieden wurde, in `Kern/DECISIONS.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`
Kein Datum, keine Tagesplanung — das ist Sache von `PLAN.md`.

## Läuft gerade
- [ ] **Überholung auf Version 1.0.0.** Stand und Reihenfolge in
  `PLAN.md`, Befunde in `_HARNESS_REVIEW.md`, Handgriffe in
  `_HARNESS_UMSETZUNG.md`.

## Als Nächstes
- [ ] **Abnahme abschließen.** 30 der 33 Befunde sind am 2026-08-22
  behoben; offen sind nur noch drei, und alle drei hängen an einem
  Zeitpunkt statt an Arbeit: **A10** und **A25** kurz vor dem Archivieren
  der Review-Dateien, **A12** am ersten Pflegetag. Danach die
  Artifact-Seite `⚙️ System · Harness`, dann die Auslieferung
  `Harness_1.0.0`. Einzelheiten in `_HARNESS_ABNAHME.md`, Abschnitt
  „Stand der Umsetzung".
- [ ] **Prüfskripte in den Kern übernehmen** als
  `Kern/Werkzeuge/pruefen.py`, Aufruf am Pflegetag. Zwei Prüfungen:
  alle Datei-Verweise gegen den tatsächlichen Bestand, und die
  Formatzusagen der Chroniken und Entscheidungsdateien
  (Datumsreihenfolge, Pflichtfelder). Grund: In der Abnahme vom
  2026-08-22 haben genau diese zwei Prüfungen 6 der 33 Befunde allein
  gefunden — tote Verweise, verdrehte Reihenfolge und nicht gedeckte
  Haken rutschen beim Lesen durch. Wegwerf-Fassungen lagen im
  Scratchpad; für den Dauerbetrieb zusammenfassen und aufräumen.
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
- [ ] **Zwei Reste aus dem ARTIFACT_INDEX** (E46): Die Zeile „Seite →"
  ist erst bei drei Seiten gefüllt — wird nachgetragen, wenn die
  jeweilige Seite das nächste Mal angefasst wird. Und für die tote ID
  `0dd96ec7-…` ist nicht entschieden, welche heutige Seite sie beerbt.

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
