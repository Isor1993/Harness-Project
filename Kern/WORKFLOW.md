# WORKFLOW.md — Session-Disziplin

Ownership: Wie eine Session abläuft — Begriffe, Typ und Modus samt
Reglern, Session-Typen, Doku-Pflicht, die Befehle, der Pflegetag und das
Session-Ende.
Regeln über Dokumente stehen in `DOC_RULES.md`, Code-Regeln in
`CODE_GUIDELINES.md`, Nummernsysteme in `VERSIONIERUNG.md`.

## Begriffe

- **Session** — ein durchgehender Arbeitsraum von Anfang bis `/clear`.
  Isors Wort dafür ist „Work Area".
- **Abschnitt** — eine Phase innerhalb einer Session mit genau **einem**
  Typ. `/harness:wechsel` beendet einen Abschnitt und öffnet den nächsten.
- **Baustein** — eine abgeschlossene Funktionseinheit, die sich in einem
  Zug entwerfen und bauen lässt. **Fertig heißt gebaut, geprüft *und*
  dokumentiert** — solange der zugehörige Abschnitt im Abgabetext fehlt,
  ist der Baustein nicht fertig.
- **Befund** — Ergebnis einer Prüfung: eine Stelle, an der etwas falsch,
  doppelt, widersprüchlich ist oder fehlt. Entsteht beim gezielten
  Hinsehen (Abnahme, Review-Gate, Prüfstand, Sonntagsabgleich) und wird
  **notiert, nicht sofort geändert**.

**Befund gegen Störung:** Ein **Befund ist ein Zustand**, eine
**Störung ein Ereignis** (`STOERUNGEN.md`). Ein Befund kann eine Störung
nach sich ziehen — dann nämlich, wenn er zeigt, dass eine Regel nicht
gegriffen hat —, aber die meisten tun das nicht. Ein fehlender Ordner
ist ein Befund; dass niemand das Fehlen bemerkt hat, wäre die Störung.

Jeder **Abschnitt** hat genau einen Typ und einen Fokus. Eine **Session**
kann mehrere Abschnitte enthalten. Höchstens 2–4 Sessions parallel offen
— wer dabei wohin schreiben darf, regelt „Parallele Sessions" unten.

## Typ, Modus und Regler

**Am Anfang jeder Session fragt Claude nach Typ und Modus** — bei jedem
Typ, nicht nur beim Entwerfen. Beide gehören zusammen und hängen am
Abschnitt, nicht an der Session: Der **Typ** entscheidet, welche Dateien
die Doku-Pflicht am Ende schreibt, der **Modus**, wie dazwischen
gearbeitet wird. Die Typen stehen unten unter „Session-Typen".

Wird der Typ nicht gefragt, fällt es erst bei `/harness:sichern` auf —
dann steht die Doku-Pflicht ohne ihren Maßstab da.
*(Regel aus einem echten Aussetzer, 2026-08-22.)*

### Der Typ steht im Session-Titel

Damit sichtbar ist, worin man gerade steckt, trägt der Session-Titel den
laufenden Abschnitt — im Schema `<Thema> (<Typ>)`:

    Harness 1.0.0 (Prüfung)
    Harness 1.0.0 (Development · Normal)
    Isor's Tower · Platzierung (Design)

**Der Modus steht nur dann dabei, wenn er vom Lernmodus abweicht.** Der
Normalfall schweigt; so sagt die Klammer etwas, wenn sie etwas sagt.

**Arbeitsteilung:** Das **Thema gehört Isor** — er benennt die Session,
und Claude ändert daran kein Wort. Die **Klammer gehört Claude**: Er
setzt sie beim ersten Typ und schreibt sie bei jedem Wechsel um. Fehlt
eine Klammer, hängt er sie an, ohne den Rest anzufassen.

