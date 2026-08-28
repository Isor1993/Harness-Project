# Multiplayer.md — Entscheidungen Multiplayer und Netzwerk

Ownership: Nur Entscheidungen zu Multiplayer, Netzwerk und der daraus
folgenden Datentrennung — was entschieden wurde, warum, und welche
Alternativen verworfen wurden. Kein Plan (das ist die ROADMAP), kein
Ereignis (das ist das LOG), keine Design-Absicht des Spiels (das ist das
`GDD.md`).
Nicht hier: der Bestand aus Semester 2 samt seiner Befunde
(`ALTSTAND.md`), das Verhalten der Gegner selbst (`Entities.md`), der
Aufbau der Menü-Oberfläche (`UI.md`) und alles, was das Terrain-Tool
erzeugt (`Terrain_Mesh.md`). Hier steht nur, **wer im Netz worüber
entscheidet**.
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

Diese Datei entstand in der Design-Session vom 2026-08-25/26. Die
Architektur ist zusätzlich als Artifact-Seite lesbar (`⚙️ System ·
Multiplayer`, geführt im `Kern/ARTIFACT_INDEX.md`); führend ist diese
Datei.

## 2026-08-25 — Multiplayer wird vorgezogen und ist der Rahmen von Semester 3
Was: Der Koop wird im 3. Semester gebaut, nicht „sehr spät". Ziel ist ein
fertiger Prototyp, den man solo **und** zu zweit spielen kann, mit
mindestens einem Tower-Floor, Kampf und Loot. Getestet wird mit einem
Mitspieler über das Internet.
Warum: Alle Systeme, die der Koop braucht, existieren noch nicht — von
acht ist eines halb gebaut. Sie entstehen also ohnehin neu. Werden sie
von Geburt an netzwerkfähig gebaut, kostet Multiplayer fast nichts
extra; baut man sie erst solo, baut man sie zweimal.
Verworfen: Multiplayer als Technikdemo ohne Gameplay; voller Ausbau mit
4–5 Spielern und allen Systemen (das sind zwei Semester, nicht eines);
Koop nachträglich über ein fertiges Solo-Spiel stülpen.

## 2026-08-25 — Solo ist eine Runde mit einem Spieler
Was: Es gibt genau einen Codepfad. Der Einzelspieler startet im
Hintergrund einen Host mit einem Spieler — ohne Menüeintrag, ohne
Verbindung nach außen. Eingaben laufen auch solo über den Netzweg.
Warum: 23 der 86 Skripte tragen ein `Update` oder `FixedUpdate`. Bei zwei
getrennten Pfaden müsste jedes davon zwei Fälle kennen, und beide Fälle
hätten eigene Fehlerbilder — die erfahrungsgemäß in den Abgabewochen
auftauchen. Derselbe Weg, den Minecraft, Terraria und Valheim gehen.
Verworfen: zwei getrennte Wege im Code (Solo behalten, Netz daneben
bauen); den Solo-Modus ganz streichen. Der Preis der gewählten Lösung —
Serialisierung läuft auch im Einzelspiel mit — ist bekannt und wird als
Messung ins Abgabedokument aufgenommen.

## 2026-08-25 — Host-Modell statt verteilter Autorität
Was: Der Weltbesitzer ist zugleich Server und Spieler. Er rechnet Gegner,
Schaden, Beute und den Weltzustand. Verlässt er die Runde, endet sie für
alle; Gäste landen mit ihrer Beute in ihrer eigenen Welt.
Warum: Das GDD hatte die Topologie längst entschieden, ohne sie zu
benennen — „jeder Spieler besitzt seine eigene Welt, andere joinen als
Gäste". Verteilte Autorität verteilt den Besitz genau dort, wo das Design
ihn bündelt, macht das Speichern schwer (keine Stelle kennt den ganzen
Weltzustand) und setzt zwingend einen Unity-Dienst voraus — ohne
Internet liefe gar nichts, auch nicht auf dem Rechner der Dozentin.
Verworfen: distributed authority (im selben Paket enthalten, später
nachrüstbar); eigener dedizierter Server (jemand müsste ihn betreiben und
bezahlen); Host-Wanderung beim Ausstieg des Besitzers (die komplette Welt
müsste im laufenden Spiel den Besitzer wechseln).

## 2026-08-25 — Netcode for GameObjects, Beitritt über einen Join-Code
Was: Paket ist `com.unity.netcode.gameobjects` 2.13, passend zu Editor
6000.5. Verbindung über Unity Relay: Der Gastgeber bekommt einen kurzen
Code und gibt ihn weiter. Dazu Multiplayer Play Mode zum Testen ohne
Mitspieler.
Warum: Es ist Unitys eigenes Paket, die Doku ist offiziell zitierbar
statt Forenwissen, Relay steckt bereits im NetworkManager, und
`com.unity.multiplayer.center` ist im Projekt schon installiert. Im
Prüfungsgespräch muss niemand begründen, warum die engine-eigene Lösung
nicht genügt hätte. Relay erspart Portweiterleitung — der Punkt, an dem
ein Test mit einem Kommilitonen sonst scheitert.
Verworfen: FishNet (technisch stärker, vor allem bei Prediction — aber
das zählt bei PvP, nicht bei Koop); Mirror (älteste Linie, für Unity 6
nicht mehr die natürliche Wahl); Photon Fusion 2 (Anbieterbindung);
direkte IP-Eingabe (Router-Konfiguration beim Mitspieler); Unity Lobby
mit öffentlicher Rundenliste (für zwei Testspieler ohne Nutzen).

