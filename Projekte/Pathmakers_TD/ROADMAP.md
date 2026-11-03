# ROADMAP.md — Bauplan Pathmakers TD

Ownership: Nur was an Pathmakers TD als Nächstes designt oder gebaut
wird — Aufgaben und Verweise auf offene Fragen. Begründungen gehören in
die DECISIONS dieser Schicht, die Design-Absicht ins GDD; die Termine
besitzt `Uni/Semester_3/STUNDENPLAN.md`.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

## Aufgaben

- [x] **G1 · Volles GDD** — **erledigt am 2026-10-17** (Beleg: die
  Einträge vom 2026-10-17 in `DECISIONS.md` und die gebaute Abgabe im
  Datenbaum unter `01_Uni\Semester_3\Arbeitsdateien`,
  `Kern/PFADE.md` → `DATENBAUM`). Ursprünglicher Zuschnitt: startet,
  sobald das Outbreak-GDD steht;
  Ziel für beide: Do/Fr 15./16.10. Eigene Layout-Runde (Kapitel stehen als
  Platzhalter in `GDD.md`), dann Punkt für Punkt befüllen, beginnend
  mit Pitch und Kern-Schleife aus dem „Entwurf". Die Fragenliste aus
  dem Freigabe-Feedback vom 2026-10-12 (`Uni/LOG.md`) dient als
  Prüfliste: Jede Frage soll das GDD beantworten oder bewusst
  ausschließen. Geht zusammen mit dem Outbreak-GDD an die Dozentin
  (`Uni/DECISIONS.md` → „2026-10-13 — Zwei Konzepte parallel bis zur
  Wahl der Dozentin").
  **Stand 2026-10-17:** Das GDD ist inhaltlich komplett — Durchgang
  aller sechs Kapitel (größter Fund: Wellenmodell auf „nur Sends"
  umgestellt, keine automatischen Wellen), Thema-Kapitel samt
  Turm-Entscheidung (Wächter-Figuren), Sackgassen-Regel geschlossen,
  alle Restkapitel gefüllt; offene Design-Fragen: keine; neun neue
  Einträge in `DECISIONS.md`. Gleichentags gebaut und versandt:
  Manuskript auf Abgabe-Konvention gebracht (Kommentar-Kopf,
  `#`-Kapitel, Abgabe-Ende-Marke, Quellenverzeichnis-Satz), .docx mit
  Titelteil gebaut, beide GDDs als PDF per Discord an die Dozentin.
  Die Konzept-Entscheidung ist am 2026-10-20 gefallen: Pathmakers TD
  wird das Semester-Spiel (`Uni/DECISIONS.md` → „2026-10-20 —
  Semester-Spiel: Pathmakers TD; It's D.O.T wird privates Projekt").
  Die Schicht ist damit die aktive; die Aufgaben darunter sind neu.
- [x] **P1 · Prototyp-Start** — **erledigt am 2026-10-20** (Beleg: die
  DECISIONS-Einträge vom 2026-10-20 und der Baustein-Abschnitt unten).
  Ursprünglicher Zuschnitt: zuerst eine Brainstorm-Runde zum
  Vorgehen und zum Schnitt der ersten Bausteine (Isor, 2026-10-20),
  danach der Blockout. Übernehmbar aus dem Its-DOT-Prototyp, weil
  Pathmakers ebenfalls vier Spieler über Relay braucht: Netz-Grundlage
  (NGO, Relay, Lobby mit Join-Code), die Menü-Kette und die
  Spielerfigur samt Kamera.
  **Stand 2026-10-20:** Die Brainstorm-Runde ist gelaufen — Netz von
  Anfang an, Reihenfolge und Schnitt stehen; der Blockout selbst ist
  jetzt Teil der Bausteine P-B1 und P-B3 unten.
- [ ] **P2 · Playtests und Erkenntnis-PDF** — Testrunden über das
  echte Netz und das Abgabe-PDF des Prototyps (mind. 500 Wörter:
  ursprüngliche Idee, was ändern, was übernehmen —
  `Uni/Semester_3/VORJAHR_AUFGABEN.md` → „3 · Spieleprototyp").
  Bekommt fest die letzte Woche vor dem 27.11., nicht den Rest.
  Prüf-Merkposten aus der P-B2-Runde: Macht der Fern-Abbau Umbauten
  zu billig, und zögert das Bauen beim Nahbau spürbar? Letzteres ist
  der Auslöser für die Client-Vorhersage (DECISIONS → „2026-10-23 —
  Netz: Host als Buchhalter, Verkündung an alle, Vorhersage als
  Erweiterung").
- [ ] **A1 · Pitch-Abgabe und Präsentation** — das GDD liegt fertig;
  nötig sind die Präsentationsfassung und der PDF-Export. Termine in
  `Uni/Semester_3/STUNDENPLAN.md`.
- [ ] **G2 · GDD-Nachzug nach der Präsentation** — die
  Aufgabenstellung verlangt das GDD mit eingearbeitetem Feedback
  (`Uni/Semester_3/ASSIGNMENT_GAME_PITCH.md`). Einzuarbeiten sind die
  Zweck-Kette der Mechaniken und die im Discord-Durchgang vom
  2026-10-20 gegebenen Antworten (`Uni/LOG.md`); das Rohmaterial steht
  in `GDD.md` → „Entwurf", Eintrag vom 2026-10-20. Dazu der
  Steuerungs-Nachzug: Steuerungs- und Kamera-Kapitel sowie der
  Vergleichs-Halbsatz („nicht aus der Befehlssicht") auf das
  Befehlsklick-Modell bringen (DECISIONS → „2026-10-21 — Steuerung:
  Befehlsklick statt Direktsteuerung").

## Prototyp — Bausteine

Zuschnitt und Begründung: DECISIONS → „2026-10-20 — Prototyp-Schnitt:
Isors Reihenfolge, Wächter spät". Schätzungen von Isor, bewusst mit
Multiplayer-Aufschlag; P-B1 bis P-B7 füllen das Bau-Budget bis zum
27.11. komplett, nach P-B4 steht der Prüfpunkt zum Wächter-Vorziehen.

- [x] **P-B1 · Fundament im Netz** — **erledigt am 2026-10-22** (Beleg:
  LOG-Einträge vom 2026-10-20 bis 22, Zeiten und Gebautes in
  `ABGABE_NOTIZEN.md` → „P-B1 · Fundament im Netz"; Zwei-Instanzen-
  Test über Relay bestanden). Ursprünglicher Zuschnitt: Repo
  `Pathmakers-TD` samt
  Unity-Projekt `PathmakersTD`, NGO/Relay/Lobby und Menü-Kette
  übernehmen, Kachel-Boden als Testfläche, Figur mit Kamera als
  Owner-Movement (B1-Movement-Design aus `Projekte/Its_DOT/`).
  (~12–14 h)
  **Stand 2026-10-21:** Repo, Unity-Projekt, eigenes UGS-Projekt und
  die Übernahme aus Its-DOT stehen (LOG; Commits V 0.0001/0.0002),
  das Testarea-Gym ist mitübernommen. Offen: Spielerfigur samt
  Kamera — Steuerungsmodell neu entschieden (DECISIONS → „2026-10-21
  — Steuerung: Befehlsklick statt Direktsteuerung"): NavMeshAgent
  statt Owner-Movement-Motor. Die Figur-Design-Runde ist
  abgeschlossen (drei DECISIONS-Einträge vom 2026-10-21,
  Rest-Schätzung ~8–9 h). Tafeln: Status
  https://claude.ai/artifact/5JZCpkKe2MVnCC9R2ScuvJ · Steuerung
  https://claude.ai/artifact/DztjtxavWXmwrMP3YxZoET
- [x] **P-B2 · Weg-Bau** — **erledigt am 2026-10-29** (Beleg:
  LOG-Einträge 2026-10-23 bis 29, Zeiten und Gebautes in
  `ABGABE_NOTIZEN.md` → „P-B2 · Weg-Bau"; Relay-Test in beide
  Richtungen bestanden — Client baut und reißt ab). Ausnahme: der
  Zuschnitts-Punkt Weg-Zusammenhang ab Startpunkt ist nach P-B3
  verschoben (Isor, 2026-10-29) — die Prüfung braucht die
  Start-Marker, die erst P-B3 baut. Ursprünglicher Zuschnitt:
  Kachelraster, Geisterbild an der Maus,
  Figur läuft zur Baustelle, Kacheln legen und abbauen,
  Weg-Zusammenhang ab Startpunkt — netzsynchron. (~10–12 h; Ist
  17:26 getrackt)
  **Stand 2026-10-23:** Die Design-Runde ist abgeschlossen — vier
  DECISIONS-Einträge vom 2026-10-23 (Kachel-Grundlage, Bau-Erlebnis,
  Raster-Rig, Netz-Modell samt Skript-Zuschnitt). Bau-Reihenfolge:
  Grid lokal → Geisterbild und Leiste → Auftragskette → Netz →
  Abbau-Panel → Relay-Test.
  **Stand 2026-10-27:** Die lokale Strecke ist komplett — Grid, View,
  Geisterbild, Schalter, Leiste und Auftragskette gebaut und
  sichtgeprüft, erster End-to-End-Bau bestanden (Beleg: LOG, Einträge
  2026-10-23 bis 27). Offen: Netz-Block (PathGridNet), Abbau-Panel,
  Relay-Test.
  **Stand 2026-10-28:** Netz-Block gebaut — Szene nach dem
  Drei-Körbe-Modell geordnet, Gym-Testweg (Play ohne Menü), PathGridNet
  samt Kassen-Umbau, Solo-Test bestanden (Beleg: LOG 2026-10-28, drei
  DECISIONS-Einträge). Offen: Abbau-Panel (TileInfoPanelUI),
  Zwei-Instanzen-Relay-Test.
- [x] **P-B3 · Karte + Spawns** — **erledigt am 2026-10-31** (Beleg:
  LOG-Einträge 2026-10-29 bis 31, Zeiten und Gebautes in
  `ABGABE_NOTIZEN.md` → „P-B3 · Karte + Spawns"; 7:36 h getrackt bei
  7–8 h Schätzung, einen Tag vor dem Wochen-Soll; Menü-Weg führt in
  die GameWorld, Solo-Test bestanden). Ursprünglicher Zuschnitt:
  Blockout der echten Karte: vier
  Gebiete, Größe einstellen, Start- und Endpunkte. (~7–8 h)
  Erster Einrichtungs-Schritt bei Baustart: Multiplayer Play Mode
  aufsetzen, damit Mehr-Spieler-Tests ohne zweite Editor-Instanz
  laufen (Merkposten aus der P-B2-Netz-Runde, 2026-10-28).
  Aus P-B2 verschoben (Isor, 2026-10-29): die
  Weg-Zusammenhangs-Prüfung ab Startpunkt als Editor-Gizmo
  (Raster-Entscheid vom 2026-10-23) — sie braucht die Start-Marker
  dieser Karte.
  **Stand 2026-10-29:** Die Design-Runde ist abgeschlossen — drei
  DECISIONS-Einträge vom 2026-10-29 (Karten-Blockout, Spielstart,
  Verbindungsverlust). Bau-Zuschnitt in Reihenfolge: Multiplayer Play
  Mode → Prefab-Pass (HUD-Canvas) → Szene GameWorld (ein Terrain,
  Fluss-Senke samt NavMesh-Modifier, Zonen-Texturen) → vier
  Rig-Instanzen samt Start-/Ziel-Markern und Zusammenhangs-Gizmo →
  MatchSetup (Game-Id, Spawn, Kamera-Start) → Territory-Check im
  ClickCommandInput → Menü-Weg auf GameWorld (Lade-Timeout, wenn die
  Zeit reicht). Der Standardweg-Autobau ist an P-B4 abgegeben.
  **Stand 2026-10-30:** Karte steht — GameWorld gebaut und bemalt,
  NavMesh in vier Inseln (nach der Layer-Falle, LOG 2026-10-30),
  `Tool_MapLayout.cs` als Gizmo-Tafel, PathBuildingRig als Prefab mit
  vier Instanzen samt EnemySpawn-/EnemyDespawnPoint; der Schritt
  „Multiplayer Play Mode" war schon P-B1-Bestand. Dazu die Designrunde
  Monster-Lauf (DECISIONS 2026-10-30 — Wander-Modell, Rollback).
  Offen: das Zusammenhangs-Gizmo (`PathConnectivity.cs` liegt als
  Gerüst mit sechs TODOs, Isor tippt) → MatchSetup → Territory-Check →
  Menü-Weg.
  **Stand 2026-10-31:** Gizmo gebaut und in der GameWorld geprüft,
  GameWorld spielbar (Szenen-Umzug, Build-Liste, SceneBootstrap),
  Bau-Regel (nur bei vollem Weg), MatchSetup komplett (Brett,
  Losbeutel, Spawner nach Game-Id, Kasse und Controller per
  Try-Muster), ein BuildModeController statt vier, Panel-Ausstieg aus
  P3 vorgezogen — Belege im LOG (sieben Einträge vom 2026-10-31) und
  in den DECISIONS. Territory-Check beim Laufen durch das
  Insel-NavMesh erledigt (Fehlklick-Filter → P3). **Offen nur noch:
  der Menü-Weg auf GameWorld** (SceneId-Enum + SceneLoader-Asset +
  drei Menü-Stellen; dabei den PlayerId-Anker fürs Brett nachziehen,
  sobald der UGS-Weg ihn liefert). Bekannte Naht danach:
  `PathGridNet` adressiert genau ein Rig (ein Grid, eine View,
  rig-lokale Zellindizes in den RPCs) — Rig-Kennung im Brief oder ein
  Netz-Skript je Rig; bis dahin von Hand auf Rig_1 verdrahtet (Isor,
  2026-10-31: nach dem Baustein, wenn Zeit ist).
- [ ] **P-B3a · Spielstart-Anbauten** — zwei kleine Posten aus den
  Beschlüssen, baubar seit der Menü-Weg steht (2026-10-31), Kür neben
  P-B4, kein Blocker: der **Lade-Timeout** (Beschluss „Spielstart",
  2026-10-29: verliert ein Spieler beim Laden die Verbindung, warten
  die anderen bis zu einer Minute, dann startet das Spiel ohne ihn)
  und der **PlayerId-Anker** am MatchSetup-Brett (Rejoin-Vorsorge:
  host-seitige Zuordnung UGS-PlayerId → Game-Id, jetzt möglich, weil
  der UGS-Weg die Id liefert — im Gym gibt es sie weiterhin nicht).
- [ ] **P-B4 · Gegner laufen** — ein Gegnertyp, host-gesteuert:
  Wegpunkt-Folge nach dem Wander-Modell samt Gültigkeit und Rollback
  (DECISIONS 2026-10-30 — „Monster-Lauf"; ersetzt den alten Zuschnitt
  „Gabelung abwechselnd, gerade Linie am Wegende"), Leben-Abzug am
  Endpunkt. Danach der Prüfpunkt. (~10 h; das Routing schreibt Claude
  nach der Werkzeug-Politik vom 2026-10-30)
  Erster Schritt: der Standardweg-Autobau — die vorgegebene gerade
  Kachel-Linie vom Start- zum Ziel-Marker je Gebiet (aus der
  Karten-Runde vom 2026-10-29). **Stand 2026-11-02: erster Schritt
  fertig und abgenommen** — PathConnectivity als Weg-Kopf
  (GetEntryCell/GetExitCell), DefaultPathBuilder legt die Linie lokal,
  PathGrid sperrt die zwei End-Zellen gegen Abriss (DECISIONS
  2026-11-02 — „Standardweg: lokal gebaut" und „Kachel-Sperre");
  Wochen-Soll P-B4-Start damit erfüllt. **Stand 2026-11-03: die
  Sende-Kette V1 steht** — Designrunde „Gegner laufen" entschieden
  und gebaut (DECISIONS 2026-11-02/03 — „Host simuliert",
  „Steckbrief-Assets", „HUD-Panels", „Sende-Panel", „Sende-Brief"):
  Steckbrief-SO samt Grunt, Host-Läufer, Panel-Basis, Sendegebäude
  mit beiden Öffnungswegen, MonsterSpawner; Solo-Test bestanden —
  Knopf → Grunt läuft die Linie (LOG 2026-11-02/03, Zeiten in
  ABGABE_NOTIZEN → „P-B4"). Offen, in dieser Reihenfolge:
  Aufräum-Runde zuerst (Ein-Panel-Regel in der Panel-Basis,
  Klick-Verteiler-Entscheid — Isors Ansage vom 2026-11-03), dann
  Multiplayer-Doppeltest (Sende-Kette auf beiden Bildschirmen,
  „nur meins"), dann Leben-Brett und Wander-Routing (schreibt
  Claude), dann der Prüfpunkt.
- [ ] **P-B5 · Takt + Senden** — Timer mit Bereit-Knopf, Sende-Gebäude
  mit Warteschlange, Sends laufen mit dem Wellenstart, fester
  Sende-Ring. (~5–6 h)
- [ ] **P-B6 · Ressourcen** — Gold, Diamanten, Kacheln als Werte;
  Einkommen bei Timer null; Preise verdrahtet; Minimal-HUD. (~3–4 h)
- [ ] **P-B7 · Erster Wächter** — Pfeilturm: über die Figur
  platzieren, Ziel in Reichweite, schießen, Monster sterben, Gold
  fließt — der Spaß-Test der Abgabe. (~8–10 h) Aus der P-B2-Runde
  dazu: Die Design-Runde entscheidet die Panel-Form am Wächter-Platz
  (alle vier sofort oder Sockel-Upgrade) und die Preisaufteilung
  zwischen Platz und Wahl (DECISIONS → „2026-10-23 — Bau-Erlebnis:
  Kategorie-Leiste und Objekt-Panel").
- [ ] **P-B8 · Mine + Arbeiter** — Streichkandidat, faktisch
  Alpha-Material; Notlösung ist ein Kachel-Kauf-Knopf. (~7–8 h)
- [ ] **P3 · Polish-Merkliste** — gesammelt beim Bauen, fällig
  frühestens mit den Messrunden: Szenen-Hygiene Testarea (die
  Szenendatei trägt einen verwaisten BuildModeController-Datenblock
  ohne GameObject — im Editor unsichtbar, beim Umbau vom 2026-10-31
  übrig geblieben; bei Gelegenheit ausräumen); Fehlklick-Filter beim
  Laufbefehl (Klick ins fremde Gebiet läuft heute ans Ufer, spawnt den
  Ring am unerreichbaren Punkt und storniert die Bau-Warteschlange —
  die harte Grenze erledigt das Insel-NavMesh, das hier ist nur
  Spielgefühl; Kandidat: Ziel vorab per NavMesh-Pfadprüfung ablehnen,
  2026-10-31); Menü-Branding tauschen (trägt noch
  das Isor's-Tower-Logo aus der Übernahme-Kette); Wand-Klick-Filter
  (der Klick-Strahl ignoriert Wände und trifft den Boden dahinter);
  Tick-Rate und Interpolation messen (Latenz,
  `Knowledge/Unity/netzwerk-latenz-anatomie.md`); Settings-Anbindung
  der Schalter (Edge-Pan, Freiflug-Grenze, Kamera-Dauerfolgen als
  Option); Spieler-Optik für lose Vorratskacheln (V1 lässt verbunden
  und lose bewusst gleich aussehen — DECISIONS → „2026-10-23 —
  Raster: Zellgröße als Wert, Rig als Prefab"); Halte-Bauen (Platzieren
  bei gehaltener Maustaste, gedrosselt nach dem Halte-Intervall-Muster
  des ClickCommandInput); Klick-Marker auf Kacheln (der Ring spawnt am
  Boden und verschwindet im Kachelinneren — Varianten: Lift als
  Inspector-Wert oder Kacheln in die Ground-Maske, zusammen mit P-B4
  entscheiden); Nummern auf den Queue-Geistern (DECISIONS nennt
  nummerierte Geisterbilder, V1 läuft ohne); Abriss-Modus als drittes
  Werkzeug (viele Kacheln schnell wegreißen, Zuschnitt offen);
  Rechtsklick im Bau-Modus legt das Werkzeug weg, statt nur zu laufen —
  heute storniert er dabei auch die Shift-Reihe, weil der Laufbefehl
  immer gilt; Linksklick im Bau-Modus auf ein liegendes Objekt verlässt
  den Modus und öffnet dessen Panel (drei Spielgefühl-Merkposten aus
  der Abbau-Runde, 2026-10-29); UI-Ausgestaltung als eigene große
  Design-Runde nach der Kernmechanik (Upgrades, Panel-Inhalte mit Bild
  und Werten, Hover-Infos, Anordnung — Karten-Runde 2026-10-29);
  Optik-Phase samt Asset-Liste (Welt verschönern, Monster- und
  Wächter-Figuren, Gebäude für Mine und Senden — evtl. eines für
  beide —, Bäume, Detail-Texturen; Gebiete optisch unterscheidbar
  machen — Karten-Runde 2026-10-29); Eintritts-/Austritts-Zelle:
  Panel und Upgrades ja oder nein — im Playtest entscheiden; Regel:
  verhalten sie sich anders als normale Kacheln, müssen sie auch
  anders aussehen (Portal-Optik), sonst normale Kachel mit
  Schloss-Symbol im Panel; nur der Abriss bleibt immer tabu
  (Sperre vom 2026-11-02).

## Meilenstein-Plan (Fertig-Linien und Inhalte)

Begründung: DECISIONS → „2026-10-29 — Meilenstein-Plan: immer eine
Version voraus" und „2026-10-30 — Meilenstein-Etappen". Die offiziellen
Termine besitzt `Uni/Semester_3/STUNDENPLAN.md`. Regel: **Fertig heißt
rund eine Woche vor der Abgabe** (die Fertig-Linien samt
Inhalts-Milestones gehen so ins Pitch-GDD — sie sind die verlangten
Pufferzeiten); intern gilt zusätzlich die private Ambition „immer eine
Version voraus". Der Wochenplan dazu wird sonntags aufgestellt und
lebt oben auf der Status-Tafel.

- [ ] **M1 · Spieleprototyp + Game Pitch** — fertig **Fr 20.11.**
  (Feature-Stopp; gilt nicht für Core-Loop-Essentielles), Abgabe
  Fr 27.11., Präsentation Do 03.12.
  Systeme: P-B3 → P-B7; P-B8 als letzter Baustein (~18.–20.11.) mit
  Streichrecht. Wochen-Soll: P-B3 + P-B4-Start bis So 02.11. · P-B4
  samt Prüfpunkt + P-B5-Start bis So 08.11. · P-B5 + P-B6, P-B7-Start
  bis So 15.11. · P-B7 bis ~Di 17.11., dann P-B8.
  Pufferwoche 20.–27.11. = Abgabe-Fabrik: Playtests übers echte Netz,
  Erkenntnis-PDF (≥500 Wörter), G2-GDD-Nachzug samt Zeitplan-Kapitel,
  Pitch-Slides (Teil der Abgabe), spielbarer Build, aufgeräumte
  Projektdateien; Probe-Pitch vor dem 03.12.
- [ ] **M2 · Projektplanung (benotet)** — fertig **Fr 11.12.**, Abgabe
  Fr 18.12. Reine Doku-Etappe (parallel läuft der Alpha-Bau): das GDD
  wird als PDF benotet („sinnvollen Projektplan erstellen");
  Pitch-Feedback vom 03.12. einarbeiten, Zeitplan auf Ist-Stand,
  dazu der feste Abschnitt **„Plan gegen Wirklichkeit"** — Schätzung
  gegen Grindstone-Messung je Baustein samt Kalibrierungs-Satz.
- [ ] **M3 · Alpha** — fertig **Sa 26.12.** (Isors Wahl: zwei Wochen
  Puffer, Rest-Ferien gehören der Optik), Abgabe Fr 08.01.,
  Präsentation Do 14.01.
  Systeme: Win-/Lose-Condition simpel (Leben null → raus, letzter
  gewinnt, zurück ins Menü — Statistiken/Spielerprofil bewusst nicht
  im GDD), Einkommens-Schleife rund, Lade-Timeout, Vier-Spieler-
  Härtetest, Refactor-Pass. Erste Spur (Vorjahres-Anforderung):
  Minimal-Audio (Bau-Sound, Klick) + genau ein echtes Asset als
  Pipeline-Test; Minimal-HUD deckt „erste GUI" ab.
  Paket: Build, Ist-Soll-Präsentation, GDD-Update (Änderungen
  markiert).
- [ ] **M4 · Beta** — fertig **Do 22.01.**, Abgabe Fr 29.01.,
  Präsentation Do 04.02. Bauzeit: die Ferien (27.12.–22.01.).
  UI-Design-Runde zuerst, dann Umsetzung + Menü-Branding raus. Assets
  integrieren (fertige freie Packs laut GDD): Welt, vier Gegnertypen
  (Quaternius), Wächter-Figuren (Bug Knight), Gebäude, Gebiets-
  Kennzeichnung per Zahl. Alle vier Wächter-Rollen gebaut; die drei
  Stufen je Wächter sind Wert-Ausbauten über das Objekt-Panel
  (GDD-Zusage bleibt; Absicherungs-Satz im G2: Feinabstimmung der
  Stufen liegt in den Messrunden). Sound-Grundvertonung aus freien
  Bibliotheken — der Game-Audio-Unterricht (ab 18.01.) liefert den
  Feinschliff. Fremde Tester. Paket wie M3.
- [ ] **M5 · Goldmaster** — fertig **Do 05.02.**, Abgabe Fr 12.02.,
  Präsentation Do 18.02. Nichts Neues mehr: Balancing-Messrunden
  (zwölf Stufen-Wertesätze, Preise, Startvorräte, Einkommen; dazu die
  P2-Prüf-Merkposten), Polish nach der P3-Merkliste (Einkaufszettel,
  keine Pflicht), Code-Aufräum-Pass (Conventions — wird benotet),
  finale GDD-Fassung. Kein Trailer (Isor, 2026-10-30: gehört nicht
  zum Semesterprojekt). Rejoin-Stretch: Entscheidung am 05.02.-Stand,
  keinen Tag früher (DECISIONS → Verbindungsverlust).
- [ ] **M6 · Reflexion + Portfolio** — Reflexion fertig Mo 16.02.
  (Abgabe 19.02., ≥1000 Wörter; erst Isors Bericht, dann Text;
  Rohmaterial: Lern-Log, ABGABE_NOTIZEN). Portfolio fertig So 21.02.
  (Abgabe 26.02. — trägt die Modulnote; letzter Betreuungstermin
  25.02. liegt davor).
