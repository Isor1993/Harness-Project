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

## P-B2 · Weg-Bau (2026-10-22 bis 2026-10-29)

**Zeiten** (Grindstone; die Lern-Gespräche sind zu ~90 % enthalten):

| Posten | Zeit |
|---|---|
| Design-Runde Weg-Bau | 0:54 |
| PathGrid | 1:46 |
| PathTile, TileGhost, BuildModeController, BuildBarUI | 5:43 |
| BuildOrderQueue samt Place-Klick | 1:38 |
| Netz-Block (Szenen-Umbau, Gym-Bootstrap, PathGridNet) | 5:14 |
| Abbau-Panel, Lauf-Storno, Relay-Test | 2:11 |
| **Summe getrackt** | **17:26** |

Schätzung war 10–12 h — um rund die Hälfte gerissen. Benennbare
Anteile: der Netz-Lernblock (RPC-Modell samt API-Umbruch), zwei
Claude-Fehlerrunden (StartHost-Timing, veraltetes ServerRpc-Rezept —
`Kern/STOERUNGEN.md`, 2026-10-28) und die ungeplante Struktur-Runde
(Szenen-Ordnung, Gym-Testweg) — Letztere ist Einrichtung, die P-B3
nicht mehr bezahlt.

**Gebautes:** PathBuildingRig als versetzbares Prefab: PathGrid
(Belegungstabelle, Welt-Zelle-Übersetzer, Grenz-Wächter, Scene-Gizmo),
PathTileView (Kachel-Klon je belegter Zelle; Kachel-Prefab PathTile
mit eigenem Layer), TileGhost samt Ghost-Prefab und zwei transparenten
Materialien, BuildModeController (Mausstrahl, Snap, Werkzeug-Schalter,
Place-Klick mit Shift-Reihe, Verwalten-Klick im Grundzustand).
Im HUD: BuildBarUI (drei Slots) und TileInfoPanelUI (Panel am
liegenden Objekt, Abriss als Fernbedienung). Auf der Figur:
BuildOrderQueue (Bestell-Schlange, Quittungs-Geister, Lauf-Storno).
Im Netz: PathGridNet auf dem Szenen-Objekt GameNetwork — zwei
gespiegelte RPC-Paare (Brief an den Host, Durchsage an alle) für Legen
und Abreißen; dazu NetworkManager als Prefab plus TestareaBootstrap
für den menü-freien Gym-Start und die Testarea nach dem
Drei-Körbe-Modell geordnet. Relay-Test in beide Richtungen bestanden:
Client baut und reißt ab, fremder Stempel, der Host prüft als einzige
Wahrheit.

**Erkenntnisse** (mit Isors Reflexion vom 2026-10-29):
- Isors Einordnung der gerissenen Schätzung: bewusst Verstehen vor
  Tempo — lieber über die Zeitschwelle und dafür das Netz wirklich
  begriffen; die Krankschreibungs-Woche gibt das Polster, und der
  Lernanteil soll die kommenden Netz-Bausteine verbilligen.
- Der Schnitt täuschte: „Weg-Bau" klang nach Raster und Kacheln, war
  aber zu einem großen Teil Netz-Bau — unterschätzt wurde der
  Zuschnitt des Blocks, nicht das Arbeitstempo. Dazu kamen der
  API-Umbruch und die Extra-Verständnisknoten.
- Lage im Semesterplan (Isors Einschätzung): vor dem Plan; die
  unterwegs gesammelten Spielgefühl-Funde sind bewusst als
  P3-Merkposten vertagt statt vergessen.
- Der API-Umbruch von NGO 2.7 (universelles [Rpc], InvokePermission
  statt RequireOwnership) kostete eine Runde — und der richtige Stand
  lag seit August im eigenen Knowledge-Ordner. Gegenmittel als
  Harness-Punkt: Versionsliste je Projekt (`Kern/ROADMAP.md`).
- „Der Host ist selbst Client" trägt: Der Solo-Lauf im Gym testete
  bereits den kompletten RPC-Pfad; der Relay-Test bestätigte nur noch
  den fremden Stempel und die Rundreise (~60 ms beim Client, null
  beim Host — deckt die Design-Annahme von 0,06–0,15 s).
