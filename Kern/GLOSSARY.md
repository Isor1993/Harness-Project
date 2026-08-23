# GLOSSARY.md — Begriffe mit fester Bedeutung

Ownership: Nur die **Kurzform** jedes Begriffs und der Zeiger auf seinen
Besitzer. Diese Datei definiert nichts selbst — sie sagt, wo die
Definition steht. Weicht eine Kurzform hier von der Besitzerdatei ab,
gilt die Besitzerdatei, und die Kurzform wird nachgezogen.

Warum es sie gibt: In zwei Tagen kollidierten drei Begriffspaare —
„Work Area" gegen „Session", „Uni-Modus" gegen „Lernmodus", „Modus"
gegen „Regler". Ein Begriff, der zwei Dinge meint, macht jede Regel
mehrdeutig, die ihn benutzt.

Sie ist **nachschlagbar, nicht Startgepäck** — sie steht nicht in der
Leseordnung.

## Über Dokumente

| Begriff | Kurzform | Besitzer |
|---|---|---|
| **Ownership** | Für jede Information gibt es genau ein Dokument, das sie besitzt; alle anderen verweisen. | `DOC_RULES.md`, Abschnitt 1 |
| **Schicht** | Ein als Ganzes herausnehmbarer Ordner: `Kern`, `Uni`, `IsorBackup` — und **je Projekt** ein `Projekte/<Name>`. `Projekte/` selbst ist nur der Sammelordner. Schicht = Thema, Dokumentart = Art der Information. | `DOC_RULES.md`, Abschnitt 10 |
| **Chronik** | Beantwortet „was ist wann passiert". Wird nur ergänzt, und zwar **nach Datum einsortiert, nicht hinten angehängt**; kann nie falsch werden, braucht kein Archiv. | `DOC_RULES.md`, Abschnitt 4 |
| **Verzeichnis** | Beantwortet „was existiert jetzt und wo". Muss laufend abgeglichen werden, sonst führt es in die Irre. | `DOC_RULES.md`, Abschnitt 4 |
| **Register** | Verzeichnis fremder Adressen, das vollständig sein muss und deshalb **nicht** nach Schichten geteilt wird. | `DOC_RULES.md`, Abschnitt 8 |
| **Archiv** | Überholte Einträge. Wird nie aufgeräumt; jeder Eintrag nennt, wodurch er abgelöst wurde. | `DOC_RULES.md`, Abschnitt 4 |
| **Erzeugt** | Datei, die ein Skript aus einer Quelle schreibt statt von Hand gepflegt zu werden. Das Skript besitzt die Liste, der Mensch die Beschreibung. | `DOC_RULES.md`, Abschnitt 5 |

## Über Sessions

| Begriff | Kurzform | Besitzer |
|---|---|---|
| **Session** | Ein durchgehender Arbeitsraum von Anfang bis `/clear`. Isors Wort dafür: „Work Area". | `WORKFLOW.md`, Begriffe |
| **Abschnitt** | Eine Phase innerhalb einer Session mit genau **einem** Typ. | `WORKFLOW.md`, Begriffe |
| **Baustein** | Abgeschlossene Funktionseinheit. Fertig heißt gebaut, geprüft **und** dokumentiert. | `WORKFLOW.md`, Begriffe |
| **Typ** | Was in diesem Abschnitt getan wird: Brainstorm/Design, Development, Zeugnis, Prüfung, (Art). Entscheidet, welche Dateien die Doku-Pflicht schreibt. | `WORKFLOW.md`, Session-Typen |
| **Prüfung** | Ein Abschnitt, der **liest und bewertet, aber nicht baut**. Ergebnis ist eine Befundliste; der Gegenstand wird beim Wechsel mitgenannt. | `WORKFLOW.md`, Session-Typen |
| **Modus** | Wie gearbeitet wird: **Lernmodus** (ausführlich, visuell, Verständnis prüfen) oder **Normal** (kurz). Setzt nur die Voreinstellung der Regler. | `WORKFLOW.md`, Typ, Modus und Regler |
| **Regler** | Einzeln verstellbare Einstellung innerhalb eines Modus — Visualisierung und „Wer schreibt". Nicht dasselbe wie der Modus. | `WORKFLOW.md`, Typ, Modus und Regler |
| **Doku-Pflicht** | Was am Ende eines Abschnitts geschrieben wird: die festen Punkte, die bei jedem Typ gelten, plus eine Zeile je Typ. | `WORKFLOW.md`, Doku-Pflicht |
| **Pflegetag** | Wochentakt, unabhängig vom Session-Typ: Artifacts durchsehen und gegen die veröffentlichten Seiten abgleichen. Ausgelöst durch `/harness:sonntag`. | `WORKFLOW.md`, Pflegetag |
| **Auslöser** | Eine Befehlsdatei unter `.claude\commands\harness\`. Trägt keinen Ablauf, nur den Zeiger auf die Regeldatei. | `WORKFLOW.md`, Die Befehle |
| **Review-Gate** | Checkliste, die vor dem Coden durchgegangen wird. | `CODE_GUIDELINES.md` |
| **Prüfebene** | Eine der Stellen, an denen der Harness prüft — drei davon sind Skripte (Form und Bestand), vier verlangen ein Urteil (Aussagen). | `WORKFLOW.md`, Die Prüfebenen |
| **Hook** | Kommando, das der Harness bei einem Ereignis selbst ausführt, eingetragen in `.claude\settings.json`. Erzwingt eine Skript-Prüfebene, statt an sie zu erinnern — beurteilt aber nichts. | `WORKFLOW.md`, Die Prüfebenen |
| **Befund** | Ergebnis einer Prüfung: eine Stelle, an der etwas falsch, doppelt, widersprüchlich ist oder fehlt. Wird notiert, nicht sofort geändert. Ein **Zustand**. | `WORKFLOW.md`, Begriffe |
| **Störung** | Vorfall, in dem der Harness nicht so gearbeitet hat wie vorgesehen. Ein **Ereignis** — nicht dasselbe wie ein Befund und nicht dasselbe wie ein Fehler im Code. | `STOERUNGEN.md` |

## Über Nummern und Ausgaben

| Begriff | Kurzform | Besitzer |
|---|---|---|
| **Harness-Version** | Reifegrad des Harness selbst, steht in `CLAUDE.md`. | `VERSIONIERUNG.md` |
| **V-Nummer** | Vierstellige Commit-Nummer im Titel `Update V 0.0043`. Jedes Repo zählt eigenständig. | `VERSIONIERUNG.md` |
| **Auslieferung** | **Vorlage** des Kerns unter `05_Werkzeuge\Harness_Auslieferungen\`, benannt nach der Harness-Version — keine Kopie: Was nur Isor betrifft, wird beim Packen entfernt. | `VERSIONIERUNG.md` |
| **Vorlage** | Zwei Verwendungen, beide meinen „Original zum Kopieren": die Auslieferung als Ganzes (Zeile darüber) und einzeln die Dateien unter `Kern/Vorlagen/`, deren Arbeitskopie in `.claude\` liegt. | `Kern/Vorlagen/README.md` |

Jeder hier geführte Begriff nennt seinen Besitzer. Ob die Liste
**vollständig** ist, kann diese Datei nicht selbst sagen — sie wird von
Hand gepflegt und merkt nicht, dass anderswo ein Begriff entstanden ist.
Dagegen hilft nur, dass die Doku-Pflicht danach fragt (`WORKFLOW.md`).
Beleg: Der Session-Typ „Prüfung" entstand am 2026-08-23 und fehlte hier,
bis ihn die erste Prüfung fand (Befund P10).
