# INDEX.md — Landkarte

Ownership: Nur die Landkarte — welche Dokumente existieren und wofür jedes
zuständig ist. Eine Zeile pro Dokument, keine Inhalte.

**Diese Datei wird erzeugt.** Sie kommt aus der `Ownership:`-Zeile jeder
Datei; von Hand geändert wird sie nicht, sondern über
`Kern/Werkzeuge/index_bauen.py`. Geplante, noch nicht gebaute Dokumente
stehen daneben in `index_geplant.txt`.

Der INDEX bleibt bewusst **oben** und wird nicht in eine Schicht
einsortiert: Er ist ein Register über alle Schichten, und ein Register
muss vollständig sein (`Kern/DOC_RULES.md`, Abschnitt 8).

Eine Datei ohne `Ownership:`-Zeile erscheint hier als ⚠ — so setzt sich
die Regel „keine neue Datei ohne INDEX-Eintrag" von selbst durch, statt
erinnert werden zu müssen.

Eine Gruppe führt der Index abweichend, unten mit eigener Tabelle: die
**Befehle**. Sie tragen keine Ownership-Zeile — ihre `description` ist
die Zuständigkeit. Sie stehen hier, weil ein Register vollständig sein
muss (`Kern/DOC_RULES.md`, Abschnitt 8).

## Oben — schichtübergreifend

| Dokument | Zuständigkeit |
|---|---|
| `CLAUDE.md` | Nur das Verhalten von Claude in diesem Projekt und der Einstieg in eine Session. |
| `INDEX.md` | Nur die Landkarte — welche Dokumente existieren und wofür jedes zuständig ist. |
| `PLAN.md` | Was in den nächsten ein bis drei Wochen dran ist, schichtübergreifend — und der Auftrag an die nächste Session. |

## Kern — generisch, wandert in jedes Projekt mit

