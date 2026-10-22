# ABGABE_NOTIZEN.md — Roh-Material für die Prototyp-Abgabe

Ownership: Nur das Roh-Material für die Abgabe-Doku des
Spieleprototyps von Pathmakers TD — je Baustein Zeiten, Gebautes und
Erkenntnisse, festgehalten direkt nach dem Baustein. Daraus entsteht
das Erkenntnis-PDF der Abgabe (ROADMAP → „P2 · Playtests und
Erkenntnis-PDF"); Begründungen besitzen die DECISIONS, Ereignisse das
LOG.
Format: je Baustein `## <Kürzel> · Titel (Zeitraum)` mit den Blöcken
Zeiten / Gebautes / Erkenntnisse.

## P-B1 · Fundament im Netz (2026-10-20 bis 2026-10-22)

**Zeiten** (Grindstone; die Lern-Gespräche sind zu ~90 % enthalten):

| Posten | Zeit |
|---|---|
| Design-Runde Steuerung und Kamera | 0:40 |
| PlayerSpawner (inkl. NGO-Wiedereinstieg) | 0:57 |
| PlayerMotor (inkl. Kopien-Lektion) | 0:57 |
| ClickCommandInput | 1:19 |
| StrategyCamera | 2:33 |
| ClickMarker (inkl. Material und Textur) | 1:38 |
| **Summe getrackt** | **8:05** |

Ungetrackt dazu: das Projekt- und Übernahme-Setup vom 20./21.10.
(Repo, eigenes UGS-Projekt, Export/Import samt Aufräumen) und
Lern-Zwischenstücke. Schätzung für P-B1 war 12–14 h mit bewusstem
Multiplayer-Aufschlag — getroffen.

**Gebautes:** Repo `Pathmakers-TD` mit Unity-Projekt (6.3, URP),
eigenes UGS-Cloud-Projekt; Menü-, Lobby- und Relay-Grundlage aus
It's D.O.T übernommen und bereinigt; NavMesh in der Gym-Testarea;
Spieler-Prefab (NetworkObject, NetworkTransform mit Owner-Autorität,
NavMeshAgent); `PlayerSpawner` (Host spawnt je Client eine Figur mit
Besitz), `PlayerMotor` (kapselt den Agenten, Owner-Weiche),
`ClickCommandInput` (Rechtsklick und Halten mit Zeit-Drossel,
UI-Schutz, Gültigkeits-Vorhalt), `ClickMarker` samt generierter
Ring-Textur, `StrategyCamera` (Pan, Zoom, Fokus, Start-Snap; Grenze
und Edge-Pan schaltbar), Action-Map „Gameplay" als
Controller-Vorsorge; Multiplayer Play Mode eingerichtet.
Zwei-Instanzen-Test über Relay bestanden: nur die eigene Figur
steuerbar, Positions-Sync auf der Kopie, Klick-Ring bleibt lokal.

**Erkenntnisse** (vorläufig, Reflexion folgt):
- Das NGO-Grundmodell sitzt und ist belegt — Eingabe lokal, Owner
  simuliert, nur Positionen reisen (Knowledge:
  `Unity/ngo-grundmodell-kopien-und-radio.md`).
- Latenz sichtbar gemacht und eingeordnet: ~0,1–0,15 s beim Zuschauen
  sind Tick + Reise + Glättung, fürs TD unkritisch; Tuning ist
  Messrunden-Stoff (Knowledge: `Unity/netzwerk-latenz-anatomie.md`).
- Die Schätzmethode trägt: bewusster Multiplayer-Aufschlag, Ist ~12 h
  gegen Plan 12–14 h.
- Verstehen-vor-Tippen war nicht langsamer: Die Netz-Teile (1:54)
  kosteten weniger als die frei gebauten Unity-Teile (4:12), weil dort
  die Review-Schleifen liefen.
- Isors Faustregel aus der Reflexion: „Sehen das Teil nur dieser
  Rechner oder auch die anderen? Nur hier → MonoBehaviour genügt;
  die anderen brauchen es oder es hängt am Besitz → NetworkBehaviour."

**Medien:** Demo-Clip des Bausteins (Klick-Lauf samt Ring, Kamera mit
Pan/Zoom/Fokus; ohne Grenz-Clamp und Edge-Pan) im Datenbaum unter
`02_Projekte\PathmakersTD\Media\PB1_Klicklauf-und-Kamera_2026-10-22.mp4`
(`Kern/PFADE.md` → `DATENBAUM`) — Kandidat für die Pitch-Präsentation
am 03.12.
