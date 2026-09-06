# VORJAHR_AUFGABEN.md — Aufgabentexte des Modul 5-101 vom Vorjahrgang

Ownership: Nur die Aufgabentexte des Moduls 5-101, wie sie der um ein
Semester höhere Jahrgang bekommen hat — als **unverbindliche Vorschau**,
von Isor am 2026-09-06 eingebracht. Sobald Isors eigene Originaltexte
vorliegen, bekommt jede Aufgabe ihre eigene `ASSIGNMENT_*.md` nach dem
Muster von `Uni/Semester_2/`, und diese Datei wandert ins Archiv.

**Nicht verbindlich:** Inhalte können sich ändern, und die
Fälligkeitsdaten hier sind die des Vorjahrgangs (dessen Semester lief
bis August) — **Isors Termine stehen im `STUNDENPLAN.md`.** Wortlaut
weitgehend original übernommen; dreifach wiederholte Präsentations-
Passagen sind einmal ausgeschrieben und werden referenziert.

**Die Modul-Logik, aus den Texten ablesbar:** Alle Aufgaben hängen an
**einer** durchgehenden Medienproduktion — Spieleprototyp → Game Pitch
mit GDD (das GDD ist die **benotete Zwischenprüfung**) → Alpha → Beta →
Goldmaster → Projektreflexion. Die Modulnote entsteht am Ende über ein
**Portfolio** aller Arbeitsproben (nach Feedback verbessert). Daneben
stehen zwei eigenständige C++-Aufgaben (Konsolenprojekt, 3D-Model-
Viewer).

---

## 1 · C++ Konsolenprojekt (K2, K5, S3, S4, S5) — Vorjahr fällig 10. Apr

Schreibe ein C++ Programm; was umgesetzt wird, ist frei. Pflicht-
Themenbereiche: **Klassen & OOP · Pointer & Objekte · Memory
Management.** Mindestens User-Input und Output. Vor Festlegung der
Projektidee mit dem Fachbereichs-Team austauschen.

Vor Beginn einen **Zeitplan als Tabelle mit drei Spalten** erstellen:
Meilensteine der geplanten Umsetzung · geschätzte Dauer je Meilenstein ·
tatsächlich gebrauchte Dauer (während der Arbeit gemessen).

Abgabe: Zeitplan als PDF · aufgeräumte Projektdateien · Build.

Tipps (Auszug): An den Monsterkampf-Simulator- und Escape-Room-Abgaben
orientieren · ein einfaches CPP-Spiele-Framework wie **raylib** ist
erlaubt · Code von anderen aus dem Kurs testen lassen · unzulässigen
User-Input abfangen (Wertebereiche, nicht-numerische Eingaben) ·
strukturierte Programmarchitektur.

Feedbackelemente — Proficiency: läuft stabil und fehlerfrei? Memory
Leaks zur Laufzeit? Ein-/Ausgabe verständlich? Geplante Funktionalität
erfüllt? — Process: einheitliche Coding-Convention? OOP-Prinzipien
angewandt? Logik und Architektur schlüssig? — Person: Code verständlich
und lesbar? Kreativer Umgang mit der Aufgabe?

## 2 · 3D Model-Viewer (K2, S3, S4) — Vorjahr fällig 1. Mai

Mit der **OpenGL-API und C++** einen simplen 3D-Model-Viewer erstellen,
der ein texturiertes 3D-Modell darstellt; passende **GLSL-Shader** für
Texturen und Licht schreiben.

Pflicht: Anwendungsfenster · programmierbare Render-Pipeline mit
Vertex- und Pixel-Shader · sinnvoll strukturierter, erweiterbarer
Programmaufbau · mindestens ein texturiertes 3D-Modell · mindestens ein
Licht · bewegbare Kamera · Skybox oder Ähnliches.

Optional: weitere Objekte mit unterschiedlichen Oberflächen (glänzend,
matt, reflektierend, transparent, Normal Maps) · Modell-Laden aus
Dateien (OBJ, FBX) · Post-Processing-Shader · Stencilbuffer-Effekte ·
Text-Rendering (SDFs, Dear ImGui) · Glas/Transparenz · Campus-DevKits.