- Das Brief/Durchsage-Muster skaliert wie entworfen: Der Abriss war
  ein gespiegeltes zweites Paar im selben Skript, kein neues System.
- Exploit-Fund durchs freie Spielen im Gym: Bestellung plus Wegklicken
  baute fern, weil HasArrived zielbezogen ist. Behoben als
  Design-Entscheid (Laufbefehl storniert alles), nicht als Flicken.

## P-B3 · Karte + Spawns (2026-10-29 bis 2026-10-31)

**Zeiten** (Grindstone; die Designrunden vom 29./30.10. — Karte,
Spielstart, Monster-Lauf — sind **nicht** getrackt, ebenso bewusst
nicht die Lese- und Zwischenzeiten vom 31.10.):

| Posten | Zeit |
|---|---|
| GameWorld-Blockout + Tool_MapLayout (30.10.) | 1:49 |
| PathConnectivity — Flutfüllung + Gizmo | 1:28 |
| GameWorld testbar machen (Szenen-Umzug) | 1:16 |
| Bau-Regel, MatchSetup, Panel-Fixes | 1:46 |
| BuildModeController-Umbau (Input-Zuteilung) | 1:16 |
| **Summe getrackt** | **7:36** |

Schätzung war 7–8 h — **gehalten**, einen Tag vor dem Wochen-Soll.
Der P-B2-Lernblock hat gezahlt, was er versprochen hat: Brief/
Durchsage, Besitz und die NGO-Grundmuster saßen diesmal.

**Gebautes:** Szene GameWorld spielbar und im Menü verdrahtet
(System-Umzug aus der Testarea, SceneBootstrap statt
TestareaBootstrap, Build-Liste, SceneId.GameWorld im Menü-Weg);
Tool_MapLayout als AI-geschriebenes Karten-Gizmo; PathConnectivity
(Flutfüllung ab der geklemmten Spawn-Zelle, blaues Erreichbar-Overlay
— zugleich die spätere Gültigkeits-Rechnung); Bau-Regel im Motor
(HasFullPath: gebaut wird nur bei vollem NavMesh-Weg, Verwerfen räumt
auf); MatchSetup (NetworkList-Brett, Losbeutel-Zufall, GetGameId/
GetRigGrid als einzige Index-Umrechner); PlayerSpawner spawnt nach
Game-Id statt Beitritts-Reihenfolge; BuildModeController als ein
Spieler-Objekt statt vier Rig-Kopien, samt Panel-Ausstieg im Baumodus;
Kasse und Controller holen ihr Rig per Try-Muster — keine Szenen-Suche
mehr.

**Erkenntnisse** (vorläufig, Reflexion folgt):
- Szenen-Suche skaliert nicht: FindFirst „funktionierte" mit einem
  Rig und griff mit vieren das falsche — der Falsch-Rig-Bug, von Isor
  im eigenen Debug-Durchgang überführt. Antwort auf Architektur-Ebene:
  Zuweisung statt Suche (Brett), nicht eine bessere Suchfunktion.
- Ein-Rig-Annahmen steckten an mehr Stellen als gedacht (Kasse,
  Controller, Spawner; PathGridNet bleibt als benannte Naht) — der
  Lese-Checkup über alle Skripte vor dem Weiterbauen hat sich gelohnt.
- Die Engine wusste die Bau-Antwort schon: pathStatus unterscheidet
  „angekommen" von „so weit es ging" — erst fragen, was der NavMesh
  weiß, statt selbst zu messen; der „kurz davor"-Regler existierte
  als stoppingDistance ebenfalls bereits.
- Isors Architektur-Grundsatz ausgesprochen und angewendet:
  Sauberkeit vor Umbaugröße — ein Controller beim Spieler statt vier
  schlafender Kopien (DECISIONS, 2026-10-31).
- Vier Grindstone-Schübe à ~1,5 h mit klaren Schnitten erwiesen sich
  als gut nachvollziehbare Tracking-Einheit.

**Medien:** Scene-Screenshot des Gizmos (blaue Kette, abgetrennte
Kacheln orange) liegt im Chat vom 2026-10-31; ein Demo-Clip des
Bausteins steht noch aus.

