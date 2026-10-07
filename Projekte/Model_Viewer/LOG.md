# LOG.md — Chronik 3D-Model-Viewer

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste
oben. Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur
ergänzt. Was als Nächstes kommt, steht in der ROADMAP dieser Schicht;
warum das Projekt so gebaut ist, in den DECISIONS; die Lern-Rubriken
stehen in `Kern/LERNLOG.md`.
Format: Ereignisse als `- JJJJ-MM-TT — Ereignis (1–3 Sätze)`.

- 2026-10-04 — Projekt entworfen und Schicht angelegt: Design-Session
  zum 3D-Model-Viewer auf Grundlage von Aufgabe 2
  (`Uni/Semester_3/VORJAHR_AUFGABEN.md`) und dem Minimal-Beschluss vom
  2026-10-01 (`Uni/DECISIONS.md`). Vier Einträge in den DECISIONS
  dieser Schicht (Schicht und Repo, Minimal-Zuschnitt, Technik-Stack,
  Programmaufbau), Bausteine V0–V6 plus Kür K1 in der ROADMAP. Isors
  Schnipsel aus der ersten OpenGL-Kursstunde bestätigte GLFW, GLAD und
  Core Profile und hob die Versionswahl auf 4.6.
- 2026-10-04 — V0 und V1 gebaut, in derselben Session nach dem
  Wechsel auf Development: Repo `Model-Viewer` mit VS-Solution nach
  Lane-Defender-Vorlage, alle vier Bibliotheken unter `Libraries\`
  (GLFW als DLL-Anbindung wegen LNK4098), Marke und Freigabe gesetzt;
  danach das Fenster-Programm — Isor tippte alle vier Häppchen selbst,
  F5-Test bestanden. Belege an den Haken der ROADMAP dieser Schicht,
  Lern-Rubriken in `Kern/LERNLOG.md`.
- 2026-10-04 — Window-Umzug abgeschlossen, am Abend derselben Session:
  Fenster-Code aus `main.cpp` in die RAII-Klasse `CWindow` gezogen
  (`Window.h`/`Window.cpp`), main spricht nur noch über die kleinen
  Methoden, das einzige `glfwTerminate` liegt im Destruktor. Isor zog
  den Großteil selbst vor, der Rest lief erkältungsbedingt als
  Ansage-Zettel; Gegenbau warnungsfrei, F5-Test wie vorher. Das
  Gegenlesen der drei Tippfehler-Funde ist auf den Folgetag vertagt.
- 2026-10-05 — Warmup und V2-Start: die drei Funde des Window-Umzugs
  gegengelesen (alle im Gegenbau bereits behoben), dazu Isors
  Transferfrage zur Forward-Declaration geklärt. Danach V2 begonnen:
  Shaderpaar `Shaders/triangle.vert|.frag` getippt (frag allein),
  CShader entworfen, Gerüst und Datei-Lesen gebaut. Die Session lief
  über Nacht weiter.
- 2026-10-06 — V2 fertig: CShader kompiliert und linkt mit
  Treiber-Fehler-Logs (Meldung nennt seit dem Sabotage-Test auch die
  Datei), CMesh bringt die Vertex-Daten als VBO/VAO auf die GPU,
  erstes oranges Dreieck per F5. Sabotage-Test bestanden (Farbwechsel,
  Eckpunkt ziehen, Fehlertext lesen); dabei per Experiment die
  w-Division entdeckt. Beleg am ROADMAP-Haken dieser Schicht,
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-10-05/06.
- 2026-10-07 — V3 fertig (krankgeschrieben, nach Fachwort-Warmup):
  Matrizen-Kette erst am Dreieck bewiesen, dann prozedurale Kugel
  (32×32, `Geometry.cpp` mit KI-Vermerk), Gras-Textur über `CTexture`
  und Orbit-Kamera (`CCamera`, Maus dreht, Rad zoomt) — F5 zeigt die
  drehbare Gras-Kugel, V1–V3 stehen damit vor dem Jam-Briefing.
  Unterwegs ein Lehrbuch-Fehler samt Fix (Tiefenpuffer gegen das
  Maler-Problem, DECISIONS), drei neue Wissensseiten in
  `Knowledge/Grafik/` und drei Störungen notiert (zwei zur
  Commit-Lieferung, eine zur Arbeitsteilung — `Kern/STOERUNGEN.md`).
  Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-10-07.
- 2026-10-07 — V4 und V5 am selben Tag fertig, in der Abend-Session
  auf Isors Zuruf (vorgezogen vor die Jam-Woche): Richtungslicht mit
  Stylized-Toon-Kante (smoothstep/mix, kühler Schatten-Tint — die
  floor-Stufen wurden gebaut und am Bild verworfen) und Skybox
  „Himmel 05" (CC0-Paket im Datenbaum, CSkyBox mit eigenem Shader,
  xyww/LEQUAL). Dazu ungeplant: Bodenplatte mit quadratischem
  Rand-Fade (Isors Idee, selbst getippt und getunt), Seamless-Gras
  (Isors Fund), generierte Toon-Basketball-Textur, Sonnen-Gizmo,
  Kontakt-Schatten und die zoomabhängige Kamera-Bodengrenze (Isors
  Entwurf). Damit sind alle sieben Pflichtpunkte der Aufgabe erfüllt;
  Outline-Entscheid vertagt, Blending gestrichen (DECISIONS, fünf
  Einträge). Vier neue Wissensseiten in `Knowledge/Grafik/`, eine
  Störung (VS-Puffer — `Kern/STOERUNGEN.md`), Grindstone-Stand
  18:49 h. Lern-Rubriken in `Kern/LERNLOG.md` unter 2026-10-07.
