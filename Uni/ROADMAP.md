# ROADMAP.md — Baureihenfolge Studium

Ownership: Nur was für das Studium als Nächstes zu tun ist,
semesterübergreifend. Was gerade dran ist, steht in `PLAN.md`; was
passiert ist, in `Uni/LOG.md`; Überholtes in `Uni/_ARCHIV.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`

**Diese Datei wurde am 2026-08-27 geleert**, im selben Durchgang wie
`Kern/ROADMAP.md`. Die erledigten Punkte (E62, `Abgabe_Final`, die
Befunde der Prüfung vom 2026-08-26) stehen mit ihren Belegen in
`Uni/LOG.md`.

## Als Nächstes

- [x] **Abgabe-Struktur beim Semesterstart kopieren, nicht am Ende
  sortieren.** Die Vorlage liegt im Datenbaum unter
  `05_Werkzeuge\Vorlagen\SAE_Abgabe_Struktur\` (`Kern/PFADE.md` →
  `DATENBAUM`). Im zweiten Semester wurde erst am Schluss einsortiert;
  das nächste Mal steht der Baum von Anfang an.
  **Erledigt am 2026-09-08:** `01_Uni\Semester_3\` nach der
  Semester-Vorlage aufgebaut; darin
  `Abgabe\Portfolio_5FSC0XD101_Rosenberg\` mit READ_ME und den acht
  Aufgabenordnern des Moduls (1_LaneDefender bis 8_Projektreflexion,
  Projekt-Aufgaben mit src/release/other, Dokument-Abgaben nur mit
  other\Dokumente). Die Anleitungsdatei der Vorlage wurde absichtlich
  nicht mitkopiert.

- [ ] **`U6` streichen, sobald das TDD neu gebaut wird.** Der Satz über
  die abgegebene Fassung vom 21.08. in `Uni/DOCX_RULES.md` gibt bis dahin
  eine richtige Auskunft; er wird falsch in dem Moment, in dem eine neue
  Fassung entsteht. Einziger übriger Befund der Prüfung vom 2026-08-26,
  bewusst stehen gelassen.

## Semester 3

- [x] **Ordner `Uni/Semester_3/` anlegen**, sobald die Aufgaben da sind,
  und die Aufgabentexte gleich zu Beginn ablegen. `ASSESSMENT_RULES`
  verlangt für jedes Zeugnis die Kriterien im Originaltext — im zweiten
  Semester fehlten sie für vier von sieben Abgaben und mussten
  nachträglich zusammengesucht werden. **Erledigt am 2026-09-06/07:**
  Der Ordner steht mit `STUNDENPLAN.md` und `VORJAHR_AUFGABEN.md`; die
  Moduleinführung hat die Texte als Originalaufgaben bestätigt. Die
  eigenen `ASSIGNMENT_*.md` folgen, sobald Isors Canvas-Texte exportiert
  sind (Vermerk im Kopf von `VORJAHR_AUFGABEN.md`).

- [x] **Semester-3-Roadmap in einem Design-Abschnitt bauen**:
  Bronze/Silber/Gold als Fixpunkte, Puffer **vor** den Statusterminen,
  eigene Features nur bei Vorsprung auf den Unterricht und nach Nutzen
  für den Main Loop (Isor, 2026-08-30). Grundlage seit dem 2026-09-07:
  die Stack-Entscheidung (`DECISIONS.md` → „Engine- und Sprachfokus:
  Unreal + C++") und die bestätigten Aufgaben samt Terminen
  (`Semester_3/STUNDENPLAN.md`, `Semester_3/VORJAHR_AUFGABEN.md`).
  **Erledigt am 2026-09-08:** Grundsätze in `DECISIONS.md` →
  „2026-09-08 — Semester-3-Roadmap", Phasenplan unten, Zeitstrahl auf
  der Artifact-Seite `📍 Status · Semester 3` (`Kern/ARTIFACT_INDEX.md`).

### Der Phasenplan — beschlossen am 2026-09-08

Grundsätze (Frontloading, 24-Stunden-Woche, Schätzlogik, Feature-Stopp):
`DECISIONS.md` → „2026-09-08 — Semester-3-Roadmap". Geschätzte Termine
tragen `~` und gelten, bis Isors Canvas-Export sie ersetzt.

- [ ] **Phase 1 · C++-Grundlagen und Lane Defender (08.09.–05.10.)** —
  C++-Kurs plus Lern-Vorlauf und Meilensteine
  (`Projekte/Lane_Defender/ROADMAP.md`); Ziel: abgabefertig vor dem
  geschätzten Termin ~15.10.
- [ ] **Phase 2 · 3D-Model-Viewer (05.10.–26.10.)** — OpenGL/GLSL im
  Selbststudium; der Muss-Umfang (Fenster, Pipeline, texturiertes
  Modell, Licht, Kamera, Skybox) steht vor dem Unreal-Block,
  Feinschliff bis zum echten Abgabetermin (~05.11.).
- [ ] **Phase 3 · Unreal-Block und Tower-Prototyp (27.10.–23.11.)** —
  Unterricht mitnehmen, parallel den spielbaren Unreal-Prototyp in der
  Tower-Welt bauen (~20.11.) — das ist der Stack-Kontrollpunkt
  (`DECISIONS.md` → „2026-09-07 — Engine- und Sprachfokus").
- [ ] **Phase 4 · Pitch und GDD (24.11.–10.12.)** — Pitch am 03.12.
  (fest), danach das benotete GDD (~10.12.); die Prototyp-Erkenntnisse
  fließen ein.
- [ ] **Phase 5 · Alpha (11.12.–14.01.)** — Core-Loop feature-complete
  mit Win/Lose zur Präsentation am 14.01. (fest); die Weihnachtslücke
  ist Crunch-Reserve, ab der Betreuung am 07.01. (Generalprobe)
  Feature-Stopp.
- [ ] **Phase 6 · Beta (15.01.–04.02.)** — feature-complete, Content
  vollständig, fremde Tester zur Präsentation am 04.02. (fest); ab der
  Betreuung am 28.01. (Generalprobe) Feature-Stopp.
- [ ] **Phase 7 · Gold und Portfolio (05.02.–25.02.)** — Goldmaster am
  18.02. (fest, Generalprobe 11.02.), danach Projektreflexion und
  Portfolio (~25.02.).
