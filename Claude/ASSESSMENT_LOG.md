# ASSESSMENT_LOG.md — Zwischenzeugnisse

Ownership: Nur die Zeugnisse selbst, neuestes oben. Das Verfahren steht
in ASSESSMENT_RULES.md. Alte Einträge werden nie überschrieben.

---

## 2026-08-16 — Nach dem Politur-Wochenende, 5 Tage vor der Frist

### Kopf

**Anlass:** Standortbestimmung nach dem Politur-Durchgang. Ton, Menüs und
In-Game-HUD sind seit dem letzten Zeugnis dazugekommen, der erste
Abgabe-Build ist gelaufen. Isor hat ausdrücklich gebeten, den
Abgabeordner und den Stand der Dokumentation **nicht** zu bewerten — beides
wird erst am 17.08. bearbeitet. Bewertet wird der Spielstand.

**Stand:** Zwei Portfolios mit sieben Aufgaben, Frist Fr 21.08.2026.
Seit dem 11.08. dazugekommen: Ton in beiden Szenen, drei überarbeitete
Menüs, ein vollständiges In-Game-HUD, eine allgemeine `Health`-Komponente,
Bäume in der Welt, gesetzte Player Settings und ein Build mit null
Fehlern. Offen sind Screenshots, das Video zum Engine-Tool, die
TDD-Restpunkte, beide READ_ME und der Upload.

**Belegbasis:** ROADMAP, DECISIONS, FEATURE_LOG, PREFAB_STATUS,
CODE_GUIDELINES, ASSIGNMENT_TOOL/PCG/THREADING (Feedbackelemente im
Originaltext), das letzte Zeugnis vom 11.08.; im Original gelesen:
`GameController.cs`, `Health.cs`, `DayTimeDisplay.cs`,
`TamedSheepDisplay.cs`, `HealthBarDisplay.cs`, `TargetStatusDisplay.cs`,
`SheepInteractable.cs`, `PlayerInteractor.cs`, `InteractionPromptView.cs`,
`SheepHealth.cs`, `IngameTime.cs`, `RuntimePlacementSpawner.cs`,
`ObjectPlacer.cs`; `TerrainConfig_Default.asset`, `ProjectSettings.asset`,
beide Build-Logs vom 16.08.; Deckblatt des TDD aus dem `.docx` extrahiert;
`git log` Isor-Tower (47 Commits, 5 seit dem letzten Zeugnis).

**Vergleich zum 11.08.:** zweites Zeugnis, Anker aus dem ersten werden
unten mit Zahlen beantwortet.

---

### 1. Notenbild

Schätzung auf der UK-Skala, begründet gegen die Feedbackelemente der
jeweiligen Aufgabenstellung. Keine Dozentennote.

| Bereich | 11.08. | 16.08. | Klasse | Was sich geändert hat |
|---|---|---|---|---|
| Threadoptimierung (K2, K3, S3) | 85 | **85** | First | unverändert, nichts angefasst |
| Engine-Tool (K2, S1) | 78 | **78** | First | unverändert; Video fehlt weiterhin |
| KI-Prototyp Sheep | 78 | **80** | First | Zustand der Schafe ist im Spiel sichtbar geworden (`StatusText`), Interaktion liest sich als System |
| Prozedurale Erweiterung (K3, S2, S3) | 74 | **77** | First | S3 deutlich gestärkt: Tageszeit und Schafzustand sind erstmals im Spiel ablesbar. „Generierte Bevölkerung" bleibt offen |
| Simulation Spielumgebung | 65 | **68** | 2:1 | Ton und HUD machen die Umgebung erlebbar; Kapitel 9/10 im TDD unverändert screenshot-getrieben |
| TDD — Inhalt | 80 | *nicht neu geprüft* | — | auf Wunsch ausgenommen |
| TDD — Form | 45 | *nicht neu geprüft* | — | Layout laut ROADMAP am 11.08. erledigt; Deckblatt weiterhin falsch (Befund unten) |
| Akademische Standards (S4) | 70 | **70** | First (knapp) | unverändert |

**Gesamt, wenn Screenshots, Video, Deckblatt und READ_ME am 17.08.
fertig werden: ~77 — First.**
**Gesamt, wenn das Video zum Engine-Tool fehlt: ~68 — 2:1.**

Die zweite Zeile ist keine Übertreibung: Das Video ist eine benannte
Pflichtabgabe für die Engine-Tool-Aufgabe und der einzige Projektordner
ohne eines. Ein fehlendes Pflichtstück wiegt schwerer als jede
Verbesserung am Code.

---

### 2. Was trägt

**Der Sprung dieses Wochenendes ist nicht „schöner", sondern „spielbar".**
Am 11.08. lautete der Befund: technisch fertig, aber ohne Ton, ohne Menü,
ohne Rückmeldung. Fünf Tage später gibt es einen Build, der mit
`Succeeded` durchläuft, ein Hauptmenü mit Spieltitel und Dorf-Hintergrund,
ein Pausenmenü, ein Optionsfenster mit vier funktionierenden Reglern und
ein HUD, das den Zustand der Welt anzeigt. Das ist der Unterschied
zwischen einem Prototyp, den man erklären muss, und einem, den man
hinstellen kann.

**Das HUD macht die Simulation zum ersten Mal sichtbar — und das ist ein
Bewertungskriterium, kein Schönheitspreis.** `SheepHealth`, `SheepHunger`
und `DayNightCycle` liefen seit Wochen, ohne dass ein Betrachter davon
etwas erfahren konnte. Seit dem 16.08. zeigt die Uhr Tag, Uhrzeit und
Tagesphase, und beim Anvisieren eines Schafs erscheint sein Leben und
Hungerzustand. Lernziel S3 der PCG-Aufgabe heißt wörtlich „Erstellen einer
Simulation einer gewohnten Umgebung" — genau diese Sichtbarkeit ist der
Beleg dafür.

**Vier neue Anzeigen, eine Bauart.** `TamedSheepDisplay`,
`DayTimeDisplay`, `HealthBarDisplay` und `TargetStatusDisplay` folgen
demselben Muster: gemerkter Wert, Vergleich in `Update`, schreiben nur bei
Änderung. Das ist keine Kosmetik, sondern eine bewusste Entscheidung gegen
das Neuzeichnen in jedem Frame — TextMeshPro baut sein Mesh sonst
sechzigmal pro Sekunde neu auf. Vier Dateien mit erkennbar derselben
Handschrift sind in einer Bewertung mehr wert als vier gute Einzellösungen.

