# _HARNESS_ABNAHME.md — Befundliste der Abnahme (Phase 8)

Ownership: Nur die Befunde des Schlussdurchgangs vom 2026-08-22 ff. —
was falsch, doppelt, widersprüchlich ist oder fehlt. Keine Handgriffe
(die kommen nach der Abnahme in `_HARNESS_UMSETZUNG.md`), keine
Begründungen von Entscheidungen (DECISIONS). Temporär — wird zusammen
mit `_HARNESS_REVIEW.md` und `_HARNESS_UMSETZUNG.md` archiviert.

Format: `### A<Nr> — Kurztitel` mit den Zeilen **Was**, **Warum es
zählt**, **Vorschlag** und **Gewicht** (`muss` · `lohnt sich` · `bei
Bedarf`). Die A-Nummern sind fortlaufend und werden nicht neu vergeben.

Verhältnis zu den beiden anderen Review-Dateien: `_HARNESS_REVIEW.md`
sammelte die Befunde **vor** dem Umbau (E-Nummern), diese Datei die
Befunde **am fertigen Stand**. Ein A-Befund darf auf eine E-Nummer
verweisen, wenn er dieselbe Stelle noch einmal trifft.

---

## Stand der Umsetzung (2026-08-22)

Diese Liste ist der Zähler — die einzelnen Befunde unten werden **nicht**
abgehakt, sonst stünde derselbe Stand an 33 Stellen.

**Erledigt (30):** A1 · A2 · A3 · A4 · A5 · A6 · A7 · A8 · A9 · A11 ·
A13 · A14 · A15 · A16 · A17 · A18 · A19 · A20 · A21 · A22 · A23 · A24 ·
A26 · A27 · A28 · A29 · A30 · A31 · A32 · A33

**Offen (3) — alle drei hängen an einem späteren Zeitpunkt, nicht an Arbeit:**

| Befund | Wann |
|---|---|
| A10 | kurz **vor** dem Archivieren: die Review-Dateien auf nur dort lebende Regeln durchsuchen |
| A25 | beim Archivieren: `Kern/ROADMAP.md` → „Läuft gerade" mitziehen |
| A12 | erster `/harness:sonntag`, bevor `Harness_1.0.0` ausgeliefert wird |

**Aus dem Beheben selbst kamen zwei Nachträge:**
- **A32 war schlimmer als beschrieben.** Nicht ein künftiges Risiko,
  sondern aktiver Verlust: `prefab_status.py` las 34 Prefabs als 33
  Einträge ein, weil `Torch` und `Torch ` auf denselben Schlüssel
  fielen. Der von Hand geschriebene Befund zu `Torch` wäre beim nächsten
  `--write` gelöscht worden. Nachgewiesen vor der Behebung.
- **A13 war unvollständig belegt.** Der Assets-Baum enthält vierzehn
  Typordner, nicht die neun aus dem DECISIONS-Eintrag; `Shared/` ist
  ersatzlos weg (Querschnitts-Code liegt als `Scripts/Interfaces/`,
  `Timer/`, `Health/`, `Diagnostic/`); und `FolderTemplate/` wie
  `Sandbox/` liegen im Projekt, ohne in einer Regel vorzukommen. Die
  beiden letzten stehen jetzt als offener Punkt in `CODE_GUIDELINES.md`.

---

## Durchgang 1 — Kern, Grundregeln

Gelesen: `CLAUDE.md` (oberste + Claude/) · `INDEX.md` · `PLAN.md` ·
`Kern/WORKFLOW.md` · `Kern/DOC_RULES.md` · `Kern/VERSIONIERUNG.md` ·
`Kern/GLOSSARY.md` · `Kern/STOERUNGEN.md` · `_HARNESS_UMSETZUNG.md`

### A1 — Einstiegsdatei nennt einen überholten Stand
**Was:** `Claude/CLAUDE.md`, Zeile 8: „Harness-Version: 1.0.0 — im
Aufbau (Überholung seit 2026-08-21, **Phase 2 von 7**)." Tatsächlich
sind die Phasen 1–7 durch, und die Liste hat inzwischen **acht** Phasen.
**Warum es zählt:** Es ist die erste Zeile, die eine frische Session
liest, und sie ist doppelt falsch — Zähler und Nenner. Zugleich der
Musterfall von `DOC_RULES.md` Abschnitt 7: ein Statusvermerk in einer
handgeschriebenen Datei, den keine Prüfung abgleicht.
**Vorschlag:** Den Phasenzähler ersatzlos streichen statt ihn
nachzuziehen. Der Fortschritt gehört `PLAN.md`, das ihn ohnehin führt;
in CLAUDE.md bleibt „1.0.0 — im Aufbau" bzw. nach der Abnahme „1.0.0".
**Gewicht:** muss

### A2 — Phase 8 zählt die offenen Störungen falsch
**Was:** `_HARNESS_UMSETZUNG.md`, Phase 8: „Offene Störungen abarbeiten
… offen ist noch die Regel ‚wer eine Bauliste abhakt…'." Der
Übergabe-Abschnitt derselben Datei sagt dagegen „die **vier** offenen
Einträge in `Kern/STOERUNGEN.md`". Nachgezählt: von acht Einträgen ist
einer unbehoben (*Angekündigte Fragen nicht gestellt*), zwei tragen eine
offene Restfrage (*Berechtigungsliste wächst nach* — Ursache bleibt ·
*Regel überlebte in einer Erledigt-Liste* — ob daraus eine Harness-Regel
wird, sollte die Abnahme entscheiden), und einer steht auf `offen`,
obwohl er erledigt ist (siehe A7).
**Warum es zählt:** Nach der kürzeren Fassung fiele die Hälfte der
offenen Punkte lautlos weg — und zwar genau die, die niemand vermisst,
weil sie schon einmal abgehakt aussahen.
**Vorschlag:** Den Phase-8-Punkt auf die vier Einträge umschreiben und
sie namentlich nennen, statt eine Zahl zu führen.
**Gewicht:** muss

### A3 — „Behoben: offen" widerspricht sich selbst
**Was:** `Kern/STOERUNGEN.md` gibt im Kopf das Format vor: die Zeilen
**Was**, **Ursache**, **Regel** „und, sobald behoben, **Behoben**". In
vier Einträgen steht aber `**Behoben:** offen`.
**Warum es zählt:** Das Feld beantwortet zwei verschiedene Fragen (*ist
es erledigt* / *seit wann*) und heißt nach der einen. Wer die Datei
überfliegt, sieht in jeder Zeile das Wort „Behoben" — auch dort, wo
nichts behoben ist. Genau danach wurde in A2 falsch gezählt.
**Vorschlag:** Zeile in **Stand** umbenennen, Werte `offen` oder
`behoben JJJJ-MM-TT`. Dann ist die Liste der offenen Störungen ein
Suchlauf nach `Stand: offen` statt eine Zählarbeit.
**Gewicht:** lohnt sich

### A4 — Die Regel „keine Anzahl in Überschriften" bricht sich selbst
**Was:** `DOC_RULES.md` Abschnitt 7 verbietet Anzahlen in Überschrift
und Einleitung, „wenn die Liste wachsen kann". Verstöße im eigenen Haus:
`DOC_RULES.md` → „### Die **drei** Prüfungen" · `VERSIONIERUNG.md` →
„## Die **drei** Nummern auf einen Blick" · `DOC_RULES.md` Abschnitt 10,
`CLAUDE.md` und `GLOSSARY.md` → „**vier** Schichten".
**Warum es zählt:** Bei den Nummern ist das Wachstum schon terminiert —
`_HARNESS_UMSETZUNG.md` führt „Repo-/Git-Regeln samt
**Build-Versionsschema**" als offenen Punkt. Die vierte Nummer kommt,
die Überschrift bleibt bei drei.
**Vorschlag:** Nicht alle Überschriften entkernen, sondern die Regel
schärfen: Eine Anzahl ist erlaubt, wenn die Aufzählung **abgeschlossen**
ist und der Text sagt, warum es nicht mehr werden können. Wo das nicht
gilt (Nummern, Prüfungen), fällt die Zahl weg.
**Gewicht:** lohnt sich

