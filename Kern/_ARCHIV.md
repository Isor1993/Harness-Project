# _ARCHIV.md — Kern, überholte Einträge

Ownership: Nur überholte Einträge der Kern-Schicht. Jeder nennt, wodurch
er abgelöst wurde. Wird nie aufgeräumt — ein Archiv wird selten gelesen,
seine Größe kostet nichts (`Kern/DOC_RULES.md`, Abschnitt 4).

---

## 2026-08-22 — Der „Erledigt"-Block der alten ROADMAP

**Abgelöst durch:** die Chroniken `Kern/LOG.md`, `Uni/LOG.md` und
`Projekte/Isor_Tower/LOG.md`.

**Was war das:** 48 Zeilen mit sechzehn abgehakten Punkten, überwiegend
Zusammenfassungen von Ereignissen, die ausführlicher im damaligen
`FEATURE_LOG.md` standen — der Block verwies selbst dorthin.

**Was übernommen wurde:**
- Sieben Harness-Bauten → `Kern/LOG.md` (Kern-Dateien, WORKFLOW,
  Knowledge-System, FEATURE_LOG/DECISIONS, CODE_GUIDELINES,
  Artifact-Seiten, Session-Typ Zeugnis)
- „GDD.md als Short GDD angelegt" → `Projekte/Isor_Tower/LOG.md`
- „Abgabe-Ordnerstruktur gebaut und befüllt" → `Uni/LOG.md`

**Was nicht übernommen wurde und warum:** Terrain-Pipeline,
Gras-Instancing, Threadoptimierung, Gras-Rendering, die neun Diagramme,
das fertige TDD und das TDD-Layout. Alle sieben standen bereits
ausführlich in den LOGs; eine zweite, kürzere Fassung wäre eine Kopie
gewesen und hätte gegen den Ein-Ort-Test verstoßen.

