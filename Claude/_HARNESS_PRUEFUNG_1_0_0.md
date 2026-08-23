# _HARNESS_PRUEFUNG_1_0_0.md — Befunde der Nachlese zu Version 1.0.0

Ownership: Nur die Befunde **dieses einen Prüfdurchgangs** — der rund
zwanzig Dateien, die am 2026-08-23 beim Bau der Version 1.0.0
geschrieben und nicht gegengelesen wurden. Temporär: Was überlebt, ist
der Punkt in `Kern/ROADMAP.md`, nicht diese Liste
(`Kern/WORKFLOW.md` → „Prüfung"). Danach ins Archiv.
Format: `### P<Nr> — Titel` mit **Datei** / **Befund** / **Soll** /
**Auftrag** / **Gewicht**. Gewicht ist `muss` · `lohnt sich` ·
`bei Bedarf`. Behoben wird hier nichts.

Gegenstand: der Harness. Prüfer: eine frische Session, nicht die
bauende (`WORKFLOW.md` → „Prüfer und Ausführender sollen nicht dieselbe
Session sein").

---

## Durchgang 1 — die vier neuen Regeln

### P1 — Die Übergabe greift
**Datei:** `PLAN.md`, Abschnitt „Für die nächste Session".
**Befund:** Kein Mangel, sondern ein **Beleg**. Eine frische Session
ohne jeden Zuruf kam über `CLAUDE.md` → Leseordnung → `PLAN.md` zum
Auftrag und nannte Typ und Gegenstand von selbst. Der Fall, aus dem die
Regel entstand (Befund A34: die Übergabe stand am Ende einer Bauliste
und wurde nicht gefunden), tritt so nicht mehr auf.
**Soll:** unverändert.
**Auftrag:** keiner. Der Beleg gehört in `Kern/LOG.md`, damit die
Wirksamkeit datiert nachlesbar ist.
**Gewicht:** —

### P2 — „Plan nachziehen" prüft nur den Übergabe-Abschnitt, nicht den Rest
**Datei:** `Kern/WORKFLOW.md` → „Ablauf von `/harness:ende`", Schritt
**Plan nachziehen**.
**Befund:** Die drei Handgriffe lauten: erledigte Punkte abhaken · den
Übergabe-Abschnitt überschreiben · einen vollständig abgehakten Zeitraum
melden. Keiner davon fragt, ob die **stehen gebliebenen** Punkte noch
gelten. Genau das ist am 2026-08-23 passiert: Der Abschnitt „Testphase —
beginnt nach der Prüfung" blieb unberührt stehen, obwohl Isor die
Reihenfolge längst anders entschieden hatte. Gemessen am 2026-08-23: Die
prüfende Session las den Satz vor, als wäre er gültig, und Isor musste
widersprechen. Ein nicht überschriebener Abschnitt sieht genauso
verbindlich aus wie ein frisch geschriebener.
**Soll:** Ein vierter Handgriff, der die stehenden Punkte einmal gegen
den heutigen Stand hält — nicht neu schreiben, nur bestätigen oder
melden. `PLAN.md` ist mit ~100 Zeilen klein genug, dass das nichts
kostet.
**Auftrag:** Handgriff in `WORKFLOW.md` ergänzen; prüfen, ob dieselbe
Lücke bei `/harness:sichern` besteht (dort wird `PLAN.md` gar nicht
angefasst).
**Gewicht:** muss

### P3 — `Kern/ROADMAP.md` widerspricht dem korrigierten `PLAN.md`
**Datei:** `Kern/ROADMAP.md` → „Als Nächstes".
**Befund:** Zwei Punkte, zwei Fehler.
(a) **Widerspruch:** „Testphase beginnen" steht dort ohne Vorbehalt,
während `PLAN.md` und `Kern/DECISIONS.md` seit dem 2026-08-23 sagen: erst
auf Isors Zuruf. Offenlegung: Dieser Widerspruch ist am 2026-08-23 durch
die Korrektur in `PLAN.md` entstanden, also **von der prüfenden Session
selbst erzeugt** und hier ungeschönt notiert.
(b) **Reihenfolge:** „Testphase beginnen" steht **vor** „Nachlese zum Bau
vom 2026-08-23", obwohl die Nachlese zuerst kommt. Die Ownership-Zeile
sagt „Baureihenfolge" — die Reihenfolge trägt also Bedeutung.
**Soll:** Die Testphase trägt den Zuruf-Vorbehalt und steht hinter der
Nachlese.
**Auftrag:** Beide Punkte in `Kern/ROADMAP.md` tauschen und den Vorbehalt
als Halbsatz aufnehmen, mit Verweis auf den DECISIONS-Eintrag.
**Gewicht:** muss

### P4 — Die Anzahl-Regel wird an sechs Stellen gebrochen, vier davon neu
**Datei:** `Kern/DOC_RULES.md` (Abschnitt 7 besitzt die Regel),
gebrochen in `WORKFLOW.md`, `ARTIFACT_RULES.md` und `DOC_RULES.md`
selbst.
**Befund:** Die Regel lautet: keine Anzahl in Überschrift oder
Einleitung, wenn die Liste wachsen kann — erlaubt nur, wenn die
Aufzählung abgeschlossen ist **und der Text sagt, warum**. Sie stammt
aus Befund A4 der Abnahme und brach sich schon damals in der eigenen
Überschrift. Stand heute:

| Stelle | Text | vom |
|---|---|---|
| `WORKFLOW.md` → „Prüfung" | „Prüfbogen … — **fünf Fragen**" | 23.08. |
| `WORKFLOW.md` → `/harness:ende` | „Plan nachziehen, **drei Handgriffe**" | 23.08. |
| `DOC_RULES.md` → Abschnitt 11 | „gelten **vier Handgriffe**" | 23.08. |
| `ARTIFACT_RULES.md` | „### **Zwei** Seiten als Muster" | 23.08. |
| `ARTIFACT_RULES.md` | „### Schrift — **drei** Rollen" | älter |
| `ARTIFACT_RULES.md` | „## Symbole an **zwei** Stellen" | älter |

Keine der sechs sagt, warum nichts dazukommen kann. Bei „Zwei Seiten als
Muster" ist Wachstum sogar erwünscht. Gegenprobe: `DOC_RULES.md` →
„### Die Prüfungen" hat die Zahl weggelassen — es geht also, wenn man
daran denkt.
**Soll:** Entscheidend ist nicht das Nachbessern der sechs Stellen,
sondern die Einsicht aus `DOC_RULES.md` selbst: *„Ein Ausführungsfehler
gehört automatisiert oder ins Format eingebaut, nicht neu geregelt."*
Vier Verstöße an einem einzigen Bautag zeigen, dass die Verhaltensregel
allein nicht trägt.
**Auftrag:** Die sechs Stellen entzahlen oder begründen — und als vierte
Prüfung in `Kern/Werkzeuge/pruefen.py` aufnehmen (ROADMAP-Punkt
„Prüfskripte in den Kern übernehmen"): Zahlwort in Überschrift oder
Fettung melden. In Chroniken, Archiven und Zeugnissen gilt die Regel
nicht — sie werden nie geändert.
**Gewicht:** muss

### P5 — Das Präfix `_HARNESS_` lebt nur im Skript
**Datei:** `Kern/WORKFLOW.md` → „Prüfung" gegen
`Kern/Werkzeuge/index_bauen.py`.
**Befund:** Das INDEX-Skript sortiert jede Datei mit Präfix `_HARNESS_`
in die Kategorie „Temporär". Die Regel dazu sagt nur, die Befundliste
werde „nach dem Anlass benannt" — vom Präfix steht dort nichts. Wer sich
an die Regel hält und die Datei `PRUEFUNG_1_0_0.md` nennt, bekommt sie
vom Skript als reguläre Datei ohne Schicht geführt. Gemessen am
2026-08-23: Die prüfende Session schlug genau diesen Namen vor und
korrigierte ihn erst, nachdem sie zufällig ins Skript sah.
**Soll:** Die Namensregel nennt das Präfix, oder das Skript erkennt
temporäre Dateien an etwas, das in der Regel steht.
**Auftrag:** Einen Satz in `WORKFLOW.md` → „Prüfung": Befundlisten heißen
`_HARNESS_<Anlass>.md` und liegen oben in `Claude\`. Prüfen, ob
`DOC_RULES.md` Abschnitt 8 dieselbe Aussage braucht.
**Gewicht:** lohnt sich

### P6 — Die Ownership-Zeile von `ARTIFACT_RULES.md` wiederholt sich
**Datei:** `Kern/ARTIFACT_RULES.md`, Zeilen 3–4.
**Befund:** Beim Nachtragen des Gestaltungsabschnitts wurde „samt
Farbwelt und Schriftrollen" angehängt, obwohl „Gestaltung" in derselben
Aufzählung schon steht — Farbwelt und Schriftrollen *sind* Gestaltung.
Der Nachtrag hat außerdem den Zeilenumbruch der Datei gesprengt: Zeile 4
läuft über die Breite, an der jede andere Zeile umbricht.
**Soll:** Ownership-Zeile nennt „Gestaltung" einmal; Umbruch wieder bei
~72 Zeichen.
**Auftrag:** Zeile kürzen und neu umbrechen, danach `INDEX.md` neu
erzeugen — die Zeile ist dessen Quelle.
**Gewicht:** lohnt sich

---

## Durchgang 2 — die geretteten Regeln

**Woran geprüft:** die drei archivierten Arbeitsdateien in
`C:\IsorBackup\99_Archiv\_Zu_Loeschen\2026-08-23_Harness_Ueberholung_Arbeitsdateien\`,
Abschnitt für Abschnitt gegen den lebenden Bestand gehalten.

**Ergebnis: die geretteten Regeln sitzen richtig.** Belegt nachgeprüft:
Isors fünf Grenzen (→ `DECISIONS.md`, 2026-08-21) · der Prüfbogen
(→ `WORKFLOW.md`, Prüfung — beim Übertragen sogar richtig entschärft:
aus „Auftrag für die Bau-Session" wurde „für die Session, die es
umsetzt") · Schritt F, die Zuständigkeits-Tabelle (→ `WORKFLOW.md`,
„Widersprüche sind ein eigener Durchgang") · die Rückfrage-Regel E87
(→ beide `CLAUDE.md`) · die fünf DOC_RULES-Nachträge E82–E86 (→ Abschnitte
3, 4, 6, 7 und `ROADMAP.md`) · die Eintragsregel für Störungen
(→ `STOERUNGEN.md`, Kopf) · die draw.io-Exportregel
(→ `DIAGRAM_RULES.md`, schon am 22.08.).

Zwei Dinge sind trotzdem hängen geblieben:

### P7 — Eine achte Regel wurde übersehen
**Datei:** `_HARNESS_REVIEW.md` → „E57 — Umsetzungsliste vor dem Bauen
(Isors Sorge, 2026-08-22)", Punkt 1.
**Befund:** Dort steht verbindlich: *Befunde, Entscheidungen und Belege
werden sofort nach jeder Datei eingetragen — nichts bleibt nur im
Kontext. Bricht eine Session ab, wird dort weitergearbeitet.* Diese
Regel steht in **keiner** lebenden Datei; die Suche nach „sofort" und
„nur im Kontext" über alle Kern-Dateien ist leer. Punkt 2 und 3
derselben Stelle wurden gerettet (Auftrag je Datei, Schritt F), Punkt 1
nicht. Sie war Isors eigene Gegenmaßnahme gegen genau die Gefahr, die
sie beschreibt.
**Soll:** Der Session-Typ Prüfung sagt, dass laufend in die Befundliste
geschrieben wird, nicht am Ende. Ein abgebrochener Kontext darf keine
Befunde kosten.
**Auftrag:** Einen Satz in `WORKFLOW.md` → „Prüfung" aufnehmen. Prüfen,
ob dasselbe für den Typ Zeugnis gilt (`ASSESSMENT_RULES.md`).
**Gewicht:** muss

### P8 — `STOERUNGEN.md` schreibt die Doku-Pflicht ab, und zwar zu eng
**Datei:** `Kern/STOERUNGEN.md`, Kopf („Wer einträgt"), gegen
`Kern/WORKFLOW.md` → „Doku-Pflicht".
**Befund:** Dort steht „zusätzlich fragt `/harness:ende` danach". Nach
der Besitzerdatei ist die Störungs-Frage aber Teil der Doku-Pflicht, die
bei **jedem** Typ gilt und von `/harness:sichern` abgearbeitet wird —
also auch bei `/harness:wechsel`, wo `/sichern` vollständig durchläuft.
Wer nur `STOERUNGEN.md` liest, hält die Frage für eine Sache des
Session-Endes. Zugleich ein Verstoß gegen „Verweis statt Kopie"
(`DOC_RULES.md`, Abschnitt 1, dritte Prüfung): Der Ablauf gehört
`WORKFLOW.md`.
**Soll:** Ein Verweis statt der abgeschriebenen Fassung — „Claude trägt
sofort ein, sobald Isor einen Aussetzer meldet; zusätzlich fragt die
Doku-Pflicht danach (`WORKFLOW.md`)".
**Auftrag:** Zwei Zeilen in `STOERUNGEN.md` umschreiben.
**Gewicht:** lohnt sich

### P9 — Die Arbeitsdateien wurden mit offenen Haken archiviert
**Datei:** `_HARNESS_UMSETZUNG.md`, Zeilen 445–461 (im Archiv).
**Befund:** Drei Punkte stehen dort als `[ ]` offen — darunter
ausgerechnet *„Vor dem Archivieren: die Review-Dateien auf Regeln
durchsuchen, die nur dort leben"*, außerdem die Auslieferung und das
Archivieren selbst. Alle drei sind laut `Kern/LOG.md` erledigt. Der
Haken wurde nicht mehr gesetzt, weil die Datei im selben Zug ins Archiv
ging. Wer später hineinsieht, liest das Gegenteil der Wahrheit — und ein
Archiv wird nach eigener Regel nie aufgeräumt, der Fehler ist also
dauerhaft. Spiegelbild der Störung *„Haken gesetzt, Arbeit nicht getan"*
vom 2026-08-22, diesmal andersherum.
**Soll:** Eine Arbeitsdatei wird geschlossen, bevor sie archiviert wird:
letzte Haken setzen oder den Rest ausdrücklich als „nicht gemacht"
markieren.
**Auftrag:** Halbsatz zur Archivierungsregel in `DOC_RULES.md`
Abschnitt 11 („Wenn Inhalt umzieht"), Handgriff 4. Die drei Haken im
Archiv **nicht** nachtragen — dort wird nichts geändert; stattdessen
gehört dieser Befund als Beleg in `STOERUNGEN.md`.
**Gewicht:** lohnt sich

---

## Durchgang 3 — Widersprüche quer über den Bestand

Eine Zeile je Art von Information, Spalte „Besitzer", über alles, was am
2026-08-23 berührt wurde. Drei Treffer, alle in derselben Datei — und
alle drei sind **Widersprüche zwischen zwei lebenden Dateien**, die beim
Lesen einer einzelnen unsichtbar bleiben.

### P10 — Das Glossar kennt den fünften Session-Typ nicht
**Datei:** `Kern/GLOSSARY.md`, Zeile „Typ".
**Befund:** Dort steht „Brainstorm/Design, Development, Zeugnis, (Art)".
Der am 2026-08-23 eingeführte Typ **Prüfung** fehlt — also gerade der,
unter dem dieser Durchgang läuft. Der Schlusssatz der Datei behauptet
zusätzlich Vollständigkeit („Alle Begriffe haben einen Besitzer").
**Soll:** Fünf Typen, und der Schlusssatz ohne Vollständigkeitszusage
(oder mit Begründung, warum sie hält).
**Auftrag:** Zeile ergänzen, Schlusssatz prüfen.
**Gewicht:** muss

### P11 — Das Glossar sagt bei „Chronik" das Gegenteil der Regel
**Datei:** `Kern/GLOSSARY.md`, Zeile „Chronik", gegen `DOC_RULES.md`
Abschnitt 4.
**Befund:** Die Kurzform lautet „Wird nur **hinten** ergänzt". Die
Besitzerdatei sagt seit dem 2026-08-22 ausdrücklich das Gegenteil:
*„Ergänzt wird nach Datum, nicht hinten angehängt."* Das war Befund A28
der Abnahme, entstanden aus drei echten Fällen. Die Schärfung wurde in
`DOC_RULES.md` eingebaut, aber nicht in die Kurzform gezogen — und wer
das Glossar liest, bekommt genau die Fassung, die A28 abgestellt hat.
**Soll:** Kurzform folgt der Besitzerdatei.
**Auftrag:** Zeile richtigstellen.
**Gewicht:** muss

### P12 — Das Glossar nennt die Auslieferung eine Kopie
**Datei:** `Kern/GLOSSARY.md`, Zeile „Auslieferung", gegen
`Kern/DECISIONS.md` → „Eine Auslieferung ist eine Vorlage, keine Kopie"
(2026-08-23) und `Kern/VERSIONIERUNG.md`.
**Befund:** Die Kurzform sagt „**Kopie** des Kerns". Der
Entscheidungseintrag vom selben Tag heißt wörtlich „ist eine Vorlage,
keine Kopie" — der Unterschied ist der ganze Inhalt der Entscheidung
(Zeugnisse, ARTIFACT_INDEX-Einträge und `index_geplant.txt` werden
entfernt).
**Soll:** Kurzform folgt der Besitzerdatei.
**Auftrag:** Zeile richtigstellen.
**Gewicht:** muss

### P13 — Ursache der drei: Das Glossar steht in keiner Doku-Pflicht
**Datei:** `Kern/WORKFLOW.md` → „Doku-Pflicht", Punkt 3.
**Befund:** Die Doku-Pflicht verlangt „**INDEX** nachziehen, falls
Dateien dazukamen oder wegfielen" — vom `GLOSSARY.md` steht dort nichts.
Der INDEX wird erzeugt und kann deshalb gar nicht veralten; das Glossar
wird von Hand gepflegt und ist nach eigener Einordnung ein
**Verzeichnis**, das laut `DOC_RULES.md` Abschnitt 4 „laufend abgeglichen
werden muss, sonst führt es in die Irre". Genau das ist eingetreten: drei
falsche Zeilen aus zwei Bautagen. Die Automatik schützt die Datei, die
sie nicht braucht, und die ungeschützte verfällt.
**Soll:** Entweder ein vierter Punkt in der Doku-Pflicht („ist ein
Begriff dazugekommen oder hat sich eine Definition geändert?"), oder —
besser, weil es dem eigenen Grundsatz folgt, dass Ausführungsfehler
automatisiert gehören — eine Prüfung in `pruefen.py`: Jede Glossar-Zeile
nennt ihren Besitzer; das Skript kann melden, wenn die Besitzerdatei seit
dem letzten Abgleich geändert wurde.
**Auftrag:** Entscheiden, welcher der beiden Wege. Der zweite ist der
Punkt „Prüfskripte in den Kern übernehmen" in `Kern/ROADMAP.md`.
**Gewicht:** muss

### P14 — Die Temporär-Überschrift des INDEX ist an die Überholung gebunden
**Datei:** `Kern/Werkzeuge/index_bauen.py`, Abschnittstitel; sichtbar in
`INDEX.md`.
**Befund:** Der erzeugte Abschnitt heißt „Temporär — werden **nach der
Überholung** archiviert". Die Überholung ist am 2026-08-23 abgeschlossen;
temporäre Dateien wird es weiter geben, denn jede Prüfung bringt eine
Befundliste hervor. Aufgefallen beim Neuerzeugen des INDEX in dieser
Session — die frisch angelegte Befundliste landete korrekt in der
Kategorie, unter einer Überschrift, die von einem beendeten Vorgang
spricht.
**Soll:** Ein Titel, der die Sorte benennt statt den Anlass, etwa
„Temporär — je Durchgang, danach ins Archiv".
**Auftrag:** Eine Zeile im Skript ändern, INDEX neu erzeugen.
**Gewicht:** bei Bedarf

---

## Stand

Vierzehn Befunde, davon acht `muss`, vier `lohnt sich`, einer `bei
Bedarf`, einer ist ein Beleg ohne Auftrag (P1). Nicht geprüft und offen für einen späteren
Durchgang: `ARTIFACT_INDEX.md` gegen die tatsächlich veröffentlichten
Seiten (das ist Sache des Pflegetags), `CODE_GUIDELINES.md` und die
Uni-Schicht — beide am 2026-08-23 nicht angefasst.

**Nächster Schritt:** ein eigener Abschnitt, der behebt. Nicht diese
Session (`WORKFLOW.md` → „Prüfer und Ausführender sollen nicht dieselbe
Session sein").

---

## Behebung (2026-08-23, eigener Abschnitt, Typ Development)

Alle vierzehn behoben. Je Befund die Stelle, an der die Änderung steht —
nachprüfbar, nicht bloß abgehakt:

| Befund | steht jetzt in |
|---|---|
| P1 | kein Auftrag; Beleg ist im `Kern/LOG.md` eingetragen |
| P2 | `WORKFLOW.md` → `/harness:ende`, Schritt „Plan nachziehen": zweiter Spiegelstrich, die stehenden Punkte gegen den Stand halten |
| P3 | `Kern/ROADMAP.md`: Testphase steht hinter der Behebung, trägt den Zuruf-Vorbehalt und den Verweis auf die DECISIONS |
| P4 | acht Stellen entzahlt — `WORKFLOW.md` (Prüfbogen, Plan nachziehen), `DOC_RULES.md` Abschnitt 11, `ARTIFACT_RULES.md` (Muster-Seiten, Schriftrollen, Symbol-Abschnitt, Kategorie-Farben), `GLOSSARY.md` (Doku-Pflicht) |
| P5 | `WORKFLOW.md` → „Prüfung": Befundlisten heißen `_HARNESS_<Anlass>.md`, mit dem Grund (das INDEX-Skript erkennt daran „temporär") |
| P6 | `ARTIFACT_RULES.md`, Ownership-Zeile gekürzt und neu umbrochen |
| P7 | `WORKFLOW.md` → „Prüfung": geschrieben wird laufend, nicht am Ende |
| P8 | `STOERUNGEN.md`, Kopf: Verweis auf die Doku-Pflicht statt abgeschriebener Fassung |
| P9 | `DOC_RULES.md` Abschnitt 11, neuer Handgriff „Eine Arbeitsdatei wird geschlossen, bevor sie geht" |
| P10 | `GLOSSARY.md`: Typ-Zeile um „Prüfung" ergänzt, eigene Zeile für den Begriff, Schlusssatz ohne Vollständigkeitszusage |
| P11 | `GLOSSARY.md`, Zeile „Chronik": nach Datum einsortiert, nicht hinten angehängt |
| P12 | `GLOSSARY.md`, Zeile „Auslieferung": Vorlage statt Kopie |
| P13 | `WORKFLOW.md` → „Doku-Pflicht", neuer Punkt „Glossar-Frage" |
| P14 | `Kern/Werkzeuge/index_bauen.py`, Abschnittstitel; INDEX neu erzeugt |

**Zwei Aufträge sind bewusst nur halb erledigt.** Die Textkorrekturen zu
P4 und P13 stehen, die dazugehörige **Automatisierung** nicht — sie
gehört ins geplante `Kern/Werkzeuge/pruefen.py` und ist dort als Punkt
aufgenommen (`Kern/ROADMAP.md` → „Prüfskripte in den Kern übernehmen").
Solange das Skript fehlt, hängen beide Regeln wieder am Erinnern, und
genau daran sind sie schon einmal gescheitert.

**Gegenprobe nach der Behebung:** Suchlauf über alle Überschriften der
Kern-Dateien nach Zahlwörtern — verbleibende Treffer nur in
`DECISIONS.md` (datierte Chronik, dort gilt die Regel nicht) und in
dieser Liste selbst (temporär, und die Zahlen beschreiben einen
abgeschlossenen Durchgang). INDEX neu erzeugt: 45 Dateien, alle mit
Ownership-Zeile.

**Diese Liste ist damit archivierbar** — Ziel nach `DOC_RULES.md`
Abschnitt 11: `99_Archiv\_Zu_Loeschen\<Datum>_Pruefung_1_0_0\`. Vorher
schließen, nicht offen ins Archiv geben (P9).