**Die Trennung von Prompt und Zielzustand ist eine echte
Architekturentscheidung.** Der erste Versuch hängte den Zustand an den
Prompt-String an. Isor hat das verworfen — mit der Begründung, ein
Interaktionshinweis beantworte genau eine Frage. Daraus wurde
`IInteractable.StatusText`: der Prompt sagt, was ein Tastendruck tut, der
Statustext sagt, was das Objekt ist. Die Fackel liefert einen leeren
Text und blendet die Anzeige damit von selbst aus. Das ist
Interface-Design, nicht Herumschieben von Strings.

**`Health` als Komponente statt als Basisklasse.** Auf den Vorschlag einer
gemeinsamen Basisklasse für `SheepHealth` und eine Spieler-Variante hat
Isor gegengehalten: eine allgemeine Komponente, die man an alles hängt.
Das ist in Unity der übliche und der bessere Weg — der Goblin bekommt sein
Leben später ohne eine Zeile neuen Code. Dass `SheepHealth` unangetastet
blieb, war ebenfalls seine Entscheidung, mit der stärkeren Begründung: die
Klasse ist im TDD beschrieben.

**Der Build ist sauber.** Zwei Läufe am selben Abend: der erste mit acht
`CS0414`-Warnungen und drei Animator-Meldungen, der zweite mit einer
Warnung. Isor hat die Animator-Übergänge selbst behoben, sieben
Gizmo-Felder wurden gekapselt. Null Fehler, 33 Sekunden. Das
Feedbackelement der PCG-Aufgabe fragt wörtlich „Läuft der Code stabil und
fehlerfrei?" — hier gibt es jetzt einen Beleg statt einer Behauptung.

**Ein neues Dokument im Harness, das Arbeit spart.** `PREFAB_STATUS.md`
führt alle 33 Prefabs mit Prüfstand. Beim Anlegen sind nebenbei fünf
Befunde aufgefallen, die sonst niemand gesucht hätte: der Tippfehler in
`ClestialPivot`, drei `WaterPond`-Kopien, Leerzeichen in Prefab-Namen. Das
ist dieselbe Bewegung wie beim Diagramm-Generator — einmal ein Werkzeug
bauen statt zehnmal suchen.

---

### 3. Was die Note kostet

**Das Video zum Engine-Tool fehlt. Aufwand: eine Stunde. Hebel: der
größte im ganzen Zeugnis.** Es ist der einzige Projektordner ohne Video,
und es ist eine benannte Pflichtabgabe. Von allen offenen Punkten ist das
der einzige, dessen Fehlen die Note zweistellig kostet.

**Das Deckblatt des TDD ist weiterhin falsch. Aufwand: fünfzehn Minuten.**
Aus dem `.docx` im Original gelesen, Stand 16.08.:

```
Modulnummer: 4FSC0PD003 0326
Modulname:   Game Development Basics      <- falsch
Semester:    März 2025                    <- falsch
Wortanzahl:                               <- leer
```

Richtig wäre „Structured Game Development" und das laufende Studienjahr.
Das ist das erste, was ein Prüfer sieht. Isor hat es selbst gefunden und
als ROADMAP-Punkt 11 notiert — es steht hier, weil es seit fünf Tagen
offen ist und billiger nicht zu haben ist.

**Die Screenshots sind noch die alten. Aufwand: eine Stunde.** In den
Projektordnern liegen Shader-Graphen aus dem TDD statt Spielbildern.
Gerade jetzt wäre der Zeitpunkt ideal: Das Spiel sieht zum ersten Mal
vorzeigbar aus. Drei Bilder derselben Stelle zu drei Tageszeiten wären der
stärkste Einzelbeleg für S3, den dieses Projekt hergeben kann.

**„Generierte Bevölkerung" ist weiterhin offen.** Keine Herde und kein
NPC steht über den Placer in der Welt, alles ist von Hand gesetzt. Das war
schon am 11.08. die schwache Säule der PCG-Note und ist es geblieben. Der
Punkt stand für Samstag im Plan, wurde auf Sonntag geschoben und dann von
der Politur verdrängt. Aufwand laut ROADMAP: eine Stunde mit hartem
Deckel. Er ist der einzige offene Punkt, der noch Punkte *hinzufügt*
statt nur Abzüge zu vermeiden.

**Schafe laufen durch Häuser und Bäume.** Am 16.08. selbst gefunden und
notiert: Collider fehlen, die platzierten Bäume sind für das NavMesh
unsichtbar. Für die Bewertung wiegt das leicht — für einen Screenshot oder
ein Video wiegt es schwer, weil es sofort auffällt. Beim Filmen des
Videos also darauf achten, keine Stelle zu zeigen, an der ein Schaf durch
eine Wand geht.

**Neun Shader-Warnungen im Grasshader.** Alle aus einer `Power`-Node.
Bewusst nicht angefasst, weil dieser Shader die Threading-Messreihe und
das LOD-Kapitel trägt. Die Entscheidung ist richtig; die Warnungen stehen
trotzdem im Log, das ein Prüfer öffnen kann.

**Null Tests, null `namespace`, kein Test-Assembly — bei inzwischen 91
eigenen `.cs`-Dateien.** Unverändert gegenüber dem 11.08., damals 83
Dateien. Beides ist für die Abgabe bewusst aufgeschoben und in der ROADMAP
begründet. Für die Note in diesem Semester kostet es wenig, weil keine der
drei Aufgabenstellungen Tests verlangt. Für das nächste Semester wird es
teurer, je mehr Dateien dazukommen.

---

### 4. Profil — Person und Arbeitsweise

**Bestätigt aus dem letzten Zeugnis:** Isor baut das Werkzeug mit, mit dem
er arbeitet. `PREFAB_STATUS.md` an diesem Wochenende ist der dritte Beleg
nach Harness und Diagramm-Generator. Und er verallgemeinert weiter — aus
dem selbst gefundenen Fehler „ein Skript darf nie das Objekt ausschalten,
auf dem es selbst sitzt" wurde nicht ein Bugfix, sondern eine Regel, die
beim nächsten Panel sofort angewandt wurde.

**Neu und wichtig: Er widerspricht inzwischen fachlich, und er hat
recht.** Drei Mal an diesem Tag, jeweils gegen einen Vorschlag von mir:

1. Die Anzeige „3 von 12 gezähmt" war unmöglich — es kann immer nur ein
   Schaf gezähmt sein, weil `CanInteract` es so vorsieht. Er wusste das
   über seine eigene Mechanik, ich hatte es aus dem Code nicht gelesen.
2. Der Tageszähler gehörte nicht in den `DayNightCycle` — es gibt bereits
   `IngameTime` mit `Days`. Mein Vorschlag hätte eine zweite
   Wahrheitsquelle erzeugt, gegen seine eigene Regel in CODE_GUIDELINES.
