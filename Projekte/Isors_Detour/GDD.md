# GDD.md — Isor's Detour

Ownership: Design-Absicht des Spiels Isor's Detour (Arbeitstitel) —
was es sein soll, nicht wie es gebaut wird. Begründungen gehören in die
DECISIONS dieser Schicht, Aufgaben in die ROADMAP, Technik ins spätere
TDD. Aufbau und Pflege regelt `Kern/GDD_RULES.md`.
Format: feste Kapitelfolge nach `Kern/GDD_RULES.md`; die Abgabe-Kapitel
der Aufgabenstellung (`Uni/Semester_3/ASSIGNMENT_GAME_PITCH.md`) stehen
als „weitere Kapitel nach Bedarf" dahinter; offene Punkte als
`**Offen:**` im Kapitel und gesammelt unter „Offene Design-Fragen";
Rohes datiert im Abschnitt „Entwurf". Eine Zeile `*(Platzhalter — …)*`
markiert ein noch unbefülltes Kapitel.

## Pitch

*(Platzhalter — Befüllung in der Layout-Runde: zwei bis drei Sätze aus
der Grundidee im „Entwurf".)*

## Kern-Schleife

### Die Schleife

*(Platzhalter — Befüllung: Weg bauen und Türme setzen → Welle läuft
den Weg ab → Belohnung → Weg umbauen, nächste Welle.)*

### Weg-Bau

*(Platzhalter — Befüllung: Wegkacheln als Ressource, Gabelungen,
Sackgassen.)*

**Offen:** Sackgassen-Regel und Kachel-Quelle — siehe „Offene
Design-Fragen".

### Türme und Upgrades

*(Platzhalter — Befüllung: Turmtypen, Upgrade-Stufen; hier liegt die
Vielfalt des Spiels.)*

### Wellen und Gegner

*(Platzhalter — Befüllung: Gegnertypen, Wellen-Eskalation, Verhalten
an Gabelungen.)*

**Offen:** Verteilung an Gabelungen — siehe „Offene Design-Fragen".

## Welt-Struktur

*(Platzhalter — Befüllung: Spielfeld aus Kacheln, Start- und
Endpunkt, Größe je nach Spielerzahl.)*

**Offen:** Spielfeldgröße — siehe „Offene Design-Fragen".

## Spieler

### Perspektive und Kamera

*(Platzhalter — Befüllung: Figur in dritter Person, Kamera schräg von
oben.)*

### Steuerung

*(Platzhalter — Befüllung: Laufen, Kachel legen, Turm bauen und
upgraden.)*

## Persistenz

*(Platzhalter — Befüllung: was eine Partie überdauert.)*

## Benutzeroberfläche

*(Platzhalter — Befüllung: HUD, Menüs, Lobby mit Join-Code;
Barrierefreiheit: Bedeutung nie nur über Rot/Grün tragen.)*

## Thema, Aussehen und Story

*(Platzhalter)*

## Audio und Musik

*(Platzhalter)*

## Vergleichbare Produkte und Referenzen

*(Platzhalter — Befüllung: Kandidaten stehen im „Entwurf".)*

## USP

*(Platzhalter)*

## Zielpublikum

*(Platzhalter)*

## Ziel und Umfang

*(Platzhalter)*

## Zeitplan

*(Platzhalter)*

## Technische Daten

*(Platzhalter)*

## Entwicklungsumgebung

*(Platzhalter)*

## Vorgehensweise und Qualitätssicherung

*(Platzhalter — Befüllung: wie Qualität über die Projektdauer gehalten
wird; die Punkte aus dem Freigabe-Feedback vom 2026-10-12 — Gameplay-
Feedback, einheitlicher Stil, passender Sound, klarer Fokus — sind
hier der Maßstab.)*

## Quellenverzeichnis

*(Platzhalter — füllt sich zuletzt.)*

## Offene Design-Fragen

- **Sackgassen-Regel:** Was tun die Gegner, wenn der Weg noch nicht bis
  zum Ziel reicht — direkte Linie zum Ziel (Isors erster Gedanke),
  oder eine andere Lösung?
- **Kachel-Quelle:** Kommen Wegkacheln aus Abbau, als Belohnung nach
  der Welle oder aus beidem?
- **Verteilung an Gabelungen:** Feste 50:50-Teilung, abwechselnd oder
  zufällig?
- **Spielfeldgröße:** Wächst das Feld mit der Spielerzahl, und wie
  ändert sich das Balancing?

## Entwurf

*(2026-10-12, Isors Grundidee aus der Ideen-Vergleichsrunde — roh,
bindet nichts)*

- 3D-Welt, Figur in dritter Person, Kamera schräg von oben.
- Feste Start- und Endpunkte; die Monster laufen vom Start zum Ziel und
  dürfen nur auf Wegkacheln laufen.
- Den Weg baut der Spieler selbst: Wegkacheln werden abgebaut oder als
  Belohnung verdient und nach und nach verlegt; über das Layout findet
  man eigene Strategien.
- Gegner-KI im Kern nur eine: von A nach B auf den Kacheln. An
  Gabelungen teilt sich die Gruppe (etwa 50:50 oder zufällig).
- Die Figur läuft selbst hin, legt Wege, baut Türme und rüstet sie auf.
- Multiplayer denkbar: größeres Spielfeld, das man als Team bebauen
  muss.
- Wellensystem wie in einer klassischen Tower Defense.
- Isors Einschätzung: geringer in der Umsetzung, flexibel, leicht um
  Content erweiterbar, trägt schon mit minimalistischen Systemen.
- Referenz-Kandidaten (Claude, unbestätigt): Isle of Arrows
  (Weg-Kacheln und Türme auf einer Insel), Rogue Tower (Pfad wächst
  pro Welle, aber automatisch), Thronefall (minimalistisches 3D, Figur
  läuft herum und baut), Maze-TDs aus Warcraft 3 (Weg durch Bauen
  formen). Die Kombination aus Koop, eigener Figur und Weg als
  Ressource wirkt unbesetzt — bei der Recherche prüfen.
- Art-Kandidat: Kenney Tower Defense Kit (frei, Kacheln und Türme).
