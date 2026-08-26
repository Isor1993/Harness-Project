# _HARNESS_CODE_GUIDELINES.md — Befunde der Prüfung von CODE_GUIDELINES

Ownership: Nur die Befunde **dieses einen Prüfdurchgangs** — der Datei
`Kern/CODE_GUIDELINES.md`, die beim Durchgang vom 2026-08-23
ausdrücklich ausgelassen wurde und seither nie einen Prüfbogen gesehen
hat. Temporär: Was überlebt, ist der Punkt in `Kern/ROADMAP.md`, nicht
diese Liste (`Kern/WORKFLOW.md` → „Prüfung"). Danach ins Archiv.
Format: `### C<Nr> — Titel` mit **Befund** / **Beleg** / **Soll** /
**Auftrag** / **Gewicht**. Gewicht ist `muss` · `lohnt sich` ·
`bei Bedarf`. Behoben wird hier nichts.

Gegenstand: `Kern/CODE_GUIDELINES.md`, 348 Zeilen. Anlass: der Punkt
„Die nie geprüfte Fläche nachholen" in `Kern/ROADMAP.md`, gerettet am
2026-08-26 aus der Befundliste zur Version 1.0.0, bevor sie ins Archiv
ging. Die Uni-Schicht — der zweite Teil derselben Lücke — ist **nicht**
Gegenstand dieses Durchgangs (fremdes Revier, Isor entscheidet).

---

## Durchgang 1 — der Prüfbogen

Die fünf Fragen aus `Kern/WORKFLOW.md` → „Prüfung", plus die Frage für
Listendateien: Die Datei ist keine Liste, trägt aber **zwei
„Offen"-Blöcke**, die wie zurückgestellte Punkte funktionieren — für die
gilt sie sinngemäß.

**Frage 1 — welche Frage beantwortet sie, und beantwortet die sonst
niemand?** „Wie schreiben wir Code?" Kein anderes Dokument beantwortet
das. Sauber: Die Assets-Ordnerstruktur teilt sie sich mit
`Projekte/Isor_Tower/SYSTEME.md`, aber ohne Konflikt — hier steht die
**Regel**, dort der **Bestand**.

**Frage 4 — in welche Schicht gehört sie?** Kern, obwohl Block 1
Uni-Pflicht ist. Der Abschnitt „Priorität" löst das sauber: Die Geltung
leitet sich aus der Existenz eines Ordners `Uni/` ab, statt von Hand
gesetzt zu werden. Eine Auslieferung ins Privatprojekt trägt die
SAE-Regeln mit, wo sie stillgelegt sind — bewusst so gebaut
(`Kern/DECISIONS.md`, 2026-08-22). Kein Befund.

**Frage 5 — verfällt ihr Inhalt?** Ja, und nichts prüft es. Drei der
Befunde unten sind bereits eingetretener Verfall.

### C1 — Die Stand-Zeile ist falsch und dürfte nicht dort stehen
**Befund:** Zeile 6–9 trägt einen Stand-Stempel: „seither in einem
vollen Uni-Durchgang erprobt und mehrfach nachgeschärft (**zuletzt der
Abschnitt „Ordnerstruktur" am 2026-08-22**…)". Beides ist falsch. Die
Datei wurde danach dreimal geändert, und keine dieser Änderungen betraf
die Ordnerstruktur: der Abschnitt „Tests" am 2026-08-25, „Repo & Git"
am 2026-08-26.
**Beleg:** `git log --date=short -- Kern/CODE_GUIDELINES.md` → 2026-08-26,
2026-08-25, 2026-08-23. Die Stand-Zeile nennt den 22.
**Soll:** `Kern/DOC_RULES.md`, Abschnitt 7 ist eindeutig: „Stand-Stempel
nur, wo etwas ihn kontrolliert… Gibt es keine Prüfung, wird kein Datum
hingeschrieben." Für diese Datei gibt es keine. Der Satz „entstanden als
Rohmaterial aus dem Brainstorm vom 2026-07-17" darf bleiben — das ist
Herkunft, kein Stand.
**Auftrag:** Den Halbsatz ab „seither" streichen. Wo die Datei zuletzt
angefasst wurde, sagt `git log` genauer, als eine Hand es je nachführt.
**Gewicht:** muss

### C2 — Die Ownership-Zeile verschweigt ein Fünftel der Datei
**Befund:** Sie lautet „Code-Konventionen — Namen, Architektur,
Ordnerstruktur, Tests, das Review-Gate und die Repo-/Git-Regeln". Der
Block „Kommentare & Datei-Header" (Zeilen 47–112) kommt darin nicht vor
— Datei-Header, Summaries, Inline-Kommentare, Inspector-Felder. Das sind
66 der 348 Zeilen, und es ist der Teil, den Claude bei jedem Review
anwendet.
**Beleg:** Wortvergleich Ownership-Zeile gegen die Abschnittsüberschriften.
Der Fehler vervielfältigt sich: `INDEX.md` erzeugt seine Zeile aus genau
dieser Angabe, die Landkarte ist also ebenso unvollständig.
**Soll:** Die Ownership-Zeile nennt alles, was die Datei besitzt.
**Auftrag:** „Kommentare" in die Aufzählung aufnehmen, danach
`python Kern/Werkzeuge/index_bauen.py --write`.
**Gewicht:** muss

### C3 — Das LFS-Muster ist das nachweislich kaputte
**Befund:** Abschnitt „Repo & Git" nennt als LFS-Regel „das
Unity-Template … plus `*.unity` und **`NavMesh*.asset`**". Genau dieses
Muster hat bei der Migration am 2026-08-26 zu breit gegriffen und die
1-KB-Einstellungsdatei `ProjectSettings/NavMeshAreas.asset` mitgenommen.
Es wurde noch am selben Tag auf `NavMesh-*.asset` geändert — in der
`.gitattributes`, nicht in der Regeldatei.
**Beleg:** `.gitattributes` des Unity-Repos, Zeile 176–179, mit
Kommentar: „The NavMesh pattern needs the dash: bare `NavMesh*` also
caught ProjectSettings/NavMeshAreas.asset". `Kern/ROADMAP.md` beschreibt
die Korrektur ebenfalls — nur die Regel selbst blieb stehen.
**Soll:** Die Regeldatei nennt das Muster, das gilt.
**Auftrag:** `NavMesh*.asset` → `NavMesh-*.asset`, mit dem Grund in
einem Halbsatz, damit niemand den Bindestrich für einen Tippfehler hält.
**Gewicht:** muss

### C4 — Ein „Offen"-Block zeigt auf eine Aufgabe, die es nicht mehr gibt
**Befund:** Der Block „Offen (2026-08-22…)" am Ende der Ordnerstruktur
nennt zwei ungeklärte Ordner — `FolderTemplate/` und `Sandbox/` — und
schließt: „Beides gehört zur Aufgabe `Projekte/Isor_Tower/ROADMAP.md` →
‚Ordnerstruktur im Unity-Projekt gegen die Vorlage prüfen'." Diese
Aufgabe existiert nicht mehr: Die Projekt-ROADMAP wurde am 2026-08-26
für Semester 3 neu geschrieben. Die beiden Ordner sind damit herrenlos.
**Beleg:** `grep "Ordnerstruktur\|FolderTemplate\|Sandbox"` über
`Projekte/Isor_Tower/ROADMAP.md` → kein Treffer. `pruefen.py` findet das
nicht: Prüfung 1 schlägt Dateipfade nach, und die Datei gibt es ja — nur
den Abschnitt nicht.
**Soll:** Entweder die Aufgabe steht wieder irgendwo, oder der
„Offen"-Block sagt, dass sie ersatzlos entfallen ist.
**Auftrag:** Isor entscheidet, ob `FolderTemplate/` und `Sandbox/` noch
geklärt werden sollen. Wenn ja, gehört der Punkt in
`Projekte/Isor_Tower/ROADMAP.md` — fremdes Revier, also melden statt
schreiben.
**Gewicht:** muss

### C5 — Der zweite „Offen"-Block steht in keiner ROADMAP
**Befund:** „Offen (Isor, 2026-08-16)" bei der Member-Reihenfolge: Die
Liste der Unity-Event-Methoden deckt nur ab, was bisher vorkam;
`OnValidate`, `OnTriggerEnter`, `OnCollisionEnter`, `OnApplicationQuit`
fehlen. Der Text sagt „Beim Harness-Ausbau übernehmen und hier als
verbindliche Folge hinterlegen" — das ist ein Auftrag ohne Adressat.
**Beleg:** Suche nach „Event-Methoden", „Order of Execution",
„OnValidate" über alle ROADMAPs und `PLAN.md` → kein Treffer. Der Punkt
wartet seit dem 2026-08-16 an einer Stelle, an der niemand nach Aufgaben
sucht.
**Soll:** Ein zurückgestellter Punkt lebt in der ROADMAP, nicht im
Fließtext einer Regeldatei.
**Auftrag:** Als Punkt nach `Kern/ROADMAP.md` (er betrifft eine
Kern-Datei), im „Offen"-Block nur der Zeiger dorthin. Zugleich der
vierte Fall desselben Musters an einem Tag — siehe Durchgang 2.
**Gewicht:** lohnt sich

### C6 — Das Review-Gate kennt die Ausnahme nicht, die es selbst ausgelöst hat
**Befund:** Punkt 5 des Review-Gate sagt: Steht ein angefasstes Skript
in einer Skripte-Zeile von `ARTIFACT_INDEX.md`, „dann veraltet die Seite
durch die Änderung und **wird nach dem Coden nachgezogen**". Für die
Seite `⚙️ System · Harness` stimmt das seit heute nicht: Ihr Stand hängt
an der Versionsnummer, nachgezogen wird sie **nicht** zwischendurch,
sondern die Abweichung wird gesammelt.
**Beleg:** `Kern/ARTIFACT_INDEX.md` → „Was ohne neue Versionsnummer
passiert", geschrieben am 2026-08-26 in dieser Session, ausgelöst genau
von diesem Gate-Punkt beim Bau von Prüfung 8.
**Soll:** Punkt 5 nennt die Ausnahme oder verweist auf sie.
**Auftrag:** Halbsatz ergänzen. **Offenlegung:** Dieser Widerspruch ist
am 2026-08-26 von der bauenden Session selbst erzeugt worden und hier
ungeschönt notiert — dieselbe Offenlegung wie bei Befund P3 des
Durchgangs zur Version 1.0.0.
**Gewicht:** lohnt sich

---

## Durchgang 2 — Widersprüche quer über den Bestand

Eine Zeile je Art von Information, Spalte „Besitzer" — Widersprüche
liegen *zwischen* Dateien und sind beim Lesen einer einzelnen unsichtbar
(`Kern/WORKFLOW.md` → „Prüfung").

| Information | Besitzer laut Regel | tatsächlich in | Urteil |
|---|---|---|---|
| Sprache von Code und Kommentaren | `DOC_RULES.md`, Abschnitt 9 | **auch** CODE_GUIDELINES, zweimal, in zwei Fassungen | **Konflikt → C7** |
| Namen, Format, Kapselung | CODE_GUIDELINES | dort | sauber |
| Assets-Ordnerstruktur | CODE_GUIDELINES (Regel) | `SYSTEME.md` führt den Bestand | sauber getrennt |
| Review-Gate, Inhalt | CODE_GUIDELINES | `WORKFLOW.md` nennt die fünf Punkte in der Prüfebenen-Tabelle mit | schwach → C9 |
| Review-Gate, Zeitpunkt | `WORKFLOW.md` | dort | sauber |
| Artifact-Check | CODE_GUIDELINES („dort steht er vollständig") | `ARTIFACT_RULES.md` verweist nur | sauber |
| LFS-Begriff | `GLOSSARY.md` → CODE_GUIDELINES | dort | sauber, aber Muster falsch (C3) |
| Repo-Sichtbarkeit | CODE_GUIDELINES (Regel) | `DECISIONS.md` trägt das Warum | sauber |
| Nummern, Build-Ablage | `VERSIONIERUNG.md` | CODE_GUIDELINES verweist | sauber |
| Tests | CODE_GUIDELINES | `WORKFLOW.md` definiert „geprüft" im Baustein | sauber, gegenseitig verwiesen |

### C7 — Die Sprachregel steht dreimal und sagt zweierlei
**Befund:** `Kern/DOC_RULES.md`, Abschnitt 9 erklärt sich selbst zum
Besitzer und verbietet die Kopie ausdrücklich: *„Diese Tabelle ist der
Besitzer. Wo die Sprache anderswo erwähnt wird (**CODE_GUIDELINES**,
WORKFLOW, ASSESSMENT_RULES), steht dort nur ein Verweis."* In
CODE_GUIDELINES steht kein Verweis, sondern zwei ausformulierte
Fassungen — und die zweite widerspricht dem Besitzer:

| Stelle | sagt über Kommentare |
|---|---|
| `DOC_RULES.md`, Abschnitt 9 (**Besitzer**) | „Englisch **oder Deutsch**, aber einheitlich" |
| CODE_GUIDELINES, Block 1, Punkt 1 | „Englisch **oder Deutsch** — aber einheitlich" |
| CODE_GUIDELINES, „Kommentare & Datei-Header" | „**immer Englisch** — keine Ausnahme" |

Die dritte Zeile ist Isors gelebter Standard; sie bezeichnet sich selbst
so und begründet sie. Formal gilt aber die erste, denn sie ist die
Besitzerdatei — **also gilt buchstäblich die Fassung, die niemand
befolgt.**
**Beleg:** Wortlaut der drei Stellen; `DOC_RULES.md` nennt
CODE_GUIDELINES namentlich als Ort, an dem nur ein Verweis stehen darf.
**Soll:** Der Besitzer trägt die geltende Regel — „Englisch" ohne
Alternative —, und CODE_GUIDELINES verweist an beiden Stellen dorthin,
statt sie auszuschreiben. Nicht umgekehrt: Die Verschärfung ist die
Wahrheit, die Tabelle ist zu weich.
**Auftrag:** Zeile „Kommentare im Code" in `DOC_RULES.md` auf „Englisch"
setzen; in CODE_GUIDELINES Block 1 Punkt 1 und den Kopf des
Kommentar-Abschnitts auf Verweise kürzen. **Beides sind Kern-Dateien,
die in jede Auslieferung wandern** — die weiche Fassung reist sonst in
jedes neue Projekt mit.
**Gewicht:** muss

### C8 — Ein Datumsverweis zeigt auf den falschen Tag
**Befund:** In „Unity-Handwerk" steht: „Reine Pipeline-Klassen loggen
ohnehin nicht (**DECISIONS 2026-07-19**)." Am 2026-07-19 gibt es genau
zwei Einträge — „Asset-Ordner: Kategorie + FolderTemplate" und
„Session-Typen: Brainstorm+Design ein Typ". Keiner handelt von Logging.
Die gemeinte Entscheidung steht unter **2026-07-23**,
„Kommentar-Konventionen geschärft", die als Grund die Dozenten-Regel
„keine Debug-Logs im Build" nennt.
**Beleg:** `grep "^## 2026-07-19" Kern/DECISIONS.md` → zwei Treffer, beide
ohne Bezug; Suche nach „Pipeline-Klassen" und „loggen" über
`Kern/DECISIONS.md`, `Kern/_ARCHIV.md` und `Uni/DECISIONS.md` → ein
Treffer, im Eintrag vom 2026-07-23.
**Soll:** Datum richtigstellen.
**Auftrag:** `2026-07-19` → `2026-07-23`. **Bemerkenswert an diesem
Befund ist nicht der Tippfehler, sondern die Lücke:** `pruefen.py`,
Prüfung 1 schlägt Dateipfade nach — ein Verweis auf einen *Eintrag*
innerhalb einer Datei wird von nichts geprüft. Solche Zeiger gibt es im
Bestand reichlich („`DECISIONS.md`, 2026-08-22"), und jeder von ihnen
kann still danebenliegen.
**Gewicht:** lohnt sich

### C9 — Das Review-Gate steht inhaltlich auch in WORKFLOW
**Befund:** Die Prüfebenen-Tabelle in `Kern/WORKFLOW.md` führt das
Review-Gate mit seinen fünf Punkten als Stichworte: „Fattening ·
Enum-Sicherheit · Werkzeugwahl · Naming · Artifact-Bezug". Ändert sich
das Gate, veraltet die Tabelle still.
**Beleg:** Derselbe Mechanismus hat heute zugeschlagen: Prüfung 8 machte
zwei Listen in `WORKFLOW.md` falsch, die `pruefen.py` aufzählen — beide
mussten von Hand nachgezogen werden, kein Werkzeug hat es gemeldet.
**Soll:** Grenzfall, kein klarer Verstoß. `WORKFLOW.md` sagt von sich:
„Dieser Abschnitt besitzt die **Übersicht**, jede Zeile verweist auf
ihren Besitzer" — eine Übersicht darf Stichworte nennen. Der Preis ist
bekannt und wird bewusst gezahlt.
**Auftrag:** Keiner, solange die Tabelle Stichworte trägt und keine
Regeln. Wenn sie je erklärend wird, ist sie eine Kopie.
**Gewicht:** bei Bedarf

---

## Stand

Neun Befunde: `muss` sind C1, C2, C3, C4 und C7 · `lohnt sich` sind C5,
C6 und C8 · `bei Bedarf` ist C9. Behoben ist nichts —
das gehört in einen eigenen Abschnitt, nicht in diese Session
(`Kern/WORKFLOW.md` → „Prüfer und Ausführender sollen nicht dieselbe
Session sein").

**Was auffällt, über die Einzelbefunde hinaus:** Fünf der neun Befunde
sind **Verfall**, nicht Fehler beim Schreiben — die Datei war zum
Zeitpunkt ihrer Entstehung jeweils richtig und ist seither von der
Wirklichkeit überholt worden (C1 Stand-Zeile, C3 LFS-Muster, C4 tote
Aufgabe, C6 neue Ausnahme, C8 verschobene Entscheidung). Genau davor
schützt keine der acht Prüfungen: Sie prüfen Form und Bestand, nicht ob
eine Aussage noch stimmt.

**Nicht Gegenstand dieses Durchgangs:** die Uni-Schicht, der zweite Teil
des ROADMAP-Punktes „Die nie geprüfte Fläche nachholen". Fremdes Revier;
Isor entscheidet, ob und wann.

