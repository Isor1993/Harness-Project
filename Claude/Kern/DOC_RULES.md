# DOC_RULES.md — Regeln über die Dokumente des Harness

Ownership: Alle Regeln, die für die .md-Dateien des Harness selbst
gelten — Zuständigkeit, Aufbau, Verweise, Verfall, Sprache. Nicht
geregelt werden hier äußere Erzeugnisse; dafür gibt es KNOWLEDGE_RULES,
ARTIFACT_RULES, DIAGRAM_RULES, DOCX_RULES, GDD_RULES und ASSESSMENT_RULES.

Wann zu lesen: vor dem Anlegen oder Ändern eines Dokuments (CLAUDE.md
verweist darauf). Diese Datei steht bewusst **nicht** in der Leseordnung
— sie ist Nachschlagewerk, nicht Startgepäck.

---

## 1. Ownership — der Kern

**Für jede Information gibt es genau ein Dokument, das sie besitzt. Alle
anderen dürfen darauf verweisen, sie aber nicht wiederholen.**

Der Schaden, den die Regel verhindert, ist nicht die Doppelung selbst.
Er entsteht danach: Steht dieselbe Tatsache an drei Stellen und wird an
einer geändert, behaupten die Dokumente Verschiedenes — und alle drei
sehen gleich glaubwürdig aus. Der Fehler fällt nicht beim Lesen auf,
sondern erst, wenn nach der falschen Fassung gehandelt wurde.

**Ownership schneidet nach der *Art* der Information, nicht nach dem
*Thema*.** Fünf Dokumente dürfen vom Terrain handeln, solange jedes eine
andere Art besitzt:

| Frage | Art | Besitzer |
|---|---|---|
| Wann wurde es gebaut? | Ereignis | LOG |
| Warum so und nicht anders? | Begründung | DECISIONS |
| Was kommt danach? | Plan | ROADMAP |
| Wie heißen die Felder? | Regel | CODE_GUIDELINES |
| Was soll sich anfühlen? | Absicht | GDD |

### Die Prüfungen
1. **Ein-Ort-Test** — Ändert sich die Tatsache: an wie vielen Stellen
   muss ich sie ändern? Die Antwort muss „an einer" sein.
2. **Widerspruchs-Test** — Können zwei Dateien darüber Verschiedenes
   behaupten? Dann ist die Zuständigkeit unklar.
3. **Verweis statt Kopie** — Braucht Datei B die Information, schreibt
   sie „siehe A", nicht die Information selbst. Diese Prüfung wird am
   häufigsten gebrochen, weil Kopieren im Moment bequemer ist.

### Wer gerade was besitzt
Steht **nicht hier**, sondern in der `Ownership:`-Zeile jeder Datei — und
gesammelt im erzeugten INDEX.md. Diese Datei besitzt das *Verfahren*, der
INDEX das *Ergebnis*. Eine Tabelle beider Zuordnungen hier wäre genau die
Kopie, die Regel 1 verbietet.

### Wenn mehrere Dateien dieselbe Art besitzen
Die Tabelle oben trennt nach Art. Sobald eine Art auf mehrere Dateien
aufgeteilt wird — sieben `DECISIONS/`-Dateien eines Projekts —, ist das
Thema wieder die Grenze, und damit Geschmackssache. Gehört der
Wasserspiegel zu „Terrain" oder zu „Welt"?

> **Eine Entscheidung gehört der Datei, deren Code sie ändert** — nicht
> der, über deren Thema sie redet.

Das ist prüfbar statt strittig: Der Wasserspiegel wird vom Terrain-Tool
gebaut, also Terrain. Zusätzlich trägt **jede** Geschwisterdatei eine
Zeile `Nicht hier:` mit dem Nachbarn, der den Grenzfall bekommt — sonst
lebt die Zuordnung nur im Kopf dessen, der sie einmal getroffen hat.