### A5 — „Vier Schichten" stimmt nicht, sobald es zwei Projekte gibt
**Was:** `Kern/` · `Uni/` · `IsorBackup/` · `Projekte/<Name>/` werden
durchgehend als vier gleichrangige Schichten geführt. Die vierte ist
aber keine Schicht, sondern eine **Familie**: Bei zwei Projekten sind es
fünf Ordner.
**Warum es zählt:** Nicht die Zahl ist das Problem, sondern die
Gleichsetzung. Alles, was für „eine Schicht" gilt — eigene ROADMAP, LOG,
DECISIONS, herausnehmbar als Ganzes —, gilt bei `Projekte/` **je
Projekt**, und das steht nirgends.
**Vorschlag:** In `DOC_RULES.md` Abschnitt 10 eine Zeile: `Projekte/`
ist ein Sammelordner, jedes Projekt darin eine eigene Schicht.
`GLOSSARY.md` zieht die Kurzform nach.
**Gewicht:** lohnt sich

### A6 — Die Ownership-Pflicht endet an der Ordnergrenze
**Was:** `DOC_RULES.md` Abschnitt 3 macht die `Ownership:`-Zeile zur
Pflicht „in jeder Datei", und der erzeugte INDEX setzt sie durch — aber
nur unterhalb von `Claude\`. Ohne Zeile und ohne Registereintrag sind
damit: `Harness Project\CLAUDE.md` (die **einzige**, die automatisch
lädt), `My Harness Development\CLAUDE.md` und die fünf Auslöser unter
`.claude\commands\harness\`.
**Warum es zählt:** Erweitert den Phase-8-Punkt „INDEX-Blindstelle", der
nur die fünf Auslöser nennt. Betroffen ist auch die Datei mit dem
Notkern — also ausgerechnet die, deren Inhalt eine bewusste Kopie ist
und die deshalb am ehesten auseinanderlaufen kann.
**Vorschlag:** Skript um die beiden Wegweiser-`CLAUDE.md` und
`.claude\commands\harness\` erweitern und beide Gruppen im INDEX als
eigenen Abschnitt führen. Die Alternative — Ausnahme benennen — deckt
den Notkern nicht ab.
**Gewicht:** muss

---

## Durchgang 2 — Kern, Ausgabeformen

Gelesen: `Kern/ARTIFACT_RULES.md` · `Kern/ARTIFACT_INDEX.md` ·
`Kern/KNOWLEDGE_RULES.md` · `Kern/DIAGRAM_RULES.md`

### A7 — Eine behobene Störung steht weiter auf „offen"
**Was:** `Kern/STOERUNGEN.md`, Eintrag *Haken gesetzt, Arbeit nicht
getan*, schließt mit „**Behoben:** offen. Der Eintrag wird im Zuge der
Harness-Seite gebaut." Der Eintrag existiert aber längst:
`Kern/ARTIFACT_INDEX.md` führt seit Phase 7 den Abschnitt
„⚙️ System — Schicht: Kern (der Harness selbst)" samt vorbereitetem
Block und Begründung. Der Befund selbst („das Wort Harness kommt nicht
vor") beschreibt korrekt den Stand von damals — falsch ist nur die
Statuszeile.
**Warum es zählt:** Derselbe Mechanismus wie der Vorfall, den der
Eintrag beschreibt, nur andersherum: Damals war ein Haken gesetzt ohne
Arbeit, jetzt ist Arbeit getan ohne Haken. Beides hat dieselbe Ursache —
Status und Datei werden getrennt gepflegt.
**Vorschlag:** Statuszeile auf `behoben 2026-08-22` mit Nennung der
geänderten Datei. Das ist zugleich die kleinste Fassung der Regel, die
in dieser Störung als Kandidat steht: **Wer abhakt, nennt die Datei.**
Statt sie als eigene Harness-Regel zu formulieren, sollte sie in das
Format von `STOERUNGEN.md` und der Baulisten eingebaut werden — eine
Formatvorgabe wird befolgt, eine Verhaltensregel vergessen.
**Gewicht:** muss

### A8 — Dieselbe Regel steht zweimal in derselben Datei
**Was:** `Kern/KNOWLEDGE_RULES.md` sagt unter „Format pro Datei":
„Härtegrenze: Passt es nicht auf einen Bildschirm, sind es zwei Konzepte
→ zwei Dateien." Und unter „Wann wird geschrieben": „Ein Konzept, das
nicht auf einen Bildschirm passt, sind zwei — dann zwei Dateien mit
gegenseitigem Verweis."
**Warum es zählt:** Lehrbuchfall für `DOC_RULES.md` Regel 1, und zwar
innerhalb einer einzigen Datei — die Fassungen unterscheiden sich schon
jetzt, die zweite verlangt zusätzlich den gegenseitigen Verweis.
**Vorschlag:** Die Fassung unter „Format pro Datei" streichen, die
vollständigere behalten.
**Gewicht:** lohnt sich

### A9 — Positionsverweise dort, wo die Regel sie verbietet
**Was:** `Kern/DIAGRAM_RULES.md` verweist fünfmal auf „Bedienregel 1",
„Bedienregel 2", „Bedienregel 3" und „Bedienregel 5". `DOC_RULES.md`
Abschnitt 6 verbietet genau das: „Nur über Namen, nie über Positionen."
Die Gefahr hat sich hier bereits verwirklicht — Regel 5 wurde
nachträglich angehängt und stammt vom 2026-08-11, während die Überschrift
der Liste „aus dem Praxisbetrieb 2026-08-08" sagt.
**Warum es zählt:** Verschiebt sich die Liste einmal, zeigen fünf
Verweise still auf die falsche Regel. `DOC_RULES.md` nennt dafür den
Grundsatz „sichtbar kaputt ist besser als still falsch".
**Vorschlag:** Jede Bedienregel bekommt einen fettgedruckten Kurznamen
(*Zielkasten leuchtet* · *In die Datei speichern* · *Nicht kopieren* ·
*Datei schließen* · *Freies Ende bleibt frei*), Verweise gehen über den
Namen. Datumsangabe der Überschrift streichen.
**Gewicht:** lohnt sich

### A10 — Die Ausnahme für die Diagramm-Skripte steht nur in einer Datei, die archiviert wird
**Was:** `Kern/DIAGRAM_RULES.md` beginnt mit „Der Ablageort folgt der
Schicht, nicht dieser Datei … Hier steht das Verfahren, nicht der Pfad"
— und listet elf Zeilen später feste Pfade
(`C:\IsorBackup\05_Werkzeuge\Vorlagen\`, `Diagramme_Quellen\_Sicherung\`).
Dass das Absicht ist, steht ausschließlich in `_HARNESS_UMSETZUNG.md`,
Phase 5: „Die Diagramm-Skripte bleiben, wo sie sind." Diese Datei wird
am Ende der Abnahme archiviert.
**Warum es zählt:** Das ist wortgleich der Vorfall *Regel überlebte nur
zufällig in einer Erledigt-Liste* — eine geltende Ausnahme lebt in einer
Bauliste, die nach dem Abhaken niemand mehr liest. `DOC_RULES.md`
Abschnitt 8 verlangt, dass eine Ausnahme sich selbst benennt.
**Warum das über diesen Fall hinausgeht:** Vor dem Archivieren der
beiden Review-Dateien ist zu prüfen, **was sonst noch nur dort steht**.
Kandidaten sind alle Phasen-Vorbemerkungen (Phase 5 „Ablage
entschieden", Phase 6 „Fund an der Repo-Grenze", Phase 2 und 4
„Zusätzlich zur Planung erledigt"). Das ist ein eigener Arbeitsschritt,
nicht nur ein Befund — er gehört vor den letzten Punkt von Phase 8.
**Vorschlag:** Ausnahme in `DIAGRAM_RULES.md` unter „Ablage" benennen
und begründen; Phase 8 um den Schritt „Review-Dateien auf nur dort
lebende Regeln durchsuchen" ergänzen, **vor** dem Archivieren.
**Gewicht:** muss

### A11 — Feldliste des ARTIFACT_INDEX kennt ihr eigenes Feld nicht
**Was:** `Kern/ARTIFACT_INDEX.md` zählt oben die Zeilen je Eintrag auf:
URL, Stand, Quelle, Skripte/Beispiel, Seite →, Seite ←. Die drei
Zeugnis-Einträge benutzen stattdessen `Datum` — begründet an Ort und
Stelle, aber in der Feldliste nicht vorgesehen.
**Warum es zählt:** Gering. Es fällt nur auf, weil der Index sonst
sauber ist.
**Vorschlag:** Eine Zeile in der Feldliste: `Datum` ersetzt `Stand` bei
Zeugnis-Seiten, weil dort kein Prüfstand gemeint ist.
**Gewicht:** bei Bedarf

### A12 — Kein Artifact kennt den Umbau
**Was:** Die Stände im `ARTIFACT_INDEX` reichen vom 2026-08-05 bis
2026-08-12. Der Umbau vom 21./22.08. hat `PLAN.md`, alle ROADMAPs und
die DECISIONS vollständig ersetzt — die Seite `📍 Status · Wo das
Projekt steht` nennt als Quelle genau diese Dateien und ist damit
inhaltlich überholt, nicht nur alt.
**Warum es zählt:** Kein Fehler im Harness, sondern fällige Arbeit: Der
Pflegetag `/harness:sonntag` ist gebaut, aber noch nie gelaufen. Wenn
`Harness_1.0.0` den abgenommenen Stand enthalten soll, gehört ein erster
Sonntagsdurchgang davor.
**Vorschlag:** Als Empfehlung führen (Gewicht „lohnt sich"), nicht als
Befund abarbeiten — die Artifact-Seiten sind nicht Teil der
Auslieferung.
**Gewicht:** lohnt sich

---

## Durchgang 3 — Kern, Arbeitsregeln

Gelesen: `Kern/ASSESSMENT_RULES.md` · `Kern/CODE_GUIDELINES.md` ·
`Kern/GDD_RULES.md` · `Kern/ROADMAP.md` · `Kern/DECISIONS.md` ·
`Kern/LOG.md` · `IsorBackup/RULES.md` · `IsorBackup/DECISIONS.md` ·
`Uni/DOCX_RULES.md` · `Projekte/Isor_Tower/GDD.md`

### A13 — Die geltende Ordnerstruktur steht nirgends als Regel
**Was:** Am 2026-08-20 wurde der gesamte Assets-Baum von Themenordnern
auf **Typordner** umgestellt (`Kern/DECISIONS.md`, „Assets nach Typ statt
nach Thema"). Die Regeldatei kennt die Umstellung nicht:
`Kern/CODE_GUIDELINES.md`, Abschnitt „Ordnerstruktur (Praxis-Stand
2026-07-19)", beschreibt weiterhin `Entities/<Name>/`,
`Environment/<Name>/`, `Systems/<Name>/`, `FolderTemplate/` und
`Shared/`. Auch der Editor-Ordner widerspricht sich: DECISIONS sagt
„Editor-Code liegt getrennt in `Assets/Editor/`", CODE_GUIDELINES sagt
„er darf im System-Ordner liegen (z. B. `Systems/TerrainGenerator/
Editor/`)".
Dazu stehen vier DECISIONS-Einträge ohne Ablöse-Vermerk nebeneinander,
obwohl sie einander widersprechen: 2026-07-19 (Kategorie +
FolderTemplate) · 2026-08-08 (Ordner folgen den Systemgrenzen) ·
2026-08-14 (FolderTemplate um `Audio`) · 2026-08-20 (Assets nach Typ).
Der Kopf von `Kern/DECISIONS.md` verlangt: „Ein neuer Eintrag nennt,
welchen er ablöst."
**Warum es zählt:** Der schwerste Befund der Abnahme. Es ist die einzige
Stelle, an der eine **falsche Regel** dasteht statt eines falschen
Verweises — wer beim nächsten Baustein einen Ordner anlegt, legt ihn nach
der Datei an, die als Regeldatei gilt, und baut die vor zwei Tagen
aufgelöste Struktur nach. Der Stand-Stempel „Praxis-Stand 2026-07-19" in
der Überschrift macht es schlimmer: Er sieht aus wie eine Bestätigung.
**Vorschlag:** Abschnitt „Ordnerstruktur" gegen den Stand vom 2026-08-20
neu schreiben (Isor besitzt den Inhalt, Claude die Formulierung), den
Editor-Widerspruch dabei entscheiden. Die drei überholten
DECISIONS-Einträge nach `Kern/_ARCHIV.md` mit Angabe des Nachfolgers,
oder — wenn ihre Begründung weitergilt — mit einer Zeile „Fortgeführt am
…", wie es Phase 4 bei zwei anderen Einträgen gemacht hat.
**Gewicht:** muss

### A14 — CODE_GUIDELINES beruft sich auf eine Entscheidung, die es nicht gibt
**Was:** `Kern/CODE_GUIDELINES.md`, Abschnitt „Priorität": Die neue
Ableitung „Uni-Ordner vorhanden → Block 1 gewinnt" endet mit dem Beleg
„(`Kern/DECISIONS.md`, 2026-08-22)". Unter diesem Datum stehen dort vier
Einträge — Werkzeuge in der Schicht, Notkern, Befehle als Auslöser,
Berechtigungen. Ein Eintrag zum Projekt-Typ ist nicht darunter.
**Warum es zählt:** Die Begründung steht damit ausschließlich in der
Regeldatei. `Kern/DECISIONS.md` beansprucht in seiner Ownership-Zeile
genau das Gegenteil: „keine ausformulierte Regel — hier steht nur, warum
sie gilt". Zugleich behauptet die Regeldatei einen Beleg, den niemand
nachschlagen kann.
**Vorschlag:** Den fehlenden Eintrag nachtragen (Was: Ableitung aus dem
Vorhandensein von `Uni/` · Warum: beim Kopieren in ein privates Projekt
vergisst man das Umstellen · Verworfen: `Projekt-Typ:`-Zeile von Hand)
und dabei den Eintrag von 2026-07-17 als abgelöst markieren.
**Gewicht:** muss

### A15 — Ein DECISIONS-Eintrag nennt eine gelöschte Datei und einen abgelösten Auslöser
**Was:** `Kern/DECISIONS.md`, 2026-08-11 („Zeugnis als vierter
Session-Typ"): „die Zeugnisse in ASSESSMENT_LOG.md" — die Datei wurde in
Phase 3 in zwei Zeugnisdateien aufgelöst. Und: „Auslöser ist der Skill
`/zeugnis`" — es ist kein Skill mehr, sondern `/harness:zeugnis`; der
globale Skill ist laut Eintrag vom 2026-08-22 archiviert.
**Warum es zählt:** Phase 4 hakte eine „Gesamtprüfung auf tote Verweise"
ab und nennt als Fundort „fünf **aktive Regeldateien**". `DECISIONS.md`
fiel offenbar unter eine Ausnahme, die nirgends benannt ist — die
maschinelle Nachprüfung findet den Verweis sofort.
**Vorschlag:** Zeile „Fortgeführt am 2026-08-22" nach dem Muster, das
Phase 4 bei zwei anderen Einträgen benutzt hat. Den Eintragstext selbst
nicht ändern — er ist datiert und beschreibt den Stand von damals.
**Gewicht:** muss

### A16 — Der Zeugnis-Befehl heißt in seiner eigenen Regeldatei falsch
**Was:** `Kern/ASSESSMENT_RULES.md`, Abschnitt „Auslöser": „Auf Zuruf
(„Zeugnis", `/zeugnis`)." Der Befehl heißt `/harness:zeugnis`;
`Kern/WORKFLOW.md` legt den Namensraum ausdrücklich fest.
**Warum es zählt:** `/zeugnis` gibt es nicht — der Aufruf läuft ins
Leere, und zwar in der Datei, die den Session-Typ vollständig besitzt.
**Vorschlag:** Auf `/harness:zeugnis` korrigieren. Die weiteren
Fundstellen ohne Präfix (`Kern/DECISIONS.md`, `Kern/LOG.md`,
`Kern/STOERUNGEN.md`-Kopf) sind datierte Einträge und bleiben — außer
der Kopfzeile von `STOERUNGEN.md`, die eine geltende Regel formuliert
(„zusätzlich fragt die `/ende`-Routine danach").
**Gewicht:** muss

---

## Durchgang 4 — Befehle und Auslieferung

Gelesen: die fünf Auslöser unter `.claude\commands\harness\` ·
`Kern/VERSIONIERUNG.md`, Abschnitt „Die Kern-Auslieferung"

### A17 — `zeugnis.md` trägt Ablauf, obwohl Auslöser keinen tragen dürfen
**Was:** `Kern/WORKFLOW.md` legt fest: „Die Dateien unter
`.claude\commands\` sind nur Auslöser. Sie zeigen hierher und **tragen
keinen Ablauf** … Weicht ein Auslöser von hier ab, gilt dieser Abschnitt,
und die Abweichung wird gemeldet." Hiermit gemeldet: `zeugnis.md`
enthält drei Dinge, die nirgends sonst stehen —
(1) den Arbeitsschritt „Prüfanker des jüngsten Zeugnisses holen, heutige
Zahl neben die alte",
(2) die Vorgabe für die Chat-Antwort („Kernaussage, Notenbild und die
drei wichtigsten Punkte — nicht nur auf die Datei verweisen"),
(3) einen Absatz, der sich selbst als einzige Fundstelle ausweist:
„Werkzeugseitig, **steht sonst nirgends**: Ein `.docx` lässt sich per
Python in Text wandeln (`zipfile` auf `word/document.xml` …)."
**Warum es zählt:** `.claude\` ist **nicht versioniert** — das ist die
tragende Begründung der ganzen Auslöser-Konstruktion
(`Kern/DECISIONS.md`, 2026-08-22). Drei Arbeitsregeln liegen damit
ausgerechnet an der einzigen Stelle ohne Historie und ohne Backup durch
Git. Punkt (3) sagt es selbst.
**Vorschlag:** (1) und (2) nach `Kern/ASSESSMENT_RULES.md` — (1) ist
faktisch eine Dublette zum Pflichtabschnitt „Prüfanker des letzten
Zeugnisses — beantwortet", (2) gehört in die Schreibregeln. (3) nach
`Uni/DOCX_RULES.md`, Abschnitt „Werkzeuge", wo `validate.py` und
`soffice.py` schon stehen. Danach ist `zeugnis.md` acht Zeilen lang wie
die anderen vier.
**Gewicht:** muss

### A18 — `wechsel.md` zitiert eine Überschrift, die es nicht gibt
**Was:** Der Auslöser verweist auf `Kern/WORKFLOW.md`, Abschnitt „Modus
und Regler". Der Abschnitt heißt seit der Behebung der Typ-Störung „**Typ,**
Modus und Regler".
**Warum es zählt:** Klein, aber es ist genau der Verweistyp, den
`DOC_RULES.md` als den sicheren empfiehlt (Pfad + Überschrift) — er
trägt nur, wenn die Überschrift stimmt.
**Vorschlag:** Überschrift im Auslöser korrigieren.
**Gewicht:** lohnt sich

### A19 — Die Auslieferung enthält die Befehle nicht
**Was:** `Kern/VERSIONIERUNG.md` legt den Inhalt einer Auslieferung fest:
„nur `Kern/` plus die Datei mit der Leseordnung. Keine Uni, kein Projekt,
keine Altbestände." Die fünf Auslöser liegen unter
`.claude\commands\harness\` und sind damit weder im Repo noch in der
Auslieferung.
**Warum es zählt:** Ein neues Projekt bekäme den Harness ohne
`/harness:sichern`, `:wechsel`, `:ende`, `:sonntag`, `:zeugnis` — also
ohne die Bedienoberfläche, die `WORKFLOW.md` beschreibt. Die
Begründung der Auslöser-Konstruktion sagt, ein verlorener Auslöser sei
„aus WORKFLOW in zwei Minuten neu geschrieben". Das stimmt — aber nur,
wenn jemand weiß, dass fünf davon fehlen. In der Auslieferung steht das
nirgends.
**Vorschlag:** Die fünf Auslöser als Ordner `Kern/Befehle/` **im Repo**
mitführen und beim Einrichten eines Projekts nach `.claude\commands\
harness\` kopieren. Dann sind sie versioniert, stehen im INDEX (löst
zugleich die halbe Blindstelle aus A6) und wandern mit der Auslieferung
mit. Der Kopierschritt gehört in die Auslieferungs-Beschreibung.
**Gewicht:** muss

---

## Durchgang 5 — Querprüfungen über den ganzen Bestand

Maschinell geprüft: alle `.md`/`.py`/`.ps1`/`.txt`-Verweise in 50 Dateien
gegen den tatsächlichen Bestand (Skript im Scratchpad,
`verweise_pruefen.py`) · Existenz der genannten Außenstellen ·
Knowledge-READMEs · Probelauf `index_bauen.py`.

Sauber und ohne Befund: alle sieben Knowledge-Themenordner haben ihr
`README.md`, der Root-README existiert · alle drei Wissensseiten, auf die
`STOERUNGEN.md` und `DOCX_RULES.md` zeigen, existieren · die externen
Uni-Pfade (`_Regelwerk`, `Abgabe_Packliste.txt`) stimmen ·
`index_bauen.py` findet 47 Dateien, alle mit Ownership-Zeile · die
verbliebenen Verweise auf `FEATURE_LOG.md` und `ASSESSMENT_LOG.md`
stehen ausschließlich in Chroniken und Archiven, wo sie zulässig sind
(Ausnahme: A15).

### A20 — Der Auslieferungsordner ist abgehakt, aber nicht vorhanden
**Was:** `_HARNESS_UMSETZUNG.md`, Phase 1: „[x] Auslieferungs-Ordner
anlegen: `C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\` (E80)".
Der Ordner existiert nicht. `Kern/VERSIONIERUNG.md` und
`IsorBackup/RULES.md` (Baum, `05_Werkzeuge\`) nennen ihn beide als
bestehend.
**Warum es zählt:** Der **zweite** nachgewiesene falsche Haken, und
damit der Beleg, dass der Vorfall vom 2026-08-22 kein Einzelfall war.
Genau danach fragt Phase 8, Punkt 2.
**Vorschlag:** Ordner anlegen — das ist ohnehin der erste Schritt des
letzten Phase-8-Punkts. Wichtiger ist die Folgerung für A7: Ein Haken
braucht die geänderte oder angelegte Datei daneben.
**Gewicht:** muss

### A21 — Vier Aufgabentexte sind abgehakt und fehlen
**Was:** `_HARNESS_UMSETZUNG.md`, Phase 4: „[x] vier fehlende
Aufgabentexte nachtragen; wo es keinen gibt, genau das als Datei
festhalten (E62)". Die vier Dateien existieren nicht —
`ASSIGNMENT_AKADEMISCH.md`, `ASSIGNMENT_KI_PROTOTYP.md`,
`ASSIGNMENT_SIMULATION.md`, `ASSIGNMENT_SOFTWAREPLANUNG.md` stehen
weiterhin als „(geplant)" in `INDEX.md` und in `index_geplant.txt`.
**Warum es zählt:** Der **dritte** falsche Haken. Entwarnung gegenüber
der ersten Fassung dieses Befundes: Die Arbeit ist **nicht** verloren —
`Uni/ROADMAP.md` führt den Punkt „Fehlende Aufgabentexte nachtragen
(E62)" ausführlich als offen, mitsamt der Begründung aus
`ASSESSMENT_RULES.md` („beide bisherigen Zeugnisse haben sieben Abgaben
bewertet und hatten die Kriterien für drei"). Falsch ist allein der
Haken in der Bauliste. Es bleibt aber ein Widerspruch zwischen zwei
aktiven Dateien: Die eine sagt erledigt, die andere offen.
**Vorschlag:** Haken zurücknehmen und durch einen Zeiger auf
`Uni/ROADMAP.md` ersetzen. Die Texte selbst kann nur Isor beschaffen; wo
es keinen gibt, bleibt es bei der Datei mit genau dieser Aussage.
**Gewicht:** muss

### A22 — Positionsverweise, vollständige Liste
**Was:** Erweitert A9 um die maschinelle Suche. Verweise über eine
Listenposition statt über einen Namen stehen in:
`Kern/DIAGRAM_RULES.md` (5×, „Bedienregel 1/2/3/5", „Regel 1") ·
`Kern/ARTIFACT_RULES.md` und `Kern/ARTIFACT_INDEX.md` („Punkt 5 des
Review-Gate") · `Kern/CODE_GUIDELINES.md` („Die Liste unter Punkt 4") ·
`Kern/DECISIONS.md` („Block-1-Regel 5", „ROADMAP-Punkt 8") ·
`Kern/LOG.md` („jetzt Bedienregel 5") ·
`IsorBackup/RULES.md` und `IsorBackup/DECISIONS.md` („Regel 7",
„Regel 5 in RULES.md") ·
`Projekte/Isor_Tower/DECISIONS/Gras.md` („ROADMAP Punkt 4") und
`Projekte/Isor_Tower/LOG.md` („ROADMAP-Punkt 8") ·
`_HARNESS_UMSETZUNG.md` („ROADMAP Punkt 9", „Punkt 7").
**Warum es zählt:** Die ROADMAP-Verweise sind bereits tot: Nach dem
Neuschnitt in Phase 3 tragen weder `Kern/ROADMAP.md` noch
`Projekte/Isor_Tower/ROADMAP.md` überhaupt Nummern. Vier Verweise zeigen
auf eine Nummerierung, die es nicht mehr gibt — still, wie
`DOC_RULES.md` es vorhergesagt hat.
**Nicht betroffen:** Die Verweise der Form „`DOC_RULES.md`, Abschnitt 8"
(rund 15 Stellen). Dort ist die Nummer Teil der Überschrift
(`## 8. Grenzfälle…`) und damit ein Name, keine Position.
**Vorschlag:** Zwei Handgriffe. Erstens die ROADMAP-Verweise in
Chroniken und DECISIONS durch den Titel des Punkts ersetzen — sie sind
datiert, aber unauffindbar. Zweitens in `DOC_RULES.md` Abschnitt 6 den
zulässigen Fall benennen: Eine Nummer darf zitiert werden, wenn sie in
der Überschrift des Ziels steht; nummerierte Listen ohne Titel bekommen
Kurznamen.
**Gewicht:** lohnt sich

