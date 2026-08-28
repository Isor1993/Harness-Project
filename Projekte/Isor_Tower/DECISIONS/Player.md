# Player.md — Entscheidungen Spielerfigur und Steuerung

Ownership: Nur Entscheidungen zur Spielerfigur und ihrer Steuerung — was
entschieden wurde, warum, und welche Alternativen verworfen wurden. Kein
Plan (das ist die ROADMAP), kein Ereignis (das ist das LOG), keine
Design-Absicht des Spiels (das ist das `GDD.md`).
Nicht hier: wer im Netz worüber entscheidet (`Multiplayer.md`), die
Bedienoberfläche (`UI.md`), das Verhalten der Wesen (`Entities.md`).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

Diese Datei entstand am 2026-08-28, weil die Entscheidung unten sonst
kein Zuhause gehabt hätte: `GDD.md` und die ROADMAP tragen das Was, nicht
das Warum.

## 2026-08-28 — Die Steuerung wird für das richtige Spiel neu entworfen
Was: Die First-Person-Steuerung aus dem zweiten Semester —
`PlayerInputReader`, `PlayerMotor`, `PlayerLook`, `PlayerInteractor` —
bleibt im Prototyp in Betrieb und wird dort nur netzfähig gemacht. Für
das richtige Spiel wird sie **neu entworfen** statt weiter angepasst.
Wie sie sich anfühlen soll, ist offen und steht als Frage im `GDD.md` →
„Spielersteuerung".
Warum: Isors Entscheidung. Ausführlich begründet ist sie nicht;
festgehalten ist die Richtung — was im zweiten Semester als Lernstück
entstand, trägt den Prototyp, soll aber nicht der Stand des fertigen
Spiels sein. Die Übernahme-Regel kennt drei Antworten (*mitnehmen*,
*anpassen*, *neu*); für diesen Baustein lautet sie über den Prototyp
hinaus **neu**.
Verworfen: die bestehende Steuerung dauerhaft weiterentwickeln; den
Neuentwurf schon im Prototyp angehen — er blockiert nichts, und Phase 1
braucht von der Steuerung nur die Netzfähigkeit.

## 2026-08-28 — Die Eingabe wird der Figur gereicht: eine Push-Komponente je Spieler
Was: Eine neue Komponente `PlayerInputRelay` auf dem Spieler-Prefab liest
die Actions aus `PlayerControls` — nur beim Besitzer — und reicht die
Werte per Methodenaufruf weiter (`SetMoveInput`, `SetLookInput`,
`RequestJump`, `RequestInteract`). `PlayerMotor`, `PlayerLook` und
`PlayerInteractor` verlieren ihre `PlayerInputReader`-Referenz und kennen
ihre Quelle nicht mehr. `GameController` und `TimeFastForward` bleiben am
geteilten Asset.
Warum: Wörtliche Umsetzung von „der Motor bekommt sie gereicht"
(`Multiplayer.md`, 2026-08-25). Host-geprüfte Bewegung tauscht später
genau eine Datei — die Komponente, die die Methoden aufruft — statt drei.
Controller-Tauglichkeit hängt nicht an dieser Wahl: Der Relay liest
Actions, nicht Tasten, und die Gamepad-Bindungen stehen bereits im
`PlayerControls`-Asset.
Verworfen: Pull mit einer Komponente je Figur als abgefragter Quelle
(kleinster Eingriff heute, aber bei host-geprüfter Bewegung fehlte die
Naht dann doch); ein `IInputSource`-Interface mit zwei Umsetzungen
(Abstraktion auf Verdacht, solange nur eine existiert — dieselbe
Begründung wie beim Verschieben von `ISessionService` auf Phase 1).
Folge, als ROADMAP-Punkt: Die Pause muss danach die Relay-Komponente des
eigenen Spielers erreichen — `EnableUI()` am Asset schaltet die Figur
nicht mehr still.
