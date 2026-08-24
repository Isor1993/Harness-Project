# KNOWLEDGE_RULES.md — Regeln für das externe Wissensarchiv

Ownership: Schreib- und Ablageregeln für den externen Knowledge-Ordner.
Warum extern: Wissen ist projektübergreifend.

## Ablageort
Der Ort steht als Marke `KNOWLEDGE` in `Kern/PFADE.md` — außerhalb des
Harness, für alle Projekte. Extern deshalb, weil Wissen das Projekt
überlebt; ein eigenes Repo deshalb, weil es eine eigene Geschichte hat.

## Struktur
- Unterordner = Themengruppen, wachsen nach Bedarf.
- **Jeder Themenordner trägt ein `README.md` mit einer Zeile**, was er
  enthält. Kein zentrales Verzeichnis der Gruppen: Eine solche Liste war
  nach acht Stunden falsch, weil sie neben ihrer Quelle herlief. Fehlt
  ein README, sieht man es im Ordner — fehlt eine Zeile in einer Liste,
  ist die Liste still unvollständig.
- Der Root-`README.md` gibt eine kurze Orientierung: was der Ordner ist,
  wie er gegliedert ist, wo die Regeln dafür liegen. Damit ist das Repo
  auch allein verständlich.
- Eine .md-Datei pro Konzept. Dateiname: `klein-mit-bindestrichen.md`.
- `Seiten/` enthält Offline-Kopien der Artifact-Seiten als eigenständige
  HTML-Dateien: `JJJJ-MM-TT-titel.html`.
- Kein eigener Index: Der Ordnerbaum ist der Index.

## Format pro Datei
1. `# Titel`
2. `## Was & Warum` — 3–6 Sätze in eigenen Worten (nicht kopiert).
3. Optional `## Anwendung im Projekt` — das konkrete Beispiel aus der Session.
4. Optional ein Visual bei komplexen Konzepten: Mermaid-Block direkt im
   Markdown; zusätzlich Link auf die Artifact-Seite und/oder Offline-Kopie.
5. Abschlusszeile `Quelle:` mit Session-Datum und Links.
- Verweise zwischen Dateien als relative Markdown-Links. Die
  Bildschirm-Härtegrenze steht unten unter „Wann wird geschrieben".

## Wann wird geschrieben

**Den Zeitpunkt besitzt `WORKFLOW.md`** (Doku-Pflicht): Die
Knowledge-Frage wird bei **jedem** Session-Ende gestellt, unabhängig vom
Typ und vom Modus. Claude schlägt Themen vor, Isor wählt aus oder ergänzt.
„Nein" ist eine gültige Antwort — die Frage darf nie ausfallen.

Hier steht nur, was beim Schreiben gilt:
- **Bestehende Datei zum selben Konzept: erweitern statt duplizieren.**
- Ein Konzept, das nicht auf einen Bildschirm passt, sind zwei — dann
  zwei Dateien mit gegenseitigem Verweis.
- Eine Seite wird zusätzlich als Artifact gebaut, **wenn sie visuell
  ist** — Diagramme, Zahlenbeispiele, Vergleiche. Reiner Text liest sich
  in der .md genauso gut. Form und Pflege der Seite: `ARTIFACT_RULES.md`.