### A23 — Zeugnis-Session darf den INDEX nicht schreiben, muss ihn aber
**Was:** `Kern/WORKFLOW.md`, Doku-Pflicht, Punkt 3 gilt „immer, bei jedem
Typ": „INDEX nachziehen, falls Dateien dazukamen." `Kern/ASSESSMENT_RULES.md`
sagt für dieselbe Session: „Geschrieben wird ausschließlich in
`Kern/Zeugnisse/<Datum>.md` und `Kern/ARTIFACT_INDEX.md`; die ROADMAP …,
sonst nichts."
**Warum es zählt:** Bei jedem Zeugnis kommt genau eine Datei dazu — das
Zeugnis selbst. Der Fall tritt also **immer** ein, nicht selten.
**Vorschlag:** In `ASSESSMENT_RULES.md` den erzeugten INDEX ausnehmen:
Er wird nicht geschrieben, sondern neu erzeugt, und fällt deshalb nicht
unter „fremde Dateien anfassen".
**Gewicht:** lohnt sich

### A24 — Die offenen Design-Fragen sind nummeriert und sollen über Namen zitiert werden
**Was:** `Kern/GDD_RULES.md` verlangt beides: „Offene Design-Fragen —
**nummeriert**" (Aufbau) und „Die ROADMAP darf sie als Aufgabe aufnehmen,
aber nur über einen Verweis (**Pfad + Überschrift**)". Die fünf Fragen in
`Projekte/Isor_Tower/GDD.md` haben keine Überschrift, nur eine Nummer.
**Warum es zählt:** Ein Verweis kann damit nur „GDD, Frage 3" lauten —
also der Positionsverweis, den `DOC_RULES.md` verbietet. Und Fragen
werden gestrichen, sobald sie beantwortet sind: Die Nummern rutschen
garantiert.
**Vorschlag:** Fragen als fettgedruckte Stichzeile führen
(`**Village-Größe:** bleibt es bei ~2 km …`) statt als Nummernliste.
`GDD_RULES.md` „nummeriert" durch „mit Stichzeile" ersetzen.
**Gewicht:** lohnt sich

