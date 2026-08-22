# _HARNESS_UMSETZUNG.md — Bauliste der Harness-Überholung

Ownership: Nur die abzuarbeitenden Handgriffe der Überholung, in
Baureihenfolge. Befunde und Begründungen stehen in `_HARNESS_REVIEW.md`,
die E-Nummern verweisen dorthin. Temporär — wird nach Abschluss
archiviert, INDEX-Eintrag entfernt.

Reihenfolge-Grundsatz: **Regeln → Struktur → Inhalt → Automatik.**
Erst gilt eine Regel, dann richtet sich die Ablage danach, dann zieht der
Inhalt um, zuletzt wird automatisiert. Wer umgekehrt vorgeht, baut zweimal.

Vor Phase 3 (erstem Umzug): **Commit des Ist-Standes** — Rückweg sichern.

---

## Phase 1 — Regeln schreiben (es wird nichts verschoben)

- [x] `Kern/DOC_RULES.md` neu anlegen — die 15 Regeln aus E64
- [x] darin: Sprachtabelle, eine Zeile je Erzeugnis (E70)
- [x] ~~darin: Zuständigkeits-Tabelle aus Schritt F~~ — **gestrichen
      2026-08-22.** Wäre eine Kopie gewesen: Wer was besitzt, steht in
      jeder `Ownership:`-Zeile und gesammelt im erzeugten INDEX.
      DOC_RULES besitzt das Verfahren, der INDEX das Ergebnis.
      Stattdessen steht dort ein Verweis.
- [x] darin: „Vor einem Ownership-Befund die Ownership-Zeile **aller**
      beteiligten Dateien lesen" (aus STOERUNGEN, 2026-08-21)
- [x] `Kern/GDD_RULES.md` neu anlegen (E60) — Aufbau und Pflege eines GDD,
      `offen`-Mechanismus, wann aus Entwurf feste Absicht wird
- [x] `Kern/VERSIONIERUNG.md` neu anlegen (E77–E80) — die drei
      Nummernsysteme und ihre Lesarten
- [x] CLAUDE.md bekommt die Zeile `Harness-Version: 1.0.0` (E79)
- [x] Auslieferungs-Ordner anlegen:
      `C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\` (E80)
- [x] Erste Auslieferung `Harness_1.0.0` erst **nach Phase 7**, wenn der
      Kern vollständig ist

## Phase 2 — Struktur anlegen — **erledigt 2026-08-22**

Zusätzlich zur Planung erledigt: 17 Dateien mit geklärter Schicht wurden
gleich mitverschoben (statt erst in Phase 4), der INDEX wurde nach
Schichten neu geschrieben, und `_split_check.txt` ist archiviert.
Oben blieben nur `CLAUDE.md` (Automatik-Ladung, siehe P1), `INDEX.md`
(Register über alle Schichten), `PLAN.md` sowie die vier Dateien, die in
Phase 3 **aufgeteilt** statt verschoben werden.


- [x] Ordner `Kern/`, `Uni/Semester_2/`, `IsorBackup/`,
      `Projekte/Isor_Tower/` (E11, E50)
- [x] `PLAN.md` anlegen, max. ~100 Zeilen, wird nach jedem Zeitraum
      geleert (E12)
- [x] `Kern/STOERUNGEN.md` anlegen (E16) + die zwei ersten Einträge
- [x] `Kern/Zeugnisse/` anlegen (E53)

## Phase 3 — Große Bestände umziehen (skriptgestützt)

**DECISIONS (1.790 Zeilen, 133 Einträge)** — **erledigt 2026-08-22**
- [x] Zuordnung von Hand festgelegt, Eintrag für Eintrag — keine
      Schlagwort-Automatik
- [x] die 15 Konventions-Einträge offengelegt, die vier strittigen
      einzeln entschieden (E8): „Pipeline-Klassen loggen nicht" → Terrain
      (meint konkret die Terrain-Pipeline) · „Unity-Ordner folgen den
      Uni-Systemgrenzen" → Kern mit Herkunftsvermerk · „Assets nach Typ" →
      Kern · zwei abgelöste Einträge (Sprache, Versionsschema) → Archiv
- [x] Terrain feiner geschnitten als geplant: statt einer Datei mit 38
      Einträgen drei — Platzierung 21, Terrain_Mesh 13, Gras 5
- [x] Skript trennt an `## `-Überschriften (E10)
- [x] **Dreifach geprüft:** 133 rein / 133 raus · 1.651 nicht-leere
      Rumpfzeilen identisch · unabhängig gegen die committete Fassung
      geprüft, alle 133 Überschriften vorhanden
