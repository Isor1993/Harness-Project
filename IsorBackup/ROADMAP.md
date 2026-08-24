# ROADMAP.md — Baureihenfolge Datenablage

Ownership: Nur die offenen Aufräum-Punkte des Datenbaums
(`Kern/PFADE.md` → `DATENBAUM`). Die Regeln stehen in `RULES.md` dieser Schicht,
Begründungen in `DECISIONS.md`. Aufgaben am Unity-Projekt stehen in
`Projekte/Isor_Tower/ROADMAP.md`, Studiums-Aufgaben in `Uni/ROADMAP.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`

## Als Nächstes

- [ ] **`99_Archiv\_Zu_Loeschen\` durchsehen und leeren.** Nur Isor —
  „weg" heißt nach der Regel *Gelöscht wird nur von Isor* (`RULES.md`)
  zunächst nur „dorthin verschoben", und geleert
  wird von Hand. Inzwischen liegen dort auch die Bestände der
  Harness-Überholung vom 2026-08-22.

- [ ] **Library-Durchgang nach der Abgabe.** Alles Wiederverwertbare aus
  dem Projekt als `.unitypackage` exportieren — Shader, VFX, Texturen und
  die Skripte, die auch in anderen Projekten taugen (Timer, Interfaces,
  Basisklassen) → `03_AssetLibrary\Eigene\`. Die dort liegenden losen
  `.shadergraph`-Dateien sind Stände vom 22./28.06., das Projekt hat
  neuere. Fällig, seit die Abgabe am 2026-08-20 hoch ist.

- [ ] **`Sand.shadergraph` klären.** Existiert **nur** als lose Kopie in
  der Library, nicht im Projekt. Entweder ins Projekt zurückholen oder
  als bewusst ausgelagert kennzeichnen — im jetzigen Zustand ist unklar,
  welcher Stand gilt.

- [ ] **`.blend`-Quellen für die Gras-Meshes.** Zu
  `Grass_Clump_Cross.fbx` und `Grass_Clump_Star.fbx` fehlen die
  Blender-Dateien. Ohne Quelle lässt sich das Mesh nicht mehr ändern, nur
  ersetzen.

## Vertagt — der Harness fasst es nicht an

- [ ] **Backup auf die externe Platte.** Das Skript
  `Werkzeuge/sichern.ps1` ist gebaut, geprüft und einsatzbereit
  (Probelauf als Voreinstellung, Papierkorb statt Löschen, rund 16 GB
  über drei Ordner). **Isor fährt die Sicherung bis auf Weiteres von
  Hand**; sie ist kein Punkt des Pflegetags mehr und wird nicht als offen
  gemeldet. Wieder aufgenommen, wenn die Testphase durch ist und der
  Harness sich im Betrieb bewährt hat — kein Datum
  (`Kern/DECISIONS.md`, 2026-08-23).

## Nach der Aufräumphase

- [ ] **`LOG.md` dieser Schicht anlegen**, sobald der erste
  Aufräum-Durchgang läuft. Die Schicht ist bisher die einzige ohne
  Chronik — deshalb stand hier bis zum 2026-08-22 ein „Erledigt"-Block,
  obwohl diese Datei nur offene Punkte besitzt. Ereignisse gehören ins
  LOG, nicht in die ROADMAP.
