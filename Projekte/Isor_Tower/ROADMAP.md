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

- [ ] **Phase 0 · Netz-Prüfstand** *(2 Wochen)* — Eine nackte Szene:
  flacher Boden, zwei Kapseln, sonst nichts. Netcode for GameObjects
  installieren, Verbindung über Join-Code herstellen, Besitz und
  Nachrichten verstehen. Der Verbindungsknopf ist hier ein Behelf und
  fliegt in Phase 1 wieder raus. Dazu der erste Vergleichstest, ob die
  Generierung auf zwei Rechnern dasselbe liefert — die ungeprüfte
  Bedingung aus `DECISIONS/Multiplayer.md` → „Der Floor kommt gemischt
  herüber: Seed plus Objekte". Fällt der Test durch, wandert der
  Floor-Aufbau von „Seed" nach „Host schickt Objekte", und die
  Zeitrechnung wird enger.
  *Fertig heißt:* Du und dein Mitspieler seid über das Internet verbunden
  und seht euch laufen. Die Szene bleibt als Prüfstand stehen.
- [ ] **Phase 1 · Spielernaht und Einstieg** *(3 Wochen)* — Das
  Input-Asset wird nach Reichweite geteilt, der Motor bekommt seine
  Eingabe gereicht statt sie zu holen, das Spieler-Prefab wird zum
  Netzobjekt mit sichtbarem Körper. Dazu der Einstieg über das bestehende
  Hauptmenü: allein spielen, Welt erstellen, Welt beitreten; der
  Ladebalken wartet auf mehrere statt auf einen.
  *Fertig heißt:* Spiel starten, im Menü eine Welt erstellen, Code an den
  Mitspieler schicken, zusammen durch die Testwelt laufen.

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

## Kleinere offene Punkte des Netzbaus

Aus der Design-Session vom 2026-08-25/26; leicht zu vergessen, jeder für
sich klein.

- [ ] **Versionsprüfung beim Beitritt** — Zwei verschieden alte Builds
  dürfen sich nicht verbinden, sonst driften die Welten auseinander.
  Fällig in Phase 3.
- [ ] **Wiederverbindung des Gastes** — Der Fall „Host geht" ist
  entschieden, der Fall „Gast fliegt raus und kommt zurück" nicht.
  Fällig in Phase 3.
- [ ] **Reichweite des Sichtbarkeitsfilters messen** — Die 40–50 Gegner
  aus dem `GDD.md` sind eine Anzahl, keine Messung. Fällig in Phase 4.

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
- [ ] **Portfolio-Präsentation** (erst wenn eine Bewerbung ansteht):
  spielbarer Build aus der Build-Ablage (`Kern/VERSIONIERUNG.md` →
  „Ablage der Builds"), Video oder GIFs, gezielte Lese-Einladung ins
  private Repo; bei Bedarf ein kuratiertes Showcase-Repo mit nur eigenen
  Skripten. Das Projekt-Repo selbst bleibt dauerhaft privat
  (`Kern/DECISIONS.md` → „Sichtbarkeit und Zugang der Repos").
  *(Von der Parallel-Session am 2026-08-26 ergänzt, hier unverändert
  übernommen — er gehört nicht zum Altstand.)*
