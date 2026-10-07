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
- [x] **V3 · Texturierte Kugel und Orbit-Kamera** — Kugel-Generator,
  stb_image-Textur, GLM-Matrizen (Model/View/Projection),
  Orbit-Steuerung mit Maus und Rad. V1–V3 fertig vor Do 08.10.
  **Erledigt am 2026-10-07:** Matrizen-Kette zuerst am Dreieck
  bewiesen, dann UV-Kugel 32×32 (`Geometry.cpp`, mit KI-Vermerk),
  Gras-Textur (`CTexture`, stb_image, Mipmaps) und Orbit-Kamera
  (`CCamera`: Maus dreht, Rad zoomt mit Anschlägen, Pitch-Stopp ±89°;
  `GetAspectRatio` hält die Kugel beim Resize rund). Tiefenpuffer an
  (DECISIONS). F5-Beweis: drehbare, zoombare Gras-Kugel.
  Arbeitsteilung: GLSL und Verdrahtung Isor, Drumherum Claude mit
  Stationen-Durchgang. Lern-Rubriken in `Kern/LERNLOG.md` unter
  2026-10-07.
- [x] **V4 · Licht und Toon-Stufen** — Richtungslicht als Uniforms;
  Isor tippt die GLSL-Logik: erst weicher Lichtverlauf, dann in Stufen
  quantisiert. Outline-Entscheid am echten Bild (DECISIONS dieser
  Schicht). **Erledigt am 2026-10-07** (vorgezogen auf Isors Zuruf):
  Richtungslicht über `SetVec3`, GLSL komplett von Isor getippt; die
  floor-Stufen wurden gebaut und am Bild zugunsten der Stylized-Kante
  (smoothstep/mix, kühler Schatten-Tint) verworfen — DECISIONS. Der
  Outline-Entscheid ist herausgelöst (Kür O1).
- [x] **V5 · Skybox** — Cubemap laden (CC0-Himmel), eigener kleiner
  Skybox-Shader. **Erledigt am 2026-10-07:** CSkyBox + Shaderpaar
  (samplerCube, xyww, LEQUAL, mat3-View), Himmel 05 CC0 im Repo,
  Original im Datenbaum. Dazu ungeplant: Bodenplatte mit Rand-Fade,
  Seamless-Gras, Toon-Ball-Textur, Sonnen-Gizmo, Kontakt-Schatten,
  Kamera-Bodengrenze. **Alle sieben Pflichtpunkte erfüllt.** Belege:
  LOG und ABGABE_NOTIZEN.
- [ ] **T1 · Tuning-Fenster** — die vorhandenen Float-Regler (Kante,
  Weichzone, Lichtrichtung und -farbe, Sonne, Fade) zur Laufzeit
  verstellbar machen; Zielbild klickbares Fenster mit Slidern (Dear
  ImGui), erlaubte Vorstufe Tasten + Konsolen-Ausgabe. Nach der
  Jam-Woche, vor V6.
- [ ] **V6 · Abgabe** — Feinschliff (MSAA, die zwei
  VS-Analyse-Hinweise), **Code-Aufräum-Pass: main in benannte
  Methoden gliedern, danach gemeinsamer Erklär-Durchgang über alles**,
  Release-Build, READ_ME, UML-Entscheid (nur Tipp der Aufgabe — der
  Generator macht es billig), Abgabeordner im Portfolio füllen,
  Zeiten gegen Grindstone prüfen; Upload ~23./24.10., danach die
  Feedback-Fragen an die OCE: reicht der Stand? Werden Schatten
  erwartet? Wird ein Settings-UI erwartet?

## Kür — nur bei Zeit vor der Abgabe

- [ ] **K1 · Mini-OBJ-Loader** — ein eigenes Blender-Modell laden;
  erfüllt zusätzlich den Optional-Punkt „Modell-Laden" der Aufgabe.
- [ ] **O1 · Outline (Inverted Hull)** — den Ball als minimal
  aufgepumpte schwarze Hülle (vert: Position + Normale × Dicke) ein
  zweites Mal zeichnen, nur Rückseiten zeigen → Culling-Lernstück.
  Entscheid nach Zeitlage; der Look trägt auch ohne (2026-10-07).
- [ ] **B1 · Blending-Tag** — Alpha-Rand-Fade, additiver Sonnen-Glow,
  Multiply-Schatten: drei Design-Wünsche, eine Technik. **Gestrichen
  am 2026-10-07** (DECISIONS); reaktivieren nur, falls das
  OCE-Feedback mehr verlangt.

## Offene Aufgaben

- [x] **Knowledge · w-Division** — nach V3 als Seite in
  `Knowledge/Grafik/` festhalten (Isors Experiment vom 2026-10-06:
  w = 0.5 verdoppelt, w = 2 halbiert — der Perspektiv-Teiler der
  Projektionsmatrix, dann mit dem Matrizen-Bild komplett).
  **Erledigt am 2026-10-07:** Seite
  `Knowledge/Grafik/mvp-matrizen-und-w-division.md`, dazu ungeplant
  zwei weitere Seiten (Tiefenpuffer, Datenfluss VBO→Pixel) — Isors
  Auswahl bei der Knowledge-Frage.
- [ ] **Artifact-Fassungen der Grafik-Seiten vom 2026-10-07** —
  die neuen Knowledge-Seiten (MVP/w-Division, Tiefenpuffer, Datenfluss,
  dazu die vier Abend-Seiten: Skybox, Staffelstab, Zaun/Seil-Maß,
  Ein Mesh) sind visuell und bekommen nach `Kern/KNOWLEDGE_RULES.md`
  zusätzlich Artifact-Seiten; bauen samt `ARTIFACT_INDEX`-Einträgen und
  Rückverweisen in den .md-Dateien. Kandidat fürs nächste Warmup oder
  den Pflegetag.
- [ ] **Warmup glDepthFunc** — die LEQUAL/LESS-Zeilen um den
  Skybox-Draw als Einstiegs-Erklärstück der nächsten Viewer-Session;
  von Isor am 2026-10-07 selbst bestellt („das ist einfach da drin
  geschrieben").