## P-B4 · Gegner laufen (2026-11-01 bis 2026-11-08)

**Zeiten** (Grindstone, Zwischenstand 2026-11-03 früh — der Baustein
läuft noch; Schätzung ~10 h):

| Posten | Zeit |
|---|---|
| Sichern Standardweg + Einstieg Designrunde (02.11.) | 0:24 |
| Designrunde „Gegner laufen" (Host simuliert, Steckbriefe) | 0:45 |
| MonsterDefinition + Grunt-Asset | 0:06 |
| Monster.cs (Läufer) | 0:31 |
| SendBuilding + Panel-Basisklasse | 0:28 |
| Sende-Kette bis zum laufenden Grunt (Selector, Knopf, MonsterSpawner, Tests) | 2:08 |
| **Zwischensumme 02./03.11.** | **4:22** |

Gesamt-Grindstone am 2026-11-03: **37:49:32**. Abzüglich der
Bausteine P-B1 bis P-B3 (zusammen 33:07) sind bisher **~4:43** auf
P-B4 gebucht; die ~0:20 über der Zwischensumme oben sind der 01.11.
(Weg-Kopf/Standardweg, nur knapp getrackt). Getrackt ist die aktive
Bauzeit — Denk-, Frage- und Designstrecken laufen teils ungetrackt
(Isor, 2026-11-03); fürs „Plan gegen Wirklichkeit"-Kapitel zählt
deshalb die Tabelle als Untergrenze. Gebautes und Erkenntnisse
folgen beim Baustein-Abschluss.

