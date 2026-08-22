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

- [ ] `Kern/DOC_RULES.md` neu anlegen — die 15 Regeln aus E64
- [ ] darin: Sprachtabelle, eine Zeile je Erzeugnis (E70)
- [x] ~~darin: Zuständigkeits-Tabelle aus Schritt F~~ — **gestrichen
      2026-08-22.** Wäre eine Kopie gewesen: Wer was besitzt, steht in
      jeder `Ownership:`-Zeile und gesammelt im erzeugten INDEX.
      DOC_RULES besitzt das Verfahren, der INDEX das Ergebnis.
      Stattdessen steht dort ein Verweis.
- [ ] darin: „Vor einem Ownership-Befund die Ownership-Zeile **aller**
      beteiligten Dateien lesen" (aus STOERUNGEN, 2026-08-21)
- [ ] `Kern/GDD_RULES.md` neu anlegen (E60) — Aufbau und Pflege eines GDD,
      `offen`-Mechanismus, wann aus Entwurf feste Absicht wird
- [ ] `Kern/VERSIONIERUNG.md` neu anlegen (E77–E80) — die drei
      Nummernsysteme und ihre Lesarten
- [ ] CLAUDE.md bekommt die Zeile `Harness-Version: 1.0.0` (E79)
- [ ] Auslieferungs-Ordner anlegen:
      `C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\` (E80)
- [ ] Erste Auslieferung `Harness_1.0.0` erst **nach Phase 7**, wenn der
      Kern vollständig ist

## Phase 2 — Struktur anlegen (leere Ordner, keine Inhalte)

- [ ] Ordner `Kern/`, `Uni/Semester_2/`, `IsorBackup/`,
      `Projekte/Isor_Tower/` (E11, E50)
- [ ] `PLAN.md` anlegen, max. ~100 Zeilen, wird nach jedem Zeitraum
      geleert (E12)
- [ ] `Kern/STOERUNGEN.md` anlegen (E16) + die zwei ersten Einträge
- [ ] `Kern/Zeugnisse/` anlegen (E53)

## Phase 3 — Große Bestände umziehen (skriptgestützt)

**DECISIONS (1.790 Zeilen, 133 Einträge)**
- [ ] Zuordnungsliste erstellen: 133 Zeilen „Titel → Zieldatei"
- [ ] die ~13 Konventions-Einträge einzeln entscheiden, in Viererpaketen (E8)
- [ ] die geschätzt 8–10 weiteren Grenzfälle einzeln
- [ ] Skript trennt an `## `-Überschriften, kein Copy-Paste (E10)
- [ ] Nachzählung 133 rein / 133 raus — bei Differenz wird nichts
      geschrieben (E10)
