# GDD.md — Isor's Outbreak

Ownership: Design-Absicht des Spiels Isor's Outbreak (Arbeitstitel) —
was es sein soll, nicht wie es gebaut wird. Begründungen gehören in die
DECISIONS dieser Schicht, Aufgaben in die ROADMAP, Technik ins spätere
TDD. Aufbau und Pflege regelt `Kern/GDD_RULES.md`.
Format: feste Kapitelfolge nach `Kern/GDD_RULES.md`; offene Punkte als
`**Offen:**` im Kapitel und gesammelt unter „Offene Design-Fragen";
Rohes datiert im Abschnitt „Entwurf".

## Pitch

Bis zu vier Abenteurer gründen auf einer wilden Insel einen
Gilden-Außenposten: Mauern, Werkbänke, ein eigenes Labyrinth. Ein Timer
zählt auf den nächsten Outbreak herunter — Wellen von Fantasywesen, die
aus den Dungeons der Insel brechen und die Basis zerlegen wollen.
Zwischen den Wellen schwärmt der Trupp aus und sammelt Material; je
weiter draußen, desto besser die Beute, und die Gier gegen die Uhr ist
der eigentliche Endgegner.

## Kern-Schleife

Sammeln, solange der Timer läuft → an der Basis bauen und schmieden →
den Outbreak abwehren → verschnaufen, einlagern, reparieren → nächste
Runde, eine Stufe härter. Die Wellen sind endlos und werden stärker;
das Ziel einer Partie ist, die höchste Welle zu erreichen. Die Gegner
wollen an die Basis — wer sich in den Weg stellt oder baut, lenkt sie
auf sich; Gebautes schützt, lenkt und kann zerbrechen.

Getrennte Ströme füttern die Schleife: Material aus der Welt (Holz,
Stein, Erz) baut die Festung aus, Beute aus den Wellen entwickelt die
Waffen. Jeder Spieler trägt ein begrenztes eigenes Inventar und legt im
Team-Lager ab — volle Taschen erzwingen Rückwege, und genau daraus
entsteht die Spannung der Sammel-Phase.

**Offen:** Verloren-Kriterium und Partielänge — siehe „Offene
Design-Fragen".

## Welt-Struktur

Eine große Insel; das Wasser ist die natürliche Spielfeldgrenze. Auf
der Insel verteilt liegen feste, sichtbare Dungeons — die Quellen der
Outbreaks — und die Materialvorkommen; das beste Material liegt
gefährlich nah an fremden Dungeons. Aktiv sind nur die Dungeons in
einem Radius um das Dorf; mit steigenden Wellen erwachen weitere, und
der Druck kommt aus neuen Richtungen.

Die Partie beginnt mit der Gründung: Die Spieler wachen auf der Insel
auf, tragen die Werkbank im Gepäck und setzen sie frei — wo die Bank
steht, steht das Dorf. Wer nach etwa vier Minuten nicht gesetzt hat,
bekommt einen Platz in der Nähe zugewiesen; der erste Outbreak kommt
nach etwa sieben bis acht Minuten.

**Offen:** Inselgröße und Universum — siehe „Offene Design-Fragen".

## Spieler

Dritte Person, die eigene Figur bleibt sichtbar, mit der Möglichkeit
weiter herauszuzoomen. Ein bis vier Spieler; solo vollwertig spielbar,
zu viert am besten. Es gibt kein Klassensystem: Die Waffe entscheidet,
was man ist. Jede Waffe bringt ihren eigenen Basisangriff auf dem
Normalklick mit, dazu eine Leiste aus vier befüllbaren
Fähigkeiten-Slots. Waffen liegen im Lager, werden dort entwickelt und
jederzeit getauscht — Rollenwechsel ist ein Griff ins Regal, keine
Menüentscheidung. Zum Start gibt es wenige Waffen (im Prototyp ein
Nahkampf, ein Fernkampf); kreative und witzige Waffen sind
ausdrücklich Teil der Absicht.

**Offen:** Slot-Befüllung, Fall beim Outbreak und Waffen-Entwicklung —
siehe „Offene Design-Fragen".

## Persistenz

Innerhalb einer Partie wächst alles — Festung, Waffen, Lager. Was über
die Partie hinaus bleibt, ist bewusst noch nicht entschieden.

**Offen:** Persistenz über Partien — siehe „Offene Design-Fragen".