## 2026-08-25 — Bewegung gehört dem Gast, alles Folgenreiche dem Host
Was: Der Gast rechnet seine eigene Bewegung und meldet die Position; der
Host übernimmt sie ungeprüft. Treffer, Schaden, Beutewürfe und
Weltveränderungen prüft immer der Host. Der Gast spielt die
Trefferanzeige sofort ab, die Bestätigung kommt kurz danach.
Warum: Ungeprüfte Bewegung fühlt sich sofort richtig an und ist billig zu
bauen; für Koop unter Freunden ist die Schummelmöglichkeit hinnehmbar und
im Prüfungsgespräch begründbar. Alles mit Folgen beim Host zu lassen
kostet wenig zusätzlich und verhindert, dass sich jemand Gegenstände
erschummelt.
Verworfen: durchgehend host-geprüfte Bewegung (verlangt Vorhersage und
Rückrechnung — große, tiefe Arbeit, die bei „fertig vor tief" nicht
hineinpasst); den Treffer den Angreifer melden lassen.
Offen bleibt, **wann** auf host-geprüfte Bewegung umgestellt wird. Die Tür
dafür hält der Eintrag „Input-Asset wird nach Reichweite geteilt" offen.

## 2026-08-25 — Charakter reist, Welt bleibt
Was: Die Spieldaten zerfallen in zwei Töpfe. `PlayerProfile` reist mit
dem Spieler in jede Welt: Level, Erfahrung, Inventar, Ausrüstung,
Rezepte, Quest-Fortschritt, freigeschaltete Floors. `WorldState` bleibt
beim Besitzer: Terrain-Seed, gebaute Häuser, abgebaute Ressourcen samt
Timern, gezähmte Tiere. Beide gibt es ab dem ersten Tag als Struktur, das
Schreiben auf die Platte kommt später. Regel: **Kein Feature wird gebaut,
bevor beantwortet ist, in welchen der beiden Töpfe es schreibt.**
Warum: Folgt zwingend daraus, dass der Gast Loot, Level, Quests und
Floor-Freischaltungen mit nach Hause nimmt — dann gehört sein Charakter
nicht zur Welt. Die Aufteilung muss vor dem ersten Feature stehen, weil
jedes Feature in einen der Töpfe schreibt; das Schreiben auf die Platte
muss es nicht, solange es nichts zu speichern gibt.
Verworfen: vollständiges Speichern gleich am Anfang (wochenlang an etwas
bauen, das noch nichts speichert); Speichern gegen Ende (die gewachsene
Datenlage passt dann selten in ein sauberes Format, und der Umbau fällt
in die Abgabewochen).

## 2026-08-25 — Der Floor kommt gemischt herüber: Seed plus Objekte
Was: Gelände und Bewuchs entstehen auf beiden Rechnern aus derselben
Zahl. Gegner, Truhen und der Boss kommen einzeln vom Host. Wesen werden
vom Host gerechnet, aber nur in Spielernähe übers Netz geschickt.
Warum: Die Pipeline arbeitet bereits so — der Weltaufbau hängt an
`TerrainConfig` und einem Seed, und Gras läuft über
`Graphics.RenderMeshInstanced`, also ohne ein GameObject je Halm und
damit über das Netz kostenlos. Was einen veränderlichen Zustand hat,
lässt sich dagegen nicht aus einem Seed ableiten. Bei 19 Herden plus
40–50 Gegnern wäre das Senden aller Wesen zu viel für die Leitung.
Verworfen: alle Objekte einzeln vom Host schicken (langer Ladebalken für
den Gast); Schafe rein örtlich laufen lassen (dann könnte der Gast kein
Schaf zähmen, das der Host auch sieht).
Bedingung, noch ungeprüft: Die Generierung muss auf beiden Rechnern
dasselbe liefern. Der Vergleichstest steht in der ROADMAP als erster
Punkt.

