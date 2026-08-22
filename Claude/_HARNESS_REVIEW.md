# _HARNESS_REVIEW.md — Befundliste Harness-Überholung

Ownership: Arbeitsliste der Harness-Überholung vom 2026-08-21 ff.
Temporär — wird nach Abschluss ins Archiv verschoben und der
INDEX-Eintrag entfernt. Keine Dauerdatei.

Status je Punkt: `offen` · `entschieden` · `gebaut`

## Ziel dieser Überholung (Isor, 2026-08-21)

Der Harness wird auf eine **neue Fassung** gebracht: besser bedienbar,
stärker automatisiert, weniger Fehler, mehr Möglichkeiten. Zeit ist
**nicht** die Grenze — Gründlichkeit geht vor Tempo.
Grenzen, die dabei einzuhalten sind:
- nichts kaputtmachen,
- Zuständigkeiten dürfen sich nicht überlappen,
- es darf nicht unübersichtlich werden,
- es dürfen nicht zu viele laufende Kosten entstehen (Pflegeaufwand),
- alles, was sinnvoll geht, wird per Skill oder Automatisierung gelöst.

Danach folgt eine **Testphase** im laufenden Betrieb — Dauer offen,
mindestens bis Semesterbeginn, je nach Zeitbudget über das ganze
Semester.

## Ownership — Begriffsklärung (2026-08-21)

Isor kannte den Begriff aus einer Dozenten-Vorgabe, ohne ihn zu
verstehen. Festgehalten, weil er die Grundlage der ganzen Struktur ist —
gehört später in `DOC_RULES.md` und als erster Eintrag ins `GLOSSARY.md`.

**Definition:** Für jede Information gibt es genau ein Dokument, das sie
besitzt. Alle anderen dürfen darauf verweisen, sie aber nicht wiederholen.

**Schaden, den es verhindert:** Steht dieselbe Tatsache an drei Stellen
und wird an einer geändert, behaupten die Dokumente danach Verschiedenes
— und es ist nicht mehr erkennbar, welches stimmt. Alle sehen gleich
glaubwürdig aus (belegt durch C7).

**Kernsatz:** *Ownership schneidet nach der **Art** der Information, nicht
nach dem **Thema**.* Fünf Dokumente dürfen vom Terrain handeln, solange
jedes eine andere Art besitzt: Ereignis (LOG) · Begründung (DECISIONS) ·
Plan (ROADMAP) · Regel (CODE_GUIDELINES) · Absicht (GDD).
Daraus folgt die Struktur aus E11: **Schicht = Thema, Dokumentart = Art
der Information.**

**Drei Prüfungen:**
1. *Ein-Ort-Test* — Ändert sich die Tatsache: an wie vielen Stellen muss
   ich sie ändern? Antwort muss „an einer" sein.
2. *Widerspruchs-Test* — Können zwei Dateien darüber Verschiedenes
   behaupten? Dann ist die Zuständigkeit unklar.
3. *Verweis statt Kopie* — Braucht Datei B die Information, schreibt sie
   „siehe A", nicht die Information selbst.

## Vorgehen: Datei-für-Datei-Durchgang (E4, präzisiert 2026-08-21)

**Erst wird der gesamte Harness fertig entworfen — alle 25 Posten —,
dann wird gebaut.** Nicht: eine Datei entwerfen und gleich umsetzen.

### Prüfbogen, für jede Datei gleich
1. Welche Frage beantwortet sie, und beantwortet die sonst niemand? (E15)
2. Deckt sich die Ownership-Zeile mit dem tatsächlichen Inhalt?
3. Widerspricht sie einer anderen Datei? (Fehlertyp C7)
4. In welche Schicht gehört sie? (Kern / Uni / IsorBackup / Projekt)
5. Verfällt ihr Inhalt? → Archiv oder Erzeugung nötig, oder pflegefrei?
Ergebnis je Datei: Soll-Zustand plus konkreter Auftrag für die Bau-Session.

### Reihenfolge
- **A — Steuerung:** CLAUDE.md · WORKFLOW.md · INDEX.md (enthält I9, I11)
- **B — Werkzeug-Regeln:** KNOWLEDGE_RULES · ARTIFACT_RULES ·
  DIAGRAM_RULES · DOCX_RULES · ASSESSMENT_RULES (enthält I3, I4)
- **C — Bestände:** ARTIFACT_INDEX · ASSESSMENT_LOG · PREFAB_STATUS ·
  TDD_NOTES
- **D — Inhalt/Referenz:** CODE_GUIDELINES · GDD · ASSIGNMENT × 3
- **E — Geplante Dateien:** DOC_RULES · GLOSSARY · GDD_RULES —
  bauen oder streichen. Fund: `_split_check.txt` steht in keinem
  INDEX-Eintrag (8-Zeilen-Bruchstück vom Zeugnis 11.08.) → aufräumen.
- **F — Konflikt-Prüfung (Isors Forderung, eigener Schritt):**
  Zuständigkeits-Tabelle über alle Dateien — eine Zeile je Art von
  Information, eine Spalte „Besitzer". Zwei Besitzer = Konflikt, kein
  Besitzer = Lücke. Widersprüche liegen **zwischen** Dateien und sind
  beim Lesen einer einzelnen nicht sichtbar (deshalb eigener Schritt).
  Fängt zugleich Namensdoppelungen ab (Beispiel: zweiter INDEX, E6).

### E16 — Störungs-Dokument für die Testphase (entschieden 2026-08-21)
Eigene Datei, Vorschlag `Kern\STOERUNGEN.md` (ohne Umlaut, wie die
übrigen Dateinamen).

- **Frage, die sie besitzt:** *Was hat im Betrieb nicht funktioniert?* —
  beantwortet sonst kein Dokument. LOG besitzt „was ist passiert",
  STOERUNGEN besitzt „was ist schiefgegangen".
- **Format:** eine Zeile je Vorfall — Datum · was passiert ist · welche
  Regel nicht gegriffen hat · später: behoben am/wodurch.
- **Wer schreibt:** Claude trägt sofort ein, sobald Isor einen Aussetzer
  meldet; zusätzlich fragt die `/ende`-Routine danach — gleiches Muster
  wie die Knowledge-Frage (E2), damit es nicht ausfällt.
- **Begründung (Isor, 2026-08-21):** Nach der Testphase soll man es
  *sehen*, nicht *erinnern* müssen. Diese Überholung war nur möglich,
  weil elf konkrete Befunde vorlagen; ohne Belege wird die nächste
  Revision Ratearbeit.
- **Verfall:** Behobene Vorfälle bleiben stehen (Beleg dafür, dass die
  Änderung nötig war) — die Datei ist eine Chronik wie das LOG und
  braucht daher kein Archiv.

## Bereits entschieden (2026-08-21)

- **Reihenfolge:** Retro Punkt für Punkt zuerst, dann Umbau in eigenen
  Sessions je Baustein. Heute Brainstorm/Design — es wird nichts gebaut.
- **Drei Schichten:** Kern (generisch, mitkopierbar) · Uni (rein/raus) ·
  IsorBackup (angebunden, aber entnehmbar).
- **Umbenennung:** „Uni-Modus" heißt künftig **Lernmodus**.
- **IsorBackup** wird an den Harness angebunden. Fernziel: automatisiertes
  Backup auf externe Festplatte.

## Entscheidungen aus Retro-Runde 1 (2026-08-21)

- **E1 — Session-Ende (I1, I2, I8):** Zwei Auslöser. `/ende` auf Zuruf
  arbeitet die volle Checkliste ab; zusätzlich meldet Claude sich von
  selbst bei ca. 30 % Restkontext.
- **E2 — Knowledge (I3):** Die End-Routine fragt **automatisch**, ob eine
  Wissensseite gespeichert werden soll. Bei „ja" schlägt Claude die
  Themen vor, Isor wählt aus oder ergänzt, dann legt Claude sie an.
  Isor entscheidet — die Frage fällt aber nicht mehr aus.
- **E3 — Artifacts (I4):** Isor entscheidet fallweise. **Sonntag ist der
  allgemeine Pflegetag**; am Ende des Sonntags kommt ein Hinweis auf
  fällige Durchsicht.
  Offen für die Bau-Session: wodurch der Sonntags-Hinweis technisch
  ausgelöst wird (Prüfung beim Session-Start vs. geplante Aufgabe).

## Entscheidungen aus Retro-Runde 2 (2026-08-21) — DECISIONS

- **E4 — Vorgehen insgesamt:** Der Harness wird **Datei für Datei**
  durchgegangen: je Datei Problem benennen, Ziel entwerfen, entscheiden,
  hier festhalten. Erst danach wird gebaut. DECISIONS ist der Pilot.