## Thema und Ton

Anime-Fantasy mit Abenteurer-Gilden: Die Spieler sind ein Gilden-Trupp,
die Gegner klassische Fantasywesen — Goblins als Schwarm, Wölfe als die
Schnellen, Orks als die Robusten, Zyklopen als Brocken. Das Setting ist
ernst gemeint, der Ton ist es nicht: hell, freundlich,
Physik-Slapstick, Raum für Blödsinn unter Freunden. Grafischer
Nordstern ist der stylized Look von Chop Chop Inc.; geschriebener
Humor ist Würze, nicht Fundament.

## Offene Design-Fragen

- **Verloren-Kriterium:** Endet die Partie, wenn die Werkbank fällt,
  wenn alle Spieler am Boden sind — oder beides?
- **Partielänge:** Wellen-Takt und Eskalationskurve so, dass eine
  Partie kurz bleibt — Zielwerte im Prototyp messen; Richtwerte im
  Entwurf.
- **Slot-Befüllung:** Bringt jede Waffe ein festes Fähigkeiten-Set mit,
  oder zieht man Skills frei in die Slots? Gibt es Ultimate und
  Passive?
- **Fall beim Outbreak:** Was geschieht mit Waffe und getragenem
  Material, wenn ein Spieler umkippt?
- **Waffen-Entwicklung:** Levelt die Waffe als Objekt an der Werkbank
  aus Team-Beute? (Vermutlich ja — noch nicht festgezurrt.)
- **Persistenz über Partien:** Startet jede Partie bei null, oder
  bleibt etwas bestehen (Festung, Waffen, Freischaltungen)?
- **Universum:** Spielt die Insel in der Welt von Isor's Tower oder in
  einer eigenen?
- **Inselgröße:** Im Blockout durch Ablaufen bestimmen — die Laufwege
  zum guten Material sind der Spannungsregler.
- **Witz-Dosierung:** Wie viel geschriebener Humor neben dem
  Physik-Slapstick?

## Entwurf

*(2026-10-09, Ideenrunde — roh, bindet nichts)*

- Richtwerte Partielänge: Wellen-Takt etwa drei bis vier Minuten; eine
  normale Gruppe fällt um Welle acht bis zwölf; Partie 30–45 Minuten.
  Das Überranntwerden ist der Höhepunkt der Runde, nicht ihr Versagen.
- Technik-Notiz Gegner-Menge (gehört später ins TDD): Spieler volle
  Physik; Schwarm-Gegner als Agenten mit gefaktem Knockback und
  Ragdoll erst im Todesmoment (nur wenige gleichzeitig aktiv);
  Elite-Gegner voll. Wellen-Peak als Zielwert 200 Gegner, gleichzeitig
  lebendig deutlich weniger (Alive-Cap) — alles im Prototyp messen.
- Waffen-Ideen: Sprungfeder-Boxhandschuh als Knockback und
  Crowd-Control; später absurde Kandidaten (Fisch, Besen) und
  Quatsch-Kombos zwischen Waffen.
- Gegner-Verhalten als Comedy (Claude-Vorschlag, unbestätigt): Goblins
  klauen Material aus dem Lager und rennen damit weg.
- Referenz-Sammlung für den Pitch: Dome Keeper (Pendel aus Sammeln und
  Verteidigen), 7 Days to Die (Blutmond-Belagerung), Dungeon Defenders
  und Orcs Must Die! Deathtrap (Koop-Hero-Defense), R.E.P.O. und
  RV There Yet? (Koop-Kleinspiel-Ton), Chop Chop Inc. (Optik);
  Anime-Anker: Solo Leveling (Dungeon Breaks), KonoSuba
  (Gilden-Comedy).
- USP-Keim: „Gemeinsam draußen schuften, gemeinsam drinnen standhalten
  — die Gier ist der Endgegner." Dieser Pendel-Loop als 3D-Koop wirkt
  nach der Recherche vom 2026-10-09 unbesetzt.
- Ausbaustufen, bewusst nicht im Prototyp: begehbare Dungeons zwischen
  den Outbreaks (Material sammeln, während andere Dungeons ausbrechen
  können), weitere Waffen und Slot-Inhalte, Tränke, Persistenz-Modus,
  größere oder weitere Inseln.
- Store-Namenskandidat neben dem Arbeitstitel: „Guildbreak".
