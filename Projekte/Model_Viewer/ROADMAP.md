# ROADMAP.md — Bauplan 3D-Model-Viewer

Ownership: Nur was am 3D-Model-Viewer als Nächstes gebaut wird —
Bausteine und offene Aufgaben. Warum das Projekt so geschnitten ist,
steht in den DECISIONS dieser Schicht; was passiert ist, im LOG; die
Termine besitzt `Uni/Semester_3/STUNDENPLAN.md`.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

Zielfenster aus der Semester-Roadmap (`Uni/ROADMAP.md` → „Der
Phasenplan — beschlossen am 2026-09-08", Phase 2): frühe Abgabe
**~23./24.10.**, Frist Fr 30.10.; das Gerüst V1–V3 steht **vor dem
Game-Jam-Briefing Do 08.10.**, in der Jam-Woche (08.–15.10.) ruht der
Viewer. Arbeitsteilung je Baustein: Claude schreibt das Drumherum,
gemeinsamer Durchgang bis es sitzt; die GLSL-Dateien tippt Isor
(`Uni/DECISIONS.md` → „2026-10-01 — 3D-Model-Viewer minimal").

## Bausteine

- [x] **V0 · Baustart** — Code-Repo `Model-Viewer` anlegen (git init,
  .gitignore für VS-C++, README), Marke `PROJEKT_MODEL_VIEWER` in
  `Kern/PFADE.md`, Freigabe in `.claude\settings.json`; GLFW-Binaries,
  GLAD-Quellcode, GLM und stb_image ins Repo; VS-Solution, die leer
  baut. **Erledigt am 2026-10-04:** Repo steht mit Solution
  (Toolset v145 nach Lane-Defender-Vorlage, nur x64), GLFW 3.4 +
  GLAD 4.6 Core (lokal generiert, Unterrichts-API) + GLM 1.0.1 +
  stb_image unter `Libraries\`; Marke und Freigabe gesetzt;
  Beweis-Build Debug x64 erfolgreich (`ModelViewer.exe`). Der erste
  Commit liegt bei Isor (GitHub Desktop).
- [x] **V1 · Fenster** — GLFW-Fenster auf 4.6 Core wie im Unterricht:
  Clear-Farbe, Esc schließt, Resize-Callback. **Erledigt am
  2026-10-04:** von Isor in vier Häppchen selbst getippt
  (`ModelViewer/main.cpp`), F5-Test bestanden (Fenster steht,
  Größe ziehen sauber, Esc schließt); GLFW auf DLL-Anbindung
  umgestellt (Laufzeitbibliotheks-Konflikt LNK4098 der statischen
  Fassung), Kommentar-Pass durch Claude. Lern-Rubriken in
  `Kern/LERNLOG.md` unter 2026-10-04.
- [x] **V2 · Erstes Dreieck** — erstes eigenes Shaderpaar aus Dateien
  geladen und kompiliert, Vertex-Daten auf die GPU, ein Dreieck auf dem
  Schirm — der Beweis, dass die Pipeline läuft. **Erledigt am
  2026-10-06:** Shaderpaar `Shaders/triangle.vert|.frag`, dazu CShader
  (lesen, kompilieren, linken — mit Treiber-Fehler-Logs) und CMesh
  (VBO/VAO, RAII) nach dem CWindow-Muster; von Isor in Häppchen selbst
  getippt, Konstanten/Tippfehler durch Claude. F5-Beweis: oranges
  Dreieck auf 4.6-Core-Kontext. Lern-Rubriken in `Kern/LERNLOG.md`
  unter 2026-10-05/06. Kanten noch ohne Glättung — MSAA ist
  V6-Feinschliff.
- [ ] **V3 · Texturierte Kugel und Orbit-Kamera** — Kugel-Generator,
  stb_image-Textur, GLM-Matrizen (Model/View/Projection),
  Orbit-Steuerung mit Maus und Rad. V1–V3 fertig vor Do 08.10.
- [ ] **V4 · Licht und Toon-Stufen** — Richtungslicht als Uniforms;
  Isor tippt die GLSL-Logik: erst weicher Lichtverlauf, dann in Stufen
  quantisiert. Outline-Entscheid am echten Bild (DECISIONS dieser
  Schicht). Ab Fr 16.10., nach der Jam-Woche.
- [ ] **V5 · Skybox** — Cubemap laden (CC0-Himmel), eigener kleiner
  Skybox-Shader.
- [ ] **V6 · Abgabe** — Feinschliff, Release-Build, READ_ME,
  UML-Diagramm der Pipeline, Abgabeordner im Portfolio füllen; Upload
  ~23./24.10., danach die Feedback-Frage an die OCE (reicht der Stand?).

## Kür — nur bei Zeit vor der Abgabe

- [ ] **K1 · Mini-OBJ-Loader** — ein eigenes Blender-Modell laden;
  erfüllt zusätzlich den Optional-Punkt „Modell-Laden" der Aufgabe.

## Offene Aufgaben

- [ ] **Knowledge · w-Division** — nach V3 als Seite in
  `Knowledge/Grafik/` festhalten (Isors Experiment vom 2026-10-06:
  w = 0.5 verdoppelt, w = 2 halbiert — der Perspektiv-Teiler der
  Projektionsmatrix, dann mit dem Matrizen-Bild komplett).
