# DECISIONS.md — Entscheidungen Studium

Ownership: Nur Entscheidungen zum Studium — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.


## 2026-07-18 — PCG- und Engine-Tool-Aufgabe kombiniert
Was: Beide Uni-Aufgaben (ASSIGNMENT_PCG.md + ASSIGNMENT_TOOL.md) werden
mit einem Projekt erfüllt: die Terrain-Pipeline als prozedurale
Level-Generierung (PCG) plus ein Editor-Tool mit UI und mindestens einem
Design Pattern obendrauf (Engine-Tool). Bestückung nutzt vorhandene
Inhalte aus früheren Abgaben (Shader, Partikeleffekte wie
Glühwürmchen/Fackeln, vorhandene KI) und leicht beschaffbare Assets
(Haus fürs Start-Village, Bäume, Gras).
Warum: Spart Zeit, ergibt ein zusammenhängendes Spielprojekt; die
Aufgabenstellung erlaubt eigene Anwendungsfälle, Spawn-Inhalte sind frei
wählbar.
Verworfen: zwei getrennte Tools/Abgaben ohne gemeinsame Basis.

## 2026-08-07 — Claude bearbeitet die TDD-Datei direkt
Was: Änderungen am TDD schreibt Claude selbst in
`01_Uni\Semester_2\Arbeitsdateien\TDD Softwareplanung.docx`, nicht mehr als
Textblock zum Kopieren. Technisch wird nur `word/document.xml` als Text
verändert, alle übrigen Archivteile werden unverändert übernommen — Bilder,
Formatvorlagen und Beziehungen werden nicht angefasst. Vor jeder Änderung
entsteht eine Kopie unter `Arbeitsdateien\Sicherung\` mit Zeitstempel; nach
jeder Änderung wird geprüft, dass die Teilezahl gleich blieb und außer
`document.xml` nichts abweicht. Bedingung: Die Datei darf in Word nicht offen
sein. Bilder einfügen, Verzeichnisse erzeugen und Seitenumbrüche bleiben bei
Isor. Neue Aufzählungspunkte werden aus einem bestehenden Punkt derselben
Liste geklont, damit Nummerierung und Einrückung sicher stimmen.
Warum: Der Weg über Textblöcke kostete pro Kapitel zweimal Arbeit — Isor musste
einfügen, und Claude musste anschließend das ganze Dokument neu einlesen, um zu
sehen, was angekommen ist. Diese Volldumps waren der mit Abstand teuerste Posten
der Session. Direktes Schreiben spart sie vollständig. Dazu kommt Isors
Lese-Rechtschreib-Schwäche: Abtippen erzeugt Fehler, Kopieren aus dem Chat
schleppt Formatierung nach Word.
Die frühere Zurückhaltung („Claude fasst die .docx nicht an") bezog sich auf den
Verlust der 16 Abbildungen — der entstand aber durch Words Formatwechsel
zwischen `.odt` und `.docx`, nicht durch XML-Bearbeitung.
Verworfen: Textbausteine als `.txt` neben der Arbeitsdatei (ein Umweg mehr statt
weniger, von Isor nach einem Versuch abgelehnt); Blöcke im Chat mit
`Strg+Umschalt+V` (funktioniert, löst aber weder die Nacharbeit noch das
Wiedereinlesen).

## 2026-08-07 — Zeiterfassung im TDD tageweise, ohne Schätzspalte
Was: Die neuen Zeitkapitel 5.3 bis 5.6 führen eine Zeile pro Arbeitstag statt
pro Arbeitsschritt und haben nur noch vier Spalten — die Spalte „Geschätzte
Zeit" entfällt. Die Gliederung folgt den vier Work Items aus Grindstone
(`Semester2_PCG` 37:41, `Semester 2_Isor Tower` 27:24, `Thread Optimierung`
9:56, `SoftwarePlanung` 7:44, zusammen 82:45). PCG und Engine-Tool stehen in
einem gemeinsamen Kapitel.
Warum: Feiner aufzuteilen als gemessen wurde hieße, die Stunden innerhalb eines
Tages zu schätzen — erfundene Zahlen in einer Zeiterfassungstabelle. Die
Tagessumme ist gemessen, und was an dem Tag entstand, steht datiert im
FEATURE_LOG; damit ist jede Angabe belegt. Geschätzt wurde für diese Module
nichts, also steht dort auch nichts; die Methodenänderung wird im Fließtext
benannt statt kaschiert. PCG und Tool gemeinsam, weil das Tool die
Bedienoberfläche der Pipeline ist und jede Pipeline-Stufe ihre Bedienung sofort
mitbekam — eine getrennte Erfassung wäre nachträglich konstruiert.
Festgehalten wird außerdem, dass die Werte eine Untergrenze sind: Tutorials in
der Freizeit wurden nicht getrackt, und rund zehn Stunden Gras-Arbeit vom
04./05.08. liegen unter „Isor Tower", gehören fachlich aber zur PCG-Aufgabe.
Verworfen: Stunden nachträglich auf Einzelaufgaben verteilen; die Schätzspalte
mit nachgereichten Werten füllen; die Gras-Stunden ins PCG-Kapitel umbuchen
(hätte die Messung frisiert).

## 2026-08-08 — Beschriftungen und Verweise im TDD sind Word-Felder
Was: Alle 48 Beschriftungen wurden auf Zählfelder (`SEQ`) umgestellt und mit
einer Textmarke umschlossen; alle 39 Verweise im Fließtext („siehe Abbildung
19") wurden zu Verweisfeldern (`REF`) auf diese Marken. Vorher enthielt das
Dokument kein einziges Feld, alle Nummern waren getippt. Kontrolle: sichtbarer
Text vorher und nachher zeichengleich (85.453 Zeichen), kein Verweis ohne
Textmarke, Archivteile 56 → 56.
Warum: Die neuen Diagramme gehören in die Kapitel UML und Programmablaufplan,
die **vor** dem Shader-Kapitel stehen. Jedes eingefügte Diagramm hätte von Hand
31 Beschriftungen und 31 Verweise verschoben — bei jeder Einfügung neu. Zweiter
Grund: Abbildungs- und Tabellenverzeichnis lassen sich ohne Felder überhaupt
nicht erzeugen, und beide sind laut Formatierungsvorgaben Pflicht.
Isors eigener Versuch scheiterte an der Alles-oder-nichts-Eigenschaft: Ein
`SEQ`-Feld zählt nur andere `SEQ`-Felder, nie getippten Text. Eine einzelne
automatische Beschriftung zwischen 47 getippten wird deshalb korrekt als
„Abbildung 1" ausgewiesen und sieht dadurch kaputt aus.
Merkposten für die Bedienung: `Alt+F9` schaltet zwischen Feldfunktion und Wert
um — steht die Anzeige auf Feldfunktion, erscheinen alle Felder als Code,
inklusive der Seitenzahl in der Fußzeile. `Strg+A` und `F9` aktualisiert die
Werte.
Verworfen: nur die Beschriftungen umstellen und die 39 Verweise am Ende von Hand
prüfen (billiger, aber die Handarbeit fällt bei jeder Einfügung erneut an);
Umstellung erst nach dem Einfügen der Diagramme (dann käme die Umnummerierung
von Hand obendrauf).

## 2026-08-08 — TDD-Kapitel 6.3 nach Pipeline-Stufen statt nach Klassen
Was: Kapitel 6.3 ist in sieben Unterkapitel entlang der Pipeline gegliedert
(Überblick, Config, Heightmap, Plateau, Mesh, Placer, Gras-Rendering) statt in eine
Überschrift je Klasse wie in 6.1 und 6.2.
Warum: Eine Überschrift je Klasse hätte 24 Unterkapitel ergeben, und der Ablauf der
Pipeline — das eigentlich Erklärungsbedürftige — wäre in der Liste untergegangen.
Klassen werden innerhalb ihres Abschnitts genannt und erklärt.
Verworfen: 24 Einzelkapitel (konsistent zum Rest, aber unlesbar); drei getrennte
Hauptkapitel je Ordner (hätte die Pipeline als Zusammenhang zerschnitten).

## 2026-08-08 — Vier neue Diagramme für den Terrain-Ast, Sheep-System braucht keins
Was: Erzeugt wurden Terrain-Pipeline (5 Klassen), Platzierung (14, mit vollständig
dargestelltem Strategy-Muster), Gras-Rendering (8) und Editor-Tool (8, MVP von links
nach rechts lesbar). DayNightSystem und Sheep-FSM wurden neu erzeugt, die
handgezeichneten Vorgänger archiviert.
Warum: Die Tool-Aufgabe verlangt Klassendiagramm und Ablaufdiagramm, und für den
gesamten Terrain-Ast existierte keines. Vier statt zwei Diagramme, weil ein einzelnes
mit 25 Klassen unlesbar würde — das Sheep-Diagramm hat 17 und ist bereits voll.
`Sheep_System_UML` wurde ersatzlos archiviert: `Sheep_Komponenten` deckt es
vollständig ab und enthält sechs Klassen mehr.
Verworfen: alle alten Diagramme sofort neu erzeugen (Prüfung zeigte nur einen harten
Fehler; die Zeit gehört in die fehlenden Pflichtdiagramme).

## 2026-08-09 — Messreihe als Tabelle mit 10-pt-Schrift
Was: Die Messreihe in TDD 6.5 steht zusätzlich als Tabelle (sechs Messpunkte,
Spalten Erzeugen/Filtern, Ausschluss, Zellbau, Gesamt, Verbesserung). Tabellenschrift
10 pt statt der 12 pt des Fließtextes.
Warum: Bei 12 pt passen sechs Spalten nicht auf die Satzbreite — Word trennt dann
mitten im Wort („Ausschlussfilte r"). Weiche Trennzeichen halfen nicht, Word zeigt
sie in dieser Datei durchgehend an. Spalten zu streichen hätte die Aussage gekostet:
Erst die Abschnittsspalten zeigen, dass der Gewinn zwischen den Messpunkten die
Stelle wechselt. Die Formatvorgaben regeln Fließtext (11–12 pt) und Beschriftungen
(9–11 pt), nicht den Tabelleninhalt.
Nebenwirkung: Die Tabelle steht vor der Asset-Tabelle und wird damit Tabelle 8; die
Asset-Tabelle rückt auf 9. Beide Nummern sind SEQ-Felder und rechnen beim
Aktualisieren selbst nach.

## 2026-08-11 — Fazit dreiteilig statt als Mängelliste
Was: Kapitel 13 des TDD gliedert sich in erreichten Stand, tragfähige Ergebnisse und
offene Punkte nach Bereichen. Der Aufwand von 51 Stunden Dokumentation wird benannt
und mit der mehrsemestrigen Nutzung begründet.
Warum: Isors Sammlung offener Punkte war vollständig, aber zu 95 % eine Mängelliste.
Die stärksten Ergebnisse des Semesters sind gedanklich — Amdahl als Auswahlkriterium,
die Zwischenmessung, der dokumentierte gescheiterte Versuch. Ein Fazit, das nur
Restarbeit aufzählt, verschenkt sie. Die offenen Punkte stehen weiterhin vollständig
drin, aber als Reihenfolge-Entscheidung statt als Versäumnis.

## 2026-08-11 — Lizenzkapitel: Quellen selbst nachlesen statt Notizen glauben
Was: Vor dem Schreiben von TDD 12.4 bis 12.6 wurden alle drei Anbieterseiten
aufgerufen. Ergebnis: zwei Korrekturen an dem, was in unseren Notizen stand.
Warum: In `_Nachladen.md` stand pauschal „alle genannten Quellen sind CC0". Für
freestylized stimmt das nicht — dort gilt eine Royalty Free License, und die
Einschränkung zur Weitergabe steht nur auf der About-Seite, nicht bei der Textur.
Zweitens war der Verdacht, die Bäume stammten aus dem falschen Quaternius-Pack, ein
Fehlalarm: Die beigelegte `License.txt` ist bei allen Packs dieselbe. Lehre: Eine
Lizenzanalyse ist genau die Stelle, an der eine übernommene Angabe nichts wert ist.

## 2026-08-11 — S4-Abgabe aus dem TDD als Formatvorlagen-Spender gebaut
Was: Die verlorene Word-Fassung der S4-Aufgabe wurde neu erzeugt, indem alle Teile des
TDD-Pakets außer `document.xml` übernommen wurden — Formatvorlagen, Schrift, Fußzeile,
Nummerierung. Der Text kam wortgetreu aus der abgegebenen PDF.
Warum: So sieht die Abgabe ohne Nacharbeit aus wie das TDD, und es entsteht keine
zweite Formatwelt. Inhaltlich geändert wurden nur die Quellenangaben: Das Sekundärzitat
Shaker et al. wurde zum Direktbeleg, die Calgary-Quelle stand mit Vornamen statt
Nachnamen und mit fremdem Titel im Verzeichnis, und die Einleitung von Übungstext 4
hatte gar keinen Beleg. Damit ist das Feedback der Fachbetreuung („1–2 mehr Quellen")
erfüllt, ohne den Text umzuschreiben.

## 2026-08-12 — Abgabe in zwei Ständen
Was: Es wird zweimal abgegeben. Stand 1 am So 16.08. ist vollständig und
benotbar, als gäbe es keinen zweiten Termin; Stand 2 am Mi/Do 19./20.08.
bringt nur noch Kleinigkeiten. Frist bleibt der 21.08.
Warum: Ein vollständiger früher Stand nimmt das Risiko aus der letzten Woche —
was am Sonntag liegt, kann nicht mehr schiefgehen. In der Woche darauf ist
ohnehin kaum Zeit, dort passen nur kleine Korrekturen.
Verworfen: einmal abgeben kurz vor der Frist (setzt alles auf einen Tag).

## 2026-08-12 — Spiel vor Dokumentation
Was: Do Ton, Fr UI, Sa Welt beleben und Abgabe-Material, So die gesamte
TDD-Restarbeit an einem Stück. Der frühere Plan hatte es umgekehrt.
Warum: Bis Samstag kommen Ton, UI und Beleuchtung dazu, die im Text stehen
müssen — ein früher Textstand beschreibt einen Stand, den es Sonntag nicht
mehr gibt. Zweitens ist der sichtbare Eindruck der schwächste Punkt des
Projekts (Zeugnis 2026-08-11: „die Systeme sind gut, aber sie zeigen sich
nicht"), und der Build entscheidet laut Vorgabe über die Funktionalitätsnote.
Verworfen: Textarbeit in die kurzen Abende legen und das Spiel ans Wochenende
(hätte doppelte Textarbeit erzeugt).

## 2026-08-12 — Neuer Abgabe-Satz statt Umbau des alten
Was: Der Endstand wird als eigener Ordner `Semester_2\Abgabe_Final\` nach
SAE-Vorgabe aufgebaut; die bestehenden Portfolio-Ordner unter `Abgabe\`
bleiben unangetastet. Die Unity-Projektkopie liegt einmal je Portfolio, nicht
je Aufgabe — die übrigen Aufgabenordner verweisen über den READ_ME-Baustein
„Folgende Aufgaben sind in anderen Ordnern zu finden".
Warum: Die alte Struktur ist der Beleg der formativen Abgaben und weicht in
drei Punkten von der Vorgabe ab (`Other` statt `other`, README je Aufgabe
statt einem READ_ME, keine Nummerierung). Getrennt aufbauen kostet nichts und
kann nichts zerstören. Die Kopie einmal je Portfolio spart 2 × 198 MB und hält
nur einen Stand nachziehbar.
Verworfen: die bestehenden Ordner an Ort und Stelle umbenennen; Projektkopie
je Aufgabenordner.

## 2026-08-12 — READ_ME knapp, Lizenzen als Tabellenzeile
Was: READ_ME der Abgaben sind Stichpunkte mit einem Ordnerbaum und den
Kriterien-Kürzeln je Aufgabe — kein Fließtext wie im ersten Semester. Neue
Audio-Quellen kommen als Zeilen in die Asset-Tabelle (Tabelle 9), nicht als
eigenes Unterkapitel.
Warum: Für die Bewertung zählt, dass der Prüfer die geforderten Punkte findet,
nicht wie ausführlich sie beschrieben sind. Eine Tabellenzeile mit Quelle und
Lizenz erfüllt den Nachweis vollständig; ein Unterkapitel je Sound würde den
Text doppeln.
Verworfen: Feature-Beschreibungen als Fließtext; Audio-Lizenzen als eigenes
Kapitel wie die Texturquellen in 12.1 bis 12.3.

## 2026-08-17 — Abgabe in zwei Uploads, erster Stand vollständig
Was: Am 17.08. wurden beide Portfolios vollständig gepackt und hochgeladen,
obwohl das Lernziel S3 noch offen ist. Ein zweiter Upload nach dem Polishing
ersetzt den ersten.
Warum: Ein vollständiger, benotbarer Stand auf dem Server nimmt das Risiko
aus den letzten vier Tagen. Was liegt, kann nicht mehr schiefgehen.
Verworfen: erst nach dem Polishing hochladen; nur eines der beiden Module
vorab abgeben.

## 2026-08-17 — KI-Kennzeichnung im TDD unter Tabelle 1
Was: Der Absatz zur KI-Nutzung steht unter der Beschriftung von Tabelle 1
(Entwicklungsumgebung), nicht auf der Titelseite und nicht als eigenes Kapitel.
Warum: Dort stehen Claude und ChatGPT ohnehin schon als Werkzeuge in der
Tabelle — der Leser trifft die Erklärung im Zusammenhang. Ein eigenes Kapitel
hätte alle Nummern dahinter verschoben.
Verworfen: Titelseite unter der Rechtevereinbarung (erste Umsetzung, von Isor
verworfen — wirkt dort deplatziert); eigenes Kapitel 15.

## 2026-08-17 — Keine KI-Kennzeichnung im S4-Dokument
Was: Die Ausarbeitung „Arbeiten nach akademischen Standards" bekommt keinen
KI-Hinweis.
Warum: Isor hat den Text vollständig selbst verfasst. Eine Erklärung über
Hilfsmittel, die nicht benutzt wurden, wäre schlicht falsch.
Verworfen: denselben Absatz wie im TDD einsetzen (von Claude vorgeschlagen).

## 2026-08-17 — Audiopakete als Block statt eigener Unterkapitel
Was: Die sieben Audiopakete stehen als Zeilen in Tabelle 9 plus ein Absatz
nach der Einleitung von Kapitel 12; sie bekommen keine eigenen Unterkapitel
wie die fünf Bild-Assets.
Warum: Alle sieben sind CC0 — dieselbe Antwort auf alle fünf Prüfpunkte.
Sieben fast gleiche Unterkapitel hätten den Text aufgebläht, ohne etwas zu
zeigen. Der Absatz steht bewusst vor der Tabelle, damit der Leser vorher
weiß, warum auf zwölf Assets nur fünf Unterkapitel folgen.
Verworfen: je Paket ein Unterkapitel; den Absatz unter die Tabelle setzen
(erste Umsetzung, von Isor verworfen).

## 2026-08-17 — Ältere Videos und TDD-Abbildungen bleiben in der Abgabe
Was: Die zu kurzen Entwicklungsvideos und die `Abbildung`-Screenshots bleiben
in den Aufgabenordnern, obwohl sie die Vorgabe für Press-Material verfehlen.
Das jeweilige Abgabevideo wird stattdessen im READ_ME benannt.
Warum: Isor will sie als Beleg behalten, falls etwas schiefgeht. Und in
Aufgabe 2 sind die Shader- und VFX-Graphen sogar die Antwort auf das
Feedbackelement „Lassen sich die Materialeigenschaften flexibel einstellen?".
Verworfen: sie ins Archiv verschieben (von Claude vorgeschlagen, zweimal).

## 2026-08-17 — Build vom 16.08. trotz geänderter Szene behalten
Was: In beiden `release`-Ordnern liegt der Build vom 16.08., obwohl die Szene
am 17.08. um 18:22 mit 21.354 platzierten Bäumen neu gespeichert wurde.
Warum: Der Build zeigt eine gültige generierte Welt und läuft; ein Neubau war
Isor den Aufwand nicht wert (Isor, 17.08.).
Verworfen: vor dem Zippen neu bauen, damit `src` und `release` denselben Stand
zeigen (von Claude empfohlen).

## 2026-08-19 — Balkendiagramm kommt nicht ins TDD
Was: Die Grafik der Messreihe wurde erzeugt, aber nicht in Kapitel 6.5 neben
Tabelle 8 eingesetzt. Das TDD bleibt unverändert.
Warum: Isor hält den Aufwand am Dokument für nicht lohnend; die verbleibende
Zeit geht in den Spielstand. Die Grafik erreicht die Bewertung trotzdem, weil
sie als `Messreihe_Balkendiagramm.png` im Messungs-Ordner der D003-Abgabe
liegt und im `Messreihen_README.md` genannt ist — dort, wo auch die sechs
Rohlogs liegen.
Verworfen: Einbau über `Verweise → Beschriftung einfügen` samt Querverweis
und F9-Durchlauf (von Claude empfohlen — die Aufgabenstellung nennt
visualisierte Performancedaten ausdrücklich, und die Dozentin hat am 18.08.
grafische Auswertungen gewünscht). Die Textbausteine dafür liegen fertig in
`Arbeitsdateien\Textbaustein_Abbildung_Messreihe.txt`, falls es doch noch
gemacht wird.

## 2026-08-19 — Zweiter Upload am Donnerstagabend, nicht heute
Was: Mi 19.08. und Do 20.08. wird gebaut, hochgeladen wird erst Do abends.
Warum: Ein zweiter Upload mit nur einem Feature lohnt den Aufwand nicht —
Build, beide `release`-Ordner, `src` nachziehen, zippen und hochladen kosten
rund zwei Stunden, unabhängig davon, wie viel drin ist. Der Freitag bis 20:00
bleibt als Puffer.
Risiko, bewusst getragen: Bis zum Upload ist Stand 1 vom 17.08. der einzige
bewertbare Stand. Fällt der Donnerstag aus, zählt nichts von dieser Woche.
Verworfen: heute Abend hochladen und morgen einen dritten Stand nachschieben.


## 2026-08-12 — Eigene Unity-Version trotz abweichender Vorgabe
Was: Das Projekt läuft auf `6000.5.2f1` und weicht damit von den beiden in
der Aufgabenstellung genannten Versionen ab.
Warum: Die Dozentin hat persönlich freigegeben, dass eine eigene Version
gewählt werden darf (Isor, 2026-08-12). Kein Handlungsbedarf — hier
festgehalten, falls die Abweichung später jemandem auffällt.
Verworfen: Rückbau auf eine der Vorgabe-Versionen.


## 2026-08-07 — Prefab-Painter wird im TDD nicht erwähnt
Was: Das Prefab-Painter-Werkzeug bleibt im Projekt und in der Projektkopie
der Abgabe (2026-08-11), wird im TDD aber nicht beschrieben.
Warum: Es gehört zu keinem der bewerteten Lernziele und hätte den
Textumfang ohne Gegenwert erhöht.
Verworfen: ein eigener TDD-Abschnitt dazu; ebenso, es aus der
Projektkopie zu entfernen.
