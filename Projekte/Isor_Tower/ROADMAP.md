# ROADMAP.md — Baureihenfolge Isor's Tower

Ownership: Nur was am Projekt als Nächstes gebaut wird. Was gerade dran
ist, steht in `PLAN.md`; was fertig ist, in `LOG.md`; warum es so
entschieden wurde, in `DECISIONS/`; was das Spiel sein soll, in `GDD.md`;
was aus Semester 2 dasteht und was dabei auffiel, in `ALTSTAND.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`
Die Reihenfolge der Phasen ist **verbindlich**: Jede setzt voraus, was die
vorige fertiggestellt hat.

**Diese Datei wurde am 2026-08-26 geleert und neu geschrieben.** Semester
3 ist ein Neustart desselben Projekts (`DECISIONS/Multiplayer.md` →
„Semester 3 ist ein Neustart desselben Projekts"); der alte Inhalt ist
kein Auftrag mehr und steht als Prüfliste in `ALTSTAND.md`.

## Semester 3 — der Koop-Prototyp

Jede Phase ist für sich vorführbar. Der Umfang braucht rund 23 Wochen bei
18 Semesterwochen plus 6 Wochen Vorlauf — die Rechnung geht nur auf, wenn
die ersten beiden Phasen vor den Semesterstart fallen. Wird es dennoch
eng, ist der Village-Koop aus Phase 6 der Posten zum Streichen; die
Kernschleife bleibt dann vollständig vorführbar.

### Vor dem Semesterstart

- [x] **Phase 0 · Netz-Prüfstand** *(2 Wochen)* — **abgeschlossen am
  2026-08-28**, alle fünf Abnahmepunkte (`LOG.md`). Der Vergleichstest ist
  bestanden: Der Seed-Weg trägt, der Ausweichweg entfällt
  (`DECISIONS/Multiplayer.md`, „Die Bedingung des Seed-Wegs ist geprüft und
  erfüllt"). Eine nackte Szene
  `NetTestbed.unity`: flacher Boden, zwei Kapseln, sonst nichts. Netcode for GameObjects
  installieren, Verbindung über Join-Code herstellen, Besitz und
  Nachrichten verstehen. Der Verbindungsknopf ist hier ein Behelf und
  fliegt in Phase 1 wieder raus. Dazu der erste Vergleichstest, ob die
  Generierung auf zwei Rechnern dasselbe liefert — die ungeprüfte
  Bedingung aus `DECISIONS/Multiplayer.md` → „Der Floor kommt gemischt
  herüber: Seed plus Objekte". Fällt der Test durch, wandert der
  Floor-Aufbau von „Seed" nach „Host schickt Objekte", und die
  Zeitrechnung wird enger.
  *Fertig heißt:* Fünf Punkte stehen — Verbindung über den Join-Code,
  Besitz (jeder steuert nur seine Kapsel), Nachrichten in beide
  Richtungen, gelaufener Vergleichstest, und ein Windows-Build läuft auf
  dem Laptop. Geprüft wird auf PC und Laptop statt mit einem Mitspieler
  (`DECISIONS/Multiplayer.md`, 2026-08-27). Die Szene bleibt dauerhaft
  als Diagnose-Szene stehen.
- [ ] **Phase 1 · Spielernaht und Einstieg** *(3 Wochen)* — geschnitten
  in vier Bausteine (`DECISIONS/Multiplayer.md`, 2026-08-28), jeder mit
  sichtbarem Ergebnis:
  - [x] **Baustein A · `ISessionService` und die drei Menüwege** —
    **abgenommen am 2026-08-28** (`LOG.md`): Code im Lobby-Label,
    Fehlweg geprüft. Der Menü-Aufbau wurde dabei zur Panel-Kette mit
    Lobby (`DECISIONS/UI.md`). Allein
    spielen (`StartHost()` direkt, kein Internet), Welt erstellen, Welt
    beitreten. Noch ohne Szenenwechsel; fertig, wenn „Welt erstellen"
    den Join-Code im Menü zeigt.
  - [ ] **Baustein B · Netzsynchroner Szenenwechsel und Ladebalken** —
    Zielszene ist eine leere `StarterVillage` mit flachem Boden; der
    Ladebalken wartet auf mehrere statt auf einen. Fertig, wenn Host und
    Gast nach dem Klick in derselben Szene stehen.
  - [ ] **Baustein C · Spieler-Prefab als Netzobjekt und Eingabe-Naht** —
    `NetworkObject` plus sichtbarer Körper, `PlayerInputRelay` reicht die
    Eingabe (`DECISIONS/Player.md`, 2026-08-28), Kamera und AudioListener
    nur auf der eigenen Figur. Der Behelfsknopf und `NetTestPlayerMover`
    aus Phase 0 fliegen hier raus. Dazu: die Pause erreicht jetzt die
    Relay-Komponente statt des Assets, und `Time.timeScale = 0` entfällt
    (`DECISIONS/Multiplayer.md`, 2026-08-28, „Die Pause friert nichts
    mehr ein").
  - [ ] **Baustein D · `StarterVillage` wächst** — der Terrain-Generator
    kommt in die Szene, danach Features einzeln nach der Übernahme-Regel.
  *Fertig heißt:* Spiel starten, im Menü eine Welt erstellen, Code
  weitergeben, zusammen durch `StarterVillage` laufen — die Zielszene ist
  von Anfang an das Village, keine Wegwerf-Testwelt
  (`DECISIONS/Multiplayer.md`, 2026-08-27).

### Im Semester

- [ ] **Phase 2 · Datenskelett und Schnittstelle** *(2 Wochen)* —
  `PlayerProfile` und `WorldState` als Struktur, dazu
  `IPlayerDataService` mit der lokalen Attrappe dahinter. Beides zusammen
  und nicht nacheinander: Wer die Schnittstelle später einzieht, hat bis
  dahin überall Code, der daran vorbeischreibt.
  *Fertig heißt:* Jedes neue System weiß beim Bauen, in welchen Topf es
  schreibt und durch welche Tür.
- [ ] **Phase 3 · Floor_1 und das Portal** *(4 Wochen)* — Die neue Szene
  `Floor_1`, das Portal mit Gruppenbestätigung, die Seed-Übertragung, der
  gemischte Aufbau und der Ladebalken im Netz-Modus. Das Gelände ist
  bewusst ein Platzhalter aus der bestehenden Pipeline; verbindlich ist
  nur der Vertrag „Seed rein, Welt raus".
  *Fertig heißt:* Ihr geht gemeinsam durchs Portal und steht beide in
  derselben erzeugten Welt. Der schwierigste Einzelschritt des Semesters.
- [ ] **Phase 4 · Kampf** *(4 Wochen)* — Nahkampf zuerst, Fernkampf
  danach. Der Gast meldet den Schlag, der Host prüft und rechnet; die
  Trefferanzeige läuft beim Gast sofort. Gegner bekommen den
  Sichtbarkeitsfilter nach Entfernung. Dazu Tod, Liegen und Aufhelfen.
  *Fertig heißt:* Ihr besiegt gemeinsam einen Gegner, und wer fällt, kann
  vom anderen aufgeholfen bekommen.
- [ ] **Phase 5 · Beute und Inventar** *(3 Wochen)* — Der Host würfelt je
  Spieler getrennt, jeder sieht nur seine eigene Beute. Das Inventar
  schreibt ins `PlayerProfile` und reist damit mit.
  *Fertig heißt:* Dein Mitspieler verlässt deine Welt mit Beute, die in
  seiner eigenen Welt noch da ist.
- [ ] **Phase 6 · StarterVillage und Speichern** *(3 Wochen)* — Die neue
  Village-Szene als Hub, koop-fähig. Jetzt bekommt `WorldState` seine
  Datei, weil es zum ersten Mal etwas zu speichern gibt, das eine Sitzung
  überdauern muss. `Village.unity` bleibt daneben unangetastet.
  *Fertig heißt:* Die Kernschleife ist geschlossen — Dorf, Portal, Floor,
  Beute, zurück, beenden, wieder starten, alles noch da.
- [ ] **Puffer · Politur und Abgabe** *(2 Wochen)* — Reserve für das, was
  überzieht, plus das Abgabedokument. Nicht verhandelbar: Verloren wurde
  im letzten Semester an der Fertigstellung, nicht am Können.

## Eigene Design-Sessions

- [ ] **Floor-Generierung und Floor-Inhalt** — Wie viel eines Floors ist
  frei generiert, wie viel aus festen Bausteinen kombiniert? Dazu Mobs,
  Spezialmonster und Boss. Beantwortet die offene Frage im `GDD.md` →
  „Generierungsanteil". **Blockiert den Netzbau nicht** — die frühen
  Phasen laufen ohne sie (`DECISIONS/Multiplayer.md` → „Wie ein Floor
  entsteht, blockiert den Netzbau nicht"). Fällig, bevor Floor 1 echten
  Inhalt bekommt.
- [ ] **Village-Terrain** — handgebaut, mit einem Tool erweitert, oder
  einmalig generiert und eingefroren? Offene Frage im `GDD.md` →
  „Village-Terrain". Fällig vor Phase 6.
- [ ] **Spielersteuerung** — für das richtige Spiel wird sie neu
  entworfen statt aus Semester 2 übernommen (Isor, 2026-08-28). Offene
  Frage im `GDD.md` → „Spielersteuerung". **Blockiert den Prototyp
  nicht:** Phase 1 macht die bestehende Steuerung nur netzfähig, das
  bleibt unverändert. Fällig nach dem Prototyp.

## Kleinere offene Punkte des Netzbaus

Aus der Design-Session vom 2026-08-25/26; leicht zu vergessen, jeder für
sich klein.

- [ ] **Versionsprüfung beim Beitritt** — Zwei verschieden alte Builds
  dürfen sich nicht verbinden, sonst driften die Welten auseinander.
  Fällig in Phase 3.
- [ ] **Wiederverbindung des Gastes** — Der Fall „Host geht" ist
  entschieden, der Fall „Gast fliegt raus und kommt zurück" nicht.
  Fällig in Phase 3.
- [ ] **Umlaufzeit im Prüfstand anzeigen** — Am 2026-08-28 hieß der Befund
  „Ping kam sofort"; das ist ein Eindruck, keine Zahl. NGO liefert die
  Umlaufzeit über `GetCurrentRtt(clientId)`. Ein Feld im `NetTestbed` macht
  daraus eine Messung. Fällig in Phase 4: Dort entscheidet die Zahl, wie
  weit die sofortige Trefferanzeige beim Gast vorgreifen muss. Die
  Lobby-Liste zeigt die Umlaufzeit schon ab Baustein B (`DECISIONS/UI.md`,
  2026-08-29); der Prüfstand-Teil bleibt davon unberührt.
- [ ] **Reichweite des Sichtbarkeitsfilters messen** — Die 40–50 Gegner
  aus dem `GDD.md` sind eine Anzahl, keine Messung. Fällig in Phase 4.
- [ ] **Fingerabdruck-Test wiederholen, falls das Backend wechselt** — Mono
  ist gesetzt (`DECISIONS/Multiplayer.md`, 2026-08-28). Ein späterer Wechsel
  auf IL2CPP macht die Messung vom 2026-08-28 ungültig, weil sie dann einen
  Rechenweg misst, der nicht mehr ausgeliefert wird. Fällig nur im
  Wechselfall, dann aber vor der Abgabe.
- [ ] **Ausschlusszonen in den Vergleichstest aufnehmen** — der Prüfstand
  misst die Ausgabe des `ObjectPlacer`; der `PlacementExclusionFilter` läuft
  als eigene Stufe danach und bleibt ungemessen. Kein Termin: Die riskante
  Stelle ist die Poisson-Streuung, nicht der Formtest. Fällig, wenn der Test
  einmal als vollständige Abnahme der Weltgleichheit gelten soll.
- [x] **Session auflösen beim Verlassen der Lobby** — **gebaut und geprüft
  am 2026-08-30** (`LOG.md`): `Leave()` als vierter Weg, `SessionEnded`
  wirft Gäste sauber raus, der Sitzplatz beim Dienst wird mit freigegeben.
  Ursprünglicher Befund vom 2026-08-28 („Already connected.") behoben.
- [ ] **Lobby-Ausbau: Spielerliste und Ready-System** — **entschieden am
  2026-08-29** (`DECISIONS/UI.md` und `DECISIONS/Multiplayer.md`): Liste
  mit Name · Haken · Ping über je ein `LobbyPlayer`-Objekt, Ready als
  Anzeige statt Sperre, davor das neue Host-Optionen-Panel. Fällig in
  Phase 1, Baustein B/C — braucht die Verbunden-Meldungen des
  NetworkManagers.
- [ ] **Lobby-Chat bauen** — Verlauf (die letzten ~6 Zeilen, Luft für vier
  Schreiber) plus Eingabezeile, Enter sendet; RPC plus Textliste, der
  Platz auf der Tafel ist ab Baustein B reserviert (`DECISIONS/UI.md`,
  2026-08-29). Fällig nach Baustein C, sobald Verbinden, Spawnen und
  gemeinsames Laufen stehen — vorgezogen aus „Lobby-Komfort".
- [ ] **Meldung „Lobby geschlossen" beim Rauswurf** — der Gast landet heute
  kommentarlos auf der Host/Join-Wahl; Isor wünscht ein Bestätigungsfenster
  mit Okay (2026-08-30). **Formfrage offen:** kollidiert mit der
  Popup-Verwerfung vom 2026-08-28 (`DECISIONS/UI.md`) — beim UI-Feinschliff
  von Phase 1 bewusst entscheiden: Tafel-konforme Meldefläche oder
  Revision des Eintrags.
- [ ] **Rauswurf im Spiel: zurück ins Hauptmenü** — geht der Host, während
  alle schon in der `StarterVillage` stehen, bleibt der Gast einfach in
  der Welt stehen (Befund aus dem Paartest, 2026-08-30). Der
  `SessionEnded`-Weg endet heute im Menü — in der Spielszene hört niemand
  mehr zu, weil der `MainMenuController` mit seiner Szene starb. Braucht
  einen In-Game-Horcher, der lokal zurück in die MainMenu-Szene lädt
  (plus die Meldung aus dem Punkt oben). Fällig in Baustein C, wo die
  Spielszene ihre Netz-Seite bekommt — spätestens mit ihrem Pausenmenü.
- [ ] **AudioListener-Doppel beobachten** — trat am 2026-08-30 einmal auf
  (93.000 Warnungen: „2 audio listeners"), danach nicht reproduziert; das
  Kapsel-Prefab trägt keinen. Falls wieder: im Play Mode Hierarchy-Suche
  `t:AudioListener`, Objektnamen notieren. Löst sich spätestens mit
  Baustein C (Kamera und Listener nur auf der eigenen Figur).
- [ ] **Artifact-Seite `⚙️ System · Grundgerüst` nachziehen** — der
  Menü-Umbau vom 2026-08-28 (Panel-Kette, `ISessionService`,
  `MainMenuController`) veraltet die Seite; Befund aus dem Review-Gate.
  Fällig beim nächsten Pflegetag.
- [ ] **Stick-Umsehen dreht bildratenabhängig** — `PlayerLook` rechnet
  Maus und Stick gleich (`lookInput * _sensitivity`, ohne `deltaTime`).
  Für die Maus ist das richtig (ihr Wert ist eine Strecke), der Stick
  liefert aber eine Auslenkung: Bei 120 fps dreht dieselbe Stickstellung
  doppelt so schnell wie bei 60. Getrennter Rechenweg je Quelle nötig.
  Fällig in Phase 1, Baustein C — dort wird `PlayerLook` ohnehin umgebaut.
- [ ] **FastForward hat keine Gamepad-Bindung** — die Action kennt nur
  `T`; alle anderen Actions haben ein Gamepad-Pendant. Eine Zeile im
  `PlayerControls`-Asset. Kosmetisch, kein Termin.
- [ ] **Join-Code-Eingabe geht nur mit Tastatur** — das `TMP_InputField`
  verlangt eine; mit dem Controller allein kommt niemand in eine fremde
  Welt. Entweder eine Zeichen-Auswahl bauen oder die Code-Eingabe bewusst
  zur Tastatur-Sache erklären; auf Steam löst das Overlay das später von
  selbst. Weggabelung, fällig in Phase 1, Baustein A.
- [ ] **Vorspulen wirkt nur lokal** — `TimeFastForward` beschleunigt die
  eigene `IngameTime`; drückt der Gast `T`, ist bei ihm Nacht und beim
  Host Tag. Fällig, sobald die Ingame-Uhr ins Netz kommt — spätestens,
  wenn Gegner oder Schafe nach Tageszeit handeln sollen.
- [ ] **Projektnamen im Cloud-Dashboard kürzen** — er heißt
  `Isor Tower ProtoTyp 2026 2026-07-03_17-11-35` und trägt einen
  angehängten Zeitstempel, der das Suchen erschwert. Kosmetisch, kein
  Termin. *(Relay und Player Authentication sind seit dem 2026-08-28
  freigeschaltet — Beleg im `LOG.md`.)*
- [ ] **Steam-Profilbild in der Spielerliste** — Isors Vorschlag vom
  2026-09-01, von ihm selbst als verfrüht eingeschätzt: Es hängt an einer
  App-ID, die es erst nach der Steam-Direct-Gebühr gibt. Fällig
  frühestens mit „Steam-Transport statt Unity Relay"; bis dahin trägt die
  Liste nur Name, Haken und Ping.
- [ ] **`MainMenuController` teilen** — mit 283 Zeilen noch gesund, aber
  wachsend. Die Naht liegt zwischen **Session** (die vier Menüwege und
  die Dienst-Rückrufe) und **Navigation** (welches Panel sichtbar ist,
  Back-Ziele, Label-Rücksetzung) — **nicht** zwischen Panels und Knöpfen,
  denn ein Knopfdruck *ist* ein Panelwechsel. Auslöser ist Baustein B,
  Schritt 5: Die Spielerliste bringt Spawnen und Listenpflege mit und
  damit die zweite echte Verantwortung. Vorher wäre der Schnitt auf
  Verdacht.
- [ ] **Späteinstieg entscheiden** — Beim Test am 2026-09-04 jointe ein
  Gast in die laufende Runde, und NGO schickte ihn automatisch in die
  Szene. Heute ist die `StarterVillage` leer, nichts kann auseinander-
  laufen — sobald Terrain und Platzierung drin sind, braucht der Späte
  denselben Seed und Weltzustand, oder der Beitritt endet an der Lobby.
  Fällig in Phase 3, wo der Seed ohnehin übers Netz geht.
- [ ] **Solo-Ladebalken gegen die Glättungsregel prüfen** — Beim Test war
  kein Balken zu sehen; die Regel vom 2026-08-19 verspricht mindestens
  zwei Sekunden Anzeige. Entweder greift die Glättung im Netz-Ladeweg
  nicht, oder der Moment war schlicht zu kurz zum Hinsehen. Ein Blick in
  den `LoadingScreenController`, klein.
- [ ] **UI-Bausteine als Prefabs** — Isors Vorschlag vom 2026-09-04,
  als Design-Runde vor Schritt 5: StandardButton (mit leerer
  OnClick-Liste — entschärft die Duplikat-Falle an der Wurzel),
  Tafel-Hülle (Schleier + Content), InputRow. Die Spielerlisten-Zeile
  kommt ohnehin dazu, sie wird zur Laufzeit je Spieler instanziiert.
  Bewertung liegt vor (Chat vom 04.09.), entschieden wird in der Runde.
- [ ] **Namespace-Nachmittag vor Phase 2** — Befund aus dem Zeugnis vom
  2026-09-04, dritter Messpunkt mit 0 von inzwischen 100 Dateien in einem
  `namespace`. Der Semester-3-Code wäre reif; der Umzug wird mit jeder
  Datei teurer. Ein Nachmittag, solange der Bestand überschaubar ist.
- [ ] **UI-Feinschliff Phase 1, Sammelpunkt** — Panel-Größen
  vereinheitlichen oder wachsen lassen (Isors Frage vom 04.09.) · das
  Join-Feld ist mit 160×30 der Winzling unter den Eingaben · eine
  Solo-Fehlermeldung liefe heute ins unsichtbare Lobby-Label · das
  Textkind des `ConfirmButton` wieder sprechend benennen. Nichts davon
  blockiert; fällig mit dem bestehenden Feinschliff der Phase 1.

## Nach dem Prototyp

Aus dem Semesterschnitt herausgenommen (`DECISIONS/Multiplayer.md` →
„Semesterschnitt: was in den Prototyp kommt"). Zielbild bleibt, Zeitpunkt
offen.

- [ ] **Bauen und Dekorieren im Koop** — Grid mit Snapping, kaufbare
  Häuser, und die Frage, welcher Datentopf eine Gaständerung behält.
- [ ] **Handwerk** — Schmieden, Kochen, Tränke; Rezepte reisen im
  `PlayerProfile` mit.
- [ ] **Quests über die Adventure Guild** — der schwierigste
  Mitnahme-Fall, weil die Quest-Stände zweier Welten verschieden sind.
- [ ] **Shop** — Zeitpunkt offen, möglicherweise erst Semester 4 oder
  später. Findet die Datenschnittstelle aus Phase 2 vor.
- [ ] **Host-geprüfte Bewegung** — wann und ob die Tür benutzt wird, die
  die Input-Naht offenhält.
- [ ] **Lobby-Komfort** — Voice (eigenes System, Unity Vivox) und
  Spieler entfernen (Kick). Gewünscht am 2026-08-28, bewusst hinter den
  Prototyp gestellt. Der Text-Chat stand ursprünglich mit hier drin und
  wurde am 2026-08-29 vorgezogen — jetzt eigener Punkt „Lobby-Chat
  bauen" unter den offenen Punkten des Netzbaus.
- [ ] **Steam-Transport statt Unity Relay** — sobald eine App-ID
  existiert. Betroffen ist nur die Transportschicht hinter
  `ISessionService`; zu prüfen ist dann, ob ein Community-Transport zur
  dann aktuellen NGO-Version passt (`DECISIONS/Multiplayer.md`,
  2026-08-27).
- [ ] **Portfolio-Präsentation** (erst wenn eine Bewerbung ansteht):
  spielbarer Build aus der Build-Ablage (`Kern/VERSIONIERUNG.md` →
  „Ablage der Builds"), Video oder GIFs, gezielte Lese-Einladung ins
  private Repo; bei Bedarf ein kuratiertes Showcase-Repo mit nur eigenen
  Skripten. Das Projekt-Repo selbst bleibt dauerhaft privat
  (`Kern/DECISIONS.md` → „Sichtbarkeit und Zugang der Repos").
  *(Von der Parallel-Session am 2026-08-26 ergänzt, hier unverändert
  übernommen — er gehört nicht zum Altstand.)*
