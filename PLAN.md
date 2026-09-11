# PLAN.md — Arbeitsplan

Ownership: Was in den nächsten ein bis drei Wochen dran ist,
schichtübergreifend — und der Auftrag an die nächste Session. Was
irgendwann kommt, steht in der ROADMAP der jeweiligen Schicht; was
passiert ist, im LOG.
Format: `### <Zeitraum oder Baustein>` mit Aufzählungspunkten, je Punkt
ein Satz. Erledigtes wird abgehakt, nicht gelöscht. Der Abschnitt „Für
die nächste Session" steht oben und hat sein eigenes Format.

**Höchstens ~100 Zeilen.** Ist ein Zeitraum durch, wandert er als
Ereignis ins LOG, erledigte Punkte werden in der ROADMAP abgehakt, und
diese Datei wird **geleert** — nicht archiviert. Die Geschichte steht
im LOG.

---

## Für die nächste Session

Steht **oben**, weil es das Erste ist, was zählt. Wird bei jedem
`/harness:ende` **überschrieben**, nie ergänzt — „gerade nichts offen"
ist ein gültiger Inhalt. Höchstens fünf Zeilen; Ausführliches steht in
der Datei, auf die hier verwiesen wird.

*(überschrieben 2026-09-11 beim `/harness:ende` — Abschnitte
„Fab-Sale-Durchsicht" (Design, Revier Isor's Tower: nichts gekauft,
drei Freebies geclaimt, Merkposten UDS) und „Lane Defender Ü3"
(Development · Lernmodus, Revier Lane Defender: Ü3 fertig). Berichte in
den LOGs beider Schichten und `Kern/LERNLOG.md`.)*

Lane Defender **Ü4 Eingabe-Validierung** — `cin.fail`/`clear`/`ignore`
am Spielcode, Testreihe `abc`/`-3`/`0`/`5`, `<limits>` selbst includen;
danach **L3** (Pointer). Kür davor erlaubt: die `, true`-Argumente per
Default schrumpfen. Unverändert offen: Unreal-Toolchain-Test,
Abgabetermine der Uni, Datenbaum. Pflegetag lief am 2026-09-11 parallel.

---

### Die Testphase läuft — seit 2026-08-27

Sie hat auf Isors Zuruf begonnen, wie es seit dem 2026-08-23 vorgesehen
war (`Kern/DECISIONS.md`). Ab jetzt gilt: **Der Harness wird benutzt,
nicht gebaut.** Claude schlägt von sich aus keine Umbauten mehr vor.

Was im Betrieb nicht trägt, wird als Störung notiert
(`Kern/STOERUNGEN.md`) und über die Doku-Pflicht zu einem ROADMAP-Punkt —
nicht sofort behoben. Ein Befund ist ein Zustand, kein Auftrag.

- [x] **Phase 0 · Netz-Prüfstand** — **erledigt am 2026-08-28**, in fünf
      Tagen statt zwei Wochen. Der Vergleichstest ist bestanden (AMD gegen
      Intel, identische Prüfsummen), die Zeitrechnung des Semesters bleibt
      also wie geplant. Zusätzlich belegt: Relay trägt über zwei Netze,
      getestet bis auf die Philippinen.
- [ ] **Der Datenbaum wartet** (`IsorBackup/ROADMAP.md`, vier Punkte).
      **Kein Termin** — bewusst hinter Phase 0 gestellt, weil nur der
      Prototyp einen Semestertermin hat (Isor, 2026-08-27). Er bleibt
      die geplante Belastungsprobe des Harness im Betrieb.
- [x] **Abgabe-Struktur anlegen**, sobald die Semester-Aufgaben da sind
      (`Uni/ROADMAP.md`) — der Punkt, an dem im zweiten Semester Zeit
      verloren ging. Die Aufgaben sind seit dem 2026-09-07 bestätigt.
      **Erledigt am 2026-09-08** — Beleg: `Uni/ROADMAP.md` →
      „Abgabe-Struktur beim Semesterstart kopieren".

### Umstellung auf Unreal + C++ — entschieden 2026-09-07

