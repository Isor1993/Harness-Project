# STOERUNGEN.md — Was im Betrieb nicht funktioniert hat

Ownership: Nur Vorfälle, in denen der Harness nicht so gearbeitet hat wie
vorgesehen — was passiert ist und welche Regel nicht gegriffen hat.
Das LOG besitzt „was ist passiert", diese Datei „was ist schiefgegangen".
Keine Aufgaben (das ist die ROADMAP), keine Begründungen (DECISIONS).
Format: `### JJJJ-MM-TT — Kurztitel` mit den Zeilen **Was**, **Ursache**,
**Regel** und **Stand**. Der Stand ist entweder `offen` oder
`behoben <Datum>` samt der Stelle, an der die Behebung steht. So ist die
Liste der offenen Vorfälle ein Suchlauf nach `Stand: offen` statt eine
Zählarbeit — bei der am 2026-08-22 dreimal verschieden gezählt wurde.

Warum die Datei existiert: Die Überholung von 2026-08-21/22 war nur
möglich, weil elf konkrete Befunde vorlagen. Ohne Belege wird die nächste
Revision Ratearbeit. Behobene Vorfälle bleiben stehen — sie sind der
Beleg, dass die Änderung nötig war. Diese Datei ist eine Chronik und
braucht daher kein Archiv.

Wer einträgt: Claude, sobald Isor einen Aussetzer meldet — zusätzlich
fragt die Doku-Pflicht danach, damit es nicht ausfällt. Wann das ist,
besitzt `WORKFLOW.md`: bei jedem Typ, also auch beim Wechsel und beim
Sichern mitten in der Session, nicht erst am Ende.

---

### 2026-08-21 — Ownership-Befund ohne Gegenprüfung
**Was:** Claude meldete, `ROADMAP.md` verletze ihre eigene
Ownership-Regel, weil sie einen „Erledigt"-Block enthält.
**Ursache:** Tatsächlich war es ein Widerspruch **zwischen** ROADMAP und
FEATURE_LOG — beide Dateien schickten das Thema zur jeweils anderen.
Claude hatte nur eine der beiden Ownership-Zeilen gelesen, bevor er
urteilte.
**Regel:** Fehlte. Neu in DOC_RULES: Vor einem Ownership-Befund die
`Ownership:`-Zeile **aller beteiligten Dateien** lesen.
**Stand:** behoben 2026-08-22 mit DOC_RULES Abschnitt 1.

### 2026-08-21 — Angekündigte Fragen nicht gestellt
**Was:** Claude kündigte einen Fragenblock an und beendete den Zug, ohne
ihn zu stellen. Isor musste nachfragen.
**Ursache:** Reiner Ausführungsfehler, keine fehlende Regel.
**Regel:** —
**Stand:** offen. Beobachten, ob es sich wiederholt.

### 2026-08-22 — Kopfvorlage im Trennskript nicht je Datei angepasst
**Was:** Die sieben neuen Projekt-Entscheidungsdateien trugen alle den Titel
`# DECISIONS.md`, obwohl sie `Audio.md`, `Gras.md` und so weiter heißen.
**Ursache:** Die Kopfvorlage im Skript war fest verdrahtet; nur der
Beschreibungstext wurde je Datei eingesetzt, die Titelzeile nicht.
**Regel:** Fehlte. Aufgefallen erst bei der Gesamtprüfung auf tote Verweise —
also durch eine Prüfung, die nicht nach diesem Fehler suchte.
**Stand:** behoben 2026-08-22, im selben Durchgang.

### 2026-08-22 — Sicherung schloss zunächst `.git` aus
**Was:** Das Backup-Skript hätte die Repos ohne Versionsgeschichte gesichert
— 1.222 statt 2.127 Dateien. Eine Kopie der Arbeitsdateien ohne Historie ist
kein Repo.
**Ursache:** `.git` stand in derselben Ausschlussliste wie `Library`, `Temp`
und `obj`, die Unity beim nächsten Öffnen neu baut. Der Unterschied wurde
nicht bedacht.
**Regel:** Neu, jetzt im Skript vermerkt und als Wissensseite
`Knowledge/Werkzeuge/was-eine-sicherung-wertlos-macht.md`: Wer etwas
ausschließt, prüft, ob das Ziel danach seinen Zweck noch erfüllt.
**Stand:** behoben 2026-08-22, vor dem ersten echten Lauf.