### A25 — Nach dem Archivieren zeigt die Kern-ROADMAP ins Leere
**Was:** `Kern/ROADMAP.md`, Abschnitt „Läuft gerade": „Überholung auf
Version 1.0.0. Stand und Reihenfolge in `PLAN.md`, Befunde in
`_HARNESS_REVIEW.md`, Handgriffe in `_HARNESS_UMSETZUNG.md`." Beide
Review-Dateien werden im letzten Phase-8-Schritt archiviert.
**Warum es zählt:** Der Punkt ist dann zugleich erledigt und tot. Fällt
niemandem auf, weil er beim Archivieren nicht mitgelesen wird.
**Vorschlag:** In denselben Handgriff aufnehmen: Punkt abhaken, nach
`Kern/LOG.md` als Ereignis, Verweise entfernen. Gehört zu derselben
Schlussliste wie A10.
**Gewicht:** muss

### A26 — Das LOG bricht sein eigenes Format
**Was:** `Kern/LOG.md` gibt vor: „`- JJJJ-MM-TT — Ereignis (1–3 Sätze…)`".
Die drei Einträge zur Überholung sind 9, 11 und 9 Zeilen lang.
**Warum es zählt:** Wenig — eine Chronik kann nicht falsch werden. Aber
die Formatzeile ist damit eine Regel, der die Datei selbst nicht folgt,
und das lädt zum Weiterwachsen ein.
**Vorschlag:** Format auf „1–3 Sätze, bei einem Umbau mehrerer Dateien
bis zu einem Absatz" erweitern, statt die Einträge zu kürzen — sie sind
inhaltlich in Ordnung.
**Gewicht:** bei Bedarf