- **E5 — Zielstruktur DECISIONS:** Ordner `Claude\Decisions\` mit vier
  Schichten als **Unterordner**; das Archiv liegt jeweils **innerhalb**
  seiner Schicht, damit es beim Herausnehmen automatisch mitgeht.

  ```
  Decisions/
    Harness/     Sessions.md (~15) · Konventionen.md (~10) · _Archiv.md
    Uni/         Abgabe.md (~23) · _Archiv.md
    IsorBackup/  (geplant — noch keine Entscheidung vorhanden)
    Projekte/
      Isor_Tower/  Terrain.md (~31) · UI.md (~17) · Welt.md (~14)
                   Audio.md (~10) · Entities.md (~7) · _Archiv.md
  ```

- **E6 — Kein zweiter INDEX.** Die oberste INDEX.md besitzt weiterhin die
  gesamte Landkarte und bekommt die neuen Zeilen. Im Decisions-Ordner
  liegt keine eigene Index-Datei. (Isors Einwand, 2026-08-21)
- **E7 — CODE_GUIDELINES.md wird nicht angefasst.** Begründung: Ein
  DECISIONS-Eintrag ist das **Protokoll** (was, warum, verworfen, mit
  Datum), CODE_GUIDELINES ist die **geltende Regel** zum Nachschlagen.
  Zwei Sorten Dokument, keine zwei Fassungen. Nichts wird kopiert.
- **E8 — Die ~13 Konventions-Einträge werden einzeln zugeordnet**
  (Isors Vorbehalt, bestätigt): Sie sind nicht vom selben Typ. Echte
  Code-Regeln, Ordner-Regeln, eine Regel über CODE_GUIDELINES selbst und
  mindestens ein Projekt-Fall (`Pipeline-Klassen loggen nicht`) liegen
  gemischt. In Viererpaketen in der Umzugs-Session.
- **E9 — Archive werden nie aufgeräumt.** Grund: Kosten einer Datei =
  Größe × Lesehäufigkeit; ein Archiv wird nicht routinemäßig gelesen.
  Einzige Pflicht: Jeder Archiv-Eintrag nennt, **wodurch** er abgelöst
  wurde, und jeder neue Eintrag nennt, **welchen** er ablöst.
- **E10 — Sicherer Umzug (verbindlich):** Commit vor dem Umzug ·
  Trennung per Skript an den `## `-Überschriften, kein Copy-Paste ·
  Nachzählung 133 rein / 133 raus, bei Differenz wird nichts geschrieben ·
  die alte DECISIONS.md wird nicht gelöscht, sondern nach
  `99_Archiv\_Zu_Loeschen\` verschoben.

## Entscheidungen aus Retro-Runde 3 (2026-08-21) — Gesamtstruktur

- **E11 — Schicht zuerst, Dokumentart darin. Ersetzt E5.** Begründung
  (Isors Anforderung „modular austauschbar"): Bei Ordnern je Dokumentart
  müsste man zum Herausnehmen der Uni an drei Stellen löschen. Mit
  Schicht-Ordnern ist es ein Ordner. Eine Regel, dreimal angewandt.

  ```
  Claude/
    PLAN.md                  ← der eine Arbeitsplan, schichtübergreifend
    CLAUDE.md · INDEX.md · WORKFLOW.md · …   ← Regeln, Ablage noch offen

    Kern/        ROADMAP.md · LOG.md · DECISIONS.md (~25) · _ARCHIV.md
    Uni/         ROADMAP.md · LOG.md · DECISIONS.md (~23) · _ARCHIV.md
    IsorBackup/  (geplant)
    Projekte/
      Isor_Tower/
        ROADMAP.md · LOG.md · SYSTEME.md (erzeugt) · _ARCHIV.md
        DECISIONS/   Terrain.md · UI.md · Welt.md · Audio.md · Entities.md
  ```

- **E12 — `PLAN.md` als eigener Arbeitsplan.** Eine Datei,
  schichtübergreifend, Zeitraum ein bis drei Wochen, max. ~100 Zeilen.
  Darf Tage und Stunden enthalten. Ist ein Zeitraum durch, wandert er als
  Ereignis ins LOG, erledigte Punkte werden im ROADMAP abgehakt, und
  `PLAN.md` wird **geleert, nicht archiviert** — die Geschichte steht im LOG.
  Belegt durch den eigenen Befund: Der 498-Zeilen-Block „Abgabe in zwei
  Ständen" war genau so ein Arbeitsplan, nur in der falschen Datei.

- **E13 — FEATURE_LOG wird zur Chronik (`LOG.md` je Schicht).**
  Beantwortet nur: *Wann ist was passiert?* Eine Chronik kann nie falsch
  werden, braucht daher **kein Archiv und keine Pflege**. Neue Einträge
  beschreiben das **Ereignis**, nicht den Ablageort — Pfadangaben
  veralten (Beispiel: Assets-Umsortierung am 2026-08-20). Bestehende
  Einträge bleiben unverändert, sie waren damals richtig.

- **E14 — Systemliste: Verfahren entschieden, Bau vertagt.**
  Frage, die sie beantwortet: *Was steckt gerade im Projekt drin?* — die
  heute kein Dokument beantwortet. Arbeitsteilung nach dem bewährten
  Muster der Diagramm-Skripte (DECISIONS 2026-08-08, „hält die Handarbeit
  über Neuerzeugungen"):
  - Das **Skript** besitzt die *Liste* (Systemordner, Klassennamen,
    Anzahl Skripte, letzte Änderung) → Vollständigkeit ist garantiert.
  - Der **Mensch/Claude** besitzt die *Kurzbeschreibung* (eine Zeile je
    System) → wird bei Neuerzeugung aus der alten Fassung übernommen.
  - Neue Systeme ohne Beschreibung werden als `⚠ fehlt` markiert,
    verschwundene als `⚠ nicht mehr vorhanden`. Damit kann nichts
    stillschweigend untergehen (Isors Einwand, 2026-08-21).
  - Körnung: **Systeme, nicht Features.** Je feiner ein Verzeichnis,
    desto schneller verfällt es.
  Bau steht auf der ROADMAP, nicht auf der Wochenend-Liste.

- **E15 — Maßstab für jedes Dokument:** Ein Dokument ist gerechtfertigt,
  wenn sich eine Frage nennen lässt, die es beantwortet und die sonst
  kein anderes Dokument beantwortet. Fällt keine ein, ist es eins zu viel.

### Neuer Befund C7 — Ownership-Widerspruch (ersetzt C3 teilweise)
FEATURE_LOG.md Z. 4–5: „Harness-Bauten stehen in ROADMAP.md unter
Erledigt." · ROADMAP.md Z. 3: „Was fertig ist, steht im FEATURE_LOG.md …
nie hier." **Beide Dateien schicken das Thema zur jeweils anderen.** Der
48-zeilige „Erledigt"-Block ist damit kein Verstoß, sondern die Folge
zweier sich widersprechender Regeln. Das ist vermutlich der Mechanismus
hinter Isors Befund I6 — nicht die einzelne Datei ist kaputt, sondern
zwei Zuständigkeiten überlappen sich. **Fehlertyp, nach dem beim
Datei-für-Datei-Durchgang gesucht wird.**

### Befund C8 — ROADMAP besteht zu 77 % aus Vergangenheit
708 Zeilen gesamt: Grobziel/Nahziel 20 (gilt) · Erledigt 48 (Geschichte) ·
Abgabe-Block 498 (Geschichte, Tagesplan Mi 12.08. bis So) · Nach der
Uni-Abgabe 102 (gilt) · Später 12 (gilt) · Nach der zweiten Abgabe 28
(gilt). **546 Zeilen Vergangenheit, ~162 Zeilen echte Baureihenfolge.**
Achtung beim Umbau: Aus dem Abgabe-Block gelten „Arbeitsregeln, die
weiter gelten" und „Restliste Politur" weiter — einzeln prüfen.

### Offen: Wohin mit den 546 Zeilen ROADMAP-Vergangenheit
Von Isor vertagt, bis die Struktur steht (jetzt: E11–E13). Erledigtes
gehört nach der neuen Ownership ins LOG der jeweiligen Schicht,
Verworfenes ins `_ARCHIV.md` der Schicht.

### Offen: Ablage der Regel-Dateien
CLAUDE, INDEX, WORKFLOW, CODE_GUIDELINES, ARTIFACT_RULES, DIAGRAM_RULES,
DOCX_RULES, KNOWLEDGE_RULES, ASSESSMENT_RULES/LOG, ASSIGNMENT_*,
TDD_NOTES, GDD, PREFAB_STATUS, ARTIFACT_INDEX — welche davon gehören in
`Kern/`, welche in `Uni/`, welche zu `Projekte/Isor_Tower/`, welche
bleiben oben liegen. Noch nicht besprochen.

## Datei-Durchgang · Gruppe A

### A1 — CLAUDE.md (25 Zeilen) — durch

**Frage, die sie besitzt:** *Wie verhält sich Claude hier, und was liest
er zuerst?* Berechtigt, beantwortet sonst niemand.

**Befunde**
- **A1-a:** Keine `Ownership:`-Zeile — als einzige von 21 Dateien.
- **A1-b (Ursache für I1 und I3):** Die Doku-Pflicht steht zweimal, in
  unterschiedlichem Umfang. CLAUDE.md Z. 19 nennt **zwei** Dokumente
  (INDEX, ROADMAP), WORKFLOW.md Z. 7 nennt **sechs** (INDEX, ROADMAP,
  FEATURE_LOG, DECISIONS, Knowledge, TDD_NOTES). CLAUDE.md wird immer
  gelesen, WORKFLOW steht an vierter Stelle der Leseordnung. Wer nur die
  Kurzfassung befolgt, macht ein Drittel und hält sich für vollständig —
  und **Knowledge fehlt in der Kurzfassung ganz**, was I3 erklärt.
  Kein Gedächtnisproblem, sondern ein Ownership-Fehler.
- **A1-c:** Die Leseordnung zieht 847 Zeilen ins Fenster (ROADMAP 708
  davon), bevor gearbeitet wird.
- **A1-d:** Drei CLAUDE.md-Dateien, zwei davon reine Weiterleitungen.
  Die echten Regeln erreicht nur, wer zwei Wegweisern folgt — Anweisung
  statt Mechanismus.

**Entscheidungen**
- **E17:** Die Doku-Pflicht gehört **WORKFLOW.md** (Session-Disziplin).
  CLAUDE.md verweist nur noch darauf. Der spätere `/ende`-Skill
  **führt sie aus** — ausführen und besitzen sind zwei verschiedene Dinge.
- **E18:** Neue Leseordnung: **CLAUDE → INDEX → PLAN → WORKFLOW**,
  zusammen ca. 250 statt 847 Zeilen (−70 %). Die ROADMAP einer Schicht
  wird erst gelesen, wenn an ihr gearbeitet wird.
- **E19:** CLAUDE.md bekommt eine `Ownership:`-Zeile wie alle anderen.
- **E20:** `DOC_RULES.md` wird gebaut und besitzt **Pflege *und*
  Ownership** — Ownership-Definition, die drei Prüfungen, Archiv-Regeln,
  Kopf- und Formatvorgaben. Die drei Doku-Regeln aus CLAUDE.md ziehen
  dorthin um.
  *Beleg gegen Doppelung (Ein-Ort-Test, 2026-08-21):* 20 von 21 Dateien
  führen eine `Ownership:`-Zeile, **aber nirgends steht, dass sie das
  sollen** — Gewohnheit ohne Regel. Nur 3 von 21 haben eine
  `Format:`-Zeile (DECISIONS, FEATURE_LOG, TDD_NOTES); deshalb ist
  FEATURE_LOG eine flache Liste ohne Gliederung. Die fünf bestehenden
  `*_RULES`-Dateien regeln **äußere Erzeugnisse** (Wissensseiten,
  .drawio, .docx, Artifact-Seiten, Zeugnisse), nicht die eigenen
  .md-Dateien. Die Zuständigkeit ist also unbesetzt.

**Offene Prüfung P1 — nächste Session, vor dem ersten Öffnen einer Datei**
Feststellen, welche der drei CLAUDE.md-Dateien der Harness **von selbst**
lädt. Belegt aus dieser Session: Nr. 1 (Repo-Wurzel) und Nr. 2 (Unity-Root)
kamen automatisch. Ob Nr. 3 (`Claude\CLAUDE.md`) ebenfalls automatisch
käme, ist **nicht feststellbar** — sie wurde zu Beginn manuell gelesen,
die Beobachtung ist verdorben. Erst nach dieser Prüfung wird über das
Zusammenziehen entschieden.

### A2 — WORKFLOW.md (83 Zeilen) — durch

**Frage, die sie besitzt:** *Wie läuft eine Session ab, welche Sorten
gibt es?* Berechtigt. Ownership-Zeile deckt sich mit dem Inhalt.
**Schicht:** Kern.

**Befunde**
- **A2-a — Namenskollision (heute selbst erzeugt):** WORKFLOW Z. 33 nennt
  den Brainstorm-Modus „normal/uni" (regelt **Erklärtiefe**), Z. 47 nennt
  den Development-Fall „Lern-Modus" (regelt **wer tippt**). Zwei Achsen,
  ähnlicher Name — und die Umbenennung uni→Lernmodus hätte beide gleich
  benannt.
- **A2-b:** Die Regler hängen am Session-*Typ*. Folge: Eine
  Development-Session darf nicht ausführlich erklären, obwohl dort am
  meisten gelernt wird — vermutlich ein Teil von I3.
- **A2-c:** Statusvermerke sind aus dem Juli und stimmen nicht mehr
  („im Einsatz, getestet", „erster Praxistest: Chunk-Umbau",
  „minimal, ungetestet").
- **A2-d:** Der Commit-Vorschlag ist in WORKFLOW klar geregelt (Schema,
  Englisch, zwei Textblöcke, GitHub Desktop). I2 ist also **kein
  Regel-, sondern ein Ausführungsfehler** → gehört automatisiert, nicht
  neu geregelt.

**Entscheidungen**
- **E21 — Ein Modus, zwei Regler.** Am Anfang **jeder** Session (nicht
  nur Design) wird der Modus gefragt: **Lernmodus** oder **Normal**.
  Er setzt die Voreinstellungen. Zwei Regler sind einzeln überschreibbar,
  ohne den Modus zu wechseln:

  | Regler | Stufen | Lernmodus | Normal |
  |---|---|---|---|
  | Visualisierung | viel · wenig · keine | viel | wenig |
  | Wer schreibt (nur Development) | Isor · Claude | Isor | Claude |

  *Erklärtiefe bekommt bewusst keinen eigenen Regler* — sie bewegt sich
  nie allein, nur der Bild-Anteil wird bei knappem Nutzungslimit gesenkt.
  *Der zweite Regler heißt „Wer schreibt", kein Modus-Name* — damit ist
  die Kollision A2-a dauerhaft ausgeschlossen.
  Erledigt zugleich **I10**: Der Visualisierungsgrad wird ein Regler,
  kein eigener Skill.
- **E22 — Session-Typ „Art" bleibt, aber als „(geplant)"** gekennzeichnet
  (Isor 2026-08-21): wird später wichtig, aber jetzt fehlt die Zeit, den
  besten Weg zu entscheiden. Statusvermerke aller vier Typen werden auf
  den heutigen Stand gebracht.
- **E23 — Drei Befehle, ein gemeinsamer Kern** (Isors Vorschlag,
  2026-08-21):
  - `/sichern` — Doku-Pflicht abarbeiten, Session läuft weiter
  - `/wechsel <Typ>` — `/sichern` + Typ umstellen + Modus/Regler neu
    fragen; **spart das Neu-Einlesen des Kontexts**
  - `/ende` — `/sichern` + Commit-Vorschlag mit V-Nummer + Schluss
  Die Doku-Pflicht wird **einmal** definiert (E17: WORKFLOW.md besitzt
  sie) und dreimal benutzt — nicht in drei Befehlen abgeschrieben.
- **E24 — Wechsel Design → Development in derselben Session bleibt
  erlaubt**, ist aber ein Kontrollpunkt: Entscheidungen werden **vorher**
  festgeschrieben, nicht am Session-Ende. Grund: Ist der Kontext im Bauen
  aufgebraucht, ist die Design-Begründung verloren, bevor sie geschrieben
  wurde. Umgesetzt durch `/wechsel`. Die 30-%-Regel bleibt daneben.
  *Bewertung der bisherigen Praxis (Isors Frage):* Das Vorgehen war
  richtig — der Entwurf steht beim Bauen noch im Kontext, eine neue
  Session müsste ihn aus DECISIONS rekonstruieren und verlöre dabei das,
  was nur im Kopf stand.

**Glossar-Kandidat:** „Work Area" (Isors Wort) = das, was WORKFLOW.md
„Session" nennt. Muss im GLOSSARY festgelegt werden.

### A3 — INDEX.md (31 Zeilen) — durch

**Frage, die sie besitzt:** *Welche Dokumente gibt es, wofür ist jedes
zuständig?* Berechtigt. **Schicht:** Kern, bleibt oben (Landkarte über
alle Schichten).

**Befunde**
- **A3-a:** Ownership-Zeile verspricht „eine Zeile pro Dokument, **keine
  Inhalte**" — tatsächlich stehen Statusangaben drin, die WORKFLOW.md
  gehören („im Einsatz", „im Praxistest", „minimal"). Weil sie doppelt
  stehen, sind sie **an beiden Orten veraltet**.
- **A3-b:** Der Verweis „PREFAB_STATUS … Arbeitsliste zu **ROADMAP-Punkt
  10**" ist bereits falsch: Punkt 10 ist heute der Ladebildschirm, die
  Prefab-Arbeitsliste ist Punkt 13. Nummern verschieben sich beim
  Einfügen und Abhaken; der Verweis zeigt still auf das Falsche.

**Entscheidungen**
- **E25 — INDEX.md wird erzeugt.** Ein Skript liest die
  `Ownership:`-Zeile jeder Datei und baut daraus die Tabelle.
  Wirkung: Der INDEX kann nicht mehr veralten · die Regel „keine neue
  Datei ohne INDEX-Eintrag" wird **mechanisch** durchgesetzt (Datei ohne
  `Ownership:`-Zeile erscheint als ⚠) · Streuner wie `_split_check.txt`
  fallen sofort auf · Ein-Ort-Test erfüllt, die Zuständigkeit steht nur
  noch im Dokument selbst.
  *Voraussetzung:* CLAUDE.md bekommt seine fehlende Ownership-Zeile (E19).
  Drittes Vorkommen des Musters **erzeugen statt pflegen** (nach E14
  Systemliste und den Diagramm-Skripten).
- **E26 — Statusangaben raus aus dem INDEX.** Sie gehören WORKFLOW.md.
- **E27 — Verweise nur über Namen, nie über Nummern.**
  Format: Pfad **und** Überschrift —
  `Projekte/Isor_Tower/ROADMAP.md → „Prefab-Struktur prüfen"`.
  Grundsatz: *Sichtbar kaputt ist besser als still falsch.* Ein
  Namensverweis, dessen Ziel umbenannt wurde, findet nichts; ein
  Nummernverweis findet den falschen Punkt.