### 2026-08-22 — Haken gesetzt, Arbeit nicht getan
**Was:** In `_HARNESS_UMSETZUNG.md` war unter Phase 4 abgehakt: „Eintrag
für `⚙️ System · Harness` vorbereiten (E35, I12)". In `ARTIFACT_INDEX.md`
kommt das Wort „Harness" nicht ein einziges Mal vor. Der Haken war falsch.
**Ursache:** Die Bauliste prüft sich selbst nicht. Ein Haken belegt, dass
jemand ihn gesetzt hat — nicht, dass die Datei sich geändert hat. Bei 60
Handgriffen an einem Tag fällt eine Auslassung niemandem auf.
**Regel:** Fehlte. Kandidat für den Schlussdurchgang: Wer eine Bauliste
abhakt, nennt beim Abhaken die geänderte Datei — dann ist der Haken
nachprüfbar statt nur behauptet.
**Stand:** behoben 2026-08-22 — der Eintrag steht in `Kern/ARTIFACT_INDEX.md`,
Abschnitt „⚙️ System — Schicht: Kern (der Harness selbst)". Die Seite
selbst wird nach der Abnahme gebaut.

### 2026-08-22 — Berechtigungsliste wächst aus sich selbst nach
**Was:** Unmittelbar nach dem Eindampfen von 314 auf 51 Einträge standen
zwei neue drin — der volle Wortlaut zweier `mv`- und `mkdir`-Aufrufe mit
Archivpfad, die nie wieder vorkommen.
**Ursache:** „Dauerhaft erlauben" hängt den kompletten Befehlstext an die
Liste, nicht ein Muster. So sind die 314 entstanden.
**Regel:** Fehlte. Bei einmaligen Befehlen „nur diesmal" wählen; dauerhaft
nur, wenn der Befehl als Muster taugt. Sonst wächst die Liste in Wochen
wieder auf ihren alten Stand.
**Stand:** offen — die zwei Einträge sind am 2026-08-22 entfernt, die
Ursache bleibt: Sie liegt in der Bedienung, nicht in der Datei.

### 2026-08-22 — Typ des Abschnitts nie erfragt
**Was:** Beim ersten Lauf von `/harness:sichern` war der Typ des
laufenden Abschnitts unbekannt. Die ganze Session über war nie gesagt
worden, ob gerade Design oder Development läuft — und der Typ entscheidet,
welche Dateien geschrieben werden.
**Ursache:** WORKFLOW verlangt am Session-Anfang nur die **Modus**-Frage.
Der Typ wird ausschließlich beim `/harness:wechsel` abgefragt. Wer eine
Session ohne Wechsel durchzieht, wird nie danach gefragt.
**Regel:** Fehlte. Neu in `WORKFLOW.md`, Abschnitt „Typ, Modus und
Regler": Die Startfrage lautet „Typ und Modus", nicht nur „Modus" —
beide hängen am Abschnitt und werden ohnehin gemeinsam gebraucht.
**Stand:** behoben 2026-08-22, in derselben Session, in der es auffiel.

### 2026-08-22 — Regel überlebte nur zufällig in einer Erledigt-Liste
**Was:** Die Regel „beim draw.io-Export *Include a copy of my diagram*
angehakt lassen" stand als Zusatz an einem **abgehakten** Punkt in
`C:\IsorBackup\README.md`. Beim Kürzen des README auf einen Wegweiser
wäre sie ersatzlos verschwunden. Genau diese Option hatte am 2026-08-06
fünf Diagramme gerettet.
**Ursache:** Beim Abhaken schreibt man gern dazu, was man gelernt hat —
„erledigt, ab jetzt immer X". Das „ab jetzt" ist eine Regel und stand
damit im denkbar falschesten Dokument: einer Liste, die nach dem Abhaken
niemand mehr liest.
**Regel:** Fehlte. Neu als Wissensseite
`Knowledge/Dokumentation/regeln-versauern-in-erledigt-listen.md`: Steht
in der Erledigt-Notiz ein „ab jetzt", „immer" oder „nie wieder", ist es
eine Regel und gehört in die Regeldatei ihres Themas.
**Stand:** behoben 2026-08-22, die Regel steht in `Kern/DIAGRAM_RULES.md`.
Ob daraus zusätzlich eine Harness-Regel wird, entscheidet die Abnahme.

