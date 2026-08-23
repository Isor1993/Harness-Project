# VERSIONIERUNG.md — Was welche Nummer bedeutet

Ownership: Alle Nummernsysteme des Projekts — welche Nummer was zählt,
wie sie gelesen wird und wo sie steht. Besitzt **nicht** die Nummern
selbst: Die Commit-Nummer steht im Commit-Titel, die Spiel-Version in den
Unity Player Settings, die Harness-Version in CLAUDE.md.

Warum eigene Datei: Es gibt drei Nummern nebeneinander, die
Verschiedenes zählen. Ohne eine Stelle, an der die Lesarten stehen, hält
man sie früher oder später für dasselbe.

## Die Nummern auf einen Blick

| Nummer | Zählt | Beantwortet | Steht in |
|---|---|---|---|
| `V 0.0035` | Änderungen, fortlaufend | *Welche Sitzung war das?* | Commit-Titel |
| `0.0.3` | Reifegrad des Spiels | *Wie weit ist das Spiel?* | Unity Player Settings |
| `1.0.0` | Verträglichkeit des Harness | *Muss ein Projekt umziehen?* | CLAUDE.md |

Alle drei sehen aus wie `X.Y.Z` — **gelesen werden sie verschieden.**
Deshalb nie „Version" sagen, ohne dazuzusagen, welche.

---

## 1. Commit-Nummer — `Update V 0.0035`

**Keine Version.** Eine laufende Nummer, die Sitzungen zählt, vierstellig
hochgezählt. Sie sagt nichts über Inhalt oder Reifegrad.

- Je Repo eine eigene Zählung.
- Die nächste Nummer wird per `git log` nachgeschlagen, nicht geschätzt.
- Format und Ablauf regelt WORKFLOW.md.

## 2. Spiel-Version — Reifegrad

Grundentscheidung: DECISIONS 2026-08-16 („Versionsschema nach
Reifegrad"). Semantic Versioning wurde dort ausdrücklich verworfen, weil
„neue Funktion" oder „Fehlerbehebung" nichts darüber sagt, wie weit das
Spiel ist.

**Vor dem Release** — die vordere Stelle sagt den Reifegrad:

| Form | Bedeutung |
|---|---|
| `0.0.x` | Prototyp — `x` zählt die Stände hoch |
| `0.x.0` | Early Access |
| `1.x.x` | fertiges Spiel |

Solange vorne `0` steht, ist das Spiel nicht fertig; solange die mittlere
Stelle `0` ist, nicht einmal Early Access.

**Nach dem Release** — die Reifegrad-Frage ist beantwortet, also wechselt
die interessante Information. Ab `1.x.x` gilt:

| Stelle | Bedeutung |
|---|---|
| `Y` | neue Inhalte |
| `Z` | Fehlerbehebung, kein neuer Inhalt |

*Ergänzt die Entscheidung vom 2026-08-16, ohne sie umzustoßen: Das
Schema war für alles vor dem Release präzise und ließ die Zeit danach
offen (Isor, 2026-08-22).*

## 3. Harness-Version — Verträglichkeit

Die Frage ist hier nicht Reifegrad, sondern: **Was bedeutet ein neuer
Stand für ein Projekt, das den Harness schon benutzt?**

| Stelle | Ändert sich | Folge für ein bestehendes Projekt |
|---|---|---|
| `X` | Struktur — Schichten, Dokumentarten, Befehle | **muss umziehen** |
| `Y` | Regeln kommen dazu oder ändern sich | kann mitziehen, muss nicht |
| `Z` | Korrekturen, Formulierungen | nichts zu tun |

Steht in **CLAUDE.md**, eine Zeile, weil die Datei bei jedem
Session-Start gelesen wird — damit ist immer klar, mit welcher Fassung
gearbeitet wird.

Erster durchdachter Gesamtstand: **1.0.0** (Überholung vom 2026-08-21/22).

---

## Die Kern-Auslieferung

Ein Git-Stand enthält immer den **ganzen** Harness — Uni-Schicht,
Projekt-Schicht, den Entscheidungs-Altbestand. Zum Mitnehmen in ein neues
Projekt wird aber nur der **Kern** gebraucht.

Deshalb wird je Hauptversion eine Auslieferung abgelegt:
`C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\Harness_1.0.0\`

- Inhalt: nur `Kern/` plus die Datei mit der Leseordnung. Keine Uni, kein
  Projekt, keine Altbestände. `Kern/` enthält damit auch `Werkzeuge/` und
  `Befehle/` — beides gehört zum Harness und wäre ohne die Auslieferung
  nicht mitzunehmen.
- **Eine Auslieferung ist eine Vorlage, keine Kopie** (Isor, 2026-08-23).
  Was unter `Kern/` liegt, aber nur Isor betrifft, wird beim Packen
  entfernt: die Zeugnisse, die Einträge im `ARTIFACT_INDEX.md` (Kopf und
  Feldliste bleiben als Muster) und die Zeilen in `index_geplant.txt`.
  Wer den Harness in ein neues Projekt kopiert, bekommt ein leeres Regal
  statt fremder Sachen darin. `LOG.md`, `DECISIONS.md` und `_ARCHIV.md`
  bleiben dagegen drin — sie erklären, **warum** die Regeln so aussehen,
  und ohne sie steht der Kern ohne Begründung da.
- **Drei Handgriffe beim Einrichten** — mehr verlangt die Auslieferung
  über das Entpacken hinaus nicht:
  1. `Kern/Befehle/*.md` nach `.claude\commands\harness\` kopieren, sonst
     gibt es die Befehle im neuen Projekt nicht (`WORKFLOW.md` → „Wo die
     Auslöser liegen").
  2. `PLAN.md` neben `CLAUDE.md` anlegen — leer, nur mit Kopf und dem
     Abschnitt „Für die nächste Session". Die Leseordnung nennt die
     Datei; ohne sie zeigt sie ins Leere.
  3. `python Kern/Werkzeuge/index_bauen.py --write` laufen lassen. Der
     `INDEX.md` wird erzeugt, nicht mitgeliefert — eine mitgelieferte
     Fassung wäre ab dem ersten neuen Dokument falsch.
  *(Punkte 2 und 3 kamen beim Packen von 1.0.0 dazu: Der Probelauf in
  der fertigen Auslieferung zeigte, dass die Leseordnung auf zwei
  Dateien zeigte, die es dort nicht gibt.)*
- **Das ist kein Backup.** Zum Zurückholen alter Stände dient Git; die
  Auslieferung ist eine fertige Ausgabe zum Kopieren.
- Angelegt wird sie bei jeder Änderung von `X` oder `Y`, nicht bei `Z`.
- Eine abgelegte Auslieferung wird **nie bearbeitet**. Wer darin etwas
  ändern will, ändert den Harness und legt eine neue ab.
