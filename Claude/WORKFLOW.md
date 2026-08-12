# WORKFLOW.md — Session-Disziplin

Ownership: Session-Typen und Session-Disziplin.

## Grundregeln
- Jede Session hat genau einen Typ und einen Fokus.
- Vor jedem /clear: Doku-Pflicht — INDEX.md und ROADMAP.md nachziehen,
  Gebautes in FEATURE_LOG.md, Entscheidungen in DECISIONS.md;
  Knowledge-Abfrage in jeder Session (KNOWLEDGE_RULES.md), im
  Uni-Modus Pflicht; TDD-relevante Ergebnisse grob in TDD_NOTES.md
  einreihen (nur echte Uni-Projekt-Arbeit).
- Session-Ende: Claude schlägt den Commit vor — Titel im Schema
  `Update V <nächste Nummer>` (vierstellig hochgezählt, z. B. V 0.0003)
  plus fertige Description (was die Session geändert hat). Titel und
  Description immer auf Englisch — das Repo ist englischsprachig.
  Isor committet selbst über **GitHub Desktop**: Der Vorschlag kommt
  deshalb als zwei kopierbare Textblöcke „Summary" und „Description",
  nie als `git commit`-Befehl. Claude committet und pusht nicht.
- Max. 2–4 parallel offene Sessions.
- Session-Schnitt an der Baustein-Grenze, nicht am Kontext-Balken:
  Baustein fertig → Sichern → Commit → /clear. Einen neuen Baustein
  nicht unter ~30 % Restkontext starten — lieber vorher schneiden.

## Session-Typen

### Brainstorm/Design (im Einsatz, getestet)
Ideen verarbeiten/evaluieren, freies Brainstorming, ausdesignen was
gebaut wird und wie — Sonderaufgaben ohne Code. Ergebnis: Entscheidungen
in DECISIONS.md, Design-Absicht später ins GDD.
Regel pro Baustein: erst eine Brainstorm/Design-Session (was & wie
entscheiden), dann die Development-Session (nur Umsetzung). Eine
Brainstorm/Design-Session darf mehrere Bausteine vorentscheiden.
Zu Beginn fragt Claude, welcher Modus gilt: **normal** oder **uni**.
- **Normal** — wie oben, kurz und bündig.
- **Uni** — Fokus auf Erklären, nicht auf Bauen/Entscheiden:
  - Einfach erklären, wo möglich visuell (Skizzen/Diagramme, zusätzlich
    als Artifact fürs Handy).
  - Ausführlich statt knapp — bewusste Ausnahme von "kurz und bündig".
  - Claude prüft aktiv per Rückfrage, ob Isor es verstanden hat; falls
    nicht: einfacher erklären, nicht nur wiederholen.
  - Ziel: Isor lernt es und kann es später selbst anwenden.
  - Erkenntnisse am Session-Ende in den Knowledge-Ordner
    (KNOWLEDGE_RULES.md).

### Development (minimal; erster Praxistest: Chunk-Umbau)
Nur Umsetzung dessen, was in DECISIONS.md vorentschieden ist.
Lern-Modus ist der Normalfall: Isor tippt selbst; Claude liefert
Gerüst, Erklärungen und Rechenbeispiele zum Prüfen — keine fertigen
Dateien.
**Entwurf vor Gerüst (Regel seit 2026-08-05):** Bevor Claude ein Gerüst
zeigt, beschreibt Isor in zwei Sätzen, was das Stück tun muss und welche
Werte es dafür braucht. Erst danach kommt das Gerüst, und der Vergleich
zeigt, wo der eigene Entwurf abwich. Grund: Vorgegebene TODOs üben das
Ausfüllen, nicht das Anfangen vor einer leeren Datei — genau da liegt die
Lücke. Kostet Sekunden, keine Extra-Übungszeit.
Claude wartet die Antwort ab, statt das Gerüst nachzuschieben. Kleine Design-Fragen (Namen, Ablageort) werden inline geklärt;
Fragen, die Architektur oder mehrere Bausteine betreffen, werden
notiert und in die nächste Brainstorm/Design-Session gegeben.
Vor dem Coden: Review-Gate aus CODE_GUIDELINES.md durchgehen.
Gebautes in FEATURE_LOG.md, Entscheidungen in DECISIONS.md.
Commits: siehe Grundregel „Session-Ende". Typ wird im Praxistest
nachgeschärft. (Später-Schublade: automatisierter Modus — Claude baut,
Isor reviewt — erst nach der Lernphase.)

### Art (minimal, ungetestet)
Prompts für Image-Generation/Concepts erzeugen — bildliche Kommunikation
mit der AI.

### Zeugnis (eingeführt 2026-08-11)
Standortbestimmung zu einem festen Datum: Notenschätzung der Abgaben,
Profil zur Arbeitsweise, Profil zum Coding-Stand. Wird bewusst
wiederholt — der Vergleich zweier Stände ist der Zweck, nicht das
einzelne Feedback.
Eigene Regeln in **ASSESSMENT_RULES.md** (Verfahren, Belegpflicht,
Aufbau, Notenskala); die Zeugnisse selbst in ASSESSMENT_LOG.md.
Auslöser: `/zeugnis` oder Zuruf.
Abgrenzung: Diese Session **liest und bewertet nur**. Sie baut nichts,
entscheidet nichts und schreibt in keine fremde Datei — Befunde gehen
als Aufgaben in die ROADMAP, nie als Umbau in den Code.
Doku-Pflicht am Ende, abweichend von der Grundregel: ASSESSMENT_LOG.md
und ARTIFACT_INDEX.md sind Pflicht, ROADMAP nur um die Befunde ergänzt.
FEATURE_LOG, DECISIONS, TDD_NOTES und Knowledge bleiben unberührt —
es wurde nichts gebaut, entschieden oder gelernt.
