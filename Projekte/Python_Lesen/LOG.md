# LOG.md — Chronik und Kurs-Log Python-Lesekurs

Ownership: Nur was wann passiert ist — datierte Ereignisse und die
Einheiten-Einträge des Kurses, älteste oben. Eine **Chronik**: Einträge
werden nie geändert oder gekürzt, nur ergänzt. Was als Nächstes kommt,
steht in der ROADMAP dieser Schicht; warum der Kurs so gebaut ist, in
den DECISIONS. Zeugnisse über den Kurs lesen aus dieser Datei.
Format: Ereignisse als `- JJJJ-MM-TT — Ereignis (1–3 Sätze)`.
Einheiten als
`- JJJJ-MM-TT — Einheit <Nr> · <Thema> (Snippet: Datei)` mit den Zeilen
`Selbst:` (was Isor ohne Hilfe gelesen und richtig erklärt hat),
`Hilfe:` (wo ein Hinweis oder eine Erklärung nötig war) und
`Fehler:` (Verwechslungen und Irrtümer, wörtlich genug zum Wiederfinden).
Eine leere Rubrik schreibt `—` statt wegzufallen, damit „nichts" von
„vergessen" unterscheidbar bleibt.

- 2026-08-31 — Kurs entworfen: Ziel, Einheitsformat, Log-Form und
  Themenplan festgelegt (DECISIONS und ROADMAP dieser Schicht, je
  2026-08-31). Noch keine Einheit gelaufen.
- 2026-09-01 — Einheit 1 · Grundgerüst: Variablen, Typen, print,
  f-Strings (Snippet: `Einheiten/e01_basics.py`)
  Selbst: Ausgaben im Kern richtig vorhergesagt, darunter `87 / 20` als
  `4.3` mit einer Nachkommastelle; den `if`-Zweig korrekt als
  übersprungen erkannt (87 nicht kleiner 20).
  Hilfe: Der direkte Einstieg „erklär den Code" war ohne jede Einführung
  zu viel — erst die C#-Vergleichstabelle als Brücke machte das Lesen
  möglich. Konzept des Tages erklärt: `/` liefert in Python immer eine
  Kommazahl, ganzzahlig wäre `//`.
  Fehler: Im f-String das `%` hinter dem Platzhalter übersehen
  („Battery: 87" statt „Battery: 87%") — Text außerhalb von `{ }` wird
  wörtlich ausgegeben.