| Dokument | Zuständigkeit |
|---|---|
| `Kern/ARTIFACT_INDEX.md` | Welche Artifact-Seiten es gibt, woran jede hängt und wer auf sie zeigt. |
| `Kern/ARTIFACT_RULES.md` | Typen, Benennung, Aufbau, Gestaltung, Symbole und Pflege der Artifact-Seiten auf claude.ai. |
| `Kern/ASSESSMENT_RULES.md` | Der Session-Typ „Zeugnis" vollständig — Auslöser, Ablauf, Belegpflicht, Aufbau, Notenskala, Schreibregeln, Ablage. |
| `Kern/CODE_GUIDELINES.md` | Code-Konventionen — Namen, Architektur, Ordnerstruktur, das Review-Gate. |
| `Kern/DECISIONS.md` | Nur Entscheidungen zum Harness — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Kern/DIAGRAM_RULES.md` | Nur der Umgang mit den skriptgenerierten `.drawio`-Diagrammen — Ablage, Arbeitsteilung, Bedienregeln, Prüfung. |
| `Kern/DOC_RULES.md` | Alle Regeln, die für die .md-Dateien des Harness selbst gelten — Zuständigkeit, Aufbau, Verweise, Verfall, Sprache. |
| `Kern/GDD_RULES.md` | Aufbau und Pflege eines GDD — was hineingehört, wie mit offenen Punkten umgegangen wird, wann aus einem Entwurf feste Absicht wird, in welchem Takt es nachgezogen wird. |
| `Kern/GLOSSARY.md` | Nur die **Kurzform** jedes Begriffs und der Zeiger auf seinen Besitzer. |
| `Kern/KNOWLEDGE_RULES.md` | Schreib- und Ablageregeln für den externen Knowledge-Ordner. |
| `Kern/LOG.md` | Nur was wann passiert ist — datierte Ereignisse, älteste oben. |
| `Kern/ROADMAP.md` | Nur was am Harness als Nächstes gebaut wird. |
| `Kern/STOERUNGEN.md` | Nur Vorfälle, in denen der Harness nicht so gearbeitet hat wie vorgesehen — was passiert ist und welche Regel nicht gegriffen hat. |
| `Kern/VERSIONIERUNG.md` | Alle Nummernsysteme des Projekts — welche Nummer was zählt, wie sie gelesen wird und wo sie steht. |
| `Kern/WORKFLOW.md` | Wie eine Session abläuft — Begriffe, Typ und Modus samt Reglern, Session-Typen, Doku-Pflicht, die Befehle, der Pflegetag und das Session-Ende. |
| `Kern/Zeugnisse/2026-08-11.md` | Nur dieses eine Zeugnis — ein datierter Messpunkt. |
| `Kern/Zeugnisse/2026-08-16.md` | Nur dieses eine Zeugnis — ein datierter Messpunkt. |
| `Kern/_ARCHIV.md` | Nur überholte Einträge der Kern-Schicht. |

## Uni — studienspezifisch, herausnehmbar

| Dokument | Zuständigkeit |
|---|---|
| `Uni/DECISIONS.md` | Nur Entscheidungen zum Studium — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Uni/DOCX_RULES.md` | Nur der Umgang mit den `.docx`-Abgabedateien — Sicherung, Arbeitsteilung, bekannte Fallen, Prüfung. |
| `Uni/LOG.md` | Nur was wann passiert ist — datierte Ereignisse, älteste oben. |
| `Uni/ROADMAP.md` | Nur was für das Studium als Nächstes zu tun ist, semesterübergreifend. |
| `Uni/Semester_2/ASSIGNMENT_AKADEMISCH.md` | (geplant) Originaltext der Teilabgabe Arbeiten nach akademischen Standards |
| `Uni/Semester_2/ASSIGNMENT_KI_PROTOTYP.md` | (geplant) Originaltext der Teilabgabe KI-Prototyp |
| `Uni/Semester_2/ASSIGNMENT_PCG.md` | Originaltext der Uni-Aufgabe PCG (K3, S2, S3) als Referenz — unverändert lassen, eigene Planung gehört in die DECISIONS der Schicht. |
| `Uni/Semester_2/ASSIGNMENT_SIMULATION.md` | (geplant) Originaltext der Teilabgabe Simulation der Spieleumgebung |
| `Uni/Semester_2/ASSIGNMENT_SOFTWAREPLANUNG.md` | (geplant) Originaltext der Teilabgabe Softwareplanung |
| `Uni/Semester_2/ASSIGNMENT_THREADING.md` | Originaltext der Uni-Aufgabe Threadoptimierung (K2, K3, S3) als Referenz — unverändert lassen; eigene Planung gehört in die DECISIONS der Schicht. |
| `Uni/Semester_2/ASSIGNMENT_TOOL.md` | Originaltext der Uni-Aufgabe Engine-Tool (K2, S1) als Referenz — unverändert lassen; eigene Planung gehört in die DECISIONS der Schicht. |
| `Uni/_ARCHIV.md` | Nur überholte Einträge der Uni-Schicht. |

## IsorBackup — Regeln für den externen Datenbaum

