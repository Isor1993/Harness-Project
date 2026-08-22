# INDEX.md — Landkarte

Ownership: Nur die Landkarte — welche Dokumente existieren und wofür
jedes zuständig ist. Eine Zeile pro Dokument, keine Inhalte. Die
Zuständigkeit stammt aus der `Ownership:`-Zeile der jeweiligen Datei;
diese Tabelle wird später daraus erzeugt.
Format: `| <Pfad> | <Zuständigkeit in einem Satz> |`, gruppiert nach
Schicht. Ohne Vermerk = existiert, (geplant) = noch nicht gebaut.

Der INDEX bleibt bewusst **oben** und wird nicht in eine Schicht
einsortiert: Er ist ein Register über alle Schichten, und ein Register
muss vollständig sein (DOC_RULES, Abschnitt 8).

## Oben — schichtübergreifend

| Dokument | Zuständigkeit |
|---|---|
| `CLAUDE.md` | Verhalten von Claude: Grundregeln, Leseordnung bei Session-Start, Harness-Version. Liegt oben, weil der Harness sie automatisch lädt — gehört aber in jede Kern-Auslieferung |
| `INDEX.md` | Landkarte aller Dokumente |
| `PLAN.md` | Nur was in den nächsten 1–3 Wochen dran ist, schichtübergreifend; wird nach jedem Zeitraum geleert |

## Kern — generisch, wandert in jedes Projekt mit

