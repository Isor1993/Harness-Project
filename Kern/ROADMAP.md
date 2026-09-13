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

- [ ] **Kommentar-Pass als fester Review-Schritt festschreiben** — In
  `Kern/CODE_GUIDELINES.md` (Abschnitt „Kommentare & Datei-Header"
  bzw. Review-Gate) ergänzen: Nach jeder Tipp-Runde und jedem
  Datei-Umzug läuft ungefragt Claudes Kommentar-Pass — Datei-Köpfe,
  Summaries, sichtbare Texte —, bevor weitergebaut wird. Anlass:
  Zweimal am 2026-09-13 mussten die Köpfe neuer Dateien angemahnt
  werden (`Kern/STOERUNGEN.md`, Eintrag samt Wiederholungs-Vermerk).
- [ ] **Die Handgriffe vor Punkt 4 in `CLAUDE.md` nennen** — nämlich:
  den Session-Titel nicht anfassen, und Typ und Modus fragen. Beide
  Regeln stehen in `Kern/WORKFLOW.md` und damit an Punkt 4 der
  Leseordnung; am 2026-08-27 sind beide daran gescheitert, dass vor
  Punkt 4 gehandelt wurde (`Kern/STOERUNGEN.md`, zwei Einträge desselben
  Tages). Die Leseordnung umzustellen wäre der teurere Weg — dann müsste
  `WORKFLOW.md` vor `INDEX.md` und `PLAN.md` gelesen werden.
