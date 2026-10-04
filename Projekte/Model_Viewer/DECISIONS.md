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
