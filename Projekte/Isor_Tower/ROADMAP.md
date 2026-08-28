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
- [ ] **Phase 1 · Spielernaht und Einstieg** *(3 Wochen)* — Das
  Input-Asset wird nach Reichweite geteilt, der Motor bekommt seine
  Eingabe gereicht statt sie zu holen, das Spieler-Prefab wird zum
  Netzobjekt mit sichtbarem Körper. Dazu der Einstieg über das bestehende
  Hauptmenü: allein spielen, Welt erstellen, Welt beitreten; der
  Ladebalken wartet auf mehrere statt auf einen. Der Verbindungsaufbau
  bekommt hier seine Naht — `ISessionService`, damit ein späterer
  Steam-Transport eine Datei kostet und keinen Umbau.
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
  weit die sofortige Trefferanzeige beim Gast vorgreifen muss.
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
- [ ] **Projektnamen im Cloud-Dashboard kürzen** — er heißt
  `Isor Tower ProtoTyp 2026 2026-07-03_17-11-35` und trägt einen
  angehängten Zeitstempel, der das Suchen erschwert. Kosmetisch, kein
  Termin. *(Relay und Player Authentication sind seit dem 2026-08-28
  freigeschaltet — Beleg im `LOG.md`.)*

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
