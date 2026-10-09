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

## V3 · Texturierte Kugel und Orbit-Kamera (fertig 2026-10-07)

**Zeit:** 4:13 h am 2026-10-07 (Grindstone-Stand beim Sichern, die
Session lief noch) — enthält das Fachwort-Warmup und den
Stationen-Durchgang. Projekt gesamt damit rund 13:16 h.

**Gebaut:** MVP-Matrizenkette (GLM, `CShader::SetMat4`) zuerst am
Dreieck bewiesen · Kugel-Generator `Geometry.cpp` (UV-Kugel 32×32,
interleaved 8 Floats: Position, Normale, UV — Stride 32 Bytes) ·
`CTexture` (stb_image, Mipmaps, Fach-Bind) · `CCamera` als
Orbit-Kamera (zwei Winkel + Abstand; Maus dreht, Rad zoomt mit
Anschlägen 1,5–20, Pitch-Stopp ±89°) · Fenster-Eingabe
(Cursor-Delta, Scroll-Callback, `GetAspectRatio`) · Tiefenpuffer an,
Clear wischt Farbe und Tiefe.

**Warum so:** 8-Float-Layout von Anfang an — ein Umbau statt zwei, V4
(Licht) braucht die Normalen (DECISIONS 2026-10-07) · Tiefenpuffer
statt Culling, löst auch konkave Modelle wie den Kür-OBJ-Loader
(DECISIONS 2026-10-07) · die Kamera rechnet ihre Position mit
demselben Kugelkoordinaten-Rezept wie der Generator ·
Arbeitsteilung nach dem Beschluss vom 01.10.: GLSL und Verdrahtung
Isor, Drumherum Claude mit Stationen-Durchgang.

**Besonderheiten:** Lehrbuch-Fehler dokumentiert — ohne Tiefenpuffer
übermalte die Kugel-Rückseite die Vorderseite (Riss am Äquator) ·
**KI-Deklaration:** `Geometry.h`/`Geometry.cpp` tragen einen
KI-Vermerk im Datei-Kopf (Isors Linie: markiert wird, was er nicht
verteidigen kann — DECISIONS 2026-10-07); die Deklaration gehört in
die Abgabe-Doku (V6) · die Gras-Textur ist ein CC0-Testbild aus der
Asset-Library, die finale Textur ist offen · der Pol-Wirbel der
UV-Kugel ist bekannt und im Minimal-Rahmen akzeptiert.

## V4 · Licht und Stylized-Toon (fertig 2026-10-07)

**Zeit:** Abendblock 2026-10-07, zusammen mit V5 und den Extras
≈5:30 h (Tagessumme laut Grindstone 9:43, davon V3 4:13; Projekt
gesamt 18:49 — Screenshot-Beleg). Einzeltrennung V4/V5 nicht erfasst.

**Gebaut:** Richtungslicht als zwei vec3-Uniforms
(`CShader::SetVec3`) · `triangle.frag`: Normale normalisiert, toSun
mit Vorzeichendreh, dot-Helligkeit, **Stylized-Kante** per smoothstep
um `F_SHADOW_EDGE` mit Weichzone, mix zwischen kühlem Schatten-Tint
und voll — Texturfarbe × Lichtfarbe × Ton · GLSL-Logik komplett von
Isor getippt.

**Warum so:** floor-Stufen gebaut und am echten Bild zugunsten der
weichen Kante verworfen — Ziel Stylized Richtung Genshin; der
Schatten-Tint ist zugleich Grundhelligkeit (Nachtseite bleibt
sichtbar) und ersetzt pauschal das nicht gerechnete indirekte Licht
(DECISIONS 2026-10-07).

**Besonderheiten:** Isors erste eigene Shader-Design-Entscheidung
(Grundhelligkeit statt Vollschwarz, eigenständig eingebaut) · der
Outline-Entscheid ist aus V4 herausgelöst und wartet auf die
Zeitlage vor der Abgabe (Kür O1).

## V5 · Skybox, Boden und Optik-Extras (fertig 2026-10-07)

**Zeit:** im Abendblock enthalten (siehe V4).

