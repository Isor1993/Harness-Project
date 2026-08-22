# STOERUNGEN.md — Was im Betrieb nicht funktioniert hat

Ownership: Nur Vorfälle, in denen der Harness nicht so gearbeitet hat wie
vorgesehen — was passiert ist und welche Regel nicht gegriffen hat.
Das LOG besitzt „was ist passiert", diese Datei „was ist schiefgegangen".
Keine Aufgaben (das ist die ROADMAP), keine Begründungen (DECISIONS).
Format: `### JJJJ-MM-TT — Kurztitel` mit den Zeilen **Was**, **Ursache**,
**Regel** und **Stand**. Der Stand ist entweder `offen` oder
`behoben <Datum>` samt der Stelle, an der die Behebung steht. So ist die
Liste der offenen Vorfälle ein Suchlauf nach `Stand: offen` statt eine
Zählarbeit — bei der am 2026-08-22 dreimal verschieden gezählt wurde.

Warum die Datei existiert: Die Überholung von 2026-08-21/22 war nur
möglich, weil elf konkrete Befunde vorlagen. Ohne Belege wird die nächste
Revision Ratearbeit. Behobene Vorfälle bleiben stehen — sie sind der
Beleg, dass die Änderung nötig war. Diese Datei ist eine Chronik und
braucht daher kein Archiv.

Wer einträgt: Claude, sobald Isor einen Aussetzer meldet — zusätzlich
fragt `/harness:ende` danach, damit es nicht ausfällt.

---

### 2026-08-21 — Ownership-Befund ohne Gegenprüfung
**Was:** Claude meldete, `ROADMAP.md` verletze ihre eigene
Ownership-Regel, weil sie einen „Erledigt"-Block enthält.
**Ursache:** Tatsächlich war es ein Widerspruch **zwischen** ROADMAP und
FEATURE_LOG — beide Dateien schickten das Thema zur jeweils anderen.
Claude hatte nur eine der beiden Ownership-Zeilen gelesen, bevor er
urteilte.
**Regel:** Fehlte. Neu in DOC_RULES: Vor einem Ownership-Befund die
`Ownership:`-Zeile **aller beteiligten Dateien** lesen.
**Stand:** behoben 2026-08-22 mit DOC_RULES Abschnitt 1.

### 2026-08-21 — Angekündigte Fragen nicht gestellt
**Was:** Claude kündigte einen Fragenblock an und beendete den Zug, ohne
ihn zu stellen. Isor musste nachfragen.
**Ursache:** Reiner Ausführungsfehler, keine fehlende Regel.
**Regel:** —
**Stand:** offen. Beobachten, ob es sich wiederholt.

### 2026-08-22 — Kopfvorlage im Trennskript nicht je Datei angepasst
**Was:** Die sieben neuen Projekt-Entscheidungsdateien trugen alle den Titel
`# DECISIONS.md`, obwohl sie `Audio.md`, `Gras.md` und so weiter heißen.
**Ursache:** Die Kopfvorlage im Skript war fest verdrahtet; nur der
Beschreibungstext wurde je Datei eingesetzt, die Titelzeile nicht.
**Regel:** Fehlte. Aufgefallen erst bei der Gesamtprüfung auf tote Verweise —
also durch eine Prüfung, die nicht nach diesem Fehler suchte.
**Stand:** behoben 2026-08-22, im selben Durchgang.

### 2026-08-22 — Sicherung schloss zunächst `.git` aus
**Was:** Das Backup-Skript hätte die Repos ohne Versionsgeschichte gesichert
— 1.222 statt 2.127 Dateien. Eine Kopie der Arbeitsdateien ohne Historie ist
kein Repo.
**Ursache:** `.git` stand in derselben Ausschlussliste wie `Library`, `Temp`
und `obj`, die Unity beim nächsten Öffnen neu baut. Der Unterschied wurde
nicht bedacht.
**Regel:** Neu, jetzt im Skript vermerkt und als Wissensseite
`Knowledge/Werkzeuge/was-eine-sicherung-wertlos-macht.md`: Wer etwas
ausschließt, prüft, ob das Ziel danach seinen Zweck noch erfüllt.
**Stand:** behoben 2026-08-22, vor dem ersten echten Lauf.

### 2026-08-22 — Haken gesetzt, Arbeit nicht getan
**Was:** In `_HARNESS_UMSETZUNG.md` war unter Phase 4 abgehakt: „Eintrag
für `⚙️ System · Harness` vorbereiten (E35, I12)". In `ARTIFACT_INDEX.md`
kommt das Wort „Harness" nicht ein einziges Mal vor. Der Haken war falsch.
**Ursache:** Die Bauliste prüft sich selbst nicht. Ein Haken belegt, dass
jemand ihn gesetzt hat — nicht, dass die Datei sich geändert hat. Bei 60
Handgriffen an einem Tag fällt eine Auslassung niemandem auf.
**Regel:** Fehlte. Kandidat für den Schlussdurchgang: Wer eine Bauliste
abhakt, nennt beim Abhaken die geänderte Datei — dann ist der Haken
nachprüfbar statt nur behauptet.
**Stand:** behoben 2026-08-22 — der Eintrag steht in `Kern/ARTIFACT_INDEX.md`,
Abschnitt „⚙️ System — Schicht: Kern (der Harness selbst)". Die Seite
selbst wird nach der Abnahme gebaut.

