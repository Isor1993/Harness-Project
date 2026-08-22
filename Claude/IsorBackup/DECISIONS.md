# DECISIONS.md — Entscheidungen Datenablage

Ownership: Nur Entscheidungen zum Datenbaum `C:\IsorBackup\` — was
entschieden wurde, warum, und welche Alternativen verworfen wurden. Kein
Plan (das ist `ROADMAP.md` dieser Schicht), keine ausformulierte Regel
(die steht in `RULES.md`; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden.

## 2026-08-06 — Datenbaum direkt auf `C:\`, nicht unter `C:\Users\`
Was: `C:\IsorBackup\` liegt auf der Laufwerkswurzel.
Warum: Zwei Gründe. OneDrive kann nur den OneDrive-Ordner und umgeleitete
Benutzerordner (Desktop, Dokumente, Bilder) erfassen — was hier liegt,
ist für OneDrive **strukturell unerreichbar** und wird nicht ungefragt
hochgeladen. Dazu kurze Pfade: Windows bricht bei 260 Zeichen ab, und
Unity-Projekte werden tief.
Verworfen: Ablage unter `C:\Users\<Name>\`, der Windows-Normalfall.

## 2026-08-06 — `Repos Isor` behält seinen Namen
Was: Der Repo-Ordner heißt weiter `C:\Repos Isor` — **kein** Umbenennen
nach `IsorRepos`, obwohl das besser zum Namensschema passen würde.
Warum: Umbenennen löst die Verknüpfungen in GitHub Desktop, ohne dass ein
Nutzen dem gegenübersteht. Der Name enthält ein Leerzeichen und verstößt
damit gegen Regel 5 in `RULES.md` — das ist eine bewusst hingenommene
Ausnahme, keine Nachlässigkeit.
Verworfen: Umbenennen nach `IsorRepos`. Der Plan stand am 2026-08-06 noch
im Kopf des `README.md` und wurde am selben Tag verworfen, die Kopfzeile
aber nicht nachgezogen — der Widerspruch stand bis 2026-08-22 in der
Datei (Befund G-a der Überholung).

## 2026-08-22 — Die Regeln ziehen in den Harness
Was: `RULES.md`, `ROADMAP.md` und diese Datei liegen in der
Harness-Schicht `IsorBackup/`. In `C:\IsorBackup\README.md` bleibt nur
ein Wegweiser.
Warum: `C:\IsorBackup` ist kein Git-Repo — der Regeltext hatte dort keine
Versionsgeschichte. Dazu enthielt das README vier Sorten Information in
einer Datei: Regeln, eine ROADMAP („Offene Punkte"), eine Entscheidung
(„Bewusst verworfen") und ein Verzeichnis (den Ordnerbaum). Nach der
Ownership-Regel sind das drei Dateien plus Wegweiser.
Verworfen: Das README als Ganzes im Datenbaum lassen — bequemer beim
Nachschlagen vor Ort, aber ohne Historie und weiter viersortig.