| Dokument | Zuständigkeit |
|---|---|
| `Kern/DOC_RULES.md` | Alle Regeln für die .md-Dateien des Harness selbst: Zuständigkeit, Aufbau, Verweise, Verfall, Sprache, Schichten |
| `Kern/WORKFLOW.md` | Session-Disziplin: Session-Typen, Modus und Regler, Doku-Pflicht, Befehle |
| `Kern/VERSIONIERUNG.md` | Die drei Nummernsysteme (Commit, Spiel-Reifegrad, Harness-Verträglichkeit): was jede zählt, wie sie gelesen wird, wo sie steht |
| `Kern/CODE_GUIDELINES.md` | Code-Konventionen: Namen, Architektur, Review-Gate, Unity-Ordnerstruktur |
| `Kern/GDD_RULES.md` | Aufbau und Pflege eines GDD: Kapitelfolge, offen-Mechanismus, Entwurfs-Abschnitt, Takt, GDD als Abgabetext |
| `Kern/KNOWLEDGE_RULES.md` | Ablage- und Schreibregeln für das externe Wissensarchiv `C:\Repos Isor\Knowledge\` |
| `Kern/ARTIFACT_RULES.md` | Typen, Benennung, Aufbau, Symbole und Pflege der Artifact-Seiten |
| `Kern/ARTIFACT_INDEX.md` | Bestand der Artifact-Seiten — über alle Schichten, mit Schicht-Angabe je Eintrag |
| `Kern/DIAGRAM_RULES.md` | Verfahren für die erzeugten `.drawio`-Diagramme: Arbeitsteilung, Bedienregeln, Prüfung |
| `Kern/ASSESSMENT_RULES.md` | Regeln des Session-Typs „Zeugnis": Auslöser, Disziplin, Belegpflicht, Aufbau, Notenskala, Artifact-Ausnahme |
| `Kern/STOERUNGEN.md` | Vorfälle im Betrieb: was schiefging und welche Regel nicht griff — Chronik, kein Archiv |
| `Kern/Zeugnisse/` | Die Zeugnisse selbst, eine Datei je Termin — derzeit `2026-08-11.md` und `2026-08-16.md` |
| `Kern/GLOSSARY.md` | (geplant) Begriffe mit fester Bedeutung — entsteht am Ende aus den fertigen Dateien |
| `Kern/ROADMAP.md` | Baureihenfolge des Harness — nur Offenes, ohne Datum |
| `Kern/LOG.md` | Chronik des Harness: was wann gebaut wurde — Ereignisse, nie geändert, kein Archiv |
| `Kern/DECISIONS.md` | Entscheidungen zum Harness und zu den projektübergreifenden Code- und Ordner-Konventionen (27) |
| `Kern/_ARCHIV.md` | Überholte Kern-Einträge, jeder mit Angabe, wodurch er abgelöst wurde |

## Uni — studienspezifisch, herausnehmbar

| Dokument | Zuständigkeit |
|---|---|
| `Uni/DOCX_RULES.md` | Umgang mit den `.docx`-Abgabedateien: Sicherung, Arbeitsteilung, Fallen, Felder, Prüfung |
| `Uni/Semester_2/ASSIGNMENT_PCG.md` | Originaltext Uni-Aufgabe „Prozedurale Erweiterung der Spielwelt" (Referenz, unverändert lassen) |
| `Uni/Semester_2/ASSIGNMENT_TOOL.md` | Originaltext Uni-Aufgabe „Engine-Tool-Entwicklung" (Referenz, unverändert lassen) |
| `Uni/Semester_2/ASSIGNMENT_THREADING.md` | Originaltext Uni-Aufgabe „Threadoptimierung" (Referenz, unverändert lassen) |
| `Uni/ROADMAP.md` | Baureihenfolge der Studienarbeit, semesterübergreifend |
| `Uni/LOG.md` | Chronik der Studienarbeit: TDD, Abbildungen, Abgaben |
| `Uni/_ARCHIV.md` | Abgeschlossene Semester und überholte Einträge — enthält den Abgabe-Tagesplan von Semester 2 |

## IsorBackup — Regeln für den externen Datenbaum

| Dokument | Zuständigkeit |
|---|---|
| `IsorBackup/RULES.md` | (geplant) Baum, Ablageregeln, Benennung, Asset-Library für `C:\IsorBackup\` |
| `IsorBackup/ROADMAP.md` | (geplant) Offene Aufräum-Punkte |
| `IsorBackup/DECISIONS.md` | (geplant) Entscheidungen zur Datenablage |

## Projekte

| Dokument | Zuständigkeit |
|---|---|
| `Projekte/Isor_Tower/GDD.md` | Design-Absicht des Spiels — zugleich Markdown-Manuskript der Abgabe |
| `Projekte/Isor_Tower/TDD_NOTES.md` | Stoffsammlung fürs TDD — geprüfte Fakten und Zahlen in zehn Themenblöcken, kumulativ über alle Semester |
| `Projekte/Isor_Tower/PREFAB_STATUS.md` | Prüfstand jedes Prefabs — Arbeitsliste mit Ende, wird erzeugt |
| `Projekte/Isor_Tower/DECISIONS/Platzierung.md` | Entscheidungen zu Poisson, Dichte, Placer, Exclusion, Kachelung (21) |
| `Projekte/Isor_Tower/DECISIONS/UI.md` | Entscheidungen zu Menüs, HUD, Optionen, Ladescreen (16) |
| `Projekte/Isor_Tower/DECISIONS/Terrain_Mesh.md` | Entscheidungen zu Heightmap, Mesh, Chunks, Config, Wasserspiegel (13) |
| `Projekte/Isor_Tower/DECISIONS/Welt.md` | Entscheidungen zu Szene, Hierarchie, Interaktion, Tag/Nacht (11) |
| `Projekte/Isor_Tower/DECISIONS/Audio.md` | Entscheidungen zu Mixer, Klangquellen, Audio-Library (9) |
| `Projekte/Isor_Tower/DECISIONS/Entities.md` | Entscheidungen zu Schafen, Herden, FSM, Health (7) |
| `Projekte/Isor_Tower/DECISIONS/Gras.md` | Entscheidungen zu Instancing, LOD, Gras-Verteilung (5) |
| `Projekte/Isor_Tower/ROADMAP.md` | Baureihenfolge des Projekts: Basiszustand, Aufräumen, HUD, Beobachtungspunkte, Politur |
| `Projekte/Isor_Tower/LOG.md` | Chronik des Projekts: was wann gebaut und geprüft wurde |
| `Projekte/Isor_Tower/SYSTEME.md` | (geplant) Was gerade im Projekt steckt — wird erzeugt |
| `Projekte/Isor_Tower/_ARCHIV.md` | (geplant) Überholte Projekt-Einträge |

## Temporär — werden nach der Überholung archiviert

| Dokument | Zuständigkeit |
|---|---|
| `_HARNESS_REVIEW.md` | Befunde und Entscheidungen der Harness-Überholung ab 2026-08-21 |
| `_HARNESS_UMSETZUNG.md` | Bauliste der Überholung in Baureihenfolge — Handgriffe zum Abhaken |