- [ ] alte `DECISIONS.md` nach `99_Archiv\_Zu_Loeschen\` (E10)
- [ ] Ziel: `Kern/DECISIONS.md` (~25) · `Kern/Konventionen` (~10) ·
      `Uni/Abgabe` (~23) · `Projekte/Isor_Tower/DECISIONS/` Terrain (~31),
      UI (~17), Welt (~14), Audio (~10), Entities (~7)

**ROADMAP (708 Zeilen, davon 546 Vergangenheit — C8)**
- [ ] „Erledigt"-Block (48 Z.) ins LOG der jeweiligen Schicht
- [ ] Abgabe-Block (498 Z.) ins `_ARCHIV.md` der Uni-Schicht
- [ ] **Achtung, einzeln prüfen:** „Arbeitsregeln, die weiter gelten" und
      „Restliste Politur" gelten weiter — nicht mitarchivieren
- [ ] Rest (~162 Z.) auf die Schicht-ROADMAPs verteilen
- [ ] die zwei „Offenen Punkte" aus ARTIFACT_INDEX aufnehmen (E46)
- [ ] Tests-Lücke als offenen Punkt aufnehmen (E56)
- [ ] ClaudeSetup steht nur noch hier, nicht mehr in CODE_GUIDELINES (E55)
- [ ] „Harness-Dokumente auf Englisch umstellen" zur **Bedingung**
      umformulieren: erst prüfen, wenn der Harness tatsächlich
      weitergegeben werden soll (E83)

**FEATURE_LOG (497 Zeilen, 73 Einträge)**
- [ ] wird Chronik `LOG.md` je Schicht (E13) — kein Archiv, keine Pflege
- [ ] Kopfregel ändern: Einträge beschreiben das **Ereignis**, nicht den
      Ablageort (E13)
- [ ] widersprüchliche Zeile „Harness-Bauten stehen in ROADMAP" streichen (C7)

**TDD_NOTES (556 Zeilen, 85 Einträge)**
- [ ] nach `Projekte/Isor_Tower/` (E51) — nicht Uni
- [ ] nach Themenblöcken gliedern statt chronologisch (~1 h Arbeit)
- [ ] veraltetes „Abgabe ca. 2026-07-28" im Kopf korrigieren (C3-a)

**ASSESSMENT_LOG (782 Zeilen, 2 Zeugnisse)**
- [ ] auftrennen in `Kern/Zeugnisse/2026-08-11.md` und `2026-08-16.md` (E53)

## Phase 4 — Einzeldateien nachziehen

**CLAUDE.md**
- [ ] `Ownership:`-Zeile ergänzen (E19) — fehlt als einziger von 21
- [ ] Doku-Pflicht durch Verweis auf WORKFLOW ersetzen (E17)
- [ ] Leseordnung: CLAUDE → INDEX → PLAN → WORKFLOW (E18)
- [ ] die drei Doku-Regeln nach DOC_RULES verschieben (E20)
- [ ] **offene Prüfung P1** vorher: welche der drei CLAUDE.md lädt der
      Harness von selbst? Nur in einer frischen Session feststellbar

**WORKFLOW.md**
- [ ] besitzt die Doku-Pflicht vollständig (E17)
- [ ] besitzt „wann Knowledge geschrieben wird" (E29)
- [ ] Modus (Lernmodus/Normal) + zwei Regler (E21)
- [ ] Regler-Untergrenze: nie auf inneres Vorstellen ausweichen (E69)
- [ ] Erklärstil „zeigen statt vorstellen lassen" (E69)
- [ ] „Session" und „Abschnitt" trennen (E67) — Widerspruch „ein Typ" vs.
      „2–4 parallel" auflösen
- [ ] „Baustein" definieren samt Fertig-Kriterium (E68)
- [ ] `/sichern`, `/wechsel`, `/ende` beschreiben (E23)
- [ ] Übergang Design→Development als Kontrollpunkt (E24)
- [ ] wiederholte Zeugnis-Doku-Pflicht streichen, nur Verweis (E43)
- [ ] Typ „Art" als `(geplant)` kennzeichnen (E22)
- [ ] alle Statusvermerke auf den heutigen Stand (E26)

**INDEX.md**
- [ ] wird aus den `Ownership:`-Zeilen erzeugt (E25)
- [ ] Statusangaben entfernen (E26)
- [ ] Nummernverweis „ROADMAP-Punkt 10" durch Namen ersetzen (E27)

**KNOWLEDGE_RULES.md**
- [ ] Bestandsliste der Themenordner ersatzlos streichen (E30)
- [ ] `README.md` je Themenordner anlegen, eine Zeile (E30)
- [ ] Root-`README.md` des Knowledge-Repos: kurze Orientierung (E31)
- [ ] „wann" durch Verweis auf WORKFLOW ersetzen (E29)
- [ ] „Uni-Modus" → „Lernmodus", Zusatz „in Brainstorm-Sessions" weg (E21)
- [ ] Regel: Artifact nur bei visuellen Themen (E32) — Text in ARTIFACT_RULES

**ARTIFACT_RULES.md**
- [ ] abgeschriebenen Artifact-Check durch Verweis ersetzen (E33)
- [ ] Sonntagsroutine mit Vorschlagsliste beschreiben (E34)
- [ ] `🗑` aus der Typentabelle in „Pflege" verschieben (E36)
- [ ] Zählwort „Die drei Typen" korrigieren (E41)
- [ ] Spalte „Führende Quelle" auf die neue Struktur (B2-d)
- [ ] Erklärstil-Regel durch Verweis auf WORKFLOW ersetzen (E69)

**ARTIFACT_INDEX.md**
- [ ] Schicht-Angabe je Eintrag, benannte Ausnahme von E11 begründen (E45)
- [ ] „Offene Punkte" in die Kern-ROADMAP (E46)
- [ ] Stand-Stempel korrigieren (C1-b)
- [ ] Review-Gate-Erklärung auf einen Verweis kürzen (C1-a)
- [ ] Eintrag für `⚙️ System · Harness` vorbereiten (E35, I12)

**DIAGRAM_RULES.md**
- [ ] konkrete Pfade entfernen, Ablage folgt der Schicht (E37)
- [ ] Abschnitt für das Zustandsdiagramm (E38)

**DOCX_RULES.md** → Schicht Uni
- [ ] die sechs XML-Fallen nach Knowledge auslagern, Verweis behalten (E39)
- [ ] Abschnitt „Werkzeuge": docx-Skill, `validate.py` für den Prüfschritt (E40)
- [ ] Zählwort „Alle vier" korrigieren (E41)

**ASSESSMENT_RULES.md**
- [ ] „Bewertungskriterien liefert die aktive Schicht" (E42)
- [ ] „Prüfanker des letzten Zeugnisses — beantwortet" als Pflichtabschnitt (E52)
- [ ] Ablageregel auf eine Datei je Zeugnis umstellen (E53)
- [ ] Knowledge-Frage auch bei Zeugnissen, Antwort meist „nein" (E44)
- [ ] Belegpflicht gegen die Teilabgaben abgleichen (E63)

**CODE_GUIDELINES.md**
- [ ] Projekt-Typ aus der Schicht ableiten, eigene Angabe streichen (E54)
- [ ] „Bewusst nicht übernommen" nach Art aufteilen (E55)
- [ ] Status-Vermerk „Rohmaterial" auf den heutigen Stand (D1-b)
- [ ] Ownership-Zeile behält „Tests", Lücke bleibt sichtbar (E56)

**GDD.md** → `Projekte/Isor_Tower/GDD.md`
- [ ] Abschnitt „Entwurf" für noch nicht Einsortiertes (E59)
- [ ] offene Design-Fragen: GDD ist Besitzer, ROADMAP verweist (E58)
- [ ] ist zugleich das Markdown-Manuskript der Abgabe (E71)

**PREFAB_STATUS.md** → Projekt-Schicht
- [ ] `VFX_FireFly.prefab` ergänzt sich beim ersten Skriptlauf (C2-b)
- [ ] zwei Nummernverweise durch Namen ersetzen (C2-a)
- [ ] Ende festlegen: alles `geprüft` → Befunde in die ROADMAP, Datei
      ins Projekt-Archiv (E49)

**ASSIGNMENT_PCG / _TOOL / _THREADING**
- [ ] unverändert nach `Uni/Semester_2/` (E50)
- [ ] vier fehlende Aufgabentexte nachtragen; wo es keinen gibt, genau
      das als Datei festhalten (E62)

**Streuner**
- [ ] `_split_check.txt` nach `99_Archiv\_Zu_Loeschen\` (E66)

## Phase 5 — Erzeugte Dateien und Skripte

- [ ] INDEX-Skript: liest alle `Ownership:`-Zeilen, meldet Dateien ohne
      als `⚠` (E25)
- [ ] PREFAB_STATUS-Skript: liest alle `.prefab`, überträgt Status und
      Befund über den Namen (E48)
- [ ] Backup-Skript: `robocopy` über die drei Ordner, Wegfallendes nach
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
