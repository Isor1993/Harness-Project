# LOG.md — Chronik Pathmakers TD

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste
oben. Begründungen gehören in die DECISIONS der Schicht, Pläne in die
ROADMAP.
Format: `- JJJJ-MM-TT — Ereignis.` Ein bis drei Zeilen je Eintrag.

- 2026-10-20 — P1-Brainstorm-Runde: Prototyp-Vorgehen entschieden und
  der Prototyp in die Bausteine P-B1 bis P-B8 geschnitten (DECISIONS,
  Einträge vom 2026-10-20; Bausteine in der ROADMAP). Abends Repo
  `Pathmakers-TD` mit Unity-Projekt `PathmakersTD` (6.3, URP)
  angelegt; .gitignore-Anker-Falle vor dem ersten Projekt-Commit
  behoben (Commit „Update V 0.0001").
- 2026-10-21 — P-B1-Übernahme: Netz-Pakete, eigenes UGS-Cloud-Projekt,
  Menü- und Netz-Grundlage per Export/Import aus Its-DOT geholt und
  nachbereinigt (Testkram, Alt-Szenen, tote Verweise; Commit „Update
  V 0.0002"); Menü-Kette im Play-Test lauffähig. Steuerungsmodell
  korrigiert: Befehlsklick statt Direktsteuerung (DECISIONS →
  „2026-10-21 — Steuerung: Befehlsklick statt Direktsteuerung").
- 2026-10-21/22 — P-B1 fertiggebaut: Figur-Paket (PlayerSpawner,
  PlayerMotor, ClickCommandInput samt Klick-Ring, StrategyCamera mit
  Start-Snap, Action-Map „Gameplay", Multiplayer Play Mode) und der
  Zwei-Instanzen-Test über Relay bestanden — nur die eigene Figur
  steuerbar, Positions-Sync auf der Kopie, Ring bleibt lokal.
  8:05 h getrackt (`ABGABE_NOTIZEN.md` → „P-B1").
- 2026-10-23/24 — P-B2-Baustart nach der Design-Runde: PathGrid gebaut
  (Belegungstabelle, Welt-Zelle-Übersetzer, Grenz-Wächter, Scene-Gizmo)
  und sichtgeprüft (Raster, Zieh-Test, zwei Testzellen als Würfel);
  GetLength-Fix nach Live-Dreh der Rastergröße im Play. PlayerSpawner
  gegen fehlenden NetworkManager im Offline-Play gehärtet.
- 2026-10-24 — PathTileView gebaut (sichtbare Kachel je belegter Zelle,
  Abend-Regler „Claude schreibt") samt Kachel-Prefab PathTile;
  Sichtprüfung: zwei Kacheln deckungsgleich mit den Gizmo-Würfeln. Der
  gemeinsame Durchgang wurde am 2026-10-25 in vier Häppchen nachgeholt.
- 2026-10-25 — Geisterbild-Paket gebaut: TileGhost samt Ghost-Prefab und
  zwei transparenten Materialien, BuildModeController (Mausstrahl, Snap
  über beide Übersetzer, Werkzeug-Schalter über die neuen
  Gameplay-Actions Slot1/Cancel) und BuildBarUI mit drei Slot-Scheiben;
  dazu die CellSize-Property am PathGrid. Sichtprüfungen: Hover wechselt
  blau/rot an der Rastergrenze, Leiste und Taste schalten synchron.
- 2026-10-27 — Auftragskette fertig: HasArrived-Auskunft am PlayerMotor,
  BuildOrderQueue (Bestell-Warteschlange, stehende Quittungs-Geister,
  Ankunfts-Bau als Tabelle-und-View-Paar) und der Place-Klick samt
  Shift-Reihe und Owner-Queue-Suche im Controller. Erster
  End-to-End-Bau im Gym bestanden (Play mit Start-Host: Klick → Geist →
  Figur läuft → Kachel) — die lokale Strecke von P-B2 ist damit
  komplett, offen bleibt der Netz-Block.
- 2026-10-28 — Netz-Block-Vorbau: Testarea nach dem Drei-Körbe-Modell
  geordnet (SYSTEM-Trennstrich auf der Wurzel, World und UI als echte
  Parents; das Rig heißt jetzt PathBuildingRig) und der Gym-Testweg
  gebaut — NetworkManager als Prefab plus TestareaBootstrap, Play
  direkt in der Testarea spawnt die Host-Figur. Claudes Awake-Rat
  kostete eine Fehlerrunde (DECISIONS → Gym-Testweg).
- 2026-10-28 — Netz-Block gebaut: PathGridNet auf dem neuen
  Szenen-Objekt GameNetwork (Brief und Durchsage als RPC-Paar im
  universellen [Rpc]-Attribut — das alte ServerRpc-Attribut ist seit
  NGO 2.7 Alt-Bestand), Kassen-Umbau auf den Brief-Aufruf, Solo-Test
  im Gym bestanden. Offen in P-B2: Abbau-Panel, Relay-Test.
- 2026-10-28/29 — Abbau-Panel gebaut: TileInfoPanelUI im HUD (merkt
  sich die Zelle, Knöpfe schließen oder schicken den Abriss-Brief),
  Verwalten-Klick im BuildModeController (nur im Grundzustand, eigener
  PathTile-Layer, Zelle aus der Objektmitte des Treffers) und das
  gespiegelte Remove-RPC-Paar in PathGridNet. Abriss ist Fernbedienung,
  wie am 2026-10-23 entschieden.
- 2026-10-29 — Lauf-Storno nach Isors Exploit-Fund: Bestellung plus
  Wegklicken baute bei Ankunft am falschen Ort fern, weil HasArrived
  zielbezogen ist, die Kasse es aber auftragsbezogen las. Entscheid:
  Der manuelle Laufbefehl storniert alle Bestellungen (DECISIONS);
  CancelAllOrders in der Kasse, Aufruf im ClickCommandInput.
- 2026-10-29 — Relay-Test in beide Richtungen bestanden
  (Blockende-Beweis): Client baut und reißt ab — fremder Stempel,
  ~60 ms Rundreise —, der Host desgleichen mit null Briefweg; 17:26
  getrackt (ABGABE_NOTIZEN → „P-B2").
- 2026-10-29/30 — P-B3-Design-Runde: Karten-Blockout entschieden (vier
  gleiche Gebiete à 50×70 Zellen im 2×2, getrennt durch ein
  Fluss-Kreuz, ein Unity-Terrain, NavMesh zerfällt per Senke in vier
  Inseln; Szene GameWorld), dazu Spielstart (zufällige Game-Id über
  MatchSetup, an der stabilen UGS-PlayerId verankert, Kennzeichnung
  per Zahl) und Verbindungsverlust (Gebiet friert ein, Rejoin als
  vorbereitete Erweiterung) — DECISIONS, Einträge vom 2026-10-29.
- 2026-10-30 — Meilenstein-Planung in fünf Etappen: Fertig-Linien und
  Inhalte von Prototyp bis Portfolio festgelegt (ROADMAP →
  „Meilenstein-Plan", DECISIONS → „Meilenstein-Etappen"); beide
  Status-Tafeln nachgezogen, die Pathmakers-Tafel neu geschnitten mit
  Wochenplan-Band und M1–M6-Karten.
- 2026-10-30 — P-B3-Karte gebaut: GameWorld mit Terrain, Fluss-Senke
  und Zonen-Texturen bemalt (Anker in DECISIONS → „GameWorld-Anker");
  `Tool_MapLayout.cs` als AI-geschriebenes Gizmo-Tool (DECISIONS →
  „Werkzeug-Politik", Karten-Tafel `⚙️ System · Pathmakers-Karte` im
  ARTIFACT_INDEX); NavMesh in vier Inseln zerlegt nach zwei
  Fehlerrunden (Y-Spanne, dann die Layer-Falle — Knowledge:
  `Unity/navmesh-include-layers-filtern-modifier.md`); PathBuildingRig
  zum Prefab gemacht, vier Instanzen auf die Raster-Ecken, Spawn- und
  Despawn-Punkte als Kinder; `PathConnectivity.cs` als Gerüst
  angelegt (Isor tippt die Flood-Fill-TODOs). Hinweis: Schritt
  „Multiplayer Play Mode" des Bau-Zuschnitts war schon P-B1-Bestand.
- 2026-10-30 — Designrunde Monster-Lauf, aus Isors Stopp vor dem
  Gizmo-Coden: Wander-Modell, Rollback und Solo-Lernraum in sieben
  Punkten entschieden, zwei Alt-Regeln abgelöst (DECISIONS →
  „Monster-Lauf: Wander-Modell, Rollback, Solo-Lernraum"); Knowledge:
  `Patterns/flood-fill-breitensuche.md`.