- **E28 — Gleiche Dateinamen je Schicht bleiben** (Isors Einwand zur
  Namensdoppelung, 2026-08-21): Es wird künftig drei `ROADMAP.md`,
  drei `LOG.md` und drei `_ARCHIV.md` geben. Kein Umbenennen zu
  `ROADMAP_Uni.md` — das widerspräche E11, weil eine Schicht ein
  herausnehmbarer, kopierbarer Ordner sein soll und der Dateiname sonst
  den alten Schichtnamen mitträgt. Der Ordner unterscheidet bereits.
  Dafür zwei Sprachregeln in DOC_RULES:
  - Im Gespräch nie bloß „die Roadmap", immer mit Schicht
    („die Uni-Roadmap", „die Kern-Roadmap").
  - Im Text nie ein nackter Dateiname, immer Pfad + Überschrift (E27).

**Gruppe A ist damit abgeschlossen (3 von 3).**

## Datei-Durchgang · Gruppe B

### B1 — KNOWLEDGE_RULES.md (33 Zeilen) — durch

**Frage, die sie besitzt:** *Wo und wie wird projektübergreifendes Wissen
abgelegt?* Berechtigt. **Schicht:** Kern — ein Wissensarchiv ist Teil des
Harness und ausdrücklich projektübergreifend. Eine eigene Schicht
„Knowledge" wäre nach E15 nicht gerechtfertigt (anders als IsorBackup,
das gezielt herausnehmbar sein soll).