**Vollständiger Originaltext:** `ROADMAP.md` in
`C:\IsorBackup\99_Archiv\_Zu_Loeschen\2026-08-22_Harness_Umbau\`.

## 2026-08-22 — Grobziel und Nahziel der alten ROADMAP

**Grobziel** („Generischer Harness für Game-Dev- und Learn-Sessions,
.md-Dateien als Gedächtnis, Sessions als Wegwerf-Arbeitsräume") →
abgelöst durch `CLAUDE.md`, wo es seither in kürzerer Form steht. Eine
Zielbeschreibung ist keine Baureihenfolge.

**Nahziel** (zwei Phasen: bis zur Uni-Abgabe am 2026-08-21, danach
Ausrichtung am GDD) → überholt. Die Abgabe ist am 2026-08-20 hochgeladen;
die zweite Phase läuft seit dem 2026-08-22 und steht in `PLAN.md`.

## 2026-08-22 — Abgelöster Konventions-Eintrag: Sprache

Stand bis heute in `DECISIONS.md` und ist dort nicht mehr die gültige
Fassung. Die Begründung von damals bleibt hier nachlesbar.

**Abgelöst durch `Kern/DOC_RULES.md`, Abschnitt 9 (Sprachtabelle).**

*Hier stand bis zum 2026-08-22 auch der Eintrag „Versionsschema nach
Reifegrad" (2026-08-16). Er war fälschlich als abgelöst einsortiert:
`Kern/VERSIONIERUNG.md` nennt ihn seine Grundentscheidung und ergänzt
ihn ausdrücklich, ohne ihn umzustoßen. Er steht deshalb wieder in
`Kern/DECISIONS.md`, mit einer „Fortgeführt am"-Zeile (Befund A30 der
Abnahme).*

### 2026-07-17 — Sprache: Code englisch, Unterhaltung deutsch
Was: Code, Kommentare, Debug-Ausgaben und Commit-Messages ausnahmslos
Englisch; Harness-Doku und Unterhaltung mit Claude vorerst Deutsch.
Warum: GitHub-Repo ist englischsprachig, Fachbegriffe bleiben konsistent
mit der Unity-/C#-Welt; Deutsch hilft beim Lernen.
Verworfen: Sprachwahl je Situation; sofortige Englisch-Umstellung des
Harness (geparkt in ROADMAP „Später").

## 2026-08-23 — Der Notkern in der obersten CLAUDE.md

**Abgelöst durch:** den Struktur-Umbau auf Harness 2.0.0. Die Wurzel des
Repos ist seither der Harness selbst — die Datei, die automatisch lädt,
**ist** die Regeldatei. Damit entfällt die Voraussetzung, aus der der
Notkern entstand.

**Warum vollständig archiviert und nicht fortgeführt:** Bei den meisten
überholten Einträgen bleibt die Entscheidung gültig und nur ihre
Begründung altert; dann bekommt der Eintrag eine „Fortgeführt am"-Zeile.
Hier ist es umgekehrt: Der Notkern war **ausschließlich** die Antwort auf
die Frage „was gilt, wenn niemand der Weiterleitung folgt?". Es gibt
keine Weiterleitung mehr, also auch keine Frage. Ein „Fortgeführt" hätte
nichts fortzuführen.

**Originaltext, unverändert:**

> ## 2026-08-22 — Notkern in der obersten CLAUDE.md (Ergebnis von P1)
> Was: `Harness Project\CLAUDE.md` behält die Weiterleitung und trägt
> zusätzlich vier Regeln als benannte Kopie: Isor entscheidet · nichts in
> fremde Dateien · Rückfrage an der Weggabelung · zeigen statt vorstellen
> lassen. Dazu Sprache und „Claude committet nicht".
> Warum: Prüfung P1, gemessen in einer frischen Session vor dem ersten
> Werkzeugaufruf — von den drei `CLAUDE.md` lädt nur die oberste von
> selbst. Die im Unity-Root lädt erst beim Zugriff auf eine Datei darunter,
> die mit den echten Regeln nie. Ohne Notkern hängt jede Regel daran, dass
> dem Verweis gefolgt wird; bei knappem Kontext oder in einem Subagenten
> gilt dann gar nichts.
> Verworfen: alles so lassen (die Kette hielt im Test, aber aus Gehorsam,
> nicht aus Automatik) · die Regeln ganz nach oben ziehen (dann ist
> `Claude\` nicht mehr als Ganzes herausnehmbar, gegen die Schichten-Idee).

**Was von ihm bleibt:** nichts als Kopie — die vier Regeln stehen
unverändert in `CLAUDE.md`, jetzt als Original statt als Untergrenze.
Der Begriff „Notkern" ist aus `Kern/GLOSSARY.md` entfernt.

---

## 2026-08-26 — ROADMAP-Punkt „Knowledge-Archivierung automatisieren"

**Abgelöst durch:** nichts. Der Vorgang, den er automatisieren sollte,
ist am 2026-07-17 verworfen worden — der Punkt hat seither kein Objekt
mehr. An seine Stelle tritt Prüfung 8 in `Kern/Werkzeuge/pruefen.py`,
die etwas anderes tut (unten).

**Originaltext, unverändert** — Stand zuletzt unter „Später, nur bei
Bedarf" in `Kern/ROADMAP.md`:

> - [ ] **Knowledge-Archivierung automatisieren.**

**Was er einmal meinte:** Der Punkt stammt vom 2026-07-14 aus dem
allerersten ROADMAP-Entwurf und hieß dort vollständig „Erweiterung:
Knowledge-Archivierung automatisieren (Befehl/Skill) — erst nach
Praxistest". Zwei Zeilen darüber stand: „KNOWLEDGE.md — Puffer für
Gelerntes, wird ins externe Archiv ausgelagert". **Die „Archivierung"
war dieses Auslagern** — Gelerntes sollte zuerst in eine projektinterne
Pufferdatei und von dort in Sammelläufen ins externe Archiv wandern.

**Warum er hinfällig ist:** Die Puffer-Architektur wurde drei Tage
später verworfen. `Kern/DECISIONS.md`, 2026-07-17 („Knowledge als
externer Ordner"), Zeile Verworfen: „einzelne KNOWLEDGE.md im Projekt
als Puffer mit Auslagerung". Geschrieben wird seither direkt in den
externen Ordner; es gibt keinen Auslagerungsvorgang, den ein Skript
übernehmen könnte. Der Punkt überlebte nur, weil er beim Umbau auf
1.0.0 als Ein-Satz-Zeile mitwanderte — ohne das „was und warum", das
das Format der ROADMAP verlangt, und damit ohne die Angabe, die seine
Hinfälligkeit gezeigt hätte.

**Was an seiner Stelle steht:** Vor dem Archivieren wurde gemessen, ob
am Knowledge-Ordner etwas anderes zu automatisieren wäre (2026-08-26,
89 Dateien): sieben von sieben Themenordnern mit `README.md`, keine
Datei ohne `Quelle:`-Zeile, vier Artifact-IDs — alle vier gültig und im
`ARTIFACT_INDEX.md` geführt. Der Bestand trägt also, ein Skript zum
Aufräumen hätte nichts zu tun. Gebaut wurde deshalb nur die Sicherung
gegen den einen Schaden, der dort wirklich entstanden ist: fünfzehn tote
Artifact-Links am 2026-08-09, weil die Handregel „vor dem Löschen im
Knowledge nach der ID suchen" (`Kern/ARTIFACT_RULES.md`, Pflege)
vergessen wurde. Prüfung 8 hält die IDs beider Seiten gegeneinander —
erzwingen statt erinnern, dasselbe Muster wie beim SessionStart-Hook.

---

## 2026-08-26 — Befundliste `_HARNESS_PRUEFUNG_1_0_0.md`

**Abgelöst durch:** nichts — sie ist planmäßig abgelaufen. Eine
Befundliste gehört dem Durchgang, der sie erzeugt hat
(`Kern/WORKFLOW.md` → „Prüfung"); was überlebt, sind die Punkte in der
ROADMAP. Die Datei selbst liegt im Datenbaum unter
`99_Archiv\_Zu_Loeschen\2026-08-26_Pruefung_1_0_0\` (`Kern/PFADE.md` →
`DATENBAUM`).

**Was sie war:** Die Nachlese zur Version 1.0.0, gelaufen am 2026-08-23
in einer frischen Session gegen rund zwanzig Dateien, die am Bautag
geschrieben und nicht gegengelesen worden waren. Vierzehn Befunde in
drei Durchgängen — die neuen Regeln, die aus den Arbeitsdateien
geretteten Regeln, und ein Querschnitt über den Bestand nach
Widersprüchen. Alle vierzehn wurden am selben Tag in einem eigenen
Abschnitt behoben; die Liste trug dafür eine Tabelle „Behebung" mit der
Stelle je Befund, nachprüfbar statt abgehakt.

**Warum sie erst am 2026-08-26 ging:** Sie war seit dem 2026-08-23
archivierbar und blieb drei Tage in der Repo-Wurzel liegen. Aufgefallen
ist es erst, als Isor fragte, ob am Harness wirklich alles fertig sei —
kein Werkzeug hat es gemeldet, weil kein Werkzeug weiß, wann eine
temporäre Datei ihren Zweck erfüllt hat.

**Was vor dem Archivieren gerettet wurde** (`DOC_RULES.md`, Abschnitt 11
— eine Arbeitsdatei wird geschlossen, bevor sie geht): Ein einziger
Posten, und er stand nicht bei den Befunden, sondern im Abschnitt
„Stand": Die Prüfung hatte **`Kern/CODE_GUIDELINES.md` und die
Uni-Schicht ausdrücklich ausgelassen**, weil beide am 2026-08-23 nicht
angefasst worden waren. Diese Auslassung stand in keiner ROADMAP und
wäre mit der Datei verschwunden. Sie steht jetzt als eigener Punkt in
`Kern/ROADMAP.md` → „Die nie geprüfte Fläche nachholen". Die zwei
halb erledigten Aufträge, die die Liste selbst benannte (die
Automatisierung zu P4 und P13), sind seit dem 2026-08-23 gebaut —
Prüfungen 4 und 5 in `Kern/Werkzeuge/pruefen.py`.