Abgabe: aufgeräumte Projektdateien **mit allen externen Dependencies** ·
funktionstüchtiger Build.

Tipps: Render-Pipeline vorab als **UML-Diagramm** planen · iterativ
arbeiten — erst Must-Haves, dann Optionales (wertet zugleich das
Portfolio auf) · **RenderDoc** zum Pipeline-Debugging · Arbeitsschritte
und Umfang mit der Fachbetreuung planen.

Feedbackelemente — Proficiency: stabil und fehlerfrei? Objekt richtig
texturiert und beleuchtet? — Process: Memory Leaks? Pipeline stabil,
performant, modular und erweiterbar? — Person: Code kommentiert und
lesbar? Liebe zum Detail? Über die Vorlesung hinaus beschäftigt?

## 3 · Spieleprototyp (K1, K5, S3, S4, S5, S6) — Vorjahr fällig 15. Mai

Funktionierenden Spieleprototyp mit der **Engine deiner Wahl**
entwickeln und vor der Klasse präsentieren; Spielidee vorher mit der
**Fachbereichsleitung absprechen**. Allein oder im Team freigestellt.
„Hierbei hast du auch die Chance, deine Fähigkeiten in der Unreal
Engine unter Beweis zu stellen." Ziel: die Grundidee der
**Abschluss-Medienproduktion** austesten — sinnvoller Game Flow, macht
es Spaß? Zweckdienliche Werkzeuge sind hier erlaubt (bei Unreal z. B.
Blueprints), anders als in der Hauptproduktion.

Drei Schritte: Konzept (Idee mit Fachbereichsteam besprechen) →
Umsetzung → Überprüfung (testen, überarbeiten; Ergebnis fließt in die
Game-Pitch-Abgabe ein).

Abgabe: PDF (**mind. 500 Wörter**, eigenes Deckblatt) über die
ursprüngliche Idee und die Prototyp-Erkenntnisse (was ändern, was
übernehmen) · aufgeräumte Projektdateien · spielbarer Build.

Tipps: Ziel des Prototyps im Hinterkopf halten · das PDF taugt als
GDD-Grundlage · genug Zeit für die Grundidee · keine zeitintensiven
Entwicklungsprozesse · **kreative Risiken ja, technische Risiken
nein** · nicht „stuck" bleiben.

Feedbackelemente — Proficiency: Erkenntnis-taugliche Anpassung der
Idee? Verständnis für Spielspaß? klare Dokumentation der Erkenntnisse?
Gameplay richtig implementiert, fehlerfrei? — Process: sinnvolle
Anpassungen? Logik fehlerfrei fürs Testziel? Teamaufteilung? Zeit in
erkenntnisfördernde Funktionalität? kreative Risiken? — Person:
geplant? wie getestet? Beteiligung? Code/Blueprints lesbar?

## 4 · Game Pitch (S1, K2, K3, K4) — Vorjahr fällig 22. Mai

Präsentation der Spielidee: Projektbeschreibung, vergleichbare
Produkte, **USP**, Ziele und Ergebnisse, zeitlicher Ablauf. Alles in
ein ausführliches **GDD** überführen, das nach Einarbeitung des
Präsentations-Feedbacks hochgeladen wird.

GDD-Pflichtinhalte: **mind. 1500 Wörter** · Projektbeschreibung
(Kernkonzept, Mechaniken) · USP · Thema/Aussehen/Story · Referenzen ·
Zeitplan · technische Daten (Zielplattform, Hardware) ·
Entwicklungsumgebung (Engine, Asset-Tools) · Zielpublikum · Ziel- und
Umfangsbeschreibung. Teams dokumentieren Rollenverteilung; alle tragen
gleich bei. Zusätzlich beschreiben, wie hohe Qualität über die
Projektdauer gesichert wird (Produktionsprozesse analysieren).

Abgabe: PDF mit Deckblatt · Präsentation als PDF.

Tipps: Idee weiterdenken · Pitch vorab Mitstudierenden/Zielgruppe
zeigen · **Lerntagebuch bzw. Produktionslogbuch** führen.

