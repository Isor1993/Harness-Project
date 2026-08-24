# PFADE.md — Orte außerhalb des Harness

Ownership: Nur die Pfade zu Orten außerhalb dieses Repos — welche Marke
wofür steht und wo der Ort auf diesem Rechner liegt. **Diese Datei ist
der einzige Besitzer eines absoluten Pfads.** Was dort inhaltlich gilt,
besitzen die Regeldateien: der Datenbaum `IsorBackup/RULES.md`, das
Wissensarchiv `Kern/KNOWLEDGE_RULES.md`, die Auslieferung
`Kern/VERSIONIERUNG.md`.
Format: eine Tabellenzeile je Marke, `| \`MARKE\` | \`Pfad\` | Zweck |`.
Die Marke steht in Großbuchstaben, der Pfad in Backticks — daran erkennen
die Werkzeuge die Zeile.

Warum es diese Datei gibt: Ein absoluter Pfad ist eine Information wie
jede andere und hatte bis 2.0.0 keinen Besitzer. Er stand an sieben
Stellen in Regeldateien verstreut, die alle in die Auslieferung wandern —
wer den Harness in ein neues Projekt kopierte, bekam Isors Ordner
vorgesetzt. Schlimmer als der offensichtliche Fall (Ordner gibt es nicht,
laute Fehlermeldung) ist der stille: Liegen zwei Harness-Ordner auf
demselben Rechner, findet der Pfad **eine** Datei — nur die falsche.

**Der Harness selbst steht hier nicht.** Er kennt sich: Innerhalb des
Repos wird relativ verwiesen (`Kern/WORKFLOW.md`), und wo ein Werkzeug den
Stamm braucht, liefert Claude Code ihn als `${CLAUDE_PROJECT_DIR}`
(`.claude\settings.json`). Eine Marke dafür wäre eine dritte Schreibweise
für dieselbe Sache.

## Die Pfade

| Marke | Pfad | Zweck |
|---|---|---|
| `DATENBAUM` | `C:\IsorBackup\` | Fester Ablagebaum für alles, was kein Repo ist — Uni-Material, Assets, Vorlagen, Auslieferungen, Archiv. Regeln: `IsorBackup/RULES.md`. |
| `KNOWLEDGE` | `C:\Repos Isor\Knowledge\` | Externes Wissensarchiv, eigenes Repo, projektübergreifend. Regeln: `Kern/KNOWLEDGE_RULES.md`. |
| `PROJEKT` | `C:\Repos Isor\Isor-Tower-ProtoTyp-2026\` | Das Code-Repo, an dem gearbeitet wird. Wird über `additionalDirectories` freigegeben, liegt nie im Harness. Bei mehreren Projekten je eine Zeile mit eigener Marke. |

## Regeln

- **Kein absoluter Pfad außerhalb dieser Datei.** Regeldateien nennen die
  Marke und verweisen hierher: „im Datenbaum unter `05_Werkzeuge\`
  (`Kern/PFADE.md` → `DATENBAUM`)". Geprüft von `pruefen.py`, Prüfung 7.
- **Ausgenommen sind die Chroniken** — `LOG.md`, `DECISIONS.md`,
  `STOERUNGEN.md`, `_ARCHIV.md` und die Zeugnisse. Sie beschreiben den
  Stand von damals, und was geschrieben ist, bleibt (`DOC_RULES.md`,
  Abschnitt 6). Ein Pfad dort ist ein Tatsachenbericht, keine Anweisung.
- **Beim Umzug wird hier geändert, sonst nirgends.** Das ist der ganze
  Zweck: eine Zeile statt einer Suche über den Bestand.
- **Ausgefüllt wird beim Einrichten**, durch `/harness:einrichten`. In
  einer frisch ausgepackten Auslieferung steht in der Pfad-Spalte
  `(nicht eingerichtet)`; der Befehl fragt die Werte ab und trägt sie ein.
- **Ein Pfad endet auf einen Backslash**, damit beim Zusammensetzen keine
  Zweifel entstehen.
