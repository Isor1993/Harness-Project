# ROADMAP.md — Bauplan Game Jam Semester 3

Ownership: Nur was an Isors Teil des Game Jams als Nächstes gebaut wird
— Bausteine und offene Absprachen mit dem Team. Warum etwas so
geschnitten ist, steht in den DECISIONS dieser Schicht; was passiert
ist, im LOG; die Termine besitzt `Uni/Semester_3/STUNDENPLAN.md`.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

Zielfenster: Game-Jam-Review **Do 15.10.**. Das Spiel: 2D-Jump'n'Run
mit zwei Welten in einer Szene, übereinander wie ein Filmstreifen. In
der **bunten Welt** sammelt der Spieler Farbeimer und besiegt Gegner;
jeder besiegte Gegner hinterlässt ein Portalpaar. In der **Skizzenwelt**
fehlt die Farbe — dort werden die Sprites mit den Eimern angemalt.

## Bausteine

- [x] **J1 · IInteractable** — Vertrag für alles, womit der Spieler
  interagiert. **Erledigt am 2026-10-10:**
  `Assets/Scripts/Interfaces/IInteractable.cs`, gepusht.
- [x] **J2 · Color Bucket** — einsammelbare Farbladung über
  IInteractable. **Erledigt am 2026-10-10:**
  `Assets/Scripts/ColorBucket/ColorBucket.cs`. Offen: Inventar-Anschluss
  (TODO in der Datei), sobald das Inventar steht.
- [x] **J3 · Portal** — teleportiert einmal zur per `Init` übergebenen
  Position und zerstört sich. **Erledigt am 2026-10-10:**
  `Assets/Scripts/Portal/Portal.cs`, gepusht.
- [x] **J4 · Scene Change** — Menü ↔ Spielszene, Lade-Panel optional.
  **Erledigt am 2026-10-11:** `Assets/Scripts/SceneLoader/SceneLoader.cs`,
  Szene `Menu` auf Platz 0, gepusht.
- [x] **J5 · Enemy** — Leben, Tod mit Portalpaar, Patrol, Sicht,
  Attack, Kontaktschaden. **Erledigt am 2026-10-10:**
  `Assets/Scripts/Enemy/Enemy.cs` und `Interfaces/IDamageable.cs`,
  gepusht (J5a Isor, J5b/J5c Claude).
- [x] **J6 · Paintable** — Überblenden zur bunten Sprite. **Erledigt am
  2026-10-11:** `Assets/Scripts/Paintable/Paintable.cs`, gepusht. Offen:
  Eimer-Prüfung und -Abzug (zwei TODOs), sobald das Inventar steht.

Alle Bausteine am 2026-10-11 in der lokalen Sandbox durchgetestet
(LOG dieser Schicht).

## Mit dem Team zu klären

- [ ] **Inventar anschließen** — sobald der Player-Programmierer Player
  und Inventar gebaut hat: Methodennamen absprechen, dann die drei TODOs
  füllen (Eimer +1, Paintable prüft ≥ 1, Paintable −1).
- [ ] Wie der Player interagierbare Objekte findet (Trigger, Raycast …)
  — davon hängt der Collider2D der Prefabs ab.
- [ ] Wie der Spieler Gegner trifft (Angriffstaste oder Draufspringen) —
  Entscheidung des Player-Programmierers; der Gegner ist für beides
  fertig.
- [x] Paket *2D Sprite* — **angelegt und gepusht am 2026-10-11**, dazu
  die Layer Player und Enemy.