Beschluss und Begründung: `Uni/DECISIONS.md` → „2026-09-07 — Engine- und
Sprachfokus". Der Unity-Bauplan des Towers ist archiviert
(`Projekte/Isor_Tower/_ARCHIV.md`). Isors Lernpfad: Konsolenprojekt =
C++-Grundlagen auf C#-Niveau bringen → 3D-Model-Viewer = Grafik und
Shader → dann Unreal-C++ mit seinen Eigenheiten.

- [x] **Visual Studio 2022 mit C++-Workload installieren** — vor der
      ersten eigenen C++-Übung nötig; Unreal-Version mit dem Kurs
      abgleichen und installieren (Unterrichtsblock ab 27.10., früher
      schadet nicht). **Erledigt am 2026-09-08 (VS-Teil):** VS
      Community 2026 samt C++-Workload und cl.exe war schon
      installiert und ist verifiziert — ein 2022 braucht es dafür
      nicht. Der Unreal-Teil steht als eigener Punkt darunter.
- [ ] **Unreal installieren, sobald die Kursversion bestätigt ist** —
      Kandidat laut Abgabe-Vorlage im Datenbaum: 5.6. Dabei prüfen, ob
      diese Unreal-Version das installierte VS 2026 als Toolchain
      akzeptiert — sonst die VS-2022-Build-Tools daneben installieren.
      **Stand 2026-09-08:** Kursversion offiziell bestätigt
      (Versionsblatt Studienjahr 0925: Unreal 5.6, dazu
      OpenGL-Empfehlung Core 450 für den Model-Viewer — `Uni/LOG.md`).
      5.6.1 ist installiert, Bridge und Fab-Plugin folgen automatisch.
      Offen nur noch der Toolchain-Test (neues C++-Blank-Projekt):
      Epics Doku empfiehlt für 5.8 ausdrücklich VS 2026, für 5.6 ist es
      ungeprüft — Plan B bleiben die VS-2022-Build-Tools.
- [x] **Neues Projekt-Repo für den Unreal-Tower anlegen** —
      Namensvorschlag kommt von Claude; `.gitignore`/LFS nach
      Unreal-Muster (`Binaries/`, `Intermediate/`, `Saved/`,
      `DerivedDataCache/`, `.vs/`; `*.uasset`/`*.umap` über LFS).
      Danach `Kern/PFADE.md` und die Freigaben nachziehen.
      **Erledigt am 2026-09-08:** `Isor-Tower-Unreal` angelegt (git
      init, .gitignore, LFS-Attribute, README), Marke `PROJEKT_UNREAL`
      in `Kern/PFADE.md`, Freigabe in `.claude\settings.json`. Dazu
      ungeplant das Repo `Lane-Defender` (Marke
      `PROJEKT_LANE_DEFENDER`), Begründung in
      `Projekte/Lane_Defender/DECISIONS.md`.
- [x] **`Kern/CODE_GUIDELINES.md` auf C++ erweitern** — SAE-C++-
      Konvention (aus den Semester-3-Unterlagen holen) fürs
      Konsolenprojekt, Epic C++ Coding Standard fürs Spiel; die
      C#/Unity-Blöcke bleiben als Altstand-Regeln gekennzeichnet.
      Sicherungskopie der Unity-Fassung liegt im Datenbaum. Wartet auf
      das SAE-Kursmaterial — der C++-Kurs ist am 2026-09-08 gestartet.
      **Erledigt am 2026-09-08:** die Abschnitte „C++ — welche
      Konvention wo gilt", „C++ · Konsolenprojekt — SAE-Konvention
      (Pflicht)" und „C++ · Unreal — Epic C++ Coding Standard
      (vorgegeben)" stehen in der Datei; SAE-PDF im Datenbaum
      (`01_Uni\_Regelwerk\`), Epic-Destillat ausgelagert
      (`Kern/ROADMAP.md` → „Epic C++ Coding Standard destillieren"),
      dazu `💡 Lernstück · SAE-C++-Konventionen` im `ARTIFACT_INDEX.md`.
- [x] **Unreal-Pendant zur „nie durchsuchen"-Regel** — heute nennt
      `CLAUDE.md` nur die Unity-Ordner; sobald das Unreal-Repo
      existiert, kommen `Binaries/`, `Intermediate/`, `Saved/`,
      `DerivedDataCache/`, `.vs/` dazu. **Erledigt am 2026-09-08** —
      die Regel steht in `CLAUDE.md`, im selben Zug wie das Repo.
