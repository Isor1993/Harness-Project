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

- [ ] **Arbeitsteilung um den Durchgang-Zeitpunkt schärfen** — In
  `DECISIONS.md` → „2026-10-01 — 3D-Model-Viewer minimal" die
  Arbeitsteilung ergänzen: Schreibt Claude ein Stück, kommt der
  gemeinsame Durchgang **sofort nach dem Stück**, vor dem nächsten;
  bei Zeitdruck wird der Baustein geschnitten, nicht der Durchgang.
  Anlass: `Kern/STOERUNGEN.md` → „2026-10-07 — Fließband-Code ohne
  gemeinsamen Durchgang" (Isors Ja vom 2026-10-07).

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

- [ ] **Spielkonzept engine-neutral entwickeln** — Core Loop, Spielidee
  und Pitch-Grundlage für das eigenständige kleine Spiel; läuft ab
  sofort und hängt nicht an der Engine-Entscheidung vom 02.11.
  (`DECISIONS.md`, Einträge vom 2026-10-01). Eigener Design-Abschnitt;
  mit dem Konzept entsteht die neue Projekt-Schicht samt GDD.
  **Stand 2026-10-09:** Spielidee in der Ideenrunde festgezurrt, die
  Schicht `Projekte/Isors_Outbreak/` ist mit GDD, DECISIONS und ROADMAP
  angelegt. Offen bleibt die Pitch-Grundlage: das Mini-GDD zur Freigabe
  (`Projekte/Isors_Outbreak/ROADMAP.md` → „G1 · Mini-GDD zur
  Freigabe").

- [ ] **Zwei fertige Spiele bis Studienende, eines veröffentlicht** —
  Isors Ziel vom 2026-10-01 hinter der Portfolio-Strategie
  (`DECISIONS.md` → „2026-10-01 — Semester-Spiel: eigenständiges
  kleines Spiel statt Tower-Variante"). Spiel 1 ist das Semester-Spiel;
  Spiel 2 folgt in Semester 4–6, Release-Fragen nach dem ersten
  Prototyp.

### Der Phasenplan — beschlossen am 2026-09-08

Grundsätze (Frontloading, 24-Stunden-Woche): `DECISIONS.md` →
„2026-09-08 — Semester-3-Roadmap"; der Schnitt nach Fertig-Zielen seit
dem 2026-09-14: `DECISIONS.md` → „2026-09-14 — Fertig-vor-fällig". Die
Abgabetermine besitzt `Semester_3/STUNDENPLAN.md`.

**Jede Phase endet mit ihrem Fertig-Ziel vor dem Abgabetermin** — das
Fertig-Ziel ist der Feature-Stopp, das letzte Wochenende davor die
Crunch-Reserve, und die Betreuung am Vortag der Abgabe prüft den
fertigen Stand. Der Plan trägt nur Fertig-Ziele und Abgabetermine;
Projekt-Meilensteine werden beim Start der jeweiligen Phase
dazwischengesetzt.

- [ ] **Phase 1 · C++-Grundlagen und Lane Defender (08.09.–27.09.)** —
  C++-Kurs plus Lern-Vorlauf und Meilensteine
  (`Projekte/Lane_Defender/ROADMAP.md`); Fertig-Ziel So 27.09., Abgabe
  Fr 02.10., die Abgabewoche ist nur Feinschliff. Isors Streckziel vom
  2026-09-14: wenn möglich schon So 20.09. fertig.
- [ ] **Phase 2 · 3D-Model-Viewer (03.10.–25.10.)** — OpenGL/GLSL im
  Selbststudium; seit dem 2026-10-01 bewusst minimal: nur die
  Minimalkriterien der Aufgabe plus ein simpler Toon-Shader, früh
  abgeben und OCE-Feedback einholen (`DECISIONS.md` → „2026-10-01 —
  3D-Model-Viewer minimal"). Vorher die Aufgabe gegen eine
  Minimal-Checkliste lesen (`Semester_3/VORJAHR_AUFGABEN.md`,
  Aufgabe 2). Dazwischen liegt der Game Jam (08.–15.10.,
  `Semester_3/STUNDENPLAN.md`) mit Minimal-Beteiligung — das Gerüst
  (Fenster, Modell laden) steht deshalb vor dem Jam. Frühe Abgabe
  ~23./24.10. statt Fertig-Ziel So 25.10.; Frist Fr 30.10.
- [ ] **Phase 3 · Unreal-Block, Spiel-Prototyp und Pitch-Material
  (26.10.–22.11.)** — Unterricht mitnehmen; vorweg das Engine-Hands-on
  (Toolchain-Test plus zwei Mini-Übungen, ~24.10.–01.11.) mit der
  **Engine-Entscheidung spätestens So 02.11.** (`DECISIONS.md` →
  „2026-10-01 — Engine-Kontrollpunkt vorgezogen"); danach der Prototyp
  des eigenständigen kleinen Spiels (`DECISIONS.md` → „2026-10-01 —
  Semester-Spiel: eigenständiges kleines Spiel statt Tower-Variante")
  im gewählten Stack, das Pitch-Material entsteht mit, weil beides am
  selben Tag fällig ist. Fertig-Ziel So 22.11., Abgabe Fr 27.11.
  (Prototyp und Pitch).
- [ ] **Phase 4 · Projektplanung (23.11.–13.12.)** — Pitch-Präsentation
  Do 03.12. (vor Ort); die benotete Projektplanung (Summative
  Zwischenprüfung) mit den Prototyp-Erkenntnissen: Fertig-Ziel
  So 13.12., Abgabe Fr 18.12.
- [ ] **Phase 5 · Alpha (14.12.–06.01.)** — Core-Loop feature-complete
  mit Win/Lose; die Weihnachtslücke ist Bauzeit, nicht Reserve.
  Fertig-Ziel Mi 06.01., Betreuung Do 07.01., Abgabe Fr 08.01.,
  Präsentation Do 14.01.
- [ ] **Phase 6 · Beta (09.01.–27.01.)** — feature-complete, Content
  vollständig, fremde Tester. Fertig-Ziel Mi 27.01., Betreuung
  Do 28.01., Abgabe Fr 29.01., Präsentation Do 04.02.
- [ ] **Phase 7 · Goldmaster (30.01.–10.02.)** — Fertig-Ziel Mi 10.02.,
  Betreuung Do 11.02., Abgabe Fr 12.02., Präsentation Do 18.02.
- [ ] **Phase 8 · Reflexion und Portfolio (13.02.–21.02.)** —
  Projektreflexion: Fertig-Ziel Mi 17.02., Abgabe Fr 19.02.;
  Portfolio: Fertig-Ziel So 21.02., Abgabe Fr 26.02. Der letzte
  Betreuungstermin (Do 25.02.) liegt noch vor der Portfolio-Abgabe.
