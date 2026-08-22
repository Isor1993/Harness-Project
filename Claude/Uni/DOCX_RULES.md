# DOCX_RULES.md — Regeln für das Arbeiten an Word-Dokumenten

Ownership: Nur der Umgang mit den `.docx`-Abgabedateien — Sicherung,
Arbeitsteilung, bekannte Fallen, Prüfung. Was im TDD steht, gehört in
ROADMAP.md und FEATURE_LOG.md; warum es so steht, in DECISIONS.md.

Entstanden aus dem Praxisbetrieb 2026-08-07 bis 2026-08-11 am TDD. Claude
schreibt Änderungen direkt in die Datei (DECISIONS 2026-08-07), und zwar über
das entpackte `word/document.xml` — nicht über Word.

## Vor jedem Eingriff
1. **Sicherung anlegen**, mit Zeitstempel und Zweck im Namen:
   `Arbeitsdateien\Sicherung\TDD Softwareplanung_JJJJ-MM-TT_HHMM_vor-Fazit.docx`
2. **Prüfen, ob Word die Datei offen hat** — eine Datei `~$…docx` im Ordner
   bedeutet: abbrechen. Word schreibt beim Speichern über alles hinweg.
3. **Immer vom Original ausgehen.** Bei einem Fehlversuch nicht auf dem
   halbfertigen Stand weiterbauen, sondern neu entpacken und die Schritte
   erneut laufen lassen. Deshalb gehört jeder Eingriff in ein Skript, nicht
   in eine Folge von Handgriffen.

## Arbeitsteilung
- **Claude:** Text, Struktur, Tabelleninhalte, Quellenangaben, Felder. Alles,
  was sich als Regel formulieren lässt.
- **Isor:** Layout. Seitenumbrüche, Zeilenabstände, Bildgrößen, Abschnitts-
  wechsel, Seitennummerierung. Das braucht Augenmaß und ist in Word ein Klick,
  per XML dagegen ein Ratespiel mit Renderdurchlauf.
- **Word selbst:** Verzeichnisse und Feldwerte. Claude setzt das Feldgerüst,
  Word füllt es bei `Strg+A`, `F9`.

## Fallen beim Suchen und Ersetzen
Alle vier sind aufgetreten, drei davon hätten Schaden angerichtet.

1. **Ein Suchbegriff kann mehrfach vorkommen und Verschiedenes bedeuten.**
   „26.02.2026" stand als Datum der Selbstständigkeitserklärung *und* als
   echtes Erfassungsdatum in einem Zeitplan. Vor jedem Ersetzen zählen und
   die Fundstellen ansehen; bei Mehrdeutigkeit über die Lage im Dokument
   eingrenzen (z. B. „vor der ersten Tabelle").
2. **`find` liefert das erste Vorkommen.** „Quaternius, 2022" steht im
   Lizenzkapitel und im Quellenverzeichnis — mit `find` landen neue Einträge
   an der falschen Stelle. Für das Ende des Dokuments `rfind` nehmen.
3. **`<w:t[^>]*>` passt auch auf `<w:tc>`.** Das Muster muss
   `<w:t(?:\s[^>]*)?>` lauten, sonst wird beim Ersetzen der halbe
   Tabellenzelleninhalt verschluckt.
4. **Eine Zelle kann mehrere Textelemente enthalten.** Word teilt Text an
   Rechtschreibmarken. Wer nur das erste ersetzt, bekommt „Moon 002Stylized
   Nature Pack". Also: erstes Element setzen, alle weiteren leeren.
5. **Fließtext ist über Runs zerstückelt.** Ein Begriff, den man im Fenster
   als Wort sieht, existiert im XML oft nicht als zusammenhängende Zeichen-
   kette. Für Ersetzungen über Run-Grenzen den Absatz als Ganzes einlesen,
   die Runs zu einem Text zusammensetzen und danach neu aufbauen.
6. **Beim Klonen einer Tabellenzeile trifft `count=1` immer dieselbe Zelle.**
   Wer die fünf Zellwerte in einer Schleife nacheinander mit
   `re.sub(..., count=1)` einsetzt, ersetzt jedes Mal wieder das *erste*
   Textelement — am Ende steht der letzte Wert in Spalte 1 und die Spalten 2
   bis 5 tragen noch den Mustertext. Stattdessen **ein** `re.sub` über alle
   Textelemente mit einer Ersetzungsfunktion, die die Werte der Reihe nach
   aus einem Iterator zieht (aufgetreten 2026-08-17 beim Nachtragen der
   Audiozeilen in Tabelle 9; im XML unauffällig, beim Nachzählen sofort
   sichtbar).

## Felder
- Beschriftungen und Verweise sind Felder (DECISIONS 2026-08-08). Neue
  Abbildungen deshalb nur über *Verweise → Beschriftung einfügen*.
- Ein neu eingefügtes Bild oder eine neue Tabelle **verschiebt alle Nummern
  danach**. Die Anzeige stimmt erst nach `Strg+A`, `F9`.
- Nummern sind positionsabhängig, nicht „die nächste freie": Ein Bild, das
  vorne eingefügt wird, bekommt eine niedrige Nummer, und alles dahinter
  rückt nach.
- Überschriften von Verzeichnissen brauchen `numId 0` und `outlineLvl 9`,
  sonst zählen sie als Kapitel und stehen im eigenen Inhaltsverzeichnis.

## Prüfung
Nach jedem Eingriff, in dieser Reihenfolge:
1. XML wohlgeformt (`ET.parse`) — fängt nur grobe Fehler.
2. Datei packen und **in Word öffnen, Felder aktualisieren, als PDF
   exportieren**. Öffnet Word die Datei, ist die Struktur in Ordnung.
3. **Die betroffenen Seiten als Bild ansehen.** Kein Schritt ist fertig, bevor
   das Ergebnis gesehen wurde — die drei schlimmsten Fehler dieser Sitzung
   waren im XML unauffällig und im Bild sofort sichtbar.
4. Zählen statt hoffen: Beschriftungen, Verweise und Tabellenzeilen gegen den
   erwarteten Stand prüfen.

## Formatvorgaben
Verbindlich ist `C:\IsorBackup\01_Uni\_Regelwerk\Allgemeine_Formatierungs-
vorgaben.pdf`. Zwei Punkte, die man leicht übersieht:
- **Seitennummerierung:** entweder durchgehend arabisch, oder römisch bis zum
  Ende der Verzeichnisse und ab Kapitel 1 neu mit 1 arabisch. Eine dritte
  Variante gibt es nicht.
- **Hauptkapitel erfordern stets einen Seitenumbruch.**
Zur Kennzeichnung von KI-erzeugten Inhalten steht dort nichts — diese Pflicht
kommt aus der Selbstständigkeitserklärung im Dokument selbst.