## 2026-08-25 — Die Koop-Regeln: Portal, Tod, Beute
Was: Das Portal fragt nach Bestätigung und wechselt dann die **ganze
Gruppe**. Wer stirbt, liegt am Boden und kann von einem Mitspieler durch
Halten einer Taste wiederbelebt werden. Beute fällt für jeden Spieler
getrennt; jeder sieht nur seine eigene.
Warum: Es gibt immer nur eine aktive Welt — genau wie im GDD; zwei
gleichzeitig laufende Welten würden die Last auf dem Host verdoppeln.
Aufhelfen ist das schönste Koop-Gefühl und hält die Gruppe zusammen, ohne
dass jemand lange still zusieht. Getrennte Beute ist im Netz der
einfachste Fall, weil nichts umkämpft ist — bei einem gemeinsamen Haufen
müsste der Host entscheiden, wer bei gleichzeitigem Zugriff gewinnt.
Verworfen: jeder wechselt für sich (widerspricht dem GDD); nur der Host
darf ein Portal auslösen (bevormundend); Zuschauen bis zum Floor-Ende;
gemeinsamer Beutehaufen; Beute reihum verteilen (braucht Buchführung und
fühlt sich mechanisch an).

## 2026-08-25 — Semesterschnitt: was in den Prototyp kommt
Was: Im Prototyp sind Kampf, Loot und Inventar, der Turm mit Portal und
mindestens einem Floor, sowie Speichern und Laden. Verschoben sind Bauen,
Handwerk und Quests. Der Gast darf im Zielbild alles — kämpfen, looten,
abbauen, bauen, handwerken —, im Prototyp nur, was der Schnitt hergibt.
Perspektive bleibt First Person, aber die Figur bekommt einen sichtbaren
Körper mit Animationen. Alles wird für beliebig viele Spieler gebaut,
getestet und vorgeführt wird mit zweien.
Warum: Kampf, Loot und Inventar sind der Kern der Kernschleife — ohne sie
gibt es keinen Grund, gemeinsam in den Turm zu gehen. Die Village-Seite
(Bauen, Handwerk, Quests) ist der teuerste Block und trägt für eine
Koop-Vorführung am wenigsten. Ein sichtbarer Körper ist Pflicht, sobald
ein zweiter Spieler zusieht; die Umschaltung auf Third Person ist es
nicht. Annahmen wie „der andere Spieler" im Code würden jede spätere
Erweiterung zu einem Umbau machen.
Verworfen: alles ins Semester nehmen; fest auf zwei Spieler auslegen; von
Anfang an mit vier bis fünf testen (viel Rechner, viel Terminabsprache);
die im GDD geplante Perspektivumschaltung sofort mitbauen.

## 2026-08-25 — Das Input-Asset wird nach Reichweite geteilt
Was: `PlayerInputReader` bleibt nicht ein einziges geteiltes
ScriptableObject. Was zur Spielerfigur gehört — `PlayerMotor`,
`PlayerLook`, `PlayerInteractor` — bekommt eine Eingabequelle je Spieler
als Komponente. Was nur den eigenen Rechner betrifft — `GameController`
(Pause) und `TimeFastForward` — behält das Asset. Der Motor holt seine
Eingabe nicht mehr selbst, sondern bekommt sie gereicht.
Warum: Ein ScriptableObject ist projektweit eines. Existieren zwei
Spielerfiguren auf demselben Rechner, lesen beide dasselbe Asset und
laufen mit denselben Tasten los. Die Aufteilung ist kleiner als gedacht:
Von fünf Nutzern wandern drei, zwei bleiben. Dass der Motor die Eingabe
gereicht bekommt, ist die Naht, die eine spätere Umstellung auf
host-geprüfte Bewegung billig hält — dem Motor ist dann gleich, ob die
Werte von der Tastatur oder aus dem Netz kommen.
Verworfen: nur auf fremden Figuren Motor und Kamera abschalten (reicht
für die gewählte Bewegungsvariante, macht die spätere Umstellung aber
teurer); alles beim geteilten Asset lassen.

