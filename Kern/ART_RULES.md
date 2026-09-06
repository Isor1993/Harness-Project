# ART_RULES.md — Regeln für erzeugte Grafik-Assets

Ownership: Nur das Verfahren, mit dem Grafik-Assets entstehen — was vor dem
Bau feststehen muss, wie der Ablauf aussieht, welche Werkzeuge es gibt, wo
Ergebnis und Generator liegen und was gemessen wird. Nicht hier: die
`.drawio`-Diagramme (`Kern/DIAGRAM_RULES.md`), der Aufbau des Datenbaums
(`IsorBackup/RULES.md`), die Pfade dorthin (`Kern/PFADE.md`), der
Session-Ablauf im Allgemeinen (`Kern/WORKFLOW.md`). **Warum ein bestimmtes
Asset so aussieht, wie es aussieht, gehört in die DECISIONS-Datei der
Schicht** — hier steht nur, wie man dorthin kommt.
Format: Regeln tragen einen **Kurznamen** in Kursiv; verwiesen wird auf den
Namen, nie auf eine Nummer (`DOC_RULES.md`, Abschnitt 6).

Entstanden am 2026-09-06 aus der ersten Blender-Session (Grasbüschel in drei
LOD-Stufen). Die Belege unten stammen aus dieser Session; sie sind der Grund
für die jeweilige Regel, nicht Beiwerk.

---

## Womit gearbeitet wird

Blender läuft **ohne Fenster**, gesteuert per Python:
`blender --background --factory-startup --python <skript>`. Das Skript ist
die Quelle, nicht die `.blend`-Datei — es liegt in Git, eine geänderte Zahl
erzeugt in Sekunden ein neues Modell, und jeder Lauf ist wiederholbar.
`--factory-startup` gehört dazu: Ohne das greifen gespeicherte
Benutzereinstellungen ein, und der Lauf ist auf einem anderen Rechner ein
anderer.

**Claude sieht das Ergebnis.** Ein Render wird gelesen wie eine Datei; ein
Fehler in der Form fällt damit im selben Durchgang auf, in dem er entsteht.
Das ist der eigentliche Grund, warum der Weg trägt — nicht dass es beim
ersten Mal sitzt, sondern dass jede Runde Minuten kostet.

---

## Der Weg hängt vom Typ ab

| Typ | Weg | Was entsteht |
|---|---|---|
| 3D-Mesh | Blender headless, prozedural | vollständiges Asset samt Attributen und Export |
| Sprite, Icon, UI-Grafik | SVG von Hand, oder Pillow prozedural | vollständiges Asset |
| Gemaltes — Konzeptkunst, Charakter, Textur | **geht nicht** | ein genauer Prompt für ein Bildwerkzeug |

Die Weiche gehört an den **Anfang**, nicht in die Mitte. Beim dritten Fall
ist die Leistung die Übersetzung eines Vorbilds in messbare Merkmale —
Seitenverhältnisse, Winkel, Farbverläufe, Beleuchtungsart. Genau das, was
beim ersten Fall in Parameter fließt, fließt hier in Sprache.

---

## Was vor dem Bau feststehen muss

Ohne diese Angaben wird geraten, und Raten kostet ganze Runden.

| Angabe | Warum sie fehlt, wenn sie fehlt |
|---|---|
| **Referenzbild** | Ein Stilname ist keine Maßangabe |
| **Zielgröße in Metern** | „klein" ist keine Zahl |
| **Zielumgebung** | Cel-Shading und PBR verlangen entgegengesetzte Geometrie |
| **Was der Shader vom Mesh braucht** | Attribute lassen sich nicht nachrüsten, ohne den Generator umzubauen |
| **Budget oder Priorität** | entscheidet jede einzelne Formfrage |
| **Bestand** | vorhandene Assets liefern Maße, Attribute und Konventionen gratis |

**Das Referenzbild ist der wichtigste Posten.** Beleg: Am 2026-09-06 wurden
drei Formen gebaut und alle drei verworfen, solange nur „Genshin-Look" als
Vorgabe vorlag — Halme dreimal zu breit, Biegung dreimal zu stark, ein
großes Büschel statt vieler kleiner. Nach vier Screenshots saß es in einem
Durchgang. Ein Bild vorab hätte drei Runden gespart.

**Der Punkt zum Shader wird am leichtesten übersehen.** Ein Mesh muss
wissen, was später von ihm gelesen wird: Ein Windshader braucht eine
Höhenmaske je Ecke, ein Farbverlauf eine Koordinate, ein Phasenversatz eine
Zufallszahl je Teil. Wird das nachträglich bemerkt, ist nicht das Asset zu
ändern, sondern der Generator.

---

## Ablauf

1. **Bestand vermessen** — vorhandene Dateien auslesen statt nach ihrem
   Inhalt zu fragen. Dreieckszahlen, Maße, Attribute, Achsen.
2. **Referenz auswerten** — das Vorbild in Zahlen übersetzen:
   Seitenverhältnisse, Winkel, Anzahl, Farbwerte.
