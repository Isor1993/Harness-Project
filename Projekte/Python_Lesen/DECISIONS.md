# DECISIONS.md — Entscheidungen Python-Lesekurs

Ownership: Nur Entscheidungen zum Python-Lesekurs — was entschieden
wurde, warum, und welche Alternativen verworfen wurden. Kein Plan (das
ist die ROADMAP dieser Schicht), kein Ereignis (das ist das LOG).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.



## 2026-08-31 — Python-Lesekurs als eigene Projekt-Schicht
Was: Ein täglicher Kurs (15–30 Minuten je Einheit) mit dem Ziel, Python
**lesen und verstehen** zu können — für die Arbeit bei Omega Robotik,
nicht fürs Studium. Er lebt als eigene Schicht `Projekte/Python_Lesen/`
mit ROADMAP (Themenplan), LOG (Kurs-Log) und dieser Datei.
Warum: Das Ziel gehört zum Job, nicht zu Uni oder Kern; eine eigene
Schicht ist als Ganzes herausnehmbar (`Kern/DOC_RULES.md`, Abschnitt
10). Der Tagesrhythmus passt zu Isors Woche: Mo–Do wenig Zeit — eine
kleine Einheit geht trotzdem; am Wochenende dürfen es mehrere sein.
Verworfen: Einordnung in die Uni-Schicht (falsches Thema); eine breitere
Schicht `Projekte/Omega_Robotik/` (kann später kommen, wenn mehr als der
Kurs anfällt); ein gemeinsames Design mit dem generischen Lern-Log —
Isor will für den Kurs einen eigenen, einfacheren Log, der Punkt
`Kern/ROADMAP.md → „Lern-Log einführen"` bleibt davon unberührt offen.

## 2026-08-31 — Einheitsformat: Lesen statt Schreiben
Was: Jede Einheit hat denselben Ablauf: (1) Claude liefert einen kurzen
Code-Ausschnitt als Datei unter `Einheiten/` (nie zum Abtippen),
(2) Isor erklärt in eigenen Worten, was der Code tut, (3) Claude prüft,
korrigiert und erklärt das eine neue Konzept des Tages — mit
Zahlenbeispielen und externen Diagrammen, mit dem Vergleich zu C# als
rotem Faden, (4) der Log-Eintrag wird geschrieben. Die Ausschnitte
werden mit dem Themenplan praxisnäher, Richtung Robotik-Alltagscode.
Warum: Das Jobziel ist Lesekompetenz, nicht Schreiben von null; Isor
kennt C# aus dem Studium, der Vergleich trägt das Neue. Dateien statt
Chat-Blöcke wegen der Lese-Rechtschreib-Schwäche.
Verworfen: klassische Schreibübungen ab leerer Datei (übt das Falsche
und kostet die knappe Tageszeit); Theorie zuerst, Code später (der Kurs
soll vom ersten Tag an an echtem Code hängen).

## 2026-08-31 — Kurs-Log ist das LOG.md der Schicht
Was: Der Kurs-Log ist keine eigene Datei, sondern `LOG.md` dieser
Schicht mit einem festen Einheiten-Format (dort definiert): je Einheit
Thema, Snippet, was Isor selbst gelesen hat, wo Hilfe nötig war, welche
Fehler oder Verwechslungen auftraten. Auslöser: das Ende jeder Einheit —
Claude schreibt den Eintrag, Isor bestätigt ihn. Zeugnisse über den Kurs
(`/harness:zeugnis`) lesen aus diesem LOG statt aus Erinnerung.
Warum: Eine Chronik mit Standardnamen erbt alle Chronik-Regeln, und
`pruefen.py` prüft die Datumsfolge mit; eine zweite Log-Datei daneben
beantwortete keine Frage, die das LOG nicht beantwortet
(`Kern/DOC_RULES.md`, Abschnitt 2). Der Auslöser „Ende der Einheit"
hängt an etwas, das ohnehin jedes Mal passiert — die größte Gefahr eines
Logs ist eine Pflicht, die einschläft.
Verworfen: eigene Datei `KURSLOG.md` (Doppelstruktur); Eintrag nur bei
Problemen (dann fehlt gerade das Belegte „lief allein", das ein Zeugnis
braucht).

## 2026-09-01 — Einheiten in der Mittagspause, vom Handy
Was: Die Einheiten laufen in Isors Mittagspause vom Handy aus. Die
Kurs-Session bleibt dafür dauerhaft offen; Isor schreibt hinein, sobald
es losgeht, und Claude legt dann los. Damit das am Handy lesbar ist,
zeigt Claude das Snippet zusätzlich direkt im Chat (nur zum Lesen — die
Datei unter `Einheiten/` bleibt die abgelegte Fassung), und Diagramme
zur Erklärung kommen als Artifact-Seite, die das Handy anzeigen kann.
Warum: Kein Anlauf verloren — Session öffnen, Ordner wählen und
Einlesen entfallen in der knappen Pause. Repo-Dateien sind am Handy
schlecht zu öffnen; die Nicht-abtippen-Regel betrifft Text, den Isor
weiterverwenden muss, nicht Code, den er nur liest.
Verworfen: je Einheit eine frische Session (Einstiegskosten jeden Tag);
Snippet nur als Repo-Datei (am Handy nicht greifbar).