Feedbackelemente — Proficiency: sicher präsentiert? USP erkennbar?
Ziel eindeutig? — Process: GDD vollständig, Features genau? realistische
Zeitabläufe **mit Pufferzeiten**? Prototyp-Ergebnisse berücksichtigt?
Referenzen? — Person: Liebe zum Detail? Formatvorgaben bzw. passendes
eigenes Design? Aufgabenverteilung? Quellenverzeichnis?

### Summative Zwischenprüfung: Projektplanung — Vorjahr fällig 29. Mai

Das **GDD wird als PDF benotet** (zählt in die Modul-Gesamtnote).
Kriterium: „sinnvollen Projektplan erstellen (Umfang, Aufgaben,
Termine) und die Projektidee erfolgreich kommunizieren." Skala:
Sehr gut – First · Gut – Upper Second · Befriedigend – Lower Second ·
Ausreichend – Third · Nicht ausreichend / keine Abgabe – Fail.

## 5 · Alpha (K1, K5, S2, S3, S4, S5, S6) — Vorjahr fällig 26. Jun

Stand: möglichst **Core-Feature-Complete**, Win-/Lose-Conditions,
**spielbar — der Core-Gameloop funktioniert**. Content absehbar, erste
Level testbar, erste GUI-Elemente, Audiofeedback, erste Assets; alle
essentiellen Skripte und Grundverhalten stehen. Ab hier Tester-Feedback
für Core-Mechaniken einholen; GDD nach der Präsentation anpassen.

