# README.md — Bilder des Kerns

Ownership: Nur die von Hand gebauten Erklärskizzen des Kerns — was hier
liegt, wozu es gehört und woran es hängt. Die skriptgenerierten
`.drawio`-Diagramme regelt `Kern/DIAGRAM_RULES.md` und sie liegen
woanders; die Artifact-Seiten regelt `Kern/ARTIFACT_RULES.md`.

Warum es diesen Ordner gibt: Eine Skizze, die einen Harness-Mechanismus
erklärt, hatte bis zum 2026-08-23 keinen Ort. `DIAGRAM_RULES.md` gilt
ausdrücklich nur für erzeugte `.drawio`-Dateien, und ein Artifact ist
eine Ausgabeform, keine Ablage. Die erste solche Skizze wäre sonst im
Sitzungs-Zwischenspeicher liegen geblieben und mit ihm verschwunden.

## Was hier liegt

| Datei | erklärt | gehört zu |
|---|---|---|
| `hook_sessionstart.svg` | den `SessionStart`-Hook: vorher eine Bitte, nachher ein Handgriff des Harness; dazu die fünf Auslöser | `CLAUDE.md` Punkt 5, `Kern/Vorlagen/README.md`, `Kern/WORKFLOW.md` → Die Prüfebenen |

## Regeln

- **Führende Quelle bleibt die `.md`-Datei.** Eine Skizze zeigt, was dort
  steht — sie entscheidet nichts. Widerspricht sie der Regeldatei, gilt
  die Regeldatei, und die Skizze ist der Befund.
- **Jede Skizze trägt ihren Stand im Bild**, nicht nur hier. Ein Bild
  wandert in Artifact-Seiten und Abgaben weiter und wird dort ohne diese
  Datei gelesen.
- **Reines SVG, keine eingebetteten Schriften oder Bilder.** So bleibt es
  im Browser, im Repo und in einer Artifact-Seite gleich lesbar.
- **Nicht doppelt pflegen:** Wandert eine Skizze in eine Artifact-Seite,
  ist die Datei hier das Original. Geändert wird hier, danach wird die
  Seite nachgezogen — dieselbe Richtung wie bei `Kern/Vorlagen/` und
  `Kern/Befehle/`.