- [x] Endstand: `Kern/DECISIONS.md` 27 · `Uni/DECISIONS.md` 22 ·
      Platzierung 21 · UI 16 · Terrain_Mesh 13 · Welt 11 · Audio 9 ·
      Entities 7 · Gras 5 · Kern-Archiv 2
- [x] Original nach `99_Archiv\_Zu_Loeschen\2026-08-22_Harness_Umbau\`

**Phase 3 ist damit abgeschlossen — alle fünf Umzüge durch.**

**Aus „Arbeitsregeln, die weiter gelten" — in Phase 4 einsortieren**
Sechs Punkte aus dem archivierten Abgabe-Block. Es sind **Regeln und
Fakten, keine Aufgaben** — sie gehören daher nicht in eine ROADMAP:
- [x] → `Uni/DOCX_RULES.md`: Arbeitsdatei ist ausschließlich
      `01_Uni\Semester_2\Arbeitsdateien\TDD Softwareplanung.docx`,
      Sicherungen unter `Arbeitsdateien\Sicherung\`. Beim Einsortieren
      gegen E61b prüfen — der Text lebt künftig in Markdown.
- [x] → `Uni/DOCX_RULES.md`: Verweis auf die Abgabe-Packliste
      `Arbeitsdateien\Abgabe_Packliste.txt` („die ROADMAP sagt *wann*,
      die Packliste sagt *was wohin*").
- [x] → `Kern/WORKFLOW.md`, beim Regler „Wer schreibt": **Arbeitsteilung
      am Text** (Isor, 2026-08-08). Korrekturen an bestehendem Text
      schreibt Claude direkt; neue Fachkapitel formuliert Isor selbst,
      Claude liefert Struktur, geprüfte Zahlen und glättet hinterher.
      Grund: Der Text soll von ihm kommen, und das Durchgehen ist
      zugleich das Lernen des Stoffs.
- [x] → `Uni/DECISIONS.md`: Unity-Version `6000.5.2f1` weicht von den
      beiden in der Vorgabe genannten ab; die Dozentin hat persönlich
      freigegeben, dass eine eigene Version gewählt werden darf
      (Isor, 2026-08-12). Kein Handlungsbedarf, nur festgehalten.
- [x] → `Uni/DECISIONS.md`: Prefab-Painter wird im TDD nicht erwähnt
      (Isor, 2026-08-07), bleibt aber in der Projektkopie (2026-08-11).
- [x] **gestrichen:** „Word-Felder: Beschriftungen und Verweise sind
      Felder" — steht wörtlich in `Uni/DOCX_RULES.md`, Abschnitt Felder.
      Reine Dublette.

**ROADMAP (708 Zeilen, davon 546 Vergangenheit — C8)** — **erledigt 2026-08-22**
- [x] „Erledigt"-Block aufgelöst: 7 Harness-Bauten → `Kern/LOG.md`,
      GDD-Anlage → Projekt-LOG, Abgabe-Ordnerstruktur → Uni-LOG, der Rest
      als Dublette der LOGs nicht übernommen (begründet in `Kern/_ARCHIV.md`)
- [x] Abgabe-Block (498 Z.) → `Uni/_ARCHIV.md`; Prüfung: 457 archiviert +
      41 zurückbehalten = 498, keine Zeile verloren
- [x] „Arbeitsregeln, die weiter gelten" zurückbehalten — sind Regeln und
      Fakten, keine Aufgaben; Einsortierung siehe Abschnitt oben
- [x] „Restliste Politur" → Projekt-ROADMAP, bereinigt um Ton und Menü
      (gebaut am 14./16.08.) und um die `SheepSense`-Dublette
- [x] Rest verteilt: `Kern/ROADMAP.md` 50 Z. · `Uni/ROADMAP.md` 25 Z. ·
      `Projekte/Isor_Tower/ROADMAP.md` 129 Z. — aus 708 Zeilen wurden
      204 Zeilen Baureihenfolge und 521 Zeilen Archiv
- [x] die zwei „Offenen Punkte" aus ARTIFACT_INDEX aufgenommen (E46)
- [x] Tests-Lücke aufgenommen (E56)
- [x] ClaudeSetup steht nur noch in `Kern/ROADMAP.md` (E55)
- [x] „Harness auf Englisch" als Bedingung formuliert (E83)
- [x] Grobziel gestrichen (steht in CLAUDE.md), Nahziel archiviert
- [x] Original nach `99_Archiv\_Zu_Loeschen\2026-08-22_Harness_Umbau\`

**FEATURE_LOG (497 Zeilen, 73 Einträge)** — **erledigt 2026-08-22**
- [x] verteilt auf drei Chroniken nach der Regel „ein Ereignis gehört der
      Schicht, für die es gemacht wurde": Projekt 64 · Uni 6 · Kern 3
- [x] Prüfung bestanden: 490 nicht-leere Rumpfzeilen, Inhalt identisch
- [x] Kopf jeder Chronik nach E13 und E85: nie geändert, kein Archiv;
      Ablageorte erlaubt als Stand von damals
- [x] Widerspruch C7 aufgelöst — es gibt jetzt `Kern/LOG.md`, die alte
      Zeile „Harness-Bauten stehen in ROADMAP" ist mit der Datei weg
- [x] Original nach `99_Archiv\_Zu_Loeschen\2026-08-22_Harness_Umbau\`

**TDD_NOTES (556 Zeilen, 85 Einträge)** — **erledigt 2026-08-22**
- [x] nach `Projekte/Isor_Tower/` verschoben (E51, in Phase 2)
- [x] nach **zehn Themenblöcken** gegliedert: Terrain & Mesh 19 ·
      Platzierung 15 · Architektur & Muster 10 · Performance & Threading 9 ·
      Werkzeuge 9 · Interaktion & UI 9 · Audio 7 · Welt & Persistenz 3 ·
      Rendering 2 · Lizenzen & Quellen 2
- [x] Zeitfolge innerhalb jedes Blocks erhalten, Marken im Text
      unverändert gelassen — sie tragen teils Kapitelhinweise
      (`[Kapitel 14, Änderungsverlauf]`), die sonst verloren gingen
- [x] Kopf neu: Ownership, Format, Begründung für die Projekt-Schicht;
      veraltetes „Abgabe ca. 2026-07-28" entfernt (C3-a)
- [x] **Doppelte Prüfung bestanden:** Skript meldet 545 = 545 nicht-leere
      Rumpfzeilen identisch; unabhängig davon gegen die committete Fassung
      geprüft — alle 85 Eintragszeilen Zeichen für Zeichen gleich
- Befund am Rande: Fünf Marken benannten ein TDD-Kapitel statt ein Thema
  (`[Kapitel 14]`, `[Kapitel 6.5]`, `[Abgabe]`, `[Formate]`, `[Planung]`).
  Inhaltlich sind alle fünf Projekt-Stoff — sie wurden thematisch
  einsortiert, der Kapitelhinweis bleibt im Text stehen.

**ASSESSMENT_LOG (782 Zeilen, 2 Zeugnisse)** — **erledigt 2026-08-22**
- [x] aufgetrennt in `Kern/Zeugnisse/2026-08-11.md` und `2026-08-16.md` (E53)
- [x] Prüfung bestanden: 17 von 17 `###`-Abschnitten angekommen,
      650 nicht-leere Rumpfzeilen **Zeile für Zeile identisch**
