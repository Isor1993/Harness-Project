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
