# WORKFLOW.md — Session-Disziplin

Ownership: Wie eine Session abläuft — Begriffe, Modus und Regler,
Session-Typen, Doku-Pflicht, die Befehle und das Session-Ende.
Regeln über Dokumente stehen in `DOC_RULES.md`, Code-Regeln in
`CODE_GUIDELINES.md`, Nummernsysteme in `VERSIONIERUNG.md`.

## Begriffe

- **Session** — ein durchgehender Arbeitsraum von Anfang bis `/clear`.
  Isors Wort dafür ist „Work Area".
- **Abschnitt** — eine Phase innerhalb einer Session mit genau **einem**
  Typ. `/wechsel` beendet einen Abschnitt und öffnet den nächsten.
- **Baustein** — eine abgeschlossene Funktionseinheit, die sich in einem
  Zug entwerfen und bauen lässt. **Fertig heißt gebaut, geprüft *und*
  dokumentiert** — solange der zugehörige Abschnitt im Abgabetext fehlt,
  ist der Baustein nicht fertig.

Jeder **Abschnitt** hat genau einen Typ und einen Fokus. Eine **Session**
kann mehrere Abschnitte enthalten. Höchstens 2–4 Sessions parallel offen.

## Modus und Regler

**Am Anfang jeder Session fragt Claude nach dem Modus** — bei jedem Typ,
nicht nur beim Entwerfen.

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
Vergleich zweier Stände ist der Zweck. Auslöser `/zeugnis` oder Zuruf.
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
Umgesetzt durch `/wechsel`.

## Die drei Befehle

Alle drei benutzen denselben Kern — die Doku-Pflicht steht **einmal** hier
und wird nicht in die Befehle abgeschrieben.

| Befehl | tut | danach |
|---|---|---|
| `/sichern` | Doku-Pflicht abarbeiten | Session läuft weiter |
| `/wechsel <Typ>` | `/sichern` + Typ umstellen + Modus und Regler neu fragen | weiterarbeiten ohne Neu-Einlesen |
| `/ende` | `/sichern` + Commit-Vorschlag | Session ist zu, `/clear` folgt |

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
