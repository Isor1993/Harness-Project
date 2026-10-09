# DECISIONS.md — Entscheidungen 3D-Model-Viewer

Ownership: Nur Entscheidungen zum 3D-Model-Viewer (Uni-Aufgabe 2, Modul
5-101) — was entschieden wurde, warum, und welche Alternativen verworfen
wurden. Kein Plan (das ist die ROADMAP dieser Schicht), kein Ereignis
(das ist das LOG). Die Aufgabenstellung besitzt
`Uni/Semester_3/VORJAHR_AUFGABEN.md`; der Minimal-Rahmen und die
Arbeitsteilung stehen in `Uni/DECISIONS.md` → „2026-10-01 —
3D-Model-Viewer minimal".
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.
Überholte Einträge wandern ins Archiv der Schicht (wird beim ersten
Fall angelegt), mit Angabe, wodurch sie abgelöst wurden.

## 2026-10-04 — Eigene Projekt-Schicht und eigenes Code-Repo

Was: Der Viewer bekommt die Schicht `Projekte/Model_Viewer/` (DECISIONS,
ROADMAP, LOG) und ein eigenes Code-Repo `Model-Viewer` nach dem Muster
von Lane Defender. Marke `PROJEKT_MODEL_VIEWER` in `Kern/PFADE.md` und
Freigabe folgen mit der Repo-Anlage (ROADMAP dieser Schicht, V0).
Warum: Projekt-Details sollen die Uni-Chronik nicht fluten; das
Lane-Defender-Muster (Schicht + eigenes Repo mit eigener V-Nummer) hat
getragen. Entschieden von Isor in der Design-Session.
Verworfen: alles in der Uni-Schicht führen (weniger Dateien, aber
Chronik und Projekt-Kleinteile mischen sich).

## 2026-10-04 — Minimal-Zuschnitt: Kugel, Orbit-Kamera, Cubemap, Toon in Stufen