### Vor einem Befund
Immer **alle beteiligten Dateien** lesen, bevor geurteilt wird — bei
einem Ownership-Befund mindestens die `Ownership:`-Zeile jeder von ihnen.
Ein Widerspruch liegt zwischen zwei Dateien; wer nur eine liest, hält ihn
für einen Verstoß dieser einen.

**Das gilt für jede Art von Befund, nicht nur für Ownership**, und
ausdrücklich über Schichtgrenzen hinweg. *(Zwei echte Fehlurteile:
2026-08-21 zwischen ROADMAP und FEATURE_LOG, und 2026-08-22 — eine
Bauliste behauptete etwas als erledigt, was die ROADMAP einer anderen
Schicht als offen führte. Beide in `STOERUNGEN.md`.)*

---

## 2. Wann ein Dokument berechtigt ist

**Ein Dokument ist gerechtfertigt, wenn sich eine Frage nennen lässt, die
es beantwortet und die sonst kein anderes Dokument beantwortet.**

Fällt keine ein, ist es eins zu viel. Fällt eine ein, die heute
unbeantwortet bleibt, fehlt eines.

---

## 3. Aufbau jeder Datei

1. `# DATEINAME.md — Kurztitel`
2. `Ownership:` — **Pflicht in jeder Datei.** Ein bis drei Sätze: was sie
   besitzt, und ausdrücklich, was sie *nicht* besitzt.
3. `Format:` — überall dort, wo Einträge einem Muster folgen. Ohne
   Formatvorgabe entstehen flache, ungegliederte Listen.
4. Inhalt.

Die `Ownership:`-Zeile ist zugleich die Quelle des erzeugten INDEX.
Eine Datei ohne sie erscheint dort als `⚠`.

---

## 4. Was eine Datei kostet

> **Kosten = Größe × Lesehäufigkeit.**

Eine **Arbeitsdatei** wird oft gelesen; jede überflüssige Zeile kostet
dauerhaft. Sie muss kurz gehalten werden.
Ein **Archiv** wird selten gelesen; seine Größe ist fast folgenlos.

### Chronik gegen Verzeichnis
- Eine **Chronik** beantwortet „was ist wann passiert". Sie wird nur
  ergänzt, nie geändert, und **kann nie falsch werden**. Kein Archiv,
  keine Pflege.
  **Ergänzt wird nach Datum, nicht hinten angehängt.** Für das Heutige
  ist beides dasselbe; für einen **nachgetragenen** Eintrag nicht — etwa
  beim Auflösen einer Erledigt-Liste. Wird er ans Ende gehängt,
  behauptet die Chronik eine Zeitfolge, die sie nicht hat, und der
  falsche Eintrag steht ausgerechnet an der Stelle, die am seltensten
  gegengelesen wird. *(Regel aus drei echten Fällen, 2026-08-22.)*
  Ein Eintrag darf durchaus einen Ablageort nennen — er trägt sein Datum
  und sagt damit, wo etwas **damals** lag; das ist beim Nachvollziehen
  oft der Schlüssel. Die Chronik verspricht nur nicht, dass es dort
  **heute** noch liegt. Der aktuelle Ort kommt aus dem Code bzw. aus der
  erzeugten Systemliste.
- Ein **Verzeichnis** beantwortet „was existiert jetzt und wo". Es muss
  laufend abgeglichen werden, sonst führt es in die Irre.

Ein Dokument, das der Form nach Chronik und dem Inhalt nach Verzeichnis
ist, hat die Nachteile von beidem.

### Archive
Werden **nie aufgeräumt** — siehe Kostenformel. Genau eine Pflicht:
**Jeder Archiv-Eintrag nennt, wodurch er abgelöst wurde; jeder neue
Eintrag nennt, welchen er ablöst.** Ohne diese Zeile ist ein Archiv ein
Friedhof, in dem man nichts wiederfindet.

---

## 5. Erzeugen statt pflegen

