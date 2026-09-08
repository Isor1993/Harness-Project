# ROADMAP.md — Baureihenfolge Isor's Tower

Ownership: Nur was am Projekt als Nächstes gebaut wird. Was gerade dran
ist, steht in `PLAN.md`; was fertig ist, in `LOG.md`; warum es so
entschieden wurde, in `DECISIONS/`; was das Spiel sein soll, in `GDD.md`;
was aus Semester 2 dasteht und was dabei auffiel, in `ALTSTAND.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`

**Diese Datei wurde am 2026-09-07 erneut geleert:** Die Stack-Entscheidung
(`Uni/DECISIONS.md` → „2026-09-07 — Engine- und Sprachfokus: Unreal +
C++") löst den Unity-Bauplan vom 2026-08-26 ab; er steht wortgleich in
`_ARCHIV.md`. Die neue Semester-Roadmap entsteht im Design-Abschnitt —
geplant für den 2026-09-08. Die Unity-Werkzeuge der Schicht
(`Werkzeuge/prefab_status.py`, `systeme.py`, `szene_pruefen.py`) gehören
zum Altstand und laufen nicht gegen das Unreal-Projekt.

## Mitgenommene Design-Fragen aus dem Unity-Bau

Engine-neutral; die Herleitungen stehen im Archiv-Eintrag vom
2026-09-07. Fälligkeiten vergibt die neue Semester-Roadmap.

- [ ] **Versionsprüfung beim Beitritt** — zwei verschieden alte Builds
  dürfen sich nicht verbinden, sonst driften die Welten auseinander.
- [ ] **Wiederverbindung des Gastes** — der Fall „Gast fliegt raus und
  kommt zurück" ist unentschieden.
- [ ] **Späteinstieg in eine laufende Runde** — der Späte braucht Seed
  und Weltzustand, oder der Beitritt endet an der Lobby.
- [ ] **Join-Code-Eingabe ohne Tastatur** — Controller-Fall; auf Steam
  löst das Overlay das später von selbst.
- [ ] **Zeit und Vorspulen im Netz** — die Ingame-Uhr muss synchron
  sein, sobald etwas nach Tageszeit handelt.

## Eigene Design-Sessions

- [ ] **Floor-Generierung und Floor-Inhalt** — Wie viel eines Floors ist
  frei generiert, wie viel aus festen Bausteinen kombiniert? Dazu Mobs,
  Spezialmonster und Boss. Beantwortet die offene Frage im `GDD.md` →
  „Generierungsanteil". Fällig, bevor der erste Floor echten Inhalt
  bekommt.
- [ ] **Village-Terrain** — handgebaut, mit einem Tool erweitert, oder
  einmalig generiert und eingefroren? Offene Frage im `GDD.md` →
  „Village-Terrain". Fällig, bevor das Village gebaut wird.
- [ ] **Spielersteuerung** — für das richtige Spiel wird sie neu
  entworfen statt aus Semester 2 übernommen (Isor, 2026-08-28). Offene
  Frage im `GDD.md` → „Spielersteuerung". Fällig mit dem Neuaufbau der
  Steuerung in Unreal.

## Gras-Assets

Aus der Design-Session vom 2026-09-06 (`DECISIONS/Gras.md`, die beiden
Einträge dieses Datums). Das Set aus fünf Varianten in je drei LOD-Stufen
liegt fertig im Datenbaum (`Kern/PFADE.md` → `DATENBAUM`,
`03_AssetLibrary\Eigene\Art\Grass\`), der Generator daneben unter
`05_Werkzeuge\Vorlagen\Blender\`.

- [ ] **Das Gras-Set in Unreal gegentesten** — mit Foliage bzw. dem
  Instancing der Engine, echtem Material und Beleuchtung. Die bisherigen
  Bilder stammen aus einem Platzhalter-Shader in Blender. Dabei die
  Dichte neu ansetzen: Die Vorbilder liegen bei rund 16 Büscheln je
  Quadratmeter (der alte Eigenbau-Renderer war auf 0,05 gerechnet — sein
  Rechenweg steht im `_ARCHIV.md`).

## Nach dem Prototyp

Zielbild bleibt, Zeitpunkt offen
(`DECISIONS/Multiplayer.md` → „Semesterschnitt: was in den Prototyp
kommt").

- [ ] **Bauen und Dekorieren im Koop** — Grid mit Snapping, kaufbare
  Häuser, und die Frage, welcher Datentopf eine Gaständerung behält.
- [ ] **Handwerk** — Schmieden, Kochen, Tränke; Rezepte reisen im
  Spielerprofil mit.
- [ ] **Quests über die Adventure Guild** — der schwierigste
  Mitnahme-Fall, weil die Quest-Stände zweier Welten verschieden sind.
- [ ] **Shop** — Zeitpunkt offen, möglicherweise erst Semester 4 oder
  später. Findet die Datenschnittstelle des Neustarts vor.
- [ ] **Host-geprüfte Bewegung** — in Unreal über die
  CharacterMovement-Replication weitgehend eingebaut; prüfen, was der
  Prototyp davon erbt.
- [ ] **Lobby-Komfort** — Voice und Spieler entfernen (Kick); Technik
  wird nach dem Engine-Neustart neu bewertet. Gewünscht am 2026-08-28,
  bewusst hinter den Prototyp gestellt.
- [ ] **Steam-Anbindung statt Relay-Dienst** — sobald eine App-ID
  existiert; Technik nach dem Engine-Neustart neu bewerten (in Unreal:
  Online Subsystem Steam). Dazu später Steam-Profilbilder in der
  Spielerliste (Isor, 2026-09-01 — hängt an derselben App-ID).
- [ ] **Portfolio-Präsentation** (erst wenn eine Bewerbung ansteht):
  spielbarer Build aus der Build-Ablage (`Kern/VERSIONIERUNG.md` →
  „Ablage der Builds"), Video oder GIFs, gezielte Lese-Einladung ins
  private Repo; bei Bedarf ein kuratiertes Showcase-Repo mit nur eigenen
  Skripten. Das Projekt-Repo selbst bleibt dauerhaft privat
  (`Kern/DECISIONS.md` → „Sichtbarkeit und Zugang der Repos").
