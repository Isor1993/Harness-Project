# DIAGRAM_RULES.md — Regeln für die erzeugten Diagramme

Ownership: Nur der Umgang mit den skriptgenerierten `.drawio`-Diagrammen —
Ablage, Arbeitsteilung, Bedienregeln, Prüfung. Die Begründung, warum
Diagramme erzeugt statt gezeichnet werden, steht in DECISIONS 2026-08-06;
was gebaut wurde, im LOG der jeweiligen Schicht.

## Ablage

**Der Ablageort folgt der Schicht, nicht dieser Datei.** Ein Diagramm,
das ein Projektsystem beschreibt, liegt beim Projekt; eines, das nur für
eine Abgabe entstand, bei der Uni. Hier steht das Verfahren, nicht der
Pfad — sonst wäre die Datei nach einem Semesterwechsel falsch und beim
Kopieren in ein anderes Projekt unbrauchbar.

Der jeweils geltende Ort steht in der ROADMAP bzw. den DECISIONS der
Schicht. Stand 2026-08-22 liegen die neun vorhandenen Quellen noch unter
`01_Uni\Semester_2\Diagramme_Quellen\`; der Umzug in die Projekt-Ablage
steht auf der Projekt-ROADMAP.

- Skripte: `C:\IsorBackup\05_Werkzeuge\Vorlagen\`
  - `uml_drawio.py` — Kästen, Sinnbilder, Linienarten, Erhalt der Handarbeit
  - `pruefer.py` — vergleicht ein Diagramm gegen den Quellcode
  - `diagramm_<name>.py` — ein Skript je Klassendiagramm
  - `ablauf_<name>.py` — ein Skript je Ablaufplan
  - `linienstaerke_setzen.py` — nur für **nicht** erzeugte Diagramme
- Sicherungen: `Diagramme_Quellen\_Sicherung\`
- Der Pfad im Skript ist verbindlich. Wird woanders gespeichert, liest das
  Skript beim nächsten Lauf die alte Datei — die Anordnung ist dann nicht
  weg, aber die Arbeit war vergeblich.

## Export aus draw.io

**Beim Export „Include a copy of my diagram" angehakt lassen.** Ein
`.drawio.png` trägt das XML dann eingebettet mit sich, und aus einem
scheinbar reinen Bild lässt sich die bearbeitbare Quelle wieder
herauslösen.

Der Beleg ist ein Beinahe-Verlust: Am 2026-08-06 existierten fünf
Diagramme nur noch als `.drawio.png`-Export. Sie waren nur deshalb zu
retten, weil diese Option angehakt war — das XML wurde herausgelöst und
liegt seither als eigene Quelle vor. Seitdem wird mit den `.drawio`-
Dateien gearbeitet, nicht mit der Browser-Fassung (Bedienregel 2).

## Arbeitsteilung
- **Claude** schreibt und pflegt die Skripte und führt sie aus. Inhalt,
  Vollständigkeit und Korrektheit der Member sind Maschinensache.
- **Isor** ordnet an: Kästen schieben, Linien führen, Beschriftungen
  zurechtrücken. Das Layout ist Menschensache.
- Ein Lauf des Skripts übernimmt die Anordnung. Das gilt aber nur unter
  den Bedienregeln unten.

## Bedienregeln (aus dem Praxisbetrieb 2026-08-08)
1. **Beim Ziehen eines Linienendes muss der Zielkasten aufleuchten.**
   Grün = fester Punkt, Blau = schwebend am Kasten — beides ist richtig.
   Leuchtet nichts, hängt das Ende an einer freien Koordinate. Eine solche
   Linie sieht verbunden aus, wandert aber nicht mit dem Kasten mit, und
   sie lässt sich keiner Klasse zuordnen: Ihre Führung geht beim nächsten
   Lauf verloren.
2. **Direkt in die Datei speichern, nicht in den Browser-Speicher.**
   Entweder draw.io Desktop, oder im Browser über *Open Existing Diagram →
   Device*. Per Drag & Drop geöffnete Dateien darf der Browser nicht
   zurückschreiben.
3. **Nicht zwischen zwei Dateien kopieren.** draw.io vergibt dabei neue
   Ids. Die Zuordnung läuft zwar über den Klassennamen und hält das aus,
   aber die Ids sind danach unlesbar.
4. **Datei schließen, bevor Claude ein Skript darauf laufen lässt.** Ein
   offenes Fenster arbeitet auf seinem eigenen Stand und schreibt beim
   Speichern darüber.

5. **Ein bewusst frei gelassenes Linienende muss auch im Skript frei sein.**
   Lässt du ein Ende schwebend am Kasten (blau, ohne festen Punkt), steht dazu
   nichts in der Datei — und dann greift beim nächsten Lauf die Vorgabe aus dem
   Skript und verschiebt das Ende. Claude erkennt den Fall daran, dass
   `kanten_lesen` für diese Kante keinen Andockpunkt meldet, obwohl das Skript
   einen setzt; die Vorgabe gehört dann dort heraus (aufgefallen 2026-08-11 am
   Zustandsdiagramm, fünf Kanten betroffen).

## Was ein Lauf erhält
Kastenpositionen, Linien-Wegpunkte, Andockpunkte und die Lage der
Multiplizitäts-Beschriftungen. Andockpunkte an einer Member-Zeile werden
auf den Kasten umgerechnet — optisch dieselbe Stelle, technisch stabil.
Nicht erhalten wird ein Ende ohne Verbindung (siehe Regel 1).

## Prüfung
- Jedes Skript ruft am Ende `pruefen`. **Der Abschnitt FEHLER muss leer
  sein** — dort steht, was im Diagramm dargestellt ist, aber im Code nicht
  existiert. Das ist immer zu beheben.
- Der Abschnitt ZUR ANSICHT listet öffentliche Member, die das Diagramm
  weglässt. Meist Absicht; einmal drüberlesen genügt.
- Der Prüfer vergleicht **nur Membernamen**. Er sieht nicht, ob die Pfeile
  stimmen, ob eine ganze Klasse fehlt oder ob die Struktur veraltet ist.
  „Null Fehler" heißt „nichts Erfundenes dargestellt", nicht „vollständig".
- Zweiter Lauf muss dieselbe Datei erzeugen. Tut er das nicht, stimmt
  etwas an der Zuordnung nicht.

## Ablaufpläne (zweiter Diagrammtyp, seit 2026-08-09)
- Sechs Sinnbilder nach DIN 66001: `start`, `ende`, `prozess`, `entscheidung`,
  `unterprogramm`, `ein_aus`. Bedienung, Ablage und Erhalt der Handarbeit sind
  dieselben wie bei den Klassendiagrammen — nur die Bausteine im Skript heißen
  `knoten` und `pfeil` statt `klasse` und `kante`.
- **Kein Prüferlauf.** Der Prüfer vergleicht Membernamen in Klassenkästen; ein
  Ablaufplan enthält Fließtext. Was er zeigt, ist von Hand gegen den Code zu
  lesen — die einzige Absicherung ist die Quellenangabe im Skriptkopf.
- Die Zuordnung läuft über die **Id** des Sinnbilds, nicht über seinen Text:
  „Ende" kommt in einem Plan mehrfach vor. Deshalb greift hier Bedienregel 3
  (nicht zwischen zwei Dateien kopieren) doppelt — mit neuen Ids ist die
  Anordnung weg.
- Erhalten wird zusätzlich die **Größe** eines Kastens. Ein von Hand
  verbreitetes Sinnbild schnurrt also nicht wieder auf die Vorgabe zusammen.
- Vereinfachungen gegenüber dem Code (zusammengefasste Schleifen, doppelte
  Prüfungen nur einmal gezeigt) gehören in den Skriptkopf. Sonst lässt sich im
  Prüfungsgespräch nicht sagen, ob eine Abweichung Absicht oder Fehler ist.

## Zustandsdiagramme (dritter Diagrammtyp)
- Skript-Muster `zustand_<name>.py`, Quelle `Zustand_<Name>.drawio`.
  Bisher genau eines: die Sheep-FSM (2026-08-11).
- Bedienung, Ablage und Erhalt der Handarbeit wie bei den Ablaufplänen.
- **Kein Prüferlauf.** Der Prüfer vergleicht Membernamen in
  Klassenkästen; ein Zustandsdiagramm enthält Zustandsnamen und
  Übergangsbedingungen. Gegenprüfung von Hand gegen die FSM-Klassen, die
  Quellenangabe im Skriptkopf ist die einzige Absicherung.
- Die Zuordnung läuft über die **Id** des Kastens, nicht über den Text —
  Zustandsnamen können sich wiederholen. Bedienregel 3 (nicht zwischen
  zwei Dateien kopieren) greift hier deshalb doppelt.
- An diesem Typ ist Bedienregel 5 aufgefallen (fünf Kanten betroffen):
  Ein bewusst frei gelassenes Linienende muss auch im Skript frei sein.

## Feste Darstellungsvorgaben
Zentral in `uml_drawio.py`, damit alle Diagramme gleich aussehen. Beim nächsten
Lauf eines Skripts greifen sie automatisch, ohne die Anordnung anzutasten.
- `LINIENSTAERKE = 2` — 1 ist zu dünn, sobald das Bild ins Dokument verkleinert
  wird (Isor 2026-08-08).
- `SPRUNG = jumpStyle=arc` — an jeder Kreuzung ein Bogen. Ohne ihn laufen zwei
  sich kreuzende Linien wie ein T ineinander, und man sieht nicht mehr, welche
  wohin gehört (Isor 2026-08-11).

## Beim Anlegen eines neuen Diagramms
- Andockpunkte gleich verteilen. Bekommen mehrere Kanten denselben Punkt
  (z. B. elf Vererbungspfeile auf eine Basisklasse), liegen sie exakt
  übereinander und müssen einzeln von Hand getrennt werden.
- Eine bestehende Vorgabe **nicht nachträglich ändern**, wenn das Diagramm
  bereits angeordnet ist: Die Änderung wirkt genau auf die Kanten, an denen
  nichts gespeichert ist, und verrückt sie.
- Faustzahl für die Lesbarkeit: bis ~17 Klassen je Diagramm. Darüber
  aufteilen.