| Dokument | Zuständigkeit |
|---|---|
| `IsorBackup/DECISIONS.md` | Nur Entscheidungen zum Datenbaum `C:\IsorBackup\` — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `IsorBackup/LOG.md` | (geplant) Chronik des Datenbaums — fällig, sobald der erste Aufräum-Durchgang läuft |
| `IsorBackup/ROADMAP.md` | Nur die offenen Aufräum-Punkte des Datenbaums `C:\IsorBackup\`. |
| `IsorBackup/RULES.md` | Baum, Ablageregeln, Benennung und Asset-Library für `C:\IsorBackup\`. |
| `IsorBackup/_ARCHIV.md` | (geplant) Überholte Einträge der IsorBackup-Schicht — DECISIONS.md verweist bereits darauf |

## Projekte

| Dokument | Zuständigkeit |
|---|---|
| `Projekte/Isor_Tower/DECISIONS/Audio.md` | Nur Entscheidungen zu Audio — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/DECISIONS/Entities.md` | Nur Entscheidungen zu Entities und KI — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/DECISIONS/Gras.md` | Nur Entscheidungen zu Gras und Instancing — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/DECISIONS/Platzierung.md` | Nur Entscheidungen zu Platzierung — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/DECISIONS/Terrain_Mesh.md` | Nur Entscheidungen zu Terrain und Mesh — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/DECISIONS/UI.md` | Nur Entscheidungen zu UI, Menüs und HUD — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/DECISIONS/Welt.md` | Nur Entscheidungen zu Welt, Szene und Interaktion — was entschieden wurde, warum, und welche Alternativen verworfen wurden. |
| `Projekte/Isor_Tower/GDD.md` | Design-Absicht des Spiels — was es sein soll, nicht wie es gebaut wird. |
| `Projekte/Isor_Tower/LOG.md` | Nur was wann passiert ist — datierte Ereignisse, älteste oben. |
| `Projekte/Isor_Tower/PREFAB_STATUS.md` | Nur der Prüfstand jedes Prefabs — welche schon durchgesehen sind und was dabei auffiel. |
| `Projekte/Isor_Tower/ROADMAP.md` | Nur was am Projekt als Nächstes gebaut wird. |
| `Projekte/Isor_Tower/SYSTEME.md` | (geplant) Was gerade im Projekt steckt — wird erzeugt |
| `Projekte/Isor_Tower/TDD.md` | (geplant) Markdown-Manuskript des TDD, aus dem die Abgabefassung entsteht |
| `Projekte/Isor_Tower/TDD_NOTES.md` | Nur Rohmaterial für das Technical Design Document von Isor's Tower — geprüfte Fakten, Zahlen und Formeln aus der Projektarbeit. |
| `Projekte/Isor_Tower/_ARCHIV.md` | (geplant) Überholte Projekt-Einträge, jeder mit Angabe des Nachfolgers |

## Temporär — eine Datei je Durchgang, danach ins Archiv

| Dokument | Zuständigkeit |
|---|---|
| `_HARNESS_ARTIFACTS_1_0_0.md` | Nur die Befunde **dieses einen Durchgangs** durch die acht Altbestand-Seiten, geprüft am 2026-08-23 gegen die veröffentlichten Seiten und den Code von Isor's Tower. |
| `_HARNESS_PRUEFUNG_1_0_0.md` | Nur die Befunde **dieses einen Prüfdurchgangs** — der rund zwanzig Dateien, die am 2026-08-23 beim Bau der Version 1.0.0 geschrieben und nicht gegengelesen wurden. |
| `_HARNESS_UMBAU_STRUKTUR.md` | Nur die Handgriffe **dieser einen Umbau-Folge** — der Harness wird sein eigenes Repo, danach werden die Skript-Prüfungen als Hooks erzwungen. |

## Werkzeuge — erzeugen und pflegen die Dateien oben

| Skript | Zweck |
|---|---|
| `IsorBackup/Werkzeuge/sichern.ps1` | sichern.ps1 — wöchentliche Sicherung auf die externe Platte. |
| `Kern/Werkzeuge/index_bauen.py` | Erzeugt INDEX.md aus den Ownership-Zeilen der Harness-Dateien. |
| `Kern/Werkzeuge/pruefen.py` | Prüft die Harness-Dateien gegen die Regeln, die sich mechanisch prüfen lassen. |
| `Projekte/Isor_Tower/Werkzeuge/prefab_status.py` | Erzeugt PREFAB_STATUS.md aus den tatsächlich vorhandenen .prefab-Dateien. |

## Befehle — Auslöser, Ablauf in `Kern/WORKFLOW.md`

Original in `Kern/Befehle/`, Arbeitskopie in `.claude\commands\harness\` — geändert wird das Original, dann kopiert.

| Befehl | Tut |
|---|---|
| `/harness:ende` | Session abschließen — sichern, Baustein prüfen, Commit-Vorschlag |
| `/harness:sichern` | Doku-Pflicht des laufenden Abschnitts abarbeiten, Session läuft weiter |
| `/harness:sonntag` | Pflegetag — Artifact-Durchsicht, unabhängig vom Session-Typ |
| `/harness:wechsel` | Abschnitt beenden und auf einen anderen Session-Typ umstellen |
| `/harness:zeugnis` | Standortbestimmung zu einem festen Datum — Session-Typ „Zeugnis" |