- [ ] **Regel gegen ungeprüfte Angaben über Fremdsoftware** — In
  `CLAUDE.md` aufnehmen: Vor einer versionsabhängigen Aussage über die
  Engine, ein Paket oder ein Werkzeug erst im Projekt oder in der Doku
  nachsehen;
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
- [ ] **Datei-Befunde nur aus der Originalquelle** — In `CLAUDE.md`
  aufnehmen: Bevor Claude einen Befund an einer Datei meldet (kaputte
  Zeichen, fehlende Zeilen), liest er die Stelle in der Datei selbst
  gegen — nie nur in einer Such- oder Diff-Anzeige, die die Darstellung
  verfälschen kann. Anlass: Fehlalarm „`\` statt `//`" am 2026-08-30
  (`Kern/STOERUNGEN.md`); dieselbe Linie wie der Ownership-Vorfall vom
  2026-08-21 („Befund braucht Beleg").
- [ ] **Pflege-Fälligkeiten als Hinweis in `pruefen.py`** — Gegenmittel
  zur Störung vom 2026-09-11 (`Kern/STOERUNGEN.md`): ein Hinweis (`?`,
  kein Fund), wenn der letzte Pflegetag-Eintrag in `Kern/LOG.md` älter
  als sieben Tage ist, und einer, wenn die Harness-Version in `CLAUDE.md`
  nicht die Version im Stand von `⚙️ System · Harness` im
  `ARTIFACT_INDEX.md` ist. Beides steht in Dateien; den veröffentlichten
  Bestand selbst sieht das Skript weiterhin nicht, der bleibt Sache des
  Pflegetags.
- [x] **Lern-Log einführen** — eine laufend geführte Aufzeichnung
  darüber, was Isor selbst geschafft hat, wo Gerüste oder Hilfe nötig
  waren und welche Fehler auftraten; die Zeugnisse
  (`Kern/ASSESSMENT_RULES.md`) sollen daraus lesen statt aus Erinnerung
  (Isor, 2026-08-30). Erst das Führen bauen, die Auswertung bewusst
  später. Offen für den Design-Abschnitt: Ablageort und Eintragsform,
  vor allem aber der Auslöser — Kandidaten sind die Doku-Pflicht und das
  Review-Gate; die größte Gefahr ist eine Pflicht, die einschläft.
  **Erledigt am 2026-09-04:** `Kern/LERNLOG.md` angelegt und rückwirkend
  erstbefüllt; geführt wird laufend, die Doku-Pflicht fragt als Netz nach
  (fünfte Immer-Frage in `WORKFLOW.md`); die Auslieferung lässt die Datei
  weg (Packliste + `ausliefern.py`); die Zeugnis-Belegpflicht liest sie
  als Quelle 7. Begründungen in `Kern/DECISIONS.md`. Die Auswertung
  passiert im Zeugnis — bewusst kein eigener Bau.
- [ ] **Zeugnis in zwei Zuschnitte teilen** — Isors Wunsch vom
  2026-09-04: eine Fassung nur zur Person (wie er programmiert, wo Hilfe
  nötig ist, wo er besser wurde) und eine volle mit Projektstand und
  Notenbild. Entschieden wird nach dem nächsten vollen Zeugnis — dann
  liegt ein Erfahrungswert vor, wie stark sich die beiden Hälften
  wirklich trennen.
- [ ] **Zeile „Setzt voraus:" im DECISIONS-Format** — In
  `Kern/DOC_RULES.md` eine vierte, **optionale** Zeile neben Was, Warum und
  Verworfen vorsehen: die Bedingung, unter der eine Entscheidung gilt und
  die selbst nicht entschieden wurde. Optional, weil die meisten
  Entscheidungen keine haben und eine Pflichtzeile mit „keine" zugemüllt
  würde. Anlass: Eine Entscheidung vom 2026-08-27 schrieb ihre Folge auf und
  ließ die Voraussetzung weg; eine Session plante einen Tag darauf
  (`Kern/STOERUNGEN.md`, 2026-08-28).

- [ ] **Doku-Pflicht „Abgabe-Abschnitt" an die Existenz des
  Abgabedokuments binden** — Die Development-Zeile der Doku-Pflicht und
  der Baustein-Begriff in `Kern/WORKFLOW.md` verlangen den Abgabetext
  auch dann, wenn es das Abgabedokument des Semesters noch gar nicht
  gibt; so entstand am 2026-09-06 ein PLAN-Auftrag ins Leere
  (`Kern/STOERUNGEN.md`). Ergänzung der Art „sobald es das
  Abgabedokument gibt — bis dahin sichern die TDD_NOTES die Fakten".

- [ ] **Session-Typ „Art" ausarbeiten** — `Kern/WORKFLOW.md` führt ihn
  seit dem 2026-07-17 als geplant und nie benutzt („Prompts für
  Bildgenerierung und Concept-Art"). Am 2026-09-06 lief die erste
  Art-Arbeit tatsächlich — als Brainstorm/Design-Abschnitt, weil es den
  Typ nicht gibt —, und `Kern/ART_RULES.md` beantwortet seither das
  *Verfahren*. Offen bleibt der **Typ**: eine Zeile in der
  Doku-Pflicht-Tabelle, und die Entscheidung, ob er überhaupt einer sein
  muss oder ob Brainstorm/Design mit den ART_RULES genügt. Belegt ist
  bisher nur, dass Design-Abschnitt plus ART_RULES getragen haben.

- [ ] **Epic C++ Coding Standard destillieren** — den Standard aus der
  Quelle in `Kern/CODE_GUIDELINES.md` → „C++ · Unreal — Epic C++ Coding
  Standard (vorgegeben)" einmal ganz durchgehen und das Arbeitsdestillat
  dort eintragen, wie es fürs Konsolenprojekt schon steht. Fällig vor
  dem ersten eigenen Unreal-Code (Unterrichtsblock des Moduls 5-101);
  angestoßen von Isor am 2026-09-08 — die Vorgabe ist Epics, nicht
  unsere.

- [x] **Dritte C++-Umgebung in `CODE_GUIDELINES.md` aufnehmen** — die
  Tabelle „C++ — welche Konvention wo gilt" führt nur Konsolenprojekt
  und Unreal; der 3D-Model-Viewer (OpenGL, Aufgabe 2 des Moduls 5-101)
  fehlt, obwohl er die dritte eigenständige C++-Umgebung des Semesters
  ist. Von Isor am 2026-09-08 über die Frage gefunden, ob der Viewer
  nicht ebenfalls ein Konsolenprojekt sei. Was der Aufgabentext hergibt
  (`Uni/Semester_3/VORJAHR_AUFGABEN.md`): „einheitliche
  Coding-Convention" steht als Feedbackelement bei Aufgabe 1 und
  Aufgabe 7, bei Aufgabe 2 dagegen nur „Code kommentiert und lesbar" —
  ausdrücklich verlangt ist die SAE-Konvention dort also nicht.
  Eingetragen wird erst nach der Rückfrage beim Dozenten
  (Unterricht am 2026-09-10), nicht auf diese Auslegung hin.
  **Erledigt am 2026-09-10:** Dozenten-Auskunft im Unterricht — die
  SAE-Konvention gilt auch für den Model-Viewer, wie fürs
  Konsolenprojekt; die Tabelle führt ihn jetzt als drittes Ziel.
  Belege: `Kern/LOG.md` (Eintrag), `Uni/LOG.md` (Auskunft).

- [ ] **Kommentar-Nachpflege ans Review anhängen** — Die Arbeitsteilung
  „Header, Summaries und Kommentare ergänzt Claude automatisch beim
  Review" (`Kern/CODE_GUIDELINES.md`, seit 2026-07-18) hat keinen
  Prüfpunkt: Das Review-Gate greift nur **vor** dem Coden, und am
  2026-09-11 wurde die Regel übergangen, bis Isor sie einforderte
  (`Kern/STOERUNGEN.md`). Als festen Punkt nach Coden/Review verankern,
  damit die Regel im Format liegt statt im Gedächtnis.

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
  prüft, was Claude an Engine-Code gebaut hat. **Der Modus selbst ist
  gebaut und in Betrieb:** Der Regler „Wer schreibt" steht in
  `Kern/WORKFLOW.md` (E21), und bei Harness-Arbeit tippt ohnehin Claude.
  Offen ist die zweite Hälfte. Für Harness-Werkzeuge ist das Gegenlesen
  gelebte Praxis, für Engine-/C++-Code gibt es kein Verfahren — und dort zählt
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
- [ ] **Sechster Punkt fürs Review-Gate: Widerspruch zu den DECISIONS** —
  Das Gate in `Kern/CODE_GUIDELINES.md` prüft Fattening, Enum-Sicherheit,
  Werkzeugwahl, Naming und Artifact-Bezug. Keiner dieser Punkte fragt, ob
  der Plan einer bereits getroffenen Entscheidung widerspricht — und genau
  daran ist am 2026-09-01 ein Gerüst durchgerutscht, das ein Panel sein
  eigenes GameObject abschalten ließ, obwohl `DECISIONS/UI.md` diesen Weg
  am 2026-08-16 mit einem gemessenen Fehlerbild verworfen hatte
  (`Kern/STOERUNGEN.md`). Gefunden hat es Isor, nicht die Prüfliste. Der
  Punkt trifft die Lücke, weil die DECISIONS die einzige Stelle sind, an
  der **verworfene** Wege festgehalten werden.