Präsentation (10–20 Min, visuell begleitet, vorbereitet — „nicht
einfach die Engine aufmachen"): Fachbetreuung = Publisher, Kurs =
Industriekontakte. Zeigen: Stand vs. Planung (**Ist-Soll-Vergleich**,
Deadlines, Problemlösung bei Verzug), Workflow, Probleme und
Lösungsstrategien, Praxisdemonstration, ggf. Teamarbeit. Was sind die
nächsten Schritte bis zur Beta?

Abgabe: Präsentation als PDF · Alpha-Build · aktualisiertes GDD mit
angepassten Zeitplänen (Änderungen farblich markierbar).

Tipps: noch kein Polish, Funktionalität zuerst · bei Planungsproblemen
die Ursache benennen (Scope? Wissen?) und Strategie entwickeln · GDD
ist ein lebendes Dokument · Timeline, Aufgabenplanung, Assetliste
aktuell halten · 5×5-Folienregel · Zielgruppe der Präsentation bedenken
· Publisher-Simulation ernst nehmen (aber niemand streicht die
Finanzierung) · **Lerntagebuch/Produktionslogbuch** führen.

Feedbackelemente — Proficiency: Stand im Einklang mit der Production-
Pipeline? Game-Loop funktioniert und ergibt Sinn? stabil? Darstellung
verständlich? Gameplay richtig? Präsentationstechnik? — Process:
Entwicklungsprozess **dokumentiert und nachvollziehbar**? Probleme
identifiziert und gelöst? — Person: Alpha-Qualität erreicht?
Präsentation vertrauenserweckend? Liebe zum Detail? GDD und Zeitpläne
sinnvoll überarbeitet?

## 6 · Beta (K1, K5, S2, S3, S4, S5, S6) — Vorjahr fällig 7. Aug

Stand: **Feature-Complete, alles funktioniert, Content vollständig** —
ab hier nur noch Bugfixing und Polish. Fremde Tester heranziehen. GDD
nach der Präsentation anpassen. Präsentation und Abgabe wie bei der
Alpha (nächste Schritte: bis zum Goldmaster); Vorgabe zusätzlich:
Graphic-Assets, Sounds und GUIs implementiert.

Tipps (zusätzlich): das Spiel wirklich **vervollständigen** — fürs
Aufhübschen ist später Zeit · Code jetzt schon sauber, damit Zeit für
sichtbaren Polish bleibt.

Feedbackelemente: wie Alpha, mit „Erreicht das Projekt Beta-Qualität
oder höher?"

## 7 · Goldmaster (K1, K5, S2, S3, S4, S5, S6) — Vorjahr fällig 28. Aug

Stand: **komplett spielbar und gepolished, veröffentlichbar.** Content
nach Projektplan vollständig, GUI/Audio/Assets eingebunden, Projekt
stimmig; Code vollständig, aufgeräumt, strukturiert, lesbar.

Präsentation wie Alpha/Beta; alternativ ein Format wie eine
Spiele-Premiere auf einer Messe (mit Fachbereichsleitung absprechen).
Wurden die Ziele erreicht? Tipp: **Trailer** präsentieren; ab hier nur
noch Maintenance-Mode.

Abgabe: Präsentation (z. B. PDF) · Gold-Build · aufgeräumte
Projektdateien · finale GDD-Fassung.

Feedbackelemente — zusätzlich zu Alpha/Beta unter Process: einheitliche
Coding-Convention? Code sinnvoll strukturiert? **wartbar und
skalierbar**? — Person: Gold-Qualität? Code lesbar? GDD und Zeitpläne
**eingehalten**?

## 8 · Projektreflexion (K1, K2, K4, K5, S3, S5) — Vorjahr fällig 28. Aug

**Mind. 1000 Wörter**, ansprechend formatiert, PDF mit Deckblatt,
ggf. Quellen. Projekt und eigene Herangehensweise kritisch
reflektieren: ursprüngliche Ziele vs. erreichte, Maßnahmen aus gut und
schlecht Gelaufenem — ausdrücklich **auch Soft-Skills**: Kommunikation,
persönliche Schwachpunkte, künstlerische Idee, Zeit- und
Ressourcenplanung. Zu Problemen auch **Lösungen** formulieren.

Mögliche Punkte: kreativer Hintergrund und Richtung · Idee vs.
Umsetzung · Ergebnisse und Erfolge · Kosten-/Ressourcenmanagement ·
Zeit-/Projektmanagement · Kommunikation · Qualitätsbewusstsein ·
Gut/Schlecht + Probleme/Lösungen · Zeitaufwand und Engagement.

Feedbackelemente — Person: nicht nur extrinsische Umstände, auch
intrinsische Aspekte? nicht nur Hard-Skills? eigene Arbeitsweise
kritisch reflektiert?

## 9 · Portfolio (Modulnote, 100 Punkte) — Vorjahr fällig 28. Aug

Sammlung **aller** Arbeitsproben des Moduls, nach Feedback verbessert:
C++ Konsolenprojekt · 3D Model Viewer · Spieleprototyp · Game Pitch ·
Alpha · Beta · Goldmaster · Projektreflexion. Bewertung nach den drei
Ps, **nur wenn alle Lernziele erreicht** sind (sonst Fail mit
Hinweisen):

- **Proficiency:** „Ich beherrsche C++ und habe Kenntnisse in Graphics
  Pipeline und Shader-Programmierung. Projekte auf Industrieniveau."
- **Process:** „Einarbeiten in Sprache/Engine, dokumentieren, planen,
  präzise nach Plan umsetzen; wartbar und skalierbar entwickeln."
- **Person:** „Sorgsame, gut dokumentierte Planung; ordentliche
  Präsentationen; Feedback sammeln und umsetzen."

Tipps: **alle** Ergebnisse einpacken (Vielfalt und Menge zählen) ·
übersichtliche Ordnerstruktur und sprechende Dateinamen ·
Rechtschreibung, Grammatik, Formatierung.

## Lernziel-Katalog des Moduls

K1 Workflows auf Industriestandard erörtern · K2 geeignete
Produktionstechniken beurteilen und auswählen · K3 wesentliche Stil-
und Gestaltungselemente gegebener Produktionen erkennen · K4
Produktionsprozesse des Fachbereichs theoretisch/kulturell analysieren ·
K5 eigene Abläufe und kreative Entscheidungen bewerten · S1 komplexe
Medienproduktionen planen · S2 Produktionswerkzeuge professionell
verwenden · S3 wirksame Problemlösung · S4 Theorie in Praxis überführen
· S5 Abläufe nach Feedback anpassen · S6 industrierelevante
Arbeitsabläufe umsetzen. Je Lernziel gilt am Ende: erreicht · teilweise
erreicht · noch nicht erreicht — **alle** müssen erreicht sein.
