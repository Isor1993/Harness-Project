# ASSIGNMENT_THREADING.md — Uni-Aufgabe „Threadoptimierung"

Ownership: Originaltext der Uni-Aufgabe Threadoptimierung (K2, K3, S3) als
Referenz — unverändert lassen; eigene Planung gehört in die DECISIONS der Schicht. Quelle: Canvas, Kurs 23111 — Modul 4FSC0PD003.1
„Structured Game Development" (Übung „Multithreading"). Formative Abgabe:
Fr 2026-08-07. Echte Abgabe: Portfolio 2026-08-21. Wird kombiniert mit
ASSIGNMENT_PCG.md und ASSIGNMENT_TOOL.md.

---

## Threadoptimierung (K2, K3, S3)

Ziel dieser Aufgabe ist es euer Spielprojekt durch die Nutzung von
Multithreading-Techniken performancetechnisch zu verbessern. Das Projekt
sollte durch die Anwendung von Multithreading eine messbare
Performanceoptimierung von circa 10% der Ausgangsperformance erfahren.
Dies ist ein Richtwert und keine feste Vorgabe! Berücksichtige bei der
Implementierung von Multithreading die Absturzrisiken.

### Abgabe
- Eine Beschreibung was genau in parallele Threads ausgelagert wurde und
  warum sind in deinem TDD zu ergänzen
- Performancedaten vor und nach der Optimierung im Vergleich

### Tipps
- Mit Threadpools kannst du die Erzeugung von Threads optimieren und
  zusätzlich Performance sparen
- Mit dem Profiler kannst du Profiling-Daten in einer externen Datei
  speichern
- Denke daran Performancedaten VOR der Optimierung zu sammeln um deine
  Maßnahmen bewerten zu können
- Analysiere welche Bestandteile des Projekts ausreichend komplex sind um
  durch Optimierung die geforderte Verbesserung zu erzielen
- achte auf Rechtschreibung und Grammatik
- die Performancedaten können gut als Bilder visualisiert werden
- absolviere die [Übung](https://canvas.sae.edu/courses/23111/pages/ubung-multithreading)
  zum Thema Multithreading

### Lernziele
- K2 — Bestimmen komplexer Programmierparadigmen
- K3 — Identifizieren von Optimierungspotenzial
- S3 — Umsetzen angemessener Optimierungsmaßnahmen

### Feedbackelemente
Proficiency:
- Wurde das Multithreading korrekt umgesetzt? Wurden häufige Probleme
  dabei bedacht?
- Wurden eventuelle Abarbeitungsreihenfolgen der Logik bedacht?

Process:
- Wurden die Absturzsicherheit und Performancekosten von Threads bedacht?
- Wurde ein merkbares Optimierungspotenzial erkannt?

Person:
- Wurden die Performancedaten übersichtlich und nachvollziehbar
  zusammengestellt?
- Ist der parallel ausgeführte Quellcode identifizierbar?