Beschreibt ein Dokument etwas, das anderswo schon steht, ist es eine
zweite Fassung der Wahrheit. Statt es zu pflegen, lässt man es aus der
Quelle **erzeugen**.

**Arbeitsteilung:** Das Skript besitzt die *Liste* (Vollständigkeit
garantiert), der Mensch besitzt die *Beschreibung*. Bestehende
Beschreibungen werden bei Neuerzeugung über ihren Schlüssel übernommen;
Neues ohne Beschreibung erscheint als `⚠ fehlt`, Verschwundenes als
`⚠ nicht mehr vorhanden`.

**Warum das trägt:** Ein von Hand gepflegtes Verzeichnis merkt nie, dass
etwas Neues existiert. Es zeigt nur, was jemand hineingeschrieben hat.
Erzeugen dreht das um.

**Wann es sich *nicht* lohnt:** Wenn die Liste nur wiederholt, was das
Dateisystem ohnehin zeigt. Erst wenn sie *Bedeutung* trägt — was ein
Eintrag ist, wozu er da ist —, verdient sie ihren Platz.

**Dieselbe Bauform ist nicht überall gleich riskant.** Eine Liste
verfällt so schnell, wie ihr Gegenstand sich ändert: Themenordner in
Stunden, Werkzeuge in Monaten nicht. Die Frage ist nie „ist das eine
Liste", sondern „wie schnell ändert sich, was sie beschreibt".

**Erst Ownership klären, dann automatisieren.** Ein Skript, das eine
überflüssige Kopie pflegt, macht die Kopie nicht richtig — nur pünktlich.

---

## 6. Verweise

**Nur über Namen, nie über Positionen.** „Punkt 10" bezeichnet eine
Stelle in einer Liste; wird oben etwas eingefügt, bedeutet Punkt 10
etwas anderes — und nichts meldet sich.

> **Sichtbar kaputt ist besser als still falsch.**

**Eine Ausnahme:** Steht die Nummer in der **Überschrift** des Ziels
(`## 8. Grenzfälle, in denen Ownership anders ausgeht`), ist sie Teil des
Namens und darf zitiert werden — sie wird dann nie neu vergeben.
Nummerierte Listen **ohne** Überschrift bekommen stattdessen Kurznamen,
und verwiesen wird auf den Namen: nicht „Bedienregel 5", sondern
„Bedienregel *Freies Ende bleibt frei*".

**Format:** Pfad **und** Überschrift —
`Projekte/Isor_Tower/ROADMAP.md → „Prefab-Struktur prüfen"`.

**Gleiche Dateinamen je Schicht sind gewollt.** Es gibt mehrere
`ROADMAP.md`, `LOG.md` und `_ARCHIV.md` — der Ordner unterscheidet sie.
Kein Umbenennen zu `ROADMAP_Uni.md`: Eine Schicht soll ein kopierbarer
Ordner bleiben.