**Nachtrag 2026-11-04:** Aufräum-Runde, Spawn-Fix (Warp-Brief nach
NGO-Quelltext-Beweis), Rig-Naht Variante A und bestandener
Multiplayer-Doppeltest (Belege: DECISIONS/LOG 2026-11-04). Dazwischen
der **Ordnungssystem-Durchgang** (Gewerk-Modell, Präfixe, Szenen-Zonen;
kompletter Bestand umgezogen) — eigener Posten fürs „Plan gegen
Wirklichkeit"-Kapitel: Infrastruktur-Tag mitten im Baustein, bewusst
gewählt („erst sauber machen, dann weiter"). Grindstone-Zeiten des
03./04.11. beim Baustein-Abschluss nachtragen.

**Nachtrag 2026-11-08 (Routing fertig):** WanderRouter komplett
(Zähler + Strecken-Schleife, Zeile für Zeile), erster Sichttest
kippte die Lauf-Regel — Design-Befund, kein Code-Bug: Abwechseln an
jeder Gabelung erzeugt unlesbare Umwege. Inline-Design-Runde →
**Distanzfeld** (DECISIONS „Lauf-Regel") samt Dirty-Flag-Cache; der
Regelwechsel kostete dank Planer/Sieb/Zähler-Trennung nur eine
geänderte und eine neue Methode. Dazu Höhen-Feature (DECISIONS
„Monster-Höhe"), Prefab-Eichung, Mess-Log raus. Zeiten (Grindstone,
Screenshots 08.11. ~02:41):

| Posten | Zeit |
|---|---|
| Bühne Block 3: BuildModeController ans Interface (07.11.) | 0:44 |
| Lebensbrett samt Designrunde „Daten senden wie?" (07.11.) | 3:01 |
| PathConnectivity/Routing-Algo, drei Schübe (07.11.) | 3:26 |
| WanderRouter Zeile für Zeile, Nachtstrecke (07./08.11.) | 2:34 |
| **Summe der Schübe 07./08.11.** | **9:45** |

Gesamt-Grindstone am 08.11.: **51:40:33** → abzüglich P-B1 bis P-B3
(33:07) sind **~18:33** auf P-B4 gebucht, Schätzung war ~10 h.
Einordnung fürs „Plan gegen Wirklichkeit"-Kapitel: Im Ist stecken der
Ordnungssystem-Tag (04.11.), mehrere Designrunden (Monster-Lauf,
Wander-Routing, Lauf-Regel) und ein kompletter Regelwechsel nach
Sichttest — der reine Bau lag näher an der Schätzung. Die
08.11.-Strecke nach 02:41 (Lauf-Regel-Umbau, Höhen-Feature, Tests)
war bei Screenshot-Stand noch ungebucht; beim Baustein-Abschluss
nachtragen, zusammen mit den noch offenen Zeiten des 03.–06.11.

**Zeiten-Schluss 2026-11-08:** Die Strecke nach 02:41 ist nie gebucht
worden — Gegenprobe: Gesamtstand 56:27:23 minus der beiden
P-B5-Scheiben (4:47) ergibt exakt den 02:41-Stand 51:40:33. P-B4
schließt damit endgültig bei **~18:33** als Untergrenze (die
Schluss-Strecke und Teile des 03.–06.11. liefen ungetrackt);
Gebautes und Belege stehen im LOG (Einträge 2026-11-02 bis 08) und
in den DECISIONS.

## P-B5 · Takt + Senden (2026-11-08)

**Zeiten** (Grindstone; Schätzung ~5–6 h):

| Posten | Zeit |
|---|---|
| Design-Runde „Takt + Senden" (Nachtstrecke) | 0:33 |
| Bau: vier Stationen samt Tests | 4:13 |
| **Summe** | **4:47** |

Gesamt-Grindstone am 08.11. abends: **56:27:23**. Die lange
Design-Diskussion der Nacht ist nur mit 0:33 enthalten
(Untergrenzen-Regel wie gehabt: getrackt ist die aktive Zeit).
**Erste Unterschreitung der eigenen Schätzung** — 4:47 gegen 5–6 h,
trotz des Multiplayer-Kerns.

**Gebautes:** `SeatState`- und `RoundPhase`-Enum
(`Scripts/Enums/GameState/`); MatchSetup-Erweiterung —
Platz-Zustände als zweite NetworkList, `GetSendTarget` (nächster
aktiver Platz im Uhrzeigersinn, Selbst-Senden gratis als letzter
Kandidat), `Instance`-Zeiger (Scene-Singleton); `GameClock` neu
(`Scripts/GameState/`) — Zwei-Phasen-Takt mit Karte-leer-Tor über
Lebend-Zähler, freilaufende Einkommens-Uhr, synchronisiert werden
Endzeitpunkte auf der ServerTime statt tickender Werte;
`MonsterSpawner`-Umbau — Pool je Absender, Schnappschuss bei Timer
null, Ausschüttungs-Kolonne per Coroutine (Inspector-Takt), Spawn
aufs **Ziel**-Rig (der V1-Vermerk „sender's own" ist getilgt);
Monster meldet seinen Abgang an die Uhr; `GameClockUI`
(`Scripts/HUD/`) als Minimal-HUD — Phase plus beide Countdowns,
reines Ablesen der Getter. Tests bestanden: Solo-Selbstsenden,
gegenseitiges Senden, Schnappschuss-Abgrenzung (später Einkauf
wartet auf die nächste Welle), HUD-Countdowns auf Host und Client.

**Erkenntnisse** (vorläufig, Reflexion folgt):
- Die Unterschreitung hat zwei benennbare Quellen: komplette
  Design-Runde **vor** dem Bau (keine Inline-Designstrecken wie in
  P-B4) und TODO-Gerüste, die seit Isors Feedback das Werkzeug
  nennen, nicht nur das Ziel.
- Werkzeug-Deklaration fürs „Plan gegen Wirklichkeit"-Kapitel: Die
  fünf Schluss-Korrekturen im MonsterSpawner tippte Claude auf
  Zuruf (Missverständnis über den Umfang, nur eine Stelle war
  gemeint); alles andere tippte Isor nach Gerüst.
- Endzeitpunkt-Muster belegt: nichts tickt übers Netz, die über die
  Partie eingefrorene Nachkommastelle des Income-Termins ist der
  sichtbare Drift-Freiheits-Beweis.
- Design-Befund aus dem Spieltest: Die Kampfphase kann sich am
  Karte-leer-Tor stark ziehen (~3-Minuten-Runden auf dem großen
  Feld); als Prüf-Merkposten bei P2, Isors eigene
  Änderungswahrscheinlichkeit ~90 %.
