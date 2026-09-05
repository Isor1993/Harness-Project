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

## 1. Commit-Nummer, im Gespräch „V-Nummer" — `Update V 0.0035`

**Keine Version.** Eine laufende Nummer, die Sitzungen zählt, vierstellig
hochgezählt. Sie sagt nichts über Inhalt oder Reifegrad.

- Je Repo eine eigene Zählung.
- Die nächste Nummer wird per `git log` nachgeschlagen, nicht geschätzt.
- Format und Ablauf regelt WORKFLOW.md.
- **Sie zählt Sessions, nicht jeden Commit:** Der Commit-Vorschlag bei
  `/harness:ende` trägt sie. Zwischenstände, die Isor von Hand sichert,
  tragen freie Titel und zählen nicht hoch. *(Klarstellung 2026-08-26;
  Begründung in `Kern/DECISIONS.md`.)*

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

### Ablage der Builds

Ein gebauter Stand liegt im Datenbaum unter
`02_Projekte\<Projekt>\Builds\<Spielversion>_<JJJJ-MM-TT>\`
(`Kern/PFADE.md` → `DATENBAUM`) — das Repo ignoriert `Build/` zu Recht.
Die Spielversion kommt aus den Player Settings; das Datum unterscheidet
zwei Stände derselben Prototyp-Version. *(Entschieden 2026-08-26,
Begründung in `Kern/DECISIONS.md`.)*

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

Deshalb wird je Hauptversion eine Auslieferung abgelegt, im Datenbaum
unter `05_Werkzeuge\Harness_Auslieferungen\Harness_<Version>\`
(`Kern/PFADE.md` → `DATENBAUM`).

- Inhalt: nur `Kern/` plus die Datei mit der Leseordnung. Keine Uni, kein
  Projekt, keine Altbestände. `Kern/` enthält damit auch `Werkzeuge/`,
  `Befehle/`, `Vorlagen/` und `Bilder/` — alles gehört zum Harness und
  wäre ohne die Auslieferung nicht mitzunehmen.
- **Eine Auslieferung ist eine Vorlage, keine Kopie** (Isor, 2026-08-23).
  Wer den Harness in ein neues Projekt kopiert, bekommt ein leeres Regal
  statt fremder Sachen darin.
- **Dieses Repo bleibt davon unberührt.** Gepackt wird in den Datenbaum;
  die Originale hier behalten ihren vollen Inhalt. Was die Packliste
  „leert", leert sie in der Kopie. *(Ausdrücklich hingeschrieben am
  2026-08-27, weil die Frage beim Neufassen der Packliste aufkam.)*

### Die Packliste

Welche Datei wie behandelt wird, steht **hier** und wird nicht je
Auslieferung neu entschieden (Isor, 2026-08-24). Grund: Die Frage stellte
sich beim Packen von 2.0.0 zum zweiten Mal, und beide Male anders
beantwortet zu haben wäre schlimmer als jede der beiden Antworten.

**Neu gefasst am 2026-08-27 (Isor): eine Auslieferung trägt keine fremde
Geschichte.** Bis dahin gingen die Chroniken vollständig mit, damit die
Regeln ihre Begründung dabeihaben. Der Preis dafür war ein neues Projekt,
das ab dem ersten Blick Isors Entscheidungen, Störungen und Bauschritte
vor sich hat — Altbestand, den dort niemand lesen will und niemand pflegt.
Begründung samt verworfener Wege in `Kern/DECISIONS.md`.

| Behandlung | Dateien | Warum |
|---|---|---|
| **bleibt vollständig** | alle Regeldateien — `CLAUDE.md`, `WORKFLOW.md`, `DOC_RULES.md`, `CODE_GUIDELINES.md`, `VERSIONIERUNG.md`, `GLOSSARY.md` und die übrigen · `Werkzeuge/` · `Befehle/` · `Vorlagen/` · `Bilder/` | Das **ist** der Harness. Eine Regel ohne ihren Wortlaut ist keine. |
| **Kopf plus ein Musterbeispiel** | `LOG.md` · `DECISIONS.md` · `STOERUNGEN.md` · `_ARCHIV.md` · `ROADMAP.md` · `ARTIFACT_INDEX.md` | Titelzeile, `Ownership:`, `Format:` und **genau ein** Eintrag, erkennbar als Beispiel gekennzeichnet. Ganz leer wäre die Form nicht ablesbar, und die Formatzeile allein hat sich als zu wenig erwiesen; voll wäre es fremde Geschichte. |
| **auf den Kopf geleert** | `index_geplant.txt` (Kommentarkopf) · `PFADE.md` (Marken und Zweck bleiben, Pfad-Spalte auf `(nicht eingerichtet)`) | Reine Bestandslisten ohne Eintragsformat. Hier gibt es nichts vorzumachen — die Tabelle selbst ist schon das Muster. |
| **fällt ganz weg** | `Kern/Zeugnisse/` · `LERNLOG.md` | Bewerten und beschreiben eine Person, nicht den Harness. |

Neue Datei im Kern? Dann gehört sie beim Anlegen in eine dieser Zeilen —
nicht erst beim nächsten Packen.

### Gepackt wird per Skript

`Kern/Werkzeuge/ausliefern.py` setzt die Tabelle oben um. Ohne Schalter
ist es ein **Trockenlauf**, der nur meldet; `--schreiben` legt die
Auslieferung wirklich an. Eine schon vorhandene Auslieferung rührt es
nicht an, sondern bricht ab — eine abgelegte wird nie bearbeitet (unten).

Warum als Skript: Die Packliste sagt, dass sie nicht je Auslieferung neu
entschieden wird. Von Hand gepackt wurde sie beide bisherigen Male
verschieden ausgelegt; ein Skript legt sie jedes Mal gleich aus. Dieselbe
Bauart wie beim INDEX — erzeugen statt pflegen (`Kern/DOC_RULES.md`,
Abschnitt 5).

**Ein Absatz, der nur dieses Projekt betrifft, wird in der Quelle
eingeklammert:**

    <!-- nicht ausliefern -->
    *Für dieses Projekt:* … was hier geschah, mit Datum …
    <!-- /nicht ausliefern -->

Beim Packen fällt er weg. Das ist der Weg, wie ein Kopf-Absatz zugleich
die Regel begründen und die eigene Geschichte erzählen kann, ohne dass
Letztere mitreist — und wie die Auslieferung ohne Nachbearbeitung von
Hand entsteht. Das Skript meldet am Ende jede geschnittene Datei, deren
Kopf noch ein konkretes Datum trägt; steht die Liste leer, ist nichts
mehr nachzusehen. Der Name „Isor" gilt dabei **nicht** als Altbestand —
er steht in jeder Regeldatei als Rolle.

**Was die gekürzten Chroniken kosten:** Regelsätze der Form „Begründung in
`Kern/DECISIONS.md`" zeigen in einer Auslieferung auf ein Musterbeispiel
statt auf die echte Entscheidung. Der Zeiger bleibt richtig — die Datei
gibt es, und im neuen Projekt füllt sie sich mit den eigenen
Entscheidungen. Wer die ursprüngliche Begründung sucht, findet sie im
öffentlichen Harness-Repo; dass es öffentlich bleibt, ist genau dafür
entschieden (`Kern/DECISIONS.md` → „Sichtbarkeit und Zugang der Repos").
Kein Werkzeug prüft das nach: `pruefen.py` sieht, ob eine Datei existiert,
nicht ob der Satz darin steht.

### Das Einrichten

**Ein Befehl statt einer Handgriff-Liste:** `/harness:einrichten` im
neuen Projekt aufrufen. Er fragt die Pfade ab und führt aus, was früher von
Hand zu tun war — Befehle in die Arbeitskopie, `PLAN.md` anlegen, INDEX
erzeugen, Hook eintragen. Was er im Einzelnen tut, steht in
`WORKFLOW.md` → „Ablauf von `/harness:einrichten`"; wie jeder Befehl
trägt die Auslöserdatei selbst keinen Ablauf.

*(Bis 2.0.0 standen die Schritte hier als Liste zum Abarbeiten. Zwei
davon kamen erst durch den Probelauf in der fertigen Auslieferung dazu,
ein dritter mit dem `SessionStart`-Hook — eine Liste, die man von Hand
abarbeitet, wächst und wird dabei unvollständiger. Seit 2.0.0 führt der
Befehl sie aus, siehe `Kern/DECISIONS.md`, 2026-08-24.)*
- **Das ist kein Backup.** Zum Zurückholen alter Stände dient Git; die
  Auslieferung ist eine fertige Ausgabe zum Kopieren.
- Angelegt wird sie bei jeder Änderung von `X` oder `Y`, nicht bei `Z`.
- Eine abgelegte Auslieferung wird **nie bearbeitet**. Wer darin etwas
  ändern will, ändert den Harness und legt eine neue ab.
