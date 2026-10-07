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
| **Pflegetag** | Wochentakt, unabhängig vom Session-Typ: Artifacts durchsehen und gegen die veröffentlichten Seiten abgleichen, dazu **höchstens eine** Seite gründlich gegen Code und Quelle — eine nie geprüfte oder eine, deren Quelle sich seit der letzten Prüfung geändert hat; sonst nichts zu tun. Ausgelöst durch `/harness:sonntag`. | `WORKFLOW.md`, Pflegetag |
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
| **Stack-Entscheidung** | Die Festlegung vom 2026-09-07: Unreal Engine + C++ als ein Stack für Studium, Isor's Tower und Beruf — mit dokumentiertem Rückweg. Kontrollpunkt seit dem 2026-10-01 vorgezogen: Engine-Entscheidung spätestens So 02.11.2026 nach eigenem Hands-on; eine Stack-Entscheidung pro Portfolio-Spiel. | `Uni/DECISIONS.md`, „2026-09-07 — Engine- und Sprachfokus" und „2026-10-01 — Engine-Kontrollpunkt vorgezogen" |
| **Frontloading** | Grundsatz der Semester-3-Roadmap: Jede Abgabe soll vor dem Termin und vor dem zugehörigen Unterricht fertig sein; verplant werden 24 Stunden je Woche, der Überschuss ist Crunch-Reserve. | `Uni/DECISIONS.md`, „2026-09-08 — Semester-3-Roadmap: Frontloading mit 24-Stunden-Wochen" |
| **Fertig-vor-fällig** | Grundsatz des Phasenplans seit dem 2026-09-14: Jede Phase endet mit einem **Fertig-Ziel** vor dem Abgabetermin — das Fertig-Ziel ist der Feature-Stopp, der Puffer ist eingebaut; der Plan trägt nur Fertig-Ziele und Abgabetermine, Projekt-Meilensteine kommen je Phase beim Start dazu. | `Uni/DECISIONS.md`, „2026-09-14 — Fertig-vor-fällig: Phasenplan an den echten Abgabeterminen" |
| **Besitz** | Wem eine Figur im Netz gehört. Genau ein Rechner ist Besitzer; nur dort liest ihr Skript die Tastatur (`IsOwner`), alle anderen zeigen an, was ankommt. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Bewegung gehört dem Gast, alles Folgenreiche dem Host" |
| **Autorität** | Wessen Wert im Streitfall gilt. **Nicht dasselbe wie Besitz:** Die Bewegung liegt beim *Besitzer*, Treffer, Beute und Weltzustand beim *Host*. In `NetworkTransform` heißt die Einstellung `Authority Mode`. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Bewegung gehört dem Gast, alles Folgenreiche dem Host" |
| **RPC** | „Remote Procedure Call" — ein Methodenaufruf, dessen Rumpf auf einem **anderen** Rechner ausgeführt wird. In NGO 2.x mit `[Rpc(SendTo.…)]` oder klassisch mit `[ServerRpc]`/`[ClientRpc]` markiert — im Projekt sind beide in Gebrauch; der Methodenname muss auf das jeweilige Attribut-Suffix enden. | `Projekte/Isor_Tower/TDD_NOTES.md`, Block „Netzwerk & Multiplayer" |
| **NetworkVariable** | Ein Wert, der sich von selbst über alle Rechner verteilt und einem später Beitretenden **nachgeliefert** wird. **Gegenstück zum RPC:** Ein RPC ist ein Ereignis und verpufft, eine `NetworkVariable` ist ein Zustand und bleibt. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Ein Zähler ist ein Zustand, kein Ereignis" |
| **Fingerabdruck** | Eine Prüfsumme über alle Ergebnisse eines Generierungslaufs. Zwei Läufe mit gleicher Anzahl, aber verschiedenem Fingerabdruck zeigen eine Abweichung an, die niemand sieht — der mittlere von drei Ausgängen des Vergleichstests. | `Projekte/Isor_Tower/DECISIONS/Multiplayer.md`, „Der Vergleichstest misst Anzahl und Fingerabdruck" |
| **Lobby** | Der Vorraum zwischen Menü und Spielstart. **Ein** Panel für beide Rollen — jeder Rechner zeigt sein eigenes, gefüllt mit dem, was das Netz meldet; was sich unterscheidet, ist der sichtbare Inhalt je Rolle. | `Projekte/Isor_Tower/DECISIONS/UI.md`, „Der Netz-Einstieg ist eine Panel-Kette mit einer Lobby" |
| **Szene** | **Zwei Bedeutungen, die auseinanderzuhalten sind.** In Unity: eine Asset-Datei mit Objekten (Isor's Tower). Im Lane Defender: ein Zustand des Konsolen-Zustandsautomaten — eine Funktion, die einen Bildschirm besitzt (Hauptmenü, Spiel, Endszene), keine Datei. | `Projekte/Lane_Defender/DECISIONS.md`, „M1-Ablauf: Szenen-Zustandsautomat mit sechs Stationen" |
| **Zustandsautomat** | Das Programm-Gerüst des Lane Defender: ein enum-Zustand plus Schleife in `main` rufen je Zustand die passende Szenen-Funktion auf; jede Szene meldet die nächste als Rückgabewert, `main` weist zu — Szenenwechsel heißt Zustand umstellen. | `Projekte/Lane_Defender/DECISIONS.md`, „Szenen melden die nächste Szene (Melde-Muster)" |
| **Ein-Puffer-Rendering** | Je Tick wird der komplette Bildschirm als **ein** String gebaut und nach Cursor-Home mit einem einzigen `cout` gesendet — überschreiben statt löschen, gegen Flackern und halbe Zustände. | `Projekte/Lane_Defender/DECISIONS.md`, „Tick-Modell: Rundensimulation, Eingabe nur zwischen Wellen" |
| **Gelieferter Baustein** | Codeteil, den Claude fertig liefert, statt Isor ihn tippen zu lassen (Konsolen-Init, Einzeltasten-Abfrage). Kein Freibrief: Er wird gemeinsam abgenommen, und Isor muss ihn erklären und verteidigen können. | `Projekte/Lane_Defender/DECISIONS.md`, „Umschwenk auf den Lane-Shooter: Lane Defender" |
| **Zeichen-Schleife** | Eingabe-Schleife, die jede Taste einzeln über ReadKey verarbeitet, statt Zeilen zu lesen — eine Taste pro Runde im Home-Frame-Muster; das Programm echot, prüft und färbt selbst. Gegenstück zur modalen Zeileneingabe (getline). | `Projekte/Lane_Defender/DECISIONS.md`, „2026-09-19 — Eingabe selbst gezeichnet — löst den getline-Beschluss ab" |
| **Balance-Datei** | Die eine zentrale Code-Datei des Lane Defender nur für Tuning-Werte — Leben, Gold, Preise, Intervalle, Boss-Werte, ab M6 die Level-Tabelle. Layout- und Technik-Konstanten bleiben bewusst in ihren Dateien: schmal geschnitten, kein God-Header. | `Projekte/Lane_Defender/DECISIONS.md`, „2026-09-30 — Balance-Datei: schmal, nur Tuning-Werte" |
| **RAII** | „Resource Acquisition Is Initialization": Eine Klasse holt ihre Ressource im Konstruktor und gibt sie im Destruktor zurück — aufgeräumt wird beim Objekt-Tod von selbst, keine Stelle im Programm muss daran denken. Im Model-Viewer der Schnitt der vier GPU-Besitzer-Klassen. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-04 — Programmaufbau: sieben Module, GPU-Besitz nach RAII" |
| **Uniform** | Wert, den das C++-Programm dem Shader je Bild übergibt (Matrizen, Lichtrichtung, Farbe) — für alle Ecken und Pixel desselben Zeichenaufrufs gleich, daher der Name. Gegenstück zu den je Ecke wechselnden Vertex-Daten. Seit V3 in Gebrauch: die drei Matrizen über `SetMat4`, das Sampler-Fach über `SetInt`. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-04 — Programmaufbau: sieben Module, GPU-Besitz nach RAII" |
| **Tiefenpuffer** | Je Pixel merkt sich die GPU neben der Farbe eine Entfernung; gemalt wird nur, was näher ist — das Gegenmittel zum Maler-Problem „wer zuletzt malt, gewinnt". Gehört eingeschaltet **und** je Frame mitgewischt. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-07 — Tiefenpuffer ab der ersten 3D-Geometrie" |
| **UV** | Bildkoordinaten von 0 bis 1 nach dem Weltkarten-Prinzip: u läuft rundherum, v von unten nach oben; `texture(sampler, uv)` schlägt die Farbe an dieser Stelle nach. Je Ecke gespeichert (Steckdose 2), dazwischen mischt die GPU. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-07 — Vertex-Layout: 8 Floats je Ecke von Anfang an" |
| **Grundhelligkeit** | Untergrenze der Beleuchtung („Ambient"): Auch die sonnenabgewandte Seite bleibt sichtbar — der Pauschal-Ersatz für das indirekte Licht (Himmel, Abpraller), das Echtzeit nicht rechnet. Im Viewer als kühler Schatten-Tint im mix-Anschlag des Toon-frag. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-07 — Stylized-Toon: weiche Kante statt harter Stufen" |
| **Cubemap** | Textur aus sechs gleich großen Quadraten als Würfel-Innenseiten; nachgeschlagen wird per 3D-Richtung statt UV (`samplerCube`). Sind die Gesichter nicht exakt gleich groß und gleich formatiert, ist sie **unvollständig** und liefert für jede Richtung Schwarz. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-07 — Skybox: eine GPU-Ressource, Würfel als CMesh, xyww-Tiefe" |
| **Z-Fighting** | Flackern, wenn zwei Flächen um denselben Tiefenwert streiten — je Pixel gewinnt mal die eine, mal die andere. Medizin ist ein kleiner Abstand: Der Kontakt-Schatten liegt deshalb bei −0.99 statt auf der Bodenhöhe −1. | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-07 — Sonnen-Gizmo und Kontakt-Schatten über einen Unlit-Shader" |
| **Unlit-Shader** | Das kleinste Shaderpaar: MVP durchreichen, eine flache Farbe raus — keine Normalen, kein Licht. Für Dinge, die selbst leuchten oder reine Markierung sind (Sonnenscheibe, Schatten-Fleck). | `Projekte/Model_Viewer/DECISIONS.md`, „2026-10-07 — Sonnen-Gizmo und Kontakt-Schatten über einen Unlit-Shader" |

## Über Nummern und Ausgaben

| Begriff | Kurzform | Besitzer |
|---|---|---|
| **Harness-Version** | **Verträglichkeit** des Harness — sagt, ob ein bestehendes Projekt beim Mitziehen umziehen muss. Kein Reifegrad (das ist die Spiel-Version). Steht in `CLAUDE.md`. | `VERSIONIERUNG.md` |
| **V-Nummer** | Vierstellige Commit-Nummer im Titel `Update V 0.0043`; zählt Sessions, nicht jeden Commit — Zwischenstände von Hand tragen freie Titel. Jedes Repo zählt eigenständig. | `VERSIONIERUNG.md` |
| **Auslieferung** | **Vorlage** des Kerns unter `05_Werkzeuge\Harness_Auslieferungen\`, benannt nach der Harness-Version — keine Kopie: Was nur Isor betrifft, wird beim Packen entfernt. | `VERSIONIERUNG.md` |
| **Vorlage** | Zwei Verwendungen, beide meinen „Original zum Kopieren": die Auslieferung als Ganzes (Zeile darüber) und einzeln die Dateien unter `Kern/Vorlagen/`, deren Arbeitskopie in `.claude\` liegt. | `Kern/Vorlagen/README.md` |
| **Marke** | Platzhalter-Name in Großbuchstaben für einen Ort außerhalb des Repos (z. B. `DATENBAUM`, `KNOWLEDGE`, `PROJEKT_UNREAL`). Regeldateien nennen die Marke; den Pfad dahinter besitzt allein `PFADE.md`. | `Kern/PFADE.md` |
| **Datenbaum** | Der feste Ablagebaum für alles, was kein Repo ist — Marke `DATENBAUM`. | `IsorBackup/RULES.md` |
| **LFS** | Git Large File Storage — Nebenspeicher für große Dateien: Im Repo liegt ein Zeiger, die Bytes liegen daneben, und ein Clone lädt nur die Stände des Checkouts. | `CODE_GUIDELINES.md`, Repo & Git |
| **Zustand einer Seite** | Lebensabschnitt einer Artifact-Seite, nicht ihre Sorte: `(geplant)` vor dem Bau, `🗑` am Ende. Ändert den **Typ** nicht — der sagt, worauf die Seite blickt. Nicht zu verwechseln mit „Zustand" beim **Befund**, wo das Wort den Gegensatz zum Ereignis meint. | `ARTIFACT_RULES.md`, Die Typen |
| **Systems Hungarian** | Typkürzel vor dem Namen (`i`, `f`, `b`, `p`, `C` …), in der SAE-C++-Konvention kombiniert mit den Rollen-Präfixen `m_`/`a_` — `m_iNumb`, `bIsValid`. Gilt in Konsolenprojekt und Model-Viewer durchgängig, wie in den SAE-Beispielen. | `CODE_GUIDELINES.md`, C++ · Konsolenprojekt |
| **Epic C++ Coding Standard** | Epics verbindliche C++-Konvention für alles im Unreal-Repo — vorgegeben, nicht gewählt; Typ-Präfixe nach Vererbung (`U`/`A`/`F`/`E`/`I`/`T`, `b` für bool). Das Arbeitsdestillat steht noch aus. | `CODE_GUIDELINES.md`, C++ · Unreal |
| **Fab** | Epics Marketplace für Unreal-Assets. „Holen" heißt dort claimen: Einmal Geclaimtes bleibt dauerhaft in der Account-Bibliothek, heruntergeladen wird erst bei Bedarf. | `Projekte/Isor_Tower/ROADMAP.md`, „Unreal-Grundausstattung über Fab" |

Jeder hier geführte Begriff nennt seinen Besitzer. Ob die Liste
**vollständig** ist, kann diese Datei nicht selbst sagen — sie wird von
Hand gepflegt und merkt nicht, dass anderswo ein Begriff entstanden ist.
Dagegen hilft nur, dass die Doku-Pflicht danach fragt (`WORKFLOW.md`).
Beleg: Der Session-Typ „Prüfung" entstand am 2026-08-23 und fehlte hier,
bis ihn die erste Prüfung fand (Befund P10).
