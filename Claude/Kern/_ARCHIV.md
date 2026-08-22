# _ARCHIV.md — Kern, überholte Einträge

Ownership: Nur überholte Einträge der Kern-Schicht. Jeder nennt, wodurch
er abgelöst wurde. Wird nie aufgeräumt — ein Archiv wird selten gelesen,
seine Größe kostet nichts (`Kern/DOC_RULES.md`, Abschnitt 4).

---

## 2026-08-22 — Der „Erledigt"-Block der alten ROADMAP

**Abgelöst durch:** die Chroniken `Kern/LOG.md`, `Uni/LOG.md` und
`Projekte/Isor_Tower/LOG.md`.

**Was war das:** 48 Zeilen mit sechzehn abgehakten Punkten, überwiegend
Zusammenfassungen von Ereignissen, die ausführlicher im damaligen
`FEATURE_LOG.md` standen — der Block verwies selbst dorthin.

**Was übernommen wurde:**
- Sieben Harness-Bauten → `Kern/LOG.md` (Kern-Dateien, WORKFLOW,
  Knowledge-System, FEATURE_LOG/DECISIONS, CODE_GUIDELINES,
  Artifact-Seiten, Session-Typ Zeugnis)
- „GDD.md als Short GDD angelegt" → `Projekte/Isor_Tower/LOG.md`
- „Abgabe-Ordnerstruktur gebaut und befüllt" → `Uni/LOG.md`

**Was nicht übernommen wurde und warum:** Terrain-Pipeline,
Gras-Instancing, Threadoptimierung, Gras-Rendering, die neun Diagramme,
das fertige TDD und das TDD-Layout. Alle sieben standen bereits
ausführlich in den LOGs; eine zweite, kürzere Fassung wäre eine Kopie
gewesen und hätte gegen den Ein-Ort-Test verstoßen.

**Vollständiger Originaltext:** `ROADMAP.md` in
`C:\IsorBackup\99_Archiv\_Zu_Loeschen\2026-08-22_Harness_Umbau\`.

## 2026-08-22 — Grobziel und Nahziel der alten ROADMAP

**Grobziel** („Generischer Harness für Game-Dev- und Learn-Sessions,
.md-Dateien als Gedächtnis, Sessions als Wegwerf-Arbeitsräume") →
abgelöst durch `CLAUDE.md`, wo es seither in kürzerer Form steht. Eine
Zielbeschreibung ist keine Baureihenfolge.

**Nahziel** (zwei Phasen: bis zur Uni-Abgabe am 2026-08-21, danach
Ausrichtung am GDD) → überholt. Die Abgabe ist am 2026-08-20 hochgeladen;
die zweite Phase läuft seit dem 2026-08-22 und steht in `PLAN.md`.

## 2026-08-22 — Zwei abgelöste Konventions-Einträge

Beide standen bis heute in `DECISIONS.md` und sind dort nicht mehr
die gültige Fassung. Die Begründungen von damals bleiben hier
nachlesbar.

**Abgelöst durch `Kern/DOC_RULES.md`, Abschnitt 9 (Sprachtabelle)
bzw. `Kern/VERSIONIERUNG.md`:**

### 2026-07-17 — Sprache: Code englisch, Unterhaltung deutsch
Was: Code, Kommentare, Debug-Ausgaben und Commit-Messages ausnahmslos
Englisch; Harness-Doku und Unterhaltung mit Claude vorerst Deutsch.
Warum: GitHub-Repo ist englischsprachig, Fachbegriffe bleiben konsistent
mit der Unity-/C#-Welt; Deutsch hilft beim Lernen.
Verworfen: Sprachwahl je Situation; sofortige Englisch-Umstellung des
Harness (geparkt in ROADMAP „Später").

### 2026-08-16 — Versionsschema nach Reifegrad
Was: Die Build-Version (`Player Settings > Version`) folgt dem Reifegrad des
Spiels, nicht dem üblichen Semantic Versioning:

| Form | Bedeutung |
|---|---|
| `0.0.x` | Prototyp — x zählt die Stände hoch |
| `0.x.0` | Early Access |
| `1.x.x` | fertiges Spiel |

Solange die vordere Stelle `0` ist, ist das Spiel nicht fertig; solange die
mittlere `0` ist, ist es nicht einmal Early Access. Stand 2026-08-16: `0.0.2`.
Warum: Isor will an der Versionsnummer den Reifegrad ablesen, nicht die Art
der letzten Änderung. Bei Semantic Versioning stünde die mittlere Stelle für
neue Funktionen und die hintere für Fehlerbehebungen — das sagt nichts
darüber, wie weit das Spiel ist, und genau das ist hier die interessante
Information.
Verworfen: Semantic Versioning (MAJOR.MINOR.PATCH). Aufgefallen war die
Vermischung an `0.1.1`, das nach Isors eigenem Schema bereits Early Access
behauptet hätte.

