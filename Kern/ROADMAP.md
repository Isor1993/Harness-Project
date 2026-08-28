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

- [ ] **Die Handgriffe vor Punkt 4 in `CLAUDE.md` nennen** — nämlich:
  den Session-Titel nicht anfassen, und Typ und Modus fragen. Beide
  Regeln stehen in `Kern/WORKFLOW.md` und damit an Punkt 4 der
  Leseordnung; am 2026-08-27 sind beide daran gescheitert, dass vor
  Punkt 4 gehandelt wurde (`Kern/STOERUNGEN.md`, zwei Einträge desselben
  Tages). Die Leseordnung umzustellen wäre der teurere Weg — dann müsste
  `WORKFLOW.md` vor `INDEX.md` und `PLAN.md` gelesen werden.
- [ ] **Regel gegen ungeprüfte Angaben über Fremdsoftware** — In
  `CLAUDE.md` aufnehmen: Vor einer versionsabhängigen Aussage über Unity,
  ein Paket oder ein Werkzeug erst im Projekt oder in der Doku nachsehen;
  wo das nicht geht, die Unsicherheit benennen statt sie zu glätten. Für
  Diagramme gibt es die Regel bereits („erst die Quelle lesen"), für
  Behauptungen im Gespräch nicht — am 2026-08-28 kosteten drei davon eine
  Suche nach einem Schalter, den es gar nicht mehr gibt
  (`Kern/STOERUNGEN.md`).
- [ ] **Regler „Wer schreibt" und „Entwurf vor Gerüst" zusammenführen** —
  In `Kern/WORKFLOW.md` klären, was mit „Entwurf vor Gerüst" geschieht,
  wenn der Regler auf *Claude* steht: Die Regel begründet sich damit,
  dass Isor das Anfangen vor einer leeren Datei übt — und das entfällt
  dann. Im selben Zug entscheiden, ob die am 2026-08-28 entstandene
  Aufteilung nach Code-Sorte (Bibliotheks-Anbindung und Wegwerf-Code →
  Claude, Entscheidungstragendes und selbst Entworfenes → Isor) eine
  dritte Reglerstufe wird, statt mündliche Absprache zu bleiben
  (`Kern/STOERUNGEN.md`, 2026-08-28).
- [ ] **Unbeantworteter Themenvorschlag gilt als abgelehnt** — In
  `Kern/WORKFLOW.md` bei „Der geerbte Titel" ergänzen: Bleibt Claudes
  Themenvorschlag ohne Antwort, ist das **keine** Zustimmung. Der geerbte
  Titel bleibt dann bis zum Session-Ende stehen, gepflegt wird nur die
  Klammer. Anlass: dritter Fall desselben Musters am 2026-08-28
  (`Kern/STOERUNGEN.md`) — die Regel benennt den Fall „keine Antwort"
  bisher nicht, und das Umbenennen fasst immer den ganzen Titel an, nie
  die Klammer allein.
- [ ] **Zeile „Setzt voraus:" im DECISIONS-Format** — In
  `Kern/DOC_RULES.md` eine vierte, **optionale** Zeile neben Was, Warum und
  Verworfen vorsehen: die Bedingung, unter der eine Entscheidung gilt und
  die selbst nicht entschieden wurde. Optional, weil die meisten
  Entscheidungen keine haben und eine Pflichtzeile mit „keine" zugemüllt
  würde. Anlass: Eine Entscheidung vom 2026-08-27 schrieb ihre Folge auf und
  ließ die Voraussetzung weg; eine Session plante einen Tag darauf
  (`Kern/STOERUNGEN.md`, 2026-08-28).

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
