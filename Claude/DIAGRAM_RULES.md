# DIAGRAM_RULES.md — Regeln für die erzeugten Diagramme

Ownership: Nur der Umgang mit den skriptgenerierten `.drawio`-Diagrammen —
Ablage, Arbeitsteilung, Bedienregeln, Prüfung. Die Begründung, warum
Diagramme erzeugt statt gezeichnet werden, steht in DECISIONS 2026-08-06;
was gebaut wurde, im FEATURE_LOG.

## Ablage
- Quellen: `C:\IsorBackup\01_Uni\Semester_2\Diagramme_Quellen\`
- Skripte: `C:\IsorBackup\05_Werkzeuge\Vorlagen\`
  - `uml_drawio.py` — Kästen, Linienarten, Erhalt der Handarbeit
  - `pruefer.py` — vergleicht ein Diagramm gegen den Quellcode
  - `diagramm_<name>.py` — ein Skript je Diagramm
  - `linienstaerke_setzen.py` — nur für **nicht** erzeugte Diagramme
- Sicherungen: `Diagramme_Quellen\_Sicherung\`
- Der Pfad im Skript ist verbindlich. Wird woanders gespeichert, liest das
  Skript beim nächsten Lauf die alte Datei — die Anordnung ist dann nicht
  weg, aber die Arbeit war vergeblich.

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

## Beim Anlegen eines neuen Diagramms
- Andockpunkte gleich verteilen. Bekommen mehrere Kanten denselben Punkt
  (z. B. elf Vererbungspfeile auf eine Basisklasse), liegen sie exakt
  übereinander und müssen einzeln von Hand getrennt werden.
- Eine bestehende Vorgabe **nicht nachträglich ändern**, wenn das Diagramm
  bereits angeordnet ist: Die Änderung wirkt genau auf die Kanten, an denen
  nichts gespeichert ist, und verrückt sie.
- Faustzahl für die Lesbarkeit: bis ~17 Klassen je Diagramm. Darüber
  aufteilen.