### 2026-08-22 — Befund geurteilt, bevor die beteiligte Datei gelesen war
**Was:** Die Abnahme hielt in Befund A21 fest, der Haken „vier fehlende
Aufgabentexte nachtragen" sei falsch **und** die Arbeit damit verloren.
Der Haken ist tatsächlich falsch — die Tragweite nicht: `Uni/ROADMAP.md`
führt den Punkt ausführlich und begründet als offen. Aufgefallen erst im
sechsten Durchgang, als die Uni-Schicht gelesen wurde; im selben Zug
korrigiert.
**Ursache:** Geurteilt wurde allein aus der Bauliste heraus, ohne die
ROADMAP der betroffenen Schicht zu prüfen. `DOC_RULES.md` Abschnitt 1
verlangt genau das — aber dem Wortlaut nach nur „vor einem
**Ownership**-Befund". Ein Befund über eine nicht getane Arbeit fällt
nicht darunter, obwohl derselbe Fehler droht.
**Regel:** Vorhanden, aber zu eng gefasst. Vorschlag: die Regel „vor
einem Befund die beteiligten Dateien **aller** Schichten lesen" von
Ownership-Befunden auf alle Befunde ausweiten.
**Stand:** behoben 2026-08-22 — `DOC_RULES.md` Abschnitt 1 sagt jetzt
„vor einem Befund", nicht mehr nur „vor einem Ownership-Befund".

### 2026-08-22 — Auswahl vorgelegt, wo ein Vorschlag hingehört
**Was:** Beim letzten offenen Befund der Abnahme (A29, Abgrenzung der
sieben Entscheidungsdateien) legte Claude drei Grenzfälle als Frage vor,
statt sie zu entscheiden. Isor musste mit „Was soll ich jetzt machen?"
nachfragen.
**Ursache:** Die Regel steht in `CLAUDE.md` und im Notkern —
„Rückfrage an der Weggabelung, Empfehlung im Detail". Wohin eine
Entscheidung abgelegt wird, ist ein Detail: Es führt nicht zu
unterschiedlicher Arbeit, nur zu einem anderen Dateinamen. Claude hat die
Grenze zwischen beiden falsch gezogen, weil es um Projektwissen ging —
aber ein begründeter Vorschlag wäre auch dort möglich gewesen, und er kam
danach in einem Satz.
**Regel:** Vorhanden und ausreichend. Der Fehler lag in der Anwendung,
nicht in der Formulierung. Merkmal für den Wiederholungsfall: Wenn beide
Antworten dieselbe Arbeit nach sich ziehen, ist es ein Detail.
**Stand:** offen. Beobachten, ob es sich wiederholt — wie beim Eintrag
vom 2026-08-21 oben.

