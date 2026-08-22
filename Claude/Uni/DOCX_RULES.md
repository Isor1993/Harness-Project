# DOCX_RULES.md — Regeln für das Arbeiten an Word-Dokumenten

Ownership: Nur der Umgang mit den `.docx`-Abgabedateien — Sicherung,
Arbeitsteilung, bekannte Fallen, Prüfung. Was im TDD steht, gehört in
`Uni/ROADMAP.md` und `Uni/LOG.md`; warum es so steht, in
`Uni/DECISIONS.md`.

Entstanden aus dem Praxisbetrieb 2026-08-07 bis 2026-08-11 am TDD. Claude
schreibt Änderungen direkt in die Datei (DECISIONS 2026-08-07), und zwar über
das entpackte `word/document.xml` — nicht über Word.

## Welche Datei

- **Arbeitsdatei ist ausschließlich**
  `01_Uni\Semester_2\Arbeitsdateien\TDD Softwareplanung.docx`.
  Nur diese anfassen; Sicherungen unter `Arbeitsdateien\Sicherung\`.
- **Ab Harness 1.0.0 gilt zusätzlich (E61b):** Der *Text* lebt in
  `Projekte/Isor_Tower/TDD.md`, die `.docx` ist die Abgabefassung und
  keine eigene Quelle. Solange das Werkzeug Markdown→`.docx` nicht
  gebaut ist (steht auf `Kern/ROADMAP.md`), bleibt die `.docx` führend
  und diese Regeln gelten unverändert.
- **Was wohin gehört**, steht in der Packliste
  `Arbeitsdateien\Abgabe_Packliste.txt` — die ROADMAP sagt *wann*, die
  Packliste sagt *was wohin*.

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

Die sechs dokumentierten Fallen stehen im Wissensarchiv:
`C:\Repos Isor\Knowledge\Werkzeuge\word-xml-fallen.md`.
Sie gelten für jedes Word-Dokument, nicht nur für die Abgabe — deshalb
liegen sie dort und nicht hier. **Vor jedem größeren Eingriff einmal
durchlesen.**

## Werkzeuge

- **docx-Skill** (im Harness vorhanden, im August benutzt): `validate.py`
  prüft ein gepacktes Dokument gründlicher als ein bloßer XML-Parse —
  **Prüfschritt 1 unten läuft darüber**. `soffice.py` wandelt nach PDF,
  wenn Word nicht zur Verfügung steht.
- **Word selbst** bleibt für Feldwerte und Verzeichnisse zuständig
  (`Strg+A`, `F9`) und für den PDF-Export mit aktualisierten Feldern.
- **Handarbeit am entpackten XML** bleibt nötig, wo gezielt in
  bestehenden Text eingegriffen wird — dafür gibt es kein Werkzeug.
- **Nur lesen, nichts ändern:** Ein `.docx` lässt sich per Python in
  reinen Text wandeln — `zipfile` auf `word/document.xml`, Absatz-Tags
  durch Zeilenumbruch ersetzen, den Rest strippen. Gebraucht wird das
  beim Zeugnis, das die Abgabedokumente liest, ohne sie anzufassen
  (`Kern/ASSESSMENT_RULES.md`, Belegpflicht). **Das Ergebnis gehört in
  den Scratchpad, nie ins Projekt.**

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
1. `validate.py` aus dem docx-Skill laufen lassen — prüft gründlicher als
   ein bloßer `ET.parse` und fängt auch Strukturfehler im Paket.
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