**Gebaut:** `CSkyBox` (RAII-Cubemap: sechs Gesichter, CLAMP_TO_EDGE
S/T/R, kein Flip, Fehlerpfad nennt das fehlende Gesicht) · eigenes
Shaderpaar `skybox.vert|.frag` (samplerCube über die Eckrichtung,
`gl_Position.xyww`, GL_LEQUAL, View ohne Translation per mat3) ·
Würfel und Bodenplatte als Geometry-Builder im CMesh-Layout · Boden
mit Seamless-Gras, UV-Kachel-Regler und quadratischem Rand-Fade
(`max(abs(x), abs(z))` + smoothstep in Horizontfarbe) · generierte
Toon-Basketball-Textur · Unlit-Shaderpaar; Sonnenscheibe bei
−Lichtrichtung × 60 m; Kontakt-Schatten als plattgedrückte Kugel
(y-Skalierung 0.01, Höhe −0.99, sonnenabgewandt versetzt) ·
`CCamera`-Bodengrenze: tiefster Pitch aus asin(Augenhöhe ÷ Abstand),
greift in Rotate und Zoom.

**Warum so:** Himmel 05 aus CC0-Paket (Screaming Brain Studios,
Original im Datenbaum, Kreuz per Skript zerschnitten) · Würfel als
CMesh hält den Ein-Ressource-RAII-Schnitt · Bodenplatte als
Weltobjekt statt bottom-Gesicht-Tausch (Cubemap-Vollständigkeit!) ·
Kontakt-Fleck statt Projektion — er soll erden · alles Weitere in
den fünf DECISIONS-Einträgen vom 2026-10-07.

**Besonderheiten:** Damit sind **alle sieben Pflichtpunkte der
Aufgabe erfüllt** · Kamera-Nebel gebaut und bewusst verworfen
(lieferte die Staffelstab-Lektion) · Blending-Baustein gestrichen,
nur auf OCE-Feedback zurück · Zeiten bei V6 noch einmal gegen
Grindstone prüfen (Ansage war diktiert).

## O1 + V6 · Outline, Aufräum-Pass und Abgabe (fertig 2026-10-09)

**Zeit:** 3:49 h am 08.10. (Grindstone-Session, Screenshot) plus die
Nachtstunden bis zum Upload am 09.10. gegen 00:30. **Projekt gesamt
laut Grindstone 22:39 h**, dazu nach Isors Einordnung ~2–3 h bewusst
nicht erfasste Lernanteile außerhalb der Produktionskette.

**Gebaut:** Inverted-Hull-Outline als skalierter Zweit-Draw
(`F_OUTLINE_SCALE` 1.03, unlit schwarz, Front-Culling mit
Rückstellung) · Wicklungs-Fix des Kugel-Generators auf CCW ·
`CApplication` (Zeiger-Member, drei Initialize-Gruppen, sechs
Ein-Zweck-Render-Stationen, alle deletes gesammelt im Destruktor) ·
4x MSAA (Window-Hint plus Enable) · Review-Pass über alle Dateien:
benannte Konstanten (GL-Version, Log-Puffer, −1, Kugel-Minima, 36er,
RGBA-Kanäle, MAT4_IDENTITY), Include-Konvention, GetUniformLocation-
Helfer ohne Guards, GLSL-Kopf-Kommentare, triangle→toon · deutsches
README mit Pflichtkriterien-Tabelle · Portfolio-Ordner
`2_ModelViewer` (READ_ME · src · release · other) und Canvas-Zip.

**Warum so:** Skalierung statt Normalen-Versatz und der Zeiger-Bau
sind Isors Entwürfe (DECISIONS 2026-10-08) — Leitlinie „jede Zeile
verteidigbar" · die Fremd-Header sind aus Warnstufe und Code-Analyse
genommen, damit die Prüfer-Ansicht nur eigenen Code zeigt (die
stb-Hinweise waren die zwei offenen VS-Analyse-Hinweise) · Guards an
den Set-Methoden entfielen auf Isors Einwand: glUniform ignoriert
−1 laut Spezifikation.

**Besonderheiten:** Der erste Culling-Einsatz deckte den schlafenden
Wicklungs-Fehler aus V3 auf — Prozess-Story für „Liebe zum Detail" ·
ballTexture-Prüffehler aus V3 im Review gefunden und behoben ·
CMake-Frage offen (Leons Ansage kam nach Fertigstellung; Nachfrage
steht im Feedback-Kästchen, Stuttgart entscheidet) · T1
Tuning-Fenster bewusst zurückgestellt bis zum OCE-Feedback ·
unbenutzte grass_color1.png entfernt · Abgabe als Zip (19,7 MB) am
09.10. gegen 00:30 in Canvas, 21 Tage vor der Frist.
