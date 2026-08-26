# _HARNESS_UNI_SCHICHT.md — Befunde der Prüfung der Uni-Schicht

Ownership: Nur die Befunde **dieses einen Prüfdurchgangs** — der
Uni-Schicht, die beim Durchgang vom 2026-08-23 ausdrücklich ausgelassen
wurde und seither nie einen Prüfbogen gesehen hat. Temporär: Was
überlebt, ist der Punkt in der ROADMAP, nicht diese Liste
(`Kern/WORKFLOW.md` → „Prüfung"). Danach ins Archiv.
Format: `### U<Nr> — Titel` mit **Befund** / **Beleg** / **Soll** /
**Auftrag** / **Gewicht**. Gewicht ist `muss` · `lohnt sich` ·
`bei Bedarf`. Behoben wird hier nichts.

Gegenstand: `Uni/`, zwölf Dateien, 1.663 Zeilen. Zweite Hälfte des
Punktes „Die nie geprüfte Fläche nachholen"; die erste
(`Kern/CODE_GUIDELINES.md`) steht in `_HARNESS_CODE_GUIDELINES.md`.

**Revier:** Die Uni-Schicht ist nicht das Revier dieses Abschnitts
(Fokus: Kern). Gelesen wurde deshalb alles, geschrieben nur diese
Befundliste — was in `Uni/ROADMAP.md` und `Uni/LOG.md` gehörte, ist
unten unter „Zu melden" aufgeführt und wartet auf Isors Freigabe
(`Kern/WORKFLOW.md` → „Parallele Sessions").

---

## Was geprüft wurde, und wie tief

| Datei | Zeilen | Tiefe |
|---|---|---|
| `Uni/DOCX_RULES.md` | 122 | voller Prüfbogen — echte Regeldatei |
| `Uni/ROADMAP.md` | 30 | voller Prüfbogen plus die Frage für Listendateien |
| `Uni/DECISIONS.md` | 314 | Einordnung und Gegenprobe zu DOCX_RULES; Chronik, wird nie geändert |
| `Uni/LOG.md` | 66 | Einordnung; Chronik |
| `Uni/_ARCHIV.md` | 497 | Einordnung; Archiv, wird nie aufgeräumt |
| 7 × `Semester_2/ASSIGNMENT_*.md` | 654 | nur Einordnung — Originaltexte der Uni, inhaltlich nicht zu bewerten |

Die Chroniken und das Archiv sind **sauber**: Ownership-Zeilen decken
sich mit dem Inhalt, Format und Datumsfolge prüft `pruefen.py` laufend
(Prüfung 2, 0 Funde). Die sieben Aufgabentexte tragen jeweils die
Ansage „unverändert lassen; eigene Planung gehört in die DECISIONS der
Schicht" — richtige Einordnung, kein Befund. Alle sechs Befunde unten
stammen aus den zwei echten Regeldateien.

---

## Durchgang 1 — der Prüfbogen

### U1 — Die Ownership-Zeile schickt den TDD-Inhalt an den falschen Ort
**Befund:** `Uni/DOCX_RULES.md`, Kopf: „**Was im TDD steht, gehört in
`Uni/ROADMAP.md` und `Uni/LOG.md`**; warum es so steht, in
`Uni/DECISIONS.md`." Das ist die übliche Abgrenzungsformel — sie sagt,
wohin der Inhalt gehört, der *nicht* dieser Datei gehört. Nur stimmt das
Ziel nicht: Eine ROADMAP trägt Aufgaben, ein LOG Ereignisse; der
**Inhalt** des TDD gehört in keine von beiden. Seit dem 2026-08-25 hat
er einen echten Besitzer — `Projekte/Isor_Tower/TDD.md`, laut INDEX „das
Markdown-Manuskript des TDD, die führende Quelle". Die Zeile stammt aus
der Zeit davor und wurde bei E61b nicht mitgezogen.
**Beleg:** `INDEX.md`, Zeile 103. Dieselbe Datei sagt zwölf Zeilen
weiter unten schon das Richtige: „Seit 2026-08-25 führt das Markdown
(E61b): Der *Text* lebt in `Projekte/Isor_Tower/TDD.md`." Die
Ownership-Zeile widerspricht damit dem eigenen Fließtext.
**Soll:** Die Zeile nennt `Projekte/Isor_Tower/TDD.md` als Ort des
Inhalts; ROADMAP und LOG bleiben für Aufgaben und Ereignisse.
**Auftrag:** Ownership-Zeile umschreiben, danach
`python Kern/Werkzeuge/index_bauen.py --write` — der INDEX erbt sie.
**Gewicht:** muss

### U2 — Prüfschritt 1 verlangt einen Lauf, der planmäßig rot ist
**Befund:** Der Abschnitt „Prüfung" schreibt als **ersten** Schritt nach
jedem Eingriff vor: „`validate.py` aus dem docx-Skill laufen lassen".
Der Abschnitt „Werkzeuge" derselben Datei sagt dagegen, dass genau
dieses Skript bei **Pandoc-gebauten** Dateien systematisch fehlschlägt —
„88 Fehlalarme bei einer korrekten Datei", weil Pandoc Medien per
Override deklariert. Und seit E61b baut Pandoc jede Abgabefassung. Die
Warnung wurde am 2026-08-25 eingetragen, die Prüfliste blieb stehen.
**Beleg:** Wortlaut beider Abschnitte in derselben Datei;
`Kern/Werkzeuge/abgabe_bauen.py` baut den Fließtext per Pandoc
(`Kern/ROADMAP.md`, Punkt E61b).
**Soll:** Ein erster Prüfschritt, der im Normalfall grün ist — sonst
gewöhnt man sich das Wegklicken an, und ein Prüfer, dessen Meldungen man
wegklickt, ist wertlos. Entweder rückt `validate.py` hinter den
Sichttest, oder der Schritt sagt ausdrücklich, welche Meldungsart bei
Pandoc-Dateien erwartet und zu ignorieren ist.
**Auftrag:** Isor entscheidet die Reihenfolge; die Begründung steht
bereits im Werkzeug-Abschnitt und muss nur an den Prüfschritt gezogen
werden.
**Gewicht:** muss

### U3 — Ein Pfad ohne seine Marke
**Befund:** „Arbeitsdatei ist ausschließlich
`01_Uni\Semester_2\Arbeitsdateien\TDD Softwareplanung.docx`" — der Pfad
nennt die Marke nicht, zu der er gehört. Erst achtzig Zeilen später,
bei den Formatvorgaben, steht „(`Kern/PFADE.md` → `DATENBAUM`)". Wer
oben einsteigt, weiß nicht, worauf `01_Uni\` sich bezieht.
**Beleg:** `Kern/PFADE.md`, Regel „Regeldateien nennen die Marke und
verweisen hierher". `pruefen.py`, Prüfung 7 findet das **nicht**: Sie
sucht Pfade mit Laufwerksbuchstaben, und dieser hat keinen — dieselbe
Art Lücke wie bei Befund C8 der Schwesterliste.
**Soll:** Beim ersten Pfad der Datei steht die Marke.
**Auftrag:** „(`Kern/PFADE.md` → `DATENBAUM`)" beim ersten Vorkommen
ergänzen.
**Gewicht:** lohnt sich

### U4 — Eine Überschrift mit Verfallsdatum
**Befund:** `Uni/ROADMAP.md` trägt die Überschrift „## Semester 3
(**beginnt in rund zwei Wochen, Stand 2026-08-22**)". Das ist eine
relative Zeitangabe plus Stand-Stempel, beides in einer Überschrift.
Am 2026-08-26 ist die Angabe noch nicht falsch, wird es aber
zwangsläufig — und niemand prüft sie.
**Beleg:** `Kern/DOC_RULES.md`, Abschnitt 7: „Stand-Stempel nur, wo
etwas ihn kontrolliert… Gibt es keine Prüfung, wird kein Datum
hingeschrieben." Für diese Überschrift gibt es keine.
**Soll:** Entweder das absolute Startdatum, sobald es feststeht, oder
schlicht „## Semester 3". Der Zeitpunkt gehört ohnehin in `PLAN.md` —
die ROADMAP sagt selbst im Kopf: „Was gerade dran ist, steht in
`PLAN.md`."
**Auftrag:** Klammer aus der Überschrift entfernen; wenn der
Semesterstart terminiert ist, das Datum in `PLAN.md`.
**Gewicht:** lohnt sich

### U5 — „Abgeschlossenes" gehört nicht ins Archiv
**Befund:** `Uni/ROADMAP.md`, Ownership-Zeile: „…was passiert ist, in
`Uni/LOG.md`; **Abgeschlossenes in `Uni/_ARCHIV.md`**." Das widerspricht
der Definition eines Archivs. Abgeschlossene Punkte werden **abgehakt
und bleiben stehen** — archiviert wird, was **überholt** ist.
**Beleg:** `Kern/GLOSSARY.md`: „Archiv | Überholte Einträge. Wird nie
aufgeräumt; jeder Eintrag nennt, wodurch er abgelöst wurde."
`Uni/_ARCHIV.md` sagt über sich selbst: „Nur **überholte** Einträge der
Uni-Schicht. Jeder nennt, wodurch er abgelöst wurde." Ein abgehakter
Punkt hat keinen Nachfolger zu nennen — er passt dort gar nicht hinein.
Die eigene ROADMAP hält sich auch nicht daran: Zwei abgehakte Punkte
stehen unverändert in der Datei, keiner im Archiv.
**Soll:** „Überholtes in `Uni/_ARCHIV.md`", oder die Zeile lässt das
Archiv weg — der Kopf der Datei muss nicht jeden Nachbarn nennen.
**Auftrag:** Ein Wort. Danach INDEX neu erzeugen.
**Gewicht:** lohnt sich

### U6 — Eine Zustandsaussage in einer Regeldatei
**Befund:** `Uni/DOCX_RULES.md`: „Die abgegebene Fassung vom 21.08.
bleibt liegen, bis der nächste Textstand gebaut wird." Das ist kein
Umgang mit `.docx`-Dateien, sondern der Zustand eines einzelnen
Vorgangs — und er endet, sobald jemand baut. Eine Regeldatei, die den
Tagesstand mitführt, veraltet mit ihm.
**Beleg:** `Kern/DOC_RULES.md`, Abschnitt 7: „Statusvermerke gehören zu
der Datei, die den Gegenstand besitzt, nicht in eine zweite."
**Soll:** Der Satz steht in `Uni/LOG.md` (als Ereignis) oder nirgends.
**Auftrag:** Streichen, sobald der nächste Stand gebaut ist — vorher
gibt er eine echte Auskunft, danach eine falsche.
**Gewicht:** bei Bedarf

---

## Durchgang 2 — Widersprüche quer über den Bestand

| Information | Besitzer laut Regel | tatsächlich in | Urteil |
|---|---|---|---|
| Inhalt des TDD | `Projekte/Isor_Tower/TDD.md` (seit 2026-08-25) | `DOCX_RULES.md` zeigt auf ROADMAP/LOG | **Konflikt → U1** |
| Bauweg `.md` → `.docx` | `DOCX_RULES.md` | dort; `Kern/ROADMAP.md` nennt nur das Ereignis | sauber |
| Word-XML-Fallen | Knowledge, `Werkzeuge\word-xml-fallen.md` | `DOCX_RULES.md` verweist, kopiert nicht | **vorbildlich** |
| Formatvorgaben der SAE | die PDF im Datenbaum | `DOCX_RULES.md` verweist und hebt zwei Punkte hervor | sauber |
| Was wohin bei der Abgabe | `Abgabe_Packliste.txt` im Datenbaum | `DOCX_RULES.md` grenzt ausdrücklich ab: „die ROADMAP sagt *wann*, die Packliste *was wohin*" | **vorbildlich** |
| Archivbegriff | `GLOSSARY.md` / `DOC_RULES.md` | `Uni/ROADMAP.md` weicht ab | Konflikt → U5 |
| Aufgabentexte | die sieben `ASSIGNMENT_*.md` | dort, unverändert | sauber |

Zwei Stellen sind ausdrücklich hervorzuheben, weil sie zeigen, wie es
aussieht, wenn Ownership funktioniert: Die Word-Fallen liegen im
Knowledge, **weil sie für jedes Word-Dokument gelten**, und die Datei
sagt diesen Grund dazu. Und die Grenze zur Packliste ist in einem
Halbsatz geregelt, der beide Seiten benennt. Beides sind Muster, keine
Befunde.

---

## Stand

Sechs Befunde: `muss` sind U1 und U2 · `lohnt sich` sind U3, U4 und U5 ·
`bei Bedarf` ist U6. Behoben ist nichts — das gehört in einen eigenen
Abschnitt, nicht in diese Session (`Kern/WORKFLOW.md` → „Prüfer und
Ausführender sollen nicht dieselbe Session sein").

**Gesamturteil:** Die Uni-Schicht ist deutlich gesünder als
`CODE_GUIDELINES.md` — sechs Befunde auf 1.663 Zeilen gegen neun auf
348. Der Grund liegt in der Zusammensetzung: Zwei Drittel der Schicht
sind Chroniken, Archiv und unveränderliche Originaltexte, und die
altern nicht. Beide Befunde mit Gewicht `muss` sitzen an derselben
Stelle — in `DOCX_RULES.md`, und beide stammen aus **derselben
Umstellung**: Seit dem 2026-08-25 führt das Markdown und baut Pandoc.
Die Datei hat den Wechsel im Fließtext nachgezogen, aber weder in ihrer
Ownership-Zeile noch in ihrer Prüfliste.

## Zu melden (fremdes Revier, nicht geschrieben)

Die Doku-Pflicht für den Typ Prüfung verlangt „ROADMAP der geprüften
Schicht um die Befunde · LOG der Schicht, ein Satz". Beides liegt in
`Uni/` und damit außerhalb des Reviers dieses Abschnitts. Vorbereitet,
wartet auf Freigabe:

- **`Uni/ROADMAP.md`**, neuer Punkt: „Die sechs Befunde der Prüfung vom
  2026-08-26 beheben — Liste in `_HARNESS_UNI_SCHICHT.md`, zwei davon
  `muss`, beide in `DOCX_RULES.md` und beide Folge der
  Markdown-Umstellung vom 2026-08-25."
- **`Uni/LOG.md`**, ein Satz: „2026-08-26 — Uni-Schicht geprüft, erster
  Prüfbogen für diese Schicht: sechs Befunde auf zwölf Dateien, geprüft
  gegen Prüfbogen, INDEX und die Regeldateien des Kerns."