### 2026-08-23 — Überholten Planabschnitt als gültig vorgelesen
**Was:** Beim Session-Start gab Claude den Stand aus `PLAN.md` wieder und
nannte darin die Testphase („danach `C:\IsorBackup` aufräumen") als
Nächstes. Isor musste widersprechen: Er hatte längst entschieden, dass
zuerst der Harness fertig wird und die Testphase erst auf seinen Zuruf
beginnt.
**Ursache:** Der Abschnitt stand unverändert in `PLAN.md`, weil
`/harness:ende` nur den Übergabe-Abschnitt überschreibt. Die drei
Handgriffe unter „Plan nachziehen" prüfen die **stehen gebliebenen**
Punkte nicht — ein alter Abschnitt sieht danach genauso verbindlich aus
wie ein frisch geschriebener. Claude hat ihn nicht gegen den Stand
gehalten, sondern vorgelesen.
**Regel:** Lücke. Vorschlag: ein vierter Handgriff in `WORKFLOW.md` →
„Ablauf von `/harness:ende`", der die stehenden Punkte einmal bestätigt
oder meldet. Ausführlich als Befund **P2** in
`_HARNESS_PRUEFUNG_1_0_0.md`.
**Stand:** offen. `PLAN.md` und `Kern/DECISIONS.md` sind am selben Tag
richtiggestellt; die Regel selbst ist unverändert.

### 2026-08-23 — Befundliste lag außerhalb des Repos
**Was:** Eine Parallel-Session prüfte die acht Altbestand-Artifacts gegen
Code und veröffentlichte Seiten und schrieb 540 Zeilen Befunde in ihren
**Scratchpad** — sessiongebunden, nicht versioniert, in keinem Register.
Die Arbeit hing an einem Temp-Ordner.
**Ursache:** Regel-Lücke. `WORKFLOW.md` sagte zur Befundliste nur „nach
dem Anlass benannt" und nannte keinen Ablageort. Die Session hielt ihre
Liste folgerichtig für eine private Arbeitsunterlage. Dieselbe Lücke
wurde am selben Tag unabhängig in der Harness-Prüfung gefunden (Befunde
P5 und P7) — zwei Sessions, die voneinander nichts wussten, stolperten
über denselben Stein.
**Regel:** Fehlte, steht jetzt: Befundlisten heißen `_HARNESS_<Anlass>.md`
und liegen im Repo; geschrieben wird laufend, nichts bleibt nur im
Kontext (`WORKFLOW.md` → „Prüfung").
**Stand:** behoben 2026-08-23 — Regel ergänzt, die Datei unverändert nach
`Claude\_HARNESS_ARTIFACTS_1_0_0.md` übernommen und im INDEX geführt.

### 2026-08-23 — Der Pflegetag fand drei von rund dreißig
**Was:** Der erste Pflegetag meldete **drei** Artifact-Funde. Eine
Parallel-Session fand am selben Tag auf denselben acht Seiten rund
**dreißig**, darunter ein Skript, das es nie gab (`PauseMenuController`),
sämtliche Dateipfade einer Seite und ein Widerspruch zweier Seiten über
die Zellgröße um den Faktor vier.
**Ursache:** Der Sonntagsabgleich prüft den `ARTIFACT_INDEX` gegen die
Änderungen der Woche und gegen die Veröffentlichungsliste — also
**Metadaten**. Ob die Aussagen einer Seite noch stimmen, sieht er nicht;
dazu müsste die Seite abgerufen und gegen den Code gehalten werden. Der
Harness verlässt sich aber auf ihn: `ARTIFACT_RULES.md` erlaubt den
Stand-Stempel auf Seiten ausdrücklich deshalb, weil „der
Sonntagsabgleich ihn kontrolliert".
**Regel:** Vorhanden, aber zu schwach für das, was auf ihr aufbaut.
Vorschlag: Der Pflegetag nimmt sich **eine** Seite je Woche inhaltlich
vor, statt alle oberflächlich. Aufgabe steht in `Kern/ROADMAP.md`.
**Stand:** behoben 2026-08-25 — der Pflegetag prüft zusätzlich genau
eine Seite je Woche gründlich, dran ist die mit dem ältesten Stand
(`ARTIFACT_RULES.md` → „Wann geschaut wird"; `WORKFLOW.md` → Pflegetag).

### 2026-08-23 — Aus dem Session-Titel auf den Typ geschlossen
**Was:** Claude meldete als Störung, eine Parallel-Session sei unter dem
falschen Typ gelaufen. Einziger Beleg war ihr Titel „Design", während
inhaltlich eine Prüfung stattfand. Isor widersprach: Die Titel vergibt
**er**, sie sind frei gewählt und tragen keine Typ-Information. Der
Eintrag war nicht gedeckt und wurde durch diesen ersetzt.
**Ursache:** Aus einem Etikett geurteilt, statt die Quelle zu lesen. Vom
Transkript lagen nur die letzten Nachrichten vor, der Session-Anfang mit
der Typ-Frage war nicht darunter — beurteilt wurde trotzdem.
`DOC_RULES.md` Abschnitt 1 verlangt seit dem 2026-08-22 ausdrücklich das
Gegenteil, und zwar für **jede** Art von Befund.
**Regel:** Vorhanden und ausreichend, der Fehler lag in der Anwendung.
Zweiter Fall derselben Sorte an einem Tag — der erste war der
vorgelesene Planabschnitt oben.
**Stand:** offen. Der eigentliche Fund dahinter ist kein Fehlverhalten,
sondern eine Lücke: **Typ und Modus sind nirgends sichtbar** — weder
während der Session noch hinterher. Als Aufgabe in `Kern/ROADMAP.md`.

### 2026-08-23 — Befehlsdateien mit einem BOM zerschossen
**Was:** Claude schrieb die zehn Befehlsdateien beim Pfad-Umbau mit
`Set-Content -Encoding UTF8` zurück. PowerShell 5.1 setzt dabei eine
Byte-Order-Mark an den Dateianfang. Das BOM stand damit **vor** dem
`---` des Frontmatter; die Beschreibungen der Befehle fielen aus und
standen im Menü nur noch als `---`. Aufgefallen, weil die Skill-Liste im
selben Zug ihre Beschreibungen verlor.
**Ursache:** Werkzeugwahl. `Set-Content -Encoding UTF8` heißt in
PowerShell 5.1 „UTF-8 **mit** BOM"; die Variante ohne BOM gibt es dort
nur über `[System.IO.File]::WriteAllText` mit einer eigenen
`UTF8Encoding($false)`. Dazu kam `-NoNewline`, das die abschließende
Leerzeile fraß.
**Regel:** Fehlte. `CODE_GUIDELINES.md` regelt Code, nicht das Schreiben
von Dateien mit Frontmatter. Kurzfassung bis dahin: Für jede Datei, die
maschinell gelesen wird, nie `Set-Content -Encoding UTF8` — und nach
einem Schreibvorgang die ersten Bytes prüfen, nicht nur den Text.
**Stand:** behoben 2026-08-23, gleiche Session. Alle zehn Dateien auf
UTF-8 ohne BOM zurückgeschrieben, erste Bytes einzeln nachgezählt
(`239,187,191` vorher, `45,45,45` nachher), Beschreibungen wieder da.

### 2026-08-23 — Typ und Modus nicht gefragt, sondern übernommen
**Was:** Beim Start des Development-Abschnitts fragte Claude weder nach
Typ noch nach Modus. Den **Typ** übernahm er aus dem Vorschlag in
`PLAN.md` und stellte ihn als feststehend hin, den **Modus** ließ er ganz
aus und leitete ihn aus einer Erinnerung ab. Gefragt wurden nur der
Gegenstand und der Regler Visualisierung. Isor hat es bemerkt und
nachgetragen verlangt.
**Ursache:** Die Übergabe in `PLAN.md` nannte den Typ bereits („Typ
Development — Gegenstand: …"). Ein **Vorschlag** der vorigen Session
wurde damit wie eine getroffene Entscheidung behandelt. `WORKFLOW.md`
verlangt die Frage aber am Anfang jeder Session und bei jedem Typ, gerade
weil beide am Abschnitt hängen und nicht an der Übergabe. Beim Regler
fiel es nicht auf, weil dort tatsächlich gefragt wurde — die Teilfrage
verdeckte die fehlende Hauptfrage.
**Regel:** Vorhanden und ausreichend (`WORKFLOW.md` → „Typ, Modus und
Regler"), der Fehler lag in der Anwendung. **Zweiter Vorfall dieser
Sorte:** Der erste ist der Eintrag vom 2026-08-22 „Typ des Abschnitts nie
erfragt", aus dem die Regel überhaupt entstanden ist. Damals fehlte sie,
diesmal wurde sie übergangen.
**Stand:** offen. Zu beobachten, ob ein in der Übergabe vorgeschlagener
Typ die Frage regelmäßig verdrängt — dann liegt die Lücke im Format des
Abschnitts „Für die nächste Session", der einen Vorschlag heute nicht von
einer Festlegung unterscheidet.

### 2026-08-23 — Das Prüfwerkzeug scheiterte an seinem eigenen Fund
**Was:** `pruefen.py` brach mit einem `UnicodeEncodeError` ab, sobald
Prüfung 5 einen Fund meldete, der ein `→` enthielt. Der Abbruch kam
**nach** den ersten beiden Meldungen: Sie waren gedruckt, der dritte
Fund und das Gesamtergebnis gingen verloren.
**Ursache:** Die Windows-Konsole steht auf cp1252. Python schreibt
`sys.stdout` in dieser Codepage, und der Pfeil hat dort kein Zeichen.
Der Fehler steckte seit dem Bau des Skripts am 2026-08-23 darin und
wurde nie ausgelöst, weil bis dahin kein Fund einen Pfeil enthielt — die
Meldung mit dem Pfeil entsteht nur, wenn das Glossar gegengelesen werden
muss.
**Regel:** Fehlte. Ein Prüfwerkzeug darf an der Ausgabe seines eigenen
Ergebnisses nicht scheitern — gerade dann nicht, wenn es etwas gefunden
hat. Der Fehlerfall ist der Normalfall, für den es gebaut ist.
**Stand:** behoben 2026-08-23 in `Kern/Werkzeuge/pruefen.py`, direkt
nach den Imports: `sys.stdout.reconfigure(encoding="utf-8",
errors="replace")`. Nebenwirkung zum Guten — die Umlaute in der Ausgabe
stimmen seither ebenfalls.

### 2026-08-25 — Session-Thema beim Klammer-Setzen überschrieben
**Was:** Beim Setzen der Typ-Klammer schrieb Claude den ganzen
Session-Titel neu und ersetzte dabei Isors Thema „Harness · Kern-Punkte"
durch ein eigenes. Bemerkt nur, weil die Werkzeug-Rückmeldung den alten
Titel nannte; im nächsten Zug zurückgesetzt, die Klammer korrekt.
**Ursache:** Das Umbenennen-Werkzeug kann den eigenen Titel nur
überschreiben, nicht vorher lesen — die Sitzungsliste schließt die
eigene Session aus. Die Regel „das Thema gehört Isor, Claude ändert
daran kein Wort" (`WORKFLOW.md` → „Der Typ steht im Session-Titel") ist
damit blind auszuführen: Wer die Klammer setzt, muss raten, was er
stehen lässt.
**Regel:** Vorhanden, aber ohne Lese-Werkzeug nicht sicher befolgbar.
Gegenmittel: Die Rückmeldung des Umbenennens nennt den alten Titel —
nach jedem Setzen gegenprüfen und ein überschriebenes Thema sofort
wiederherstellen.
**Stand:** offen — der Werkzeug-Mangel bleibt; das Gegenmittel hat im
selben Vorfall funktioniert.

### 2026-08-26 — In die fremde Schicht geschrieben statt gemeldet
**Was:** Die Repo/Git-Session (Revier: Kern) schrieb zwei Einträge in
`Projekte/Isor_Tower/` — einen LOG-Eintrag zur Repo-Hygiene und den
Punkt „Portfolio-Präsentation" in die ROADMAP. Zeitgleich arbeitete
eine Parallel-Session an genau dieser Schicht und schrieb ihre ROADMAP
**vollständig neu**. Der Eintrag überlebte nur, weil sie ihn bemerkte
und ausdrücklich übernahm.
**Ursache:** Ausführungsfehler, keine Regellücke. Die Revier-Regel
(`WORKFLOW.md` → „Parallele Sessions") verlangt seit dem 2026-08-25
„melden statt schreiben", wenn die Arbeit eine fremde Schicht braucht.
Sie wurde nicht angewandt, weil der Gegenstand — die drei Repos —
über alle Schichten läuft und der Schreibweg dadurch naheliegend
wirkte. Genau dafür ist die Regel aber da: Das Thema greift über die
Schichten, das **Revier** folgt trotzdem dem Fokus des Abschnitts.
**Regel:** Vorhanden und ausreichend, erster scharfer Test bestanden
hat sie nicht. Merkmal für den Wiederholungsfall: Wenn eine Datei
außerhalb der eigenen Schicht liegt, ist die Frage nicht „passt der
Inhalt dorthin", sondern „ist es mein Revier".
**Stand:** offen. Beobachten, ob der schichtübergreifende Gegenstand
regelmäßig zum Schreiben verführt — dann fehlt in der Regel ein Satz
für genau diesen Fall.
**Zum Nachbareintrag:** „Zwei Sessions wollten dieselbe Datei
schreiben" (unten, gleicher Tag) beschreibt **denselben** Zusammenstoß
von der anderen Seite und urteilt milder — „beide Sessions handelten
für sich richtig". Das trifft auf die Projekt-Session zu: Sie schrieb
in ihr eigenes Revier und konnte nicht wissen, dass jemand von außen
hineinschreibt. Für **diese** Seite gilt es nicht: Die Regel hängt am
eigenen Fokus, nicht am Wissen über die Nachbarsession, und war damit
ohne jede Sichtbarkeit befolgbar. Beide Einträge bleiben stehen — eine
Chronik wird nicht geändert —, aber wer nur einen liest, bekommt den
Vorfall halb.

### 2026-08-26 — Zwei Sessions wollten dieselbe Datei schreiben
**Was:** Die Design-Session „Isor's Tower · Multiplayer" wollte
`Projekte/Isor_Tower/ROADMAP.md` leeren und neu schreiben. Zwischen dem
Lesen und dem Schreiben hatte eine Parallel-Session dort den Punkt
„Portfolio-Präsentation" ergänzt. Das Schreiben schlug fehl, weil das
Werkzeug den veränderten Dateistand bemerkte; der fremde Punkt wurde
danach gelesen und in den neuen Plan übernommen.
**Ursache:** Die Revier-Regel (`WORKFLOW.md` → „Parallele Sessions", seit
2026-08-25) weist Schichten zu, aber nichts zeigt einer Session, welches
Revier gerade belegt ist. Beide Sessions handelten für sich richtig: Die
eine hatte die Projekt-Schicht als Fokus, die andere trug das Ergebnis
ihrer Repo/Git-Entscheidung dorthin ein, wo es hingehört. Ohne
Sichtbarkeit ist die Regel nicht befolgbar, sondern nur einhaltbar, wenn
man zufällig weiß, was nebenan läuft.
**Regel:** Vorhanden, aber ohne Anzeige nicht durchsetzbar — dieselbe
Sorte Lücke wie beim Session-Titel am 2026-08-25. Was gerettet hat, war
kein Regelwerk, sondern das Werkzeug: Ein Schreibversuch auf einen
veränderten Stand wird abgewiesen. Kandidat als bewusste Gegenmaßnahme:
Vor dem Ersetzen einer ganzen Datei wird sie unmittelbar davor erneut
gelesen, nicht nur zu Beginn des Abschnitts.
**Stand:** offen. Der Zusammenstoß selbst ist aufgelöst — der fremde
Punkt steht unverändert in der neuen `ROADMAP.md`, im Abschnitt „Nach dem
Prototyp", mit Herkunftsvermerk.

### 2026-08-26 — „Später, nur bei Bedarf" ist ein blinder Fleck
**Was:** In `Kern/ROADMAP.md` stand unter „Später, nur bei Bedarf" der
Punkt „Knowledge-Archivierung automatisieren." — eine Zeile ohne das
„was und warum", das die ROADMAP im eigenen Kopf vorschreibt. Er stammt
vom 2026-07-14 und meinte das Auslagern aus einer projektinternen
Pufferdatei; diese Architektur wurde am 2026-07-17 verworfen. Der Punkt
war damit **sechs Wochen lang gegenstandslos** und überlebte dabei den
Umbau auf 1.0.0, den auf 2.0.0 und die Prüfung vom 2026-08-23, die
vierzehn Befunde fand und die ROADMAP ausdrücklich zum Gegenstand hatte
(Befund P3 betraf sie). Im selben Abschnitt stand die unprüfbare
Bedingung „wieder prüfen, wenn er sicher programmiert" — dieselbe
Bauart, die am 2026-08-23 bei der Testphase erkannt und repariert wurde,
hier dreizehn Tage länger unbemerkt.
**Ursache:** Die Überschrift wirkt wie ein Häkchen. „Später, nur bei
Bedarf" sagt dem Auge „nicht jetzt", und der Blick springt weiter — die
Zeilen darunter werden zwar mitgelesen, aber nicht mehr geprüft. Keine
Prüfebene deckt den Abschnitt ab: `pruefen.py` sieht Form und Bestand,
nicht ob ein Punkt noch ein Objekt hat; der Pflegetag sieht Artifacts;
der Prüfbogen des Typs Prüfung fragt je **Datei**, nicht je Abschnitt,
und eine ROADMAP besteht die Fragen 1 bis 5 als Ganzes, während eine
einzelne tote Zeile darin durchrutscht.
**Regel:** Lücke, keine Missachtung. `DOC_RULES.md` Abschnitt 7 bekämpft
Verfall über Anzahlen und Stand-Stempel, hat aber nichts für einen Punkt,
dessen **Voraussetzung** weggefallen ist. Kandidat als Gegenmaßnahme:
Der Prüfbogen bekommt eine sechste Frage für Listendateien — *steht jeder
zurückgestellte Punkt noch auf einer Grundlage, die es gibt?* Nicht
maschinell prüfbar; ein Skript sieht die verworfene Architektur nicht.
**Stand:** offen als Bauart. Der konkrete Punkt ist am 2026-08-26
erledigt: archiviert in `Kern/_ARCHIV.md`, ersetzt durch Prüfung 8, und
die unprüfbare Bedingung bei „ClaudeSetup" ist auf Zuruf umgestellt.

### 2026-08-26 — Session-Thema überschrieben, Wiederholungsfall
**Was:** Beim Setzen der Klammer zu Beginn dieser Session hieß der Titel
`Harness · Repo/Git (zu)`; Claude machte daraus
`Harness · Restpunkte (Design)` und änderte damit **das Thema**, nicht
nur die Klammer. `WORKFLOW.md` → „Der Typ steht im Session-Titel" sagt:
„Das Thema gehört Isor — er benennt die Session, und Claude ändert daran
kein Wort." Aufgefallen ist es Claude selbst, später am Tag, beim
Durchgehen der offenen Störungen auf Isors Frage hin; Isor hatte nicht
widersprochen.
**Ursache:** Der Titel war von der vorigen Session geerbt und trug die
Klammer `(zu)` — also der Anzeigezustand „abgeschlossen". Claude las das
als „kein gültiges Thema" und setzte ein neues. Diese Auslegung ist
nirgends gedeckt: Die Regel kennt nur „Thema gehört Isor" und „fehlt
eine Klammer, hängt Claude sie an, ohne den Rest anzufassen" — der Fall
„Klammer da, aber von gestern" kommt darin nicht vor.
**Regel:** Lücke plus Ausführungsfehler. Der Buchstabe war eindeutig und
wurde gebrochen; zugleich beantwortet die Regel den geerbten Titel nicht.
Dieselbe Sorte wie am 2026-08-25 („Session-Thema beim Klammer-Setzen
überschrieben"), nur aus anderem Anlass — dort ein Werkzeug ohne
Vorschau, hier eine eigene Auslegung. Der richtige Handgriff wäre
gewesen, das neue Thema **vorzuschlagen** statt es zu setzen; Claude hat
den alten Titel immerhin gemeldet, weil das Werkzeug ihn zurückgibt —
genau das Gegenmittel aus dem Eintrag vom 2026-08-25, das hier den
Nachweis überhaupt erst möglich machte.
**Stand:** offen. Das Thema `Harness · Restpunkte` steht und ist von
Isor nicht beanstandet, der Regelfall bleibt ungeklärt.

### 2026-08-26 — Niemand fragt, ob eine temporäre Liste überfällig ist
**Was:** `_HARNESS_PRUEFUNG_1_0_0.md` lag vom 2026-08-23 bis zum
2026-08-26 in der Repo-Wurzel, obwohl sie sich im eigenen Schlusssatz
für archivierbar erklärte („Diese Liste ist damit archivierbar") und
alle vierzehn Befunde behoben waren. In diesen drei Tagen liefen
mehrere Sessions samt SessionStart-Hook über den Bestand; jede zählte
die Datei brav als eine von 56 mit. Aufgefallen ist es erst, als Isor
ausdrücklich fragte, ob am Harness alles fertig sei.
**Ursache:** Eine temporäre Datei ist die einzige Gattung im Bestand,
die **planmäßig wieder verschwindet** — und keine Prüfebene kennt diesen
Lebenslauf. `pruefen.py` prüft ihre Form und lässt sie bei den Prüfungen
1, 4 und 7 bewusst aus; `index_bauen.py` sortiert sie korrekt in die
Kategorie „Temporär"; beide fragen nicht, ob ihr Durchgang durch ist.
Der Zustand steht nur im Fließtext der Datei selbst, und dorthin sieht
niemand, der nicht gerade mit ihr arbeitet. Verwandt mit „Später, nur
bei Bedarf ist ein blinder Fleck" (oben, gleicher Tag), aber eine eigene
Mechanik: Dort wird eine Zeile übersehen, hier eine ganze Datei, die
sich sogar selbst für erledigt erklärt hat.
**Regel:** Lücke. `Kern/WORKFLOW.md` → „Prüfung" sagt „danach ins
Archiv", nennt aber kein „danach", das jemand feststellt — dieselbe
Bauart wie bei den unprüfbaren Bedingungen vom selben Tag. Gegenmittel,
als ROADMAP-Punkt aufgenommen (`Kern/ROADMAP.md`): `pruefen.py` meldet
als **Hinweis**, dass eine `_HARNESS_*.md` in der Wurzel liegt, samt der
Frage, ob ihr Durchgang abgeschlossen ist. Bewusst ein Hinweis und kein
Fund — während einer laufenden Prüfung gehört die Datei dorthin, ein
Fund wäre dann Rauschen.
**Stand:** offen als Bauart; der konkrete Fall ist am 2026-08-26
erledigt (archiviert, Eintrag in `Kern/_ARCHIV.md`).