3. **Design entscheiden**, Punkt für Punkt, jede Weggabelung als Bild.
4. **Bauen.**
5. **Messen** — nicht anschauen und für gut befinden.
6. **Ablegen** — Ergebnis und Generator, getrennt.

---

## Bedienregeln

- ***Entscheiden vor Bauen.*** Erst steht das Design vollständig, dann wird
  gebaut. Beleg: Am 2026-09-06 musste Isor den Bau zweimal stoppen, weil
  Claude aus dem Vermessen ins Modellieren gerutscht war — beide Male,
  bevor die Form entschieden war.
- ***Bild vor Wort.*** Eine Formentscheidung wird als Bild vorgelegt, nie
  als Beschreibung. Geometrie lässt sich nicht in Worten wählen, und für
  Isor gilt das doppelt (`CLAUDE.md`, „Zeigen statt vorstellen lassen").
  Vier Varianten nebeneinander, mit den Kosten je Variante daneben.
- ***Messen statt schätzen.*** Wo eine Zahl getroffen werden muss, wird sie
  gemessen. Beleg: Eine Formel für die Halmbreiten lag bei einer von fünf
  Varianten um 42 Prozentpunkte daneben; drei automatische Messdurchläufe
  brachten alle fünf unter zwei Punkte.
- ***Rahmen prüfen.*** Nach jedem Render wird das Bild gelesen, bevor es
  ausgewertet wird. Beleg: Dreimal an einem Tag stand die Kamera falsch —
  Objekt abgeschnitten, Vergleichsstück außerhalb des Ausschnitts, Biegung
  genau zur Kamera und damit unsichtbar. Jedes Mal wäre die Auswertung
  falsch gewesen, nicht nur hässlich.
- ***Der Generator reist mit.*** Ein Asset ohne sein Skript ist tot — es
  lässt sich nicht mehr ändern, nur ersetzen. Beides wird abgelegt, auch
  wenn nur das Asset gebraucht wird.
- ***Verbrauchte Skripte bleiben liegen.*** Skripte, die nur Varianten zur
  Auswahl gestellt haben, werden nicht aufgehoben. Ihr Ergebnis steht als
  Parameter im Generator; das Skript selbst beantwortet keine Frage mehr.

---

## Werkzeuge

Sie liegen im Datenbaum unter `05_Werkzeuge\Vorlagen\Blender\`
(`Kern/PFADE.md` → `DATENBAUM`) — dieselbe benannte Ausnahme wie bei den
Diagramm-Skripten (`DIAGRAM_RULES.md`, Abschnitt „Ablage"): Sie bearbeiten
keine Harness-Dateien, sondern Dateien außerhalb des Repos.

| Werkzeug | Tut | Gilt für |
|---|---|---|
| `distance_test.py` | rendert ein Objekt in echter Bildschirmauflösung aus mehreren Entfernungen und misst seine Pixelgröße | jedes Mesh |
| `measure_variants.py` | zählt die Silhouettenfläche in Pixeln | jedes Mesh |
| `calibrate_widths.py` | Schleife aus messen, korrigieren, neu bauen, bis die Abweichung unter der Toleranz liegt | Muster übertragbar |
| `grass_variants.py` | erzeugt die Gras-Büschel in Varianten und LOD-Stufen | nur Gras |
| `variant_views.py` | Vorschau-Renders: Reihe und Fläche | nur Gras |

Die ersten drei sind der bleibende Ertrag: Sie beantworten „sieht man den
Unterschied" und „ist es gleich groß" mit Zahlen statt mit Meinung.

---

## Ablage

- **Assets** in die Asset-Library nach ihrer Herkunft
  (`IsorBackup/RULES.md`, Abschnitt „Baum") — Eigenes unter `Eigene\`.
- **Generatoren und Messwerkzeuge** zu den Werkzeugen, siehe oben.
- **Abgelöste Fassungen** wandern nach `99_Archiv\_Zu_Loeschen\<Datum>_<Anlass>\`.
  Gelöscht wird nur von Isor (`IsorBackup/RULES.md`).
- **Zwischenrenders** bleiben im Sitzungsordner und werden nicht abgelegt.

---

## Was gemessen wird

Bei einem Asset mit mehreren Detailstufen sind drei Größen zu belegen,
bevor es abgelegt wird:

- **Höhe und Ausdehnung** müssen über alle Stufen übereinstimmen. Weicht
  eine ab, springt das Objekt beim Umschalten.
- **Silhouettenfläche** in Pixeln, gemessen, nicht gerechnet. Toleranz
  drei Prozentpunkte.
- **Pixelgröße auf dem Schirm** bei den Entfernungen, an denen umgeschaltet
  wird. Erst diese Zahl sagt, ob ein Unterschied überhaupt sichtbar wird.

Die dritte Messung liefert zugleich die Umschaltabstände. Ein Unterschied,
der bei zwanzig Pixeln Objekthöhe verschwindet, braucht keine feinere Stufe.