**Befunde**
- **B1-a — Selbstwiderspruch:** Z. 15 sagt „Kein eigener Index: Der
  Ordnerbaum ist der Index", Z. 11 führt vier Zeilen darüber einen
  („Bestand: Patterns/, Unity/, ProcGen/, CSharp/, Seiten/"). Diese Liste
  war **nach acht Stunden falsch** — `Dokumentation/` wurde am 2026-08-22
  angelegt und fehlt. Kürzester belegter Verfall im ganzen Durchgang.
- **B1-b — Kreisverweis:** WORKFLOW Z. 9 verweist für die
  Knowledge-Abfrage auf KNOWLEDGE_RULES, KNOWLEDGE_RULES Z. 28 verweist
  zurück auf WORKFLOW. Kein inhaltlicher Widerspruch, aber die
  Zuständigkeit ist unbesetzt — gleicher Typ wie C7.
- **B1-c:** Bestand am 2026-08-22: 66 Dateien in sechs Gruppen — Unity 27,
  ProcGen 14, Patterns 11, Seiten 6, CSharp 4, Dokumentation 4.
- **B1-d:** Der Root-`README.md` des Knowledge-Repos enthält nur die Zeile
  `# Knowledge`. Wer das Repo allein öffnet, hat keine Orientierung — die
  Regeln liegen in einem anderen Repo.

**Entscheidungen**
- **E29 — WORKFLOW.md besitzt das „wann"**, KNOWLEDGE_RULES das „wohin
  und wie" (Ablageort, Ordnerstruktur, Dateiformat, Namensschema).
  Konsequent zu E17.
- **E30 — Bestandsliste ersatzlos streichen. Statt dessen ein
  `README.md` je Themenordner** mit einer Zeile, was die Gruppe enthält.
  Begründung: Die Liste enthielt nur Ordnernamen — sie zu *erzeugen* wäre
  ein Skript, das `ls` nachbaut, ohne Informationsgewinn. Was fehlt, ist
  die **Bedeutung** je Gruppe (`Seiten/` = Offline-Kopien der
  Artifact-Seiten rät niemand; `Dokumentation/` ist mit der
  Uni-Dokumentation verwechselbar). Die Beschreibung gehört dorthin, wo
  sie beschrieben wird, und entsteht mit dem Ordner.
  *Grundsatz:* **Erst Ownership klären, dann automatisieren.** Ein Skript,
  das eine überflüssige Kopie pflegt, macht die Kopie nicht richtig, nur
  pünktlich. Fehlt ein README, sieht man es im Ordner — fehlt eine Zeile
  in einer Liste, ist die Liste still unvollständig (B1-a).
  Eine erzeugte Übersichtsseite bleibt später möglich, dann aus den
  READMEs — dort verdient das Erzeugen sein Geld, weil die Quelle
  woanders liegt.
- **E31 — Root-`README.md` bekommt eine kurze Orientierung** (5–10
  Zeilen): was der Ordner ist, wie er organisiert ist, wo die Regeln dazu
  liegen (Verweis in den Harness). Damit ist das Repo auch allein
  verständlich.
- **E32 — Wissensseiten werden nur bei visuellen Themen zusätzlich als
  Artifact gebaut** (Diagramme, Zahlenbeispiele, Vergleiche). Reiner Text
  liest sich in der .md genauso gut. Die Regel selbst gehört in
  ARTIFACT_RULES.md (B2), nicht hierher.
- **Folgeänderung aus E21:** In Z. 28 wird „Uni-Modus" zu „Lernmodus",
  und der Zusatz „in Brainstorm-Sessions" entfällt — der Modus gilt
  künftig für alle Session-Typen.

### B2 — ARTIFACT_RULES.md (110 Zeilen) — durch

**Frage, die sie besitzt:** *Wie sind Artifact-Seiten aufgebaut, benannt
und gepflegt?* Berechtigt. Die Datei grenzt sich selbst sauber ab (Z. 8:
„Diese Datei besitzt die Regeln, der Index den Bestand") und begründet
ihre Existenz. Ownership deckt sich. **Schicht:** Kern.

**Befunde**
- **B2-a — Kopie, die schon auseinanderläuft:** Der Artifact-Check steht
  in CODE_GUIDELINES Z. 249 (Review-Gate, Punkt 5) und in ARTIFACT_RULES
  Z. 77–80 fast wörtlich doppelt. Unterschied bereits vorhanden:
  „wird **nach dem Coden** nachgezogen" gegen „gehört **mit**
  nachgezogen". WORKFLOW.md macht es dagegen richtig — dort steht nur ein
  Verweis.
- **B2-b — Lücke hinter I4:** Die Datei regelt genau, *wann man auf eine
  Seite schaut* (Z. 72–82), aber nicht, *wann eine Seite entsteht* und
  wann der Bestand als Ganzes durchgesehen wird.
- **B2-c:** Die Tabelle heißt „Die drei Typen" und hat vier Zeilen. Die
  vierte (`🗑 veraltet`) ist ein **Zustand**, kein Typ.
- **B2-d:** Die Spalte „Führende Quelle" nennt ROADMAP, FEATURE_LOG,
  DECISIONS, TDD_NOTES — alle vier werden gerade umgebaut. Nach dem Umzug
  nachziehen (Status-Seite: künftig PLAN.md + ROADMAP der Schicht).

**Entscheidungen**
- **E33 — Der Artifact-Check bleibt vollständig im Review-Gate**
  (CODE_GUIDELINES, Punkt 5). ARTIFACT_RULES streicht die vier
  abgeschriebenen Zeilen und behält einen Verweis.
  *Grundsatz:* **Eine Checkliste gehört dem Moment, nicht den Themen.**
  Eine Liste, deren fünf Punkte auf fünf Dateien zeigen, ist keine
  Checkliste mehr. Themendateien verweisen auf das Gate, nicht umgekehrt.
  Ergänzt E29: **WORKFLOW besitzt den Zeitpunkt, die Fachdatei den
  Inhalt** — WORKFLOW verweist bereits korrekt aufs Gate.
- **E34 — Sonntags-Pflegetag konkretisiert (schließt I4):** Claude
  gleicht ARTIFACT_INDEX gegen die Änderungen der Woche ab und legt eine
  **Vorschlagsliste** vor — welche Seite veraltet ist, was drinsteht, was
  sich geändert hat. Isor entscheidet, welche nachgezogen werden.
  Nicht selbsttätig ändern.
- **E35 — Die Harness-Seite (I12) wird `⚙️ System · Harness`.** Kein
  vierter Typ: Der Harness ist ein System, das Isor gebaut hat, und die
  Frage „wie funktioniert mein System X" passt. Führende Quelle sind die
  Kern-Dateien.
- **E36 — `🗑` verlässt die Typentabelle** und wird im Abschnitt „Pflege"
  erklärt, wo es ohnehin vorkommt. Dann stimmt die Überschrift wieder.

**Vormerkung für Gruppe C:** `ARTIFACT_INDEX.md` führt Seiten über
Isor-Tower-Systeme, übertragbare Lernstücke **und** Zeugnisse — der
Bestand läuft quer über drei Schichten und kollidiert mit E11. Muss beim
Index gelöst werden, nicht in den Regeln.

### B3 — DIAGRAM_RULES.md (108 Zeilen) — durch

**Frage, die sie besitzt:** *Wie gehe ich mit den erzeugten
`.drawio`-Diagrammen um?* Berechtigt. Ownership vorbildlich: verweist für
die Begründung auf DECISIONS 2026-08-06 und für Gebautes aufs
FEATURE_LOG, statt abzuschreiben. Die Bedienregeln stammen erkennbar aus
echten Fehlern. **Schicht:** Kern (Verfahren), siehe B3-a.

**Befunde**
- **B3-a — Kern-Regeln mit Uni-Pfaden:** Quellen liegen unter
  `01_Uni\Semester_2\Diagramme_Quellen\`. Das Verfahren ist generisch,
  der Ablageort hängt am zweiten Semester. Inhaltlich passt es außerdem
  nicht: Die neun Diagramme beschreiben **Isor's Tower** (Terrain,
  Sheep-FSM, Gras) — die Uni hat sie nur benutzt. Spiegelbild von C6.
- **B3-b — dritter Diagrammtyp ungeregelt:** Neben `diagramm_<name>.py`
  und `ablauf_<name>.py` existiert `zustand_sheep_fsm.py` →
  `Zustand_Sheep_FSM.drawio`, also ein **Zustandsdiagramm** mit eigenem
  Muster `zustand_<name>.py`. In den Regeln kommt es nur beiläufig in
  Bedienregel 5 als Fehlerbeispiel vor; kein eigener Abschnitt, keine
  Aussage zum Prüferlauf.
- **B3-c — bewusste Ausnahme von E30:** Die Skriptliste (Z. 11–15) ist
  dieselbe Bauform wie die gestrichene Knowledge-Liste, **hält aber seit
  zwei Wochen** (alle drei genannten Dateien geprüft, 2026-08-22). Sie
  bleibt, weil sie erklärt, *was* jedes Skript tut (Kriterium aus E30),
  und weil Werkzeuge sich selten ändern.
  *Grundsatz:* **Dieselbe Bauform ist nicht überall gleich riskant** —
  eine Liste verfällt so schnell, wie ihr Gegenstand sich ändert.
  Themenordner wachsen ständig (8 Stunden), Werkzeuge kaum.

**Entscheidungen**
- **E37 — Konkrete Pfade raus, Ablage folgt der Schicht.**
  DIAGRAM_RULES beschreibt nur noch das Verfahren; wo die Quellen liegen,
  bestimmt die Schicht (Projekt-Diagramme beim Projekt, Uni-Diagramme bei
  der Uni). Damit wird die Datei semester- und projektunabhängig und ist
  beim Kopieren des Harness sofort brauchbar.
  *Offen für die Bau-Session:* ob die neun bestehenden `.drawio`-Quellen
  physisch aus `01_Uni\Semester_2\` herauswandern — das ist ein
  Dateiumzug, kein Regelthema.
- **E38 — Das Zustandsdiagramm bekommt einen eigenen Abschnitt**, nach
  dem Muster der Ablaufpläne: Namensschema `zustand_<name>.py`, was ein
  Lauf erhält, ob ein Prüferlauf gilt.

### B4 — DOCX_RULES.md (91 Zeilen) — durch

**Frage, die sie besitzt:** *Wie arbeite ich sicher an den
`.docx`-Abgabedateien?* Berechtigt. Entstanden aus echtem Schaden.
**Schicht: Uni** — die erste Datei im Durchgang, die eindeutig dorthin
gehört.

**Befunde**
- **B4-a — Zählwort veraltet:** Z. 31 sagt „**Alle vier** sind
  aufgetreten", darunter stehen **sechs** Punkte (Nr. 6 datiert
  2026-08-17). Gleicher Mechanismus wie B2-c („Die drei Typen" mit vier
  Zeilen). Zweimal derselbe Fehler in zwei Dateien = Muster.
- **B4-b — zwei Sorten Wissen in einer Datei:** Sicherung, Arbeitsteilung
  und Prüfablauf gelten dem TDD-Workflow; die Formatvorgaben den
  SAE-Abgaben; **die sechs XML-Fallen aber jedem Word-Dokument überall**
  (`<w:t[^>]*>` trifft auch `<w:tc>`; Fließtext über Runs zerstückelt;
  `count=1` trifft beim Zeilenklonen immer dieselbe Zelle). Beim
  Ausmustern der Uni-Schicht ginge dieses Wissen verloren.
- **B4-c — Werkzeuglücke:** Im Harness liegt ein **docx-Skill** mit
  Hilfsskripten, den Isor im August benutzt hat (`validate.py`,
  `soffice.py`). In DOCX_RULES steht davon kein Wort; die Regeln
  beschreiben durchweg Handarbeit am entpackten XML.

**Entscheidungen**
- **E39 — Die XML-Fallen wandern ins Knowledge-Archiv** (eigene Seite),
  DOCX_RULES behält einen Verweis. Begründung: teuer bezahltes,
  übertragbares Werkzeugwissen überlebt so die Uni-Schicht — genau der
  Zweck des Archivs („Wissen ist projektübergreifend").
- **E40 — Der docx-Skill wird als Abschnitt „Werkzeuge" aufgenommen:**
  was er kann, wofür er benutzt wird (Prüfen, PDF-Export), und wo
  weiterhin Handarbeit am XML nötig ist. Der Prüfschritt „XML
  wohlgeformt" wird auf `validate.py` umgestellt.
- **E41 — Allgemeine Regel für DOC_RULES:** *Keine Anzahl in Überschrift
  oder Einleitung, wenn die Liste wachsen kann.* Betroffen heute:
  DOCX_RULES Z. 31 und ARTIFACT_RULES „Die drei Typen".

### B5 — ASSESSMENT_RULES.md (115 Zeilen) — durch

**Frage, die sie besitzt:** *Wie läuft ein Zeugnis ab?* Berechtigt.
**Vorbild für alle anderen Regeldateien:** begründet ihre Existenz (Z. 7),
verweist auf WORKFLOW statt abzuschreiben (Z. 34) und **benennt ihre
eigene Ausnahme ausdrücklich** samt Begründung (Z. 91–104: „eine benannte
Ausnahme, die diese Datei besitzt" — pro Zeugnis eine eigene URL, weil
der alte Stand hier der halbe Zweck ist). Eine Ausnahme mit Besitzer und
Begründung ist keine Unordnung.

**Befunde**
- **B5-a:** WORKFLOW.md Z. 80–83 wiederholt die abweichende Doku-Pflicht
  wörtlich, obwohl im selben Absatz „Eigene Regeln in
  ASSESSMENT_RULES.md" steht.
- **B5-b — Konflikt mit E2:** Diese Datei verbietet Knowledge-Einträge
  aus Zeugnis-Sessions; E2 verlangt die Frage bei jedem Session-Ende.
- **B5-c — wichtige Folge für den Bau von `/ende`:**
  **Die Doku-Pflicht ist keine einzige Liste — sie hängt am Session-Typ.**
  Eine Zeugnis-Session schreibt in andere Dateien als eine
  Development-Session. Weiß `/ende` das nicht, macht er zu viel oder zu
  wenig. Muss in den Entwurf der Befehle (E23) einfließen.
- **B5-d:** Uni-Anteile in einer sonst generischen Datei — UK-Notenskala
  (Z. 63–69), `ASSIGNMENT_*`, Pfad `01_Uni\Semester_<n>\Arbeitsdateien\`.
  Rund 15 von 115 Zeilen.

**Entscheidungen**
- **E42 — ASSESSMENT_RULES bleibt ganz im Kern.** Die Datei sagt künftig:
  *Die Bewertungskriterien liefert die aktive Schicht* — die Uni liefert
  UK-Skala und ASSIGNMENT-Dateien. Kein Zerschneiden für 15 Zeilen. Nimmt
  man die Uni heraus, bleibt das Ritual heil und braucht nur einen neuen
  Maßstab.
- **E43 — WORKFLOW streicht die wiederholte Zeugnis-Doku-Pflicht** und
  behält nur Typname, Anlass und den Zeiger hierher. Konsequent zu E17,
  E29 und E33.
- **E44 — Die Knowledge-Frage wird auch bei Zeugnissen gestellt**,
  Antwort ist in der Regel „nein". Fällt beim Bewerten doch etwas
  Übertragbares auf, darf es festgehalten werden. E2 bleibt damit
  ausnahmslos: Die **Frage** fällt nie aus, die **Antwort** darf leer sein.

**Gruppe B ist abgeschlossen (5 von 5).**

## Datei-Durchgang · Gruppe C

### C1 — ARTIFACT_INDEX.md (210 Zeilen, 12 Seiten) — durch

**Frage, die sie besitzt:** *Welche Artifact-Seiten gibt es, woran hängt
jede?* Berechtigt, sauber gegen ARTIFACT_RULES abgegrenzt.
Bestand: 1 Status · 2 Zeugnisse · 3 System · 6 Lernstücke.

**Befunde**
- **C1-a:** Der Review-Gate-Zweck steht hier zum **dritten** Mal (Z. 6–10)
  — nach CODE_GUIDELINES (Besitzer) und ARTIFACT_RULES (B2-a).
- **C1-b:** Stand-Stempel falsch. Z. 210 sagt „Stand dieses Index:
  2026-08-12", Z. 48 führt aber das Zeugnis vom **16.08.** Gepflegt
  wurde, der Stempel nicht. Gleicher Mechanismus wie E41.
- **C1-c:** Der Abschnitt „Offene Punkte" (Z. 201–208) enthält **Aufgaben**
  in einer Bestandsdatei.
- **C1-d:** Der Bestand läuft über drei Schichten — Status und System
  (4) = Projekt, Zeugnisse (2) = Uni, Lernstücke (6) = Kern.

**Entscheidungen**
- **E45 — Eine Datei im Kern, Schicht als Angabe je Eintrag.**
  **Benannte Ausnahme von E11**, nach dem Vorbild von ASSESSMENT_RULES:
  Die Ausnahme steht mit Begründung in der Datei selbst.
  *Grundsatz:* **Ein Register muss vollständig sein, sonst erfüllt es
  seinen Zweck nicht.** Die Hauptzusage des Index (Z. 12: „Nie eine
  zweite Seite zum selben Thema anlegen") kann nur eine vollständige
  Liste geben; drei Teillisten heißen dreimal nachsehen. Schichten ordnen
  *Inhalt* — ein Verzeichnis fremder Adressen ist kein Inhalt.
  Zweitgrund: Wird die Uni-Schicht ausgemustert, verschwinden die
  Zeugnis-**Seiten** nicht (sie liegen auf claude.ai). Eine gelöschte
  Indexzeile erzeugte genau das, was die Tabelle „Gelöschte Seiten"
  verhindern soll — eine URL ohne Erklärung.
- **E46 — Die „Offenen Punkte" wandern in die Kern-ROADMAP.** Der Index
  behält reinen Bestand.
- **E47 — E34 wird um einen maschinellen Abgleich erweitert:** Am
  Sonntag holt Claude die Liste der **tatsächlich veröffentlichten**
  Seiten (Titel, URL, letzte Änderung) und vergleicht sie mit dem Index —
  Seite ohne Eintrag, Eintrag ohne Seite, Seite neuer als ihr
  Stand-Stempel. Zweite unabhängige Quelle statt Gedächtnis; C1-b wäre so
  am ersten Sonntag aufgefallen.

### C2 — PREFAB_STATUS.md (67 Zeilen, 30 Einträge) — durch

**Frage, die sie besitzt:** *Welche Prefabs sind durchgesehen, was fiel
auf?* Berechtigt. **Ownership-Zeile ist die strengste im Harness** —
schließt Aufgabenplanung, Begründungen und Fertiges ausdrücklich aus.
**Schicht:** Projekte/Isor_Tower.

**Befunde**
- **C2-a — zwei kaputte Nummernverweise, beide still falsch:**
  Z. 4 „das ist ROADMAP **Punkt 10**" → Punkt 10 ist der Ladebildschirm,
  richtig wäre 13. Z. 40 „Relevant für ROADMAP-**Punkt 7** (Gegner über
  den Placer)" → Punkt 7 ist die GameObject-/Prefab-Aufbau-Konvention.
  Dritter Fall nach A3-b; **E27 ist damit gut belegt.**
- **C2-b — Bestand nachweislich veraltet:** Kopfzeile sagt „Stand:
  2026-08-16. 33 Prefabs", auf der Platte liegen am 2026-08-22 **34**.
  Es fehlt `VFX_FireFly.prefab` (angelegt 2026-08-20, Glühwürmchen). In
  keiner der vier Tabellen.
  *Grundsatz:* **Ein Verzeichnis merkt nicht, dass etwas Neues
  existiert** — es zeigt nur, was jemand hineingeschrieben hat.

**Entscheidungen**
- **E48 — PREFAB_STATUS wird erzeugt, nach dem E14-Muster.** Das Skript
  liest alle `.prefab`-Dateien und baut die Tabelle; Status- und
  Befundspalte werden über den Prefab-Namen aus der alten Fassung
  übernommen. Neue erscheinen als `offen`, verschwundene als `⚠ nicht
  mehr vorhanden`. Damit wäre C2-b am 20.08. von selbst aufgefallen.
- **E49 — Die Datei ist eine Arbeitsliste mit Ende.** Sind alle Prefabs
  `geprüft`, wandern offene Befunde als Aufgaben in die Projekt-ROADMAP
  und die Datei ins `_ARCHIV.md` der Projekt-Schicht — wie
  `_HARNESS_REVIEW.md`. Danach keine Pflegepflicht mehr.

### C3 — TDD_NOTES.md (556 Zeilen, 85 Einträge) — durch

**Frage, die sie besitzt:** *Welches Rohmaterial gibt es fürs TDD?*
**Schicht: Projekte/Isor_Tower — nicht Uni** (Isors Beobachtung,
2026-08-22, siehe E51).

**Befunde**
- **C3-a:** Kopfzeile nennt „Abgabe ca. **2026-07-28**" — die Frist war
  der 21.08. Nie nachgezogen.
- **C3-b:** Flache chronologische Liste ohne Gliederung, obwohl das
  Format bereits `[Themenblock]`-Marken vorsieht. Beim Schreiben eines
  Kapitels liest man 556 Zeilen statt der 20 zum Thema; zwei Einträge zum
  selben Gegenstand liegen 300 Zeilen auseinander, Widersprüche fallen
  nicht auf.

**Entscheidungen**
- **E50 — Die Uni-Schicht wird nach Semestern gegliedert:**
  `Uni/Semester_2/`, künftig `Semester_3/`, dazu `Uni/ROADMAP.md` und
  `Uni/LOG.md` für das Semesterübergreifende. Spiegelt den bewährten
  Datenbaum unter `C:\IsorBackup\01_Uni\`.
- **E51 — TDD_NOTES wird eine Projekt-Datei, nach Themenblöcken
  gegliedert.** Begründung (Ein-Ort-Test): Einträge wie die
  MeshBuilder-Formeln sind keine Semester-Tatsachen — der `MeshBuilder`
  läuft weiter, und im nächsten TDD braucht man dieselbe Zeile. Je
  Semester abgelegt müsste sie kopiert (Verstoß) oder rückverwiesen
  werden. Kumulativ über alle Semester; überholte Einträge nach E9 ins
  `_ARCHIV.md` der Projekt-Schicht, mit Angabe, wodurch sie abgelöst
  wurden. Nichts geht verloren, es steht nur nicht mehr im Weg.
  *Aufwand:* einmalig ca. 1 h Sortierarbeit für die 85 Einträge.
  Die Chronologie bleibt erhalten — jeder Eintrag trägt sein Datum.

### C4 — ASSESSMENT_LOG.md (782 Zeilen, 2 Zeugnisse) — durch

**Frage, die sie besitzt:** *Wie stand es zu Datum X?* Berechtigt.
**Chronik** im Sinne von E13 — kann nie falsch werden, kein Archiv, keine
Pflege. **Schicht: Kern, und zwar ganz** — die Notenbilder sind Uni, aber
„Profil Person" und „Profil Coding" überleben jedes Semester, und der
Zweck ist der **Vergleich**. Eine Messreihe, die man nach Schichten
zerschneidet, ist keine Messreihe mehr (gleiches Argument wie E45).

**Befunde**
- **C4-a — Regel hinkt der Praxis hinterher:** ASSESSMENT_RULES
  beschreibt acht Abschnitte, endend bei „Prüfanker fürs nächste Mal".
  Das Zeugnis vom 16.08. hat neun — zusätzlich `### 7. Prüfanker vom
  11.08. — beantwortet`. Genau dieser Abschnitt macht aus zwei
  Momentaufnahmen eine Messreihe, steht aber in keiner Regel und kann
  beim dritten Zeugnis stillschweigend ausfallen (Fehlertyp wie I3).
- **C4-b:** 782 Zeilen für 350 gebrauchte. Beim nächsten Zeugnis wird die
  ganze Datei gelesen, um an das jüngste Zeugnis zu kommen; nach acht
  Zeugnissen wären es ~2.800 Zeilen.

**Entscheidungen**
- **E52 — „Prüfanker des letzten Zeugnisses — beantwortet" wird
  Pflichtabschnitt** in ASSESSMENT_RULES.
- **E53 — Eine Datei je Zeugnis**, z. B. `Kern/Zeugnisse/2026-08-16.md`.
  Der Ordner ist der Index (wie im Knowledge-Archiv). Beim nächsten
  Zeugnis wird eine Datei mit ~350 Zeilen gelesen statt 782, und der
  Vorteil wächst mit jedem weiteren. Ersetzt die Regel „Neuestes Zeugnis
  oben in ASSESSMENT_LOG.md" in ASSESSMENT_RULES.

**Gruppe C ist abgeschlossen (4 von 4).** Stand: 12 von 25 Posten.

## Datei-Durchgang · Gruppe D

### D1 — CODE_GUIDELINES.md (260 Zeilen) — durch

**Frage, die sie besitzt:** *Welche Code-Konventionen gelten?* Berechtigt.
**Schicht: Kern** — Block 1 ist Uni-Pflicht (24 von 260 Zeilen), der Rest
eigene Wahl. Ganz im Kern, Block 1 als Vorgabe der Uni-Schicht
gekennzeichnet (wie E42).

**Befunde**
- **D1-a:** Ownership nennt „Namen, Architektur, **Tests**" — es gibt
  keinen Test-Abschnitt.
- **D1-b:** Status-Vermerk „Rohmaterial aus Brainstorm 2026-07-17 — beim
  ersten Development-Einsatz nachschärfen" ist überholt: Die Datei war
  einen ganzen Uni-Durchgang im Einsatz und enthält selbst einen
  Abschnitt „Member-Reihenfolge (Isor, **2026-08-16**)".
- **D1-c:** „Bewusst nicht übernommen" mischt drei Sorten — eine
  **aufgeschobene Aufgabe** (ClaudeSetup, steht wortgleich auch in
  ROADMAP „Später" = Doppelung), eine **geltende Regel**
  (`_camelCase` gilt überall — keine Ablehnung), und eine **echte
  Verwerfung** mit korrektem DECISIONS-Verweis. Der dritte Eintrag zeigt,
  wie die anderen zwei aussehen müssten.
- **D1-d:** „Projekt-Typ: Uni/Privat" (Z. 8) nimmt die Schichten von
  gestern vorweg — zwei Schalter für dieselbe Sache.

**Entscheidungen**
- **E54 — Projekt-Typ wird aus der Schicht abgeleitet.** `Uni/`-Ordner
  vorhanden → Block 1 gewinnt im Konflikt; kein `Uni/` → Block 2. Stellt
  sich beim Kopieren des Harness von selbst richtig; die eigene
  Typ-Angabe entfällt. Heute müsste man daran denken umzustellen —
  vergisst man es, gelten in einem privaten Projekt still die Uni-Regeln.
- **E55 — „Bewusst nicht übernommen" wird nach Art aufgeteilt:**
  ClaudeSetup nur noch in der ROADMAP · `_camelCase` wandert zu den
  Naming-Regeln · die Verwerfung bleibt mit DECISIONS-Verweis. Danach
  enthält der Abschnitt nur noch echte Verwerfungen.
- **E56 — Tests: Lücke bleibt sichtbar, Abschnitt wird später
  nachgeholt** (Isor, 2026-08-22). Gemeint sind **automatische** Tests
  (Unity Test Framework); Isor testet heute von Hand über `TestMode`-
  Schalter (siehe FEATURE_LOG, MeshBuilder: „Flach-, Random-, Rampen-
  Test"). Ob automatische Tests überhaupt gewollt sind, ist eine eigene
  Entscheidung mit echtem Aufwand — als offener Punkt in die
  Kern-ROADMAP, Ownership-Zeile bleibt unverändert, damit die Lücke nicht
  unsichtbar wird.
- **D1-b wird beim Bauen mit erledigt:** Status-Vermerk auf den
  tatsächlichen Stand bringen.

### E57 — Umsetzungsliste vor dem Bauen (Isors Sorge, 2026-08-22)
Isor: Gefahr, dass beim Entwerfen-erst-dann-Bauen etwas verloren geht.
Gegenmaßnahmen, verbindlich:
1. Befunde, Entscheidungen und Belege werden **sofort nach jeder Datei**
   hier eingetragen — nichts bleibt nur im Kontext. Die Datei liegt im
   Git-Repo; bricht eine Session ab, wird hier weitergearbeitet.
2. Nach dem Durchgang werden die Entscheidungen in eine
   **Checkliste konkreter Handgriffe je Datei** übersetzt („CLAUDE.md:
   Ownership-Zeile ergänzen · Doku-Pflicht durch Verweis ersetzen ·
   Leseordnung auf PLAN.md umstellen"). Beim Bauen wird abgehakt, nicht
   erinnert.
3. **Schritt F** (Zuständigkeits-Tabelle) ist zugleich die
   Vollständigkeitsprüfung: Jede Art von Information braucht genau einen
   Besitzer; Übersehenes fällt als „kein Besitzer" auf.
4. Iterationen sind eingeplant, nicht Versagen — dafür gibt es
   `STOERUNGEN.md` (E16) und die Testphase. Der Unterschied zu vorher:
   Fehler sind dann belegt statt erinnert.

### D2 — GDD.md (98 Zeilen) — durch

**Frage, die sie besitzt:** *Was soll das Spiel sein?* Berechtigt.
Ownership ungewöhnlich klar („was es sein soll, nicht wie es gebaut
wird") und erklärt `offen` ausdrücklich zum gültigen Eintrag.
**Schicht:** Projekte/Isor_Tower.

**Befunde**
- **D2-a:** Z. 87 kündigt an: „Erst das laufende Semester abschließen
  (Portfolio 2026-08-21), danach das Bestehende am GDD ausrichten."
  **Diese Phase hat am 2026-08-22 begonnen.**
- **D2-b — eine offene Frage an drei Orten:** GDD-Frage 5 (Village-
  Terrain handgebaut / Tool / eingefroren) steht zugleich als DECISIONS
  2026-07-29 („Welt-Wahrheit: vertagt") und als ROADMAP Punkt 1
  („Welt-Wahrheit als Seed statt Szene"). Wird sie beantwortet, sind drei
  Stellen nachzuziehen.
- **D2-c:** Das „später ins GDD" aus WORKFLOW.md hat keinen Besitzer —
  es gibt keinen Ort für Design-Absicht, bis sie einsortiert ist. Das GDD
  wurde seit dem 2026-07-29 nicht mehr angefasst.

**Entscheidungen**
- **E58 — Eine offene Frage hat genau einen Besitzer.** Design-Fragen
  gehören dem GDD, technische der Projekt-DECISIONS. Die ROADMAP verweist
  nur als Aufgabe (nach E27 über den Namen). **DECISIONS bekommt einen
  Eintrag erst, wenn die Frage beantwortet ist** — dann streicht der
  Besitzer sie aus seiner Offen-Liste.
- **E59 — Abschnitt „Entwurf" im GDD** für noch nicht Einsortiertes.
  Kein eigenes `GDD_NOTES`: Die Begründungen, die Isor dort vermutet
  hatte, gehören nach DECISIONS („was, warum, verworfene Alternativen").
  Was fehlt, ist nur ein sichtbarer Ort für das „später".
- **E60 — `Kern/GDD_RULES.md` wird gebaut.** Besitzt Aufbau und Pflege
  eines GDD: was hineingehört, der `offen`-Mechanismus, wann aus Entwurf
  feste Absicht wird, wann ein Eintrag geschlossen wird. Gilt für jedes
  künftige Projekt; das GDD selbst bleibt beim Projekt (Trennung wie
  ARTIFACT_RULES ↔ ARTIFACT_INDEX).

### E61 — Abgabedokumente: Markdown ist der Master (Isor, 2026-08-22)

Klarstellung durch Isor: **Das GDD wird wie das TDD am Ende ein
Word-Dokument.** Beide sind Living Documents und sollen laufend
nachgezogen werden, statt am Ende in einem Durchgang zu entstehen
(das TDD entstand 07.–11.08. mit 149.948 Zeichen in fünf Tagen).

- **E61a — Takt: an der Baustein-Grenze, nicht nach Kalender.** Ein
  Baustein gilt erst als fertig, wenn sein Abschnitt geschrieben ist.
  Grund: Der Inhalt ändert sich an Feature-Grenzen, nicht sonntags; über
  ein halbfertiges System schreibt man zweimal. Bester Teil des TDD war
  der Threading-Abschnitt, direkt nach der Messreihe geschrieben.
- **E61b — Text lebt in Markdown, `.docx` ist die Abgabefassung.
  Beide Dokumente**, also auch das TDD (Isors Entscheidung, entgegen
  meiner Empfehlung, das TDD unangetastet zu lassen).
  Begründung dafür: Word-Eingriffe sind teuer — DOCX_RULES dokumentiert
  **sechs** Fallen, jeder Eingriff braucht Sicherung, Prüfung und
  Renderkontrolle. Markdown kostet nichts und liegt im Git-Diff.
  *Wichtig, senkt den Preis:* Das vorhandene TDD-Layout wird **nicht
  weggeworfen, sondern zur Formatvorlage** — Formatvorlagen, Kopfzeilen,
  Seiteneinrichtung, Verzeichnisgerüst bleiben; nur der Text kommt aus
  Markdown. Isor hat dieses Verfahren bereits angewandt (DECISIONS
  2026-08-11: „S4-Abgabe aus dem TDD als Formatvorlagen-Spender gebaut").
  *Aufwand, ehrlich:* Das ist ein **Werkzeug**, kein Regelwechsel —
  Markdown lesen, in die Vorlage füllen, Überschriftenebenen und
  Formatvorlagen zuordnen. Realistisch ein voller Arbeitstag, die ersten
  Läufe sitzen nicht auf Anhieb. **Gehört auf die ROADMAP, nicht auf die
  Wochenendliste.**
- **E61c — Bilder zuletzt, Texttabellen früh.** Belegt durch die eigenen
  DOCX_RULES: „Ein neu eingefügtes Bild verschiebt **alle** Nummern
  danach … Nummern sind positionsabhängig." Zwanzig über das Semester
  verteilte Bilder heißen zwanzigmal Felder aktualisieren und prüfen.
  Tabellen aus Text sind billig und können sofort hinein.

### D3–D5 — ASSIGNMENT_PCG / _TOOL / _THREADING (206 Zeilen) — durch

**Frage, die sie besitzen:** *Was verlangt die Uni-Aufgabe im
Originaltext?* Berechtigt — die Zeugnis-Belegpflicht hängt daran.
**Alle drei sauber:** Ownership klar, Quelle genannt (Canvas, Kursnummer,
Modul), „unverändert lassen", eigene Planung nach DECISIONS/TDD_NOTES
verwiesen, und sie verweisen **über Dateinamen** aufeinander — genau
was E27 verlangt. Keine inhaltlichen Befunde.
**Schicht:** `Uni/Semester_2/`.

**Befund D-a — vier von sieben Aufgabentexten fehlen**
Das Portfolio hat sieben Teilabgaben (geprüft am 2026-08-22 gegen
`Abgabe_Final`):
4FSC0PD003.1 — 1_Softwareplanung · 2_Engine-Tool ✔ · 3_Threadoptimierung ✔
4FSC0PD004.1 — 1_KI Prototyp · 2_Simulation der Spieleumgebung ·
3_Prozedurale Erweiterung ✔ · 4_Arbeiten nach akademischen Standards
Hinterlegt sind nur drei Aufgabentexte.

Folge: ASSESSMENT_RULES verlangt „Alle `ASSIGNMENT_*.md` — die
Bewertungskriterien im Originaltext" und „begründet gegen die
Feedbackelemente der jeweiligen `ASSIGNMENT_*.md`, nicht gegen ein
Bauchgefühl". **Beide bisherigen Zeugnisse haben sieben Abgaben bewertet,
aber nur für drei die Kriterien im Original gehabt.** Die Belegpflicht
konnte das nicht bemerken, weil sie „alle vorhandenen" prüft statt „alle
nötigen" — derselbe Satz wie bei den Prefabs: *Ein Verzeichnis merkt
nicht, dass etwas fehlt.*

**Entscheidungen**
- **E62 — Fehlende Aufgabentexte nachtragen.** Isor holt die vorhandenen
  aus Canvas, Claude legt sie nach demselben Muster an. Gibt es für eine
  Teilabgabe keinen eigenen Text, wird **genau das** als Datei
  festgehalten — damit die Lücke belegt ist statt unsichtbar.
- **E63 — Belegpflicht wird gegen die Teilabgaben abgeglichen:** Jede
  Teilabgabe des Portfolios braucht einen hinterlegten Aufgabentext;
  fehlt einer, wird das im Zeugnis ausdrücklich vermerkt statt still
  geschätzt.

**Gruppe D ist abgeschlossen (5 von 5).** Stand: 17 von 25 Posten.

## Datei-Durchgang · Gruppe E — geplante Dateien und Streuner

### E64 — Inhalt von `Kern/DOC_RULES.md` (steht fest, ~120 Zeilen)
Fünfzehn Regeln aus dem Durchgang, die heute **keinen Besitzer** haben:
1. Ownership-Definition und die drei Prüfungen
2. Jede Datei beginnt mit `Ownership:` (20 von 21 tun es — nie verlangt)
3. `Format:`-Zeile, wo Einträge einem Muster folgen (3 von 21)
4. Maßstab: eine Frage, die sonst niemand beantwortet (E15)
5. Kosten = Größe × Lesehäufigkeit
6. Chronik gegen Verzeichnis — was Pflege braucht (E13)
7. Erzeugen statt pflegen: wann ja, wann nein (E30 gegen B3-c)
8. Verweise über Namen, Pfad **und** Überschrift (E27)
9. Gleiche Dateinamen je Schicht, nie ohne Schicht sprechen (E28)
10. Keine Zählwörter in Überschriften wachsender Listen (E41)
11. Archiv: Nachfolger und Vorgänger benennen (E9)
12. Eine Checkliste gehört dem Moment, nicht den Themen (E33)
13. Ein Register muss vollständig sein (E45)
14. Eine offene Frage hat genau einen Besitzer (E58)
15. Eine Ausnahme muss sich selbst benennen und begründen
    (Vorbild ASSESSMENT_RULES)

### E65 — `GLOSSARY.md` wird **nicht** als eigene Aufgabe gebaut
Isor kannte den Begriff nicht und sah den Bedarf nicht — die Begriffe
werden ohnehin gerade in DOC_RULES, WORKFLOW und GDD_RULES definiert.
Das Glossar **fällt am Ende als Nebenprodukt ab**: je Begriff eine
Kurzform plus Verweis auf die Stelle, wo er herkommt („erzeugen statt
pflegen"). Zeigt sich dann kein Bedarf, entsteht es nicht.
*Beleg, dass das Problem real ist:* drei Begriffskollisionen in zwei
Tagen — „Work Area" gegen „Session", „Uni-Modus" gegen „Lern-Modus",
„Modus" gegen „Regler".
Kandidaten fürs Einsammeln: Ownership · Schicht · Work Area · Baustein ·
Lernmodus · Regler · Chronik · Verzeichnis · Register · Archiv · Befund.

### E66 — `_split_check.txt` wandert nach `99_Archiv\_Zu_Loeschen\`
Acht Zeilen, mitten im Satz abbrechend, Bruchstück des Zeugnisses vom
2026-08-11, das vollständig im ASSESSMENT_LOG steht. In keinem
INDEX-Eintrag. Nicht löschen — Isor leert selbst.

**Gruppe E ist abgeschlossen. Der Datei-Durchgang ist damit vollständig:
alle 25 Posten.** Offen bleibt **Schritt F** — die Zuständigkeits-Tabelle
über alle Dateien als Vollständigkeitsprüfung.

## Schritt F — Zuständigkeits-Tabelle (2026-08-22)

Prüfung nach Isors Forderung: eine Zeile je **Art** von Information, eine
Spalte „Besitzer". Zwei Besitzer = Konflikt, kein Besitzer = Lücke.
Die vollständige Tabelle geht beim Bauen in `DOC_RULES.md`.

**Bereits im Durchgang bereinigt — neun Fälle mit zwei Besitzern:**
Doku-Pflicht (E17) · Fertiges (E13/E11) · Artifact-Check, dreifach (E33) ·
Knowledge-Zeitpunkt (E29) · Zeugnis-Doku-Pflicht (E43) · Statusangaben
(E26) · Welt-Wahrheit-Frage, dreifach (E58) · Projekt-Typ (E54) ·
ClaudeSetup (E55).

**Neu durch die Tabelle gefunden:**

- **E68 — „Baustein" ist undefiniert**, obwohl mehrere Regeln daran
  hängen (WORKFLOW: „Session-Schnitt an der Baustein-Grenze"; E61a: „Ein
  Baustein gilt erst als fertig, wenn sein Abschnitt geschrieben ist").
  **Besitzer: WORKFLOW.md** — Definition und Fertig-Kriterium zusammen:
  Ein Baustein ist eine abgeschlossene Funktionseinheit, die sich in
  einem Zug entwerfen und bauen lässt; *fertig* heißt gebaut, geprüft
  **und** dokumentiert.
- **E69 — Erklärstil: „zeigen statt vorstellen lassen".**
  *Richtigstellung:* ARTIFACT_RULES sagt bereits beides („Diagramme sind
  erwünscht — sie sind extern, nicht vorgestellt"); Claude hatte daraus
  fälschlich „Zahlen statt Bilder" gemacht. Die Grenze verläuft zwischen
  **außen und innen**, nicht zwischen Bild und Zahl:
  - Nie: „stell dir vor" — alles, was ein inneres Bild verlangt
  - Gern: Diagramme, Skizzen, Artifact-Seiten, Screenshots (ansehbar)
  - Dazu: Zahlen und Tabellen, weil sie unabhängig vom Bild tragen
  **Besitzer: WORKFLOW.md**, bei Modus und Regler — die Regel gilt in
  jeder Session. ARTIFACT_RULES behält einen Verweis für den Seitenaufbau.
  **Untergrenze für den Visualisierungs-Regler (E21):** Auch bei „wenig"
  oder „keine" wird nie auf inneres Vorstellen ausgewichen; was sonst ein
  Diagramm gezeigt hätte, wird über Zahlen und Tabellen erklärt — länger,
  aber nie über „stell dir vor". Der Regler steuert den **Aufwand** der
  Darstellung, nicht ob Isor sich etwas vorstellen muss.
- **E70 — Sprachregeln bekommen einen Besitzer:** eine Tabelle in
  `DOC_RULES.md`, eine Zeile je Erzeugnis (Code englisch · Kommentare
  einheitlich · Commits englisch · Harness-Dokumente deutsch · Zeugnisse
  deutsch · Unterhaltung deutsch). Die vier bisherigen Fundstellen
  (DECISIONS 2026-07-17, CODE_GUIDELINES Block 1, WORKFLOW,
  ASSESSMENT_RULES) verweisen darauf. Kein Widerspruch bisher — aber
  niemand besaß „welche Sprache wo".
- **E71 — Die Markdown-Manuskripte liegen beim Projekt.**
  `Projekte/Isor_Tower/GDD.md` ist zugleich Design-Absicht **und**
  Abgabetext — kein zweites Dokument, kein Übertragungsschritt.
  Daneben `Projekte/Isor_Tower/TDD.md`. Die `.docx`-Abgabefassung
  entsteht daraus und ist keine eigene Quelle (E61b).

**Verbleibende Lücken ohne Besitzer** (noch zu besprechen):
IsorBackup (Schicht beschlossen, aber leer — inklusive des
Backup-Ziels) · Repo- und Git-Regeln samt Build-Versionsschema
(ROADMAP Punkt 9) · Prefab-Innenaufbau (ROADMAP Punkt 7) ·
Tests (E56, bewusst offen).

## Schicht IsorBackup (2026-08-22)

**Befunde am `C:\IsorBackup\README.md`**
- **G-a — Selbstwiderspruch:** Z. 4 kündigt an „`Repos Isor` **wird**
  `IsorRepos`", Z. 92 sagt „Bewusst verworfen: `Repos Isor` **bleibt so
  heißen** (2026-08-06)". Der Kopf wurde beim Verwerfen nicht nachgezogen.
- **G-b — vier Sorten Information in einer Datei:** Regeln (Baum, sieben
  Ablageregeln, Benennung, Asset-Library) ✔ · „Offene Punkte" = **eine
  ROADMAP** (8 Aufgaben) · „Bewusst verworfen" = **eine DECISION** ·
  der Ordnerbaum als Textblock = ein Verzeichnis. Dritter Fall nach
  ARTIFACT_INDEX (C1-c) und CODE_GUIDELINES (D1-c).
- **G-c:** Die Aufgabenliste ist veraltet — „Vier der sieben
  Aufgabenordner sind noch leer", die Abgabe ist seit 2026-08-20 hoch.
- **G-d:** `C:\IsorBackup` ist **kein Git-Repo** — die Regeln dort haben
  keine Versionsgeschichte.

**Entscheidungen**
- **E72 — Die Regeln ziehen in den Harness**, parallel zu E31 (Knowledge):
  `IsorBackup/RULES.md` (Baum, Ablageregeln, Benennung, Asset-Library) ·
  `IsorBackup/ROADMAP.md` (die offenen Aufräum-Punkte) ·
  `IsorBackup/DECISIONS.md` („Repos Isor bleibt so heißen").
  `C:\IsorBackup\README.md` wird ein kurzer Wegweiser dorthin.
  Zusatzgrund: Damit bekommt der Text Versionsgeschichte (G-d).
- **E73 — Aufräumen erst nach dem Harness-Umbau, als erste Aufgabe der
  Testphase** (Isor, 2026-08-22). Verfahren: Arbeitsliste mit Ende wie
  PREFAB_STATUS (E49), Entscheidungen in **Viererpaketen** mit Claudes
  Einschätzung je Posten.
  *Zusätzliche Begründung:* Das Aufräumen ist die erste echte
  Belastungsprobe des neuen Harness — es benutzt Schichten, Viererpakete,
  Archivregel und `/ende`, und es kann dabei nichts kaputtgehen.
  Akut ist nichts: `00_Eingang` ist bis auf einen Unterordner leer.
- **E74 — Externes Backup: Spiegeln mit Papierkorb.** `robocopy` gleicht
  die Platte an, verschiebt aber alles Wegfallende vorher nach
  `_Geloescht\<Datum>\` statt es zu löschen. Isor leert selbst — die
  eigene Regel „niemals löschen, nur archivieren", angewandt auf die
  Platte. Ausdrücklich **kein** `/MIR` ohne Papierkorb: Ein versehentliches
  Löschen wäre nach dem nächsten Lauf endgültig.
- **E75 — Umfang: alle drei Ordner** (IsorBackup + die beiden
  Repo-Ordner), wie im README vorgesehen. Begründung: `C:\IsorBackup` ist
  der einzige der drei **ohne zweite Kopie** — die Repos liegen auf
  GitHub. Die lokale Repo-Kopie bringt nach einem Plattendefekt trotzdem
  in Minuten statt Stunden zurück, samt unversionierter Dateien.
- **E76 — Auslöser: Erinnerung in der Sonntagsroutine.** Der Pflegetag
  trägt schon die Artifact-Durchsicht (E34, E47); Backup kommt als Punkt
  dazu. Isor steckt die Platte an, Claude startet das Skript.
  *Begründung gegen die Windows-Aufgabenplanung:* Eine dauerhaft
  angesteckte Platte schützt gegen Defekt, aber nicht gegen
  versehentliches Massenlöschen oder Verschlüsselungstrojaner — die
  erreichen eine angeschlossene Platte genauso.

## Nachträge zu DOC_RULES (Durchsprache 2026-08-22)

- **E82 — Stand-Stempel nur, wo etwas ihn kontrolliert.** In erzeugten
  Dateien setzt ihn das Skript; in handgeschriebenen nur, wenn eine
  Prüfung ihn abgleicht (Artifact-Seiten: der Sonntagsabgleich, E47).
  Ohne Prüfung kein Datum.
  *Beleg:* Von vier vorgefundenen Stempeln waren drei falsch —
  ARTIFACT_INDEX (10 Tage), PREFAB_STATUS (33 statt 34), TDD_NOTES
  (Frist 28.07. statt 21.08.). Der vierte, die Stempelpflicht auf
  Artifact-Seiten, ist gewollt und funktioniert. Ein pauschales
  „lieber weglassen" hätte genau den getroffen.
- **E83 — „Harness auf Englisch prüfen" wird eine Bedingung**, kein
  vager Punkt: erst prüfen, wenn der Harness tatsächlich an jemanden
  weitergegeben werden soll. Grund: Bei Lese-Rechtschreib-Schwäche kostet
  Lesen in der Fremdsprache **in jeder Session** etwas, während der
  Nutzen nur in einem Fall eintritt. Löst zugleich den Widerspruch zur
  Sprachtabelle (E70), die Harness-Dokumente auf Deutsch festlegt.
- **E84 — Sprachregel bindet nur Claude.** Claude nennt immer die Schicht
  („die Uni-Roadmap"); sagt Isor bloß „die Roadmap", erschließt Claude
  sie aus dem Zusammenhang. Grund: Isor diktiert per Spracheingabe, eine
  Sprechregel wäre dort Reibung ohne Gewinn.
- **E85 — Chronik-Einträge dürfen Ablageorte nennen** (schärft E13 nach):
  Ein Eintrag trägt sein Datum und sagt damit, wo etwas **damals** lag —
  das ist beim Nachvollziehen oft der Schlüssel. Die Chronik verspricht
  nur nicht, dass es dort heute noch liegt; der aktuelle Ort kommt aus
  dem Code bzw. der erzeugten Systemliste.
- **E86 — `Format:`-Zeile ist Pflicht, wo Einträge einem Muster folgen**
  (nicht in reinen Regeldateien). Belegt durch FEATURE_LOG: ohne
  Formatvorgabe wurden daraus 73 Einträge als flache Liste.

**Phase 1 ist damit abgeschlossen:** `DOC_RULES.md`, `GDD_RULES.md`,
`VERSIONIERUNG.md` gebaut, alle drei im INDEX, DOC_RULES Abschnitt für
Abschnitt mit Isor durchgesprochen und an fünf Stellen nachgeschärft.

## Versionierung (Isors Einwurf, 2026-08-22)

Ausgangspunkt: Isor wollte den Harness versionieren und einen Ordner für
„Builds", weil er unsicher war, ob sich über GitHub Desktop ein alter
Stand zurückholen lässt.

**Klarstellung:** Git kann das — 35 Commits, jeder ein vollständiger
Stand. Das Problem ist nicht der Speicher, sondern der **Zugang**:
GitHub Desktop hat keinen offensichtlichen Knopf für „zeig mir die
Dateien von damals, ohne etwas zu ändern".

**Der eigentliche Bedarf ist ein anderer** — eine *Auslieferung*: Beim
Kopieren in ein neues Projekt wird nur der **Kern** gebraucht, nie die
Uni-Schicht, das Projekt oder der Entscheidungs-Altbestand. Das kann Git
nicht, und dafür verdient der Ordner seine Existenz.

- **E77 — Spiel-Schema wird nach hinten geschlossen.** DECISIONS
  2026-08-16 (`0.0.x` Prototyp · `0.x.0` Early Access · `1.x.x` fertig)
  bleibt gültig und wird **ergänzt**: Ab `1.x.x` ist die Reifegrad-Frage
  beantwortet, also wechselt die Lesart — `Y` = neue Inhalte,
  `Z` = Fehlerbehebung. Isors Frage war: „Was ist, wenn das Spiel draußen
  ist und ein Fix kommt?" — dafür sagte das Schema bisher nichts.
- **E78 — Ein Schema für alles geht nicht**, weil die drei Nummern
  Verschiedenes zählen: Commit = Sitzungen · Spiel = Reifegrad ·
  Harness = Verträglichkeit. Was geht und Isors Sorge löst: **eine
  gemeinsame Schreibweise `X.Y.Z`, drei aufgeschriebene Lesarten.**
  Die Commit-Nummer ist ausdrücklich **keine Version**, sondern eine
  laufende Nummer.
- **E79 — Harness-Version `X.Y.Z` nach Verträglichkeit:** `X` = Struktur,
  Projekt muss umziehen · `Y` = Regeln, kompatibel · `Z` = Korrekturen.
  Steht als eine Zeile in **CLAUDE.md** (wird bei jedem Session-Start
  gelesen). Der jetzige Umbau wird **1.0.0**.
- **E80 — Kern-Auslieferung je Hauptversion** unter
  `C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\Harness_<X.Y.Z>\`.
  Inhalt: nur `Kern/`. **Kein Backup** — zum Zurückholen dient Git.
  Angelegt bei Änderung von `X` oder `Y`, nicht bei `Z`. Eine abgelegte
  Auslieferung wird nie bearbeitet.
- **E81 — `Kern/VERSIONIERUNG.md`** besitzt die drei Lesarten. Nach E15
  berechtigt: „Welche Nummer bedeutet was" beantwortet heute niemand,
  und Isor hat genau danach gefragt. Besitzt **nicht** die Nummern selbst
  — die stehen im Commit-Titel, in den Player Settings und in CLAUDE.md.

### E67 — „Session" und „Abschnitt" festgelegt (2026-08-22)
Anlass: Isor stockte beim Benennen des laufenden Arbeitsraums — ein
Beleg für die Begriffskollision aus E65.
- **Session** — ein durchgehender Arbeitsraum von Anfang bis `/clear`.
  Isors Wort dafür ist „Work Area"; bleibt als Synonym im Glossar.
- **Abschnitt** — eine Phase innerhalb einer Session mit genau einem Typ.
  `/wechsel` beendet einen Abschnitt und öffnet den nächsten.

*Widerspruch, den das auflöst:* WORKFLOW.md sagt „Jede **Session** hat
genau einen Typ" (gemeint ist der Abschnitt) und „Max. 2–4 parallel
offene **Sessions**" (gemeint ist der Arbeitsraum) — ein Wort für zwei
Dinge. Neue Fassung: **Jeder Abschnitt hat genau einen Typ. Eine Session
kann mehrere Abschnitte enthalten, getrennt durch `/wechsel`.**

### Erste Einträge für `STOERUNGEN.md` (E16), sobald die Datei existiert
- **2026-08-21** — Claude meldete, ROADMAP.md verletze ihre eigene
  Ownership-Regel („Erledigt"-Block). Tatsächlich war es ein Widerspruch
  **zwischen** ROADMAP und FEATURE_LOG (C7). Ursache: nur eine der beiden
  Ownership-Zeilen gelesen, bevor geurteilt wurde.
  *Regel, die gefehlt hat:* Vor einem Ownership-Befund immer die
  Ownership-Zeile **aller** beteiligten Dateien lesen. Gehört in DOC_RULES.
- **2026-08-21** — Claude kündigte einen Fragenblock an, stellte ihn aber
  nicht (Isor musste nachfragen). Reiner Ausführungsfehler.

### Vorabnotiz für Gruppe B — KNOWLEDGE_RULES.md
Beim Anwenden am Session-Ende aufgefallen: Die Regel aus **E2** steht dort
**bereits** (Z. 29–32: „Claude fragt bei jedem Session-Ende — egal welcher
Typ — ob etwas als Knowledge behalten werden soll. Claude schlägt vor,
Isor entscheidet."). **I3 war also kein fehlender, sondern ein nicht
ausgeführter Regelsatz.** Zusammen mit A2-d (Commit-Format) ergibt das ein
Muster: Ein Teil von Isors Befunden sind **Ausführungs-, keine
Regelfehler** — sie gehören automatisiert, nicht neu geregelt.
Beim Durchgang durch Gruppe B je Datei mitprüfen: Regel fehlt oder Regel
wird nur nicht befolgt?

Ergänzung KNOWLEDGE_RULES: Die Themengruppen (`Patterns/`, `Unity/`,
`ProcGen/`, `CSharp/`, `Seiten/`) hatten keinen Platz für Regeln über
Wissensarbeit selbst. Neue Gruppe **`Dokumentation/`** angelegt
(2026-08-22), nach der Regel „Unterordner wachsen nach Bedarf".

## Befunde von Isor (Retro 2026-08-21)

| # | Befund | Status |
|---|---|---|
| I1 | Doku-Pflicht am Session-Ende: hat meistens geklappt, aber nicht immer vollständig | offen |
| I2 | Commit-Vorschlag hat sich in Form/Darstellung mehrfach geändert — kein festes Format | offen |
| I3 | Knowledge wird nicht immer abgefragt und nicht immer gespeichert | offen |
| I4 | Artifacts: Erzeugung hat sich verändert; offen, **wann** sie erzeugt und auf Aktualität geprüft werden | offen |
| I5 | Berechtigungs-Nachfragen: manches sollte dauerhaft erlaubt sein — Liste einmal durchgehen | offen |
| I6 | Gewisse .md-Dateien tun nicht zu 100 %, was sie sollen — Ursache unklar | offen |
| I7 | DECISIONS.md und ROADMAP.md brauchen ein besseres System; veraltete Einträge stehen drin | offen |
| I8 | Session-Anfang und Session-Ende sollen weitgehend automatisiert kommen | offen |
| I9 | Session-Typen nachschärfen (Brainstorm / Design / Development) und Lernmodus verbessern | offen |
| I10 | Neuer Skill: Visualisierungsgrad steuerbar (viel / wenig / fast keine) | offen |
| I12 | Artifact-Seite über den Harness selbst: wie er funktioniert, wie der Session-Loop läuft — visuell, laufend aktuell gehalten. Design in Gruppe B (ARTIFACT_RULES), Eintrag später in ARTIFACT_INDEX | offen |
| I11 | Rückfrage-Pflicht: bei unklarer Richtung erst fragen, statt loszulaufen — als feste Regel verankern. Achtung: steht in Spannung zu CLAUDE.md „eine begründete Empfehlung statt Optionsliste". Auflösung nötig (Vorschlag: Rückfrage bei Weggabelung, Empfehlung bei Detailfrage) | offen |

## Befunde aus dem Bestand (Claude, 2026-08-21)

| # | Befund | Beleg | Status |
|---|---|---|---|
| C1 | Doku 5.770 Zeilen in 20 Dateien; DECISIONS.md allein 1.790 (31 %) | `wc -l Claude/*.md` | offen |
| C2 | Leseordnung zieht 847 Zeilen ins Fenster, davon 708 ROADMAP | CLAUDE.md Leseordnung | offen |
| C3 | ROADMAP verletzt die eigene Ownership-Regel: 48-zeiliger „Erledigt"-Block, Begründungen in den offenen Punkten (Nr. 11: 13 Zeilen) | ROADMAP.md Z. 3 vs. Z. 21–68 | offen |
| C4 | Automatisierung fast nicht vorhanden: 1 Skill (`zeugnis`), 0 Slash-Commands, 0 Hooks | `~/.claude/`, `settings.json` | offen |
| C5 | `settings.local.json` hat 280 Allow-Einträge, überwiegend Einmal-Befehle mit Session-UUID im Pfad — greifen nie wieder | `.claude/settings.local.json` | offen |
| C6 | Uni-Spezifisches liegt im selben Ordner wie der generische Kern (ASSIGNMENT_*, DOCX_RULES, TDD_NOTES, ASSESSMENT_*) — widerspricht dem Grobziel „generischer Harness, später pro Projekt kopiert" | ROADMAP.md Z. 6–10 | entschieden (Drei-Schichten) |

## Vier Baustellen

- **A — Doku-Struktur:** Ownership durchsetzen, ROADMAP entschlacken,
  DECISIONS archivieren. (C1, C2, C3, I6, I7)
- **B — Automatisierung:** Session-Start und Session-Ende als feste
  Abläufe; Knowledge und Artifacts darin verankert. (C4, I1, I2, I3, I4, I8)
- **C — Schichten:** Kern / Uni / IsorBackup trennen. (C6)
- **D — Berechtigungen:** 280 Einträge auf generische Muster eindampfen. (C5, I5)

Reihenfolge: **C → A → B**, D dazwischen. Grund: Die Schicht bestimmt, ob
eine Datei bleibt, umzieht oder gekürzt wird (C vor A). Skills und Hooks
nageln Regeln fest — erst festlegen, was gilt, dann automatisieren (A vor B).