### A27 — Das GDD trägt zwei Ereignisse
**Was:** `Projekte/Isor_Tower/GDD.md`, Abschnitt „Umfang und Ziel": „Das
Portfolio von Semester 2 ist am 2026-08-20 hochgeladen. **Seit dem
2026-08-22 läuft die zweite Phase**." Beides sind datierte Ereignisse —
Besitzer ist das LOG der Schicht. Die Datei erklärt zehn Zeilen weiter
oben, warum sie bewusst keinen Stand-Stempel trägt.
**Warum es zählt:** Gering, aber es ist der Anfang genau des Verfalls,
gegen den der fehlende Stand-Stempel schützen sollte.
**Vorschlag:** Beide Sätze durch einen Verweis auf
`Projekte/Isor_Tower/ROADMAP.md`, Abschnitt „Basiszustand nach der
Abgabe" ersetzen — der steht ohnehin schon daneben.
**Gewicht:** bei Bedarf

---

## Durchgang 6 — Inhaltsschichten

Gelesen: `Uni/ROADMAP.md`, `Uni/LOG.md`, Köpfe von `Uni/DECISIONS.md` und
`Uni/_ARCHIV.md` · `IsorBackup/ROADMAP.md` · `Kern/_ARCHIV.md` ·
`Projekte/Isor_Tower/PREFAB_STATUS.md`, Kopf von `TDD_NOTES.md`, Köpfe
aller sieben `DECISIONS/`-Dateien · maschinelle Formatprüfung über drei
Chroniken und zehn Entscheidungsdateien (`formate_pruefen.py` im
Scratchpad).

