# ABGABE_NOTIZEN.md — Roh-Material für die Abgabe-Doku

Ownership: Nur das Roh-Material für die Abgabe-Doku des
3D-Model-Viewers — je Baustein Zeiten, Gebautes und Begründungen,
festgehalten direkt nach dem Baustein. Der ausformulierte Abgabetext
(READ_ME und UML, Baustein V6) entsteht daraus am Projektende. Die
Zeiten kommen aus Isors Grindstone.
Format: `## <Baustein>` mit Stichpunkt-Blöcken Zeit · Gebaut ·
Warum so · Besonderheiten.

## V0–V1 · Baustart und Fenster (fertig 2026-10-04)

**Zeit:** 3:17 h am 2026-10-04 — enthält die Design-Session (fünf
DECISIONS-Einträge, ROADMAP-Zuschnitt V0–V6 plus Kür).

**Gebaut:** Repo `Model-Viewer` mit VS-Solution (Toolset v145, nur
x64) · GLFW 3.4, GLAD 4.6 Core (lokal generiert), GLM 1.0.1 und
stb_image unter `Libraries\` · GLFW-Fenster auf 4.6 Core mit
Clear-Farbe, Esc und Resize-Callback · RAII-Klasse `CWindow`, main
spricht nur über die kleinen Methoden.

**Warum so:** Bibliotheken im Repo erfüllen wörtlich die
Abgabe-Vorgabe „Projektdateien mit allen Dependencies"; GLFW als DLL
statt statisch wegen LNK4098 (Laufzeitbibliotheks-Konflikt, DECISIONS
2026-10-04); der RAII-Schnitt beantwortet das Feedbackelement
„Memory Leaks" strukturell statt über Disziplin.

**Besonderheiten:** Kursstunde bestätigte 4.6 Core gegen die
450-Empfehlung des Versionsblatts (DECISIONS → Technik-Stack).

## V2 · Erstes Dreieck (fertig 2026-10-06)

**Zeit:** 1:27 h am 05.10. (eventuell untererfasst, Isor krank) +
4:19 h am 06.10. (inklusive Lern- und Reflexionsanteil) — Projekt
gesamt laut Grindstone 9:03 h.

**Gebaut:** Shaderpaar `Shaders/triangle.vert|.frag` (GLSL 460
core) · `CShader`: Datei-Lesen, Kompilieren und Linken als je ein
static-Helfer, Treiber-Fehler-Logs samt Dateiname, RAII um die
Programm-ID · `CMesh`: VBO/VAO mit benannten Konstanten statt Magic
Numbers, RAII · Draw-Call GL_TRIANGLES · Verdrahtung in main
(Konstanten, Wächterkette Window → Shader → Mesh).

**Warum so:** Shader als Dateien statt Code-Strings — Ändern ohne
Neubau, F5 lädt den neuen Stand (Treiber kompiliert zur Laufzeit);
„je Pipeline-Schritt ein Helfer" für Lesbarkeit (DECISIONS
2026-10-06); das Mesh bleibt bewusst dumm (fertige Daten rein), damit
Kugel-Generator (V3) und ein möglicher OBJ-Loader (K1) dasselbe
unveränderte Mesh füttern.

**Besonderheiten:** Abnahme als Sabotage-Test (Farbwechsel, Eckpunkt
ziehen, Treiber-Fehlertexte lesen) · die w-Division per eigenem
Experiment entdeckt (Perspektiv-Teiler, wird in V3 gebraucht) ·
Kanten noch ohne MSAA — Feinschliff in V6.
