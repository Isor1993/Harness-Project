# ROADMAP.md — Baureihenfolge Datenablage

Ownership: Nur die offenen Aufräum-Punkte des Datenbaums
`C:\IsorBackup\`. Die Regeln stehen in `RULES.md` dieser Schicht,
Begründungen in `DECISIONS.md`. Aufgaben am Unity-Projekt stehen in
`Projekte/Isor_Tower/ROADMAP.md`, Studiums-Aufgaben in `Uni/ROADMAP.md`.
Format: `- [ ] **Titel** — ein bis drei Sätze, was zu tun ist und warum.`

## Als Nächstes

- [ ] **`99_Archiv\_Zu_Loeschen\` durchsehen und leeren.** Nur Isor —
  „weg" heißt nach Regel 7 zunächst nur „dorthin verschoben", und geleert
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

## Erledigt, hier nur als Zeiger

Die beiden `.drawio`-Punkte vom 2026-08-06 sind durch. Die **Regel**, die
dabei entstand, steht jetzt dort, wo sie hingehört:
`Kern/DIAGRAM_RULES.md`, Abschnitt „Export aus draw.io".