Nicht Zeile für Zeile gelesen: die 133 Projekt- und Uni-Entscheidungen,
`TDD_NOTES.md` (588 Z.), die beiden Zeugnisse und `Uni/_ARCHIV.md`
(478 Z.) im Volltext. Begründung: Ihr Inhalt ist Projektwissen, nicht
Harness-Gerüst; ihre Vollständigkeit wurde in Phase 3 dreifach geprüft,
und Format wie Verweise sind hier maschinell abgedeckt. Ein inhaltlicher
Abgleich der Projektentscheidungen gegen den Code gehört in eine
Projekt-Session, nicht in die Harness-Abnahme.

Sauber und ohne Befund: alle zehn Entscheidungsdateien halten ihr
Format (Datum, Titel, Was/Warum) · `Kern/LOG.md` und alle sieben
Projekt-Entscheidungsdateien sind lückenlos chronologisch · in den
Projektentscheidungen steht genau eine offene Frage, sie hat einen
Besitzer.

### A28 — Drei Chroniken haben ihre Reihenfolge verloren
**Was:** Alle LOGs sagen im Kopf zu: „datierte Ereignisse, **älteste
oben**". Geprüft ergibt das drei Sprünge rückwärts:
`Uni/LOG.md` Z.37 (2026-08-09 nach 2026-08-11) und Z.47 (2026-08-12 nach
2026-08-20) · `Projekte/Isor_Tower/LOG.md` Z.444 (2026-07-29 nach
2026-08-20).
**Warum es zählt:** Die Ursache ist bei allen dreien dieselbe und steht
in `Kern/_ARCHIV.md`: Beim Auflösen des „Erledigt"-Blocks in Phase 3
wanderten „GDD.md als Short GDD angelegt" ins Projekt-LOG und
„Abgabe-Ordnerstruktur gebaut" ins Uni-LOG — **angehängt statt nach
Datum einsortiert**. Eine Chronik „kann nie falsch werden" (DOC_RULES),
solange ihre Ordnung stimmt; genau die ist hier gebrochen, und beim
letzten Eintrag fällt es am wenigsten auf.
**Vorschlag:** Die drei Einträge an ihr Datum schieben. Dazu eine Zeile
in `DOC_RULES.md` Abschnitt 4: Wer einen Eintrag in eine Chronik
**nachträgt**, sortiert ihn nach Datum ein — Anhängen ist nur für das
Heutige richtig.
**Gewicht:** lohnt sich

### A29 — Sieben Geschwisterdateien, keine benennt ihre Grenze
**Was:** Die sieben Dateien unter `Projekte/Isor_Tower/DECISIONS/` tragen
identische Köpfe bis auf das Thema: „Nur Entscheidungen zu Audio /
Entities und KI / Gras und Instancing / Platzierung / Terrain und Mesh /
UI, Menüs und HUD / Welt, Szene und Interaktion". `DOC_RULES.md`
Abschnitt 3 verlangt von der Ownership-Zeile aber ausdrücklich, auch zu
sagen, **was sie nicht besitzt**. Alle sieben grenzen sich nur gegen
ROADMAP, LOG und die Regeldateien ab — nicht gegeneinander.
**Warum es zählt:** Bei sieben Dateien mit gleichem Zweck ist genau das
die Grenze, die zählt. Gehört eine Entscheidung zum Wasserspiegel nach
`Welt` oder nach `Terrain_Mesh`? (Sie liegt in `Terrain_Mesh`.) Eine zur
Gras-Verteilung nach `Gras` oder `Platzierung`? Phase 3 hat die
Zuordnung von Hand entschieden — die Regel dafür ist mit der Bauliste
weg, sobald sie archiviert wird. Derselbe Mechanismus wie A10.
**Vorschlag:** Je eine Halbzeile „Nicht hier: …" in jeden der sieben
Köpfe, mit dem Geschwister, das den Grenzfall bekommt. Vier Zeilen
Arbeit, und die Frage „wohin damit" ist beim nächsten Eintrag
beantwortet.
**Gewicht:** lohnt sich

### A30 — Das Archiv erklärt für abgelöst, worauf sich eine geltende Regeldatei beruft
**Was:** `Kern/_ARCHIV.md` führt den Eintrag „2026-08-16 —
Versionsschema nach Reifegrad" unter der Überschrift „Zwei **abgelöste**
Konventions-Einträge", abgelöst durch `Kern/VERSIONIERUNG.md`.
`VERSIONIERUNG.md` behandelt denselben Eintrag als weiterhin geltend:
„**Grundentscheidung:** DECISIONS 2026-08-16 … Semantic Versioning wurde
**dort** ausdrücklich verworfen" und, über die eigene Ergänzung,
„*ergänzt die Entscheidung vom 2026-08-16, ohne sie umzustoßen*".
**Warum es zählt:** Zwei aktive Dateien sagen Gegenteiliges über
denselben Eintrag — der Widerspruchs-Test aus `DOC_RULES.md` Abschnitt 1,
angewandt aufs Archiv. Praktisch: `VERSIONIERUNG.md` verweist auf eine
Grundlage, die als überholt markiert ist.
**Vorschlag:** Der Eintrag wurde nicht abgelöst, sondern **fortgeführt**.
Ihn aus dem Abschnitt „abgelöst" herausnehmen und stattdessen in
`Kern/DECISIONS.md` belassen mit der Zeile „Fortgeführt am 2026-08-22:
geltende Fassung `Kern/VERSIONIERUNG.md`" — genau das Muster, das Phase 4
bei zwei anderen Einträgen benutzt hat. Beim Sprach-Eintrag daneben
stimmt „abgelöst" dagegen.
**Gewicht:** muss

### A31 — Die IsorBackup-Schicht ist nicht vollständig gebaut
**Was:** Drei Lücken, die zusammengehören.
(1) `IsorBackup/DECISIONS.md` sagt im Kopf: „Überholte Einträge wandern
nach `_ARCHIV.md` der Schicht." Diese Datei existiert nicht und steht
auch nicht in `index_geplant.txt` — anders als das Projekt-Archiv, das
dort korrekt als geplant geführt wird.
(2) Die Schicht hat **kein LOG**, als einzige der vier.
(3) `IsorBackup/ROADMAP.md` trägt deshalb einen Abschnitt „Erledigt, hier
nur als Zeiger" — in einer Datei, deren Ownership-Zeile „**nur** die
offenen Aufräum-Punkte" sagt. Ein „Erledigt"-Block in einer ROADMAP ist
genau der Befund, der die Überholung am 2026-08-21 ausgelöst hat
(`Kern/STOERUNGEN.md`, erster Eintrag).
**Warum es zählt:** (3) ist die Folge von (2): Der Zeiger steht dort,
weil es keinen anderen Ort gibt. Die Testphase fängt mit dieser Schicht
an — sie wird die erste sein, die Ereignisse produziert.
**Vorschlag:** `IsorBackup/_ARCHIV.md` in `index_geplant.txt` aufnehmen
(anlegen erst, wenn etwas hineingehört). Über das LOG entscheiden: Ich
empfehle, eines anzulegen, sobald der erste Aufräum-Durchgang läuft —
dann hat der „Erledigt"-Zeiger sein Zuhause und kann aus der ROADMAP
verschwinden. Vorher ersatzlos streichen: Die gerettete Export-Regel
besitzt `Kern/DIAGRAM_RULES.md`, das Ereignis besitzt `Kern/LOG.md`
(Phase 7).
**Gewicht:** lohnt sich