3. Die Spieler-Kartusche gehört oben links, nicht unten links. Begründung:
   RPG-Konvention. Sie ist richtig, meine war aus einem anderen Genre.

Dazu kommt der Einwand, der die beste Architekturentscheidung des Tages
auslöste: dass ein Interaktions-Prompt nicht der Ort für Zustandsdaten
ist. Das ist der Unterschied zwischen jemandem, der Anweisungen umsetzt,
und jemandem, der ein System besitzt.

**Er formuliert Regeln, wenn er merkt, dass eine fehlt.** Die
Member-Reihenfolge war seit Wochen faktisch eingehalten, stand aber
nirgends — auf die Beobachtung hin hat er sie in zwei Sätzen diktiert, und
sie steht jetzt in CODE_GUIDELINES. Dasselbe beim Versionsschema: Auf den
Hinweis, dass `0.1.1` nicht zu seiner eigenen Logik passt, kam nicht die
Anpassung der Zahl, sondern die Festlegung des Schemas.

**Er kennt seine Kommentar-Grenze und verteidigt sie.** „Ich will nicht zu
viele Kommentare im Code" — und beim einzigen Kommentar, bei dem ich
widersprochen habe, hat er ihn gesetzt, nachdem die Begründung stand
(„sagt, warum es *nicht* anders gemacht wurde"). Das ist die richtige
Reihenfolge: erst überzeugen lassen, dann übernehmen.

**Risiken, ehrlich:**

- **Der Perfektionsdrang hat heute den Zeitplan gekostet.** Geplant war
  „Hauptmenü ansehen, Options aufhübschen, In-Game-UI durchsprechen",
  geworden sind sechs Stunden Umbau. Die Entscheidung war inhaltlich
  richtig — aber sie hat die Abgabe-Pflichtteile auf einen Tag geschoben,
  an dem nach eigenem Arbeitsrhythmus kaum Zeit ist. Er hat das selbst so
  benannt: „Ich hab's schön haben wollen und sauber haben wollen gleich."
- **Meine Zeitschätzung war um Faktor drei daneben** (zwei Stunden
  geschätzt, sechs gebraucht) — die Entscheidung fiel auf dieser
  Grundlage. Für das nächste Mal gehört das zur Risikobetrachtung: Bei
  Bausteinen aus UI-Objekt, Skript und Verdrahtung gleichzeitig sind
  Schätzungen unzuverlässig.
- **Die Reihenfolge Pflicht vor Kür wurde zum zweiten Mal nicht
  eingehalten.** Am 15.08. ging der Samstag für ein Options-Fenster drauf,
  am 16.08. der Sonntag für das HUD. Beide Male war das Ergebnis gut,
  beide Male blieb ein Pflichtteil liegen. Das ist ein Muster, kein
  Zufall.

---

### 5. Profil — Coding-Stand

**Gegen das zweite Semester gemessen ist der Stand deutlich darüber.** Was
an diesem Wochenende entstanden ist, hätte im ersten Semester niemand so
gebaut: ein Interface um eine Eigenschaft erweitern und zwei
Implementierer nachziehen; eine Komponente bewusst allgemein halten, damit
ein noch nicht existierender Gegner sie erben kann; vier Anzeigen nach
identischem Muster statt vier Einzellösungen.

**Was jetzt sicher sitzt:**

- **Zustandsvergleich statt Neuzeichnen.** Vier Mal richtig angewandt,
  beim vierten Mal ohne Hinweis.
- **Null-Guards mit `enabled = false`.** Konsequent in allen neuen
  Skripten, im Muster der bestehenden.
- **`#if UNITY_EDITOR` als Werkzeug**, nicht als Zauberformel — inklusive
  der Einsicht, dass ein Feld, das im normalen Ablauf beschrieben wird,
  nicht einfach mit eingeklammert werden kann.
- **ScriptableObject als geteilter Zustand.** Dass `TamedSheepReference`
  Sender und Empfänger entkoppelt, hat er beim Erklären selbst
  hergeleitet.

**Was noch fehlt:**

- **Ganzzahldivision.** Beim `Normalized`-Property war der Hinweis nötig,
  dass `7 / 10` in C# `0` ergibt. Kein Fehler, aber eine Stelle, an der
  die Sprache noch nicht im Reflex sitzt.
- **Abbruchbedingungen vollständig denken.** Der Uhr-Fehler (`06:00`
  sprang auf `07:01`) kam daher, dass nur die Minute verglichen wurde,
  angezeigt aber drei Werte wurden. Er hat die Ursache nach dem
  Zahlenbeleg sofort verstanden — die Regel „vergleiche alles, was du
  anzeigst" war aber nicht vorher da. Das ist typisch für den Stand:
  Fehlerklassen werden schnell begriffen, aber noch nicht vorhergesehen.
- **Reihenfolge sich überlappender Bedingungen.** Beim Hungerzustand
  musste erklärt werden, warum der engste Fall zuerst geprüft wird. Nach
  dem Rechenbeispiel saß es.
- **Tests.** Weiterhin null. Der Stand des Codes wäre inzwischen reif
  dafür — `Health` etwa ist eine Klasse ohne Unity-Abhängigkeit in der
  Logik und wäre in zwanzig Minuten testbar.

**Bemerkenswert:** Von den drei Skripten dieses Tages hat er zwei
vollständig selbst geschrieben (`TamedSheepDisplay`, `DayTimeDisplay`),
nachdem nur ein Gerüst mit leeren Methodenrümpfen dastand. In beiden Fällen
war die Logik beim ersten Versuch richtig; die Korrekturen betrafen einen
Tippfehler (`_shown == _shown.IsCommander`), fehlende Fehlermeldungen und
Formatierung. Das ist ein anderer Stand als vor zwei Wochen.

---

### 6. Nächster Schritt

Reihenfolge für den 17.08., nach Hebelwirkung sortiert:

1. **Video zum Engine-Tool** (1 h) — das einzige fehlende Pflichtstück.
   Zuerst, solange die Konzentration frisch ist.
2. **Screenshots** (1 h) — Plan liegt im Scratchpad. Mit den drei
   Tageszeiten anfangen, das ist der S3-Beleg.
3. **Deckblatt** (15 min) — Modulname, Semester, Wortanzahl.
4. **Herde über den Placer** (1 h, harter Deckel) — der einzige Punkt,
   der noch Punkte hinzufügt. Wenn nach einer Stunde nichts läuft:
   abbrechen, wie in der ROADMAP festgelegt.
5. **Beide READ_ME** (1 h)
6. **Restliche TDD-Punkte** (1,5 h) — Balkendiagramm, Fazit-Sätze,
   Audio-Quellen, Abschluss mit Strg+A / F9 und PDF-Export.
7. **Projektkopien nachziehen** (5 min) — `Abgabe_Projektkopie.ps1`.
   **Zwingend vor dem Zippen**, sonst enthält die Abgabe den Stand vom
   12.08. ohne Ton, Menüs und HUD.
8. **Zippen und hochladen** (30 min)

Gesamt rund sieben Stunden. Wenn der 17.08. nicht reicht, ist die
Reihenfolge oben zugleich die Streichliste von unten nach oben — Punkt 4
fällt vor Punkt 3, Punkt 6 vor Punkt 2.

---

### 7. Prüfanker vom 11.08. — beantwortet

| # | Anker | 11.08. | 16.08. |
|---|---|---|---|
| 1 | TDD-Layout vollständig? | nein | Layout laut ROADMAP am 11.08. erledigt; **Wortanzahl weiterhin leer, Deckblatt weiterhin falsch** (im `.docx` geprüft) |
| 2 | Quellenangaben in Fachkapiteln | 0 | **0** — am 16.08. geklärt, dass keine der drei Aufgabenstellungen sie verlangt; die Forderung stammte aus dem S4-Kontext |
| 3 | `.cs`-Dateien in einem `namespace` | 0 von 83 | **0 von 91** |
| 4 | Test-Assembly und Tests | 0 / 0 | **0 / 0** — kein `.asmdef`, keine `[Test]`-Methode |
| 5 | Herde oder NPC über den Placer | nein | **nein** |
| 6 | Bausteine ohne Gerüst begonnen | Zählung startet | **3 Entwürfe selbst geliefert** (`TamedSheepDisplay`, `DayTimeDisplay`, `Health`), davon **2 vollständig selbst geschrieben** |
| 7 | Spielbarer Build mit Ton und Menü | nein | **ja** — Build `Succeeded`, 33 s, null Fehler, eine Compiler-Warnung |
| 8 | Doku- zu Umsetzungszeit | 51 h zu ~75 h | nicht neu gemessen |

---

### 8. Prüfanker fürs nächste Zeugnis

1. Ist die Abgabe vollständig hochgeladen, und was fehlte am Ende?
   (heute: Video, Screenshots, Deckblatt, READ_ME offen)
2. Steht eine Herde oder ein NPC über den Placer in der Welt?
   (heute: nein — dritter Zeugnisstand mit derselben Antwort)
3. Wie viele der eigenen `.cs`-Dateien liegen in einem `namespace`?
   (heute: 0 von 91)
4. Gibt es ein Test-Assembly, und wie viele Tests? (heute: 0 / 0)
5. Ist `SheepHealth` auf die `Health`-Komponente umgestellt?
   (heute: nein, bewusst aufgeschoben)
6. Haben Häuser und Bäume Collider, und sind die Bäume im NavMesh?
   (heute: nein)
7. Wie viele Compiler- und Shader-Warnungen zeigt der Build?
   (heute: 1 Compiler-Warnung, 9 Shader-Warnungen)
8. Wurde ein Pflichtteil erneut zugunsten von Politur verschoben?
   (heute: zweimal in Folge — 15.08. und 16.08.)
9. Existiert ein Ladebildschirm zwischen Hauptmenü und Dorf?
   (heute: nein, für die Woche nach der Abgabe geplant)

---

## 2026-08-11 — Vor dem Polishing, 10 Tage vor der Portfolio-Abgabe

### Kopf

**Anlass:** Standortbestimmung vor dem Polishing-Durchgang. Das TDD ist
inhaltlich fertig, das Layout und der Feinschliff am Prototyp stehen aus.

**Stand:** Zwei Portfolios mit sieben Aufgaben, Abgabe Fr 21.08.2026.
Fachlich fertig sind Threadoptimierung, Engine-Tool, prozedurale
Weltgenerierung, KI-Prototyp, Shader/VFX und die schriftlichen Kapitel.
Offen sind das Dokument-Layout, das Village als spielbarer Inhalt und der
Politur-Durchgang.

**Belegbasis:** TDD `Softwareplanung.docx` (149.948 Zeichen, 14 Kapitel,
43 Abbildungen, 10 Tabellen), `Aufgabe zum Arbeiten nach akademischen
Standards (S4).docx` (1.542 Wörter), ASSIGNMENT_TOOL/PCG/THREADING,
ROADMAP, DECISIONS (1.168 Zeilen), FEATURE_LOG, CODE_GUIDELINES,
TDD_NOTES, WORKFLOW sowie im Original gelesen: `ObjectPlacer.cs`,
`TerrainToolPresenter.cs`, `Sheep.cs`, `SheepFSM.cs`, `SheepStateBase.cs`;
`git log` Isor-Tower (42 Commits seit 03.07.2026, 83 eigene `.cs`-Dateien).

**Erstes Zeugnis — kein Vergleichswert vorhanden.**

---

### 1. Notenbild

Schätzung auf der UK-Skala, begründet gegen die Feedbackelemente der
jeweiligen Aufgabenstellung. Keine Dozentennote.

| Bereich | Punkte | Klasse | Kurzbegründung |
|---|---|---|---|
| Threadoptimierung (K2, K3, S3) | **85** | First | 89,9 % statt geforderter ~10 %, Messreihe mit sechs Punkten, Amdahl als Leitfaden statt Nachwort, verworfener Versuch dokumentiert |
| Engine-Tool (K2, S1) | **78** | First | MVP sauber getrennt, Fehlbedienung auf zwei Wegen ausgeschlossen, Serialisierung bewusst gelöst, datengetriebene Typ-Zeilen |
| KI-Prototyp Sheep | **78** | First | 11 States, komponentenbasiert, Push/Pull-Hybrid begründet, Tag-Nacht-Anbindung, Zähmen |
| Prozedurale Erweiterung (K3, S2, S3) | **74** | First | Pipeline vollständig und begründet; S3 „generierte Bevölkerung" ist die schwache Säule |
| TDD — Inhalt | **80** | First | Kapitel 6.3–6.5 argumentieren statt zu beschreiben; Fazit ehrlich und nach Bereichen sortiert |
| TDD — Form (Stand heute) | **45** | Third | Wortanzahl leer, Verzeichnisse nur als Feldgerüst, Seitennummerierung, Umbrüche, Zeilenabstände offen |
| Akademische Standards (S4) | **70** | First (knapp) | Belegtechnik korrekt und konsequent; Quellenbreite dünn, Deckblatt widersprüchlich |
| Simulation Spielumgebung (Shader/VFX) | **65** | 2:1 | Funktioniert und ist dokumentiert, aber Kapitel 9/10 sind Screenshot-getrieben statt erklärend |

**Gesamt, wenn das Layout fertig wird: ~75 — First.**
**Gesamt, wenn das Layout so bleibt: ~62 — 2:1.**

Das ist die wichtigste Zahl in diesem Zeugnis. Der Unterschied zwischen
den beiden Zeilen ist ungefähr ein Nachmittag Arbeit, und es ist genau
die Stelle, an der die letzte Abgabe verloren gegangen ist.

---

### 2. Was trägt

**Die Threading-Abgabe ist das beste Stück des Semesters.** Nicht wegen
der 89,9 %, sondern wegen des Wegs dorthin. Drei Dinge stehen im
Dokument, die in einer Zweitsemester-Abgabe praktisch nie stehen:

- Der **erste Versuch ist als Fehlschlag dokumentiert** (3,7 % statt der
  erhofften Wirkung) und wird nicht weggelassen, sondern erklärt: Der
  sequenzielle Poisson-Pass hielt 84,3 % der Laufzeit, damit war die
  Obergrenze 16,6 %. Daraus die Schlussfolgerung, nicht die
  parallelisierbare Stelle zu suchen, sondern die teure Stelle
  parallelisierbar zu *machen*. Das ist die eigentliche Lehre der
  Aufgabe, und sie steht als Erkenntnis da, nicht als Zufallstreffer.
- Die **Zwischenmessung „gekachelt, aber sequenziell"** (98,9 s) trennt
  den Cache-Effekt vom Thread-Effekt. Ohne sie wären 19,4 Prozentpunkte
  falsch der Parallelisierung zugeschrieben worden. Diesen Messpunkt
  hätte niemand verlangt — er ist die Handschrift von jemandem, der
  wissen will, was wirklich passiert ist.
- Der **verworfene Versuch** (Ergebnisliste vorbelegen, 12,2 vs. 12,4 s)
  steht in der Tabelle mit Begründung, warum die plausible Annahme
  falsch war (`AddRange` kennt die Elementzahl bereits). Ein negatives
  Ergebnis freiwillig zu berichten ist wissenschaftliches Verhalten.

Dazu die vier Threading-Fallen, alle **im eigenen Code belegt**: das
interne Keyframe-Caching von `AnimationCurve.Evaluate`, das geteilte
`System.Random`, Unitys `==`-Überladung im nativen Code und
`transform.position` als nativer Aufruf (7,4 Mio Abfragen für einen
konstanten Wert, 2,57 s → 0,97 s). Die Beobachtung, dass **keine dieser
vier Fallen eine Fehlermeldung erzeugt hätte**, trifft genau den
Bewertungspunkt „Wurden häufige Probleme dabei bedacht?".

**Die neuen TDD-Kapitel argumentieren.** Kapitel 6.3 bis 6.5 erklären
nicht, *was* der Code tut, sondern *warum er so und nicht anders ist* —
mit Zahlen:

- Warum die Oktaven-Offsets bei ±10.000 gedeckelt sind: bei Koordinaten
  um 100.000 löst float nur in ~0,008er-Schritten auf, der Abfrageabstand
  liegt bei ~0,004 → zwei Nachbarn runden auf denselben Wert →
  Terrassen. Das ist ein Float-Präzisionsargument mit Rechnung.
- Warum die Poisson-Zellkante `r/√2` ist: dann entspricht die Diagonale
  genau `r`, also höchstens ein Punkt je Zelle, also reicht ein
  5×5-Block, also linear statt quadratisch. Vier Sätze, kein Wort zu viel.
- Warum 64 Kacheln: Lastverteilung gegen Cache-Größe gegen Nahtlänge
  (~28 km), drei Größen gegeneinander abgewogen und die Konsequenz
  (Mindestabstand an den Kachelrändern verletzbar) offen benannt.
- Warum das Gras-Zellgitter *nicht* das Chunk-Gitter ist: zwei
  verschiedene Zwänge (1023 Instanzen je Aufruf vs. 65.535 Vertices je
  Mesh), eine gemeinsame Größe wäre für beides falsch.

**Das Fazit ist ehrlich und nach Bereichen sortiert.** Der Abschnitt
„Quelltext" nennt die eigenen Schwachstellen beim Namen — zu lange
Methode in der Platzierung, unbenannte Zahlenwerte im Netzaufbau,
gemischte Member-Reihenfolge, `SheepSense` fordert je Bild Speicher an.
Und er nennt den Grund, warum die lange Methode *nicht* jetzt zerlegt
wird: sie ist das Messobjekt der Threadoptimierung, ein Umbau entwertet
die Messreihe. Das ist kein Ausreden, das ist Prioritätenbegründung.

**Die Lizenzanalyse geht über die Aufgabe hinaus.** Fünf Quellen, je
nach Lizenztyp / Attribution / kommerzielle Nutzung / Gewährleistung /
Copyleft / Kompatibilität / Projektwirkung durchdekliniert, plus die
ausdrückliche Kennzeichnung der KI-erzeugten Grastextur. Beim
`Grass 05`-Material ist sogar aufgefallen, dass die Lizenzseite eine
Einschränkung nennt, die auf der Materialseite fehlt — und es steht
dabei, dass diese Einschränkung fürs Projekt folgenlos bleibt. Das ist
die Sorgfaltsstufe, die man in einer Bachelorarbeit sehen will.

**Der Code ist über Semesterniveau.** Belege aus den gelesenen Dateien:

- Kommentare erklären ausschließlich das Warum. `ObjectPlacer.cs:240`:
  „Read here, not inside the loop: Unity's `==` overload reaches into
  native code" — genau richtig, weder Nacherzählung noch Roman.
- `TerrainToolPresenter.cs:244`: „Composed, not replaced: an axis
  correction baked into the prefab survives". Die Quaternion-Reihenfolge
  ist an drei Stellen im Projekt dieselbe Lektion, und sie ist an jeder
  Stelle als solche erkannt worden.
- `Sheep.cs`: `Init(herd, graveyard)` statt Szenenreferenzen im Prefab —
  das ist die richtige Antwort auf „Ein Prefab darf keine Referenz in die
  Szene halten", und sie kam aus der eigenen Regel.
- `SheepFSM.cs`: Dictionary-Registry mit `GetState<T>()`, States einmal
  erzeugt und wiederverwendet, `ChangeState` mit `Exit`/`Enter`-Paar und
  Selbstwechsel-Schutz. Sauber, klein, richtig.
- Der Push/Pull-Bruch beim Zähmen ist die reifste Entscheidung im
  KI-Code: Statt sechs States um eine eigene Prüfung zu erweitern, wurde
  *eine* Stelle zum Drücken gebracht — und der Grund steht im Kommentar
  über `ToggleTame`. Zu wissen, wann man ein Muster gezielt bricht, ist
  ein Stück weiter als das Muster zu kennen.

**Der Harness ist ein Nebenprodukt mit eigenem Wert.** Ein Doku-System
mit Ownership-Regel je Datei, Leseordnung, Session-Typen und
Doku-Pflicht vor jedem `/clear` ist kein Studentenverhalten. DECISIONS.md
mit 1.168 Zeilen samt verworfenen Alternativen ist ein Werkzeug, mit dem
sich in einem halben Jahr noch rekonstruieren lässt, warum etwas so ist.

---

### 3. Was die Note kostet

Sortiert nach Hebelwirkung — oben steht, was am meisten Note pro Minute
bringt.

**A — Das Layout des TDD. Aufwand: ein Nachmittag. Wirkung: bis zu 13
Punkte.**
Abschnittsumbruch und Seitennummerierung (die durchgehend römische
Nummerierung entspricht keiner der beiden erlaubten Varianten),
Seitenumbrüche vor den Hauptkapiteln, Zeilenabstände, leere Absätze vor
den Verzeichnissen, Strg+A / F9, Wortanzahl auf der Titelseite,
Unterschriften. Das steht alles schon in der ROADMAP — es ist kein
unbekanntes Problem, sondern ein Terminproblem. Ein Dokument mit
150.000 Zeichen exzellentem Inhalt und fehlendem Inhaltsverzeichnis wird
schlechter bewertet als ein mittelmäßiges mit sauberer Form, weil die
Form das Erste ist, was der Prüfer sieht. **Diese Aufgabe gehört auf das
Wochenende 15./16.08., nicht in die Woche danach.**

**B — Widersprüche auf den beiden Deckblättern. Aufwand: 5 Minuten.**
Zwei Funde, beide auf der Seite, die zuerst gelesen wird:
- TDD: `Semester: März 2025`. S4: `Semester: März 2026`. Die Modulnummern
  (`… 0326`) sprechen für 2026 — im TDD steht vermutlich ein Tippfehler.
- TDD: `Modulname: Game Development Basics`. Die eigene ASSIGNMENT-Datei
  führt Modul `4FSC0PD003.1` dagegen als „Structured Game Development",
  und beim zweiten Portfolio stimmt es (`4FSC0PD004` → „Game Dynamics").
  Bitte gegen Canvas prüfen — wenn der Kursname gilt, ist der TDD-Titel
  falsch.

**C — Keine Quellenangaben in den Fachkapiteln. Aufwand: 30 Minuten.
Wirkung: hoch, weil eines der Portfolios „akademische Standards" heißt.**
Bridson wird namentlich genannt, aber nicht belegt. Amdahl wird
namentlich genannt, aber nicht belegt. Perlin Noise gar nicht. Im
S4-Text wird sauber nach Autor/Jahr/Seite zitiert — die Technik sitzt
also, sie ist im TDD nur nicht angewendet. Drei bis vier Belege in
Kapitel 6.3 und 6.5 plus ein Literaturverzeichnis am Dokumentende
schließen die auffälligste Lücke des sonst stärksten Kapitels.

**D — Die Messreihe hat keine Grafik. Aufwand: 20 Minuten.**
Die Aufgabenstellung sagt wörtlich: „die Performancedaten können gut als
Bilder visualisiert werden", und das Feedbackelement unter *Person*
fragt nach der übersichtlichen Zusammenstellung. Es gibt Tabelle 8 und
sonst nichts. Ein Balkendiagramm der sechs Messpunkte (122,7 / 118,1 /
98,9 / 16,5 / 12,4 / 12,2 s) ist ein direkter Treffer auf ein benanntes
Bewertungskriterium.

**E — Kein `namespace` in 83 eigenen Dateien. Aufwand: 10 Minuten (als
Text), nicht als Umbau.**
Die eigenen CODE_GUIDELINES führen unter Block 1 (SAE-Pflicht, Regel 8)
„Namespaces und Ordner strukturieren das Projekt". Tatsächlich verwendet
keine der 83 eigenen Dateien einen Namespace, und Assembly Definitions
gibt es auch keine. Das PCG-Feedbackelement fragt unter *Process*
ausdrücklich: „Wurde die vorgegebene Coding-Convention verwendet?"
**Nicht jetzt umbauen** — 83 Dateien zehn Tage vor der Abgabe anzufassen
ist das falsche Risiko, zumal die Beobachtung aus TDD_NOTES
(2026-08-08), dass Unity-Referenzen an der `.meta`-GUID und nicht am
Pfad hängen, genau deshalb möglich war. Stattdessen: zwei Sätze im
Abschnitt „Quelltext" des Fazits, dass die Namensraum-Gliederung bewusst
aufgeschoben ist und warum. Damit wird aus „Konvention nicht eingehalten"
ein „Abweichung erkannt und begründet" — derselbe Zug, der bei
`PlaceType` schon gemacht wurde.

**F — Kapitel 9 und 10 sind der schwächste Teil des Dokuments.**
Von 43 Abbildungen sind rund 30 Screenshots von Shader- und
VFX-Graphen, aufgeteilt in „Part 1" bis „Part 5". Ein Node-Graph als
Bild erklärt die Idee nicht. Was fehlt, ist je Shader ein Absatz „was
soll er erreichen, welcher Trick macht das, was war das Problem" — beim
Wasser steht das ansatzweise in Kapitel 5.2 (UV-Richtung, Backface an
den Plane-Übergängen) und gehört eigentlich nach Kapitel 9. **Wenn Zeit
knapp wird, ist das der Punkt, den man liegen lässt** — es kostet mehr
als es bringt, weil die zugehörige Aufgabe schon abgeschlossen ist.

**G — Die inhaltliche Lücke: S3 „generierte Bevölkerung".**
Das PCG-Lernziel S3 lautet „Erstellen einer Simulation einer gewohnten
Umgebung mit einer generierten Bevölkerung". Aktuell ist die Herde
handgesetzt, die Goblins im Umland sind offen, die Glühwürmchen sind
offen. Der Placer *kann* das — er platziert 7,4 Mio Grasbüschel — er
tut es für Lebewesen nur nicht. **Eine einzige Herde und ein paar
Goblins über den Placer statt von Hand zu setzen, deckt ein Lernziel ab,
das sonst nur halb belegt ist.** Das ist nach dem Layout die zweitbeste
Investition der verbleibenden Zeit. Hängt allerdings am NavMesh-Bake und
damit an der finalen Weltgröße (Punkt 1b der ROADMAP).

**H — Kein Nachweis von Fremd-Feedback.**
Beide Aufgabenstellungen nennen es unter *Person*: „Lass dein Tool von
deinen Mitstudenten testen" (Tool), „Wurde sich genügend Feedback zur
Abgabe geholt und dieses umgesetzt?" (PCG). Im TDD steht dazu nichts.
Falls es Rückmeldungen aus der formativen Abgabe gab: zwei Zeilen im
Änderungsverlauf oder im Fazit, was zurückkam und was daraufhin geändert
wurde. Das ist ein Punkt, den man nicht durch Qualität ersetzen kann.

---

### 4. Profil — Person und Arbeitsweise

**Was Isor auszeichnet: Er baut das Werkzeug, mit dem er arbeitet, mit.**
Der Harness ist dafür der Beleg, aber nicht der einzige. Nach dem
Laptop-Defekt wurde nicht nur der Datenverlust hingenommen, sondern der
Prozess geändert (zusätzliche Sicherung, Grindstone für die
Zeiterfassung) — und das steht auch so im TDD, statt es zu verschweigen.
Der Diagramm-Generator, der `.drawio`-Dateien aus dem Code erzeugt,
gehört in dieselbe Reihe: einmal ein Werkzeug bauen statt zehnmal von
Hand zeichnen.

**Er plant Messungen, bevor er sie braucht.** In TDD_NOTES steht am
19.07.: „Threading bewusst ans Ende: langsame Version = Baseline-Messdaten
für die Threading-Abgabe." Das ist siebzehn Tage vor der
Threading-Session geschrieben. Eine Abgabe so vorzubereiten, dass die
Ausgangsmessung von selbst entsteht, ist Planung auf einem Niveau, das
man normalerweise erst im Berufsalltag lernt.

**Er korrigiert sich gegen die eigenen Notizen.** Am 08.08. wurden die
Rohlogs aller sechs Threading-Builds nachgerechnet und dabei zwei eigene
Speicherwerte berichtigt (134 MB / 2,1 MB statt 94 MB / 1,5 MB), samt
Erklärung, woher die falschen Zahlen kamen. Die daraus gezogene Lehre —
„Rohlogs aufheben, nicht nur die Zusammenfassung; nur so lässt sich eine
Notiz später widerlegen" — ist der wissenschaftliche Kern des ganzen
Semesters.

**Er verallgemeinert.** Durch die Notizen zieht sich ein Muster: „gleiche
Klasse Fehler wie die Quaternion-Reihenfolge und der Prompt-Cache",
„dritte Stelle derselben Lektion komponieren statt ersetzen". Er sammelt
nicht Bugfixes, er sammelt Fehlerklassen. Das ist der Unterschied
zwischen jemandem, der langsam besser wird, und jemandem, der schnell
besser wird.

**Er entscheidet Umfang bewusst und schreibt die Begründung auf.**
`PlaceType` nicht anfassen (Messobjekt). Prefab-Painter nicht ins TDD.
Kein `namespace`-Umbau. Threading ans Ende. Das sind alles Entscheidungen
gegen den eigenen Aufräumreflex, mit Begründung — und die Begründung
steht in DECISIONS, nicht nur im Kopf.

**Risiken, ehrlich:**

1. **Fertigstellung ist die wiederkehrende Verlustzone.** Der Inhalt ist
   jedes Mal stark, der letzte mechanische Meter fehlt. Das ist beim
   letzten Mal passiert und ist heute wieder der größte Einzelposten
   (Punkt A). Das ist kein Können-, sondern ein Reihenfolge-Problem: Die
   Politur wird ans Ende gelegt, und ans Ende passt sie nie ganz.
   Gegenmittel: Layout-Arbeit ist kein „Rest", sondern ein Baustein mit
   eigenem Termin — und der Termin muss auf einem Tag liegen, an dem
   wirklich Zeit ist.
2. **Der Umfang läuft der Zeit davon.** 51 Stunden Dokumentation, dazu
   ein selbstgebauter Diagramm-Generator und ein Prefab-Painter, der
   ausdrücklich nicht Abgabeumfang ist. Jede dieser Investitionen ist für
   sich richtig begründet — zusammen sind sie der Grund, warum das
   Village leer ist. Die Zeitrechnung ist unbestechlich: eine Herde
   platzieren hätte weniger gekostet als der Prefab-Painter.
3. **Selbstständigkeit ist der erwartbare offene Punkt** — er ist selbst
   benannt worden, und das ist die halbe Miete. Der Befund ist
   differenzierter, als es sich anfühlt: Der Code ist getippt, die
   Architektur ist mitentschieden, die Fehlerklassen sind selbst erkannt.
   Was noch nicht geübt ist, ist der Anfang vor einer leeren Datei in
   unbekanntem Gebiet. Genau dafür ist die eigene Regel „Entwurf vor
   Gerüst" vom 05.08. da — sie ist die richtige Maßnahme, sie braucht
   jetzt nur Wiederholungen.
4. **Das Zeitfenster ist enger als es aussieht.** Heute ist Dienstag, der
   11.08. Abgabe ist Freitag, der 21.08. Bei Mo–Do wenig und am
   Wochenende viel Zeit bleibt genau **ein volles Wochenende** (15./16.08.)
   plus Abende. Alles, was mehr als einen halben Tag kostet, muss auf
   dieses Wochenende — und es passt nicht alles hin. Punkt F und Teile
   von Punkt G sind die Kandidaten zum Streichen.

---

### 5. Profil — Coding-Stand

**Kurzfassung: Der Code liegt sichtbar über dem zweiten Semester. Was
fehlt, ist Werkzeugbreite, nicht Denkweise.**

**Was sitzt:**

| Bereich | Beleg | Einordnung |
|---|---|---|
| Konsequenter Stil | 83 Dateien mit Header, `<summary>`, `[Tooltip]`, `_camelCase`, Allman | über Semesterniveau — hier fällt sonst fast jeder durch |
| Trennung von Zuständigkeiten | Pipeline als reine statische Stufen, Szene erst im Presenter | 4. Semester |
| Entwurfsmuster mit Begründung | MVP im Tool, Strategy bei der Dichte — beide *weil*, nicht *weil man muss* | 4. Semester |
| Komposition statt Vererbung | Sheep als Knotenpunkt über Komponenten, eine flache Basisklasse für States | solide |
| Unity-Lebenszyklus | `OnEnable`/`OnDisable`-Paare, `Awake` für eigene, `Start` für fremde Objekte, `Init()`-Injektion | über Semesterniveau |
| Determinismus als Entwurfsziel | zwei getrennte Seeds, Offsets einmal gebaut und gereicht, Seeds je Kachel vorab gezogen | selten in dieser Ausbildungsphase |
| Nebenläufigkeit | `Parallel.For` über Kacheln, alles Unveränderliche vorher auf dem Main Thread aufgelöst | deutlich über Semesterniveau |
| Messen statt raten | Messreihe, Zwischenmessung, verworfene Optimierung | Berufspraxis |

**Was fehlt — und das ist normal für den Zeitpunkt:**

- **Keine automatisierten Tests.** Die Verifikation ist manuell und
  durchdacht (flach / zufällig / Rampe beim MeshBuilder, Determinismus /
  Seed-Variation / Oktaven beim Generator), aber es gibt kein
  Test-Assembly. Für die Abgabe irrelevant, für das dritte Semester und
  für Bewerbungen ein echter Zugewinn: `HeightmapGenerator` und
  `MeshBuilder` sind reine Funktionen und damit die einfachsten
  Testkandidaten, die es gibt.
- **Keine Namespaces, keine Assembly Definitions.** Siehe Punkt E. Nach
  der Abgabe der richtige Zeitpunkt — Assembly Definitions verkürzen
  zusätzlich die Kompilierzeit spürbar.
- **Methodenlänge.** `PlaceType` (~100 Zeilen) macht Seeding, Kachelschleife,
  Punktfilter und Transform-Aufbau in einem. Selbst gefunden, bewusst
  aufgeschoben, richtig entschieden.
- **Keine Objekt-Pools.** `SheepSense` fordert je Bild Speicher an —
  selbst gefunden, steht auf der Politur-Liste.
- **Kein Profiler-gestütztes Arbeiten.** Gemessen wurde per Stoppuhr und
  `Debug.Log`, was für diese Aufgabe völlig ausreichte und sogar
  robuster war als Editor-Profiling. Der Unity Profiler und die
  Frame-Debugger-Ansicht sind trotzdem Werkzeuge, die im dritten
  Semester dazukommen sollten.
- **Datenstrukturen jenseits von List/Dictionary/Array** sind noch nicht
  gebraucht worden. Kommt mit C++ von selbst.

**Zum dritten Semester (C++ und Unreal):** Der Übergang wird leichter
ausfallen als befürchtet, weil das, was schwer zu lernen ist, schon da
ist — Zerlegung, Determinismus, Messen, Warum-Kommentare. C++ bringt
drei Dinge, die C# abgenommen hat: manuelle Lebensdauer von Objekten
(Zeiger, Referenzen, RAII), Header/Implementierungs-Trennung und den
fehlenden Sicherheitsgurt (kein `NullReferenceException`, sondern ein
Absturz oder Schlimmeres). Unreal bringt sein eigenes Vokabular
(`UPROPERTY`, Actor/Component statt GameObject/MonoBehaviour,
Blueprints als zweite Sprache daneben). Was **direkt überträgt**: die
FSM, die Pipeline-Denkweise, die Trennung Model/View/Presenter, das
Threading-Verständnis. Was **neu wehtun wird**: dass ein Fehler nicht
mehr höflich meldet, wo er passiert ist.

---

### 6. Nächster Schritt

Reihenfolge bis zum 21.08., nach Hebelwirkung sortiert und gegen die
verfügbare Zeit geschnitten:

1. **Do/Fr 13.–14.08. (abends, je 1–2 h):** Deckblatt-Widersprüche (B),
   Quellenangaben in 6.3/6.5 (C), zwei Sätze zum `namespace` im Fazit (E).
   Alles kleine, abgeschlossene Häppchen — passt in Abende.
2. **Sa 15.08. (der wichtigste Tag):** Layout des TDD komplett (A).
   Nicht anfangen, bevor der Tag frei ist, und nicht aufhören, bevor
   Strg+A / F9 durchgelaufen ist und die Verzeichnisse stehen.
3. **So 16.08.:** Messreihen-Diagramm (D), dann Village und Herde über
   den Placer (G), soweit der NavMesh-Bake es zulässt.
4. **Mo–Do 17.–20.08. (abends):** Politur nach der ROADMAP-Liste,
   Abgabeordner sortieren und befüllen (ROADMAP 3b), Endcheck.
5. **Nicht mehr anfangen:** Kapitel 9/10 überarbeiten (F),
   `namespace`-Umbau, `PlaceType` zerlegen, Prefab-Painter-Fragen.

**Zur Bewerbungsfrage.** Die Einschätzung, erst nach dem dritten
Semester zu bewerben, ist richtig — aber aus einem anderen Grund als
angenommen. Es liegt nicht am Können; das Threading-Kapitel allein ist
ein besseres Bewerbungsstück als das, was viele Absolventen mitbringen.
Es liegt daran, dass ein Studio zuerst **etwas Spielbares** sehen will:
einen Build, ein Video von 60 Sekunden, dann erst den Text. Aktuell ist
der Spieler eine Kapsel, das Dorf leer und es gibt keinen Ton — die
Systeme sind gut, aber sie *zeigen* sich nicht.

Konkret für die Zeit nach dem 21.08. bis zur Bewerbung: **eine polierte
vertikale Scheibe schlägt eine große unfertige Welt.** Ein Dorf, eine
Herde, Ton, Licht, ein Menü und fünf Minuten, die sich rund anfühlen —
das ist bewerbungsfähig. Dazu die Threading-Messreihe als
zweiseitige Fallstudie (Ausgangslage, Fehlversuch, Amdahl, Kachelung,
Messtabelle, Diagramm) als eigenes PDF. Diese zwei Dinge zusammen sind
eine gute Bewerbung. Realistisch ist der Einstieg als Praktikum oder
Werkstudent, nicht als Junior — und das ist der normale Weg, kein
Rückschritt.

---

### 7. Prüfanker fürs nächste Zeugnis

Beim nächsten Mal wird gegen diese Punkte verglichen — jeweils mit einer
Zahl, damit die Entwicklung messbar ist und nicht nur gefühlt:

1. Ist das TDD-Layout vollständig? (Verzeichnisse vorhanden, Wortanzahl
   eingetragen, Seitennummerierung regelkonform — ja/nein)
2. Wie viele Quellenangaben stehen in den Fachkapiteln? (heute: 0)
3. Wie viele der 83 eigenen `.cs`-Dateien liegen in einem `namespace`?
   (heute: 0)
4. Gibt es ein Test-Assembly, und wie viele Tests? (heute: 0)
5. Steht eine Herde oder ein NPC-Typ über den Placer in der Welt statt
   von Hand? (heute: nein)
6. Wie viele Bausteine hat Isor ohne Gerüst begonnen — also nach dem
   eigenen Entwurf, ohne dass Claude vorher ein Skelett gezeigt hat?
   (heute: die Regel existiert seit 05.08., Zählung beginnt hier)
7. Existiert ein spielbarer Build mit Ton und Menü? (heute: nein)
8. Verhältnis Dokumentationszeit zu Umsetzungszeit im nächsten
   Abschnitt (heute: 51 h Doku zu ~75 h Umsetzung im 2. Semester)