**Der geerbte Titel** *(seit 2026-08-26)*: Eine frische Session kann den
Titel der vorigen tragen, samt deren Klammer `zu`. Das ist **kein Thema,
das Isor für diese Session gesetzt hat** — aber auch keine Erlaubnis,
eines zu erfinden. Claude **schlägt** dann ein Thema vor und setzt den
Titel erst nach Isors Zustimmung; die Klammer darf er sofort richtig
stellen. Grund: Genau hier ist am 2026-08-26 ein Thema überschrieben
worden, weil `zu` als „gilt nicht mehr" gelesen wurde und die Regel den
Fall nicht kannte (`STOERUNGEN.md`, „Session-Thema überschrieben,
Wiederholungsfall").

**Der Titel ist Anzeige, kein Beleg.** Er lebt in der App, nicht im Repo,
und trägt immer nur den *letzten* Abschnitt — was eine Session
tatsächlich getan hat, steht im LOG der Schicht. Aus einem Titel wird
kein Befund abgeleitet. *(Genau das ist am 2026-08-23 passiert:
`STOERUNGEN.md` → „Aus dem Session-Titel auf den Typ geschlossen".)*

#### Was in der Klammer stehen kann

Drei Sorten, mehr nicht — die Aufzählung ist abgeschlossen, weil die
Klammer nur einen von drei Lebenszuständen anzeigt:

| Klammer | heißt |
|---|---|
| ein **Typ** | hier wird gerade gearbeitet |
| **zu** | mit `/harness:ende` abgeschlossen, `/clear` folgt |
| **aufgehoben** | absichtlich offen gelassen, damit etwas darin erhalten bleibt — nicht vergessen, nicht in Arbeit |

Gesetzt wird an drei Punkten: **am Anfang**, sobald Typ und Fokus
feststehen (nicht früher — vorher weiß niemand, was in die Klammer
gehört) · **bei jedem `/harness:wechsel`** · **bei `/harness:ende`** auf
`zu`. `aufgehoben` setzt Claude nur auf Zuruf.

**Bekannte Grenze:** Bei `/clear` kann Claude nichts mehr setzen — der
Befehl leert den Kontext, ohne ihn noch einmal aufzurufen. Deshalb sitzt
der Handgriff bei `/harness:ende`, dem letzten Moment davor. Wer `/clear`
ohne `/harness:ende` tippt, lässt einen Titel stehen, der Arbeit
behauptet. Das ist nicht abzufangen und deshalb hier benannt.

Das Umbenennen ist **Schritt des Wechsels**, keine Regel zum Erinnern —
siehe „Ablauf von `/harness:wechsel`". Grund: Ein falscher Titel ist
schlimmer als gar keiner, weil er so verbindlich aussieht wie ein
richtiger.

| Modus | bedeutet |
|---|---|
| **Lernmodus** | ausführlich erklären, visuell arbeiten, Verständnis prüfen, Erkenntnisse ins Knowledge. Isors Normalfall. |
| **Normal** | kurz und bündig. |

Der Modus setzt die Voreinstellungen. Zwei Regler lassen sich einzeln
überschreiben, ohne den Modus zu wechseln („Lernmodus, aber wenig Bilder"):

| Regler | Stufen | Lernmodus | Normal |
|---|---|---|---|
| **Visualisierung** | viel · wenig · keine | viel | wenig |
| **Wer schreibt** *(nur Development)* | Isor · Claude | Isor | Claude |

Die Erklärtiefe hat bewusst **keinen** eigenen Regler — sie bewegt sich
nie allein. Heruntergedreht wird bei knappem Nutzungslimit der Bildanteil.

### Zeigen statt vorstellen lassen
- **Nie** „stell dir vor" oder etwas, das ein inneres Bild verlangt.
- **Gern** Diagramme, Skizzen, Artifact-Seiten, Screenshots — ansehbar.
- **Dazu** Zahlen und Tabellen, weil sie unabhängig vom Bild tragen.

**Untergrenze des Visualisierungs-Reglers:** Auch bei „wenig" oder
„keine" wird nie auf inneres Vorstellen ausgewichen. Was sonst ein
Diagramm gezeigt hätte, wird über Zahlen und Tabellen erklärt — länger,
aber nie über „stell dir vor". Der Regler steuert den **Aufwand** der
Darstellung, nicht ob Isor sich etwas vorstellen muss.

### Entscheidungen in Viererpaketen
Beim Sichten und Sortieren — Dateien einordnen, Listen durchgehen,
Altbestand bewerten — werden **höchstens vier Posten pro Runde**
vorgelegt, jeder mit Claudes Einschätzung und einem Zielvorschlag. Dann
Isors Entscheidung abwarten, ausführen, nächstes Paket. Nie zwei Pakete
auf einmal. Grund: Längere Listen werden abgenickt statt geprüft, und
geprüft werden sollen sie.

### Arbeitsteilung am Text (Isor, 2026-08-08)
Korrekturen an bestehendem Text schreibt Claude direkt. **Neue
Fachkapitel formuliert Isor selbst**; Claude liefert Struktur, geprüfte
Fakten und Zahlen und glättet hinterher. Grund: Der Text soll von ihm
kommen, und das Durchgehen ist zugleich das Lernen des Stoffs.

## Session-Typen

### Brainstorm/Design
Ideen verarbeiten und bewerten, ausdesignen was gebaut wird und wie —
Sonderaufgaben ohne Code. Ergebnis: Entscheidungen in die DECISIONS der
Schicht, Design-Absicht ins GDD (Abschnitt „Entwurf", siehe GDD_RULES).

Regel je Baustein: erst ein Design-Abschnitt (was und wie), dann der
Development-Abschnitt (nur Umsetzung). Ein Design-Abschnitt darf mehrere
Bausteine vorentscheiden.

### Development
Nur Umsetzung dessen, was vorentschieden ist.
**Entwurf vor Gerüst (seit 2026-08-05):** Bevor Claude ein Gerüst zeigt,
beschreibt Isor in zwei Sätzen, was das Stück tun muss und welche Werte
es braucht. Erst danach kommt das Gerüst, und der Vergleich zeigt, wo der
eigene Entwurf abwich. Grund: Vorgegebene TODOs üben das Ausfüllen, nicht
das Anfangen vor einer leeren Datei — genau da liegt die Lücke. Claude
wartet die Antwort ab, statt das Gerüst nachzuschieben.

Kleine Design-Fragen (Namen, Ablageort) werden inline geklärt. Fragen,
die Architektur oder mehrere Bausteine betreffen, werden notiert und in
den nächsten Design-Abschnitt gegeben.

Vor dem Coden: **Review-Gate** aus `CODE_GUIDELINES.md` durchgehen.

### Zeugnis
Standortbestimmung zu einem festen Datum. Wird bewusst wiederholt — der
Vergleich zweier Stände ist der Zweck. Auslöser `/harness:zeugnis` oder Zuruf.
Vollständige Regeln in `ASSESSMENT_RULES.md`; dieser Eintrag ist nur der
Zeiger. Die Session **liest und bewertet, sie baut nicht.**

### Prüfung
**Liest und bewertet, baut nicht.** Ergebnis ist eine Befundliste, kein
Umbau — behoben wird danach, in einem eigenen Abschnitt. Zuschnitt:
Haken gegenlesen, Regeln mit frischem Blick prüfen, Bestände gegen die
Wirklichkeit abgleichen.

**Der Gegenstand wird beim Wechsel mitgenannt**, weil der Typ auf
Verschiedenes zeigt: *„Prüfung — Gegenstand: der Harness"* ·
*„… die Prefabs von Isor's Tower"* · *„… der Datenbaum IsorBackup"*.
Ohne den Zusatz ist unklar, was geprüft wird.

**Die Befundliste ist temporär** — eine Datei je Durchgang, nach dem
Anlass benannt, danach ins Archiv. Was überlebt, ist der Punkt in der
ROADMAP, nicht die Liste (`DOC_RULES.md`, Abschnitt 8: eine Checkliste
gehört dem Moment).

Sie heißt `_HARNESS_<Anlass>.md` und liegt oben in der Repo-Wurzel. Das Präfix
ist keine Zierde: `Kern/Werkzeuge/index_bauen.py` erkennt daran, dass die
Datei temporär ist, und führt sie im INDEX in einem eigenen Abschnitt
statt in einer Schicht.

**Geschrieben wird laufend, nicht am Ende.** Jeder Befund geht sofort in
die Liste, samt Beleg — nichts bleibt nur im Kontext. Bricht die Session
ab, wird an der Datei weitergearbeitet. *(Isors Gegenmaßnahme vom
2026-08-22; sie stand bis zum 2026-08-23 nur in einer Arbeitsdatei und
wäre mit ihr fast ins Archiv gegangen.)*

**Prüfbogen, für jede Datei gleich** — diese Fragen, in dieser Folge:
1. Welche Frage beantwortet sie, und beantwortet die sonst niemand?
2. Deckt sich die `Ownership:`-Zeile mit dem tatsächlichen Inhalt?
3. Widerspricht sie einer anderen Datei?
4. In welche Schicht gehört sie?
5. Verfällt ihr Inhalt? → Archiv oder Erzeugung nötig, oder pflegefrei?

Ergebnis je Datei: Soll-Zustand plus konkreter Auftrag für die Session,
die es umsetzt.

**Eine Frage mehr bei Listendateien** (ROADMAP, PLAN, Baulisten), außer
der Reihe gestellt, weil sie nicht auf die Datei zielt, sondern auf jede
einzelne Zeile darin: *Steht jeder zurückgestellte Punkt noch auf einer
Grundlage, die es gibt?* Der Bogen oben prüft die Datei als Ganzes — und
eine ROADMAP besteht ihn mühelos, während eine tote Zeile darin
durchrutscht. Kein Skript kann das übernehmen: Dass die Voraussetzung
eines Punktes weggefallen ist, sieht nur, wer die Entscheidung dazu
kennt. *(Belegt am 2026-08-26: „Knowledge-Archivierung automatisieren"
stand sechs Wochen ohne Gegenstand unter „Später, nur bei Bedarf" und
überlebte dabei diesen Prüfbogen — `STOERUNGEN.md`, „Später, nur bei
Bedarf ist ein blinder Fleck".)*

**Widersprüche sind ein eigener Durchgang.** Sie liegen *zwischen* zwei
Dateien und sind beim Lesen einer einzelnen nicht sichtbar — wer Datei
für Datei prüft, findet sie nie. Deshalb am Ende ein Durchgang quer über
den Bestand: eine Zeile je Art von Information, eine Spalte „Besitzer".
Zwei Besitzer = Konflikt, kein Besitzer = Lücke.

**Prüfer und Ausführender sollen nicht dieselbe Session sein.** Wer
gerade dreißig Befunde behoben hat, liest seine eigenen Haken nicht mehr
unbefangen. Belegt am 2026-08-23: Ein Gegenlese-Durchgang fand zwei von
dreißig Haken nicht gedeckt — einmal war die Korrektur geschrieben, aber
am falschen Eintrag abgelegt, einmal war nur die Regel geändert und nicht
das, was sie vorschrieb. Beide hätten jede Suche innerhalb derselben
Session überstanden.

Abgrenzung zum **Zeugnis**: Beide lesen und bewerten. Ein Zeugnis
bewertet **Isor** und trägt deshalb eine Notenskala und eine Messreihe;
eine Prüfung bewertet **das Gebaute** und trägt eine Befundliste.

### Art *(geplant, nie benutzt)*
Prompts für Bildgenerierung und Concept-Art. Am 2026-07-17 angelegt,
seither kein Einsatz. Wird ausgearbeitet, wenn er gebraucht wird — dann
ist zuerst zu entscheiden, wie er überhaupt aussehen soll.

## Wechsel des Abschnitts

Der Wechsel von Design zu Development **innerhalb derselben Session ist
erlaubt** — der Entwurf steht dann noch im Kontext, und eine neue Session
müsste ihn aus den DECISIONS rekonstruieren, wobei verloren geht, was nur
im Kopf stand.

Er ist aber ein **Kontrollpunkt**: Die Entscheidungen werden **vor** dem
Wechsel festgeschrieben, nicht am Session-Ende. Sonst ist die Begründung
weg, bevor sie geschrieben wurde, falls der Kontext im Bauen aufgeht.
Umgesetzt durch `/harness:wechsel`.

## Parallele Sessions

Laufen mehrere Sessions zugleich (Obergrenze siehe „Begriffe"), regelt
das **Revier**, wer schreiben darf *(seit 2026-08-25; Begründung in
`DECISIONS.md`)*:

- **Frei geschrieben wird nur im Revier** — der Schicht, auf die der
  Fokus des laufenden Abschnitts zeigt. Eine Prüfung schreibt zusätzlich
  ihre eigene Befundliste (Typ „Prüfung" oben). Braucht die Arbeit eine
  fremde Schicht, wird das **gemeldet statt geschrieben** — genau so hat
  die Parallel-Session vom 2026-08-23 richtig gehandelt, nur geraten;
  jetzt ist es Regel.
- **Der Gemeinschaftsboden läuft nur über die Befehle.** Die
  Immer-Pflichten der Doku (`STOERUNGEN.md`, `GLOSSARY.md`, INDEX) und
  `PLAN.md` berühren jede Session, egal welches Revier — aber nur
  innerhalb von `/harness:sichern`, `/harness:wechsel` und
  `/harness:ende`. Diese Befehle stößt Isor an, zwangsläufig
  nacheinander, weil er immer nur mit einer Session zugleich spricht;
  deshalb braucht es keine Sperre. Außerhalb der Befehle schreibt dort
  niemand.
- **Eine ganze Datei wird unmittelbar vor dem Ersetzen erneut gelesen**
  *(seit 2026-08-26)*. Nicht zu Beginn des Abschnitts — dazwischen kann
  eine Parallel-Session geschrieben haben. Das Revier verhindert den
  Zusammenstoß nur, solange sich alle daran halten; am 2026-08-26 tat
  das eine Session nicht, und gerettet hat den fremden Eintrag allein
  das Werkzeug, das den veränderten Dateistand bemerkte
  (`STOERUNGEN.md`, „Zwei Sessions wollten dieselbe Datei schreiben").
  Auf einen Werkzeug-Zufall soll sich keine Regel verlassen.
- **Das Revier wird frei durch Abschnittsende** — Klammer `zu`,
  `aufgehoben` oder Wechsel des Fokus. Wollen zwei offene Sessions
  dieselbe Schicht, entscheidet Isor, wer schreibt: Nur er sieht beide
  Sessions. Der Session-Titel bleibt dabei Anzeige, kein Beleg (siehe
  „Der Typ steht im Session-Titel").

## Die Befehle

Alle benutzen denselben Kern — die Doku-Pflicht steht **einmal** hier
und wird nicht in die Befehle abgeschrieben.

| Befehl | tut | danach |
|---|---|---|
| `/harness:sichern` | Doku-Pflicht abarbeiten | Session läuft weiter |
| `/harness:wechsel <Typ>` | sichern + Typ umstellen + Modus und Regler neu fragen | weiterarbeiten ohne Neu-Einlesen |
| `/harness:ende` | sichern + Commit-Vorschlag | Session ist zu, `/clear` folgt |
| `/harness:sonntag` | Pflegetag, siehe unten | unabhängig vom Session-Typ |
| `/harness:zeugnis` | Session-Typ „Zeugnis" starten | Regeln in `ASSESSMENT_RULES.md` |
| `/harness:einrichten` | Auslieferung im neuen Projekt betriebsbereit machen | einmalig nach dem Auspacken |

**Die Befehlsdateien sind nur Auslöser.** Sie zeigen hierher und tragen
keinen Ablauf. Grund: Alles Inhaltliche gehört an eine Stelle, und das
ist dieser Abschnitt. Weicht ein Auslöser von hier ab, gilt dieser
Abschnitt, und die Abweichung wird gemeldet.

### Wo die Auslöser liegen
Sie liegen an **zwei** Orten, und das ist eine benannte Ausnahme von der
Ownership-Regel (`DOC_RULES.md`, Abschnitt 8):

| Ort | Rolle |
|---|---|
| `Kern/Befehle/` | **Original.** Versioniert, im INDEX geführt, wandert mit der Auslieferung mit. |
| `.claude\commands\harness\` | **Arbeitskopie.** Nur von hier aus findet Claude Code die Befehle. |

**Geändert wird das Original, danach wird kopiert** — nie umgekehrt.

Grund für die Doppelung, **neu gefasst zu 2.0.0**: `.claude\` liegt
seither in der Repo-Wurzel und ist damit versioniert — das alte Argument
(„was dort liegt, ist nicht in der Versionsgeschichte") ist mit dem
Umbau weggefallen. Die Doppelung bleibt trotzdem nötig, aus zwei
anderen Gründen:

1. **Claude Code findet Befehle ausschließlich in `.claude\commands\`.**
   Läge das Original dort, ginge es nicht in die Auslieferung ein — die
   packt `Kern/`, und `.claude\` ist Konfiguration des Programms, nicht
   Teil des Harness.
2. **Das Register.** Der INDEX führt die Befehle über `Kern/Befehle/`;
   ohne Original dort stünden sie in keinem Verzeichnis (Befunde A6 und
   A19 der Abnahme, 2026-08-22 — der Befund gilt, seine damalige
   Begründung nicht mehr).

Dass beide Fassungen gleich sind, prüft `pruefen.py`, Prüfung 3.

Beim Einrichten eines neuen Projekts wird `Kern/Befehle/*.md` nach
`.claude\commands\harness\` kopiert. Das ist der einzige Handgriff, den
die Auslieferung über das Entpacken hinaus verlangt.

### Alle eigenen Befehle in einer Kategorie
Das `/`-Menü mischt drei Quellen: die eingebauten Befehle von Claude
Code, die mitgelieferten Skills und Plugins, und die eigenen. Es sortiert
sie nicht sichtbar auseinander. Deshalb liegen **alle** eigenen Befehle
im Unterordner `.claude\commands\harness\` und erscheinen dadurch als
`/harness:<Name>`. Tippt man `/harness`, steht die vollständige Liste da
und sonst nichts.

**Ein neuer eigener Befehl kommt ausnahmslos in diesen Ordner** — auch
wenn er thematisch woanders hingehört. Der Namensraum ist die einzige
Stelle, an der die eigenen Befehle von den fremden zu unterscheiden sind.
Kein globaler Skill unter `~\.claude\skills\` mehr: Der ließe sich nicht
in die Kategorie einordnen. Preis dafür — die Befehle gibt es nur, wenn
`Harness Project` der geöffnete Ordner ist. Das ist gewollt, denn sie
schreiben ohnehin alle in dieses Repo.

### Ablauf von `/harness:sichern`
1. Diesen Abschnitt und „Doku-Pflicht" lesen, falls in dieser Session
   noch nicht geschehen.
2. **Typ des laufenden Abschnitts** feststellen. Ist er nie genannt
   worden, wird gefragt statt geraten — er entscheidet, welche Dateien
   geschrieben werden.
3. Doku-Pflicht abarbeiten: erst die Punkte, die immer gelten, dann die
   Zeile der Typ-Tabelle.
4. **Nur Belegtes.** Geschrieben wird, was in dieser Session tatsächlich
   passiert ist. Keine Zahl, die nicht gemessen wurde; keine
   Entscheidung, die nicht gefallen ist.
5. **`Kern/Werkzeuge/pruefen.py` laufen lassen** — nach dem Schreiben,
   denn das Schreiben erzeugt die Fehler, die es findet. Die Prüfungen:
   tote Verweise · Datumsfolge und Pflichtfelder der Chroniken · Befehle
   gegen ihre Arbeitskopie · Zahlwörter in Überschriften · Glossar gegen
   die Besitzerdateien · Hooks gegen ihre Vorlage · absolute Pfade
   außerhalb von `Kern/PFADE.md` · Artifact-IDs im Knowledge-Ordner gegen
   den `ARTIFACT_INDEX.md`. Das Skript **meldet nur**; jeder Fund ist ein
   Befund, kein Auftrag. Was es nicht sieht, ist, ob eine Aussage stimmt
   — dafür braucht es weiterhin einen Abschnitt vom Typ Prüfung.
6. **Ergebnis melden:** eine Zeile je Eintrag mit Zieldatei. „Nichts zu
   schreiben" ist ein gültiges Ergebnis und wird ebenso gemeldet — sonst
   ist nicht unterscheidbar, ob nichts anfiel oder etwas vergessen wurde.
   Die Funde des Skripts kommen dazu, auch wenn es null waren.

### Ablauf von `/harness:einrichten`

Einmalig, nachdem eine Auslieferung in ein neues Projekt ausgepackt
wurde. Er ersetzt die Handgriff-Liste, die bis 2.0.0 in
`VERSIONIERUNG.md` stand — eine Liste zum Abarbeiten wuchs mit jeder
Version und wurde dabei unvollständiger.

1. **Nachsehen, was schon da ist.** Trägt `Kern/PFADE.md` bereits Pfade,
   ist das Projekt eingerichtet: melden, was dort steht, und fragen, ob
   geändert werden soll. Nichts stillschweigend überschreiben.
2. **Die Pfade abfragen — einzeln, nicht als Block.** Je Marke aus
   `Kern/PFADE.md`: wofür sie steht, was dort liegen soll, und ein
   Vorschlag, wenn sich einer aus der Umgebung ableiten lässt. Ein Ort,
   den es noch nicht gibt, wird angelegt — nach Rückfrage.
   Marken, die das Projekt nicht braucht, werden auf `(nicht benutzt)`
   gesetzt statt geraten.
3. **`Kern/PFADE.md` schreiben.** Nur die Pfad-Spalte; Marken, Zweck und
   Regeln bleiben, wie sie sind.
4. **Befehle in die Arbeitskopie:** `Kern/Befehle/*.md` nach
   `.claude\commands\harness\`. Ohne diesen Schritt gibt es die Befehle
   im neuen Projekt nicht (siehe „Wo die Auslöser liegen").
5. **`PLAN.md` anlegen**, falls sie fehlt — nur Kopf und der Abschnitt
   „Für die nächste Session". Die Leseordnung nennt die Datei; ohne sie
   zeigt sie ins Leere. Eine vorhandene `PLAN.md` wird nicht angefasst.
6. **Hook eintragen:** `Kern/Vorlagen/settings.json` nach
   `.claude\settings.json`. Gibt es die Datei dort schon, wird **nur der
   `hooks`-Block** hineinübernommen — der Rest ist rechner- und
   personenabhängig und gehört dem Nutzer. Ohne diesen Schritt läuft
   `pruefen.py` beim Session-Start nicht von selbst, und die Leseordnung
   fällt auf ihre Rückfallebene zurück (`CLAUDE.md`, Punkt 5).
7. **INDEX erzeugen:** `python Kern/Werkzeuge/index_bauen.py --write`.
   Zuletzt, weil die Schritte davor Dateien anlegen. Der `INDEX.md` wird
   erzeugt und nie mitgeliefert — eine mitgelieferte Fassung wäre ab dem
   ersten neuen Dokument falsch.
8. **`pruefen.py` laufen lassen und das Ergebnis melden.** Der erste Lauf
   in einem frischen Baum meldet Verweise auf Schichten, die es dort noch
   nicht gibt (`Uni/`, `Projekte/<Name>/`) — das ist erwartet und kein
   Befund. Danach einmal `python Kern/Werkzeuge/pruefen.py --glossar-ok`:
   Frisch kopierte Dateien tragen alle dasselbe Datum, und der
   Glossar-Hinweis stünde sonst ohne Anlass da. Was zu tun bleibt,
   entscheidet der Nutzer.

**Der Befehl legt keine Schichten an.** Welche Schichten ein Projekt
braucht, weiß nur der Mensch; ein leerer Ordner `Uni/` in einem Projekt
ohne Studium wäre eine Behauptung. Der Kern läuft ohne sie.

### Ablauf von `/harness:wechsel <Typ>`
Der Wechsel ist ein **Kontrollpunkt**, siehe „Wechsel des Abschnitts".
1. `/harness:sichern` vollständig — **vor** dem Wechsel, nicht am Session-Ende.
2. Bei Design → Development zusätzlich: Steht jede getroffene
   Entscheidung in der DECISIONS der Schicht? Was fehlt, wird jetzt
   geschrieben, solange die Begründung noch da ist.
3. Neuen Typ benennen und den alten Abschnitt für beendet erklären. Beim
   Typ **Prüfung** gehört der Gegenstand dazu („Prüfung — Gegenstand:
   der Harness"). Im selben Zug den **Session-Titel** umschreiben: nur
   die Klammer, das Thema bleibt (siehe „Der Typ steht im
   Session-Titel").
4. **Modus und die zwei Regler neu fragen.** Sie hängen am Abschnitt,
   nicht an der Session.

### Ablauf von `/harness:ende`
1. `/harness:sichern`.
2. **Baustein-Frage:** Ist der Baustein fertig — gebaut, geprüft *und*
   dokumentiert? Wenn nein: benennen, was fehlt, und in die ROADMAP der
   Schicht, damit die nächste Session nicht bei null sucht.
3. Commit-Vorschlag nach Abschnitt „Session-Ende" — je berührtem Repo
   einer, jedes zählt seine eigene Nummer.
4. **Plan nachziehen** (`PLAN.md`):
   - erledigte Punkte **abhaken** — nicht löschen;
   - die **stehen gebliebenen Punkte einmal gegen den heutigen Stand
     halten**. Nicht neu schreiben — nur bestätigen oder melden, was
     überholt ist. Grund: Überschrieben wird sonst allein die Übergabe,
     und ein alter Abschnitt sieht danach genauso verbindlich aus wie ein
     frisch geschriebener. Belegt am 2026-08-23: Eine frische Session las
     „Testphase — beginnt nach der Prüfung" als gültigen Auftrag vor,
     obwohl Isor längst anders entschieden hatte (`STOERUNGEN.md`);
     `PLAN.md` ist mit ~100 Zeilen klein genug, dass der Blick nichts
     kostet;
   - Abschnitt **„Für die nächste Session" überschreiben**. Immer, nicht
     nur wenn etwas offen ist: „gerade nichts offen" ist ein gültiger
     Inhalt. Grund: Nur so findet die nächste Session ihren Auftrag —
     er lag zuletzt am Ende einer Bauliste und wurde übersehen
     (`Kern/DECISIONS.md`, 2026-08-23).
   - Sind dabei **alle** Punkte eines Zeitraums abgehakt, meldet Claude
     das und fragt, ob der Zeitraum geschnitten wird. Entschieden wird
     das von Isor; melden ist Pflicht. Der Schnitt selbst steht im Kopf
     von `PLAN.md`: Ereignis ins LOG, Punkte in der ROADMAP abhaken,
     Datei leeren.
5. **Session-Titel auf `(zu)` setzen.** Letzter Moment, in dem das geht —
   `/clear` ruft Claude nicht mehr auf.
6. Danach ist die Session zu. Claude fängt nichts Neues mehr an.

## Pflegetag (`/harness:sonntag`)

Wochentakt, unabhängig von Session und Typ. **Dieser Abschnitt besitzt
den Zeitpunkt und die Liste, die Fachdatei je Punkt den Inhalt** —
dieselbe Arbeitsteilung wie beim Review-Gate.

1. **Artifact-Durchsicht** samt Abgleich gegen die tatsächlich
   veröffentlichten Seiten — Verfahren in `ARTIFACT_RULES.md`,
   Abschnitt „Wann geschaut wird". Claude legt eine Vorschlagsliste vor
   und ändert nichts von selbst.
2. **Eine Seite gründlich** *(seit 2026-08-25)* — die lebendige Seite
   mit dem ältesten Stand im `ARTIFACT_INDEX.md`, gegen Code und
   führende Quelle gehalten. Verfahren, Auswahlregel und Ausnahmen in
   `ARTIFACT_RULES.md`, Abschnitt „Wann geschaut wird". Grund: Der
   Abgleich allein sieht nur Metadaten — er fand drei von rund dreißig
   Funden (2026-08-23).

Mehr Punkte hat der Pflegetag derzeit nicht — und `pruefen.py` wird
bewusst **keiner**. Das Skript läuft in Sekunden und bei jedem
`/harness:sichern`; die Fehler, die es findet, entstehen beim Schreiben
und sollen nicht bis Sonntag warten. Der Pflegetag ist für Arbeit, die
Aufwand kostet und deshalb einen Termin braucht — das Abrufen und
Gegenlesen der Artifact-Seiten. *(Entschieden 2026-08-23, nachdem die
Trennung beim Bau des Skripts auffiel.)*

**Nicht Teil des Pflegetags: das Backup** (Isor, 2026-08-23). Das Skript
`IsorBackup/Werkzeuge/sichern.ps1` ist gebaut und bleibt liegen; Isor
fährt die Sicherung bis auf Weiteres **von Hand**, ohne den Harness.
Claude erinnert nicht daran und meldet den Punkt auch nicht als offen.
Wieder aufgenommen wird er erst, wenn die Testphase durch ist und der
Harness sich im laufenden Betrieb bewährt hat — nicht nach Kalender.
Begründung in `Kern/DECISIONS.md`, 2026-08-23.

## Die Prüfebenen

Der Harness prüft an mehreren Stellen, und ohne Übersicht verliert man
sie aus dem Blick *(Isor, 2026-08-23: „so viele Prüfebenen, dass ich
nicht mehr den Überblick habe")*. Dieser Abschnitt besitzt die
**Übersicht**, jede Zeile verweist auf ihren Besitzer.

| Ebene | prüft | wann | wer urteilt |
|---|---|---|---|
| `Kern/Werkzeuge/pruefen.py` | Verweise · Chronik-Format · Befehle gegen Arbeitskopie · Zahlwörter · Glossar · Hooks gegen Vorlage · Pfade gegen `PFADE.md` · Artifact-IDs im Knowledge | Session-Start (**per Hook erzwungen**) und jedes `/harness:sichern` | Skript |
| `Kern/Werkzeuge/index_bauen.py` | fehlt eine `Ownership:`-Zeile? | wenn Dateien dazukommen oder wegfallen | Skript |
| `Projekte/<Name>/Werkzeuge/prefab_status.py` | welche Prefabs es gibt und was auffiel | bei Projektarbeit | Skript und Mensch |
| **Review-Gate** (`CODE_GUIDELINES.md`) | Fattening · Enum-Sicherheit · Werkzeugwahl · Naming · Artifact-Bezug | vor dem Coden | Mensch und Claude |
| **Doku-Pflicht** (unten) | Knowledge- · Störungs- · INDEX- · Glossar-Frage | jedes `/harness:sichern` | Claude fragt, Isor entscheidet |
| **Pflegetag** (`/harness:sonntag`) | stimmen die Artifact-Seiten noch? | wöchentlich | Mensch und Claude |
| **Typ Prüfung** (oben) | stimmt der Inhalt? | auf Zuruf | Mensch und Claude |

**Die Trennlinie verläuft zwischen Skript und Urteil: Skripte prüfen
Form und Bestand, Menschen prüfen Aussagen.** Sie ersetzen einander
nicht. Kein Skript hätte gefunden, dass eine Artifact-Seite ein Skript
beschreibt, das es nie gab; kein Mensch geht zuverlässig 46 Dateien nach
Zahlwörtern durch. *(Beides am 2026-08-23 gemessen: die Artifact-Prüfung
fand rund dreißig inhaltliche Fehler, die kein Werkzeug sieht;
`pruefen.py` fand eine Begriffskollision, die drei Leserunden übersehen
hatten.)*

## Doku-Pflicht

**Sie hängt am Typ des Abschnitts** — eine Zeugnis-Session schreibt in
andere Dateien als eine Development-Session.

Immer, bei jedem Typ:
1. **Knowledge-Frage.** Claude fragt, ob etwas als Wissensseite behalten
   werden soll, schlägt Themen vor, Isor wählt aus oder ergänzt. „Nein"
   ist eine gültige Antwort — die **Frage** darf nie ausfallen.
   Ablage und Form: `KNOWLEDGE_RULES.md`.
2. **Störungs-Frage.** Gab es einen Aussetzer? Wenn ja, ein Eintrag in
   `STOERUNGEN.md`. **Nennt er ein Gegenmittel, wird im selben Zug
   gefragt, ob es als Punkt in die ROADMAP der Schicht mitkommt** — die
   Antwort darf „nein" sein, die Frage nicht ausfallen. Ohne diesen
   zweiten Halbsatz versandet der Vorschlag: `STOERUNGEN.md` ist eine
   Chronik, und eine Chronik wird nach Belegen durchsucht, nicht nach
   Aufgaben. Belegt am 2026-08-26 — dort standen drei benannte
   Gegenmittel, von denen keines je eine Aufgabe geworden war.
3. **INDEX** nachziehen, falls Dateien dazukamen oder wegfielen.
4. **Glossar-Frage.** Ist ein Begriff dazugekommen, oder hat sich eine
   Definition geändert? Dann `GLOSSARY.md` nachziehen. Der INDEX wird
   erzeugt und kann nicht veralten — das Glossar wird von Hand gepflegt
   und ist nach `DOC_RULES.md` Abschnitt 4 ein **Verzeichnis**, das
   laufend abgeglichen werden muss. Ohne diesen Punkt sammelte es
   zwischen dem 2026-08-22 und dem 2026-08-23 drei falsche Zeilen
   (Befunde P10 bis P13).

Nach Typ zusätzlich:

| Typ | schreibt außerdem |
|---|---|
| Brainstorm/Design | DECISIONS der Schicht · GDD (Entwurf) · ROADMAP, wenn Aufgaben entstanden |
| Development | LOG der Schicht · DECISIONS · ROADMAP abhaken · TDD_NOTES bei echter Projektarbeit · Abgabe-Abschnitt, wenn ein Baustein fertig wurde |
| Zeugnis | `Kern/Zeugnisse/<Datum>.md` · ARTIFACT_INDEX · ROADMAP nur um die Befunde. **Sonst nichts** — es wurde nichts gebaut und nichts entschieden. |
| Prüfung | Befundliste (temporär, je Durchgang) · ROADMAP der geprüften Schicht um die Befunde · LOG der Schicht, **ein Satz**: was geprüft, wie viele Befunde, woran geprüft. Keine DECISIONS — es wurde nichts entschieden. |

## Session-Ende

- **Schnitt an der Baustein-Grenze**, nicht am Kontext-Balken: Baustein
  fertig → sichern → Commit → `/clear`. Einen neuen Baustein nicht unter
  etwa 30 % Restkontext anfangen — lieber vorher schneiden.
- **Commit-Vorschlag:** Titel im Schema `Update V <nächste Nummer>`
  (vierstellig hochgezählt; die nächste Nummer wird per `git log`
  nachgeschlagen, nicht geschätzt). Titel und Beschreibung auf Englisch.
  Isor committet selbst über **GitHub Desktop** — der Vorschlag kommt
  deshalb als Datei zum Kopieren, nie als `git commit`-Befehl. Claude
  committet und pusht nicht.
  Die Bedeutung der Nummer steht in `VERSIONIERUNG.md`.
