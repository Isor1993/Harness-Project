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
| **Altstand** | Der Bestand einer abgeschlossenen Phase samt seiner Befunde. **Kein Auftrag** — wird aufgeschlagen, wenn über die Übernahme eines Bausteins entschieden wird. Nicht dasselbe wie ein Archiv: Archiviertes ist überholt, Altstand ist vertagt. | `Projekte/Isor_Tower/ALTSTAND.md` |

## Über Sessions

| Begriff | Kurzform | Besitzer |
|---|---|---|
| **Session** | **Zwei Bedeutungen, die auseinanderzuhalten sind.** Im Harness: ein durchgehender Arbeitsraum von Anfang bis `/clear` (Isors Wort: „Work Area"). Im Spiel: die laufende Runde bei Unitys Multiplayer Services — ein Host, seine Gäste und ein Join-Code, im Code `IHostSession`. | `WORKFLOW.md`, Begriffe · `Projekte/Isor_Tower/DECISIONS/Multiplayer.md` |
| **Abschnitt** | Eine Phase innerhalb einer Session mit genau **einem** Typ. | `WORKFLOW.md`, Begriffe |
| **Baustein** | Abgeschlossene Funktionseinheit. Fertig heißt gebaut, geprüft **und** dokumentiert. | `WORKFLOW.md`, Begriffe |
| **Typ** | Was in diesem Abschnitt getan wird: Brainstorm/Design, Development, Zeugnis, Prüfung, (Art). Entscheidet, welche Dateien die Doku-Pflicht schreibt. | `WORKFLOW.md`, Session-Typen |
| **Prüfung** | Ein Abschnitt, der **liest und bewertet, aber nicht baut**. Ergebnis ist eine Befundliste; der Gegenstand wird beim Wechsel mitgenannt. | `WORKFLOW.md`, Session-Typen |
| **Prüfstand** | Eine dauerhaft leere Szene im Projekt, in der ein Baustein isoliert getestet wird. **Nicht dasselbe wie der Session-Typ „Prüfung"** — der Prüfstand ist ein Ort im Spiel, die Prüfung eine Arbeitsweise. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Phase 0 läuft im eigenen Prüfstand" |
| **Naht** | Eine bewusst eingezogene Trennstelle, die einen späteren Tausch billig hält: Der Motor bekommt seine Eingabe gereicht, der Verbindungsaufbau liegt hinter `ISessionService`. Kein Selbstzweck — eine Naht ohne absehbaren Tausch ist Abstraktion ohne Anlass. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md` |
| **Modus** | Wie gearbeitet wird: **Lernmodus** (ausführlich, visuell, Verständnis prüfen) oder **Normal** (kurz). Setzt nur die Voreinstellung der Regler. | `WORKFLOW.md`, Typ, Modus und Regler |
| **Regler** | Einzeln verstellbare Einstellung innerhalb eines Modus — Visualisierung und „Wer schreibt". Nicht dasselbe wie der Modus. | `WORKFLOW.md`, Typ, Modus und Regler |
| **Doku-Pflicht** | Was am Ende eines Abschnitts geschrieben wird: die festen Punkte, die bei jedem Typ gelten, plus eine Zeile je Typ. | `WORKFLOW.md`, Doku-Pflicht |
| **Pflegetag** | Wochentakt, unabhängig vom Session-Typ: Artifacts durchsehen und gegen die veröffentlichten Seiten abgleichen, dazu **eine** Seite gründlich gegen den Code. Ausgelöst durch `/harness:sonntag`. | `WORKFLOW.md`, Pflegetag |
| **Auslöser** | Eine Befehlsdatei unter `.claude\commands\harness\`. Trägt keinen Ablauf, nur den Zeiger auf die Regeldatei. | `WORKFLOW.md`, Die Befehle |
| **Review-Gate** | Checkliste, die vor dem Coden durchgegangen wird. | `CODE_GUIDELINES.md` |
| **Prüfebene** | Eine der Stellen, an denen der Harness prüft — drei davon sind Skripte (Form und Bestand), vier verlangen ein Urteil (Aussagen). | `WORKFLOW.md`, Die Prüfebenen |
| **Hook** | Kommando, das der Harness bei einem Ereignis selbst ausführt, eingetragen in `.claude\settings.json`. Erzwingt eine Skript-Prüfebene, statt an sie zu erinnern — beurteilt aber nichts. | `WORKFLOW.md`, Die Prüfebenen |
| **Befund** | Ergebnis einer Prüfung: eine Stelle, an der etwas falsch, doppelt, widersprüchlich ist oder fehlt. Wird notiert, nicht sofort geändert. Ein **Zustand**. | `WORKFLOW.md`, Begriffe |
| **Hinweis** | Meldung von `pruefen.py`, die **kein Befund** ist: Sie nennt einen Zustand, der auch richtig sein kann, und zählt deshalb nicht ins Ergebnis. Steht mit `?` statt `!`. Damit bleibt „0 Funde" ein Zeichen, dem man trauen kann. | `WORKFLOW.md`, Ablauf von `/harness:sichern` |
| **Revier** | Die Schicht, in die eine Session frei schreiben darf — bestimmt vom Fokus ihres laufenden Abschnitts. Wird frei durch Abschnittsende; Gemeinschaftsdateien laufen nur über die Befehle. | `WORKFLOW.md`, Parallele Sessions |
| **Störung** | Vorfall, in dem der Harness nicht so gearbeitet hat wie vorgesehen. Ein **Ereignis** — nicht dasselbe wie ein Befund und nicht dasselbe wie ein Fehler im Code. | `STOERUNGEN.md` |
| **Lern-Log** | Laufende Aufzeichnung, was Isor selbst schaffte, wo Hilfe nötig war und welche Fehlerbilder auftraten — Rohmaterial der Zeugnisse. Beschreibt eine Person und reist deshalb mit keiner Auslieferung. | `Kern/LERNLOG.md` |
| **Übernahme-Regel** | Nach einem Neustart wird für jeden Baustein des Altstands erst beim Bedarf entschieden, ob er *mitgenommen*, *angepasst* oder *neu gebaut* wird — nie vorab als Liste. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Semester 3 ist ein Neustart desselben Projekts" |
| **Besitz** | Wem eine Figur im Netz gehört. Genau ein Rechner ist Besitzer; nur dort liest ihr Skript die Tastatur (`IsOwner`), alle anderen zeigen an, was ankommt. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Bewegung gehört dem Gast, alles Folgenreiche dem Host" |
| **Autorität** | Wessen Wert im Streitfall gilt. **Nicht dasselbe wie Besitz:** Die Bewegung liegt beim *Besitzer*, Treffer, Beute und Weltzustand beim *Host*. In `NetworkTransform` heißt die Einstellung `Authority Mode`. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Bewegung gehört dem Gast, alles Folgenreiche dem Host" |
| **RPC** | „Remote Procedure Call" — ein Methodenaufruf, dessen Rumpf auf einem **anderen** Rechner ausgeführt wird. In NGO 2.x mit `[Rpc(SendTo.…)]` markiert; der Methodenname muss auf `Rpc` enden. | `Projekte/Isor_Tower/TDD_NOTES.md`, Block „Netzwerk & Multiplayer" |
| **NetworkVariable** | Ein Wert, der sich von selbst über alle Rechner verteilt und einem später Beitretenden **nachgeliefert** wird. **Gegenstück zum RPC:** Ein RPC ist ein Ereignis und verpufft, eine `NetworkVariable` ist ein Zustand und bleibt. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Ein Zähler ist ein Zustand, kein Ereignis" |
| **Fingerabdruck** | Eine Prüfsumme über alle Ergebnisse eines Generierungslaufs. Zwei Läufe mit gleicher Anzahl, aber verschiedenem Fingerabdruck zeigen eine Abweichung an, die niemand sieht — der mittlere von drei Ausgängen des Vergleichstests. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Der Vergleichstest misst Anzahl und Fingerabdruck" |
| **Lobby** | Der Vorraum zwischen Menü und Spielstart. **Ein** Panel für beide Rollen — jeder Rechner zeigt sein eigenes, gefüllt mit dem, was das Netz meldet; was sich unterscheidet, ist der sichtbare Inhalt je Rolle. | `Projekte/Isor_Tower/DECISIONS/UI.md`, „Der Netz-Einstieg ist eine Panel-Kette mit einer Lobby" |

## Über Nummern und Ausgaben

| Begriff | Kurzform | Besitzer |
|---|---|---|
| **Harness-Version** | **Verträglichkeit** des Harness — sagt, ob ein bestehendes Projekt beim Mitziehen umziehen muss. Kein Reifegrad (das ist die Spiel-Version). Steht in `CLAUDE.md`. | `VERSIONIERUNG.md` |
| **V-Nummer** | Vierstellige Commit-Nummer im Titel `Update V 0.0043`; zählt Sessions, nicht jeden Commit — Zwischenstände von Hand tragen freie Titel. Jedes Repo zählt eigenständig. | `VERSIONIERUNG.md` |
| **Auslieferung** | **Vorlage** des Kerns unter `05_Werkzeuge\Harness_Auslieferungen\`, benannt nach der Harness-Version — keine Kopie: Was nur Isor betrifft, wird beim Packen entfernt. | `VERSIONIERUNG.md` |
| **Vorlage** | Zwei Verwendungen, beide meinen „Original zum Kopieren": die Auslieferung als Ganzes (Zeile darüber) und einzeln die Dateien unter `Kern/Vorlagen/`, deren Arbeitskopie in `.claude\` liegt. | `Kern/Vorlagen/README.md` |
| **Marke** | Platzhalter-Name in Großbuchstaben für einen Ort außerhalb des Repos (`DATENBAUM`, `KNOWLEDGE`, `PROJEKT`). Regeldateien nennen die Marke; den Pfad dahinter besitzt allein `PFADE.md`. | `Kern/PFADE.md` |
| **Datenbaum** | Der feste Ablagebaum für alles, was kein Repo ist — Marke `DATENBAUM`. | `IsorBackup/RULES.md` |
| **LFS** | Git Large File Storage — Nebenspeicher für große Dateien: Im Repo liegt ein Zeiger, die Bytes liegen daneben, und ein Clone lädt nur die Stände des Checkouts. | `CODE_GUIDELINES.md`, Repo & Git |
| **Zustand einer Seite** | Lebensabschnitt einer Artifact-Seite, nicht ihre Sorte: `(geplant)` vor dem Bau, `🗑` am Ende. Ändert den **Typ** nicht — der sagt, worauf die Seite blickt. Nicht zu verwechseln mit „Zustand" beim **Befund**, wo das Wort den Gegensatz zum Ereignis meint. | `ARTIFACT_RULES.md`, Die Typen |

Jeder hier geführte Begriff nennt seinen Besitzer. Ob die Liste
**vollständig** ist, kann diese Datei nicht selbst sagen — sie wird von
Hand gepflegt und merkt nicht, dass anderswo ein Begriff entstanden ist.
Dagegen hilft nur, dass die Doku-Pflicht danach fragt (`WORKFLOW.md`).
Beleg: Der Session-Typ „Prüfung" entstand am 2026-08-23 und fehlte hier,
bis ihn die erste Prüfung fand (Befund P10).
