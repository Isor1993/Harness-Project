# STOERUNGEN.md — Was im Betrieb nicht funktioniert hat

Ownership: Nur Vorfälle, in denen der Harness nicht so gearbeitet hat wie
vorgesehen — was passiert ist und welche Regel nicht gegriffen hat.
Das LOG besitzt „was ist passiert", diese Datei „was ist schiefgegangen".
Keine Aufgaben (das ist die ROADMAP), keine Begründungen (DECISIONS).
Format: `### JJJJ-MM-TT — Kurztitel` mit den Zeilen **Was**, **Ursache**,
**Regel** und, sobald behoben, **Behoben**.

Warum die Datei existiert: Die Überholung von 2026-08-21/22 war nur
möglich, weil elf konkrete Befunde vorlagen. Ohne Belege wird die nächste
Revision Ratearbeit. Behobene Vorfälle bleiben stehen — sie sind der
Beleg, dass die Änderung nötig war. Diese Datei ist eine Chronik und
braucht daher kein Archiv.

Wer einträgt: Claude, sobald Isor einen Aussetzer meldet — zusätzlich
fragt die `/ende`-Routine danach, damit es nicht ausfällt.

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
**Behoben:** 2026-08-22 mit DOC_RULES Abschnitt 1.

### 2026-08-21 — Angekündigte Fragen nicht gestellt
**Was:** Claude kündigte einen Fragenblock an und beendete den Zug, ohne
ihn zu stellen. Isor musste nachfragen.
**Ursache:** Reiner Ausführungsfehler, keine fehlende Regel.
**Regel:** —
**Behoben:** offen. Beobachten, ob es sich wiederholt.

### 2026-08-22 — Kopfvorlage im Trennskript nicht je Datei angepasst
**Was:** Die sieben neuen Projekt-Entscheidungsdateien trugen alle den Titel
`# DECISIONS.md`, obwohl sie `Audio.md`, `Gras.md` und so weiter heißen.
**Ursache:** Die Kopfvorlage im Skript war fest verdrahtet; nur der
Beschreibungstext wurde je Datei eingesetzt, die Titelzeile nicht.
**Regel:** Fehlte. Aufgefallen erst bei der Gesamtprüfung auf tote Verweise —
also durch eine Prüfung, die nicht nach diesem Fehler suchte.
**Behoben:** 2026-08-22, im selben Durchgang.

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
**Behoben:** 2026-08-22, vor dem ersten echten Lauf.