- [x] Original nach `99_Archiv\_Zu_Loeschen\2026-08-22_Harness_Umbau\`
- [x] Ablage-Regel in ASSESSMENT_RULES nachgezogen (sie nannte die
      gelöschte Sammeldatei)
- Trennskript liegt im Scratchpad und wird für DECISIONS wiederverwendet

## Phase 4 — Einzeldateien nachziehen — **erledigt 2026-08-22**

Zusätzlich zur Planung erledigt: eine **Gesamtprüfung auf tote Verweise**
über alle Dateien. Gefunden und repariert wurden Verweise auf
`FEATURE_LOG.md` und `ASSESSMENT_LOG.md` in fünf aktiven Regeldateien,
nackte `DECISIONS.md`-Verweise in CODE_GUIDELINES und GDD, zwei falsche
ROADMAP-Nummernverweise, und ein Fehler von Claude: Die sieben neuen
Projekt-Entscheidungsdateien trugen alle den Titel `# DECISIONS.md`
statt ihres eigenen Namens. Außerdem fehlte zwischen den Einträgen die
Leerzeile — das Trennskript hatte zu streng getrimmt.

Zwei Einträge in `Kern/DECISIONS.md` benutzen weiter die alte
Modus-Sprache. Sie wurden **nicht** archiviert, weil ihre Begründung
weiter gilt — sie haben stattdessen eine Zeile „Fortgeführt am
2026-08-22" mit Zeiger auf die geltende Fassung bekommen (E9).