Dafür gilt eine Sprachregel — **sie bindet Claude, nicht Isor.** Claude
nennt in Text und Gespräch immer die Schicht („die Uni-Roadmap"). Sagt
Isor bloß „die Roadmap", erschließt Claude sie aus dem Zusammenhang und
fragt nur nach, wenn es wirklich mehrdeutig ist. Grund: Isor diktiert per
Spracheingabe; eine Sprechregel wäre dort Reibung ohne Gewinn.

---

## 7. Verfall vermeiden

- **Keine Anzahl in Überschrift oder Einleitung**, wenn die Liste wachsen
  kann. Nicht „Die drei Typen", sondern „Die Typen".
  **Erlaubt ist eine Anzahl nur, wenn die Aufzählung abgeschlossen ist**
  und der Text sagt, warum nichts dazukommen kann. Dann trägt die Zahl
  Information statt eines Verfallsdatums.
- **Stand-Stempel nur, wo etwas ihn kontrolliert.**
  - In **erzeugten** Dateien setzt ihn das Skript — er kann nicht falsch
    werden.
  - In **handgeschriebenen** Dateien ist er nur erlaubt, wenn eine
    Prüfung ihn abgleicht (bei den Artifact-Seiten der Sonntagsabgleich
    gegen die Veröffentlichungsliste). Gibt es keine Prüfung, wird kein
    Datum hingeschrieben.
  *Beleg:* Von vier vorgefundenen Stempeln waren drei falsch — genau die
  drei ohne Prüfung.
- **Statusvermerke** („in Arbeit", „ungetestet") gehören zu der Datei,
  die den Gegenstand besitzt, nicht in eine zweite.

---

## 8. Grenzfälle, in denen Ownership anders ausgeht

**Eine Checkliste gehört dem Moment, nicht den Themen.** Wird eine Liste
an einem Zeitpunkt am Stück abgearbeitet, besitzt sie alle ihre Punkte —
auch die, die thematisch woandershin gehörten. Eine Liste, deren fünf
Punkte auf fünf Dateien zeigen, ist keine Checkliste mehr. Die
Themendateien verweisen auf die Liste, nicht umgekehrt.

**Ein Register muss vollständig sein.** Ein Verzeichnis fremder Adressen
— veröffentlichte Seiten, externe IDs — wird nicht nach Schichten
zerschnitten. Seine Zusage lautet „es gibt keine zweite Stelle zum selben
Gegenstand", und die kann nur eine ungeteilte Liste geben.

**Eine offene Frage hat genau einen Besitzer.** Design-Fragen gehören dem
GDD, technische der DECISIONS-Datei der Schicht. Die ROADMAP verweist nur
als Aufgabe. DECISIONS bekommt einen Eintrag erst, wenn die Frage
**beantwortet** ist — dann streicht der Besitzer sie aus seiner
Offen-Liste.

**Eine Ausnahme muss sich selbst als Ausnahme benennen** und ihre
Begründung mittragen. Sonst ist sie von Unordnung nicht zu unterscheiden.

---

## 9. Sprache

| Erzeugnis | Sprache |
|---|---|
| Code, Bezeichner, Ordnernamen | Englisch |
| Kommentare im Code | Englisch oder Deutsch, aber einheitlich |
| Commit-Titel und -Beschreibung | Englisch |
| Harness-Dokumente (diese .md-Dateien) | Deutsch |
| Knowledge-Seiten | Deutsch |
| Zeugnisse | Deutsch (Ausnahme: Dateinamen, Code, Zitate daraus) |
| Unterhaltung | Deutsch |

Diese Tabelle ist der Besitzer. Wo die Sprache anderswo erwähnt wird
(CODE_GUIDELINES, WORKFLOW, ASSESSMENT_RULES), steht dort nur ein Verweis.

---

## 10. Schichten

Der Harness ist in Schichten geteilt, jede ein eigener Ordner, damit sie
sich als Ganzes herausnehmen lässt:

| Schicht | Inhalt |
|---|---|
| `Kern/` | generisch, wandert in jedes Projekt mit |
| `Uni/` | studienspezifisch, nach Semestern gegliedert |
| `IsorBackup/` | Regeln für den externen Datenbaum |
| `Projekte/<Name>/` | **eine Schicht je Projekt** |

**`Projekte/` ist keine Schicht, sondern ein Sammelordner.** Schicht ist
jeweils `Projekte/<Name>/`. Alles, was für eine Schicht gilt — eigene
ROADMAP, LOG, DECISIONS, `_ARCHIV`, herausnehmbar als Ganzes —, gilt dort
**je Projekt**. Bei zwei Projekten sind es also fünf Ordner, nicht vier.

**Schicht = Thema. Dokumentart = Art der Information.** Das Kreuz aus
beidem ergibt das Fach, in dem eine Information genau einmal liegt.

Liegt eine Datei überwiegend im Kern, aber mit wenigen
schichtspezifischen Teilen, wird sie **nicht zerschnitten**: Sie bleibt
im Kern und benennt, dass der Maßstab aus der aktiven Schicht kommt.
