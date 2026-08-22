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

Jeder **Abschnitt** hat genau einen Typ und einen Fokus. Eine **Session**
kann mehrere Abschnitte enthalten. Höchstens 2–4 Sessions parallel offen.

## Typ, Modus und Regler

**Am Anfang jeder Session fragt Claude nach Typ und Modus** — bei jedem
Typ, nicht nur beim Entwerfen. Beide gehören zusammen und hängen am
Abschnitt, nicht an der Session: Der **Typ** entscheidet, welche Dateien
die Doku-Pflicht am Ende schreibt, der **Modus**, wie dazwischen
gearbeitet wird. Die Typen stehen unten unter „Session-Typen".

Wird der Typ nicht gefragt, fällt es erst bei `/harness:sichern` auf —
dann steht die Doku-Pflicht ohne ihren Maßstab da.
*(Regel aus einem echten Aussetzer, 2026-08-22.)*

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

**Die Dateien unter `.claude\commands\` sind nur Auslöser.** Sie zeigen
hierher und tragen keinen Ablauf. Grund: Der Projektstamm ist
`Harness Project`, das Repo aber `My Harness Development` — was in
`.claude\` liegt, ist nicht versioniert. Alles Inhaltliche steht deshalb
hier, und ein verlorener Auslöser ist aus diesem Abschnitt in zwei
Minuten neu geschrieben. Weicht ein Auslöser von hier ab, gilt dieser
Abschnitt, und die Abweichung wird gemeldet.

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
5. **Ergebnis melden:** eine Zeile je Eintrag mit Zieldatei. „Nichts zu
   schreiben" ist ein gültiges Ergebnis und wird ebenso gemeldet — sonst
   ist nicht unterscheidbar, ob nichts anfiel oder etwas vergessen wurde.

### Ablauf von `/harness:wechsel <Typ>`
Der Wechsel ist ein **Kontrollpunkt**, siehe „Wechsel des Abschnitts".
1. `/harness:sichern` vollständig — **vor** dem Wechsel, nicht am Session-Ende.
2. Bei Design → Development zusätzlich: Steht jede getroffene
   Entscheidung in der DECISIONS der Schicht? Was fehlt, wird jetzt
   geschrieben, solange die Begründung noch da ist.
3. Neuen Typ benennen und den alten Abschnitt für beendet erklären.
4. **Modus und die zwei Regler neu fragen.** Sie hängen am Abschnitt,
   nicht an der Session.

### Ablauf von `/harness:ende`
1. `/harness:sichern`.
2. **Baustein-Frage:** Ist der Baustein fertig — gebaut, geprüft *und*
   dokumentiert? Wenn nein: benennen, was fehlt, und in die ROADMAP der
   Schicht, damit die nächste Session nicht bei null sucht.
3. Commit-Vorschlag nach Abschnitt „Session-Ende" — je berührtem Repo
   einer, jedes zählt seine eigene Nummer.
4. Danach ist die Session zu. Claude fängt nichts Neues mehr an.

## Pflegetag (`/harness:sonntag`)

Wochentakt, unabhängig von Session und Typ. **Dieser Abschnitt besitzt
den Zeitpunkt und die Liste, die Fachdatei je Punkt den Inhalt** —
dieselbe Arbeitsteilung wie beim Review-Gate.

1. **Artifact-Durchsicht** samt Abgleich gegen die tatsächlich
   veröffentlichten Seiten — Verfahren in `ARTIFACT_RULES.md`,
   Abschnitt „Wann geschaut wird". Claude legt eine Vorschlagsliste vor
   und ändert nichts von selbst.
2. **Backup.** Isor steckt die Platte an, Claude startet
   `IsorBackup/Werkzeuge/sichern.ps1` — Probelauf zuerst. Ist keine
   Platte angesteckt, wird das gemeldet und der Punkt bleibt offen; er
   gilt nicht als erledigt.

## Doku-Pflicht

**Sie hängt am Typ des Abschnitts** — eine Zeugnis-Session schreibt in
andere Dateien als eine Development-Session.

Immer, bei jedem Typ:
1. **Knowledge-Frage.** Claude fragt, ob etwas als Wissensseite behalten
   werden soll, schlägt Themen vor, Isor wählt aus oder ergänzt. „Nein"
   ist eine gültige Antwort — die **Frage** darf nie ausfallen.
   Ablage und Form: `KNOWLEDGE_RULES.md`.
2. **Störungs-Frage.** Gab es einen Aussetzer? Wenn ja, eine Zeile in
   `STOERUNGEN.md`.
3. **INDEX** nachziehen, falls Dateien dazukamen oder wegfielen.

Nach Typ zusätzlich:

| Typ | schreibt außerdem |
|---|---|
| Brainstorm/Design | DECISIONS der Schicht · GDD (Entwurf) · ROADMAP, wenn Aufgaben entstanden |
| Development | LOG der Schicht · DECISIONS · ROADMAP abhaken · TDD_NOTES bei echter Projektarbeit · Abgabe-Abschnitt, wenn ein Baustein fertig wurde |
| Zeugnis | `Kern/Zeugnisse/<Datum>.md` · ARTIFACT_INDEX · ROADMAP nur um die Befunde. **Sonst nichts** — es wurde nichts gebaut und nichts entschieden. |

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
