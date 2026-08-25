<!--
Ownership: Nur das Markdown-Manuskript des TDD — die führende Quelle,
aus der `Kern/Werkzeuge/abgabe_bauen.py` die .docx-Abgabefassung baut.
Formatvorlage und Bilder (TDD_Media) liegen im Datenbaum unter
Arbeitsdateien (`Kern/PFADE.md` → `DATENBAUM`); den Umgang mit der
.docx regelt `Uni/DOCX_RULES.md`. Dieser Kommentar wird beim Bauen
verworfen und landet nicht in der Abgabe.
-->

# Einleitung:

Dieses Technical Design Document (TDD) beschreibt den technischen Aufbau des Spielprototyps *Isor's Tower*. Der Prototyp ist als langfristiges Entwicklungsprojekt angelegt und soll nicht nur im aktuellen Semester, sondern auch in späteren Semestern weiterverwendet, erweitert und überarbeitet werden. Im Rahmen der Module des 2. Semesters liegt der Fokus auf der Planung, Strukturierung und Dokumentation der aktuellen technischen Systeme.

Das Dokument dient als Grundlage für die Umsetzung des Spielprojekts und soll die wichtigsten Architekturentscheidungen, Systemzusammenhänge und Erweiterungsmöglichkeiten nachvollziehbar festhalten. Da der Prototyp über mehrere Entwicklungsphasen hinweg wachsen soll, versteht sich dieses TDD als lebendes Dokument, das im weiteren Verlauf regelmäßig erweitert und aktualisiert wird.

Der Schwerpunkt im 2. Semester liegt darauf, eine simulierte und lebhafte Spielumgebung für den Spieler zu schaffen, die auch mit geringem oder keinem direkten Einfluss des Spielers eigenständig funktioniert. Die behandelten Modulthemen umfassen Softwareplanung, Asset Integration, Engine-Tool-Entwicklung, Threadoptimierung, KI-Prototyp, Simulation der Spielumgebung mit Shader- und Partikeleffekten sowie die prozedurale Erweiterung der Spielwelt.

Neue Systeme, Erweiterungen und Änderungen werden nach und nach ergänzt, überarbeitet und dokumentiert. Dadurch soll das TDD nicht nur den aktuellen Stand des Projekts beschreiben, sondern auch als technische Orientierung für spätere Semester und zukünftige Erweiterungen dienen.

## Projekt Einleitung

*Isor's Tower* ist als Adventure-RPG in einer stilisierten Fantasy-Welt geplant. Der Spieler übernimmt die Kontrolle über einen eigenen Charakter und erkundet eine offene Spielumgebung, die aus einem Dorf, den umliegenden Naturbereichen und dem namensgebenden Tower besteht. Der Bereich um das Dorf ist frei begehbar und soll in späteren Entwicklungsphasen weiter wachsen. Langfristig sollen die First- und die Third-Person-Perspektive im Spiel umschaltbar sein; der aktuelle Prototyp verwendet die First-Person-Perspektive, da das Interaktionssystem über ein Fadenkreuz und einen Strahl aus der Kamera aufgebaut ist. Das Spiel soll sowohl alleine als auch im kooperativen Multiplayer mit bis zu fünf Spielern spielbar sein.

Zu Beginn startet der Spieler in einem Dorf, das als zentraler Ausgangspunkt der Spielwelt dient. Dort kann er sich bewegen, die Umgebung erkunden und über eine Adventure Guild verschiedene Missionen annehmen. Diese Missionen führen den Spieler in die Umgebung des Dorfes oder später in den Tower. Durch das Abschließen von Missionen, das Besiegen von Monstern und das Erkunden der Spielwelt erhält der Spieler Erfahrungspunkte, mit denen er seinen Charakter aufleveln und weiterentwickeln kann.

Der Spieler soll später eine Klasse auswählen können, zum Beispiel Krieger oder Magier. Jede Klasse kann eigene Fähigkeiten, Werte und Spielweisen besitzen. Dadurch soll der Charakter über Stats, Skills und Ausrüstung stärker werden und sich langfristig an den eigenen Spielstil anpassen lassen.

Das zentrale Ziel des Spiels ist es, den Tower beim Dorf schrittweise zu erklimmen. Der Tower besteht aus mehreren Floors, wobei jeder Floor eigene Herausforderungen, Gegner und einen Floor Boss enthalten soll. Wird ein Floor Boss besiegt, kann der nächste Floor freigeschaltet werden. Dadurch entsteht eine klare Progression, bei der der Spieler seine Figur verbessert, neue Inhalte freischaltet und sich immer weiter in den Tower vorarbeitet.

Langfristig sind weitere Systeme geplant, die die Spielwelt lebendiger und persönlicher machen sollen. Dazu gehören zum Beispiel das Gestalten eines eigenen Grundstücks, das Anbauen von Pflanzen, Crafting sowie weitere Interaktionsmöglichkeiten mit der Umgebung.

# Entwicklungsumgebung und verwendete Software

Für die Entwicklung und Dokumentation des *Isor's Tower Prototype* werden verschiedene Programme und Werkzeuge verwendet. Die Entwicklungsumgebung ist so aufgebaut, dass sowohl die technische Umsetzung im Unity-Projekt als auch die Planung, Dokumentation, Zeiterfassung und Versionsverwaltung des Projekts unterstützt werden.

Stand 6.06.26

Diese Werkzeuge in [Tabelle 1](#_Ref_Tab_1) unterstützen unterschiedliche Bereiche des Entwicklungsprozesses. Unity bildet die technische Grundlage des Spielprototyps. Innerhalb von Unity werden zusätzlich der Shader Graph für die Shader von Mond, Wasser und Gras sowie der VFX Graph für die Partikeleffekte verwendet. Visual Studio dient der Programmierung der C#-Skripte, Blender der Erstellung eigener 3D-Modelle wie der Bäume und der Gras-Meshes, die anschließend als FBX importiert werden. GitHub Desktop dient der Versionsverwaltung und hilft dabei, Projektstände nachvollziehbar zu sichern. Microsoft Word wird für die schriftliche Dokumentation genutzt, während draw.io für technische Diagramme wie UML-Klassendiagramme, FSM-Übersichten und Ablaufpläne verwendet wird. Instagantt unterstützt die zeitliche Projektplanung, und Grindstone 4 wird für die genauere Erfassung der Arbeitszeit eingesetzt.

  ---------------------------------------------------------------------------------------------------------------
  Bereich                Software/Tool        Version       Verwendung im Projekt
  ---------------------- -------------------- ------------- -----------------------------------------------------
  Game Engine            Unity                6000.5.2f1    Technische Grundlage des Prototyps

  Programmiersprache     C#                   9.0           Alle Skripte des Projekts

  Entwicklungsumgebung   Visual Studio 2026   V18.6.2       Programmierung und Debugging

  3D-Modellierung        Blender              5.1           Baummodelle und Gras-Meshes inkl. LOD-Stufen

  Versionsverwaltung     GitHub Desktop                     Absicherung und Versionierung des Projekts

  Dokumentation          Microsoft Word                     Dokumente wie das TDD

  Diagramme              Draw.io              Web-Version   UML-Klassendiagramme, FSM-Übersichten, Ablaufpläne

  Projektplanung         Instagantt           Web-Version   Zeitablaufplan

  Zeiterfassung          Grindstone           4             Erfassung der tatsächlichen Arbeitszeit

  KI-Assistenz           Claude               Aktuellste    Erklärungen, sprachliche Korrektur, Code-Kommentare

  KI-Assistenz           ChatGPT              Aktuellste    Erzeugung der Gras-Farbtextur
  ---------------------------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_1 .anchor}Tabelle Entwicklungsumgebung

**Kennzeichnung KI-gestützter Hilfsmittel:**

Bei der Erstellung dieser Arbeit wurden KI-Assistenten als Hilfsmittel eingesetzt; sie sind in Tabelle 1 als Bestandteil der Entwicklungsumgebung aufgeführt. Der Einsatz umfasst die Prüfung von Rechtschreibung und Grammatik in den Texten dieses Dokuments sowie in den Code-Kommentaren, das Erklären von Fachthemen, Fehlermeldungen und fremdem Quellcode während der Einarbeitung sowie die Erzeugung der Gras-Farbtextur. Die fachlichen Entscheidungen, der Entwurf der Systeme und deren Umsetzung liegen beim Verfasser.

# Projektziel:

Das Projekt verfolgt mehrere Ziele. Einerseits dient der *Isor's Tower Prototype* dazu, die technischen Anforderungen und Themen der einzelnen Semester praktisch umzusetzen und dadurch die jeweiligen Modulaufgaben zu erfüllen. Die im Semester behandelten Inhalte sollen nicht isoliert bearbeitet, sondern in ein zusammenhängendes Spielprojekt integriert werden.

Ein weiteres Ziel besteht darin, den Prototyp als langfristiges Lernprojekt zu nutzen. Durch die Arbeit an einem größeren Projekt sollen Erfahrungen im Umgang mit verschiedenen technischen Systemen, Abhängigkeiten, Architekturentscheidungen und Entwicklungsabläufen gesammelt werden. Dabei steht nicht nur die reine Funktionalität im Vordergrund, sondern auch ein besseres Verständnis für saubere Strukturierung, Wartbarkeit und Erweiterbarkeit.

Langfristig soll der Prototyp außerdem als Grundlage für ein größeres Portfolio-Projekt dienen. Er bietet eine technische Spielwiese, um Systeme zu testen, zu überarbeiten und weiterzuentwickeln, die später in einem umfangreicheren Spielprojekt verwendet werden könnten. Dadurch entsteht ein Projekt, das sowohl für die aktuellen Semesteraufgaben als auch für zukünftige Entwicklungsphasen und die persönliche Weiterentwicklung im Bereich Game Programming relevant ist.

# Anforderung und Features:

06.06.26

Das Projekt soll eine modulare und erweiterbare Grundlage für den *Isor's Tower Prototype* schaffen. Dabei sollen die technischen Anforderungen des 2. Semesters in einem zusammenhängenden Spielprojekt umgesetzt und dokumentiert werden. Gleichzeitig soll die Projektstruktur so aufgebaut sein, dass der Prototyp auch in späteren Semestern weiterverwendet, erweitert und überarbeitet werden kann.

## Allgemeine Anforderungen

06.06.26:

- Eine nachvollziehbare und dokumentierte Softwarearchitektur

- Eine modulare Trennung der einzelnen Systeme

- Eine erweiterbare Grundlage für spätere Semester

- Die Integration fremder Assets unter Berücksichtigung ihrer Lizenzen

- Eine technische Dokumentation mit UML-Klassendiagramm, Ablaufdiagramm und TDD für 2. Semester

- Engine-Tool-Entwicklung für 2. Semester

- Eine Threadoptimierung für 2. Semester

- Eine Softwareplanung für 2. Semester

- Eine simulierte Spielumgebung mit Shader- und Partikeleffekten

- Ein KI Prototyp für 2. Semester

- Eine prozedurale Erweiterung der Spielwelt für 2. Semester

- Eine Projektstruktur, die als Grundlage für ein späteres Portfolio-Projekt dienen kann

- Eine Projektstruktur, die für die private Weiterentwicklung geeignet ist

## Aktuelle Features des KI-Prototyps

Ein Schwerpunkt des aktuellen Entwicklungsstands ist der KI-Prototyp einer Schafherde. Die Schafe agieren als einzelne NPC-Einheiten innerhalb einer Gruppe und können abhängig von ihrer Umgebung zwischen verschiedenen Verhaltensmustern wechseln. Die Steuerung dieser Verhaltensmuster erfolgt über eine Finite State Machine.

06.06.26:

- Einzelne Schafe als NPC-Einheiten

- Zwei unterschiedliche Schaf-Typen

  - Commander

  - Normal

- Gruppenverhalten über eine Herdenstruktur

- Ein Herdenanker, der entweder durch den Commander oder durch den Mittelpunkt der lebenden Schafe bestimmt wird

- Verhaltenssteuerung über eine Finite State Machine (FSM)

- Feste Hauptzustände und temporäre Zwischenzustände:

  - Idle

  - Eating

  - HerdMoving

  - Regroup

  - Patrol

  - Sleeping

  - Flee

  - OnAlert

  - Dodge

  - FollowPlayer

  - Dead

- Wahrnehmung durch SheepSense-System

  - Spieler

  - Andere Schafe

  - Gegner beziehungsweise Bedrohungen

- Bewegung über NavMeshAgent mit SheepMoveBehaviour

- Hunger-System, durch das Schafe hungrig werden und verhungern können

- Health-System für Schaden, Tod und Wiederherstellung

- Despawn- und Respawn-Logik für Schafe

- Einfaches Dodge-Verhalten zum Ausweichen vor Hindernissen

- Day-Night-System mit Einfluss auf das Schlafverhalten der Schafe

- Follow-Verhalten für einzelne Schafe und Commander

- Herdenbewegung über den Commander und den HerdManager

- Anpassbare Werte über ScriptableObjects und Unity Inspector

- Debug- und Visualisierungsmöglichkeiten über Gizmos

- Testbarkeit über Gizmos und Scene View

07.08.26:

- Zähmen und Freilassen eines Schafs durch den Spieler

- Es kann immer nur ein Schaf gleichzeitig gezähmt sein, herdenübergreifend über ein gemeinsames ScriptableObject verwaltet

- Schlafende Schafe lassen sich nicht zähmen; ein bereits gezähmtes Schaf lässt sich dagegen jederzeit freilassen

- Das Zähmen wirkt sofort und holt das Schaf aus jedem laufenden Verhalten heraus

- Anbindung an das Interaktionssystem über ein gemeinsames Interface mit kontextabhängiger Textanzeige

- Herde und Ablageposition für tote Schafe werden beim Start übergeben, statt im Prefab als Szenenreferenz zu liegen

- Staubeffekt beim Fliehen über den VFX Graph

## Aktuelle Features der prozeduralen Weltgenerierung

Neben dem KI-Prototyp wurde die Spielwelt selbst prozedural aufgebaut. Das Terrain, die Wasserfläche und die Verteilung der Objekte darauf entstehen über eine mehrstufige Pipeline, die sich über ein gemeinsames Einstellungs-Asset steuern lässt.

07.08.26:

- Prozedural im Code erzeugtes Terrain-Mesh auf Basis von oktaviertem Perlin Noise

- Aufteilung in Chunks; Chunks je Kante und Vertices je Chunk sind einstellbar

- Deterministische Erzeugung über einen Seed, derselbe Seed liefert immer dasselbe Terrain

- Höhenkurve zum Umformen des Höhenprofils, um Täler abzusenken und Gipfel zu betonen

- Plateau für eine ebene Baufläche, einstellbar über Position, Radius, Übergangsbreite und Zielhöhe

- Globaler Wasserspiegel mit eigenem Material und einem kahlen Uferstreifen

- Objektplatzierung mit garantiertem Mindestabstand über eine Poisson-Disc-Verteilung

- Regeln je Objekttyp aus Höhenband, maximaler Steigung, Mindestabstand, Skalierungsbereich und Ausrichtung am Untergrund

- Dichtesteuerung über austauschbare Strategien: gleichmäßig, feste Wahrscheinlichkeit oder Noise-Maske

- Aussparen bebauter Flächen über eine Ausschlusskomponente am jeweiligen Objekt

- Eigener Platzierungs-Seed, getrennt vom Terrain-Seed, sodass sich die Verteilung ohne Terrain-Neubau neu würfeln lässt

- Zwei Darstellungswege je Objekttyp: einzelne GameObjects oder GPU-Instancing

- Zweistufiges LOD für Gras mit Auswahl je Zelle nach Kameraentfernung

- Platzierung der Objekte zur Laufzeit beim Szenenstart

## Aktuelle Features des Editor-Tools

Die Pipeline wird über ein eigenes Editor-Tool bedient. Es fasst die einzelnen Stufen in einem Fenster zusammen und verkürzt damit den Arbeitsablauf beim Aufbau der Spielwelt.

07.08.26:

- Eigenes Editor-Fenster, erreichbar über das Menü unter Tools, Isor Tower, Terrain Generator

- Aufbau nach dem MVP-Muster: die View zeichnet nur, der Presenter besitzt die erzeugten Szenenobjekte

- Konfiguration über ein austauschbares Einstellungs-Asset, wodurch mehrere Terrain-Presets möglich sind

- Vollständiger Durchlauf der Pipeline über einen einzelnen Knopf

- Einzelne Stufen getrennt aufrufbar, um Terrain zu erzeugen oder Objekte zu platzieren

- Pro Objekttyp eine eigene Zeile zum Platzieren und Löschen, die automatisch aus der Konfiguration erzeugt wird

- Löschen von Objekten und Terrain unabhängig voneinander

- Statuszeile als Rückmeldung an den Nutzer

- Fehlbedienung ausgeschlossen: alle Knöpfe, die eine Konfiguration benötigen, sind gesperrt, solange keine zugewiesen ist, zusätzlich erscheint ein Hinweisfeld

## Aktuelle Features der Spielerinteraktion

Der Spieler kann mit einzelnen Objekten der Spielwelt interagieren. Die Interaktion läuft über ein gemeinsames Interface, sodass die Spielerseite die einzelnen Objekte nicht kennen muss und neue interaktive Objekte ergänzt werden können, ohne den Spieler zu ändern.

07.08.26:

- First-Person-Steuerung über das Input System mit Bewegen, Umsehen und Interagieren

- Zielerfassung über einen Strahl aus der Kameramitte, begrenzt durch eine Reichweite und einen Ebenenfilter

- Gemeinsames Interface für alle interaktiven Objekte, sodass die Spielerseite kein einzelnes Objekt kennen muss

- Anzeige des möglichen Vorgangs als Text, passend zum aktuellen Zustand des anvisierten Objekts

- Umgesetzte Interaktionen: Fackeln an- und ausschalten sowie Schafe zähmen und freilassen, wobei das Zähmen oben beim KI-Prototyp beschrieben ist

- Fackel als eigenständige Fähigkeit mit Flammeneffekt und Licht, die vom Spieler und vom Tag-Nacht-System gemeinsam genutzt wird

- Drei Betriebsarten je Fackel: dem Tag-Nacht-Wechsel folgen, oder unabhängig davon angezündet beziehungsweise gelöscht starten

- Fackeln, die dem Tag-Nacht-Wechsel folgen, melden sich beim Ereignisverwalter des Tag-Nacht-Systems an und brennen abends und nachts von selbst

# Zeitablaufplan/ Modulweiterentwicklung:

