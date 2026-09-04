# ROADMAP.md — Themenplan Python-Lesekurs

Ownership: Nur was im Python-Lesekurs als Nächstes drankommt — der
Themenplan in Blöcken und die offenen Kurs-Aufgaben. Warum der Kurs so
geschnitten ist, steht in den DECISIONS dieser Schicht; was in welcher
Einheit passiert ist, im LOG.
Format: `- [ ] **Block <Nr> · Titel** — Inhalt in Stichworten`. Ein
Block ist durch, wenn Isor seine Snippets ohne Gerüst erklären kann —
abgehakt wird mit Verweis auf die belegenden LOG-Einträge.

Die Blöcke bauen aufeinander auf; das Tempo bestimmt der LOG, nicht der
Kalender. Grob gilt: ein Block je Woche bei einer Einheit pro Tag, am
Wochenende gern mehr.

## Themenplan

- [ ] **Block 1 · Grundgerüst** — Variablen ohne Typangabe, die
  Grundtypen (`int`, `float`, `str`, `bool`), `print`, f-Strings,
  Operatoren; roter Faden: was C# per Typ deklariert, macht Python zur
  Laufzeit.
- [ ] **Block 2 · Kontrollfluss** — `if`/`elif`/`else`, `for`/`while`,
  `range`, `break`/`continue`; Einrückung statt geschweifter Klammern
  als die eine große Umgewöhnung.
- [ ] **Block 3 · Datenstrukturen** — `list`, `dict`, `tuple`, `set`;
  Indexierung, Slicing, `in`, `len`; Vergleich zu `List<T>` und
  `Dictionary<K,V>`.
- [ ] **Block 4 · Funktionen** — `def`, Parameter, Default-Werte,
  Rückgaben, benannte Argumente; `*args`/`**kwargs` nur so weit, dass
  sie beim Lesen nicht erschrecken.
- [ ] **Block 5 · Idiome** — List Comprehensions, `enumerate`/`zip`,
  `with`, `try`/`except`, kleine Lambdas; die Schreibweisen, an denen
  Python-Code für C#-Augen am fremdesten aussieht.
- [ ] **Block 6 · Klassen** — `class`, `__init__`, `self`, Methoden,
  einfache Vererbung; Dunder-Methoden nur erkennen, nicht schreiben.
- [ ] **Block 7 · Module und Imports** — `import`-Varianten, die
  Standardbibliothek erkennen (`os`, `time`, `math`, `json`), das
  `if __name__ == "__main__"`-Muster.
- [ ] **Block 8 · Echte Dateien lesen** — vollständige kleine Skripte
  aus der Robotik-Nachbarschaft (Sensor-Schleife, serielle Daten,
  Auswertung) am Stück zusammenfassen: was tut die Datei, wo würde man
  suchen, wenn etwas klemmt.

## Aufgaben

- [ ] **Einheit 1 bauen** — erstes Snippet unter `Einheiten/` anlegen
  (Dateien und Code auf Englisch, `Kern/DOC_RULES.md`, Abschnitt 9) und
  die erste Einheit durchlaufen.
- [ ] **Zwischen-Zeugnis nach Block 4** — erstes `/harness:zeugnis` über
  den Kurs, gelesen aus dem LOG dieser Schicht; danach entscheiden, ob
  Tempo und Zuschnitt der Blöcke 5–8 so bleiben.
