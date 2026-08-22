# ASSESSMENT_RULES.md — Regeln des Zeugnis-Modus

Ownership: Der Session-Typ „Zeugnis" vollständig — Auslöser, Ablauf,
Belegpflicht, Aufbau, Notenskala, Schreibregeln, Ablage. Die Zeugnisse
selbst stehen in ASSESSMENT_LOG.md.

Warum eigene Datei: „Zeugnis" ist ein Modus, keine Ausgabeform. WORKFLOW.md
führt ihn als vierten Session-Typ und verweist hierher — dieselbe Trennung
wie bei KNOWLEDGE_RULES.md und ARTIFACT_RULES.md: dort die Regeln, im
kurzen Eintrag nur der Zeiger.

## Zweck
Ein Zwischenzeugnis ist eine Standortbestimmung zu einem festen Datum:
Wo steht die Abgabe, wo steht Isor fachlich, wo steht er persönlich.
Es wird bewusst wiederholt, damit sich Stände vergleichen lassen — nicht
als einmaliges Feedback.

## Auslöser
Auf Zuruf („Zeugnis", `/zeugnis`). Sinnvolle Anlässe: vor dem Polishing,
nach einer Abgabe, am Semesterende, vor einer Bewerbungsrunde.

## Session-Disziplin
Die Session **liest und bewertet, sie baut nicht.**
- Kein Code wird geändert, keine Abgabedatei angefasst, keine
  Entscheidung getroffen. Was auffällt, wird Befund — nicht Umbau.
- Fremde Dateien bleiben unberührt. Geschrieben wird ausschließlich in
  ASSESSMENT_LOG.md und ARTIFACT_INDEX.md; die ROADMAP wird um die
  Befunde als Aufgaben ergänzt, sonst nichts.
- FEATURE_LOG, DECISIONS, TDD_NOTES und der Knowledge-Ordner bleiben
  leer ausgehend von dieser Session: Es wurde nichts gebaut, nichts
  entschieden und nichts gelernt, das dorthin gehört.
- Reine Lese-Session heißt auch: Zwischenstände (etwa aus `.docx`
  gezogener Text) gehören in den Scratchpad, nie ins Projekt.
- Am Ende steht ein Commit-Vorschlag wie bei jeder Session (WORKFLOW.md,
  Grundregel „Session-Ende").

## Belegpflicht — vor dem Schreiben zu lesen
Ein Zeugnis wird nie aus der Erinnerung oder aus alten Zeugnissen
geschrieben. Vor jedem Zeugnis werden gelesen:
1. `ROADMAP.md`, `FEATURE_LOG.md`, `DECISIONS.md` — Stand und Begründungen
2. Alle `ASSIGNMENT_*.md` — die Bewertungskriterien im Originaltext
3. Die aktuellen Abgabedokumente selbst (`.docx` unter
   `C:\IsorBackup\01_Uni\Semester_<n>\Arbeitsdateien\`), nicht nur die Notizen
4. Mindestens fünf repräsentative `.cs`-Dateien im Original, darunter
   eine neue, eine alte und eine als problematisch vermerkte
5. `git log` des betroffenen Repos
6. Das letzte Zeugnis in `ASSESSMENT_LOG.md` — für den Vergleich

## Aufbau eines Eintrags
Feste Reihenfolge, damit zwei Zeugnisse nebeneinander lesbar sind:
1. **Kopf** — Datum, Anlass, Projektstand in zwei Sätzen, Belegbasis
2. **Notenbild** — Tabelle je Aufgabe/Bereich, UK-Skala, plus ein
   Gesamtwert mit Bedingung („wenn X fertig, dann Y")
3. **Was trägt** — Stärken, jede mit konkreter Belegstelle
4. **Was die Note kostet** — Schwächen, jede mit Belegstelle,
   geschätztem Aufwand und Hebelwirkung
5. **Profil Person** — Arbeitsweise, Muster, Risiken
6. **Profil Coding** — Stand gegen Semester, was sitzt, was fehlt
7. **Nächster Schritt** — konkrete Reihenfolge bis zum nächsten Termin
8. **Prüfanker fürs nächste Mal** — was beim nächsten Zeugnis
   nachgesehen wird, damit der Vergleich messbar ist

## Notenskala
UK-Klassifikation (SAE, Middlesex-validiert), Punkte 0–100:
- 70+ First
- 60–69 Upper Second (2:1)
- 50–59 Lower Second (2:2)
- 40–49 Third
- unter 40 Fail

Jede Note ist ausdrücklich Claudes Schätzung, keine Dozentennote. Die
Schätzung wird immer gegen die Feedbackelemente der jeweiligen
`ASSIGNMENT_*.md` begründet, nicht gegen ein Bauchgefühl.

## Schreibregeln
- Keine Beschönigung und keine Härte um der Härte willen. Eine Schwäche
  ohne Aufwandsschätzung ist nutzlos; ein Lob ohne Belegstelle auch.
- Belegstellen als Datei/Kapitel benennen, damit sie nachprüfbar sind.
- Kein Vergleich mit anderen Studenten — nur gegen die Aufgabenkriterien
  und gegen den eigenen letzten Stand.
- Was Isor selbst schon gefunden hat (steht in ROADMAP/DECISIONS), wird
  als gefunden gekennzeichnet, nicht als neue Erkenntnis verkauft.
- Deutsch. Ausnahme: Dateinamen, Code und Zitate aus dem Code.

## Ablage
- **Eine Datei je Zeugnis** unter `Kern/Zeugnisse/<JJJJ-MM-TT>.md`.
  Der Ordner ist das Verzeichnis, es gibt keine Sammeldatei.
  Titelzeile: `# Zeugnis <JJJJ-MM-TT> — <Anlass>`.
- Grund: Beim Schreiben eines Zeugnisses wird nur das **letzte** gelesen
  (siehe Belegpflicht). Eine Sammeldatei zwingt dazu, alle zu laden —
  bei zwei Zeugnissen 782 Zeilen für 350 gebrauchte, und der Abstand
  wächst mit jedem weiteren.
- Alte Zeugnisse werden nie überschrieben oder gekürzt — der Vergleich
  ist der Zweck.

## Die Handy-Fassung — Ausnahme von ARTIFACT_RULES
Jedes Zeugnis wird zusätzlich als Artifact veröffentlicht. Dafür gelten
die Regeln aus ARTIFACT_RULES.md (Aufbau, beide Farbwelten, Scroll-Bereich
für breite Tabellen, Aphantasie über Zahlen statt Bilder) — mit **einer
benannten Ausnahme**, die diese Datei besitzt:

> **Pro Zeugnis eine eigene, neue URL.** Ein Zeugnis wird nie
> aktualisiert und nie ersetzt.

Das bricht bewusst die Pflegeregel „Bestehende Seite aktualisieren statt
neu anlegen". Grund: Bei den drei Typen Status/System/Lernstück ist der
alte Stand wertlos, sobald der neue existiert — beim Zeugnis ist er der
halbe Zweck. Ein Zeugnis ist keine Ansicht auf einen aktuellen Stand,
sondern ein datierter Messpunkt.

Deshalb ist „Zeugnis" auch **kein vierter Artifact-Typ**: Die drei Typen
beschreiben, *worauf* eine Seite blickt. Ein Zeugnis ist eine andere
Gattung — es bewertet, statt zu beschreiben. Eintrag trotzdem in
ARTIFACT_INDEX.md, damit keine URL unerklärt bleibt; dort mit dem Symbol
🎓 und dem Vermerk, dass die Seite nicht nachgezogen wird.

- Titel-Schema: `🎓 Zeugnis · <JJJJ-MM-TT>, <Anlass>`
- Favicon: 🎓, über alle Zeugnisse gleich.
- Statt eines Stand-Stempels trägt die Seite ihr Zeugnis-Datum — es ist
  kein Prüfdatum, sondern der Inhalt selbst.