**CLAUDE.md** — **erledigt 2026-08-22, vorgezogen**
Grund fürs Vorziehen: Nach dem Umzug von Phase 2 zeigte ihre Leseordnung
auf `WORKFLOW.md`, das nun in `Kern/` liegt. Ein kaputter Einstiegspunkt
konnte nicht bis Phase 4 warten.
- [x] `Ownership:`-Zeile ergänzt (E19)
- [x] Doku-Pflicht durch Verweis auf WORKFLOW ersetzt (E17)
- [x] Leseordnung: CLAUDE → INDEX → PLAN → Kern/WORKFLOW (E18)
- [x] die drei Doku-Regeln nach DOC_RULES verschoben (E20)
- [x] Zeile `Harness-Version: 1.0.0` ergänzt (E79)
- [x] Rückfrage-Regel aufgenommen, alte Empfehlungs-Zeile ersetzt (E87)
- [x] Kurzform der Regel „zeigen statt vorstellen lassen" mit Verweis
      auf WORKFLOW (E69)
- [x] **offene Prüfung P1** vorher: welche der drei CLAUDE.md lädt der
      Harness von selbst? Nur in einer frischen Session feststellbar

**WORKFLOW.md**
- [x] besitzt die Doku-Pflicht vollständig (E17)
- [x] besitzt „wann Knowledge geschrieben wird" (E29)
- [x] Modus (Lernmodus/Normal) + zwei Regler (E21)
- [x] Regler-Untergrenze: nie auf inneres Vorstellen ausweichen (E69)
- [x] Erklärstil „zeigen statt vorstellen lassen" (E69)
- [x] „Session" und „Abschnitt" trennen (E67) — Widerspruch „ein Typ" vs.
      „2–4 parallel" auflösen
- [x] „Baustein" definieren samt Fertig-Kriterium (E68)
- [x] `/sichern`, `/wechsel`, `/ende` beschreiben (E23)
- [x] Übergang Design→Development als Kontrollpunkt (E24)
- [x] wiederholte Zeugnis-Doku-Pflicht streichen, nur Verweis (E43)
- [x] Typ „Art" als `(geplant)` kennzeichnen (E22)
- [x] alle Statusvermerke auf den heutigen Stand (E26)

**INDEX.md**
- [x] wird aus den `Ownership:`-Zeilen erzeugt (E25)
- [x] Statusangaben entfernen (E26)
- [x] Nummernverweis „ROADMAP-Punkt 10" durch Namen ersetzen (E27)

**KNOWLEDGE_RULES.md**
- [x] Bestandsliste der Themenordner ersatzlos streichen (E30)
- [x] `README.md` je Themenordner anlegen, eine Zeile (E30)
- [x] Root-`README.md` des Knowledge-Repos: kurze Orientierung (E31)
- [x] „wann" durch Verweis auf WORKFLOW ersetzen (E29)
- [x] „Uni-Modus" → „Lernmodus", Zusatz „in Brainstorm-Sessions" weg (E21)
- [x] Regel: Artifact nur bei visuellen Themen (E32) — Text in ARTIFACT_RULES

**ARTIFACT_RULES.md**
- [x] abgeschriebenen Artifact-Check durch Verweis ersetzen (E33)
- [x] Sonntagsroutine mit Vorschlagsliste beschreiben (E34)
- [x] `🗑` aus der Typentabelle in „Pflege" verschieben (E36)
- [x] Zählwort „Die drei Typen" korrigieren (E41)
- [x] Spalte „Führende Quelle" auf die neue Struktur (B2-d)
- [x] Erklärstil-Regel durch Verweis auf WORKFLOW ersetzen (E69)

**ARTIFACT_INDEX.md**
- [x] Schicht-Angabe je Eintrag, benannte Ausnahme von E11 begründen (E45)
- [x] „Offene Punkte" in die Kern-ROADMAP (E46)
- [x] Stand-Stempel korrigieren (C1-b)
- [x] Review-Gate-Erklärung auf einen Verweis kürzen (C1-a)
- [x] Eintrag für `⚙️ System · Harness` vorbereiten (E35, I12)