### A32 — Zwei Prefabs sehen im Prüfstand gleich aus
**Was:** `Projekte/Isor_Tower/PREFAB_STATUS.md`, Abschnitt
`Prefabs/Torch`, führt zwei Zeilen: `Torch` (Status Befund) und `Torch `
(Status offen). Der Unterschied ist ein Leerzeichen am Ende — im
gerenderten Markdown unsichtbar. Dass es zwei Dateien gibt, ist Absicht
(Isor, 2026-08-12: eine ruhig, eine mit mehr Funken).
**Warum es zählt:** Nicht die Anzeige ist das Risiko, sondern der
Schlüssel: Der Kopf der Datei sagt, „Status und Befund kommen von Hand
und werden bei jedem Lauf übernommen" — die Übernahme läuft über den
Namen. Sobald irgendwo getrimmt wird, fallen die beiden Einträge
zusammen und ein von Hand geschriebener Befund landet am falschen
Prefab. Derselbe Fall wie `WaterPond (1)`/`(2)`, nur unsichtbar.
**Vorschlag:** Im Skript den Namen mit sichtbarer Markierung ausgeben,
wenn er auf Leerzeichen endet (etwa `Torch␣`), und beim Zuordnen nicht
trimmen. Das Umbenennen selbst steht schon in der Projekt-ROADMAP.
**Gewicht:** lohnt sich

### A33 — Kleinkram, gesammelt
**Was:** Drei Einzelheiten ohne eigenes Gewicht.
(1) `PREFAB_STATUS.md` verweist zweimal auf „`ROADMAP.md` → …" ohne
Schicht; `DOC_RULES.md` Abschnitt 6 verlangt Pfad **und** Überschrift,
und es gibt drei ROADMAPs.
(2) `Projekte/Isor_Tower/DECISIONS/Terrain_Mesh.md`, Eintrag 2026-08-19,
endet mit „Offen geblieben: Der Wasserspiegel hat bewusst keinen
Collider" — die einzige offene technische Frage im Projekt, und sie steht
in keiner ROADMAP als Aufgabe.
(3) Die Entscheidungsdateien sind faktisch chronologisch sortiert, aber
drei Einträge stehen aus der Reihe (`Kern/DECISIONS.md` Z.108,
`Uni/DECISIONS.md` Z.293 und Z.302). Die Format-Zeile verlangt keine
Reihenfolge — deshalb kein Verstoß, aber eine unausgesprochene Ordnung.
**Vorschlag:** (1) Schicht ergänzen. (2) Eine Zeile in die
Projekt-ROADMAP unter „Aufräumen und Konventionen", mit Verweis statt
Abschrift. (3) Entweder die Reihenfolge in die Format-Zeile aufnehmen
oder die drei Einträge in Ruhe lassen — meine Empfehlung ist Ersteres,
weil die Sortierung ohnehin schon eingehalten wird.
**Gewicht:** bei Bedarf

---

# Antworten auf die Punkte von Phase 8

## Haken gegenprüfen — drei falsche gefunden

| Bauliste | Haken | Wirklichkeit |
|---|---|---|
| Phase 1 | Auslieferungs-Ordner anlegen | Ordner existiert nicht (A20) |
| Phase 4 | vier Aufgabentexte nachtragen | Dateien fehlen, Punkt steht offen in `Uni/ROADMAP.md` (A21) |
| Phase 4 | ARTIFACT_INDEX-Eintrag vorbereiten | inzwischen erledigt, Störung steht noch auf „offen" (A7) |

Der Vorfall vom 2026-08-22 war also kein Einzelfall — bei 60 Handgriffen
an einem Tag sind drei Haken nicht gedeckt, einer davon in die andere
Richtung. Das ist die Antwort auf die Frage, ob sich die Regel „wer
abhakt, nennt die Datei" lohnt: ja.

## Offene Störungen — es sind drei, nicht eine

`Kern/STOERUNGEN.md` hat acht Einträge. Unbehoben sind:

1. **Angekündigte Fragen nicht gestellt** (2026-08-21) — reiner
   Ausführungsfehler, keine Regel möglich. Steht auf „beobachten". In
   dieser Abnahme nicht wieder aufgetreten; ich schlage vor, ihn nach
   einer weiteren Session ohne Wiederholung auf behoben zu setzen.
2. **Berechtigungsliste wächst nach** — die zwei Einträge sind entfernt,
   die Ursache liegt in der Bedienung („dauerhaft erlauben" hängt den
   vollen Befehlstext an). Keine Datei kann das lösen; die Regel „bei
   einmaligen Befehlen *nur diesmal* wählen" ist der ganze Hebel.
3. **Regel überlebte in einer Erledigt-Liste** — behoben, aber mit einer
   Frage an die Abnahme: Wird daraus eine Harness-Regel? **Ja, empfohlen.**
   A10 zeigt denselben Fall ein zweites Mal (die Ausnahme für die
   Diagramm-Skripte lebt nur in Phase 5 der Bauliste), A29 ein drittes
   (die Zuordnungsregel der sieben Entscheidungsdateien). Dreimal
   derselbe Mechanismus ist kein Zufall mehr.

Dazu **A7**: *Haken gesetzt, Arbeit nicht getan* ist erledigt und steht
falsch auf „offen".

## Begriff „Befund" — Vorschlag zur Klärung