## 2026-08-26 — Spielerdaten laufen über eine Schnittstelle mit Rückruf
Was: Das `PlayerProfile` wird nicht direkt gelesen und geschrieben,
sondern über `IPlayerDataService` mit `Load(playerId, onLoaded)` und
`Save(profile, onSaved)`. Dahinter liegt im 3. Semester eine lokale
Datei, die sofort antwortet. Ein echtes Backend gibt es nicht; ein Shop
ist auf Semester 4 oder später verschoben und ist ausdrücklich **nicht**
der Grund für die Schnittstelle.
Warum: Isors Vorschlag, und er trägt: Die Schnittstelle tut so, als
könnte die Antwort dauern — auch wenn sie sofort da ist. Kommt je ein
Datenserver dazu, wird eine Klasse getauscht statt jede Aufrufstelle
angefasst. Der Rückruf statt `async`/`await` ist der Grund, warum das
ohne neues Sprachkonstrukt geht: Interfaces und Events werden im Projekt
längst benutzt (`IDamageable`, `IInteractable`, `IDayNightListener`, die
Ereignisse im `PlayerInputReader`) — `async` würde quer durch den ganzen
Code wandern und müsste im Prüfungsgespräch erklärt werden.
Verworfen: direkt in die Datei schreiben (spätere Umstellung fasst jede
Aufrufstelle an); `async`/`await` als Schnittstelle (Vorschlag des
Vorlaufs vom 2026-08-23, siehe unten — verworfen wegen des Maßstabs
„Abgabe-Code auf Semesterniveau"); die Schnittstelle erst mit dem
Inventar bauen (Kampf und Floor schrieben bis dahin daran vorbei).

## 2026-08-26 — Semester 3 ist ein Neustart desselben Projekts
Was: Gearbeitet wird im bestehenden Repo, direkt auf `main`. Inhaltlich
ist es ein Neuanfang: neue Szenen von Null, netzwerkfähig ab der ersten
Zeile. Der Bestand aus Semester 2 blockiert nichts — er ist Altstand, der
später übernommen, angepasst oder verworfen wird. Es gilt die
**Übernahme-Regel**: Für jeden Baustein aus Semester 2 wird erst dann
entschieden, wenn er gebraucht wird, und die Antwort ist eine von dreien —
*mitnehmen*, *anpassen* oder *neu*. Nicht vorab als Liste. Der einzige
gesetzte Fall ist das Menü: mitnehmen und erweitern. `Village.unity`
bleibt unangetastet als Beleg der letzten Abgabe stehen.
Warum: Dieser Prototyp ist der, auf dem alles Weitere aufbaut — niemand
will ihn hinterher umschreiben. Ein neues Repo würde die
Versionsgeschichte der Terrain- und Gras-Arbeit abschneiden, und die ist
vorzeigbar. Eine Übernahmeliste, die heute entsteht, stimmt beim dritten
Baustein nicht mehr; die Entscheidung fällt besser am Bauplatz, mit dem
Wissen von dort.
Verworfen: neues Repo fürs 3. Semester; eigener Branch (Isors
Entscheidung — der Preis, dass während des Umbaus nichts Startbares
dasteht, ist benannt und angenommen); die bestehende `Village.unity` zu
`StarterVillage` umbauen; eine Übernahmeliste im Voraus festlegen.

## 2026-08-26 — Der Einstieg läuft über das Menü, nicht über einen Behelfsknopf
Was: Das bestehende Hauptmenü wird um drei Wege erweitert — allein
spielen, Welt erstellen, Welt beitreten — und der Ladebalken wartet auf
mehrere Spieler statt auf einen. Der Verbindungsknopf aus der
Lernphase ist ein Behelf und fliegt danach raus.
Warum: Isors Einwand, und er deckte eine Lücke auf: Der Einstieg ist kein
Nachgedanke, sondern der erste Bildschirm. Das Menü existiert bereits und
wird erweitert, nicht neu gebaut — es ist damit zugleich der erste Fall
der Übernahme-Regel. Getrennt wird trotzdem: Erst soll das Netz beweisen,
dass es steht, ohne dass eine Oberfläche als Fehlerquelle dazwischenliegt.
Verworfen: den Behelfsknopf bis zum Semesterende behalten; das Menü erst
nach dem Floor anfassen.

## 2026-08-26 — Wie ein Floor entsteht, blockiert den Netzbau nicht
Was: Die offene GDD-Frage nach dem Verhältnis von freier Generierung zu
festen Bausteinen wird **nicht** jetzt beantwortet. Der Floor der
Netz-Phase bekommt ein Platzhalter-Gelände aus der bestehenden Pipeline.
Verbindlich ist nur der Vertrag: **Seed rein, Welt raus.**
Warum: Isors Einwand, und er trifft zu — die Netzwerkarchitektur
unterscheidet die beiden Wege gar nicht: In beiden Fällen geht eine Zahl
übers Netz und beide Rechner bauen daraus dasselbe. Gebraucht wird die
Antwort erst, wenn ein Floor echten Inhalt bekommt. Bis dahin ist sie
eine Inhaltsfrage, keine Netzfrage.
Verworfen: die Floor-Generierung vor Semesterstart entscheiden (meine
ursprüngliche Einschätzung, sie blockiere den Netzbau — sie war falsch);
den Platzhalter an der Seed-Schnittstelle vorbeibauen (dann wäre er
Wegwerfarbeit).

## 2026-08-26 — Verhältnis zum Vorlauf vom 2026-08-23/24
Was: Vor dieser Session entstand ohne den Harness eine Vorfassung als
zwei Artifact-Seiten (heute `💡 Lernstück · Netzwerkgrundlagen` und
`💡 Lernstück · NGO-Bausteine`). Ihr Lehrstoff gilt weiter und wird nicht
ersetzt. Überholt sind zwei Punkte, die auf den Seiten als solche
markiert sind: die Annahme eines neu aufgesetzten Projekts und die
Zeitschätzung von sechs bis acht Wochenenden.
Warum: Die Vorfassung kam unabhängig auf dieselbe Architektur — Netcode
for GameObjects, Host-Modell, Unity Relay, mit denselben Gegenargumenten
zu FishNet. Dass zwei getrennte Läufe dort landen, ist der beste Beleg,
den diese Empfehlung haben kann. Ihre Zeitschätzung rechnet ausdrücklich
nur die Netzwerkschicht ohne Spielinhalt, und der ist der größere Teil —
wer sie im Kopf behält, unterschätzt das Semester.
Verworfen: die beiden Seiten löschen (der Lehrstoff ist gut und müsste
sonst neu geschrieben werden); die Vorfassung als überholt behandeln, nur
weil sie ohne Harness entstand.

## 2026-08-27 — Phase 0 läuft im eigenen Prüfstand, das Village kommt ab Phase 1
Was: Der erste Verbindungstest läuft in einer eigenen, nackten Szene
`NetTestbed.unity` — flacher Boden, zwei Kapseln, Behelfsknopf —, die
danach dauerhaft als Diagnose-Szene stehen bleibt. Ab Phase 1 führt der
Einstieg über das Menü direkt nach `StarterVillage`; die „Testwelt" der
ROADMAP entfällt. Phase 0 ist fertig, wenn fünf Punkte stehen: Verbindung
über den Join-Code, Besitz (jeder steuert nur seine Kapsel), Nachrichten
in beide Richtungen, gelaufener Vergleichstest, und ein Windows-Build
läuft auf dem Laptop.
Warum: Isors Vorschlag war, gleich im Village über das Menü anzufangen,
um nichts wegzuwerfen. Der Teil trägt und ist übernommen — die Zielszene
heißt ab Phase 1 `StarterVillage` statt „Testwelt", das spart eine
Wegwerf-Szene. Die Trennung bleibt trotzdem: Beim ersten Verbindungstest
kämen sonst sieben Bausteine als Fehlerquelle in Frage statt drei, weil
Menü, netzsynchroner Szenenwechsel, Ladebalken und Spawn-Punkte
dazukommen — und zwei davon sind eigene Fallen. Der Prüfstand ist kein
Wegwerf, weil eine leere Szene später jeden Netzfehler einkreisen hilft;
weggeworfen wird nur der Behelfsknopf.
Verworfen: gleich im Village über das Menü anfangen (Isors Fassung); eine
Szene, die als Prüfstand anfängt und zum Village wächst (kostet später
die leere Szene zum Fehlersuchen); Save/Load vor Phase 1 bauen — der
Schnitt vom 2026-08-25 gilt weiter, in Woche 1 gibt es nichts zu
speichern.

## 2026-08-27 — Steam ist das Veröffentlichungsziel, die Transportschicht bleibt tauschbar
Was: Veröffentlicht werden soll auf Steam (`GDD.md` → „Umfang und Ziel").
Für das Semester bleibt es bei Unity Relay. Der Verbindungsaufbau bekommt
in Phase 1 mit dem Menü eine dünne Naht — `ISessionService` mit
`Create(onReady)` und `Join(code, onReady)`, dahinter
`RelaySessionService`. Ein Steam-Transport käme später als zweite
Umsetzung daneben.
Warum: Steam bringt eigenes Netzwerk mit (Steam Datagram Relay), das in
Steamworks enthalten ist und Einladungen über die Freundesliste erlaubt;
Unity Relay rechnet dagegen nach durchgeleiteter Datenmenge ab. Benutzen
lässt sich Steams Netzwerk heute trotzdem nicht — es braucht eine App-ID,
und die gibt es erst nach der Steam-Direct-Gebühr; vorführen ließe sich
damit nichts, und die Dozentin bräuchte Steam. Betroffen ist bei einem
Wechsel ohnehin nur die Transportschicht: Spielcode und Netcode for
GameObjects bleiben unangetastet.
Verworfen: jetzt schon auf Steams Netzwerk bauen (App-ID fehlt,
Vorführung unmöglich); die Naht sofort in Phase 0 einziehen — anders als
beim Datendienst hat der Verbindungsaufbau genau **einen** Aufrufer, das
Menü, und eine Abstraktion ohne Anlass müsste im Prüfungsgespräch
mitverteidigt werden.

## 2026-08-27 — Join-Code über die Sessions-API, Pakete über das Multiplayer Center
Was: Die Pakete werden über das bereits installierte Multiplayer Center
ausgewählt und installiert, nicht einzeln von Hand. Der Join-Code
entsteht über die Sessions-API, nicht durch eigenes Ansteuern von Relay.
Warum: Das Center kennt den Editor (`6000.5.2f1`) und setzt zueinander
passende Versionen; von Hand gewählte Versionen kollidieren
erfahrungsgemäß erst beim Build. Die Sessions-API ist Unitys aktueller
Weg für Unity 6 und damit im Prüfungsgespräch zitierbar, und Runde
erstellen wie beitreten sind je eine Handvoll Zeilen statt Anmeldung,
Allocation und Transport-Verdrahtung von Hand. Da dieser Code beim
späteren Steam-Wechsel ohnehin ersetzt wird, ist wenig davon der bessere
Einsatz.
Verworfen: die Pakete einzeln über den Package Manager holen; Relay
direkt ansteuern (mehr Zeilen, die zur Abgabe gehören und später doch
ersetzt werden).

## 2026-08-27 — Geprüft wird auf PC und Laptop, nicht mit einem Mitspieler
Was: Der Zwei-Rechner-Test läuft auf Isors eigenem PC und Laptop.
Multiplayer Play Mode ist die tägliche Schleife, die beiden Geräte sind
die Abnahme. Mitspieler kommen dazu, wenn es Gameplay zu testen gibt —
und vor der Abgabe, nicht danach.
Warum: Isors Vorschlag. Er macht Phase 0 von keinem Termin abhängig, und
bei rund vier verfügbaren Wochenendtagen in zwei Wochen ist
Terminabsprache der teuerste Posten. Dazu zeigt er beide Seiten eines
Netzfehlers gleichzeitig statt einer am Telefon beschriebenen Hälfte.
Drittens haben die Geräte verschiedene CPUs — genau die Bedingung, die
der Vergleichstest braucht.
Verworfen: mit einem Mitspieler testen (Terminabhängigkeit, nur eine
sichtbare Seite); allein mit Multiplayer Play Mode auskommen — es läuft
auf einer Maschine, beweist Phase 0 damit nicht und macht den
Vergleichstest grün und wertlos. Nicht abgedeckt bleibt echte
Internet-Verzögerung: Beide Geräte hängen am selben Router.

## 2026-08-27 — Der Vergleichstest misst Anzahl und Fingerabdruck, in zwei Läufen
Was: `GenerationFingerprint` in `Assets/Scripts/Diagnostic/` rechnet Höhen
**und** Platzierungen und meldet zweierlei — die Anzahl der Platzierungen
je Typ und einen Fingerabdruck über alle Positionen. Gemessen wird in
zwei Läufen: erst Editor gegen Build auf dem PC allein, dann Build gegen
Build auf PC und Laptop.
Warum: „Gleich oder nicht" ist zu grob. Die Anzahl ist, was spielerisch
zählt; der Fingerabdruck schlägt schon bei Abweichungen an, die niemand
sieht. So gibt es drei Ausgänge statt zwei, und der mittlere — Anzahl
gleich, Fingerabdruck verschieden — ist besprechbar statt rot. Die zwei
Läufe trennen die beiden möglichen Ursachen: Editor gegen Build isoliert
Mono gegen IL2CPP ohne zweiten Rechner, Build gegen Build isoliert die
Maschine; ein einziger Lauf über beide Variablen wäre bei Rot nicht
deutbar. Dass der Test überhaupt eine Chance hat, liegt am Bestand: Der
`ObjectPlacer` zieht die Seeds je Kachel vorab auf einem Thread und führt
die Ergebnisse über den Index zusammen, nicht über die
Fertigstellungsreihenfolge — der übliche Weg, Determinismus an den
Thread-Pool zu verlieren, ist dort schon versperrt.
Verworfen: nur die Höhen vergleichen (lässt ausgerechnet die riskante
Stelle aus — die Poisson-Streuung mit Sinus, Kosinus und einem
Ablehnungstest je Punkt, wo ein einziger anders ausgefallener Vergleich
alles ab diesem Punkt ändert); nur die Platzierungen (findet die
Abweichung, sagt aber nicht, wo sie entstand); Editor gegen Build als
einziger Aufbau.

## 2026-08-28 — `async`/`await` ist bei der Sessions-API nicht wählbar
Was: Der Verbindungsaufbau läuft über `await` —
`UnityServices.InitializeAsync`, `SignInAnonymouslyAsync`,
`CreateSessionAsync` und `JoinSessionByCodeAsync` bieten nichts anderes
an. Die Rückruf-Entscheidung vom 2026-08-26 bleibt davon **unberührt**:
Sie galt `IPlayerDataService`, also einer selbst entworfenen
Schnittstelle. `ISessionService` bekommt in Phase 1 außen Rückrufe und
hält `async` innen.
Warum: Die Begründung von damals — `async` würde quer durch den ganzen
Code wandern und müsste im Prüfungsgespräch erklärt werden — trifft
weiter zu, lässt sich hier aber anders einlösen: Hinter einer Naht steht
das Sprachkonstrukt an **einer** Stelle statt an vielen. Erklären muss
Isor es trotzdem, weil es im Abgabecode steht; die Faustregel dazu
(`async void` nur für Ereignisbehandler, und dann zwingend mit
`try`/`catch`, weil eine Ausnahme dort sonst verfällt) wurde im selben
Zug erarbeitet.
Verworfen: die Sessions-API meiden, um `async` zu vermeiden — dann bliebe
nur Relay von Hand, mit mehr Code, und `async` wäre dort ebenso dabei;
`async` ungekapselt durchs Projekt wandern lassen.

## 2026-08-28 — Ein Zähler ist ein Zustand, kein Ereignis
Was: Der Ping-Zähler des Prüfstands liegt in einer `NetworkVariable<int>`
statt in einem `int`, und der Rückweg-RPC `AnnouncePingRpc` entfällt. Als
Muster gilt ab jetzt: **Was einen Wert hält, den ein später Beitretender
kennen muss, ist eine `NetworkVariable`; was einmalig passiert, ist ein
RPC.** Betrifft ab Phase 4 Lebenspunkte, Gegner-Zustände und
Bosskampf-Fortschritt.
Warum: Ein RPC verpufft — wer beim Aufruf nicht verbunden war, erfährt nie
davon. Eine `NetworkVariable` wird beim Spawnen nachgeliefert. Gemessen am
2026-08-28: Ein nach zwei Pings beigetretener Gast bekam den Stand
lautlos mit (`OnValueChanged` feuert für den Startwert **nicht**) und
meldete danach korrekt `Ping 2`. Ein Gast, der spät in einen Bosskampf
kommt, sähe sonst eine volle Lebensleiste an einem angeschlagenen Gegner.
Nebenbei fällt Code weg statt hinzuzukommen: eine Methode weniger.
Verworfen: den Zähler im `Update` des Besitzers hochzählen — der Besitzer
einer Kapsel ist nicht der Server, und die Schreibrechte einer
`NetworkVariable` liegen ab Werk beim Server; beim Gast wäre es ein
Laufzeitfehler. Beide Wege parallel führen (RPC **und** Variable) — dann
gibt es zwei Wahrheiten für denselben Wert.

## 2026-08-28 — Gebaut wird mit Mono, nicht mit IL2CPP
Was: Das Scripting-Backend bleibt auf Unitys Voreinstellung **Mono**.
IL2CPP wird nicht installiert. Damit entfällt der ursprüngliche Zweck von
Lauf 1 des Vergleichstests (Entscheidung vom 2026-08-27): Editor und Build
rechnen denselben Weg, der Vergleich wäre automatisch grün.
Warum: Die Entscheidung vom 2026-08-27 setzte stillschweigend voraus, dass
die Builds IL2CPP nutzen — das stand nirgends und war nie entschieden. Der
Unterschied Mono gegen IL2CPP ist überhaupt nur dort ein Risiko, wo zwei
Beteiligte verschiedene Backends fahren; da alle Builds aus denselben
Projekteinstellungen kommen, kann das nur zwischen Editor und Build
passieren. Sind beide Mono, existiert der Unterschied nicht. Der Preis von
IL2CPP wären 2–3 GB Modul und minutenlange Builds bis zur Abgabe, für eine
Frage, die es dann nicht gibt.
Verworfen: IL2CPP nachinstallieren, um die Entscheidung vom 2026-08-27
wörtlich zu erfüllen (Aufwand ohne Erkenntnisgewinn, solange die Abgabe
mit Mono gebaut wird); die Entscheidung erst vor der Abgabe treffen (dann
hinge Phase 0 an einer Frage, die heute beantwortbar ist).
Folge für die ROADMAP: Wechselt das Backend später doch auf IL2CPP, wird
der Fingerabdruck-Test einmal wiederholt — das Werkzeug steht.

## 2026-08-28 — Der Vergleichstest bekommt einen Lauf-gegen-Lauf-Test vorweg
Was: Vor dem Zwei-Geräte-Vergleich läuft derselbe Build **zweimal auf
derselben Maschine**, und die zwei Berichte werden verglichen. Erst danach
kommt der Hardware-Vergleich gegen den Laptop. Der Hardware-Teil ist auf
den Laptop-Tag verschoben; Phase 0 bleibt bis dahin offen, Punkt 4 und 5
sind nicht abgehakt.
Warum: Die beiden Tests finden **verschiedene** Fehler. Lauf gegen Lauf auf
einer Maschine prüft die Nebenläufigkeit — der `ObjectPlacer` rechnet über
`Parallel.For`, und Threads sind laut eigener Knowledge-Notiz der häufigste
stille Zerstörer von Determinismus. Fiele das durch, säße der Fehler im
eigenen Code, und man hätte ihn am Laptop-Tag der Hardware zugeschrieben.
Gemessen am 2026-08-28: drei Läufe, fünf Prüfsummen, alle identisch — die
Parallelisierung ist damit ausgeschlossen. Das Verschieben des
Hardware-Teils kostet nichts, weil Phase 1 und 2 den Seed nicht
verschicken; fällig ist er vor Phase 3.
Verworfen: gleich den Zwei-Geräte-Test fahren und den Lauf-gegen-Lauf-Test
weglassen (bei einem roten Ergebnis wären zwei Ursachen im Spiel gewesen);
den Hardware-Test bis Phase 3 liegen lassen (er entscheidet, wie Phase 3
gebaut wird, und muss deshalb davor fertig sein).

## 2026-08-28 — Die Bedingung des Seed-Wegs ist geprüft und erfüllt
Was: Gelände und Bewuchs werden in Phase 3 als **Seed** übertragen, nicht
als Objektliste. Die Bedingung aus dem Eintrag vom 2026-08-25 („Die
Generierung muss auf beiden Rechnern dasselbe liefern") wechselt damit von
*ungeprüft* auf *erfüllt*. Der Ausweichweg — der Host schickt alle Objekte
einzeln — wird nicht gebaut.
Warum: Gemessen am 2026-08-28 mit `GenerationFingerprint` auf zwei Geräten
verschiedener Hersteller (AMD Ryzen 7 8700G gegen Intel Core i9-14900HX):
fünf Prüfsummen, alle identisch, bei 4,7 Millionen Grasplatzierungen und
über 10,5 Millionen geprüften Kandidatenpunkten. Vorgeschaltet war ein
Lauf-gegen-Lauf-Test auf einer Maschine, der die Nebenläufigkeit als
Fehlerquelle ausschloss. Damit sind beide möglichen Ursachen einzeln
geprüft und beide grün.
Setzt voraus: **x86-64 und Mono.** Für einen ARM-Rechner oder einen
IL2CPP-Build gilt die Messung nicht; in beiden Fällen wird sie wiederholt
(`ROADMAP.md`). Die Zeile „Setzt voraus" ist der Vorschlag aus
`Kern/STOERUNGEN.md`, 2026-08-28 — hier zum ersten Mal benutzt, damit
sichtbar wird, ob sie trägt.
Verworfen: den Ausweichweg vorsorglich trotzdem bauen (Arbeit an einem
Weg, der nach Messlage nicht gebraucht wird); die Messung als endgültig
behandeln (sie gilt für zwei Geräte und eine Plattform, nicht für alle).

## 2026-08-28 — Phase 1 wird in vier Bausteine geschnitten
Was: Erstens `ISessionService` samt der drei Menüwege, noch ohne
Szenenwechsel — fertig, wenn „Welt erstellen" den Join-Code zeigt.
Zweitens der netzsynchrone Szenenwechsel mit Ladebalken in eine leere
`StarterVillage` (flacher Boden). Drittens das Spieler-Prefab als
Netzobjekt plus Eingabe-Naht (`DECISIONS/Player.md`); der Behelfsknopf
aus Phase 0 fliegt hier raus. Viertens wächst die `StarterVillage`: erst
der Terrain-Generator, danach Features nach der Übernahme-Regel.
Warum: Isors Schnitt — erst die Menüanbindung, dann das Village nach und
nach —, ergänzt um die leere Szene dazwischen: Ohne Zielszene ist der
Menüweg nur am Log prüfbar, und beim ersten netzsynchronen Szenenwechsel
soll die Generierung nicht als zweite Fehlerquelle danebenstehen. Jeder
Baustein hat so ein Ergebnis, das man am Bildschirm sieht.
Verworfen: die Menüanbindung als ein Block bauen (drei Bausteine lang
nichts Vorführbares); den Terrain-Generator schon in den Szenenwechsel-
Baustein nehmen (zwei Fehlerquellen im selben Schritt).

## 2026-08-28 — Solo startet den Host direkt und braucht kein Internet
Was: „Allein spielen" ruft `StartHost()` am NetworkManager — ohne
`UnityServices`-Anmeldung, ohne Relay, ohne Sessions-API.
`ISessionService` bekommt dafür einen dritten Weg neben Create und Join.
Warum: Die Host-Modell-Entscheidung vom 2026-08-25 stützt sich darauf,
dass ohne Internet etwas läuft — die Sessions-API verlangt aber eine
Anmeldung übers Netz. Solo ist ein Host mit einem Spieler; dem Rest des
Spiels ist der Unterschied unsichtbar, es bleibt bei einem Codepfad.
Verworfen: Solo ebenfalls über Relay laufen lassen (Internetzwang ohne
Nutzen, und Relay rechnet nach Datenmenge ab); ein eigener Offline-Pfad
am Netz vorbei (widerspricht „Solo ist eine Runde mit einem Spieler").

## 2026-08-28 — Die Pause friert nichts mehr ein
Was: Das Pausenmenü hält die Welt nicht mehr an — `Time.timeScale = 0`
im `GameController` entfällt. Pausieren heißt: Menü zeigen, Cursor
freigeben, die eigene Spieler-Eingabe abschalten. Gilt auch solo; eine
Solo-Ausnahme (allein darf einfrieren) bleibt möglich, wird aber nicht
jetzt gebaut.
Warum: Isors Entscheidung. `timeScale` wirkt nur auf der eigenen
Maschine — der Host fröre beide Spieler ein, der Gast nur sich selbst,
zwei verschiedene Fehlerbilder aus derselben Zeile. Der Preis ist
benannt: Die pausierende Figur steht angreifbar in der Welt, wie in
Koop-Spielen üblich.
Verworfen: die Host-Pause friert alle ein (der Gast steht dann grundlos
still); die Solo-Ausnahme sofort mitbauen (ein zweiter Fall — genau was
die Solo-Entscheidung vom 2026-08-25 vermeiden will).