Was: Das eine texturierte Pflicht-Modell ist eine **prozedural erzeugte
Kugel** (Code statt Fremddatei); ein Mini-OBJ-Loader ist nur Kür, falls
vor der Abgabe Zeit übrig ist. Die Kamera ist eine **Orbit-Kamera**
(zwei Winkel, ein Abstand — Maus dreht ums Modell, Rad zoomt). „Skybox
oder Ähnliches" wird als **echte Cubemap** erfüllt. Der Toon-Shader
beginnt mit **reinen Lichtstufen**; ob eine Outline dazukommt,
entscheidet Isor am ersten echten Bild.
Warum: Eine gekrümmte Fläche zeigt die Toon-Stufen, die ein Würfel
verschluckt; Orbit ist für einen Viewer das natürliche und kleinste
Kameramodell; die Cubemap ist das Standardrezept mit Lernwert, fertige
CC0-Himmel sind frei verfügbar. Rahmen bleibt der Minimal-Beschluss
(`Uni/DECISIONS.md` → „2026-10-01 — 3D-Model-Viewer minimal").
Verworfen: hartkodierter Würfel (je Seite nur eine Lichtstufe, der
Toon-Look wäre unsichtbar); OBJ-Loader von Anfang an (Parser-Risiko vor
dem ersten Bild); Fly-Kamera (mehr Eingabe-Code, fürs Betrachten
umständlich); Farbverlauf-Hintergrund (erfüllt wörtlich, lehrt nichts);
Outline sofort mitbauen (Aufwand über dem Abhak-Kriterium — der
Entscheid am Bild ist billiger).

## 2026-10-04 — Technik-Stack: GLFW, GLAD, GLM, stb_image auf OpenGL 4.6 Core

Was: Fenster und Eingabe über **GLFW**, Funktions-Laden über **GLAD**,
Mathe über **GLM**, Bild-Laden über **stb_image**; **OpenGL 4.6 Core
Profile**; Build als **Visual-Studio-Solution ohne CMake**; alle vier
Bibliotheken liegen mit im Code-Repo. Konvention: SAE-C++ wie beim
Konsolenprojekt (`Kern/CODE_GUIDELINES.md`).
Warum: Deckungsgleich mit dem Code der ersten OpenGL-Kursstunde
(GLFW + GLAD, Core Profile, Version 4.6) — der Kurs bestätigt das
Standard-Besteck. Mitgelieferte Bibliotheken erfüllen wörtlich die
Abgabe-Vorgabe „Projektdateien mit allen externen Dependencies"; VS
2026 ist verifiziert, der Prüfer baut per Klick auf die Solution.
Verworfen: OpenGL 4.5 strikt nach Versionsblatt („Core 450") — der
Unterricht zeigt 4.6, ein Treiber mit 4.5 kann praktisch immer auch
4.6, und falls die OCE aufs Blatt pocht, sind es zwei Ziffern in zwei
WindowHints; CMake (eigenes Lernthema ohne Abhak-Gegenwert);
Paketmanager statt mitgelieferter Bibliotheken (bricht die
Dependencies-Vorgabe).

## 2026-10-04 — Programmaufbau: sieben Module, GPU-Besitz nach RAII

Was: `main.cpp` (Schleife, Verdrahtung), `Window` und `Camera` verwalten
nur CPU-Zustand; `Mesh`, `Shader`, `Texture` und `Skybox` besitzen je
**genau eine GPU-Ressource** und geben sie im Destruktor frei (RAII).
Das Licht bekommt **keine** Klasse — Richtung und Farbe gehen als zwei
Uniforms an den Shader. Dieser Aufbau wird später das UML-Diagramm der
Abgabe.
Warum: Erfüllt „sinnvoll strukturiert, erweiterbar" mit Klassen, die
Isor auf Semesterniveau verteidigen kann; der RAII-Schnitt beantwortet
das Feedbackelement „Memory Leaks" strukturell statt über Disziplin.
Verworfen: alles in `main` wie im Unterrichts-Schnipsel (läuft, aber
nicht erweiterbar); eine Licht-Klasse für zwei Werte (Fattening); eine
App-Klasse über `main` (eine Hülle mehr ohne Gegenwert).

## 2026-10-04 — GLFW als DLL angebunden, nicht statisch

Was: Das Projekt linkt `glfw3dll.lib`, und ein Post-Build-Schritt legt
`glfw3.dll` neben die Exe. Die vorkompilierte statische `glfw3.lib`
wird nicht benutzt.
Warum: Die statische Fassung ist gegen die Release-Laufzeitbibliothek
gebaut; im Debug-Build (Debug-Laufzeit) meldete der Linker LNK4098 —
zwei Laufzeitbibliotheken in einem Programm, also auch zwei getrennte
Speicherverwaltungen. Die DLL hat ihre Laufzeit bei sich, beide
Konfigurationen bauen warnungsfrei.
Verworfen: die Warnung ignorieren (gemischte Laufzeiten sind genau die
Sorte stiller Fehlerquelle, die das Feedbackelement „Memory Leaks"
meint); GLFW selbst kompilieren (bräuchte CMake, siehe
Technik-Stack-Eintrag oben).

## 2026-10-06 — Shader-Helfer je Pipeline-Schritt, Fehlermeldung nennt die Datei

Was: `Shader.cpp` trägt drei klassenlose static-Helfer — ReadTextFile,
CompileShader, LinkProgram — je einen pro Pipeline-Schritt; der
Konstruktor erzählt nur noch die Abfolge. Compile-Fehlermeldungen
drucken den Dateipfad mit (dritter Parameter von CompileShader).
Warum: Lesbarkeit, auf Isors Vorschlag (der Konstruktor blähte sich);
„je Schritt eine benannte Funktion" ist zugleich die Abgabe-Verteidigung.
Der Pfad in der Meldung ist Isors Befund aus dem Sabotage-Test: Der
Treiber kennt keine Dateinamen — ohne Zusatz bliebe unklar, ob vert
oder frag bricht.
Verworfen: ein gemeinsamer Status-Block-Helfer (wäre DRY auf gleich
*aussehendem*, nicht gleichem Code — Shader und Programm haben drei
verschiedene gl-Funktionspaare); nur den Link-Status auszulagern
(fasst den Member an, die Helfer bleiben klassenlos).

## 2026-10-07 — Vertex-Layout: 8 Floats je Ecke von Anfang an

Was: CMesh stellt auf das interleaved Layout Position (3) + Normale
(3) + UV (2) um — drei Steckdosen, Stride 32 Bytes; der
Kugel-Generator (`Geometry.cpp`) schreibt alle acht Werte je Ecke mit.
Warum: V3 braucht die UV für die Textur, V4 die Normalen fürs Licht —
ein Layout-Umbau statt zwei, und Kugel-Normalen sind geschenkt
(Richtung vom Mittelpunkt). Ungenutzte Steckdosen stören nicht: Der
Shader greift nur ab, was er deklariert.
Verworfen: erst Position plus UV, Normalen bei V4 nachrüsten (zweiter
Umbau mitten im Licht-Baustein); ein eigener Buffer je Datenart (mehr
Verwaltung ohne Gegenwert bei einem Modell).

## 2026-10-07 — Tiefenpuffer ab der ersten 3D-Geometrie

Was: GL_DEPTH_TEST ist an, und glClear wischt je Frame Farbe **und**
Tiefe (GL_DEPTH_BUFFER_BIT, Bit-Oder).
Warum: Ohne Tiefenpuffer gilt „wer zuletzt malt, gewinnt" — bei der
ersten Kugel übermalte die Rückseite die Vorderseite (Riss am Äquator,
Zacken). Der Tiefenpuffer merkt sich je Pixel die Entfernung und lässt
nur Näheres übermalen.
Verworfen: nur Rückseiten wegschneiden (GL_CULL_FACE) — hätte der
konvexen Kugel geholfen, bricht aber bei jedem konkaven Modell
(Kür K1, OBJ-Loader); der Tiefenpuffer löst den allgemeinen Fall.

## 2026-10-07 — KI-Deklaration: markiert wird, was Isor nicht verteidigen kann

Was: `Geometry.h`/`Geometry.cpp` tragen einen KI-Vermerk im Datei-Kopf
(„written with AI assistance, reviewed and walked through");
`Texture`, `Camera` und der Eingabe-Teil von `Window` nicht. Die
Deklaration wird zusätzlich in der Abgabe-Doku genannt
(ABGABE_NOTIZEN → Besonderheiten V3, ausformuliert in V6).
Warum: Isors Linie — markiert wird, was er nicht selbst hätte
schreiben können und nicht voll verteidigen kann (die
Kugelkoordinaten-Mathe); Texture und Camera sind im
Stationen-Durchgang erklärt und teils selbst nachjustiert
(Yaw-Vorzeichen).
Verworfen: alle in der V3-Arbeitsteilung von Claude geschriebenen
Dateien markieren (Isors Entscheid vom 2026-10-07: nur die Kugel-Mathe
liegt über seinem Niveau).

## 2026-10-07 — Stylized-Toon: weiche Kante statt harter Stufen

Was: Der Toon-Look rechnet eine smoothstep-Kante um die
Schattenschwelle (`F_SHADOW_EDGE` 0.4, Weichzone `F_EDGE_SOFTNESS`)
und mischt per mix zwischen getöntem Schatten (`VEC3_SHADOW_TINT`,
kühl-blau) und voller Helligkeit — zwei Töne, keine Stufenzahl. Der
Tint ist zugleich die Grundhelligkeit: Die Nachtseite bleibt sichtbar,
der Pauschal-Ersatz für nicht gerechnetes indirektes Licht.
Warum: Die floor-Stufen wurden gebaut und am echten Bild als zu hart
verworfen; Isors Ziel ist Stylized Richtung Genshin, und deren
Grundrezept ist die schmale weiche Kante plus kühler Schatten. Die
Schwelle 0.4 hält die flache Wiese bei der 27°-Sonne im Lichtband
(dot der Boden-Normale ≈ 0.45).
Verworfen: floor-Quantisierung in N Stufen (zu hart, Bänder 0.35/0.5
zu ähnlich); Vollschwarz als Nachtseite (Isors Grundhelligkeits-
Entscheid — Spielobjekte müssen nachts sichtbar bleiben; die
max-Untergrenze 0.35 ging später im Tint auf).

## 2026-10-07 — Skybox: eine GPU-Ressource, Würfel als CMesh, xyww-Tiefe

Was: `CSkyBox` besitzt nur die Cubemap (sechs 512er-Gesichter,
CLAMP_TO_EDGE in S/T/R, **kein** Vertikal-Flip); der Himmelwürfel ist
ein normales CMesh aus `GenerateSkyboxCubeVertices` (8er-Layout,
Normalen und UV null). Der eigene Shader liest per `samplerCube` über
die Eckrichtung; `gl_Position.xyww` legt die Tiefe fest auf 1.0,
gezeichnet als Letztes mit GL_LEQUAL, View per `mat3`-Stutzen ohne
Translation. Himmel 05 aus dem CC0-Paket „Cloudy Skyboxes" (Screaming
Brain Studios), Kreuz-Blätter per Skript zerschnitten, Original im
Datenbaum (`03_AssetLibrary\Extern_Frei\Himmel_Cloudy_SBS\`).
Warum: hält den Programmaufbau-Beschluss „je Klasse genau eine
GPU-Ressource"; der Würfel braucht kein Sonder-VAO; xyww nutzt die
w-Division (Tiefe w÷w = 1), LEQUAL löst den Randfall „1.0 gegen
leere Leinwand"; zuletzt zeichnen spart jeden verdeckten Himmelspixel.
Verworfen: CSkyBox besitzt zusätzlich Würfel-VBO/VAO (bräche den
RAII-Schnitt); Flip wie bei CTexture (Cubemaps lesen von oben); das
bottom-Gesicht durch eine Boden-Textur ersetzen (ungleiche Größe macht
die Cubemap unvollständig → alles schwarz; Isors Experiment).

## 2026-10-07 — Welt statt Würfeltrick: Bodenplatte mit Rand-Fade

Was: 80×80-m-Plane (`GenerateGroundPlaneVertices`: Normalen nach
oben, UV kachelt Isors Seamless-Gras über eine Tiles-Konstante),
Höhe −1 = Kugel-Südpol — der Ball steht. Der Rand blendet im frag
per Zaun-Maß `max(abs(x), abs(z))` und smoothstep 28→38 in eine
Horizontfarbe; die Fade-Grenze läuft damit parallel zur Plattenkante.
Warum: Ein „Unten" verankert das Modell — als Weltobjekt mit echter
Perspektive statt als Malerei im mitreisenden Himmelwürfel; das
quadratische Maß ist Isors Form-Entscheid am Bild, die
Seamless-Textur (Isors Fund) löste die sichtbare Wiederholung.
Verworfen: Kamera-Entfernungs-Nebel (machte beim Rauszoomen alles
milchig; lieferte nebenbei die Staffelstab-Lektion — Positionen
interpolieren, fertige Längen nicht); Kreis-Fade per `length` (fraß
die Plattenecken); Alpha-Ausblenden (braucht Blending — gestrichen,
siehe unten).

## 2026-10-07 — Sonnen-Gizmo und Kontakt-Schatten über einen Unlit-Shader

Was: Ein Mini-Paar `unlit.vert|.frag` (MVP durchreichen, flache Farbe
raus) zeichnet dieselbe Kugel-Mesh zweimal zusätzlich: als weiße
Sonnenscheibe bei −Lichtrichtung × 60 m (Radius 2.5) und als
plattgedrückten Kontakt-Schatten (Skalierung y 0.01, Höhe −0.99
gegen Z-Fighting, 0.88 m von der Sonne weg versetzt, dunkles
Grasgrün statt Schwarz).
Warum: „Ein Mesh, viele Objekte" — erste echte translate/scale-
Nutzung der Model-Matrix; das Gizmo koppelt die sichtbare Sonne an
die Licht-Konstante (eine Quelle, Settings bewegen später beides);
der Kontakt-Fleck klebt den Ball an den Boden — sein Job ist Erden,
nicht Physik.
Verworfen: Sonnen-Textur (läse sich als Planet; Anime-Sonnen sind
flache Scheiben, der Glow braucht additives Blending); echtes Shadow
Mapping (größtes Einzelstück der Echtzeitgrafik, jenseits des
Rahmens); volle Schatten-Projektion (löste den Fleck 2 m vom Ball);
Gras-Textur auf dem Fleck (Kugel-UVs strudeln am Pol, Muster deckt
sich nicht mit der Wiese — Isors Experiment).

## 2026-10-07 — Blending-Baustein gestrichen

Was: Der gebündelte Baustein „Blending" (Alpha-Rand, additiver
Sonnen-Glow, Multiply-Schatten) wird nicht gebaut; reaktiviert nur,
falls das OCE-Feedback nach der frühen Abgabe mehr verlangt.
Warum: Isors Komplexitätsgrenze ist erreicht („das ist meine
Grenze"), die Pflicht der Aufgabe ist komplett erfüllt, und der Look
trägt auch ohne — obwohl drei Design-Wünsche desselben Abends auf
genau diese Technik liefen.
Verworfen: Blending jetzt lernen (das Zeitbudget vor der Abgabe
gehört dem Tuning-Fenster und V6).

## 2026-10-08 — Outline per Skalierung, Wickelrichtung auf CCW-Standard

Was: Die Inverted-Hull-Outline (O1) entsteht nicht per
Normalen-Versatz im Vertex-Shader, sondern als zweiter Draw der Kugel
mit skalierter Model-Matrix (`F_OUTLINE_SCALE` 1.03), unlit schwarz,
Front-Culling drumherum (Schalter an, GL_FRONT, Draw, GL_BACK,
Schalter aus). Im selben Zug wickelt der Kugel-Generator seine
Dreiecke jetzt CCW von außen — OpenGLs Front-Face-Standard.
Warum: Isors eigener Entwurf — bei einer Kugel ist Skalieren
mathematisch identisch mit dem Normalen-Versatz (die Normale zeigt
vom Mittelpunkt weg), spart einen eigenen Shader, und jede Zeile ist
auf Semesterniveau verteidigbar. Der Winding-Fix: Der erste
Culling-Einsatz des Projekts enttarnte die CW-Wicklung aus V3
(schwarzer Voll-Ball statt Ring); die Konvention gehört in den
Generator korrigiert, nicht umgangen.
Verworfen: `outline.vert` mit Position + Normale × Dicke (der
ROADMAP-Plan — nötig erst für beliebige Meshes, Kür K1);
glCullFace(GL_BACK) als Symptom-Fix (hätte die falsche Wicklung
zementiert).

## 2026-10-08 — CApplication: Zeiger-Member mit Initialize-Gruppen

Was: Szene und Schleife ziehen aus main in die neue Klasse
CApplication. Alle besessenen Objekte sind rohe Zeiger-Member
(nullptr-Start, SAE-p-Präfix), erschaffen per new in
InitializeShaders/InitializeMeshes/InitializeTextures, gelöscht
gesammelt im Destruktor in umgekehrter Reihenfolge; das Fenster
bleibt geliehen (main besitzt — der Zeigertyp dokumentiert den
Besitz). Die Schleife ruft sechs parameterlose Ein-Zweck-Stationen
(Ball, Ground, Sun, Shadow, Outline, Skybox); die Frame-Matrizen
sind Wert-Member. main: erzeugen, Initialize, Run — drei Handgriffe.
Warum: Isors Design in dritter Iteration — die
Konstruktor-Initialisierungsliste („nicht verteidigbar") und
Kommentar-Regions abgelehnt, Struktur aus echten Sprachmitteln
verlangt; Zeiger geben Membern den vertrauten C#-Lebenslauf (leer
geboren, im Rumpf befüllt), und delete-auf-nullptr macht
Teil-Abbrüche der Initialisierung sicher. Revidiert „keine
App-Klasse" vom 04.10. — damals war main 30 Zeilen, vor dem Umbau
250.
Verworfen: Initialisierungsliste mit Wert-Membern (Claudes erster
Bau — baute warnungsfrei, las sich für Isor aber wie Vererbung);
alles in main mit freien Render-Funktionen (Referenz-Parameter je
Aufruf); unique_ptr (im Unterricht nur gestreift — new/delete kann
Isor vollständig erklären, der Umstieg bliebe eine
Fünf-Minuten-Änderung).