**DIAGRAM_RULES.md**
- [x] konkrete Pfade entfernen, Ablage folgt der Schicht (E37)
- [x] Abschnitt für das Zustandsdiagramm (E38)

**DOCX_RULES.md** → Schicht Uni
- [x] die sechs XML-Fallen nach Knowledge auslagern, Verweis behalten (E39)
- [x] Abschnitt „Werkzeuge": docx-Skill, `validate.py` für den Prüfschritt (E40)
- [x] Zählwort „Alle vier" korrigieren (E41)

**ASSESSMENT_RULES.md**
- [x] „Bewertungskriterien liefert die aktive Schicht" (E42)
- [x] „Prüfanker des letzten Zeugnisses — beantwortet" als Pflichtabschnitt (E52)
- [x] Ablageregel auf eine Datei je Zeugnis umstellen (E53)
- [x] Knowledge-Frage auch bei Zeugnissen, Antwort meist „nein" (E44)
- [x] Belegpflicht gegen die Teilabgaben abgleichen (E63)

**CODE_GUIDELINES.md**
- [x] Projekt-Typ aus der Schicht ableiten, eigene Angabe streichen (E54)
- [x] „Bewusst nicht übernommen" nach Art aufteilen (E55)
- [x] Status-Vermerk „Rohmaterial" auf den heutigen Stand (D1-b)
- [x] Ownership-Zeile behält „Tests", Lücke bleibt sichtbar (E56)

**GDD.md** → `Projekte/Isor_Tower/GDD.md`
- [x] Abschnitt „Entwurf" für noch nicht Einsortiertes (E59)
- [x] offene Design-Fragen: GDD ist Besitzer, ROADMAP verweist (E58)
- [x] ist zugleich das Markdown-Manuskript der Abgabe (E71)

**PREFAB_STATUS.md** → Projekt-Schicht
- [x] `VFX_FireFly.prefab` ergänzt sich beim ersten Skriptlauf (C2-b)
- [x] zwei Nummernverweise durch Namen ersetzen (C2-a)
- [x] Ende festlegen: alles `geprüft` → Befunde in die ROADMAP, Datei
      ins Projekt-Archiv (E49)

**ASSIGNMENT_PCG / _TOOL / _THREADING**
- [x] unverändert nach `Uni/Semester_2/` (E50)
- [x] vier fehlende Aufgabentexte nachtragen; wo es keinen gibt, genau
      das als Datei festhalten (E62)