Die Lücke steht in `Kern/GLOSSARY.md`, Abschnitt „Ohne Besitzer". Der
Begriff wird an fünf Stellen benutzt: Abnahme, Review-Gate
(`CODE_GUIDELINES.md`), Prüfstand (`PREFAB_STATUS.md` führt ihn sogar als
Status-Wert), Zeugnis („was auffällt, wird Befund — nicht Umbau") und
Sonntagsabgleich.

> **Befund** — Ergebnis einer Prüfung: eine Stelle, an der etwas falsch,
> doppelt, widersprüchlich ist oder fehlt. Entsteht beim gezielten
> Hinsehen und wird notiert, nicht sofort geändert.
>
> **Störung** — ein Vorfall im Betrieb: Der Harness hat nicht so
> gearbeitet wie vorgesehen. Entsteht beim Arbeiten, nicht beim Prüfen.

**Trennlinie in einem Satz: Ein Befund ist ein Zustand, eine Störung ein
Ereignis.** Ein Befund kann eine Störung nach sich ziehen — nämlich dann,
wenn er zeigt, dass eine Regel nicht gegriffen hat —, aber die meisten
tun das nicht. A20 (der Ordner fehlt) ist ein Zustand; die zugehörige
Störung („Haken gesetzt, Arbeit nicht getan") steht längst da und
braucht keinen zweiten Eintrag.

**Besitzer:** `Kern/WORKFLOW.md`, Abschnitt „Begriffe" — dort stehen
bereits Session, Abschnitt und Baustein, also die anderen
schichtübergreifenden Arbeitsbegriffe. `GLOSSARY.md` zieht die Kurzform
nach, der Abschnitt „Ohne Besitzer" entfällt.

## INDEX-Blindstelle — Vorschlag zur Entscheidung

Die Frage lautete: Skript erweitern oder Ausnahme benennen. **Empfehlung:
erweitern** — und zwar zusammen mit A19, weil beides dasselbe Loch ist.

Betroffen sind nicht nur die fünf Auslöser, sondern auch
`Harness Project\CLAUDE.md` (die einzige Datei, die automatisch lädt, und
Trägerin des Notkerns) und `My Harness Development\CLAUDE.md`. Eine
Ausnahme zu benennen hieße, ausgerechnet den Notkern aus dem Register zu
nehmen — den Text also, der schon per Bauart eine Kopie ist und deshalb
am ehesten auseinanderlaufen kann.

Der Weg, der beide Befunde auf einmal schließt: Die fünf Auslöser als
`Kern/Befehle/` **ins Repo**, von dort beim Einrichten nach
`.claude\commands\harness\` kopieren. Dann sind sie versioniert, stehen
im INDEX und gehen mit der Auslieferung mit. Das Skript bekommt
zusätzlich die beiden Wegweiser-`CLAUDE.md` und führt sie in einem
eigenen INDEX-Abschnitt.

## Artifact-Seite `⚙️ System · Harness`

Nicht jetzt. `Kern/ARTIFACT_INDEX.md` regelt es selbst: „Gebaut wird sie
erst, wenn der Kern nach der Abnahme steht; vorher beschriebe sie eine
Baustelle." Mit 15 offenen „muss"-Befunden ist der Kern noch Baustelle.
Reihenfolge: Befunde beheben → Seite bauen → Auslieferung.

---

# Woher die Befunde kommen

Nachträgliche Auswertung (Isors Frage, 2026-08-22): Liegt das Problem bei
den Regeln, beim Altbestand oder woanders? Dieselben 33 Befunde, nicht
nach Gewicht sortiert, sondern nach **Ursache**.

| Ursache | Anzahl | Befunde |
|---|---|---|
| **Nahtstellen des Umbaus** vom 21./22.08. | 14 | A1, A2, A7, A8, A10, A14, A15, A16, A18, A20, A25, A28, A29, A30 |
| **Regel unscharf oder zu eng** | 6 | A3, A4, A5, A23, A24, A26 |
| **Altbestand folgt der Regel nicht** | 6 | A11, A12, A13, A21, A27, A32 |
| **Struktur gedacht, nicht fertig gebaut** | 4 | A6, A17, A19, A31 |
| gemischt | 3 | A9, A22, A33 |

**Die größte Gruppe ist keine der beiden erwarteten.** Nicht die Regeln
und nicht der Altbestand, sondern die **Nahtstellen** — Verweise, die auf
die alten Orte zeigen; Statuszeilen, die beim Umzug nicht mitgezogen
wurden; Haken ohne Deckung; Begründungen, die in temporären Baulisten
liegengeblieben sind. Alle vierzehn sind an einem einzigen Tag
entstanden, nämlich beim Umbau selbst.

**Der Altbestand ist besser dran als vermutet.** Die maschinelle
Formatprüfung über zehn Entscheidungsdateien mit 133 Einträgen meldet
**null** Formatfehler; nach der Korrektur von A28 melden alle drei
Chroniken **null** Reihenfolge-Sprünge. Die sechs Altbestand-Befunde sind
Einzelstücke ohne gemeinsames Muster — der schwerste (A13) ist auch
keine Formatfrage, sondern eine inhaltlich überholte Regel.

**Folgerung für die Frage „müssen wir alle Inhalte ins neue Format
bringen?": Nein.** Ein pauschaler Formatdurchgang über den Altbestand
wäre Arbeit ohne Ertrag — Phase 3 hat ihn bereits geleistet und dreifach
geprüft. Was sich lohnt, ist das Gegenteil: die vierzehn Nahtstellen
schließen und danach maschinell offenhalten (Empfehlung 4). Das ist
derselbe Schluss, den `DOC_RULES.md` Abschnitt 5 schon zieht — nur hier
angewandt auf die Prüfung statt auf das Erzeugen.

---

# Empfehlungen

Getrennt nach Gewicht, wie in Phase 8 verlangt.

## Muss — bevor die Testphase beginnt

1. **Die 15 „muss"-Befunde abarbeiten**, allen voran **A13**: die
   Ordnerstruktur in `CODE_GUIDELINES.md`. Es ist der einzige Befund, bei
   dem eine *falsche Regel* dasteht statt eines falschen Verweises — wer
   danach handelt, baut die vor zwei Tagen aufgelöste Struktur nach.
2. **Vor dem Archivieren der Review-Dateien durchsuchen, was nur dort
   lebt.** Drei Fälle sind schon belegt (A10, A21, A29). Die
   Phasen-Vorbemerkungen sind die Kandidaten: Phase 5 „Ablage
   entschieden", Phase 6 „Fund an der Repo-Grenze", Phase 2 und 4
   „Zusätzlich zur Planung erledigt". Dieser Schritt gehört **vor** den
   letzten Punkt von Phase 8, nicht hinein.
3. **Auslieferung zuletzt** — Ordner anlegen (A20), Befehle mitnehmen
   (A19), erst dann `Harness_1.0.0`.

## Lohnt sich

4. **Die Prüfskripte behalten.** Für diese Abnahme sind zwei entstanden:
   `verweise_pruefen.py` (alle Dateiverweise gegen den Bestand) und
   `formate_pruefen.py` (Chronik-Reihenfolge, Pflichtfelder der
   Entscheidungen). Sie haben **6 der 33 Befunde allein gefunden** — und
   zwar genau die Sorte, die beim Lesen durchrutscht: tote Verweise,
   verdrehte Reihenfolge, nicht gedeckte Haken. Beides zusammen als
   `Kern/Werkzeuge/pruefen.py` in die Kern-Schicht, Aufruf am Pflegetag
   als dritter Punkt neben Artifact-Durchsicht und Backup.
   Begründung aus dem eigenen Regelwerk: `DOC_RULES.md` Abschnitt 5
   („erzeugen statt pflegen") und die Störungslehre „die Bauliste prüft
   sich selbst nicht".
   *Die Skripte liegen im Scratchpad und sind Wegwerfstand — sie müssten
   für den Dauerbetrieb zusammengefasst und aufgeräumt werden. Rund eine
   halbe Stunde.*
5. **Haken-Format ändern**, statt eine Verhaltensregel zu formulieren:
   Ein abgehakter Punkt nennt die geänderte oder angelegte Datei. Eine
   Formatvorgabe wird befolgt, eine Verhaltensregel vergessen — das ist
   der Unterschied zwischen den drei falschen Haken und den 57 richtigen.
6. **Ersten Pflegetag laufen lassen**, bevor der Stand als 1.0.0
   ausgeliefert wird (A12). Der Befehl ist gebaut und noch nie gelaufen;
   alle Artifact-Stände sind älter als der Umbau.
7. **Die 14 „lohnt sich"-Befunde** in einem Zug, sie sind alle klein.

## Nur bei Bedarf

8. **Die vier „bei Bedarf"-Befunde** (A11, A26, A27, A33) — sie kosten
   nichts, wenn sie liegen bleiben.
9. **Nicht vorziehen:** Tests für `CODE_GUIDELINES`, `SYSTEME.md`-Skript,
   Markdown→`.docx`. Alle drei stehen begründet auf `Kern/ROADMAP.md` und
   gehören nicht in die Abnahme.
10. **Nicht anfassen:** „Harness auf Englisch". Die Bedingung dafür
    (Weitergabe an jemanden) steht nicht an.

## Einschätzung zum Ganzen

33 Befunde auf 50 Dateien und rund 9.400 Zeilen, davon 15 mit Gewicht
„muss" — und von diesen 15 trägt genau **einer** inhaltlichen Schaden
(A13). Alle übrigen sind Verweise, Haken, Statuszeilen und Namen: Dinge,
die sich in Stunden beheben lassen, nicht in Tagen.

Das Regelwerk selbst hält. Auffällig ist, wie oft es sich **selbst
überführt** hat: Die Ownership-Regel findet die Dublette in
KNOWLEDGE_RULES, die Verweisregel findet ihre eigenen Verstöße in
DIAGRAM_RULES, die Stand-Stempel-Regel findet den falschen Zähler in
CLAUDE.md. Ein Regelwerk, dessen Regeln die eigenen Fehler benennen, ist
brauchbar. Die Lücke liegt nicht bei den Regeln, sondern beim
**Nachweis** — dass etwas getan wurde, wird bisher behauptet und nicht
belegt. Genau da setzen die Empfehlungen 4 und 5 an.