### 2026-08-22 — Berechtigungsliste wächst aus sich selbst nach
**Was:** Unmittelbar nach dem Eindampfen von 314 auf 51 Einträge standen
zwei neue drin — der volle Wortlaut zweier `mv`- und `mkdir`-Aufrufe mit
Archivpfad, die nie wieder vorkommen.
**Ursache:** „Dauerhaft erlauben" hängt den kompletten Befehlstext an die
Liste, nicht ein Muster. So sind die 314 entstanden.
**Regel:** Fehlte. Bei einmaligen Befehlen „nur diesmal" wählen; dauerhaft
nur, wenn der Befehl als Muster taugt. Sonst wächst die Liste in Wochen
wieder auf ihren alten Stand.
**Stand:** offen — die zwei Einträge sind am 2026-08-22 entfernt, die
Ursache bleibt: Sie liegt in der Bedienung, nicht in der Datei.

### 2026-08-22 — Typ des Abschnitts nie erfragt
**Was:** Beim ersten Lauf von `/harness:sichern` war der Typ des
laufenden Abschnitts unbekannt. Die ganze Session über war nie gesagt
worden, ob gerade Design oder Development läuft — und der Typ entscheidet,
welche Dateien geschrieben werden.
**Ursache:** WORKFLOW verlangt am Session-Anfang nur die **Modus**-Frage.
Der Typ wird ausschließlich beim `/harness:wechsel` abgefragt. Wer eine
Session ohne Wechsel durchzieht, wird nie danach gefragt.
**Regel:** Fehlte. Neu in `WORKFLOW.md`, Abschnitt „Typ, Modus und
Regler": Die Startfrage lautet „Typ und Modus", nicht nur „Modus" —
beide hängen am Abschnitt und werden ohnehin gemeinsam gebraucht.
**Stand:** behoben 2026-08-22, in derselben Session, in der es auffiel.

### 2026-08-22 — Regel überlebte nur zufällig in einer Erledigt-Liste
**Was:** Die Regel „beim draw.io-Export *Include a copy of my diagram*
angehakt lassen" stand als Zusatz an einem **abgehakten** Punkt in
`C:\IsorBackup\README.md`. Beim Kürzen des README auf einen Wegweiser
wäre sie ersatzlos verschwunden. Genau diese Option hatte am 2026-08-06
fünf Diagramme gerettet.
**Ursache:** Beim Abhaken schreibt man gern dazu, was man gelernt hat —
„erledigt, ab jetzt immer X". Das „ab jetzt" ist eine Regel und stand
damit im denkbar falschesten Dokument: einer Liste, die nach dem Abhaken
niemand mehr liest.
**Regel:** Fehlte. Neu als Wissensseite
`Knowledge/Dokumentation/regeln-versauern-in-erledigt-listen.md`: Steht
in der Erledigt-Notiz ein „ab jetzt", „immer" oder „nie wieder", ist es
eine Regel und gehört in die Regeldatei ihres Themas.
**Stand:** behoben 2026-08-22, die Regel steht in `Kern/DIAGRAM_RULES.md`.
Ob daraus zusätzlich eine Harness-Regel wird, entscheidet die Abnahme.

### 2026-08-22 — Befund geurteilt, bevor die beteiligte Datei gelesen war
**Was:** Die Abnahme hielt in Befund A21 fest, der Haken „vier fehlende
Aufgabentexte nachtragen" sei falsch **und** die Arbeit damit verloren.
Der Haken ist tatsächlich falsch — die Tragweite nicht: `Uni/ROADMAP.md`
führt den Punkt ausführlich und begründet als offen. Aufgefallen erst im
sechsten Durchgang, als die Uni-Schicht gelesen wurde; im selben Zug
korrigiert.
**Ursache:** Geurteilt wurde allein aus der Bauliste heraus, ohne die
ROADMAP der betroffenen Schicht zu prüfen. `DOC_RULES.md` Abschnitt 1
verlangt genau das — aber dem Wortlaut nach nur „vor einem
**Ownership**-Befund". Ein Befund über eine nicht getane Arbeit fällt
nicht darunter, obwohl derselbe Fehler droht.
**Regel:** Vorhanden, aber zu eng gefasst. Vorschlag: die Regel „vor
einem Befund die beteiligten Dateien **aller** Schichten lesen" von
Ownership-Befunden auf alle Befunde ausweiten.
**Stand:** behoben 2026-08-22 — `DOC_RULES.md` Abschnitt 1 sagt jetzt
„vor einem Befund", nicht mehr nur „vor einem Ownership-Befund".

### 2026-08-22 — Auswahl vorgelegt, wo ein Vorschlag hingehört
**Was:** Beim letzten offenen Befund der Abnahme (A29, Abgrenzung der
sieben Entscheidungsdateien) legte Claude drei Grenzfälle als Frage vor,
statt sie zu entscheiden. Isor musste mit „Was soll ich jetzt machen?"
nachfragen.
**Ursache:** Die Regel steht in `CLAUDE.md` und im Notkern —
„Rückfrage an der Weggabelung, Empfehlung im Detail". Wohin eine
Entscheidung abgelegt wird, ist ein Detail: Es führt nicht zu
unterschiedlicher Arbeit, nur zu einem anderen Dateinamen. Claude hat die
Grenze zwischen beiden falsch gezogen, weil es um Projektwissen ging —
aber ein begründeter Vorschlag wäre auch dort möglich gewesen, und er kam
danach in einem Satz.
**Regel:** Vorhanden und ausreichend. Der Fehler lag in der Anwendung,
nicht in der Formulierung. Merkmal für den Wiederholungsfall: Wenn beide
Antworten dieselbe Arbeit nach sich ziehen, ist es ein Detail.
**Stand:** offen. Beobachten, ob es sich wiederholt — wie beim Eintrag
vom 2026-08-21 oben.