In [Abbildung 1](#_Ref_Abb_1) und [Abbildung 2](#_Ref_Abb_2) ist der grobe Zeitablauf des Projekts für das 2. Semester dargestellt. Der Zeitplan zeigt die einzelnen Modulaufgaben sowie deren geplante Bearbeitungsphasen. Dazu gehören unter anderem Planung, Umsetzung, Testen, Verbessern und Dokumentieren.

Die Aufgaben wurden so eingeteilt, dass die verfügbare Zeit bis zur jeweiligen Deadline möglichst sinnvoll genutzt wird. Gleichzeitig wurden Puffer eingeplant, um auf unerwartete Probleme, technische Schwierigkeiten oder zusätzlichen Arbeitsaufwand reagieren zu können. Falls einzelne Aufgaben mehr Zeit in Anspruch nehmen als ursprünglich geplant, kann die Arbeitszeit an bestimmten Tagen erhöht oder die Priorität weniger wichtiger Zusatzaufgaben angepasst werden.

Da der *Isor's Tower Prototype* im Verlauf des Semesters schrittweise erweitert wird, dient der Zeitablaufplan nicht nur als organisatorische Übersicht, sondern auch als Grundlage für die Weiterentwicklung des TDD. Neue Systeme, Änderungen und Erweiterungen werden nach den jeweiligen Modulabschnitten ergänzt und dokumentiert.

![[]{#_Ref_Abb_1 .anchor}Abbildung Zeitplan Teil 1](TDD_Media/media/image2.png){width="6.3in" height="4.443059930008749in"}

![[]{#_Ref_Abb_2 .anchor}Abbildung Zeitplan Teil 2](TDD_Media/media/image3.png){width="6.3in" height="4.491669947506562in"}

## KI Prototyp Sheep

22.05.26

Die Zeiterfassung zu Beginn des Projekts ist durch einen Datenverlust nicht mehr vollständig vorhanden. Der ursprüngliche Projektstand befand sich auf einem Laptop, der aufgrund eines technischen Defekts zur Reparatur eingeschickt werden musste. Da zu diesem Zeitpunkt keine zusätzliche externe Sicherung der Projektdaten vorhanden war, konnten frühere Zeitdaten und Teile des ursprünglichen Projektstands nicht vollständig übernommen werden.

Aus diesem Vorfall wurde das weitere Vorgehen angepasst. Projektdaten werden nun zusätzlich gesichert, um zukünftige Datenverluste zu vermeiden. Außerdem wird für die weitere Zeiterfassung die Tracking-Software Grindstone verwendet. Die dort erfassten Daten dienen als Grundlage für zukünftige Zeitpläne und eine genauere Auswertung der tatsächlichen Arbeitszeit.

In [Tabelle 2](#_Ref_Tab_2) ist der aktuelle Detailzeitplan des KI-Prototyps dargestellt. Die Tabelle enthält die einzelnen Arbeitsschritte, die geschätzte Zeit, die tatsächliche Zeit sowie Start- und Enddatum. Die frühe Projektphase vor dem Datenverlust wurde zusammengefasst dargestellt, da sie nicht mehr vollständig im Detail rekonstruiert werden kann.

Ein großer Teil der frühen Projektzeit wurde für Recherche und Einarbeitung verwendet. Schätzungsweise 60 bis 70 Prozent der Arbeitszeit vor dem Datenverlust entfielen auf das Lernen und Recherchieren von Themen wie Finite State Machines, NavMesh, KI-Architektur, Komponentenstruktur und weiteren Grundlagen, die für die spätere Umsetzung benötigt wurden.

  -------------------------------------------------------------------------------------------
           Aufgabe           Geschätzte Zeit   Tatsächliche Zeit   Startdatum     EndDatum
  ------------------------- ----------------- ------------------- ------------- -------------
   Zeit bevor Datenverlust         80h               100h           10.04.26      22.05.26

   Sheep Health Refactored         1h                 2h            22.05.26      22.05.26

          Sheep FSM                10h               14,5h          23.05.26      24.05.26

         FSM Testing               2h                2.5h           25.05.26      25.05.26

           Prefab                  0,5                0,5           29.05.26      29.05.26

        MoveBehaviour              4h                 7h            30.05.26      30.05.26

       DodgeBehaviour              5h                11.5h          31.05.26      04.06.26

         Refactoren                4h                 7h            04.06.26      05.06.26

          Animation                2h                 5h            05.06.26      05.06.26

        Dokumentation              10h                              06.06.26    

           Extras                  3h                                           
  -------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_2 .anchor}Tabelle Zeitplan KI Prototyp

## Simulation der Spieleumgebung

12.07.26

Durch den Laptop-Defekt und den damit verbundenen Datenverlust (siehe 5.1) hat sich der ursprüngliche Zeitplan für das gesamte Semester verschoben. Für die Simulation der Spielumgebung wurde deshalb ein neues Gesamtbudget von 120 Stunden angesetzt, mit dem Ziel, den entstandenen Zeitverzug möglichst auszugleichen.

Bei der Schätzung wurde zwischen Shadern und VFX unterschieden siehe [Tabelle 3](#_Ref_Tab_3). Der MoonShader wurde mit 10 Stunden veranschlagt, da er im Vergleich zu den anderen Shadern einfacher aufgebaut ist. StylizedWaterShader, GrassAlphaShader und GrassMeshShader wurden dagegen mit jeweils rund 20 Stunden eingeplant, da sie zusätzlich Bewegungs- und Interaktionsfunktionen besitzen und nicht nur auf einfacher Texturmaskierung basieren.

Die VFX-Effekte wurden allgemein kürzer eingeschätzt, da hier stärker experimentell und nach Gefühl gearbeitet werden kann. FireFly wurde als erster VFX-Effekt mit 10 Stunden angesetzt. SheepRun und Smoke wurden danach kürzer eingeschätzt, da durch FireFly bereits Grundwissen im Umgang mit der VFX Graph vorhanden war. Für Torch wurde wieder mehr Zeit eingeplant, 20 Stunden, da der Effekt aus mindestens zwei bis drei einzelnen Partikelsystemen besteht.

Die geschätzte Zeit wurde insgesamt eingehalten, die tatsächliche Fertigstellung lag sogar etwas darunter. Erschwerend wirkten sich wiederholte Engine-Abstürze aus, wodurch zusätzliche Zeit für das erneute Aufsetzen des Arbeitsstands verloren ging. Trotz dieser Unterbrechungen konnte das Zeitbudget eingehalten werden, sodass die Gesamtbewertung dieser Modulphase positiv ausfällt.

Bei der Qualität der einzelnen Shader und VFX-Effekte gab es mehrere kleinere Probleme, für die im Verlauf jeweils eigene Lösungen gefunden wurden. Der MoonShader ist gut gelungen. Beim StylizedPondWaterShader besteht noch Optimierungsbedarf bei der Bewegungsrichtung der UV-Koordinaten: Aktuell muss die Richtung noch manuell angepasst werden, damit beim Kombinieren mehrerer Wasserflächen keine sichtbaren Übergänge beziehungsweise Backface-Artefakte zwischen einzelnen Planes entstehen. Für den aktuellen Prototypenstand reicht die Qualität aus, für eine spätere Weiterverwendung wäre eine flexiblere Lösung sinnvoll, die mit einer einzelnen Plane auskommt. Beide Grasshader funktionieren zuverlässig, hier könnten LOD-Stufen ergänzt und die Schattierung noch etwas reduziert werden. FireFly, SheepRun, Smoke und Torch funktionieren wie vorgesehen, ließen sich aber je nach Platzierung im Level noch gezielter anpassen, insbesondere bei der Wahl zwischen den unterschiedlich teuren Ausrichtungsoptionen (Face Camera Plane/Position) im Output-Block.

Die Dokumentation hat etwas mehr Zeit in Anspruch genommen als ursprünglich geplant. Der Mehraufwand entstand durch die Automatisierung der Kapitelnummerierung und Gliederung sowie durch eine insgesamt sauberere Strukturierung des Dokuments.

+----------------+-----------------+-------------------+------------+------------+
| Aufgabe        | Geschätzte Zeit | Tatsächliche Zeit | Startdatum | EndDatum   |
+:==============:+:===============:+:=================:+:==========:+:==========:+
| Shader         | 10h             | 5h 32 min         | 10.06.26   | 15.06.26   |
|                |                 |                   |            |            |
| Moon           |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| Shader         | 22h             | 15h 29 min        | 15.06.26   | 18.06.26   |
|                |                 |                   |            |            |
| Stylized Water |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| Shader         | 20h             | 20h 26 min        | 18.06.26   | 23.06.26   |
|                |                 |                   |            |            |
| Grass Alpha    |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| Shader         | 20h             | 12h 58 min        | 23.06.26   | 29.06.26   |
|                |                 |                   |            |            |
| Grass Mesh     |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| VFX            | 10h             | 4h 57 min         | 01.07.26   | 05.07.26   |
|                |                 |                   |            |            |
| Firefly        |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| VFX            | 5h              | 2h 33 min         | 11.07.26   | 11.07.26   |
|                |                 |                   |            |            |
| SheepRun       |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| VFX            | 5h              | 2h                | 11.07.26   | 11.07.26   |
|                |                 |                   |            |            |
| Smoke          |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| VFX            | 20h             | 14h 49 min        | 08.07.26   | 11.07.26   |
|                |                 |                   |            |            |
| Torch          |                 |                   |            |            |
+----------------+-----------------+-------------------+------------+------------+
| Recherche      | 2h              | 8h 10 min         | 10.06.26   | 12.07.26   |
+----------------+-----------------+-------------------+------------+------------+
| Dokumentation  | 6h              | 16h 15 min        | 12.07.26   | 12.07.26   |
+----------------+-----------------+-------------------+------------+------------+
| Gesamt         | 120h            | 98h 9min          | 10.06.26   | 12.07.26   |
+----------------+-----------------+-------------------+------------+------------+

: []{#_Ref_Tab_3 .anchor}Tabelle Zeitplan Simulation der Spieleumgebung

## Prozedurale Erweiterung der Spielwelt und Engine-Tool

07.08.26

Für die folgenden Module wurde keine Zeitschätzung mehr vorgenommen. Der ursprüngliche Plan aus [Abbildung 1](#_Ref_Abb_1) und [Abbildung 2](#_Ref_Abb_2) hatte sich durch den Datenverlust ohnehin verschoben, und unter dem wachsenden Zeitdruck sowie mangels Erfahrung mit dem Umfang der neuen Themen wurde auf eine erneute Schätzung verzichtet. Die folgenden Tabellen führen deshalb nur die tatsächlich erfasste Zeit.

Außerdem wurde die Zeit ab diesem Modul tageweise erfasst statt für jeden einzelnen Arbeitsschritt. Die Tabellen enthalten daher eine Zeile pro Arbeitstag mit der Angabe, was an diesem Tag entstanden ist. Das gilt auch für die folgenden Abschnitte.

Die prozedurale Erweiterung der Spielwelt und die Engine-Tool-Entwicklung sind hier zusammengefasst, weil beide Aufgaben ineinandergreifen. Das Tool ist die Bedienoberfläche der Generierungs-Pipeline, und beide sind nebeneinander entstanden: Jede neue Stufe der Pipeline hat unmittelbar ihre Bedienung im Tool bekommen. Eine getrennte Zeiterfassung wäre nachträglich konstruiert.

Die erfassten Werte sind als Untergrenze zu verstehen. Sowohl für dieses Modul als auch für die Threadoptimierung wurden zusätzlich in der Freizeit Tutorials und Fachbeiträge durchgearbeitet, die nicht mit erfasst wurden.

Ein Teil der Arbeit an der prozeduralen Generierung ist im folgenden Abschnitt erfasst: Am 04. und 05.08.2026 entstanden das Gras-Rendering und die Platzierung zur Laufzeit. Diese rund zehn Stunden stehen in [Tabelle 5](#_Ref_Tab_5), gehören fachlich aber zu diesem Modul.

  ---------------------------------------------------------------------------------------------------------------------
                                 Aufgabe                                 Tatsächliche Zeit   Startdatum     EndDatum
  --------------------------------------------------------------------- ------------------- ------------- -------------
                     Einarbeitung und erste Schritte                         2h 00min         17.07.26      17.07.26

   MeshBuilder, HeightmapGenerator, TerrainConfig und Engine-Tool V0.1       11h 29min        18.07.26      18.07.26

                  PlateauModifier und Umbau auf Chunks                       7h 04min         19.07.26      19.07.26

                Wasserspiegel und nahtlose Chunk-Normalen                    3h 51min         20.07.26      20.07.26

                     Entwurf der Platzierungs-Stufe                          0h 29min         21.07.26      21.07.26

                  Placeables-Struktur und ObjectPlacer                       7h 31min         23.07.26      23.07.26

                   DensityStrategy als Strategy-Muster                       2h 39min         25.07.26      25.07.26

                  Ausbau des Tool-Panels und Baum-Asset                      2h 38min         26.07.26      26.07.26

                                  Summe                                      37h 41min        17.07.26      26.07.26
  ---------------------------------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_4 .anchor}Tabelle Zeitplan prozedurale Erweiterung der Spielwelt und Engine-Tool

## Weiterentwicklung des Prototyps

07.08.26

Unter diesem Arbeitsbereich wurde alles erfasst, was am Prototyp selbst weiterentwickelt wurde und keinem einzelnen Modul eindeutig zuzuordnen ist. Dazu gehören der Aufbau der Haupt- und der Menü-Szene, das Interaktionssystem mit der Fackel, der Feinschliff am Schaf-Prototyp sowie das Gras-Rendering und die Platzierung zur Laufzeit.

  --------------------------------------------------------------------------------------------------------------
                             Aufgabe                              Tatsächliche Zeit   Startdatum     EndDatum
  -------------------------------------------------------------- ------------------- ------------- -------------
                 Aufbau von Haupt- und Menü-Szene                     4h 57min         27.07.26      27.07.26

   Interaktionssystem, Fackel, Pausenmenü und Schaf-Feinschliff       9h 33min         02.08.26      02.08.26

      Refactoring der Schaf-Skripte, FSM und Herdenbewegung           3h 05min         03.08.26      03.08.26

            Gras-Rendering per GPU-Instancing und LOD                 8h 04min         04.08.26      04.08.26

         PlacementExclusion und Platzierung zur Laufzeit              1h 45min         05.08.26      05.08.26

                              Summe                                   27h 24min        27.07.26      05.08.26
  --------------------------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_5 .anchor}Tabelle Zeitplan Weiterentwicklung des Prototyps

## Threadoptimierung

07.08.26

Die Threadoptimierung wurde an einem Tag in einem Durchgang bearbeitet. Sie umfasst die Baseline-Messung, drei aufeinander aufbauende Optimierungsschritte und die abschließende Messreihe. Die Einarbeitung in das Thema fand außerhalb der Zeiterfassung statt.

  ------------------------------------------------------------------------------------------------
                      Aufgabe                       Tatsächliche Zeit   Startdatum     EndDatum
  ------------------------------------------------ ------------------- ------------- -------------
   Messreihe und Parallelisierung der Platzierung       9h 56min         05.08.26      05.08.26

  ------------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_6 .anchor}Tabelle Zeitplan Threadoptimierung

## Softwareplanung und Dokumentation

07.08.26

Unter der Softwareplanung ist die Arbeit an der Dokumentation erfasst, insbesondere am vorliegenden TDD und an den Werkzeugen für die Diagramme. Dieser Wert wächst bis zur Abgabe weiter und wird deshalb nur als Gesamtzeit geführt.

  -----------------------------------------------------------------------------------
                Aufgabe                Tatsächliche Zeit   Startdatum     EndDatum
  ----------------------------------- ------------------- ------------- -------------
   Softwareplanung und Dokumentation          51h           06.08.26      11.08.26

  -----------------------------------------------------------------------------------

  : []{#_Ref_Tab_7 .anchor}Tabelle Zeitplan Softwareplanung und Dokumentation

#  Architekturübersicht:

## DayNightSystem:

22.05.26, überarbeitet 08.08.26

Das Day-Night-System ist dafür zuständig, der Spielwelt einen Tages- und Nachtrhythmus zu geben. Dadurch kann die Spielwelt zeitabhängig reagieren und später lebendiger wirken. Das System unterscheidet verschiedene Tagesphasen wie Morning, Afternoon, Evening und Night. Diese Tagesphasen können von anderen Systemen genutzt werden, um ihr Verhalten abhängig von der aktuellen Ingame-Zeit anzupassen. Das Day-Night-System besteht aus mehreren Komponenten und einem Interface.

### IngameTime

Die zentrale Grundlage bildet die Komponente IngameTime. Sie verwaltet die aktuelle Ingame-Zeit und stellt diese in Tagen, Stunden, Minuten und Sekunden dar. Die einzelnen Zeiteinheiten können definiert und gesetzt werden. Intern zählt das System die verstrichene Zeit hoch und wandelt sie anschließend in die entsprechenden Zeiteinheiten um. IngameTime wird als Singleton Pattern umgesetzt, da es innerhalb der Spielwelt nur eine zentrale Ingame-Zeit geben soll.

Die Umrechnungsraten sind dabei nicht fest vorgegeben: Wie viele Sekunden eine Minute, wie viele Minuten eine Stunde und wie viele Stunden einen Tag ergeben, lässt sich im Inspector einstellen. Ergänzt wird das durch einen Zeitraffer und die Möglichkeit, im Inspector direkt eine Uhrzeit zu setzen. Beides dient dem Testen zeitabhängiger Systeme, ohne einen ganzen Tagesverlauf abwarten zu müssen.

### DayNightCycle

Die Komponente DayNightCycle besitzt eine Referenz auf die aktive IngameTime-Instanz. Sie berechnet zum einen den normalisierten Tagesfortschritt von 0 bis 1, der für die visuelle Darstellung benötigt wird. Zum anderen bestimmt sie anhand der aktuellen Ingame-Stunde die aktive Tagesphase, indem sie diese mit den festgelegten Startstunden vergleicht. Die Startstunden für Morning, Afternoon, Evening und Night sind im Inspector einstellbar. Zusätzlich existiert der Wert None, der eine noch nicht bestimmte Tagesphase kennzeichnet und verhindert, dass ein Listener beim Anmelden einen ungültigen Wert erhält. Wenn sich die aktuelle Tagesphase ändert, löst DayNightCycle ein Event aus und übergibt dabei die vorherige und die neue Phase.

### DayNightCycleEventManager

Der DayNightCycleEventManager dient als zentrale Vermittlungsstelle zwischen dem DayNightCycle und allen Systemen, die auf Tageszeitänderungen reagieren sollen. Dafür wird das Observer Pattern verwendet. Der EventManager ist beim DayNightCycle angemeldet und empfängt dessen Signal, sobald sich die Tagesphase ändert. Andere Objekte können sich beim EventManager registrieren oder wieder abmelden, um Benachrichtigungen über Tageszeitänderungen zu erhalten.

Beim Anmelden erhält ein Listener die aktuell aktive Tagesphase sofort mitgeteilt, sofern bereits eine gültige Phase bestimmt wurde. Andernfalls würde ein Objekt, das während einer laufenden Phase erzeugt wird, bis zum nächsten Phasenwechsel im falschen Zustand bleiben. Zusätzlich entfernt der EventManager beim Verteilen der Ereignisse Einträge, deren Objekt nicht mehr existiert.

### IDayNightListener

Für diese Kommunikation wird das Interface IDayNightListener verwendet. Jede Klasse, die dieses Interface implementiert, kann auf Tagesphasenwechsel reagieren. Dadurch müssen die einzelnen Listener nicht direkt mit dem DayNightCycle verbunden sein. Das reduziert direkte Abhängigkeiten und macht das System leichter erweiterbar.

Aktuell implementieren die Schafe und die Fackeln dieses Interface. Die Schafe schalten dadurch ihr Schlafverhalten um, die Fackeln entzünden sich abends und erlöschen am Morgen.

### SkyController

Der SkyController ist für die visuelle Darstellung des Tagesverlaufs zuständig. Er verwendet den aktuellen Tagesfortschritt des DayNightCycle, um einen Celestial Pivot zu rotieren. Über diesen Pivot können Objekte wie Sonne oder Mond abhängig von der aktuellen Tageszeit bewegt werden. Dadurch entsteht eine sichtbare Verbindung zwischen der technischen Ingame-Zeit und der visuellen Darstellung der Spielwelt.

## KI ProtoTyp Sheep

06.06.26, überarbeitet 08.08.26

Der KI-Prototyp ist komponentenbasiert aufgebaut. Die einzelnen Systeme übernehmen klar getrennte Verantwortlichkeiten, während die zentrale Sheep-Komponente als Zugriffspunkt für die FSM dient. Dadurch bleiben Wahrnehmung, Bewegung, Gesundheit, Hunger, Ausweichen und Herdenlogik voneinander getrennt und können später erweitert oder ausgetauscht werden. Der KI-Prototyp für die Schafe bildet das zentrale NPC-System des aktuellen Projektstands. Das System besteht aus mehreren spezialisierten Komponenten, die über die zentrale Sheep-Klasse miteinander verbunden werden. Die Sheep-Klasse dient dabei als Controller beziehungsweise Knotenpunkt für die einzelnen Subsysteme und ermöglicht der Finite State Machine den Zugriff auf relevante Daten und Funktionen.

Die wichtigsten Komponenten des Sheep-Systems sind:

- Sheep

- SheepFSM

- SheepDodgeBehaviour

- SheepHealth

- SheepHunger

- SheepMoveBehaviour

- SheepSense

- HerdManager

- SheepSettings

- SheepStateSettings

- SheepInteractable

- TamedSheepReference

- DodgeBehaviourBase

- SheepAnimatorParameters

Die Verhaltenssteuerung erfolgt über eine Finite State Machine. Für die einzelnen Verhalten existieren eigene State-Klassen, welche die jeweiligen Zustandslogiken und Transitions enthalten. Zu diesen States gehören:

- DeadState

- DodgeState

- EatingState

- FleeState

- FollowPlayerState

- HerdMovingState

- IdleState

- OnAlertState

- PatrolState

- RegroupState

- SleepingState

Alle State-Klassen erben von der gemeinsamen Basisklasse SheepStateBase. Dadurch besitzen sie eine einheitliche Grundstruktur mit den Methoden Enter, Tick und Exit. Zusätzlich werden über ScriptableObjects anpassbare Werte für allgemeine Schafeinstellungen und statebezogene Einstellungen bereitgestellt.

### Sheep

Die Sheep-Komponente ist der Controller beziehungsweise Knotenpunkt, an dem alle Systeme zusammenlaufen. Sie hält die Referenzen auf Gesundheit, Hunger, Wahrnehmung, Bewegung, Ausweichverhalten und die Finite State Machine. Dadurch benötigen die States nur eine einzige Schnittstelle, um an alle Daten zu gelangen, und einzelne Systeme lassen sich später leichter austauschen.

Darüber hinaus übernimmt sie die Aufgaben, die den gesamten Lebenszyklus eines Schafs betreffen: Sie registriert alle States einmalig bei der FSM, reagiert auf die Ereignisse für Schaden und Verhungern, behandelt Tod und Respawn und steuert den Staubeffekt beim Fliehen. Über das Interface IDayNightListener reagiert sie zusätzlich auf den Tageswechsel und markiert das Schaf nachts als schlafend.

Herde und Ablageposition für tote Tiere erhält das Schaf beim Start vom HerdManager übergeben, statt sie selbst als Referenz zu halten. Nur dadurch bleibt eine Herde ein frei platzierbares Prefab. Ebenfalls beim Start wird die Ausweichpriorität des NavMeshAgent gesetzt: Der Commander erhält die höchste Priorität, damit er als Herdenanker nicht zur Seite geschoben wird, die übrigen Schafe erhalten gestreute Werte, damit sie sich nicht gegenseitig blockieren.

### SheepHealth

Die Komponente SheepHealth verwaltet das Lebenssystem eines Schafs. Sie speichert die aktuellen und maximalen Lebenspunkte und ermöglicht es, Schaden zu erhalten oder Lebenspunkte wiederherzustellen. Zusätzlich implementiert sie das Interface IDamageable, wodurch das System später auch auf andere Entitäten übertragen werden kann.

Bei erhaltenem Schaden kann ein Event ausgelöst werden. Wenn die Lebenspunkte auf null fallen, wird ein Sterbe-Event ausgelöst. Dadurch können andere Systeme, zum Beispiel die FSM, auf den Tod des Schafs reagieren. Für den Respawn steht außerdem eine Methode zur vollständigen Wiederherstellung der Lebenspunkte zur Verfügung.

Das Sterbe-Ereignis wird nur einmal ausgelöst, auch wenn ein bereits totes Schaf weiteren Schaden erhält. Erst die vollständige Wiederherstellung beim Respawn gibt das Ereignis wieder frei.

### SheepHunger

Die Komponente SheepHunger verwaltet das Hungersystem eines Schafs. Über einen zeitbasierten Tick steigt der Hungerwert des Schafs regelmäßig an. Wird ein bestimmter Grenzwert überschritten, gilt das Schaf als hungrig. Erreicht der Hunger den Maximalwert, kann Starvation-Schaden ausgelöst werden.

Das System kann außerdem erkennen, ob das Schaf gerade frisst, ob es satt ist und ob Hunger aktuell aktiv sein soll. Dadurch kann der Hunger zum Beispiel während des Schlafens pausiert werden. Die Komponente wurde so aufgebaut, dass sie später auch für andere Entitäten erweitert oder wiederverwendet werden könnte.

### SheepSense

SheepSense ist die Wahrnehmungskomponente des Schafs. Sie erkennt über OverlapSphere-Abfragen relevante Objekte in der Umgebung. Dazu gehören der Spieler, andere Schafe, Commander-Schafe und Bedrohungen.

Die Erkennung erfolgt über einstellbare Radien und LayerMasks. Dadurch kann im Inspector definiert werden, welche Objekte erkannt werden sollen und in welchem Bereich die Wahrnehmung stattfindet. Zusätzlich erkennt das System, ob sich der Spieler zu nah am Schaf befindet und dadurch eine Fluchtreaktion ausgelöst werden kann.

Für den Spieler werden dabei zwei Distanzen unterschieden: eine Fluchtdistanz, ab der das Schaf den Spieler als zu nah empfindet, und eine kürzere Zähmdistanz, innerhalb derer der Spieler das Schaf zähmen kann. Alle Radien und LayerMasks stammen aus den SheepSettings; zum Testen lassen sich die Werte über einen Schalter lokal am Objekt überschreiben, ohne das gemeinsame Asset zu verändern.

### SheepMoveBehaviour

SheepMoveBehaviour steuert die Bewegung des Schafs über den NavMeshAgent. Diese Komponente enthält Methoden zum Bewegen zu Zielpositionen, Stoppen der Bewegung, Folgen eines Ziels, Fliehen vor einer Bedrohung und Prüfen, ob ein Ziel erreicht wurde.

Für verschiedene Verhalten können unterschiedliche Bewegungswerte verwendet werden, zum Beispiel normales Gehen, Fluchtbewegung oder Herdenbewegung. Außerdem werden Zielpositionen vor der Bewegung auf dem NavMesh geprüft, damit nur erreichbare Positionen verwendet werden. Viele Werte sind im Inspector einstellbar und können dadurch flexibel angepasst werden.

Die drei Bewegungsprofile für Gehen, Herdenbewegung und Flucht unterscheiden sich nicht nur in Geschwindigkeit, Beschleunigung und Drehgeschwindigkeit, sondern auch im Anhalteabstand: Bei der Herdenbewegung ist er bewusst klein gewählt, damit die Schafe ihre Formationsposition genau einnehmen.

Die Fluchtposition wird nicht einfach in die Gegenrichtung gesetzt, sondern gesucht. Dabei werden bis zu hundert zufällige Kandidaten geprüft. Ein Kandidat wird nur angenommen, wenn er auf dem NavMesh liegt, weit genug entfernt ist, den Abstand zur Bedrohung tatsächlich vergrößert und über einen vollständigen Pfad erreichbar ist. Ein seitlicher Zufallsversatz sorgt dafür, dass das Schaf nicht schnurgerade von der Bedrohung wegläuft.

### SheepDodgeBehaviour

SheepDodgeBehaviour ist eine Komponente für ein einfaches Ausweichverhalten. Das System soll verhindern, dass Schafe zu stark ineinanderschieben oder an Hindernissen hängen bleiben. Die Erkennung erfolgt über einstellbare Raycasts.

SheepDodgeBehaviour erbt von der abstrakten Basisklasse DodgeBehaviourBase, die nur vorgibt, wann ein Ausweichen nötig ist, ob gerade ausgewichen wird und wie es gestartet wird. Dadurch könnten später andere Entitäten ein eigenes Ausweichverhalten mitbringen, ohne dass die States geändert werden müssen. Die Raycasts sind als Liste konfigurierbar, jeweils mit Richtung, Reichweite und LayerMask; ein Cooldown verhindert, dass unmittelbar erneut ausgewichen wird.

Wenn ein Hindernis erkannt wird, berechnet das Schaf eine seitliche Ausweichrichtung. Die Richtung wird abhängig davon gewählt, auf welcher Seite sich das Hindernis befindet. Anschließend wird ein gültiger Dodge-Zielpunkt auf dem NavMesh gesucht und der NavMeshAgent bewegt das Schaf kurzzeitig dorthin.

Das Dodge-System ist bewusst einfach gehalten und dient aktuell als prototypische Zusatzfunktion. Es kann später durch ein komplexeres Steering- oder Avoidance-System erweitert werden.

### SheepFSM

SheepFSM ist die Finite State Machine des KI-Prototyps. Sie verwaltet den aktuell aktiven State und ermöglicht den Wechsel zwischen registrierten States.

Die States werden einmalig registriert und anschließend wiederverwendet. Dadurch müssen sie nicht bei jedem Zustandswechsel neu erstellt werden. Die FSM verwendet generische Methoden, um States typbasiert abzurufen und zu wechseln. Dadurch bleibt das System erweiterbar und kann später um zusätzliche States ergänzt werden.

Jeder State besitzt die Methoden Enter, Tick und Exit. Enter wird beim Betreten eines States ausgeführt, Tick läuft während des aktiven States und Exit wird beim Verlassen des States aufgerufen. Zusätzlich kann die FSM prüfen, welcher State aktuell aktiv ist. Das wird unter anderem für Übergänge und Rückkehrlogik benötigt.

### DeadState

DeadState beschreibt den Zustand, in dem ein Schaf tot ist. In diesem State werden Timer verwendet, um eine Verzögerung für die Todesanimation und die spätere Respawn-Zeit zu steuern.

Nach Ablauf der Despawn-Zeit wird die eigentliche Todesbehandlung ausgeführt. Nach Ablauf der Spawn-Zeit wird der Respawn-Prozess gestartet. Zusätzlich wird aktuell ein Animator-Bool gesetzt, um die Todesanimation zu steuern.

Der Animationsparameter wird beim Betreten gesetzt und beim Verlassen wieder zurückgenommen. Die Parameternamen liegen zentral in SheepAnimatorParameters, damit sie nicht als Zeichenketten über die States verteilt sind.

### DodgeState

DodgeState ist ein temporärer Zwischenzustand. Er wird verwendet, wenn das Schaf kurzzeitig ausweichen soll und danach zu seinem vorherigen Verhalten zurückkehren muss.

Dafür speichert der State eine Referenz auf den vorherigen State sowie das vorherige Bewegungsziel. Wenn der vorherige State das Interface IResumeTargetState implementiert, kann das gespeicherte Ziel nach dem Dodge wieder aufgenommen werden. Dadurch kann ein Schaf zum Beispiel während einer Patrouille ausweichen und anschließend seine ursprüngliche Bewegung fortsetzen.

Betreten wird der State nicht von einem einzelnen Verhalten aus, sondern über die gemeinsame Hilfsmethode der Basisklasse, die das Rückkehrziel vorher setzt.

### EatingState

EatingState beschreibt den Zustand, in dem ein Schaf frisst. Beim Betreten des States wird im Hungersystem gesetzt, dass das Schaf aktuell isst. Dadurch wird der Hungerwert über das SheepHunger-System reduziert.

Der State besitzt mehrere Transitions. Erkennt das Schaf eine Bedrohung, wechselt es in den Alert-Zustand. Wenn das Schaf schlafen soll, wechselt es in den Sleeping-Zustand. Sobald das Schaf satt ist, wechselt es zurück in den Patrol-Zustand.

### FleeState

FleeState ist dafür zuständig, dass ein Schaf vor einem Ziel flieht. Dieses Ziel wird als Transform gespeichert und kann zum Beispiel ein Gegner oder der Spieler sein.

Beim Betreten des States wird das Movement auf Fluchtbewegung umgestellt. Anschließend berechnet SheepMoveBehaviour eine geeignete Position, die vom Ziel wegführt. Über einen Timer kann regelmäßig geprüft werden, ob eine neue Fluchtposition benötigt wird. Wenn das Schaf sein Ziel erreicht hat und keine Gefahr mehr erkannt wird, wechselt es in den Regroup-Zustand.

### FollowPlayerState

FollowPlayerState beschreibt das Verhalten eines gezähmten Schafs, das dem Spieler folgt. Dabei unterscheidet sich das Verhalten abhängig davon, ob es sich um ein normales Schaf oder ein Commander-Schaf handelt.

Ein normales Schaf kann dem Spieler direkt folgen. Ein Commander-Schaf kann zusätzlich die Herdenbewegung auslösen, indem es über den HerdManager die normalen Schafe in die Herdenbewegung versetzt. Die Steuerung erfolgt über den Tamed-Zustand des Schafs und über ein Herdenbewegungs-Flag.

Der Eintritt in diesen State bildet die einzige Ausnahme im sonst zustandsseitig geprüften Aufbau: Beim Zähmen wird der Wechsel von außen angestoßen, statt darauf zu warten, dass ein State das Tamed-Flag von sich aus bemerkt. Nur PatrolState und OnAlertState prüfen dieses Flag; ein fressendes oder schlafendes Schaf hätte sonst erst beim nächsten Verhaltenswechsel reagiert, und der Spieler würde auf seinen eigenen Tastendruck warten. Das Freilassen benötigt diesen Eingriff nicht, weil FollowPlayerState seine Abbruchbedingung ohnehin in jedem Frame prüft.

### HerdMovingState

HerdMovingState wird verwendet, wenn sich die Schafe als Teil einer Herde bewegen. Für normale Schafe werden dabei spezielle Bewegungswerte gesetzt. Anschließend wird über den HerdManager eine Formationsposition berechnet, die das Schaf ansteuert.

Die Formationsposition orientiert sich am Herdenanker. Wenn ein Commander vorhanden und aktiv ist, wird die Formation hinter beziehungsweise um den Commander herum aufgebaut. Dadurch entsteht ein künstliches Folgen in Formation.

### IdleState

IdleState ist ein grundlegender Zustand, in dem das Schaf wartet und keine aktive Bewegung ausführt. Der State dient häufig als Startpunkt oder Zwischenzustand.

Ein Timer bestimmt, wie lange das Schaf im Idle-Zustand bleibt. Währenddessen prüft der State, ob äußere Einflüsse auftreten, zum Beispiel eine Bedrohung, ein Spieler in der Nähe, Hunger oder Schlafbedarf. Abhängig von diesen Bedingungen kann in andere States gewechselt werden.

### OnAlertState

OnAlertState ist ein Zwischenzustand, in dem das Schaf aufmerksam wird und seine Umgebung bewertet. Der State besitzt einen Reaktionstimer, wodurch eine kurze Verzögerung simuliert wird, bevor das Schaf auf eine Situation reagiert.

In diesem Zustand wird geprüft, ob eine Bedrohung vorhanden ist, ob der Spieler zu nah ist oder ob ein gezähmtes Schaf dem Spieler folgen soll. Abhängig von der Situation wechselt das Schaf in den FleeState, FollowPlayerState oder zurück in ein normales Verhalten.

### PatrolState

PatrolState beschreibt ein normales Bewegungsverhalten, bei dem sich das Schaf zufällig innerhalb des Herdenradius bewegt. Die Zielposition wird über den HerdManager erzeugt und anschließend durch SheepMoveBehaviour auf dem NavMesh validiert.

Dieser State kann durch verschiedene Einflüsse unterbrochen werden, zum Beispiel durch Bedrohungen, Hunger, Schlaf, Player-Nähe oder Dodge. Da ein Schaf während des Patrouillierens ausweichen und anschließend sein altes Ziel wieder aufnehmen können soll, implementiert PatrolState das Interface IResumeTargetState.

### RegroupState

RegroupState sorgt dafür, dass sich ein Schaf wieder zur Herde einordnet. Der State verwendet den Herdenanker des HerdManager, um eine passende Zielposition zu bestimmen.

Wenn die Herde nicht aktiv in Bewegung ist, sucht sich das Schaf eine zufällige Regroup-Position innerhalb eines definierten Radius. Wenn die Herde aktiv bewegt wird, versucht das Schaf stattdessen eine Formationsposition einzunehmen. Genau wie PatrolState implementiert auch RegroupState das Interface IResumeTargetState, damit ein Dodge unterbrochen und anschließend fortgesetzt werden kann.

### SleepingState

SleepingState simuliert das Schlafverhalten eines Schafs. Beim Betreten dieses States stoppt das Schaf seine Bewegung und das Hungersystem wird pausiert. Das Schaf bleibt in diesem Zustand, solange es als schlafend markiert ist.

Sobald die Schlafbedingung nicht mehr erfüllt ist, wechselt das Schaf zurück in ein normales Verhalten. Dadurch kann das Day-Night-System Einfluss auf das Verhalten der Schafe nehmen.

### SheepStateBase

SheepStateBase ist die Basisklasse aller Sheep-States. Sie stellt die Grundstruktur für die einzelnen Zustände bereit und speichert Referenzen auf das gesteuerte Sheep, die zugehörige SheepFSM und die SheepStateSettings.

Alle konkreten States erben von dieser Basisklasse und können die Methoden Enter, Tick und Exit überschreiben. Dadurch besitzen alle States eine einheitliche Struktur, bleiben aber in ihrer jeweiligen Logik voneinander getrennt.

Neben den Lebenszyklus-Methoden stellt SheepStateBase eine gemeinsame Hilfsmethode für das Ausweichen bereit. Sie prüft, ob das Ausweichverhalten ein Hindernis meldet, merkt sich den gerade aktiven State als Rückkehrziel und wechselt anschließend in den DodgeState. Dadurch existiert die Ausweichlogik nur einmal, statt in jedem bewegenden State wiederholt zu werden, und ein neuer State erhält sie durch die Vererbung automatisch.

Eine Bedingung sitzt bewusst vor der Prüfung: Ein Schaf, das seine Zielposition bereits erreicht hat, weicht nicht mehr aus. Andernfalls würden dicht beieinanderstehende Schafe dauerhaft gegenseitig Ausweichmanöver auslösen.

### HerdManager

Der HerdManager ist für die Verwaltung der Herdenlogik zuständig. Er speichert die zugehörigen Schafe einer Herde, verwaltet den Commander und berechnet zentrale Positionen, die für Gruppenbewegung, Regrouping, Patrouillen und Respawn verwendet werden.

Eine wichtige Aufgabe des HerdManager ist die Berechnung des Herdenankers. Wenn ein lebender und gezähmter Commander vorhanden ist, wird dessen Position als Mittelpunkt der Herde verwendet. Falls kein gültiger Commander vorhanden ist, wird stattdessen der Mittelpunkt der lebenden Schafe berechnet. Dadurch bleibt die Herde auch ohne aktiven Commander funktionsfähig.

Zusätzlich stellt der HerdManager Positionen für verschiedene Verhaltensweisen bereit. Dazu gehören zufällige Patrouillenpositionen, Regroup-Positionen, Spawn-Positionen und Formationspositionen für die Herdenbewegung. Bei der Herdenbewegung erhalten normale Schafe individuelle Offset-Positionen, damit sie sich um den Herdenanker beziehungsweise hinter dem Commander einordnen können.

Der HerdManager trennt damit die Gruppenlogik von den einzelnen Schaf-States. Die States müssen nicht selbst berechnen, wo sich die Herde befindet oder welche Position ein Schaf innerhalb der Formation einnehmen soll, sondern können diese Informationen vom HerdManager anfordern. Dadurch bleibt die Herdenlogik zentral verwaltet und später leichter erweiterbar.

Beim Start übergibt der HerdManager jedem Mitglied die Herde und die Ablageposition für tote Tiere. Dadurch braucht kein Schaf eine eigene Referenz in die Szene, und eine komplette Herde bleibt als Prefab frei platzierbar.

## Prozedurale Weltgenerierung

### Überblick der Pipeline

Die prozedurale Weltgenerierung ist in mehrere Stufen unterteilt, die nacheinander durchlaufen werden und jeweils eine klar abgegrenzte Aufgabe übernehmen. Die Kette beginnt bei der TerrainConfig und führt über den HeightmapGenerator, den PlateauModifier und den MeshBuilder zum ObjectPlacer und schließlich zum Gras-Rendering. Jede Stufe arbeitet dabei nur mit den Daten, die ihre Vorgängerstufe erzeugt hat, und gibt ihr Ergebnis an die nächste Stufe weiter.

Die Aufteilung hat den Zweck, dass jede Stufe für sich verständlich und austauschbar bleibt. Dadurch kann eine einzelne Stufe geändert oder erweitert werden, ohne dass die übrigen Teile der Pipeline angepasst werden müssen. Gleichzeitig fasst keine dieser Stufen die Szene selbst an: Sie berechnen ausschließlich Daten, und erst das Editor-Tool erzeugt daraus die Objekte in der Szene.

Der gesamte Ablauf ist deterministisch. Grundlage dafür ist ein Seed: Solange der Seed gleich bleibt, erzeugt die Pipeline bei jedem Durchlauf dasselbe Ergebnis. Im aktuellen Projektstand werden zwei getrennte Seeds verwendet, einer für das Gelände und einer für die Platzierung der Objekte. Dadurch kann die Verteilung der Objekte neu gewürfelt werden, ohne dass das Gelände neu berechnet werden muss.

### TerrainConfig

Die TerrainConfig ist ein ScriptableObject und dient als zentrale Einstellungsdatei der Weltgenerierung. Alle Stufen der Pipeline lesen ihre Werte aus diesem Asset, sodass es für die Parameter nur eine Quelle gibt. Die Werte selbst werden ausschließlich im Inspector gesetzt; aus dem Code wird die Config nur gelesen. Da die Einstellungen in einem Asset liegen, können mehrere Configs nebeneinander bestehen und als austauschbare Presets verwendet werden, ohne dass dafür Code geändert werden muss.

Die Einstellungen sind in sechs Gruppen unterteilt: Chunks, Noise, Plateau, Mesh, Water und Placement. Jede Gruppe gehört zu einer Stufe der Pipeline, sodass die Werte dort zu finden sind, wo sie auch wirken. Eine vollständige Auflistung aller Felder ist an dieser Stelle nicht sinnvoll; die jeweils relevanten Parameter werden in den folgenden Abschnitten bei der zugehörigen Stufe genannt.

Für die Eingabefelder sind Guards gesetzt, die verhindern, dass ein Wert in einen Bereich gerät, in dem die Berechnung kein sinnvolles Ergebnis liefert oder fehlschlägt. Dazu gehören Mindestwerte für Größen, die als Divisor verwendet werden, und feste Wertebereiche für Angaben, die nur innerhalb bestimmter Grenzen definiert sind. Eine fehlerhafte Eingabe fällt dadurch nicht erst zur Laufzeit auf, sondern ist im Inspector von vornherein nicht möglich.

Zusätzlich prüft die Config bei jeder Änderung, ob die Höhe des Plateaus auf oder unter dem Wasserspiegel liegt, und gibt in diesem Fall eine Warnung aus. Diese Kombination wäre technisch gültig, würde das Dorf aber unter Wasser setzen. Der Fall lässt sich nicht über einen festen Wertebereich ausschließen, weil er von zwei unabhängigen Feldern gleichzeitig abhängt.

### HeightmapGenerator

Der HeightmapGenerator berechnet die Höhen des Geländes. Er ist als statische Klasse aufgebaut und hält keinen eigenen Zustand, sodass jede Stufe der Pipeline ihn aufrufen kann. Über seine eigentliche Aufgabe hinaus dient er als Schnittstelle: Er beantwortet die Frage, welche Höhe das Gelände an einer bestimmten Weltposition hat, und wird deshalb nicht nur beim Aufbau des Meshes verwendet, sondern auch von der Platzierung der Objekte.

Die Klasse stellt drei öffentliche Methoden bereit. Generate erzeugt die Heightmap für einen einzelnen Chunk. BuildOctaveOffsets erzeugt die Verschiebungen, mit denen der Seed auf das Rauschen wirkt. SampleHeight berechnet die Höhe an einem einzelnen Weltpunkt und wird sowohl von Generate als auch von den späteren Stufen aufgerufen.

Generate arbeitet chunkweise. Aus der in der Config hinterlegten Chunk-Auflösung wird ein quadratisches Array angelegt, anschließend werden die Oktaven-Verschiebungen einmal aufgebaut und danach für jeden Punkt des Gitters die zugehörige Weltposition berechnet. Für diese Position liefert SampleHeight den Höhenwert, der in das Array geschrieben wird. Das fertige Array wird zurückgegeben und danach nicht mehr verändert.

Die Umrechnung von Gitterpunkt auf Weltposition ist dabei entscheidend für die Nahtlosigkeit. Das Rauschen wird ausschließlich nach der Weltposition abgefragt und nie nach dem lokalen Index innerhalb eines Chunks. Zwei benachbarte Chunks fragen an ihrer gemeinsamen Kante deshalb dieselbe Koordinate ab und erhalten denselben Wert. Die Naht in der Geometrie entsteht dadurch gar nicht erst und muss nicht nachträglich geschlossen werden.

BuildOctaveOffsets ist notwendig, weil die von Unity bereitgestellte Perlin-Noise-Funktion keinen Seed kennt. Dieselben Koordinaten liefern immer denselben Wert, das Rauschen selbst lässt sich also nicht verändern. Verändern lässt sich nur, an welcher Stelle es abgefragt wird. Aus dem Seed wird daher über einen Zufallsgenerator je Oktave eine eigene Verschiebung erzeugt. Die Verschiebungen sind für das gesamte Gelände gleich und werden einmal gebaut und anschließend als Parameter weitergereicht; würden sie pro Punkt neu gezogen, läge jeder Punkt in einem anderen Rauschfeld.

SampleHeight berechnet die Höhe in vier Schritten. Zunächst werden mehrere Schichten des Rauschens übereinandergelegt. Jede Schicht erhält über die Persistence eine kleinere Amplitude und über die Lacunarity eine höhere Frequenz, wodurch die feineren Schichten nur noch Details beitragen. Im zweiten Schritt wird die Summe durch die Summe aller verwendeten Amplituden geteilt. Diese Normalisierung ist der Grund dafür, dass das Ergebnis unabhängig von der Anzahl der Oktaven im Bereich zwischen 0 und 1 bleibt: Werden weitere Schichten ergänzt, wächst der Detailgrad, aber nicht die Höhe.

Im dritten Schritt wird das Ergebnis über die HeightCurve umgeformt. Damit lässt sich einstellen, wie sich die Höhen über den Wertebereich verteilen, ohne das Rauschen selbst zu ändern; eine nach unten gebogene Kurve senkt beispielsweise die Täler ab und lässt die Gipfel stehen. Anschließend wird der Wert auf den Bereich 0 bis 1 begrenzt. Diese Begrenzung ist notwendig, weil eine AnimationCurve zwischen zwei Stützpunkten über ihren Zielbereich hinausschwingen kann und ein solcher Wert das Gelände sonst unter die Grundfläche ziehen würde. Gelesen wird dabei nicht die Kurve selbst, sondern eine daraus abgetastete Tabelle; die Begründung dafür steht im Abschnitt zur Threadoptimierung.

Im vierten Schritt wird das Plateau über die Methode SampleAt des PlateauModifier aufgesetzt. Die Berechnung des Plateaus bleibt damit in der zuständigen Klasse, während SampleHeight lediglich die Reihenfolge der Schritte vorgibt. Der Aufbau folgt damit derselben Linie wie die übrige Pipeline: Jede Klasse behält ihre eigene Aufgabe, und geteilt wird über genau einen Einstiegspunkt.

Generate liefert nicht genau so viele Werte, wie der Chunk Gitterpunkte hat, sondern eine Reihe mehr an jeder Seite. Dieser Rand wird nicht vermascht, sondern enthält die Höhen der angrenzenden Chunks. Der MeshBuilder benötigt diese Nachbarwerte, um die Normalen an den Chunk-Kanten berechnen zu können; wofür das erforderlich ist, wird im folgenden Abschnitt beschrieben.

Eine Einschränkung betrifft die Größe der Oktaven-Verschiebungen. Sie sind im aktuellen Stand auf einen Bereich von plus oder minus 10.000 begrenzt. Der Grund liegt in der Genauigkeit von Gleitkommazahlen: Bei Koordinaten um 100.000 beträgt der kleinste noch unterscheidbare Abstand etwa 0,008, während der Abstand zweier benachbarter Abfragen bei der eingestellten Auflösung nur rund 0,004 beträgt. Zwei benachbarte Punkte würden dann auf denselben Wert gerundet, was im Gelände als Terrassenbildung sichtbar wird. Bei einem Bereich von 10.000 liegt der kleinste unterscheidbare Abstand bei etwa 0,001 und damit deutlich unter dem Abfrageabstand.

### PlateauModifier

Der PlateauModifier erzeugt eine ebene Fläche im Gelände, auf der das Village aufgebaut werden kann. Ohne diese Stufe würde das Rauschen auch dort Hügel erzeugen, wo später Gebäude, Wege und begehbarer Boden liegen sollen. Die Klasse ist statisch und hält keinen Zustand; sie wird über die Methode SampleAt aus dem HeightmapGenerator aufgerufen.

SampleAt arbeitet punktweise und verändert kein Array. Die Methode erhält die bisherige Höhe eines Punktes sowie dessen Weltposition und gibt die Höhe zurück, die nach dem Plateau gilt. Dadurch kann dieselbe Berechnung sowohl beim Aufbau des Geländes als auch bei der späteren Platzierung von Objekten verwendet werden, ohne dass eine der beiden Stufen eine eigene Fassung benötigt.

Für die Abstandsmessung wird die Weltposition zunächst auf den Bereich 0 bis 1 normiert, indem sie durch die Kantenlänge des Geländes geteilt wird. Mittelpunkt und Radius des Plateaus sind dadurch unabhängig von der eingestellten Weltgröße: Wird die Karte vergrößert, liegt das Plateau weiterhin an derselben anteiligen Stelle. Der Abstand zum Mittelpunkt wird anschließend als Abstand zweier Punkte in dieser normierten Ebene berechnet.

Aus diesem Abstand ergeben sich drei Fälle. Liegt der Punkt innerhalb des Radius, wird die eingestellte Plateauhöhe zurückgegeben. Dabei handelt es sich nicht um eine Schwelle, sondern um eine Zielhöhe: Der vorherige Wert wird vollständig ersetzt, sodass die Fläche unabhängig vom darunterliegenden Rauschen eben ist. Liegt der Punkt im Ring zwischen Radius und Radius zuzüglich der eingestellten Blendbreite, wird zwischen Plateauhöhe und ursprünglicher Höhe interpoliert. Außerhalb dieses Rings bleibt die Höhe unverändert.

Für die Interpolation im Ring wird die Position im Ring zunächst auf einen Wert zwischen 0 und 1 umgerechnet und anschließend über eine SmoothStep-Funktion geführt. Eine rein lineare Interpolation würde zwar ebenfalls einen Übergang erzeugen, an den beiden Enden des Rings aber einen sichtbaren Knick hinterlassen, weil die Steigung dort abrupt wechselt. Die Richtung der Interpolation ist dabei festgelegt: Am inneren Rand des Rings gilt die volle Plateauhöhe, am äußeren Rand das ursprüngliche Gelände.

Ein Radius von 0 schaltet die Stufe vollständig ab; die Methode gibt die übergebene Höhe dann unverändert zurück. Auf ein zusätzliches Schaltfeld wurde bewusst verzichtet, da ein Plateau ohne Ausdehnung ohnehin keine Wirkung hätte und ein zweites Feld denselben Zustand doppelt abbilden würde.

Im aktuellen Projektstand ist ein Radius von 0,035 und eine Blendbreite von 0,05 eingestellt. Bezogen auf die Kantenlänge von 2.048 Metern entspricht das einer ebenen Fläche mit rund 72 Metern Radius und einem Übergangsring von rund 102 Metern Breite. Der Übergang ist damit breiter als die ebene Fläche selbst, wodurch das Plateau nicht als abgesetztes Podest wirkt, sondern flach in das umliegende Gelände ausläuft. Die Plateauhöhe liegt bei 0,15 und damit bei rund 105 Metern, also oberhalb des eingestellten Wasserspiegels.

### MeshBuilder

Der MeshBuilder übersetzt die berechneten Höhen in ein Mesh und ist die einzige Klasse der Pipeline, die die Mesh-Schnittstelle von Unity verwendet. Alle vorherigen Stufen arbeiten ausschließlich mit Zahlen; erst hier entsteht eine Geometrie, die gezeichnet werden kann. Die Klasse besitzt eine einzige öffentliche Methode und hält keinen Zustand.

Die Methode erhält drei Angaben. Die Heightmap liefert die Höhenwerte, die Kantenlänge in Metern legt fest, wie groß das Mesh in Weltkoordinaten wird, und der Höhenmultiplikator rechnet die normierten Werte in Meter um. Der Multiplikator ist dabei ausschließlich für diese Umrechnung zuständig. Die Verteilung der Höhen wurde bereits im HeightmapGenerator über die HeightCurve festgelegt, sodass die Werte hier nur noch skaliert und nicht mehr umgeformt werden.

Die übergebene Heightmap ist um einen Rand von einem Vertex größer als das Gitter, das vermascht werden soll. Die Methode zieht diesen Rand zu Beginn ab und arbeitet anschließend nur mit dem inneren Gitter. Beim Zugriff auf die Höhen wird der Index um den Rand versetzt, sodass die Randwerte gelesen, aber nie vermascht werden.

Aus der Auflösung ergeben sich die Größen der beiden Datenfelder. Die Anzahl der Vertices entspricht der Auflösung im Quadrat. Die Anzahl der Dreiecksindizes ergibt sich aus der um eins verringerten Auflösung im Quadrat, multipliziert mit sechs. Die Verringerung um eins folgt daraus, dass zwischen einer Anzahl von Punkten stets ein Feld weniger liegt als Punkte vorhanden sind; bei 129 Punkten je Kante entstehen also 128 Felder. Der Faktor sechs ergibt sich daraus, dass jedes Feld aus zwei Dreiecken mit je drei Indizes aufgebaut wird. Die Position eines Punktes im eindimensionalen Feld wird über Zeile mal Auflösung zuzüglich Spalte bestimmt, der Abstand zweier benachbarter Punkte über die Kantenlänge geteilt durch die um eins verringerte Auflösung.

Die Reihenfolge der drei Indizes eines Dreiecks ist nicht beliebig. Sie wird so gewählt, dass die Dreiecke von oben betrachtet im Uhrzeigersinn verlaufen, weil Unity daran die Vorderseite einer Fläche erkennt. Bei umgekehrter Reihenfolge zeigen die Flächen nach unten und werden durch das Backface Culling nicht gezeichnet, wodurch das Gelände von oben unsichtbar wäre.

Die Normalen werden nicht von Unity berechnen lassen, sondern selbst aus den Höhen abgeleitet. Für jeden Punkt werden die Höhen der vier angrenzenden Punkte herangezogen und daraus über eine zentrale Differenz die Flächenneigung bestimmt. In der senkrechten Komponente steht dabei die doppelte Punktdistanz, da nicht der Punkt selbst mit seinem Nachbarn verglichen wird, sondern der linke Nachbar mit dem rechten. Zwischen diesen beiden liegen zwei Felder, und nur wenn diese Strecke in der Rechnung steht, stimmen waagerechte und senkrechte Einheit überein und der Neigungswinkel wird korrekt.

Der Grund für die eigene Berechnung liegt in den Grenzen zwischen den Chunks. Die von Unity bereitgestellte Berechnung kennt jeweils nur das Mesh, zu dem sie gehört, und berücksichtigt die Höhen des Nachbarn nicht. An der gemeinsamen Kante zweier Chunks entstünden dadurch unterschiedliche Normalen und damit eine sichtbare Naht in der Beleuchtung. Durch den zusätzlichen Rand stehen die Höhen des Nachbarn zur Verfügung, sodass beide Chunks an ihrer gemeinsamen Kante dasselbe Ergebnis berechnen. Diese Naht ist von der Naht in der Geometrie zu unterscheiden, die bereits dadurch ausgeschlossen wird, dass das Rauschen nach der Weltposition abgefragt wird.

Die Aufteilung des Geländes in Chunks ergibt sich aus einer technischen Grenze. Ein Mesh verwendet standardmäßig einen 16 Bit breiten Indexpuffer und kann damit höchstens 65.535 Vertices adressieren, was einem Gitter von etwa 255 mal 255 Punkten entspricht. Bei einer Kantenlänge von 2.048 Metern in einem einzelnen Mesh läge der Punktabstand damit bei rund acht Metern und das Gelände wäre zu grob. Im aktuellen Projektstand wird die Welt daher in 8 mal 8 Chunks mit je 129 Punkten je Kante unterteilt. Daraus ergeben sich 16.641 Vertices und 32.768 Dreiecke je Chunk sowie rund 1,05 Millionen Vertices und 2,1 Millionen Dreiecke für das gesamte Gelände bei einem Punktabstand von zwei Metern. Die Aufteilung dient dabei nicht nur der Einhaltung der Grenze, sondern ermöglicht zugleich, dass nicht sichtbare Teile des Geländes vom Zeichnen ausgenommen werden können.

### ObjectPlacer

Der ObjectPlacer bestimmt, an welchen Positionen Objekte in der Welt stehen. Er ist als statische Stufe aufgebaut und damit ein Gegenstück zum MeshBuilder: Er liest das Gelände, erzeugt aber selbst keine Objekte in der Szene. Das Ergebnis ist eine Liste von Positionsangaben, aus der erst das Editor-Tool tatsächliche Objekte erzeugt. Dadurch bleibt die Berechnung unabhängig davon, wer sie später verwendet, und kann sowohl im Editor als auch zur Laufzeit aufgerufen werden.

Die Stufe arbeitet mit zwei Datentypen. Ein Placeable beschreibt als Vorlage, was platziert werden soll und unter welchen Bedingungen: das Prefab, der zulässige Höhenbereich, die maximale Steigung, der Mindestabstand, der Skalierungsbereich, die Ausrichtung am Boden sowie die gewählte Dichteverteilung. Ein Placement ist das Ergebnis für ein einzelnes Objekt und besteht aus Prefab, Position, Rotation und Skalierung. Das Placeable ist als Klasse umgesetzt, weil es im Inspector bearbeitet und dort serialisiert werden muss. Das Placement ist dagegen als Struktur umgesetzt und nach der Erzeugung nicht mehr veränderbar, da hiervon mehrere Millionen Exemplare entstehen und jede zusätzliche Referenz entsprechend ins Gewicht fiele.

Nach außen stellt die Klasse ausschließlich die Methode Place bereit, die einen einzelnen Objekttyp verarbeitet; alle weiteren Methoden sind privat. Place legt die Ergebnisliste an, prüft die übergebenen Angaben, erzeugt die Oktaven-Verschiebungen über den HeightmapGenerator und übergibt an die eigentliche Verarbeitung. Zusätzlich gibt die Methode Messwerte zurück, die im Rahmen der Threadoptimierung ausgewertet werden. Für die Zufallswerte wird ein eigener Seed verwendet, der unabhängig vom Seed des Geländes ist. Dadurch lässt sich die Verteilung der Objekte neu bestimmen, ohne dass sich das Gelände verändert.

Die Verteilung der Punkte erfolgt über ein Poisson-Disc-Verfahren nach Bridson. Ziel des Verfahrens ist eine zufällige Verteilung, bei der dennoch ein Mindestabstand zwischen zwei Punkten garantiert ist. Rein zufällig gesetzte Punkte bilden sichtbare Klumpen und Lücken, während ein regelmäßiges Raster als künstlich erkennbar bleibt. Das Verfahren arbeitet mit einer Liste aktiver Punkte. Aus dieser Liste wird ein zufälliger Punkt ausgewählt, um den herum bis zu dreißig Kandidaten in einem Ring zwischen dem einfachen und dem doppelten Mindestabstand erzeugt werden. Der erste gültige Kandidat wird übernommen und selbst in die Liste aufgenommen. Ist keiner der Versuche erfolgreich, gilt der Punkt als umschlossen und wird aus der Liste entfernt. Der Vorgang endet, wenn die Liste leer ist.

Die Prüfung, ob ein Kandidat gültig ist, besteht darin, seinen Abstand zu den bereits gesetzten Punkten zu messen. Da dieser Vergleich bei mehreren Millionen Punkten nicht gegen alle bisherigen Punkte durchgeführt werden kann, wird ein Hilfsgitter verwendet. Dieses Gitter trifft selbst keine Entscheidung, sondern dient allein dazu, die in Frage kommenden Nachbarn schnell zu finden. Seine Zellenkante entspricht dem Mindestabstand geteilt durch die Wurzel aus zwei, wodurch die Diagonale einer Zelle genau dem Mindestabstand entspricht. Damit kann in jeder Zelle höchstens ein Punkt liegen, und eine Zelle muss nur einen einzigen Verweis speichern. Aus derselben Eigenschaft folgt, dass ein zu naher Punkt höchstens zwei Zellen entfernt liegen kann; geprüft wird deshalb nur der Block von fünf mal fünf Zellen um den Kandidaten. Der Aufwand wächst dadurch linear statt quadratisch mit der Anzahl der Punkte.

Die so erzeugten Punkte durchlaufen anschließend mehrere Regeln, die festlegen, wo ein Objekt stehen darf. Geprüft wird zuerst der Wasserstand, sofern Wasser aktiviert ist, danach der zulässige Höhenbereich des jeweiligen Typs, anschließend die Dichteverteilung und zuletzt die Steigung des Untergrunds. Die Reihenfolge ist bewusst gewählt: Die Steigung ist die aufwendigste Prüfung, da sie über vier zusätzliche Höhenabfragen ermittelt werden muss. Jeder Punkt, der bereits vorher ausscheidet, erspart diese Rechnung vollständig.

Für die verbleibenden Punkte werden Rotation und Skalierung bestimmt. Die Drehung um die Hochachse ist immer zufällig. Ist für den Typ die Ausrichtung am Boden aktiviert, wird zusätzlich die Neigung des Untergrunds übernommen. Die Reihenfolge beider Drehungen ist dabei nicht beliebig, da die Multiplikation von Quaternionen nicht vertauschbar ist: Die Neigung muss zuletzt angewendet werden, weil andernfalls die zufällige Drehung die Achse verschieben würde, an der sich die Neigung ausrichtet. Die Skalierung wird zwischen einem Mindest- und einem Höchstwert zufällig gewählt.

Die Steuerung der Dichte ist über das Strategy-Muster umgesetzt und bildet neben dem MVC-Aufbau des Editor-Tools das zweite bewusst eingesetzte Entwurfsmuster des Projekts. Eine abstrakte Basisklasse gibt lediglich vor, dass zu einer Position eine Annahmewahrscheinlichkeit zurückgegeben wird. Der ObjectPlacer kennt ausschließlich diese Basis und keine der konkreten Umsetzungen. Im aktuellen Stand bestehen drei Varianten: eine gleichmäßige Verteilung, eine Verteilung über eine feste Wahrscheinlichkeit und eine Verteilung über eine Rauschmaske, mit der sich dichte und kahle Bereiche erzeugen lassen. Eine weitere Art der Verteilung erfordert damit lediglich ein zusätzliches Asset, während der ObjectPlacer unverändert bleibt. Dass ein Wahrscheinlichkeitswert und kein einfacher Ja-Nein-Wert zurückgegeben wird, ist notwendig, um Abstufungen zu ermöglichen; die Zufallsentscheidung selbst bleibt an einer einzigen Stelle im Placer und damit reproduzierbar.

Die Wahl des Verfahrens ist bewusst getroffen und mit Kosten verbunden. Ein Poisson-Disc-Verfahren ist deutlich aufwendiger als ein Raster mit zufälliger Verschiebung der einzelnen Positionen, das dasselbe Ergebnis mit einem Bruchteil der Rechenzeit erzeugen würde. Ein solches Raster bleibt jedoch bei größeren Abständen als Struktur erkennbar, was insbesondere bei Bäumen auffällt. Für die Grasverteilung, bei der die Abstände sehr klein sind, wäre dieser Einwand voraussichtlich weniger gewichtig; eine erneute Bewertung des Verfahrens ist deshalb für die Weiterentwicklung nach der Abgabe vorgesehen. Der hohe Aufwand des Verfahrens ist zugleich der Ausgangspunkt der Threadoptimierung, die in einem eigenen Abschnitt beschrieben wird.

### Gras-Rendering

Das Gras wird nicht als GameObject in die Szene gestellt, sondern über einen eigenen Weg gezeichnet. Der ursprüngliche Ansatz, jedes Grasbüschel als einzelnes Objekt zu instanziieren, erwies sich als nicht tragfähig: Jedes GameObject bringt mindestens eine Transform-Komponente mit und wird zusätzlich in der Hierarchie, in der Serialisierung und in der Rücknahmeverwaltung des Editors geführt. Bereits bei rund 211.000 Objekten wurde der Editor unbrauchbar langsam. Da die Anzahl quadratisch mit dem verringerten Abstand wächst, war dieser Weg für eine flächendeckende Bepflanzung ausgeschlossen. Im aktuellen Stand stehen rund 7,4 Millionen Grasobjekte auf der Karte.

Als erster Schritt wurde die Darstellung auf GPU-Instancing umgestellt. Dabei wird nicht jedes Objekt einzeln übergeben, sondern eine Liste von Transformationsmatrizen, aus der die Grafikkarte dasselbe Mesh mehrfach zeichnet. Die Zahl der Zeichenaufrufe sank dadurch deutlich, im Vergleichsfall von 770 auf 138 Aufrufe. Die Bildrate verbesserte sich dennoch nicht, sondern lag bei etwa 4,5 Bildern je Sekunde. Die Ursache lag nicht bei den Zeichenaufrufen, sondern bei der Geometrie: Bei rund 190.000 Büscheln mit jeweils etwa 2.664 Dreiecken ergaben sich über 500 Millionen Dreiecke je Bild. Die Optimierung war damit zwar wirksam, betraf aber nicht den tatsächlichen Engpass.

Als zweiter Schritt wurde deshalb ein Wechsel der Detailstufe eingeführt. Neben dem ursprünglichen Mesh wurde ein vereinfachtes Mesh mit deutlich weniger Dreiecken erstellt und je nach Entfernung zur Kamera das eine oder das andere gezeichnet. Die Zahl der Dreiecke sank dadurch auf etwa 12 Millionen und die Bildrate stieg auf über 87 Bilder je Sekunde. Daraus ergibt sich eine übertragbare Erkenntnis: Bei Massenobjekten bestimmt in erster Linie die Gesamtzahl der Dreiecke die Leistung, nicht die Zahl der Zeichenaufrufe. Zudem multiplizieren sich zwei Einstellwerte, die getrennt voneinander unauffällig wirken, nämlich die Anzahl der Halme je Modell und die Anzahl der Modelle in der Welt.

Das Gras-Rendering ist in vier Teile gegliedert, die demselben Schnitt folgen wie die Platzierung: Einstellwerte, Datenaufbereitung, Entscheidung und Ausführung sind getrennt. Das GrassRenderProfile enthält ausschließlich Einstellwerte und liegt als Komponente am Gras-Prefab. Der GrassCellBuilder bereitet die Daten auf. Der GrassLodSelector entscheidet über die Detailstufe. Der InstancedRenderer zeichnet, trifft aber keine Entscheidung. Dadurch können die Regeln für die Detailstufe später erweitert werden, etwa um einen Übergang zwischen den Stufen, ohne dass der zeichnende Teil angepasst werden muss.

Das GrassRenderProfile hält vier Werte: das vereinfachte Mesh für größere Entfernungen, die Entfernung, ab der auf dieses Mesh gewechselt wird, die Entfernung, ab der überhaupt nicht mehr gezeichnet wird, und die Kantenlänge einer Zelle. Die Werte liegen bewusst am Prefab und nicht in der TerrainConfig, damit sie dort bearbeitet werden, wo auch das Gras selbst definiert ist. Im aktuellen Stand betragen sie 60 Meter, 250 Meter und 32 Meter.

Der GrassCellBuilder überführt die flache Liste der Platzierungen in ein Zellgitter. Jede Platzierung wird anhand ihrer Position einer quadratischen Zelle zugeordnet, und für jede belegte Zelle entsteht ein Eintrag mit zwei Angaben: den Transformationsmatrizen der enthaltenen Objekte und einem umschließenden Quader. Dieser Quader ist nicht mit der Zellgröße identisch, sondern wird aus den tatsächlich enthaltenen Positionen aufgebaut und anschließend um die Höhe eines Halms erweitert. Ohne diese Erweiterung reichte der Quader nur bis zur Bodenhöhe, wodurch die oberen Teile der Halme bei der Sichtbarkeitsprüfung verworfen würden. Bei der Bildung der Matrizen werden Skalierung und Drehung des Prefabs mit denen der Platzierung verrechnet und nicht durch sie ersetzt. Im aktuellen Stand entstehen auf diese Weise 3.139 Zellen.

Dass hierfür ein eigenes Gitter verwendet wird und nicht die bereits vorhandene Aufteilung in Chunks, hat einen sachlichen Grund. Beide Gitter folgen unterschiedlichen Grenzen: Die Chunk-Größe richtet sich nach der zulässigen Anzahl von Vertices je Mesh, während sich die Zellgröße nach der Anzahl der Instanzen je Zeichenaufruf und nach der gewünschten Genauigkeit der Sichtbarkeitsprüfung richtet. Eine gemeinsame Größe müsste beiden Anforderungen gleichzeitig genügen und wäre für keine der beiden geeignet. Kleinere Zellen erlauben dabei eine genauere Prüfung, erhöhen aber die Zahl der Zeichenaufrufe.

Der GrassLodSelector ist bewusst klein gehalten. Er erhält den Quader einer Zelle, die Kameraposition und das Profil und gibt zurück, ob die Zelle gar nicht, mit dem vereinfachten oder mit dem detaillierten Mesh gezeichnet wird. Der Vergleich erfolgt über quadrierte Entfernungen auf beiden Seiten, wodurch je Zelle eine Wurzelberechnung entfällt. Die von Unity bereitgestellte LODGroup war für diesen Zweck nicht verwendbar, da sie Renderer-Komponenten an einzelnen Objekten voraussetzt, die hier gerade nicht vorhanden sind.

Der InstancedRenderer ist die einzige Komponente dieses Teils, die in der Szene liegt. Gespeichert werden lediglich ein Verweis auf die TerrainConfig sowie der Index des Objekttyps; die Matrizen selbst werden nicht abgelegt, sondern beim Aktivieren aus dem Seed neu berechnet. Dabei wird zuerst der ObjectPlacer aufgerufen, anschließend werden über den PlacementExclusionFilter diejenigen Platzierungen entfernt, die innerhalb einer ausgenommenen Fläche liegen, und zuletzt baut der GrassCellBuilder daraus die Zellen. An dieser Stelle werden auch die Zeiten der einzelnen Schritte gemessen und ausgegeben; die Auswertung erfolgt im Abschnitt zur Threadoptimierung. Über eine einstellbare Anzahl von Wiederholungen lassen sich mehrere Messwerte in einem Durchlauf erzeugen, wobei stets mindestens ein Durchlauf stattfindet.

Das eigentliche Zeichnen erfolgt in jedem Bild erneut, da der verwendete Aufruf nur für ein einzelnes Bild gilt. Für jede Zelle wird die Detailstufe bestimmt und der Quader als Prüfbereich übergeben; Zellen außerhalb der Zeichenentfernung werden übersprungen. Da je Aufruf höchstens 1.023 Instanzen übergeben werden können, werden die Matrizen einer Zelle in Abschnitten dieser Größe durchlaufen, sodass jeder Aufruf voll ausgelastet wird und nur der letzte den Rest übernimmt. Der Schattenwurf ist für das Gras abgeschaltet, was Rechenzeit spart und zugleich verhindert, dass der Boden bei dieser Objektdichte vollständig verschattet wird. Die Komponente ist so eingerichtet, dass sie auch außerhalb des Spielbetriebs arbeitet, damit das Gras bereits im Editor sichtbar ist. Voraussetzung für das Verfahren ist, dass am verwendeten Material die Unterstützung für Instancing aktiviert ist.

Eine Einschränkung bleibt bestehen. Die verwendeten Gras-Modelle wurden selbst erstellt und sind nicht auf eine möglichst geringe Zahl von Dreiecken hin optimiert; Vergleichssysteme arbeiten in der niedrigsten Detailstufe mit deutlich einfacheren Modellen. Die erreichte Leistung ist für den Prototyp ausreichend, lässt aber Spielraum. Eine Überarbeitung der Modelle sowie ein weicher Übergang zwischen den Detailstufen sind für die Weiterentwicklung nach der Abgabe vorgesehen.

## Editor-Tool zur Weltgenerierung

### Aufbau nach dem MVP-Muster

Die im vorherigen Abschnitt beschriebene Pipeline berechnet ausschließlich Daten und erzeugt von sich aus nichts in der Szene. Bedient wird sie über ein eigenes Editor-Fenster, das nach dem MVP-Muster aufgebaut ist. Das Muster besteht aus drei Teilen, von denen nur zwei neu hinzugekommen sind: Das Model ist die bestehende Pipeline und wurde für das Tool nicht verändert. Die View ist das Fenster selbst und zeichnet lediglich die Bedienelemente. Der Presenter nimmt die Klicks entgegen, prüft die Voraussetzungen, ruft die Stufen der Pipeline auf und verwaltet die erzeugten Objekte in der Szene. Die Aufteilung hat den praktischen Nutzen, dass die Pipeline weiterhin unabhängig vom Editor bleibt und derselbe Ablauf später auch zur Laufzeit aufgerufen werden kann.

### View

Die View ist ein EditorWindow und wird über einen eigenen Eintrag im Tools-Menü geöffnet. Sie besitzt genau zwei Felder: die zugewiesene TerrainConfig und eine Instanz des Presenters. Das Config-Feld ist als serialisiertes Feld angelegt, wodurch die einmal zugewiesene Config sowohl das Schließen des Fensters als auch einen Neustart des Editors überdauert. Das Zeichnen erfolgt in einer von Unity aufgerufenen Methode, die bei jeder Neudarstellung des Fensters vollständig durchlaufen wird. Da die verwendete Oberflächentechnik ihre Felder so aufbaut, dass jedes Feld seinen neuen Wert zurückgibt, weist sich das Config-Feld bei jedem Durchlauf selbst neu zu, und Schaltflächen liefern nur in dem Durchlauf einen Treffer, in dem sie angeklickt wurden.

Die Bedienelemente sind in drei Gruppen aufgeteilt. Eine Schaltfläche erzeugt die Welt vollständig, darunter liegen die Einzelstufen für Gelände und Platzierung, und am Ende stehen die Schaltflächen zum Entfernen. Die Zeilen für die einzelnen Objekttypen werden nicht fest programmiert, sondern aus der Liste der Placeables in der Config erzeugt. Ein neuer Objekttyp erhält dadurch automatisch seine eigene Zeile mit den Schaltflächen zum Platzieren und Entfernen, ohne dass am Tool etwas geändert werden muss. Am unteren Rand zeigt das Fenster eine Statusmeldung an, die der Presenter bereitstellt.

### Vermeidung von Fehlbedienung

Ohne zugewiesene Config lassen sich die von ihr abhängigen Stufen nicht auslösen. Die betreffenden Schaltflächen werden in einem Bereich gezeichnet, der sie geschlossen deaktiviert, und zusätzlich weist ein Hinweisfeld auf die fehlende Angabe hin. Die Schaltflächen zum Entfernen bleiben dagegen bewusst nutzbar, da zum Aufräumen der Szene keine Config benötigt wird. Ergänzend gibt der Presenter nach jedem Vorgang eine Statusmeldung zurück, die entweder das Ergebnis nennt oder erklärt, warum nichts geschehen ist. Fehlbedienung wird damit auf zwei Wegen behandelt: Wo eine Aktion sinnlos wäre, ist sie nicht auslösbar; wo sie ins Leere läuft, wird der Grund genannt.

### Presenter und Zuständigkeiten

Der Presenter besitzt die erzeugten Objekte in der Szene. Die Namen dieser Objekte sind ausschließlich dort als private Konstanten hinterlegt, und die Methode, die ein Objekt anhand seines Namens entfernt, ist ebenfalls privat. Nach außen stehen stattdessen benannte Methoden zur Verfügung, die eine Absicht ausdrücken. Die View gibt damit an, was geschehen soll, und niemals, wie ein Objekt heißt. Der Unterschied ist nicht nur stilistisch: Wäre die Entfernung über einen Namen öffentlich, wäre ein Schreibfehler in diesem Namen syntaktisch fehlerfrei, würde aber nichts entfernen und lediglich melden, dass nichts gefunden wurde. Ein solcher Fehler wäre erst im Betrieb erkennbar. Über die benannten Methoden kann er nicht entstehen.

Dasselbe Vorgehen wiederholt sich beim Platzieren und Entfernen einzelner Objekttypen. Statt einer flexiblen Methode mit zusätzlichen Angaben bestehen jeweils zwei gleichnamige Methoden, von denen die eine alle Typen betrifft und die andere einen einzelnen. Der Aufrufer wählt damit die Absicht über die Signatur. Ergänzend sind die beiden Methoden, die die View bei jeder Neudarstellung aufruft, als reine Abfragen ausgelegt und verändern keinen Zustand; andernfalls entstünden Nebenwirkungen allein dadurch, dass das Fenster sichtbar ist.

### Aufbau in der Szene

Die erzeugten Objekte liegen in einer festen Anordnung: unter einem Wurzelobjekt für das Gelände liegen die einzelnen Chunks, die Wasserfläche und ein weiteres Wurzelobjekt für die Platzierung, unter dem je Objekttyp eine eigene Gruppe angelegt wird. Diese Anordnung dient zugleich als Aufräummechanismus: Wird das Gelände neu erzeugt, entfällt die darunterliegende Platzierung automatisch, ohne dass dafür eigener Code notwendig wäre. Wird dagegen ein einzelner Typ neu platziert, wird nur dessen Gruppe ersetzt, sodass sich ein Objekttyp einstellen lässt, ohne die übrigen erneut zu erzeugen. Beim Neuerzeugen des Geländes werden außerdem nur diejenigen Kindobjekte entfernt, die das Tool selbst angelegt hat, damit von Hand eingefügte Objekte unterhalb des Geländes erhalten bleiben.

### Besonderheiten im Editor-Betrieb

Der Betrieb außerhalb des laufenden Spiels bringt Einschränkungen mit sich, die im laufenden Spiel nicht auftreten. Objekte müssen mit der sofort wirkenden Variante der Löschfunktion entfernt werden, da die übliche Variante außerhalb des Spielbetriebs nicht zulässig ist. Bei Mesh und Material werden die geteilten Varianten verwendet, weil die jeweils anderen im Editor eine Kopie anlegen und dadurch unbemerkt Daten vervielfältigen würden. Nach jedem Vorgang wird die geöffnete Szene ausdrücklich als verändert gekennzeichnet. Ohne diesen Schritt bleibt eine über ein Skript erzeugte Geometrie für den Editor unsichtbar verändert, und das Ergebnis geht beim Wechsel der Szene verloren, ohne dass überhaupt nach dem Speichern gefragt wird.

Eine weitere Anpassung betrifft das Material. Wird in der Config kein Material angegeben, greift das Tool auf das Standardmaterial der aktiven Renderpipeline zurück. Das allgemeine Standardmaterial von Unity ist mit der im Projekt verwendeten Universal Render Pipeline nicht verträglich und würde die Flächen in Magenta darstellen, was in Unity auf einen nicht übersetzbaren Shader hinweist. Für die Suche nach untergeordneten Objekten wird zudem die auf den jeweiligen Teilbaum beschränkte Suche verwendet statt der szenenweiten, sodass ein gleichnamiges Objekt an anderer Stelle nicht versehentlich gefunden werden kann.

### Bewusste Grenzen

Das Tool kennt im aktuellen Stand keine Rücknahme einzelner Schritte. Ein versehentliches Erzeugen oder Entfernen lässt sich daher nicht über die übliche Tastenkombination rückgängig machen, sondern nur durch erneutes Ausführen des jeweiligen Vorgangs. Da die Erzeugung über den Seed vollständig reproduzierbar ist, führt ein erneuter Durchlauf zum selben Ergebnis, sodass kein Datenverlust entsteht. Ebenfalls bewusst nicht umgesetzt ist eine automatische Neuerzeugung bei jeder Änderung eines Wertes: Bei den hier auftretenden Rechenzeiten wäre ein solches Verhalten nicht praktikabel, und die Erzeugung soll eine bewusste Handlung bleiben.

## Threadoptimierung

### Messverfahren

Gemessen wurde der Neuaufbau der Grasdarstellung beim Start der Szene, da dieser Vorgang die gesamte Platzierung durchläuft und damit den rechenintensivsten Teil des Projekts enthält. Die Zeiten der einzelnen Abschnitte werden über Stoppuhren erfasst und in einer Zeile ausgegeben. Die Ausgabe ist so eingegrenzt, dass sie nur im Editor und in einem Entwicklungs-Build erfolgt; in einer Verkaufsfassung entstünde keine Ausgabe, wodurch die Vorgabe eingehalten bleibt, dass fertige Builds keine Protokollausgaben enthalten.

Je Messpunkt wurde ein eigener Entwicklungs-Build erstellt und viermal ausgeführt. Der erste Durchlauf wird dabei grundsätzlich verworfen, da zu diesem Zeitpunkt die Übersetzung des Zwischencodes noch nicht abgeschlossen und der Zwischenspeicher des Prozessors nicht gefüllt ist; er war in allen Messreihen der langsamste Durchlauf. Gewertet wird der Mittelwert der Durchläufe zwei bis vier. Zusätzlich werden mit jeder Messung die zugehörigen Kennzahlen ausgegeben, also die Anzahl der Prozessorkerne, die Anzahl der Kacheln sowie die Zahl der erzeugten und der übrig gebliebenen Punkte. Ohne diese Angaben ließen sich die Protokolle zweier Builds im Nachhinein nicht mehr auseinanderhalten. Alle Messungen erfolgten auf demselben System mit acht Kernen und sechzehn Threads.

Im Verlauf der Messreihe wurde die Aufteilung der Abschnitte einmal geändert. In den ersten beiden Messpunkten wurden das Erzeugen der Punkte und deren Filterung getrennt erfasst. Nachdem beide Vorgänge in einem gemeinsamen Durchgang zusammengefasst wurden, war eine getrennte Messung nicht mehr möglich; ab diesem Punkt wird die gemeinsame Zeit ausgewiesen. Die Gesamtzeit bleibt über alle Messpunkte hinweg vergleichbar.

### Ausgangslage und erster Optimierungsversuch

Der unveränderte Ausgangszustand benötigte für den vollständigen Aufbau 122,7 Sekunden. Der erste Versuch bestand darin, die Regelprüfung der einzelnen Punkte über den Threadpool zu verteilen, da diese Prüfung punktweise erfolgt und die Punkte einander nicht beeinflussen. Das Ergebnis lag bei 118,1 Sekunden und damit bei einer Verbesserung von 3,7 Prozent.

Die Ursache lässt sich aus der Messung selbst ableiten. Von den 122,7 Sekunden entfielen rund 103,4 Sekunden auf das Erzeugen der Punkte, also etwa 84 Prozent. Dieser Teil war zu diesem Zeitpunkt nicht parallelisierbar, weil jeder neue Punkt gegen die bereits gesetzten geprüft werden muss und damit vom Ergebnis der vorherigen Schritte abhängt. Die verbleibenden 16 Prozent bilden die Obergrenze dessen, was durch die Parallelisierung des übrigen Teils überhaupt erreichbar gewesen wäre. Der gemessene Gewinn von 3,7 Prozent liegt innerhalb dieser Grenze; der Versuch ist damit nicht an der Umsetzung gescheitert, sondern war in seiner Wirkung von vornherein begrenzt. Diese Beobachtung entspricht dem Gesetz von Amdahl, nach dem der erreichbare Gewinn durch den nicht parallelisierbaren Anteil begrenzt wird. Daraus ergab sich die eigentliche Schlussfolgerung des Projekts: Nicht die bereits parallelisierbare Stelle ist zu suchen, sondern die teure Stelle ist parallelisierbar zu machen.

### Kachelung der Platzierung

Umgesetzt wurde dies dadurch, dass die Platzierung nicht mehr über die gesamte Welt in einem Durchgang erfolgt, sondern die Fläche in Kacheln unterteilt wird. Jede Kachel erzeugt und filtert ihre Punkte vollständig für sich und liest dabei keine Daten einer anderen Kachel. Damit entfällt die Abhängigkeit, die den Vorgang zuvor sequenziell erzwungen hat, und die Schleife über die Kacheln kann auf mehrere Threads verteilt werden. Die Kachelung ist über einen eigenen Wert in der Config einstellbar und unabhängig von der Aufteilung des Geländes in Chunks; ein Wert von eins stellt das ursprüngliche Verhalten wieder her.

Die Unterteilung hat zwei voneinander unabhängige Wirkungen. Zum einen wird der Speicherbedarf des Hilfsgitters, das beim Erzeugen der Punkte verwendet wird, deutlich kleiner. Über die gesamte Welt umfasst dieses Gitter bei dem eingestellten Mindestabstand rund 5.800 Zellen je Kante und damit etwa 134 Megabyte, während es je Kachel nur noch rund 725 Zellen je Kante und etwa 2,1 Megabyte umfasst. Ein Gitter dieser Größe passt in den Zwischenspeicher des Prozessors, wodurch die Zugriffe erheblich schneller erfolgen. Zum anderen wird der Vorgang überhaupt erst parallelisierbar. Um beide Wirkungen unterscheiden zu können, wurde ein zusätzlicher Messpunkt erhoben, bei dem die Kachelung bereits umgesetzt, die Verteilung auf mehrere Threads aber noch nicht aktiviert war.

Die Anzahl der Kacheln wurde auf 64 festgelegt. Die Begründung stützt sich auf drei Größen. Für eine gleichmäßige Auslastung sollten deutlich mehr Kacheln als Threads vorhanden sein, damit einzelne länger laufende Kacheln ausgeglichen werden können. Die Kacheln sollten zugleich klein genug bleiben, damit das Hilfsgitter in den Zwischenspeicher passt. Dem steht entgegen, dass mit jeder weiteren Unterteilung die Gesamtlänge der Kachelgrenzen zunimmt. An diesen Grenzen kann der Mindestabstand zwischen zwei Punkten unterschritten werden, da zwei benachbarte Kacheln einander nicht kennen. Bei der gewählten Aufteilung ergibt sich eine Gesamtlänge der Grenzen von rund 28 Kilometern, was bei der vorliegenden Objektdichte optisch nicht wahrnehmbar ist. Ein zusätzlicher Durchgang, der ausschließlich die Randstreifen bereinigt, wäre die naheliegende Lösung und ist für die Weiterentwicklung vorgemerkt.

### Fallstricke bei paralleler Ausführung

Während der Umsetzung traten vier Probleme auf, die sich erst bei paralleler Ausführung zeigen und von denen keines eine Fehlermeldung erzeugt hat. Die zur Umformung der Höhen verwendete AnimationCurve speichert intern den zuletzt getroffenen Stützpunkt, um aufeinanderfolgende Abfragen zu beschleunigen. Werden zwei Abfragen gleichzeitig gestellt, liefern sie einander falsche Werte. Gelöst wurde dies, indem die Kurve einmal auf dem Hauptthread in eine Tabelle abgetastet wird, auf die anschließend nur noch lesend zugegriffen wird.

Zweitens ist der verwendete Zufallszahlengenerator nicht für gleichzeitigen Zugriff ausgelegt. Darüber hinaus wäre bei gemeinsamer Nutzung die Reihenfolge der Zugriffe ergebnisrelevant, wodurch dasselbe Startwert nicht mehr dieselbe Welt erzeugt hätte. Jede Kachel erhält deshalb einen eigenen Generator, dessen Startwert vorab auf dem Hauptthread gezogen wird. Drittens greift der Vergleich eines Assets mit einem leeren Verweis in Unity auf nativen Code zu und darf daher nicht innerhalb der Schleife erfolgen; die Prüfung wird einmal vorher ausgewertet. Viertens ist der Zugriff auf die Position eines Objekts in der Szene kein einfacher Feldzugriff, sondern ebenfalls ein Aufruf in nativen Code. Der Ausschlussfilter fragte diese Position für jede einzelne Platzierung ab, also über sieben Millionen Mal, obwohl sich der Wert während des gesamten Vorgangs nicht ändert. Nachdem die Ausschlussbereiche einmal vor der Schleife in einfache Werte aufgelöst wurden, sank die Dauer dieses Abschnitts von 2,57 auf 0,97 Sekunden.

Allen vier Fällen liegt dasselbe Muster zugrunde: Was sich während eines Vorgangs nicht ändert, sollte einmal auf dem Hauptthread aufgelöst werden, damit die parallel ausgeführten Teile ausschließlich rechnen. Bemerkenswert ist dabei, dass keiner der Fehler zu einem Absturz oder einer Meldung geführt hätte; sie wären ausschließlich über falsche oder nicht reproduzierbare Ergebnisse aufgefallen.

### Ergebnis der Messreihe

Der Ausgangszustand benötigte 122,7 Sekunden. Die punktweise Parallelisierung der Regelprüfung ergab 118,1 Sekunden, was einer Verbesserung von 3,7 Prozent entspricht. Die Kachelung ohne Verteilung auf mehrere Threads ergab 98,9 Sekunden und damit 19,4 Prozent; dieser Anteil ist allein auf die bessere Ausnutzung des Zwischenspeichers zurückzuführen. Mit Verteilung auf mehrere Threads sank die Zeit auf 16,5 Sekunden, also 86,6 Prozent gegenüber dem Ausgangszustand; der Kacheldurchgang allein lief dabei 9,2 mal schneller als in der sequenziellen Fassung. Nach der Überarbeitung des Ausschlussfilters ergaben sich 12,4 Sekunden und damit eine Gesamtverbesserung von 89,9 Prozent.

  ---------------------------------------------------------------------------------------------------------------------------
                Messpunkt                Erzeugen und Filtern (s)   Ausschluss (s)   Zellbau (s)   Gesamt (s)   Verbesserung
  ------------------------------------- -------------------------- ---------------- ------------- ------------ --------------
             Ausgangszustand                      116,9                  2,2             3,6         122,7           --

    Regelprüfung punktweise parallel              113,1                  2,1             2,9         118,1         3,7 %

          Kachelung, ein Thread                    92,6                  2,4             3,4          98,9         19,4 %

       Kachelung, mehrere Threads                  10,1                  2,6             3,6          16,5         86,6 %

      Ausschlussfilter überarbeitet                8,8                   1,0             2,1          12,4         89,9 %

   Ergebnisliste vorbelegt (verworfen)             9,1                   1,0             2,0          12,2         90,1 %
  ---------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_Messreihe .anchor}Tabelle Messreihe der Threadoptimierung, Mittelwerte der Durchläufe zwei bis vier

Die Summe der Abschnitte liegt in jeder Zeile geringfügig unter der Gesamtzeit, da nicht jeder Zwischenschritt einzeln erfasst wurde.

Der Nutzen der zusätzlichen Zwischenmessung zeigt sich an diesen Zahlen unmittelbar. Ohne den Messpunkt mit Kachelung, aber ohne Threads, wäre der Sprung von 122,7 auf 16,5 Sekunden vollständig der Parallelisierung zugeschrieben worden. Tatsächlich entfällt ein Teil des Gewinns auf die geänderte Datenanordnung und wäre auch ohne jede Parallelisierung eingetreten. Eine Messreihe, die nur Anfangs- und Endzustand erfasst, hätte diesen Unterschied nicht sichtbar machen können.

### Verworfener Optimierungsversuch

Ein weiterer Versuch wurde durchgeführt und wieder zurückgenommen. Die Ergebnisliste der Platzierung wächst beim Befüllen und legt dabei mehrfach einen größeren Speicherbereich an. Es lag daher nahe, ihre Größe vorab festzulegen. Gemessen wurden 12,2 gegenüber 12,4 Sekunden, also 1,8 Prozent, wobei zwei der drei erfassten Abschnitte sogar langsamer ausfielen; der Unterschied liegt damit

innerhalb der Streuung der Messung. Die Ursache liegt darin, dass die Liste nicht einzeln, sondern abschnittsweise befüllt wird. Bei dieser Art des Befüllens ist die Anzahl der Elemente bereits bekannt, sodass der Speicherbereich ohnehin in einem Schritt angelegt wird und keine wiederholte Vergrößerung stattfindet. Die Änderung wurde daher zurückgenommen. Der Versuch ist hier dennoch aufgeführt, weil er zeigt, dass eine dem Grunde nach sinnvolle Optimierung wirkungslos bleibt, wenn die zugrunde liegende Annahme über den Ablauf nicht zutrifft, und dass diese Beurteilung nur über eine Messung möglich ist.

#  UML-Klassendiagramm:

## KI Prototyp Sheep

![[]{#_Toc237370231 .anchor}Abbildung Sheep Komponenten](TDD_Media/media/image4.png){width="8.722983377077865in" height="4.4528576115485565in"}

![[]{#_Toc237370232 .anchor}Abbildung Sheep FSM](TDD_Media/media/image5.png){width="9.368055555555555in" height="5.37680883639545in"}

## DayNightSystem

![](TDD_Media/media/image6.png){width="9.00942804024497in" height="3.669403980752406in"}

[]{#_Ref_Abb_8 .anchor}Abbildung UML DayNightSystem

## Terrain-Pipeline

![[]{#_Toc237370234 .anchor}Abbildung Terrain Pipeline](TDD_Media/media/image7.png){width="8.9375in" height="4.522946194225722in"}

## Objektplatzierung

![[]{#_Toc237370235 .anchor}Abbildung Objektplazierung](TDD_Media/media/image8.png){width="8.901042213473316in" height="6.025623359580052in"}

## Gras-Rendering

![[]{#_Toc237370236 .anchor}Abbildung Grass Rendering](TDD_Media/media/image9.png){width="8.894134951881014in" height="3.8047681539807523in"}

## Editor-Tool

![[]{#_Toc237370237 .anchor}Abbildung Editor Tool](TDD_Media/media/image10.png){width="8.782595144356955in" height="3.998264435695538in"}

#  Programmablaufplan:

08.06.26

## Sheep-AI

![[]{#_Ref_Abb_9 .anchor}Abbildung Allgemeiner Programmablauf der Sheep-AI von Initialisierung bis Runtime-Loop.](TDD_Media/media/image11.png){width="5.0274693788276466in" height="7.5in"}

## Zustände der Sheep-AI

![[]{#_Toc237370239 .anchor}Abbildung Zustände der Sheep-AI](TDD_Media/media/image12.png){width="9.209256342957131in" height="3.8278838582677164in"}

Der allgemeine Programmablaufplan zeigt den grundlegenden Ablauf der Sheep-Komponente von der Initialisierung bis zum laufenden Spielbetrieb. Dabei werden die wichtigsten Schritte dargestellt, die notwendig sind, damit ein Schaf seine Komponenten erhält, die Finite State Machine vorbereitet wird und das Schaf anschließend im Spiel auf Zustände und äußere Einflüsse reagieren kann.

Zu Beginn wird die Sheep-Komponente initialisiert. Dabei werden die benötigten Komponenten geladen, darunter SheepHealth, SheepHunger, SheepSense, SheepMoveBehaviour, SheepDodgeBehaviour, der NavMeshAgent und der Animator. Anschließend wird die SheepFSM erstellt und die einzelnen Sheep-States werden registriert. Dadurch stehen der FSM alle benötigten Zustände wie IdleState, PatrolState, OnAlertState, FleeState, RegroupState, HerdMovingState, DodgeState und weitere States zur Verfügung.

Nach der Registrierung der States werden relevante Events angemeldet. Dazu gehören die Events aus dem Health- und Hunger-System sowie die Anmeldung beim DayNightCycleEventManager. Dadurch kann das Schaf auf Schaden, Tod, Starvation und Tagesphasenwechsel reagieren. Nach dieser Initialisierung wechselt die FSM in den IdleState, der als Startzustand des Schafs dient.

Während des laufenden Spiels wird die FSM in jedem Frame über FSM.Tick() aktualisiert. Der aktuell aktive State prüft dabei seine Transitions und entscheidet, ob ein Zustandswechsel notwendig ist. Zusätzlich wird über HandleHerdMovementTransition() geprüft, ob ein normales Schaf aufgrund aktiver Herdenbewegung in den RegroupState wechseln muss.

Der Ablauf wiederholt sich während des Spielbetriebs fortlaufend. Dadurch entsteht ein Loop aus State-Aktualisierung, Transition-Prüfung und möglichem Zustandswechsel. Wird das Schaf deaktiviert oder das GameObject entfernt, werden die zuvor registrierten Events und Listener wieder abgemeldet. Dadurch werden ungültige Eventverbindungen vermieden und das System bleibt stabiler.

## Editor-Tool

![[]{#_Toc237370240 .anchor}Abbildung Ablauf Generate Complete](TDD_Media/media/image13.png){width="9.181719160104986in" height="6.637998687664042in"}

# Shader

## MoonShader

Wie in [Abbildung 13](#_Ref_Abb_10) zu sehen ist, wurde der Mond in einem stylized Look dargestellt. Dafür besitzt der Mond eine eigene Textur, die durch den Shader farblich angepasst und stilisiert wird. Zusätzlich wird ein äußerer Leuchteffekt erzeugt, wodurch der Mond heller wirkt und stärker in den Fokus des Spielers rückt.![](TDD_Media/media/image14.png){width="6.298608923884514in" height="4.449479440069991in"}

[]{#_Ref_Abb_10 .anchor}Abbildung The Moon

Der MoonShader besteht aus zwei Funktionsbereichen, siehe [Abbildung 14](#_Ref_Abb_11). Der erste Bereich bearbeitet die Haupttextur des Mondes. Dafür wird eine Sample Texture 2D Node verwendet, in der die Mondtextur eingelesen wird. Anschließend wird die Textur mit einer Posterize Node reduziert. Dadurch entstehen weniger Farbabstufungen, wodurch die Textur stilisierter und weniger realistisch wirkt.

Danach wird das Ergebnis mit einer Color Property multipliziert. Dadurch kann die Grundfarbe des Mondes angepasst werden. Über eine Add Node wird anschließend ein Float-Wert hinzugefügt, mit dem der Kontrast beziehungsweise die Helligkeit der Textur beeinflusst werden kann. Danach wird das Ergebnis mit einem weiteren Float-Wert multipliziert, um die allgemeine Leuchtstärke des Mondes zu steuern.

Der zweite Funktionsbereich erzeugt den äußeren Glow-Effekt. Dafür wird eine Fresnel Effect Node verwendet. Diese erzeugt einen Effekt, der vor allem an den Kanten des Objekts sichtbar wird. Die Fresnel-Maske wird anschließend mit einer Power Node verändert. Über den dazugehörigen Float-Wert kann gesteuert werden, wie stark und wie scharf der Glow an den Außenbereichen des Mondes erscheint.

Anschließend wird der Fresnel-Effekt mit einer Color Property multipliziert, um die Farbe des Glows festzulegen. Danach wird das Ergebnis nochmals mit einem Float-Wert multipliziert, wodurch die Stärke des Glow-Effekts angepasst werden kann.

Zum Schluss werden die bearbeitete Mondtextur und der Glow-Effekt mit einer Add Node zusammengeführt. Das finale Ergebnis wird anschließend mit dem Base Color Eingang des Fragment-Bereichs verbunden. Dadurch entsteht ein stilisierter Mond mit angepasster Texturfarbe, kontrollierbarer Helligkeit und einem äußeren Leuchteffekt.

![[]{#_Ref_Abb_11 .anchor}Abbildung MoonShaderGraph](TDD_Media/media/image15.png){width="6.298608923884514in" height="2.5360695538057745in"}

## StylizedPondWaterShader

Wie in [Abbildung 15](#_Ref_Abb_12) zu sehen ist, handelt es sich beim StylizedPondWaterShader um einen stilisierten Wasser-Shader. Dieser Shader ist eher für kleinere Wasserflächen wie Teiche, Brunnen oder ruhiges Wasser gedacht und weniger für große Meere. Das Wasser ist relativ transparent und besitzt mehrere Funktionen. Zum einen kann die Wasserfarbe abhängig von der Tiefe angepasst werden. Flache Bereiche können dadurch heller aussehen, während tiefere Bereiche dunkler oder stärker gefärbt werden. Zusätzlich besitzt der Shader eine Schaum-Funktion, die vor allem an Übergängen zu Objekten oder am Rand von flachen Bereichen sichtbar wird. Außerdem wird eine leichte Wasserbrechung erzeugt, wodurch die Szene unter dem Wasser verzerrt dargestellt wird.

![[]{#_Ref_Abb_12 .anchor}Abbildung Stylized Water Pond](TDD_Media/media/image16.png){width="6.298608923884514in" height="2.832979002624672in"}

In [Abbildung 16](#_Ref_Abb_13) ist der Depth Fade Subgraph zu sehen. Dieser Subgraph wurde erstellt, damit die Tiefenberechnung nicht jedes Mal neu im Shader aufgebaut werden muss. Dadurch bleibt der Shader übersichtlicher und der gleiche Aufbau kann an mehreren Stellen wiederverwendet werden.

Der Depth Fade berechnet, wie groß der Abstand zwischen der Wasseroberfläche und der Szene dahinter beziehungsweise darunter ist. Dafür wird zuerst eine Screen Position Node verwendet. Diese wird mit einer Split Node aufgeteilt. Von der Screen Position wird die A-Komponente verwendet. Zusätzlich wird mit einer Scene Depth Node die Tiefe der Szene an dieser Bildschirmposition ausgelesen. Danach wird die Tiefe der

Wasseroberfläche von der Szenentiefe subtrahiert. Dadurch entsteht ein Wert, der beschreibt, wie weit die Geometrie hinter oder unter dem Wasser entfernt ist.

Dieser Wert wird anschließend durch den Parameter Distance dividiert. Mit diesem Parameter kann eingestellt werden, wie stark oder wie weit der Tiefenübergang sichtbar sein soll. Zum Schluss wird der Wert mit einer Saturate Node auf den Bereich von 0 bis 1 begrenzt. Das Ergebnis ist eine Maske, die später für die Wasserfarbe und den Schaum benutzt werden kann. Bereiche mit wenig Abstand haben einen niedrigen Wert, während tiefere Bereiche einen höheren Wert bekommen.

![[]{#_Ref_Abb_13 .anchor}Abbildung StylizedWaterPondShader Part 1](TDD_Media/media/image17.png){width="6.298608923884514in" height="3.1210990813648296in"}

[Abbildung 17](#_Ref_Abb_14) zeigt den Movement Subgraph. Dieser Subgraph erzeugt eine Bewegung für UV-Koordinaten. Er macht also nicht direkt das Wasser sichtbar, sondern erzeugt bewegte Koordinaten, die später für Noise-Muster benutzt werden.

Dafür wird eine Time Node mit dem Parameter Speed multipliziert. Dadurch kann eingestellt werden, wie schnell sich die Bewegung verändert. Danach wird dieser Wert in eine Tiling And Offset Node geführt. Der Offset sorgt dafür, dass sich das spätere Muster über die Zeit verschiebt. Zusätzlich wird über den Parameter Scale die Größe des

Musters eingestellt. Ein kleiner oder großer Scale-Wert verändert also, wie fein oder groß das Noise-Muster auf der Wasserfläche erscheint.

Dieser Movement Subgraph wird später mehrfach verwendet, zum Beispiel für den Schaum und für die Wasserbrechung. Dadurch muss die Bewegung nicht jedes Mal neu aufgebaut werden.

![[]{#_Ref_Abb_14 .anchor}Abbildung StylizedWaterPondShader Part 2](TDD_Media/media/image18.png){width="6.3in" height="3.1743099300087487in"}

In [Abbildung 18](#_Ref_Abb_15) ist der Bereich für den Foam, also den Schaum, dargestellt. Der Schaum wird mit Hilfe des Depth Fade Subgraphs erzeugt. Über den Parameter FoamAmount wird eingestellt, wie breit der Bereich ist, in dem Schaum entstehen kann. Das Ergebnis wird anschließend mit FoamCutoff multipliziert. Dadurch kann genauer geregelt werden, ab wann der Schaum sichtbar wird.

Zusätzlich wird der Movement Subgraph verwendet. Dieser bewegt die UV-Koordinaten für ein Gradient Noise. Dadurch bleibt der Schaum nicht komplett statisch, sondern bekommt eine leichte Bewegung. Über FoamSpeed kann eingestellt werden, wie schnell sich das Schaum-Muster bewegt. Über FoamScale wird eingestellt, wie groß oder fein das Muster ist.

Das Gradient Noise wird danach zusammen mit der Tiefenmaske in eine Step Node geführt. Die Step Node macht aus dem weichen Noise einen härteren Schwarz-Weiß-Bereich. Dadurch entstehen klare Schaumflächen, statt nur ein weicher Verlauf. Danach wird diese Schaum-Maske mit der FoamColor kombiniert. So wird der Schaum nur dort sichtbar, wo die Tiefenmaske und das Noise-Muster zusammen einen sichtbaren Bereich ergeben.

![[]{#_Ref_Abb_15 .anchor}Abbildung StylizedWaterPondShader Part 3](TDD_Media/media/image19.png){width="6.298608923884514in" height="3.265968941382327in"}

[Abbildung 19](#_Ref_Abb_16) zeigt den Bereich Water Color. Hier wird die Grundfarbe des Wassers berechnet. Dafür wird wieder der Depth Fade Subgraph benutzt. Über den Parameter WaterDepth kann eingestellt werden, wie stark die Tiefe die Farbe beeinflusst.

Das Ergebnis des Depth Fade wird als T-Wert in eine Lerp Node geführt. In dieser Lerp Node wird zwischen zwei Farben überblendet. Die erste Farbe ist ShallowWater und steht für flaches Wasser. Die zweite Farbe ist DeepWater und steht für tieferes Wasser. Je nach Tiefe wird dann zwischen diesen beiden Farben gemischt.

Dadurch sieht das Wasser nicht überall gleich aus. Flache Stellen können zum Beispiel heller und klarer wirken, während tiefere Stellen dunkler oder kräftiger gefärbt werden. Das hilft dabei, die Tiefe des Wassers besser sichtbar zu machen und gibt dem Wasser einen stilisierten Look.

![[]{#_Ref_Abb_16 .anchor}Abbildung StylizedWaterPondShader Part 4](TDD_Media/media/image20.png){width="6.298608923884514in" height="4.140349956255468in"}

In [Abbildung 20](#_Ref_Abb_17) ist der Bereich Water Refraction zu sehen. Dieser Teil sorgt dafür, dass die Szene unter dem Wasser leicht verzerrt wird. Dadurch wirkt es so, als würde das Licht durch die Wasseroberfläche gebrochen werden.

Dafür wird wieder der Movement Subgraph benutzt. Dieses Mal wird er mit den Parametern RefractionSpeed und RefractionScale gesteuert. Die bewegten UV-Koordinaten werden in ein Gradient Noise geführt. Dieses Noise erzeugt ein bewegtes Muster. Danach wird dieses Muster mit einer Normal From Height Node in eine Art Normalen- beziehungsweise Verzerrungsinformation umgewandelt. Über RefractionStrength kann eingestellt werden, wie stark diese Verzerrung sein soll.

Diese Verzerrung wird danach mit der Screen Position addiert. Anschließend wird damit eine Scene Color Node abgetastet. Das bedeutet, dass die Szene unter dem Wasser nicht exakt an ihrer normalen Position angezeigt wird, sondern leicht verschoben. Dadurch entsteht der Eindruck einer Wasserbrechung.

Am Ende werden Wasserfarbe, Schaum und Brechung zusammengeführt. Die Wasserfarbe kommt aus dem Depth-Fade-Farbverlauf, der Schaum wird über die Foam-Maske darübergelegt und die Refraction sorgt für die Verzerrung der Szene unter dem Wasser. Dadurch entsteht ein transparenter, stilisierter Wasser-Shader, der besonders für ruhige Wasserflächen wie Teiche oder Brunnen geeignet ist.

![[]{#_Ref_Abb_17 .anchor}Abbildung StylizedWaterPondShader Part 5](TDD_Media/media/image21.png){width="6.298608923884514in" height="2.6315299650043746in"}

## GrassAlphaShader

Wie in [Abbildung 21](#_Ref_Abb_18) zu sehen ist, handelt es sich hierbei um einen stylized Grass Shader mit Alpha Clipping. Dabei wird eine Textur verwendet, deren Alphakanal beziehungsweise Schwarz-Weiß-Maske bestimmt, welche Bereiche des Meshes sichtbar bleiben und welche Bereiche ausgeschnitten werden. Der Shader besitzt mehrere Funktionen. Zum einen kann die Farbgebung des Grases angepasst werden. Zum anderen werden die Normalen so verändert, dass die Beleuchtung stilisierter wirkt und so behandelt wird, als würde das Gras hauptsächlich von oben beleuchtet werden. Zusätzlich verfügt der Shader über eine Wind- und Bending-Funktion, mit der die Bewegung des Grases gesteuert werden kann.

![[]{#_Ref_Abb_18 .anchor}Abbildung AlphaClip Gras](TDD_Media/media/image22.png){width="6.298608923884514in" height="2.1430599300087487in"}

Zunächst wird im Funktionsbereich Coloring, siehe [Abbildung 22](#_Ref_Abb_19), die Grastextur in eine Sample Texture 2D Node eingespeist. Der Alpha-Ausgang der Textur wird mit dem Alpha-Eingang des Fragment-Bereichs verbunden. Dadurch dient der Alphakanal als Maske für das Alpha Clipping. Dunkle beziehungsweise schwarze Bereiche der Maske werden abgeschnitten, während helle Bereiche sichtbar bleiben.

Zusätzlich wird der RGBA-Ausgang der Textur verwendet, um die Farbgebung des Grases zu steuern. Die Textur dient dabei als Maske für eine Lerp Node. Über diese Lerp Node wird zwischen zwei frei wählbaren Farben interpoliert. Dadurch entsteht ein Farbverlauf beziehungsweise ein Übergang zwischen einer helleren und einer dunkleren Grasfarbe. Das Ergebnis wird anschließend mit dem Base Color Eingang des Fragment-Bereichs verbunden.

Der nächste Funktionsbereich behandelt die Normalen des Grases. Dafür wird zunächst eine Vector3 Node verwendet, die als World Up Vector definiert wird. Dieser Vektor zeigt nach oben und wird anschließend durch eine Normalize Node normalisiert. Dadurch entsteht eine saubere Richtungsangabe.

Danach wird dieser Vektor mit einer Transform Node von World Space in Tangent Space umgewandelt. Dieser Schritt ist notwendig, da der Normal-Eingang des Fragment-Bereichs in diesem Shader einen Vektor im Tangent Space erwartet. Durch diese Logik wird das Gras so beleuchtet, als würden seine Normalen nach oben ausgerichtet sein. Dadurch entsteht ein stilisierter Look, bei dem die Beleuchtung weniger stark von der tatsächlichen Form der einzelnen Grasflächen abhängt.

![[]{#_Ref_Abb_19 .anchor}Abbildung GrassAlphaClipShader Part 1](TDD_Media/media/image23.png){width="6.298608923884514in" height="4.191139545056868in"}

Der letzte große Funktionsbereich ist der Windbereich, siehe [Abbildung 23](#_Ref_Abb_20). Zuerst wird eine Windmaske erzeugt, die auf der Position des Objekts in der Welt basiert. Dafür wird eine Position Node im World Space verwendet und in eine Split Node geleitet. Anschließend werden nur die X- und Z-Werte weiterverwendet, da sich das Windmuster horizontal über die Spielwelt bewegen soll. Diese beiden Werte werden anschließend zu einem Vector2 zusammengeführt.

Danach wird die Zeitbewegung für den Wind erzeugt. Dafür wird eine Time Node mit einem Float-Wert für die WindSpeed multipliziert. Das Ergebnis wird zu der vorherigen Windposition addiert. Dadurch verschiebt sich das Noise-Muster im Laufe der Zeit und erzeugt eine kontinuierliche Bewegung.

Im nächsten Schritt wird dieses Ergebnis in eine Simple Noise Node geführt, um ein natürlicher wirkendes Windmuster zu erzeugen. Das Noise-Ergebnis liegt zunächst im Wertebereich von 0 bis 1. Damit sich das Gras sowohl in die positive als auch in die negative Richtung bewegen kann, wird dieser Wertebereich umgerechnet. Dafür wird das Ergebnis zuerst mit 2 multipliziert und anschließend 1 subtrahiert. Dadurch entsteht ein Wertebereich von -1 bis 1.

![[]{#_Ref_Abb_20 .anchor}Abbildung GrassAlphaClipShader Part 2](TDD_Media/media/image24.png){width="6.298608923884514in" height="3.1384995625546805in"}

Danach wird dieses Windsignal mit einem Float-Wert für die WindStrength multipliziert, siehe [Abbildung 24](#_Ref_Abb_21). Dadurch kann die Stärke der Bewegung gesteuert werden. Anschließend wird das Ergebnis mit einer WindDirection multipliziert, damit eine allgemeine Windrichtung festgelegt werden kann.

Damit das Gras nicht komplett gleichmäßig verschoben wird, sondern am Boden verankert bleibt, wird zusätzlich eine Height Bend Mask erzeugt. Dafür wird eine UV Node verwendet und über eine Split Node der G-Kanal ausgelesen. Dieser Kanal entspricht dem vertikalen Verlauf der UVs und beschreibt damit die Höhe des Grases von unten nach oben. Der Wert wird anschließend mit einer Power Node und dem Parameter BendPower bearbeitet. Dadurch kann gesteuert werden, wie stark sich die unteren und oberen Bereiche des Grases bewegen. Der untere Bereich bleibt weitgehend fest, während sich die oberen Bereiche stärker im Wind biegen.

Im letzten Schritt wird die Windbewegung mit dieser Height Bend Mask multipliziert. Dadurch wirkt der Wind hauptsächlich auf die oberen Bereiche des Grases. Anschließend wird der berechnete Wind Offset zur Object Position addiert. Das Ergebnis wird mit dem Vertex Position Eingang verbunden. Dadurch werden die Vertices des Grases verschoben und das Gras erhält eine sichtbare Windbewegung.

Insgesamt entsteht so ein stylized Grass Shader, der Alpha Clipping, anpassbare Farbverläufe, stilisierte Beleuchtung und dynamische Windbewegung in einem Shader kombiniert.

![[]{#_Ref_Abb_21 .anchor}Abbildung GrassAlphaClipShader Part 3](TDD_Media/media/image25.png){width="6.298608923884514in" height="4.565099518810149in"}

## GrassMeshShader

Wie in [Abbildung 25](#_Ref_Abb_22) zu sehen ist, handelt es sich beim GrassMeshShader um einen stylized Grass Shader, der auf einem vorhandenen Gras-Mesh basiert. Das Gras wird also nicht nur über eine ausgeschnittene Textur dargestellt, sondern das Mesh selbst wird im Shader eingefärbt und im Vertex-Bereich bewegt. Der Shader besitzt mehrere Funktionen. Zum einen kann die Farbgebung des Grases über zwei Farben und einen einstellbaren Farbverlauf angepasst werden. Zusätzlich kann ein stilisiertes Muster auf das Gras gelegt und über einen Schalter aktiviert oder deaktiviert werden. Zum anderen wird eine Windbewegung simuliert, wodurch sich die Grashalme über die Zeit bewegen. Außerdem besitzt der Shader eine Interaktionsfunktion, mit der sich das Gras durch ein Objekt, zum Beispiel den Spieler, wegdrücken beziehungsweise verbiegen lässt.![](TDD_Media/media/image26.png){width="6.298608923884514in" height="1.7607097550306212in"}

[]{#_Ref_Abb_22 .anchor}Abbildung GrassMeshShader

In [Abbildung 26](#_Ref_Abb_23) ist der Aufbau der Farbgebung zu sehen. Der erste Bereich ist der First Color Mask Layer. Hier wird eine UV Node verwendet, deren Ausgabe in eine Split Node geführt wird. Aus dieser Split Node wird der G-Kanal verwendet. Dieser Kanal entspricht bei diesem Gras-Mesh der vertikalen UV-Richtung von unten nach oben. Dadurch kann er als Höhenverlauf für den Grashalm genutzt werden. Der Wert wird anschließend in eine Power Node geführt. Über den Parameter ColorMixPower kann die Verlaufskurve beeinflusst werden. Dadurch lässt sich steuern, ob der Übergang zwischen den beiden Grasfarben weicher über den gesamten Grashalm verläuft oder stärker in einen bestimmten Bereich verschoben wird.

Der zweite Bereich ist der Second Color Mask Layer. Dieser erzeugt ein zusätzliches Muster auf dem Gras. Dafür wird eine Voronoi Node verwendet, die ein unregelmäßiges, zellenartiges Muster erzeugt. Über den Parameter MaskDensity kann die Dichte beziehungsweise Skalierung dieses Musters angepasst werden. Danach wird das Muster mit einer Power Node verändert. Der Parameter MaskVisibility steuert dabei, wie stark die Voronoi-Maske später in die Farbmaske eingreift. Anschließend wird das Ergebnis mit einer Saturate Node auf den Bereich von 0 bis 1 begrenzt.

Im Bereich Coloring with Mask Switch werden die beiden Masken weiterverwendet. Die erste Farbmaske und die zweite Muster-Maske werden miteinander kombiniert. Über eine Branch Node kann anschließend entschieden werden, ob das zusätzliche Muster verwendet werden soll oder nicht. Ist der Schalter aktiv, wird die kombinierte Maske verwendet. Ist er deaktiviert, wird nur der einfache Farbverlauf aus dem First Color Mask Layer benutzt. Das Ergebnis wird danach als T-Wert in eine Lerp Node geführt. Diese interpoliert zwischen der dunklen und der hellen Grasfarbe. Das Ergebnis dieser Lerp Node bildet die finale Base Color des Grases.![](TDD_Media/media/image27.png){width="6.298608923884514in" height="4.162498906386702in"}

[]{#_Ref_Abb_23 .anchor}Abbildung GrassMeshShader Part 1

In [Abbildung 27](#_Ref_Abb_24) ist der Aufbau der Windmaske und der Windbewegung dargestellt. Zuerst wird eine Time Node verwendet. Der Zeitwert wird mit dem Parameter WindSpeed multipliziert. Dadurch kann eingestellt werden, wie schnell sich die Windbewegung verändert. Parallel dazu wird die World Position des Meshes verwendet. Diese wird mit einer Split Node aufgeteilt, wobei nur die X- und Z-Koordinaten weiterverwendet werden. Dadurch entsteht eine zweidimensionale Position auf der Bodenfläche.

Die X- und Z-Koordinaten werden anschließend mit dem bewegten Zeitwert addiert. Dadurch verschiebt sich die spätere Noise-Maske über die Welt. Diese Koordinaten werden in eine Gradient Noise Node eingespeist. Die Gradient Noise Node erzeugt eine unregelmäßige Maske, die bestimmt, welche Bereiche stärker oder schwächer vom Wind beeinflusst werden. Über den Parameter WindScale kann die Größe beziehungsweise Dichte dieses Noise-Musters angepasst werden.

Da die Gradient Noise Node Werte im Bereich von 0 bis 1 erzeugt, wird der Wert danach umgerechnet. Dafür wird der Noise-Wert zuerst mit 2 multipliziert und anschließend 1 subtrahiert. Dadurch entsteht ein Wertebereich von -1 bis 1. Das ist wichtig, damit sich das Gras nicht nur in eine Richtung bewegen kann, sondern in beide Richtungen ausschlagen kann. Anschließend wird dieser Wert mit WindStrength multipliziert, um die Stärke der Windbewegung zu bestimmen. Danach wird der Wert mit WindDir

multipliziert, wodurch die allgemeine Richtung der Vertex-Verschiebung festgelegt wird. Das Ergebnis dieses Blocks ist ein Wind-Offset, der später mit der Vertex-Position kombiniert wird.

![[]{#_Ref_Abb_24 .anchor}Abbildung GrassMeshShader Part 2](TDD_Media/media/image28.png){width="6.3in" height="2.2631889763779527in"}

[Abbildung 28](#_Ref_Abb_25) zeigt den Aufbau der Interaktionsfunktion. Diese Funktion sorgt dafür, dass das Gras auf ein Objekt reagieren kann. Dafür wird die Position des interagierenden Objekts über den Parameter InteractPos an den Shader übergeben. Zusätzlich wird die World Position des Gras-Vertices verwendet. Mit einer Distance Node wird die Entfernung zwischen der Grasposition und der Interaktionsposition berechnet.

Im Bereich Interaction Mask Radius wird aus dieser Entfernung eine Maske erzeugt. Die Entfernung wird zuerst mit einer Clamp Node begrenzt. Der maximale Bereich wird dabei durch InteractDistance bestimmt. Danach wird der Wert mit einer Remap Node umgerechnet. Direkt am Objekt ist der Einfluss der Maske am stärksten. Je weiter ein Gras-Vertex vom Objekt entfernt ist, desto schwächer wird der Einfluss. Am Rand des Interaktionsradius wird der Wert auf 0 reduziert. Dadurch reagiert nicht das gesamte Grasfeld, sondern nur der Bereich um das interagierende Objekt herum.

Im oberen Teil des Blocks wird die Richtung der Interaktion berechnet. Dafür wird die Interaktionsposition von der World Position des Gras-Vertices subtrahiert. Dadurch entsteht ein Richtungsvektor, der vom Objekt weg zeigt. Dieser Vektor wird anschließend angepasst, sodass das Gras nicht nur seitlich weggedrückt, sondern auch leicht nach unten gebogen wird. Danach wird der Vektor normalisiert, damit nur die Richtung erhalten bleibt. Anschließend wird er mit InteractStrength multipliziert, wodurch die Stärke der Interaktion eingestellt werden kann. Zum Schluss wird diese Bewegung mit der Interaktionsmaske multipliziert. Dadurch wirkt die Interaktion nur innerhalb des eingestellten Radius.

![[]{#_Ref_Abb_25 .anchor}Abbildung GrassMeshShader Part 3](TDD_Media/media/image29.png){width="6.292358923884515in" height="2.38332895888014in"}

In [Abbildung 29](#_Ref_Abb_26) wird die finale Vertex-Bewegung zusammengesetzt. Dafür wird zuerst im Bereich Height Bend Mask / Lock Grass Base eine Höhenmaske erzeugt. Auch hier wird wieder die UV Node verwendet. Der G-Kanal der UV-Koordinaten dient als Verlauf von unten nach oben. Dieser Verlauf wird in eine Power Node geführt und über BendPower angepasst. Dadurch kann gesteuert werden, wie stark die Bewegung auf den oberen Bereich der Grashalme konzentriert wird.

Diese Höhenmaske ist wichtig, damit die Basis des Grases am Boden fixiert bleibt. Ohne diese Maske würde sich der komplette Grashalm gleichmäßig verschieben. Dadurch würde das Gras so wirken, als würde es über den Boden rutschen. Durch die Höhenmaske bleiben die unteren Vertices fast unbewegt, während sich die oberen Vertices stärker durch Wind und Interaktion bewegen können.

Anschließend werden die berechnete Windbewegung und die Interaktionsbewegung jeweils mit dieser Höhenmaske multipliziert. Dadurch wirken beide Bewegungen hauptsächlich im oberen Bereich der Grashalme. Danach werden Wind-Offset und Interaction-Offset addiert. Das Ergebnis wird anschließend auf die ursprüngliche Object Position des Meshes addiert und in den Position-Eingang des Vertex-Bereichs geführt. Dadurch wird die Geometrie des Gras-Meshes direkt im Shader bewegt. So entsteht ein stylized Grass Shader, der nicht nur eingefärbt wird, sondern auch Wind und Objektinteraktion unterstützt.

![[]{#_Ref_Abb_26 .anchor}Abbildung GrassMeshShader Part 4](TDD_Media/media/image30.png){width="6.298608923884514in" height="4.066759623797025in"}

# VFX-Systeme

## FireFly

Wie in [Abbildung 30](#_Ref_Abb_27) zu sehen, sollen die FireFly-Partikel das Environment beleben und zusätzliche Lichtakzente setzen, indem kleine, leuchtende Partikel im Level verteilt werden.

![[]{#_Ref_Abb_27 .anchor}Abbildung FireFly Part 1](TDD_Media/media/image31.png){width="6.288188976377953in" height="3.4604199475065616in"}

[Abbildung 31](#_Ref_Abb_28) zeigt den Spawn- und den Initialize-Particle-Block. Im Spawn-Block legt eine konstante Spawn Rate fest, wie viele Partikel pro Sekunde erzeugt werden. Im Initialize-Particle-Block wird die Capacity auf 30 begrenzt, die Position über eine Box-Shape (Oriented Box, Surface) verteilt, die Größe auf 0,05 gesetzt und die Lifetime über einen Random-Uniform-Node definiert. Min- und Maxwert dieses Nodes stehen aktuell beide auf 5, die Lifetime ist damit im aktuellen Stand faktisch konstant; der Node bleibt als Random-Uniform angelegt, sodass später eine echte Streuung eingestellt werden kann, ohne die Struktur zu ändern. Für die Farbe wird zusätzlich ein exposed Parameter mit einem Bloom-Wert multipliziert, um den Leuchteffekt der Partikel zu verstärken.

![[]{#_Ref_Abb_28 .anchor}Abbildung FireFly Part 2](TDD_Media/media/image32.png){width="6.294438976377953in" height="6.423608923884514in"}

[Abbildung 32](#_Ref_Abb_29) zeigt den Update- und den Output-Particle-Block. Im Update-Particle-Block sorgt eine Turbulence-Node für eine unregelmäßige Bewegung, die den Partikeln ein organisches Schweben statt einer linearen Flugbahn gibt. Zusätzlich wird die Alpha über einen Random-Float-Node (0,1 bis 1) pro Frame neu gesetzt, wodurch die Partikel rhythmisch an- und abschwellen und so das charakteristische Blinken echter Glühwürmchen nachbilden. Im Output-Particle-Block ist der Blend Mode auf Additive gestellt, damit sich überlappende Partikel gegenseitig aufhellen statt zu verdecken. Main Texture und Soft Particle Fade Distance (aktuell 1, gegen harte Partikelränder) sind als exposed Parameter verfügbar. Die Ausrichtung läuft über Face Camera Position, wodurch jeder Partikel unabhängig vom Blickwinkel vollständig zur Kamera zeigt.

Die meisten Parameter (Spawn Rate, Bloom, Textur, Fade Distance) sind exposed, damit der Effekt später ohne Eingriff in den Graphen im Inspector angepasst werden kann.

![[]{#_Ref_Abb_29 .anchor}Abbildung FireFly Part 3](TDD_Media/media/image33.png){width="6.294438976377953in" height="6.490968941382327in"}

## SheepRun

Wie in [Abbildung 33](#_Ref_Abb_30) zu sehen, stellt der SheepRun-Effekt eine kleine Staubwolke dar, die entsteht, wenn das Sheep vor einem Gegner oder einer Bedrohung flieht. Der Staub soll das Gefühl von Panik und schnellem Wegrennen verstärken und die Szene dadurch lebendiger und actionreicher wirken lassen.

![[]{#_Ref_Abb_30 .anchor}Abbildung SheepRun Part 1](TDD_Media/media/image34.png){width="6.263889982502187in" height="3.276389982502187in"}

[Abbildung 34](#_Ref_Abb_31) zeigt den Spawn- und den Initialize-Particle-Block. Im Spawn-Block ist die Spawn Rate auf 30 gesetzt. Im Initialize-Particle-Block wird zunächst die Capacity begrenzt. Set Lifetime läuft über Random Uniform, damit die Partikel unterschiedlich lange leben und die Wolke dynamischer wirkt; ebenso Set Size über Random Uniform, wodurch größere und kleinere Partikel im Flipbook entstehen. Die Position wird über eine Sphere-Shape verteilt, deren Radius als exposed Parameter einstellbar ist. Set Velocity sorgt dafür, dass sich die Partikel überwiegend nach oben bewegen. Set Tex Index wählt zusätzlich zufällig zwischen den Indizes des Flipbooks, sodass nicht immer dieselbe Partikelform erscheint, sondern eine sichtbare Variation.

![[]{#_Ref_Abb_31 .anchor}Abbildung SheepRun Part 2](TDD_Media/media/image35.png){width="6.288188976377953in" height="6.619438976377952in"}

[Abbildung 35](#_Ref_Abb_32) zeigt den Update- und den Output-Particle-Block. Im Update-Particle-Block bremst ein Linear Drag die Aufwärtsbewegung ab, damit die Partikel nicht zu schnell nach oben schießen. Im Output-Particle-Block ist der UV Mode auf Flipbook gestellt, die Flipbook-Größe auf 4x4, mit der Main Texture als exposed Parameter. Multiply Size Over Life verändert die Partikelgröße über die Lebenszeit, Set Color Over Life regelt Farbverlauf und Transparenz, sodass die Partikel weich ein- und ausfaden. Orient: Face Camera Plane richtet die Partikel zusätzlich zur Kamera aus, damit die Staubwolke aus jeder Blickrichtung sichtbar bleibt.

Multiply Size Over Life, Set Color Over Life und die Orient-Node liegen bewusst im Output- statt im Update-Block: Da sie dort nur beim Rendering berechnet werden, kosten sie keine Simulationsperformance.

![[]{#_Ref_Abb_32 .anchor}Abbildung SheepRun Part 3](TDD_Media/media/image36.png){width="6.294438976377953in" height="4.8159689413823275in"}

## Smoke

Wie in [Abbildung 36](#_Ref_Abb_33) zu sehen, ist Smoke ein einfacher, generischer Raucheffekt, der sich für verschiedene Environment-Elemente einsetzen lässt, etwa für einen Magmafleck oder eine erloschene Feuerstelle, an der nur noch Rauch und keine Flamme mehr sichtbar ist.

![[]{#_Ref_Abb_33 .anchor}Abbildung Smoke Part 1](TDD_Media/media/image37.png){width="5.803468941382327in" height="5.030559930008749in"}

[Abbildung 37](#_Ref_Abb_34) zeigt den Spawn- und den Initialize-Particle-Block. Die Spawn Rate ist aktuell exposed einstellbar. Im Initialize-Particle-Block ist die Capacity auf 300 begrenzt; dieser Wert ist bewusst hochgesetzt, da noch nicht feststeht, an wie vielen Stellen der Effekt eingesetzt wird, und kann später bei Bedarf für die Performance reduziert werden. Set Lifetime läuft über Random Uniform, damit die Partikel unterschiedlich lange sichtbar bleiben statt alle gleich schnell zu verschwinden. Die Position wird über eine Sphere-Shape verteilt, bei der Position, Winkel, Radius und Arc exposed einstellbar sind. Set Velocity Random Per Component gibt dem Rauch eine Bewegung nach oben mit unterschiedlicher Reichweite sowie ein leichtes seitliches Schwanken, unabhängig von der Blickrichtung der Kamera.

![[]{#_Ref_Abb_34 .anchor}Abbildung Smoke Part 2](TDD_Media/media/image38.png){width="6.300688976377953in" height="4.711809930008749in"}

[Abbildung 38](#_Ref_Abb_35) zeigt den Update- und den Output-Particle-Block. Im Update-Particle-Block sorgt eine Turbulence mit exposed Parametern für eine abwechslungsreichere Bewegung, ein Linear Drag bremst die Partikel zusätzlich ab. Set Size Over Life lässt die Partikel über ihre Lebenszeit von klein nach groß wachsen, Set Color Over Life regelt die Transparenz so, dass der Rauch sanft einblendet und beim Verschwinden ausfadet, statt abrupt zu verschwinden. Im Output-Particle-Block ist die Textur exposed einstellbar, die Orient-Node sorgt dafür, dass der Effekt aus jeder Blickrichtung sichtbar bleibt.

![[]{#_Ref_Abb_35 .anchor}Abbildung Smoke Part 3](TDD_Media/media/image39.png){width="6.294438976377953in" height="5.907639982502187in"}

## Torch

Wie in [Abbildung 39](#_Ref_Abb_36) zu sehen, kombiniert der Torch-Effekt eine Flamme mit Rauchverhalten. Für die Umsetzung wurden zwei getrennte Partikelsysteme gewählt, ein Flame-System und ein Smoke-System, statt den Rauch über ein GPU Event aus den Flammen-Partikeln zu erzeugen. Da die Spawnpunkte der Flammen-Partikel über die Sphere-Shape verteilt sind, würde ein GPU-Event-gesteuerter Rauch an unterschiedlichen, zufälligen Stellen der Flamme entstehen. Ein eigenes Smoke-System mit einem festen Spawnpunkt sorgt stattdessen für einen konsistenten Rauchaufstieg von einer definierten Stelle aus.

![[]{#_Ref_Abb_36 .anchor}Abbildung Torch Part 1](TDD_Media/media/image40.png){width="6.294438976377953in" height="4.625688976377953in"}

[Abbildung 40](#_Ref_Abb_37) zeigt den Spawn- und den Initialize-Particle-Block des Flame-Systems. Die Spawn Rate ist exposed und aktuell auf 300 gesetzt, da viele kleine Partikel benötigt werden; im Initialize-Particle-Block ist die Capacity aus Performance-Gründen auf 500 begrenzt. Set Lifetime läuft über Random Uniform (0,5 bis 0,9), damit die einzelnen Flammen unterschiedlich lange leben. Die Position wird über eine Sphere-Shape verteilt, deren Radius (0,12) exposed ist und die Flammenform in ihrer Größe steuert. Set Velocity Random Per Component gibt den Partikeln eine Bewegung nach oben sowie ein leichtes seitliches Schwanken.

![[]{#_Ref_Abb_37 .anchor}Abbildung Torch Part 2](TDD_Media/media/image41.png){width="6.294438976377953in" height="7.411108923884514in"}

[Abbildung 41](#_Ref_Abb_38) zeigt den Update- und den Output-Particle-Block des Flame-Systems. Eine Turbulence-Node (alle Parameter exposed) mit spürbarem Drag und hoher Frequenz sorgt für die chaotische Flammenbewegung, ein Linear Drag bremst die Aufwärtsbewegung zusätzlich ab. Set Size Over Life kombiniert eine Kurve mit einem über Get Age Over Life (0 bis 1) gesteuerten Multiply-Node für zusätzliche Größenvariation; das genaue Zusammenspiel beider Kurven ist empirisch entstanden und optisch bewertet, nicht im Detail nachvollzogen. Set Color Over Life färbt die Flamme von Gelb über Orange zu Dunkelrot, während der Alpha-Wert zu Beginn hoch liegt, zur Lebensmitte leicht abnimmt und am Lebensende vollständig erlischt, sodass jede Flamme einzeln sauber ausfadet. Im Output-Particle-Block ist die Textur exposed, die Ausrichtung läuft aktuell über Face Camera Plane.

![[]{#_Ref_Abb_38 .anchor}Abbildung Torch Part 3](TDD_Media/media/image42.png){width="6.300688976377953in" height="6.56457895888014in"}

[Abbildung 42](#_Ref_Abb_39) zeigt den Spawn- und den Initialize-Particle-Block des Smoke-Systems. Der Aufbau ähnelt dem eigenständigen Smoke-Effekt (Spawn Rate, Set Lifetime Random, Position Shape Sphere, Set Velocity), verwendet aber eigene, abweichende Werte und exposed Parameter, mit etwas mehr Feinsteuerung im Update-Particle-Block.

![[]{#_Ref_Abb_39 .anchor}Abbildung Torch Part 4](TDD_Media/media/image43.png){width="6.300688976377953in" height="7.20832895888014in"}

[Abbildung 43](#_Ref_Abb_40) zeigt den Update- und den Output-Particle-Block des Smoke-Systems. Turbulence sorgt für eine unregelmäßige, flackernde Bewegung, ein Linear Drag bremst zusätzlich ab. Set Size Over Life lässt den Rauch über seine Lebenszeit wachsen. Set Color Over Life regelt die Transparenz so, dass sie mittelstark beginnt, auf etwa 25 % abnimmt und danach vollständig erlischt; dadurch verdeckt der Rauch die Flamme dahinter nicht vollständig, sondern bleibt leicht durchscheinend. Im Output-Particle-Block ist die Textur exposed, Use Soft Particle sorgt für einen weichen Partikelrand, die Ausrichtung läuft ebenfalls über Face Camera Plane.

Für beide Systeme wurde Face Camera Plane statt Face Camera Position gewählt, da Letzteres jeden Partikel einzeln zur Kamera ausrichtet und damit teurer ist. Als mögliche spätere Optimierung könnte geprüft werden, ob Face Camera Position hier einen sichtbaren optischen Vorteil bringt, der den Mehraufwand rechtfertigt.

![[]{#_Ref_Abb_40 .anchor}Abbildung Torch Part 5](TDD_Media/media/image44.png){width="6.251389982502187in" height="6.337498906386702in"}

#  Skalierbarkeit und Erweiterbarkeit:

Der *Isor's Tower Prototype* wurde so aufgebaut, dass einzelne Systeme später erweitert, ausgetauscht oder angepasst werden können. Besonders wichtig ist dabei die Trennung der Verantwortlichkeiten. Die einzelnen Komponenten übernehmen jeweils klar abgegrenzte Aufgaben, zum Beispiel Wahrnehmung, Bewegung, Gesundheit, Hunger, Tageszeit oder Herdenlogik. Dadurch müssen Änderungen nicht zwangsläufig das gesamte System betreffen, sondern können gezielt an einzelnen Komponenten vorgenommen werden.

Ein wichtiger skalierbarer Bereich ist die Finite State Machine der Sheep-AI. Neue Verhaltensweisen können ergänzt werden, indem zusätzliche State-Klassen erstellt und in der FSM registriert werden. Da alle States von SheepStateBase erben, besitzen sie eine einheitliche Grundstruktur mit Enter, Tick und Exit. Dadurch können neue Zustände wie weitere Reaktionen, spezielle Gruppenverhalten oder neue Umweltinteraktionen später eingebaut werden, ohne die bestehende FSM vollständig neu schreiben zu müssen.

Auch die Verwendung von ScriptableObjects unterstützt die Erweiterbarkeit des Projekts. Werte wie Bewegungsgeschwindigkeit, Wahrnehmungsradien, Hungerwerte, Fluchtverhalten oder State-Zeiten können über SheepSettings und SheepStateSettings angepasst werden, ohne direkt den Code verändern zu müssen. Dadurch können unterschiedliche Schaf-Typen oder später auch andere NPC-Arten mit eigenen Einstellungen erstellt werden.

Die Komponentenstruktur ermöglicht außerdem eine spätere Wiederverwendung einzelner Systeme. Komponenten wie SheepHealth, SheepHunger, SheepSense oder SheepMoveBehaviour sind aktuell auf das Schafsystem ausgelegt, können aber bei Bedarf weiter abstrahiert oder für andere Entitäten angepasst werden. Besonders das Health-System ist durch das Interface IDamageable bereits so vorbereitet, dass auch andere Objekte oder NPCs Schaden erhalten können.

Das Herden-System ist ebenfalls erweiterbar. Der HerdManager verwaltet aktuell Commander, Herdenanker, Patrouillenpositionen, Regroup-Positionen, Spawn-Positionen und Formationspositionen. Später könnten zusätzliche Formationen, mehrere Herden, unterschiedliche Commander-Verhalten oder komplexere Gruppenentscheidungen ergänzt werden. Auch das aktuelle Dodge-System kann später durch ein umfangreicheres Steering- oder Avoidance-System ersetzt oder erweitert werden.

Das Day-Night-System wurde über Events und das Interface IDayNightListener aufgebaut. Dadurch können weitere Systeme auf Tagesphasen reagieren, ohne direkt vom DayNightCycle abhängig zu sein. In späteren Entwicklungsphasen könnten dadurch zum Beispiel Gegner, Umgebungsobjekte, Lichtsysteme, Partikeleffekte, Musik oder NPC-Routinen abhängig von der Tageszeit gesteuert werden.

Trotz dieser Erweiterbarkeit gibt es Bereiche, die bei einer Weiterentwicklung überarbeitet werden könnten. Einige Entscheidungen liegen aktuell noch direkt in den States, wodurch bei wachsender Komplexität viele Transitions entstehen können. Für größere Projekte könnte später ein stärker zentralisiertes Entscheidungssystem. Auch Spawn-Logik, Animationsteuerung und Dodge-Verhalten könnten bei weiterem Ausbau in eigene spezialisierte Systeme ausgelagert werden.

Insgesamt ist die aktuelle Architektur für den Prototyp bewusst modular aufgebaut. Sie erfüllt die Anforderungen des aktuellen Projektstands und bietet gleichzeitig Ansatzpunkte für spätere Erweiterungen in weiteren Semestern.

#  Asset Integration und Lizenzanalyse:

08.06.26

Für das Projekt wurden zwölf externe Assets integriert: zwei Modellpakete, drei Texturpakete und sieben Audiopakete, um den Spielprototyp visuell und klanglich zu erweitern und Entwicklungszeit einzusparen. Dabei wurden bewusst Assets mit unterschiedlichen Lizenzarten gewählt. Dadurch kann verglichen werden, welchen Einfluss verschiedene Lizenzmodelle auf das Projekt haben.

Die sieben Audiopakete stehen ausnahmslos unter der Creative Commons Zero Lizenz (CC0) und werden deshalb nicht einzeln betrachtet. Für alle gilt dasselbe Ergebnis: keine Pflicht zur Namensnennung, private und kommerzielle Nutzung erlaubt, keine Gewährleistung, keine Copyleft-Pflicht und damit auch keine Konflikte mit den übrigen im Projekt verwendeten Lizenzen. Mehrere Anbieter bitten freiwillig um eine Nennung, ohne sie zur Bedingung zu machen; sie sind in der Tabelle namentlich aufgeführt. Ein weiteres gesichtetes Paket stand unter CC BY 3.0 und damit unter Namensnennungspflicht. Es wurde bewusst nicht in das Projekt übernommen, sodass im ausgelieferten Stand keine Attributionspflicht besteht.

##  Übersicht der verwendeten Assets

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               Asset                 Autor/Publisher           Quelle                             Lizenz                                     Verwendung im Projekt
  ------------------------------- --------------------- -------------------- ------------------------------------------------- -------------------------------------------------
             Cute Pet                    SURIYUN         Unity Asset Store    Standard Unity Asset Store EULA / Single Entity   Tiermodelle und Animationen für den KI-Prototyp

   Ultimate Stylized Nature Pack       Quaternius        Quaternius Website             Creative Commons Zero (CC0)              Natur- und Umgebungsobjekte für die Spielwelt

             Moon 002                 3dtextures.me        3dtextures.me                Creative Commons Zero (CC0)                 Texturen des Mondes im Tag-Nacht-System

            Ground082S                  ambientCG            ambientCG                  Creative Commons Zero (CC0)                  Bodentextur des generierten Geländes

             Grass 05                 freestylized        freestylized.com                 Royalty Free License                       Grastextur des generierten Geländes

          Town Theme RPG               cynicmusic           OpenGameArt                 Creative Commons Zero (CC0)                        Hintergrundmusik im Dorf

             The Wind              Loyalty Freak Music      OpenGameArt                 Creative Commons Zero (CC0)                      Hintergrundmusik im Hauptmenü

               Wind                      IgnasD             OpenGameArt                 Creative Commons Zero (CC0)                     Windböen als Umgebungsgeräusch

          Different Steps              TinyWorlds           OpenGameArt                 Creative Commons Zero (CC0)                          Schritte des Spielers

     Wood-Burning on Fireplace           PagDev             OpenGameArt                 Creative Commons Zero (CC0)                        Feuergeräusch der Fackeln

             Sheep baa                  mikewest            OpenGameArt                 Creative Commons Zero (CC0)                            Blöken der Schafe

         RPG Sound Effects               Kenney             OpenGameArt                 Creative Commons Zero (CC0)                         Rückmeldung beim Zähmen
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref_Tab_8 .anchor}Tabelle Übersicht der verwendeten Assets

## Cute Pet -- SURIYUN

SURIYUN, 2025. *Cute Pet*. \[online\] Verfügbar unter: <https://assetstore.unity.com/packages/3d/characters/animals/mammals/cute-pet-96976> \[Zugegriffen 06.06.2026\].

**Lizenztyp**\
Das Asset „Cute Pet" wird über den Unity Asset Store angeboten und besitzt den Lizenztyp „Single Entity". Es fällt damit unter die Standard Unity Asset Store EULA (SURIYUN, 2025; Unity Technologies, 2024).

**Attribution**\
Eine namentliche Nennung des Erstellers ist nach der Standard Unity Asset Store EULA grundsätzlich nicht zwingend erforderlich, sofern auf der Asset-Seite oder in zusätzlichen Lizenzdateien keine weiteren Bedingungen genannt werden. Der Publisher bleibt jedoch Rechteinhaber des ursprünglichen Assets. Im TDD wird das Asset trotzdem mit Name, Publisher, Quelle und Lizenz dokumentiert.

**Commercial / Private Use**\
Das Asset darf im privaten und kommerziellen Projektkontext verwendet werden, solange es als eingebetteter Bestandteil eines Spiels oder einer Anwendung genutzt wird. Unity beschreibt, dass Assets aus dem Asset Store grundsätzlich in kommerziellen Projekten verwendet werden können, sofern keine zusätzlichen Einschränkungen für das jeweilige Asset bestehen (Unity Support, 2025c).

**Gewährleistung**\
Es besteht kein allgemeiner Anspruch auf Fehlerfreiheit, Support oder Schadensersatz. Für das Projekt bedeutet das, dass die technische Integration, die Kompatibilität mit der verwendeten Unity-Version und mögliche Anpassungen selbst geprüft werden müssen.

**Copyleft**\
Die Standard Unity Asset Store EULA enthält keine Copyleft-Pflicht. Der eigene Projektcode muss durch die Nutzung des Assets nicht offengelegt oder unter derselben Lizenz veröffentlicht werden.

**Kompatibilität zwischen Lizenzen**\
Die Lizenz ist mit dem zweiten verwendeten Asset unter CC0 kompatibel. Es entstehen keine widersprüchlichen Offenlegungs- oder Weitergabepflichten. Wichtig ist jedoch, dass das Cute-Pet-Asset nicht als eigenständige Rohdatei oder als separates Asset-Paket weitergegeben wird. Unity weist darauf hin, dass lizenzierte Assets nicht separat weiterverbreitet werden dürfen, wenn sie dadurch aus dem Projekt herausgelöst nutzbar wären (Unity Support, 2025a).

**Einfluss auf das Projekt**Das Asset darf im *Isor's Tower Prototype* verwendet und in einen späteren Build eingebettet werden. Es darf jedoch nicht separat weitergegeben, weiterverkauft oder in einem öffentlichen Repository als Rohdatei veröffentlicht werden. Für das Projekt bedeutet das, dass bei einer späteren Veröffentlichung darauf geachtet werden muss, dass das Asset nur als eingebetteter Bestandteil des Spiels enthalten ist.

## Ultimate Stylized Nature Pack -- Quaternius

Quaternius, 2022. *Ultimate Stylized Nature Pack*. \[online\] Verfügbar unter: <https://quaternius.com/packs/ultimatestylizednature.html> \[Zugegriffen 06.06.2026\].

**Lizenztyp**\
Das „Ultimate Stylized Nature Pack" steht unter der Creative Commons Zero Lizenz (CC0). Laut Asset-Seite enthält das Pack 63 Modelle in den Formaten FBX, OBJ, glTF und Blend und darf für private und kommerzielle Projekte verwendet werden (Quaternius, 2022).

**Attribution**\
Bei CC0 ist grundsätzlich keine Namensnennung erforderlich. Creative Commons beschreibt CC0 als Möglichkeit, Werke so weit wie rechtlich möglich zur freien Nutzung bereitzustellen (Creative Commons, no date a). Obwohl keine Attribution notwendig ist, wird Quaternius im TDD freiwillig als Quelle genannt.

**Commercial / Private Use**\
Das Asset darf sowohl privat als auch kommerziell verwendet werden. CC0 erlaubt das Kopieren, Verändern, Verbreiten und Verwenden des Materials auch für kommerzielle Zwecke, ohne vorher eine zusätzliche Erlaubnis einholen zu müssen (Creative Commons, no date a).

**Gewährleistung**\
Auch bei CC0 besteht keine Gewährleistung. Die Assets werden ohne Garantie bereitgestellt. Für das Projekt bedeutet das, dass selbst geprüft werden muss, ob die Modelle korrekt importiert werden können und technisch zur Projektstruktur passen.

**Copyleft**\
CC0 enthält keine Copyleft-Pflicht. Eigener Code, eigene Szenen oder eigene Assets müssen durch die Nutzung des Nature Packs nicht offengelegt oder ebenfalls unter CC0 veröffentlicht werden.

**Kompatibilität zwischen Lizenzen**\
Die CC0-Lizenz ist mit der Standard Unity Asset Store EULA des Cute-Pet-Assets kompatibel. CC0 stellt keine zusätzlichen Anforderungen an das Projekt und erzeugt keine Pflicht zur Offenlegung oder Weitergabe eigener Inhalte. Dadurch entstehen keine Konflikte mit der restriktiveren Unity-Asset-Store-Lizenz.

**Einfluss auf das Projekt**\
Das Nature Pack kann sehr flexibel im Projekt verwendet werden. Die enthaltenen Natur- und Umgebungsobjekte dürfen integriert, verändert und für private oder kommerzielle Zwecke genutzt werden. Da keine Attribution und keine Copyleft-Pflichten bestehen, entstehen nur geringe lizenztechnische Einschränkungen für das Projekt.

## Moon 002 -- 3dtextures.me

3dtextures.me, 2025. *Moon 002*. \[online\] Verfügbar unter: <https://3dtextures.me/2025/02/18/moon-002/> \[Zugegriffen 11.08.2026\].

**Lizenztyp**\
Das Texturpaket „Moon 002" wird über 3dtextures.me unter der Creative Commons Zero Lizenz (CC0) angeboten. Verwendet werden die Karten für Farbe, Normalen, Ambient Occlusion, Rauheit und Höhe (3dtextures.me, 2025).

**Attribution**\
Bei CC0 ist eine Namensnennung nicht erforderlich. Der Anbieter weist darauf hin, dass lediglich die Urheberschaft nicht für sich beansprucht werden darf. Die Nennung erfolgt hier freiwillig, um die verwendeten Fremdinhalte nachvollziehbar zu machen.

**Commercial / Private Use**\
Die private und die kommerzielle Nutzung sind uneingeschränkt zulässig.

**Gewährleistung**\
Es besteht kein Anspruch auf Fehlerfreiheit, Support oder Schadensersatz. Die Prüfung der Eignung für den eigenen Einsatzzweck liegt beim Nutzer.

**Copyleft**\
CC0 enthält keine Copyleft-Pflicht. Der eigene Projektinhalt muss nicht unter dieselbe Lizenz gestellt werden.

**Kompatibilität zwischen Lizenzen**\
CC0 ist mit allen weiteren im Projekt verwendeten Lizenzen vereinbar. Es entstehen keine widersprüchlichen Bedingungen.

**Einfluss auf das Projekt**Die Texturen dürfen im *Isor's Tower Prototype* verwendet und in einen Build eingebettet werden. Das dem Paket beiliegende Vorschaubild trägt ein Wasserzeichen und wird deshalb nicht als Textur eingesetzt.

## Ground082S -- ambientCG

ambientCG, o. J. *Ground082S*. \[online\] Verfügbar unter: <https://ambientcg.com/view?id=Ground082S> \[Zugegriffen 11.08.2026\].

**Lizenztyp**\
Die Bodentextur „Ground082S" wird über ambientCG unter der Creative Commons Zero Lizenz (CC0) angeboten. Verwendet werden die Karten für Farbe, Normalen, Ambient Occlusion und Rauheit in der Auflösung 2K (ambientCG, o. J.).

**Attribution**\
Der Anbieter stellt seine Inhalte ausdrücklich ohne Pflicht zur Namensnennung bereit. Die Nennung erfolgt hier freiwillig.

**Commercial / Private Use**\
Die private und die kommerzielle Nutzung sind uneingeschränkt zulässig.

**Gewährleistung**\
Es besteht kein Anspruch auf Fehlerfreiheit, Support oder Schadensersatz.

**Copyleft**\
CC0 enthält keine Copyleft-Pflicht.

**Kompatibilität zwischen Lizenzen**\
CC0 ist mit allen weiteren im Projekt verwendeten Lizenzen vereinbar.

**Einfluss auf das Projekt**\
Die Textur darf im Projekt verwendet und in einen Build eingebettet werden. Von den angebotenen Formaten kommen nur die für Unity benötigten Karten zum Einsatz. Die Normalen liegen in der OpenGL-Fassung vor, da Unity dieser Konvention folgt.

## Grass 05 -- freestylized

freestylized, o. J. *Grass 05*. \[online\] Verfügbar unter: <https://freestylized.com/material/grass_05/> \[Zugegriffen 11.08.2026\].

**Lizenztyp**\
Die Grastextur „Grass 05" wird über freestylized.com unter einer Royalty Free License angeboten. Auf der Seite der Textur ist sie mit dem Hinweis versehen, die Nutzung sei für alle kommerziellen und nicht kommerziellen Zwecke frei. Die Textur wurde prozedural mit Substance Designer erzeugt und wird in der Auflösung 2K verwendet (freestylized, o. J.).

**Attribution**\
Eine Namensnennung wird nicht verlangt. Der Anbieter bezeichnet sie als erwünscht, macht sie jedoch nicht zur Bedingung. Die Nennung erfolgt hier freiwillig.

**Commercial / Private Use**\
Beides ist nach der Lizenzangabe ausdrücklich zulässig.

**Gewährleistung**\
Zur Gewährleistung trifft der Anbieter keine Aussage. Es ist daher von keinem Anspruch auf Fehlerfreiheit oder Support auszugehen.

**Copyleft**\
Die Lizenz enthält keine Copyleft-Pflicht. Der Anbieter beschreibt sie an anderer Stelle als angepasste CC0-Lizenz, die eine zusätzliche Einschränkung enthält: Die Weitergabe der Inhalte über andere Plattformen oder Marktplätze ist untersagt, sofern sie nicht wesentlich verändert wurden. Auf der Seite der Textur selbst wird diese Einschränkung nicht genannt.

**Kompatibilität zwischen Lizenzen**\
Die Lizenz stellt keine Bedingungen, die den übrigen im Projekt verwendeten Lizenzen widersprechen. Ein gemeinsamer Einsatz ist damit möglich.

**Einfluss auf das Projekt**\
Die Textur darf im Projekt verwendet und in einen Build eingebettet werden. Die genannte Einschränkung greift erst, wenn die Textur als eigenständige Datei über eine andere Plattform angeboten würde. Das ist nicht vorgesehen, sodass sich für das Projekt keine Auswirkung ergibt.

## Lizenzvergleich und Auswirkungen auf das Projekt

Die beiden Assets besitzen unterschiedliche Lizenzarten. „Cute Pet" verwendet die Standard Unity Asset Store EULA mit dem Lizenztyp „Single Entity", während das „Ultimate Stylized Nature Pack" unter CC0 steht. Dadurch unterscheiden sich besonders die Weitergaberechte der Rohdateien.

Das Cute-Pet-Asset darf im Projekt verwendet und in Builds eingebettet werden, darf aber nicht separat als Rohdatei oder Asset-Paket weitergegeben werden. Das Ultimate Stylized Nature Pack ist durch CC0 deutlich freier nutzbar und darf grundsätzlich auch verändert und weiterverbreitet werden. Beide Lizenzen enthalten keine Copyleft-Pflichten, wodurch der eigene Projektcode nicht offengelegt werden muss.

Für den *Isor's Tower Prototype* bedeutet das, dass beide Assets gemeinsam verwendet werden können. Die wichtigste Einschränkung betrifft das Cute-Pet-Asset: Dieses darf bei einer späteren Veröffentlichung nicht aus dem Projekt herauslösbar weitergegeben werden. Das Nature Pack kann dagegen frei in die Spielwelt integriert und angepasst werden.

Neben den beiden Modellpaketen kommen drei Texturpakete zum Einsatz. Zwei davon stehen unter CC0 und sind damit rechtlich am freizügigsten. Das dritte, „Grass 05", steht unter einer Royalty Free License. Für die Nutzung im Projekt bleibt dieser Unterschied folgenlos, weil beide Lizenzformen die kommerzielle Verwendung und das Einbetten in einen Build erlauben. Bedeutsam würde er erst, wenn einzelne Assets aus dem Projekt heraus weitergegeben werden sollen: Bei CC0 wäre das zulässig, bei der Royalty Free License nicht ohne wesentliche Änderung.

Neben den externen Assets wurde eine Textur mit Hilfe einer künstlichen Intelligenz erzeugt. Es handelt sich um die Farbtextur der Grasbüschel, die über ChatGPT erstellt und anschließend im Projekt weiterverwendet wurde. Sie ist damit kein Fremdasset im lizenzrechtlichen Sinn und in der Übersicht der verwendeten Assets nicht aufgeführt. Sie wird hier gesondert ausgewiesen, weil es sich nicht um eine vollständig eigene Erstellung handelt.

## Quellen

3dtextures.me, 2025. *Moon 002*. \[online\] Verfügbar unter: <https://3dtextures.me/2025/02/18/moon-002/> \[Zugegriffen 11.08.2026\].

ambientCG, o. J. *Ground082S*. \[online\] Verfügbar unter: <https://ambientcg.com/view?id=Ground082S> \[Zugegriffen 11.08.2026\].

freestylized, o. J. *About us*. \[online\] Verfügbar unter: <https://freestylized.com/about-us/> \[Zugegriffen 11.08.2026\].

freestylized, o. J. *Grass 05*. \[online\] Verfügbar unter: <https://freestylized.com/material/grass_05/> \[Zugegriffen 11.08.2026\].

Quaternius, 2022. *Ultimate Stylized Nature Pack*. \[online\] Verfügbar unter: [https://quaternius.com/packs/ultimatestylizednature.html](https://quaternius.com/packs/ultimatestylizednature.html) \[Zugegriffen 06.06.2026\].

SURIYUN, 2025. *Cute Pet*. \[online\] Verfügbar unter: [https://assetstore.unity.com/packages/3d/characters/animals/mammals/cute-pet-96976](https://assetstore.unity.com/packages/3d/characters/animals/mammals/cute-pet-96976) \[Zugegriffen 06.06.2026\].

Unity Technologies, 2024. *Asset Store Terms of Service and EULA*. \[online\] Verfügbar unter: [https://unity.com/legal/as-terms](https://unity.com/legal/as-terms) \[Zugegriffen 06.06.2026\].

# Fazit:

Zum Abgabezeitpunkt liegt ein spielbarer Prototyp vor, der die Themen des Semesters in einem gemeinsamen Projekt zusammenführt: eine prozedural erzeugte Spielwelt mit Gelände, Wasser und Bepflanzung, ein Editor-Tool zur Erzeugung dieser Welt, ein komponentenbasierter KI-Prototyp mit Zustandsmaschine und Herdenverhalten, ein Tag-Nacht-System, Shader und Partikeleffekte sowie eine über eine Messreihe belegte Optimierung der Platzierung.

Fachlich tragen drei Ergebnisse über das Semester hinaus. Erstens hat sich beim Threading gezeigt, dass die Auswahl der zu optimierenden Stelle wichtiger ist als die Umsetzung: Der erste Versuch parallelisierte einen Abschnitt, der nur rund sechzehn Prozent der Laufzeit ausmachte, und blieb deshalb wirkungslos. Erst das Umbauen der teuren, bis dahin sequenziellen Stelle brachte den Gewinn. Zweitens hat sich die zusätzliche Zwischenmessung ausgezahlt, weil sie den Effekt der geänderten Datenanordnung vom Effekt der Parallelisierung trennt -- ohne sie wäre der gesamte Gewinn falsch zugeordnet worden. Drittens zeigte der bewusst zurückgenommene Optimierungsversuch, dass eine plausible Annahme über den Programmablauf durch eine Messung widerlegt werden kann und erst die Messung die Entscheidung trägt.

Ebenso bewährt haben sich die Entwurfsentscheidungen: Die Trennung nach dem MVP-Muster hält das Editor-Tool von der Pipeline fern, das Strategy-Muster bei der Platzierungsdichte erlaubt neue Verfahren ohne Eingriff in den Placer, und die komponentenbasierte Aufteilung des KI-Prototyps macht einzelne Fähigkeiten einzeln prüfbar. Der Preis dieser Struktur ist eine höhere Anzahl kleiner Klassen; im Gegenzug ließ sich jeder Baustein für sich testen und austauschen.

Der Prototyp ist damit funktionsfähig, aber ausdrücklich nicht fertig. Die offenen Punkte lassen sich nach Bereichen ordnen.

**Audio**\
Der Prototyp enthält bislang keinen Ton. Es fehlen Geräusche für die Schafe, für das Feuer der Fackeln und für Schritte, Klanguntermalung im Hintergrund sowie Rückmeldung beim Bedienen der Menüs. Damit verbunden ist die Lautstärkeregelung: Das Optionsmenü ist vorhanden, aber noch nicht mit einer Tonausgabe verbunden.

**Benutzeroberfläche**\
Die Menüs sind funktional, aber gestalterisch unfertig. Offen sind die Schärfe der Schrift, ein aufgewertetes und auf Interaktionsziele reagierendes Fadenkreuz, die Gestaltung der Aufforderungsanzeige, das Ausblenden der Spielanzeige beim Pausieren sowie der saubere Wechsel zwischen Maus- und Tastatursteuerung. In der Spielanzeige fehlen inhaltliche Elemente wie die aktuelle Tageszeit, Lebenspunkte und eine Übersicht der gezähmten Schafe.

**Beleuchtung und Bildwirkung**\
Die Beleuchtung ist bisher nicht ausgearbeitet. Offen sind ein eigenes Mondlicht, das Setzen der Lichtquelle für die Himmelsberechnung, der Einsatz von Post Processing sowie Nebel für die Tiefenwirkung. Kleinere Fehler sind bekannt: Auf dem Gelände tritt ein unerwünschtes Glanzlicht auf, die Weitsicht der Kamera ist nicht an die Weltgröße gekoppelt, wodurch der Mond abgeschnitten wird, und das erzeugte Geländenetz besitzt keine Texturkoordinaten, was zu einer Warnung bei der Lichtberechnung führt.

**Spielwelt und Inhalt**\
Das Dorf ist erst in Ansätzen aufgebaut. Es fehlen weitere Herden, die Platzierung der Leuchtkäfer, Gegner im Umland sowie die Wegfindung, die erst nach dem endgültigen Geländestand berechnet werden kann. Ein Speichersystem ist nicht vorhanden; geplant ist eine Ablage des Weltzustands als Änderungsliste gegenüber dem erzeugten Ausgangszustand.

**Spielfigur**\
Die Spielfigur ist eine Testfassung mit einfacher Steuerung und wird derzeit durch eine Kapsel dargestellt. Der Prototyp läuft in der Ich-Perspektive; vorgesehen ist ein Umschalten zwischen Ich- und Verfolgerperspektive, wofür ein vollwertiges Figurenmodell mit Animationen benötigt wird.

**Darstellung der Vegetation**\
Das Gras wird über Instanzierung mit mehreren Detailstufen gezeichnet. Verbesserungswürdig sind die Modelle selbst, das Überblenden zwischen den Detailstufen, das Ausblenden nach Entfernung und die Sichtbarkeitsprüfung. Das Wasser benötigt eine feinere Abstimmung des Shaders, wünschenswert wäre eine steuerbare Fließrichtung. Allgemein sind die verwendeten Texturen und ihre Einstellungen noch nicht abschließend abgestimmt.

**Editor-Tool**\
Das Tool erfüllt seinen Zweck, ist aber in zwei Punkten ausbaufähig. Zum einen wird beim Aufsetzen auf das Gelände nur das oberste Objekt einer Prefab-Hierarchie ausgerichtet, sodass verschachtelte Objekte nicht korrekt sitzen. Zum anderen ließe sich die Laufzeit weiter senken, unter anderem durch einen Aufräumdurchgang an den Kachelrändern, an denen der Mindestabstand zwischen zwei Objekten derzeit unterschritten werden kann.

**Quelltext**\
Einzelne Methoden sind zu lang und sollten in Hilfsmethoden zerlegt werden; das gilt insbesondere für die Platzierung eines Objekttyps. Diese Methode ist zugleich das Messobjekt der Threadoptimierung, weshalb ein Umbau bewusst erst nach der Abgabe erfolgt. Weiterhin sollten unbenannte Zahlenwerte im Netzaufbau durch Konstanten ersetzt und die Reihenfolge der Member im Presenter vereinheitlicht werden. Bei den Komponenten des KI-Prototyps ist mehr Allgemeinheit sinnvoll: Die Herdenverwaltung ist derzeit auf Schafe zugeschnitten und sollte auch andere Tierarten aufnehmen können. Ein bekannter Leistungsfehler betrifft die Wahrnehmung der Schafe, die je Bild Speicher anfordert, statt einen wiederverwendeten Puffer zu nutzen.

Ein Wort zum Umfang dieses Dokuments. Das TDD ist nicht als einmalige Semesterabgabe angelegt, sondern begleitet den Prototyp über mehrere Semester und soll später als Grundlage für die Abschlussarbeit dienen. Aus diesem Grund werden auch Entscheidungen festgehalten, die für die aktuelle Aufgabenstellung nicht zwingend erforderlich wären, etwa verworfene Ansätze und die Begründung einzelner Zahlenwerte. Der Aufwand für die Dokumentation liegt zum Abgabezeitpunkt bei rund 51 Stunden und damit über dem, was der reine Umfang der Aufgaben verlangt. Diese Zeit ist bewusst investiert: Ein nachvollziehbar begründeter Stand lässt sich in einem späteren Semester weiterschreiben, eine nachträgliche Rekonstruktion dagegen kaum.

Insgesamt erfüllt der aktuelle Stand die Anforderungen der Modulaufgaben und bildet eine tragfähige Grundlage. Die aufgeführten Punkte sind keine Versäumnisse, sondern das Ergebnis einer bewussten Reihenfolge: Zuerst wurden die Systeme gebaut und messbar gemacht, die den weiteren Aufbau tragen. Die Ausgestaltung folgt darauf auf.

# Änderungsverlauf:

Die folgende Übersicht führt die inhaltlichen Änderungen am Dokument auf. Zusätzlich trägt jedes Kapitel den Stand seiner letzten Bearbeitung.

| Datum | Betroffene Kapitel | Änderung |
|---|---|---|
| 26.02.2026 | Gesamtdokument | Anlage des Dokuments, Titelseite und Erklärungen |
| 22.05.2026 | Architekturübersicht | Erstfassung zum KI-Prototyp Sheep und zum DayNightSystem |
| 06.06.2026 | Einleitung, Entwicklungsumgebung, Anforderungen | Projektziel, Werkzeugübersicht und allgemeine Anforderungen ergänzt |
| 08.06.2026 | Programmablaufplan, Asset Integration | Ablauf der Sheep-AI und Lizenzanalyse der beiden Modellpakete |
| 12.07.2026 | Zeitablaufplan | Abschnitt zur Simulation der Spielumgebung ergänzt |
| 07.08.2026 | Einleitung, Entwicklungsumgebung, Anforderungen, Zeitablaufplan | Beginn der Überarbeitung: Perspektive richtiggestellt, Unity-Version und Werkzeuge aktualisiert, Anforderungen um Weltgenerierung, Editor-Tool und Spielerinteraktion erweitert, Detailzeitpläne aus der Zeiterfassung ergänzt |
| 08.08.2026 | Architekturübersicht | DayNightSystem und KI-Prototyp gegen den aktuellen Stand geprüft und berichtigt; neu aufgenommen: prozedurale Weltgenerierung, Editor-Tool und Threadoptimierung |
| 09.08.2026 | Architekturübersicht, UML-Klassendiagramm, Programmablaufplan | Messreihe der Threadoptimierung als Tabelle ergänzt; Gliederung für die neuen Diagramme angelegt |
| 11.08.2026 | UML-Klassendiagramm, Programmablaufplan, Asset Integration | Diagramme eingefügt; Lizenzanalyse um die drei Texturquellen erweitert und die KI-erzeugte Textur gekennzeichnet; Fazit und Änderungsverlauf ergänzt |

  : []{#_Ref_Tab_Aenderungen .anchor}Tabelle Änderungsverlauf des Dokuments