**Streuner**
- [x] `_split_check.txt` nach `99_Archiv\_Zu_Loeschen\` (E66)

## Phase 5 — Erzeugte Dateien und Skripte — **erledigt 2026-08-22**

**Ablage entschieden:** Ein Werkzeug liegt in der Schicht, deren Dateien
es bearbeitet — dieselbe Regel wie für Dokumente. Das INDEX-Skript
wandert damit automatisch mit der Kern-Auslieferung mit. Die
Diagramm-Skripte bleiben, wo sie sind.

Ergebnisse und Funde:
- **INDEX** wird erzeugt; 42 Dateien gefunden, **alle mit
  `Ownership:`-Zeile** — die neue Pflicht greift also schon. Geplante
  Dokumente stehen von Hand in `index_geplant.txt` (11 Einträge). Der
  INDEX führt jetzt auch die Werkzeuge selbst auf, sonst fände sie niemand.
- **PREFAB_STATUS** wird erzeugt; 34 Prefabs in 17 Gruppen.
  *Befund:* Die vier alten Abschnitte (Shared/UI, Entities, Environment,
  Systems) gab es nicht mehr — seit der Umstellung „Assets nach Typ"
  vom 2026-08-20 liegen alle Prefabs unter `Assets/Prefabs/<Thema>/`.
  `VFX_FireFly` ist wie vorhergesagt von selbst aufgetaucht, dazu drei
  weitere, die nie in der Liste standen.
- **Backup** mit drei Sicherungen: Probelauf als Voreinstellung ·
  Erkennungsdatei `_ISOR_BACKUP.txt` auf der Platte (schützt gegen einen
  falschen Laufwerksbuchstaben) · Wegfallendes wandert nach
  `_Geloescht\<Datum>\` statt gelöscht zu werden.
  *Umfang gemessen:* IsorBackup 15,4 GB / 8.729 Dateien, Repos 0,6 GB /
  2.127 Dateien — rund **16 GB** auf der Platte.
  *Korrektur beim Testen:* `.git` war zuerst ausgeschlossen. Ohne
  Historie wäre die Kopie kein Repo mehr, sondern ein Haufen Dateien —
  jetzt drin (das sind die 900 Dateien Unterschied).
  *Windows-Falle:* `.ps1` ohne UTF-8-BOM wird von PowerShell 5.1 als
  ANSI gelesen; Umlaute und Gedankenstriche zerlegen dann die Syntax.


- [x] INDEX-Skript: liest alle `Ownership:`-Zeilen, meldet Dateien ohne
      als `⚠` (E25)
- [x] PREFAB_STATUS-Skript: liest alle `.prefab`, überträgt Status und
      Befund über den Namen (E48)
- [x] Backup-Skript: `robocopy` über die drei Ordner, Wegfallendes nach
      `_Geloescht\<Datum>\` statt löschen (E74, E75)

**Auf die ROADMAP, nicht auf die Wochenendliste:**
- [ ] SYSTEME.md-Skript je Projekt (E14)
- [ ] Markdown→`.docx`-Werkzeug, vorhandenes Layout wird Formatvorlage
      (E61b) — realistisch ein voller Arbeitstag
- [ ] Test-Abschnitt für CODE_GUIDELINES (E56)
- [ ] Repo-/Git-Regeln samt Build-Versionsschema (ROADMAP Punkt 9)
- [ ] Prefab-Innenaufbau (ROADMAP Punkt 7)

## Phase 6 — Befehle und Berechtigungen

- [ ] `/sichern` — Doku-Pflicht abarbeiten, Session läuft weiter (E23)
- [ ] `/wechsel <Typ>` — sichern + Typ umstellen + Modus/Regler neu fragen
- [ ] `/ende` — sichern + Commit-Vorschlag mit V-Nummer + Schluss
- [ ] **Doku-Pflicht ist typabhängig** — eine Zeugnis-Session schreibt in
      andere Dateien als eine Development-Session (B5-c)
- [ ] Knowledge-Frage in `/ende`: Claude schlägt Themen vor, Isor wählt (E2)
- [ ] Störungs-Frage in `/ende` (E16)
- [ ] Sonntagsroutine: Artifact-Durchsicht (E34) + Abgleich gegen die
      veröffentlichten Seiten (E47) + Backup-Erinnerung (E76)
- [ ] `.claude/settings.local.json`: 280 Einträge auf generische Muster
      eindampfen (C5, I5)

## Phase 7 — Nachlauf

- [ ] `IsorBackup/RULES.md`, `ROADMAP.md`, `DECISIONS.md` aus dem
      bisherigen README aufbauen; Selbstwiderspruch zu `IsorRepos`
      beheben (E72, G-a)
- [ ] `C:\IsorBackup\README.md` auf einen Wegweiser kürzen (E72)
- [ ] `GLOSSARY.md` aus den fertigen Dateien einsammeln (E65)
- [ ] `_HARNESS_REVIEW.md` und diese Datei archivieren, INDEX-Einträge
      entfernen
- [ ] **Testphase beginnen** — erste Aufgabe: IsorBackup aufräumen in
      Viererpaketen (E73)

---

## Übergabe an die nächste Session (2026-08-22)

**Phase 6 und 7 stehen aus.** Sie sind bewusst in eine frische Session
gelegt worden, und zwar nicht nur wegen des Kontexts:

- **Phase 6 ist der erste echte Test des Harness.** Die Befehle brauchen
  nur eine Grundlage — die Doku-Pflicht in `Kern/WORKFLOW.md`. Eine
  frische Session muss sie über die Leseordnung selbst finden. Klappt
  das, trägt der Harness. Klappt es nicht, ist die Lücke ein Fall für
  `Kern/STOERUNGEN.md`.
- **Die offene Prüfung P1** ist nur beim Start einer frischen Session
  feststellbar: Welche der drei `CLAUDE.md` lädt der Harness von selbst,
  bevor irgendeine Datei geöffnet wurde? Davon hängt ab, ob die echten
  Regeln zwei Weiterleitungen tief liegen dürfen.

Nächste Schritte in `PLAN.md`.
