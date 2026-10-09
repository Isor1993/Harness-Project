<!--
Ownership: Nur das Markdown-Manuskript des Mini-GDD von Isor's Outbreak
— die Kurzfassung für die Freigabe durch die Dozentin, aus der
`Kern/Werkzeuge/abgabe_bauen.py` die .docx-Fassung baut (PDF-Export von
Hand, Versand per Discord). Die volle Design-Absicht besitzt `GDD.md`,
das ausführliche Pitch-GDD entsteht als eigenes Manuskript. Dieser
Kommentar wird beim Bauen verworfen und landet nicht im Anhang.
-->

# Isor's Outbreak — Mini-GDD

Modul 5FSC0XD101_P Games Programming · Eric Rosenberg · Oktober 2026

Kurzfassung zur Projekt-Freigabe — das ausführliche Game Design Document
folgt zur Abgabe.

## Pitch

**Isor's Outbreak** (Arbeitstitel) ist ein Koop-Spiel für ein bis vier
Spieler: Die Gruppe wacht auf einer einsamen Insel auf und baut sich
eine Basis, um zu überleben. Denn über die Insel verteilt liegen
Dungeons, aus denen nach Ablauf eines Timers Wellen von Fantasywesen
brechen und auf die Basis losgehen. Zwischen den Ausbrüchen schwärmt der
Trupp aus und sammelt Material: Je weiter draußen, desto besser die
Beute, und die Gier gegen die Uhr ist der eigentliche Endgegner.

## Ablauf einer Partie

Eine Partie beginnt mit der Gründung: Die Spieler tragen eine Werkbank
im Gepäck und setzen sie, wo sie wollen — dort steht die Basis, und nach
wenigen Minuten kommt der erste Outbreak. Danach pendelt das Spiel:
sammeln, solange der Timer läuft, dann an der Basis bauen und schmieden,
den Outbreak abwehren, verschnaufen und reparieren — nächste Runde, eine
Stufe härter. Material aus der Welt baut die Festung aus, Beute aus den
Wellen verbessert die Waffen; die Waffe bestimmt dabei die Rolle und
wird am Lager einfach getauscht. Die Wellen sind endlos und werden
stärker — Ziel ist, als Team die höchste Welle zu erreichen.

## Umfang

Das entsteht im Semester:

- Koop für ein bis vier Spieler, auch solo spielbar
- eine Insel mit Basis-Bau: Werkbank setzen, Mauern und Werkstationen
  bauen — alles zerstörbar
- endlose Gegnerwellen aus festen Dungeons, mit steigender Stärke und
  neuen Angriffsrichtungen
- wenige, klar unterschiedliche Waffen (Nah- und Fernkampf) und
  verschiedene Gegnertypen

Bewusst nicht in der Abgabe, als Ausbaustufen vorgemerkt: begehbare
Dungeons, weitere Waffen und Tränke, Fortschritt über Partien hinweg,
größere Inseln.

## Rahmen

**Engine:** Unity (C#) · **Plattform:** PC

**Team:** Solo-Projekt — Design und Code bei mir, Art über fertige
Asset-Packs (frei oder zugekauft).
