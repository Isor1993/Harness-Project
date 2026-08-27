# ROADMAP.md — Baureihenfolge Harness

Ownership: Nur was am Harness als Nächstes gebaut wird. Was gerade dran
ist, steht in `PLAN.md`; was fertig ist, in `Kern/LOG.md`; warum es so
entschieden wurde, in `Kern/DECISIONS.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`
Kein Datum, keine Tagesplanung — das ist Sache von `PLAN.md`.

**Erledigtes steht nicht hier, sondern im LOG der Schicht.** Ein
abgehakter Punkt hat seinen Beleg dort; ihn zusätzlich hier stehen zu
lassen heißt, ihn bei jeder Arbeit an dieser Schicht mitzulesen.

<!-- nicht ausliefern -->
*Für dieses Projekt:* Am 2026-08-27 wurde die Regel oben zum ersten Mal
angewandt — rund 220 Zeilen abgehakter Punkte sind rausgeflogen. Vorher
wurde gegengeprüft, ob jeder Haken im LOG belegt ist: Drei waren es
nicht und wurden zum 2026-08-25 nachgetragen (`Kern/LOG.md`, Vermerk
„Nachgetragen am 2026-08-27").
<!-- /nicht ausliefern -->

## Als Nächstes

**Gerade nichts offen.** Ein leerer Abschnitt ist hier ein gültiger
Inhalt und kein Versehen. Er wird nicht vorsorglich gefüllt: Ein
erfundener Punkt sieht genauso verbindlich aus wie ein echter.

Was im Betrieb nicht trägt, kommt als Störung in `Kern/STOERUNGEN.md`
und wird von dort aus zu einem Punkt hier — genau dafür fragt die
Doku-Pflicht in `Kern/WORKFLOW.md` nach beidem im selben Zug.

<!-- nicht ausliefern -->
*Für dieses Projekt:* Der Harness ist gebaut. Seit dem 2026-08-27 wird
er benutzt statt gebaut — die Testphase läuft (`PLAN.md`).
<!-- /nicht ausliefern -->

## Später, nur bei Bedarf

- [ ] **ClaudeSetup** — ein Editor-Skript, das Szenen baut und
  verdrahtet. Zurückgestellt, solange Isor in der Lernphase selbst
  tippt. **Wieder aufgenommen auf Isors Zuruf**, nicht wenn Claude ihn
  für so weit hält: „sicher programmieren" ist keine Bedingung, die von
  außen feststellbar wäre — dieselbe Konstruktion wie bei der Testphase
  und aus demselben Grund *(geschärft 2026-08-26; die alte Fassung sagte
  „wieder prüfen, wenn er sicher programmiert")*. Der wiederkehrende
  Anlass, die Frage überhaupt zu stellen, ist `/harness:zeugnis`
  (`Kern/ASSESSMENT_RULES.md`).
- [ ] **Review-Seite zu „Claude baut, Isor reviewt"** — woran Isor
  prüft, was Claude an Unity-Code gebaut hat. **Der Modus selbst ist
  gebaut und in Betrieb:** Der Regler „Wer schreibt" steht in
  `Kern/WORKFLOW.md` (E21), und bei Harness-Arbeit tippt ohnehin Claude.
  Offen ist die zweite Hälfte. Für Harness-Werkzeuge ist das Gegenlesen
  gelebte Praxis, für Unity-Code gibt es kein Verfahren — und dort zählt
  es am meisten, weil Isors Maßstab das Prüfungsgespräch ist
  (`Projekte/Isor_Tower/ALTSTAND.md`). Anzuschließen an das Review-Gate
  in `Kern/CODE_GUIDELINES.md`, das heute ausdrücklich **vor** dem Coden
  greift und keine Zeile danach prüft.
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
