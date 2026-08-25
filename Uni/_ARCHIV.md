# _ARCHIV.md — Uni, überholte Einträge

Ownership: Nur überholte Einträge der Uni-Schicht. Jeder nennt, wodurch
er abgelöst wurde. Wird nie aufgeräumt — ein Archiv wird selten gelesen,
seine Größe kostet nichts (`Kern/DOC_RULES.md`, Abschnitt 4).

---

## 2026-08-22 — Abgabe-Block der alten ROADMAP

**Abgelöst durch:** `PLAN.md` für kurzfristige Arbeitspläne (E12) und die
LOGs für das, was tatsächlich passiert ist.
**Warum hier:** Dies war ein Tagesplan für die Portfolio-Abgabe vom
2026-08-21 — 498 der 708 ROADMAP-Zeilen für eine Woche, die vorbei ist.
Genau daran ist die ROADMAP vollgelaufen: kurzfristiger Plan und
Langfrist-Planung standen in derselben Datei.
**Nicht mit archiviert:** Die Unterabschnitte „Arbeitsregeln, die weiter
gelten" und „Restliste Politur" — sie gelten weiter und wurden einzeln
einsortiert.

Originaltext, unverändert:

## Als Nächstes — Abgabe in zwei Ständen
**Entschieden 2026-08-12:** Es wird zweimal abgegeben. Stand 1 ist
vollständig und benotbar — als hätte es keinen zweiten Termin. Stand 2
bringt nur noch Kleinigkeiten. Frist ist der 21.08.

**Stand 2026-08-17:** Stand 1 ist hochgeladen (einen Tag später als
geplant, siehe unten). Offen für Stand 2 sind das Lernziel S3 (Herde über
den Placer) und zwei TDD-Kleinigkeiten. Danach erneut kopieren, zippen und
hochladen.

Grund: Ein vollständiger früher Stand nimmt das Risiko aus der Woche.
Was am Sonntag steht, kann nicht mehr schiefgehen.

**Zeitbudget:** Mi 4 h, Do 4 h, Fr bis So zusammen rund 17 h — gut 25 h.
Der Bedarf unten liegt bei 15 bis 18 h. Der Puffer ist Absicht.

**Reihenfolge nach Isors Vorgabe (2026-08-12):** Zuerst das, was das
Spiel lebendig macht — Ton, UI, Licht, Bepflanzung. Die Dokumentation
kommt bewusst zuletzt an einem Stück (Sonntag), weil bis dahin noch
Dinge dazukommen, die im Text stehen müssen. Ein früher Textstand wäre
doppelte Arbeit. Das Dokument ist ohnehin schon einmal zum Feedback
eingereicht.

### Mi 12.08. — entfällt
Planungssession. Isor geht früher schlafen, um Donnerstag mit voller
Energie zu starten — bewusste Entscheidung, kein Verzug: die tragenden
Tage sind Fr bis So.

### Do 13.08. — Ton — ausgefallen, am Fr 14.08. nachgeholt und erledigt
Isor hatte Mi und Do keine Zeit (Isor, 2026-08-14). Entscheidung: Der
Ton-Block wurde nicht verschoben, sondern zusammen mit dem Freitagsprogramm
am 14.08. abgearbeitet. Damit bleibt Stand 1 am Sonntag vollständig und
Stand 2 frei für Kleinigkeiten.
1. [x] **Musik und Soundeffekte eingebaut** (2026-08-14) — Mixer mit drei
   Gruppen, Musik in beiden Szenen, Windböen, Fackelfeuer, Schafe,
   Spielerschritte, Antwortlaut beim Zähmen. Alle Klänge CC0, Quellen in
   `03_AssetLibrary\Extern_Frei\Audio\`. Einzelheiten im FEATURE_LOG,
   Begründungen in DECISIONS 2026-08-14, Stoff fürs TDD in TDD_NOTES.
   Offen daraus: Audio-Zeilen in Tabelle 9 (Kapitel 12) nachtragen —
   nur Quelle und Lizenz je Zeile, keine Attributionsformel nötig. `Village.unity` enthält
   derzeit **null AudioSource und null AudioListener** — es gibt keinen
   Ton. Größter einzelner Eindrucks-Hebel und ein abgeschlossener Block,
   der in einen 4-Stunden-Abend passt. Reihenfolge: Listener am Spieler
   prüfen, Umgebungsmusik, dann Einzeleffekte (Schritte, Fackel, Schafe,
   Interaktion).
   Lizenzen: Die Quellen kommen als **Zeilen in die Asset-Tabelle
   (Tabelle 9, Kapitel 12)** — kurze Nennung mit Quelle und Lizenz, kein
   eigenes Unterkapitel (Isor 2026-08-12: sonst doppelt sich der Text).
   Beim Herunterladen gleich Quelle und Lizenz mitnotieren, sonst muss
   das am Sonntag rekonstruiert werden.

### Fr 14.08. — UI (langer Block)
2. [ ] **In-Game-UI aufwerten:** Fadenkreuz kontextsensitiv auf
   Interactable, Prompt-Stil (Box, Fade, Tastensymbol), HUD beim
   Pausieren ausblenden, TMP-Font-Schärfe (Texte sind pixelig).
   **Optik in einem Rutsch über alle drei Menüs** (Isor, 2026-08-14):
   Hauptmenü, Pausenmenü und Options sollen wie ein System aussehen —
   gleiche Schrift, Farben und Abstände. Einzeln aufgehübschte Teile
   wirken zusammengewürfelt. Größter Einzelhebel ist die TMP-Schärfe,
   die alle Texte auf einmal betrifft.
   Offene Frage dabei: Das Options-Panel ist halbtransparent, damit im
   Pausenmenü das Dorf durchscheint. Im Hauptmenü scheint dadurch der
   blaue Hintergrund durch — entweder so lassen oder dort einen eigenen
   Hintergrund hinterlegen. Erst beim Optik-Durchgang entscheiden.
3. [x] **Menü-UI und Options** — fertig (2026-08-14 gebaut, 2026-08-15
   im Dorf zum Laufen gebracht). Ursache des Maus-Problems: Das
   Options-Panel war durch vier Umzüge (Szene → eigenes Prefab →
   VillageUI → PauseMenuRoot) intern beschädigt; eine frische Kopie aus
   dem Hauptmenü funktionierte sofort. Alles andere war ausgeschlossen —
   Raycast traf, Position stimmte, Click-Action feuerte, `timeScale`,
   Cursor, EventSystem und Doppel-Systeme ohne Befund. **Lehre: Bei
   unerklärlichem UI-Verhalten zuerst eine frische Kopie testen, bevor
   man stundenlang misst.**
   Ebenfalls erledigt: `GameController.Pause()` setzt das Menü beim
   Öffnen auf die Button-Seite zurück, damit nach ESC im Options-Fenster
   nicht wieder Options erscheint.

   Alter Stand der Beschreibung:
   Options-Panel gebaut mit vier Reglern (Gesamt, Musik, Effekte,
   Maus-Empfindlichkeit), Prozentanzeige, `GameSettings` mit
   Mixer-Anbindung und `PlayerPrefs`-Speicherung. **Im Hauptmenü läuft
   alles.** Panel liegt als Prefab in `Shared/UI/Prefabs/`.

   **OFFEN — erster Punkt am nächsten Arbeitstag:** Im Pausenmenü des
   Dorfes reagieren die Slider **nicht auf die Maus** — kein Hover, kein
   Klick, kein Ziehen. Tastaturnavigation funktioniert, Buttons lassen
   sich per Enter auslösen. Im Hauptmenü funktioniert dasselbe Prefab
   einwandfrei.

   Bereits ausgeschlossen (2026-08-14, alles gegen die Dateien geprüft):
   - `Time.timeScale = 0` — testweise entfernt, keine Änderung
   - `InGameUI` und `Fps` als Raycast-Blocker — beide deaktiviert, keine
     Änderung
   - `Raycast Target` am `PauseMenuRoot` — ausgeschaltet, keine Änderung
   - fehlender `GraphicRaycaster` — in beiden Canvas vorhanden, gleiche
     Einstellungen
   - `CanvasGroup` mit abgeschaltetem `Interactable` — existiert nirgends
   - zwei EventSystems — es gibt genau eines, korrekt konfiguriert
     (`Point`, `Left Click`, `Navigate`, `Submit` gesetzt)
   - Canvas-Unterschiede — beide Screen Space Overlay, gleicher
     CanvasScaler (1920×1080)
   - Cursor gesperrt — Mauszeiger ist im Pausenmenü sichtbar
   Noch nicht getestet: Game-View-Zoom auf 1x stellen und vorher ins
   Spielfenster klicken (Editor-Artefakt), sowie ein Test im Build.

   Ebenfalls offen: Mit ESC bei offenem Options-Fenster bleibt beim
   nächsten Öffnen Options statt der Pause-Buttons stehen. Zwei Zeilen in
   `GameController.Pause()` — Options aus, Pause-Panel an.

### Sa 15.08. — verbraucht für Punkt 3
Der ganze Samstag ging für das Options-Fenster im Dorf drauf (siehe
Punkt 3). Die unten geplanten Punkte 4 bis 10 sind **nicht** angefangen
und rutschen auf Sonntag bzw. in Stand 2.

**Lage am Sa 15.08., 22:30 — Neuplanung für den Sonntag:**
Fertig sind Ton (Punkt 1) und Menü/Options (Punkt 3). Offen sind alle
Abgabe-Pflichtteile. Sonntag reicht nur, wenn die Politur gestrichen wird.

Sonntag in dieser Reihenfolge — Pflicht zuerst:
1. Punkt 7 (Herde über den Placer, Lernziel S3) — ~1 h
2. Punkt 8 (Abgabe-Build) — ~1 h
3. Punkt 9 (Screenshots) — ~1 h
4. Punkt 10 (Video Engine-Tool) — ~1 h
5. Punkte 11–19 (TDD, READ_ME, Projektkopien, Zippen, Upload) — ~6 h

In Stand 2 (Mo–Do) verschoben, weil sie keine Bewertungskriterien sind:
Punkt 2 (In-Game-UI-Politur), Punkt 4 (Licht und Bepflanzung),
Punkt 5 (Baum-LOD), Punkt 6 (Terrain-Texturen).

### Sa 15.08. — ursprüngliche Planung (nicht abgearbeitet)
4. [ ] **Licht und Bepflanzung:** Fackeln setzen, Glühwürmchen setzen,
   mehrere Herden verteilen.
5. [ ] **Baum-LOD nachziehen** — die Stufen kommen aus Blender mit, die
   Umschaltabstände passen nicht.
6. [ ] **Terrain-Texturen ansehen** — Umfang bewusst offen, erst schauen
   was mit wenig Aufwand deutlich besser aussieht.
7. [ ] **Mindestens eine Herde über den Placer** statt von Hand (~1 h).
   Lernziel **S3** („generierte Bevölkerung") und damit ein
   Bewertungskriterium, kein Polish — kleinster Punkt des Tages mit der
   größten Notenwirkung. Optional daneben ein einfacher Feind (Goblin)
   über denselben Weg.
8. [ ] **Abgabe-Build erstellen und durchspielen** (~1 h): kein
   Development Build. Kommt in beide `release`-Ordner. Die Funktionalität
   wird laut Vorgabe am Build bewertet.
9. [ ] **Screenshots** (~1 h): drei je Projektordner, ab 1024x768,
   `Press1.png`, `Press2.png`, `Press3.png`. Betrifft Engine-Tool, KI
   Prototyp, Simulation, Prozedurale Erweiterung. Die vorhandenen Bilder
   sind Shader-Graphen aus dem TDD, keine Spielbilder.
10. [ ] **Video für Engine-Tool-Entwicklung** (~1 h): 30 bis 90 Sekunden.
    Der einzige Projektordner ohne Video.

### So 16.08. — Ablauf nach Isors Vorgabe (2026-08-15, 22:45)
**Vormittag bis 17:00 — Politur, in dieser Reihenfolge:**
1. [x] **Hauptmenü neu gestaltet** (2026-08-16) — Design-Session mit zwei
   Varianten, entschieden wurde die zentrierte Tafel. Dorf-Screenshot als
   Hintergrund (deckt zugleich Punkt 9), Oswald Bold SDF für Titel und
   Buttons, Fackel-Palette, englische Beschriftungen. Werte und
   Begründungen in DECISIONS 2026-08-16.
2. [x] **Options-Fenster aufgehübscht** (2026-08-16) — feste Tafel statt
   Vollbild-Schleier, damit im Dorf das Dorf sichtbar bleibt. Regler in
   Ember-Füllung. Damit ist die offene ROADMAP-Frage vom 14.08. zur
   Halbtransparenz erledigt.
3. [x] **Pausenmenü auf dieselbe Tafel gebracht** (2026-08-16) — Giftgrün
   ersetzt, ein Schleier je Ebene. Einzelheiten im FEATURE_LOG.
4. [x] **In-Game-HUD gebaut** (2026-08-16) — in sieben Bausteinen:
   HUD-Root und Ausblenden beim Pausieren, Zähmzähler, Uhr, Spieler-Kartusche
   mit neuer `Health`-Komponente, Zielzustand getrennt vom Prompt, Politur
   über alles. Einzelheiten im FEATURE_LOG, Begründungen in DECISIONS.
   Zwei Anzeigen zahlen auf **S3** ein, weil sie die vorhandene Simulation
   erstmals sichtbar machen: Tageszeit und der Zustand der Schafe.
Wunschliste dafür (Isor): Tageszeit sichtbar machen, Zustandsbalken am
Schaf, ein umherlaufender Gegner der die Herde verjagt, ggf. Spielerleben.
Zwei davon zahlen auf **S3** ein („Simulation einer gewohnten Umgebung"):
die Tageszeit-Anzeige und der Gegner. Der Rest ist Feature, kein Kriterium.

**Ab 17:00 — harte Grenze, dann nur noch Abgabe:**
Build, Screenshots, Video, TDD, READ_ME, Projektkopien, Zippen, Upload.

**Zeitwarnung (2026-08-15):** Nach 17:00 bleiben etwa sieben Stunden, der
Bedarf liegt bei acht. Entschärfung: Claude legt am Vormittag parallel die
Doku-Vorarbeit vor (siehe unten), das spart rund zwei Stunden. Und die
Frist ist der 21.08. — was am Spielstand hängt (Build, Screenshots, Video,
Projektkopien) muss Sonntag fertig werden, reiner Text kann Montag folgen.

**Punkt 7 (Herde über den Placer)** bleibt drin, aber mit hartem Deckel von
einer Stunde. S3 ist ein benanntes Lernziel der Aufgabenstellung, und die
Placer-Infrastruktur steht bereits. Läuft es nach einer Stunde nicht,
abbrechen.

### Do 17.08. — Abgabe Stand 1 hochgeladen
Beide Portfolios wurden an einem Stück fertiggestellt, Aufgabe für Aufgabe
gegen die Original-Aufgabenstellungen geprüft und **am Abend des 17.08.
vollständig hochgeladen**. Damit liegt ein benotbarer Stand auf dem Server.
Begründungen in DECISIONS 2026-08-17.

Erledigt in dieser Session:
- Beide READ_ME fertig geschrieben, alle Platzhalter und Kommentarblöcke
  raus, Kriterien-Kürzel eingetragen (D004: KI Prototyp K1/K2/K3/S1,
  Simulation K3/S2/S3)
- TDD: Deckblatt korrigiert (Isor), Wortanzahl 21366, sieben Audiopakete
  in Tabelle 9, KI-Kennzeichnung unter Tabelle 1, PDF neu exportiert
- Beide `release`-Ordner mit dem Build gefüllt, beide `src` nachgezogen
  (281,8 MB, `Village.unity` 139,7 MB mit 21.354 platzierten Bäumen)
- Neue Press-Screenshots und Videos für Engine-Tool, KI Prototyp,
  Simulation und Prozedurale Erweiterung; Zweitkopien mit sprechenden
  Namen unter `01_Uni\Semester_2\Abbildungen\`
- `Messreihen_README.md` von 132 auf 33 Zeilen gekürzt, lange Fassung
  gesichert unter `Arbeitsdateien\Messungen\`
- ZIPs erzeugt und geprüft: D003 308,4 MB, D004 540,1 MB

**Offen geblieben aus der 16.08.-Liste:**
- [ ] **Balkendiagramm der sechs Messpunkte** zu Tabelle 8 einsetzen
  (Punkt 13). Neue Abbildung nur über `Verweise → Beschriftung einfügen`.
- [ ] **Zwei Sätze im Fazit** zur fehlenden `namespace`-Gliederung
  (0 von 83 Dateien) als bewusst aufgeschoben (Punkt 14).

### ERLEDIGT (2026-08-20): Lernziel S3 — generierte Bevölkerung
**Erfüllt mit Build 0.0.3.** `TerrainConfig_Default.asset` enthält jetzt vier
Placeables: `BirchTree_1`, `GrassSingle_x2`, `VFX_FireFly` und
`SheepHerdManager_01`. Vom Herdenverwalter stehen 19 Instanzen in
`Village.unity`, gesetzt über den Placer nach Höhenband 0,14–0,30 und
Hangneigung bis 8,4°. Gesetzt wird die Herde, nicht das Einzeltier — das hält
die Zahl klein und die Agenten auf begehbarem Grund. Die unten beschriebene
Falle mit dem `RuntimePlacementSpawner` traf zu und wurde eingehalten: Der Typ
ist im Editor platziert und in der Szene gespeichert.
Ursprüngliche Notiz vom 2026-08-17:

Beim Prüfen gegen die Aufgabenstellungen gefunden (2026-08-17). **S3 steht
in Modul 004 sowohl bei Aufgabe 2 als auch bei Aufgabe 3** und ist nicht
erfüllt: `TerrainConfig_Default.asset` enthält nur zwei Placeables
(`BirchTree_1`, `GrassSingle_x2`). Die Herde sitzt von Hand als
`SheepHerdManager_01.prefab` im `Village.prefab`; in `Village.unity` kommt
„Sheep" kein einziges Mal vor.
- [ ] Herden-Prefab als drittes Placeable eintragen, im Editor-Tool
  platzieren, Szene speichern. Kein Code nötig — das Tool erzeugt die
  Bedienzeile aus der Placeable-Liste.
  **Falle:** `RuntimePlacementSpawner` spawnt zur Laufzeit nur instanced
  Typen. GameObject-Typen wie die Herde müssen im Editor platziert und in
  der Szene gespeichert werden, sonst fehlen sie im Build.
- [ ] Danach zwingend: Kopierskript erneut, neu zippen, erneut hochladen —
  der zweite Upload ersetzt den ersten.

### Mi 19.08. — Dozenten-Feedback zu Stand 1 + Polishing
**Zeitbudget (Isor, 2026-08-18 abends):** ca. 17:00–22:00, im Notfall bis
0:00. Frist bleibt Fr 21.08., 20:00 — danach also noch ein Tag Puffer.

**Feedback der Fachbetreuung am 18.08. zu Stand 1** (mündlich, mit
Zeitstempel — schriftliches Feedback steht noch aus):
- **Engine-Tool, 14:17** — sieht gut aus, besonders der Prefab-Painter
  bietet viele Möglichkeiten. Isor hat offen gelegt, dass er das Tool
  entworfen und mit KI-Unterstützung programmiert hat und dass es
  ursprünglich ein privates Werkzeug war (nicht im TDD erwähnt, siehe
  DECISIONS 2026-08-07). Die Dozentin: in Ordnung, drinlassen, dafür
  eher Zusatzpunkte als Abzug.
- **Threadoptimierung, 14:54** — sie mag grafische Auswertungen, versteht
  aber, dass reine Messdaten keine grafische Darstellung hergeben.
  Deckt sich mit dem offenen Punkt 13 (Balkendiagramm) unten — genau der
  fehlende Beleg.
- **PCG, 14:19** — sieht wirklich gut aus. Zwei Anmerkungen:
  1. Ein Ladebildschirm während der Generierung wäre schön.
  2. Sie fände es schöner, wenn die Einstellungsmöglichkeiten der
     TerrainConfig auch im Editor-Fenster selbst einstellbar wären, statt
     nur über das danebenliegende Inspector-Fenster des ScriptableObjects.
     **Isor-Entscheidung (2026-08-18): nicht umgesetzt** — zu viel Aufwand
     für die verbleibende Zeit, kein Bewertungskriterium.
- **Gesamteindruck:** alles sehr schön und gut, keine großen, nur kleinere
  Kritikpunkte.

**Für Kapitel 14 (Änderungsverlauf) vorbereitet** — deckt das
Feedbackelement *Person* ab („Wurde genügend Feedback eingeholt und
umgesetzt?"), steht in beiden Aufgabenstellungen: zwei Zeilen mit was
zurückkam und was geändert wurde. Isor trägt morgen nach dem Arbeiten ein,
was tatsächlich umgesetzt wurde.

**Prioritätsliste morgen, absteigend nach Kriteriumsbezug:**
1. [~] **Balkendiagramm der sechs Messpunkte** (2026-08-19) — Grafik erzeugt:
   `01_Uni\Semester_2\Abbildungen\Threading_Messreihe.png`, Zweitkopie als
   `Messreihe_Balkendiagramm.png` im Messungs-Ordner der D003-Abgabe, im
   `Messreihen_README.md` verlinkt. Textbausteine für Beschriftung und
   Lauftext in `Arbeitsdateien\Textbaustein_Abbildung_Messreihe.txt`.
   **Einbau ins TDD entfällt** (Isor, 2026-08-19): Das Dokument bleibt wie
   es ist. Die Grafik erreicht die Dozentin trotzdem, weil sie im
   Messungs-Ordner der Abgabe liegt und im `Messreihen_README.md` steht.
   Die Textbausteine bleiben liegen, falls es doch noch reingehen soll.
2. [x] **Schafe über den Placer** — **doch noch am 2026-08-20 gemacht.**
   Gesetzt wurde `SheepHerdManager_01`, nicht das Einzelschaf: 19 Herden
   über den Placer. Lernziel **S3 ist damit erfüllt**, siehe den Block oben.

**Upload-Termin: Do 20.08. abends** (Isor, 2026-08-19). Bis dahin wird
gebaut, danach in einem Rutsch: Build, beide `release`-Ordner, `src`
nachziehen, zippen, hochladen. Der Freitag bis 20:00 ist nur noch Puffer.
Alles, was bis dahin nicht im ZIP ist, zählt nicht — Stand 1 vom 17.08.
bleibt sonst der bewertete Stand.
3. [x] **Ladescreen beim Szenenwechsel** (2026-08-19) — erledigt. Statt um
   die Editor-Generierung wurde er um den Szenenwechsel Hauptmenü → Dorf
   gelegt: Im Build gibt es keine Generierung (der `TerrainToolPresenter`
   liegt in `Editor/` und wird gestrippt), die 90 Sekunden auf dem Rechner
   der Dozentin sind das Laden von `Village.unity`. Damit trifft der
   Ladescreen ihr Feedback genauer als ein Fortschrittsbalken im Tool.
   Deckt zugleich ROADMAP-Punkt 10 unter „Nach der Uni-Abgabe" ab.
   Einzelheiten im FEATURE_LOG, Begründungen in DECISIONS 2026-08-19.
4. [~] **Collider** — **Bäume erledigt** (Isor, 2026-08-19): `CapsuleCollider`
   gegen den Spieler, `NavMeshObstacle` mit Carve gegen die Schafe, im Spiel
   geprüft. Einzelheiten im FEATURE_LOG, Begründungen in DECISIONS.
   **Offen bleiben die Häuser** — dort ist noch nichts geprüft.
5. [x] **Karten-Begrenzung** (2026-08-19) — vier unsichtbare Wände, gebaut
   vom Terrain-Tool über `BuildWorldBounds`. Einzelheiten im FEATURE_LOG,
   Begründungen in DECISIONS 2026-08-19.
   **Dabei aufgefallen:** Der Wasserspiegel hat keinen Collider — der
   Spieler läuft in den See hinein und weiter auf dem Grund, mit Kopf unter
   Wasser und ohne Rückmeldung. Beim Vorführen derselbe Ärger wie das
   Herunterfallen. Nicht angefasst, Entscheidung offen.
6. [x] **Fackel-Licht und -Farbe** (Isor, 2026-08-19) — dazu Collider an
   beiden Fackel-Prefabs. Werte im FEATURE_LOG.
   **Weiter offen:** die beiden Prefabs heißen immer noch `Torch .prefab`
   und `Torch.prefab`, Unterschied nur ein Leerzeichen. Vorschlag bleibt
   `Torch_Calm` und `Torch_Blazing`.
7. [x] **Zeit-Vorspulen** (2026-08-20) — gehaltene Taste `T`, Anzeige unter
   der Uhr, dazu Tageslänge auf 20 Minuten. Einzelheiten im FEATURE_LOG,
   Begründungen in DECISIONS 2026-08-20.
8. [x] **Glühwürmchen über den Placer** (2026-08-20) — als dritter
   Placeable-Typ gesetzt, nur bei Abend und Nacht sichtbar über die neue
   `NightVfx`-Komponente. Einzelheiten im FEATURE_LOG.

**Nach der Abgabe: Bäume an Steilhängen** (Isor, 2026-08-20). Seit heute
stehen alle Bäume senkrecht, an steilen Stellen steht der Stammfuß dadurch
frei in der Luft. Für die Abgabe akzeptiert, für ein echtes Spiel nicht gut
genug — Isors eigene Einschätzung. Richtig wäre: `MaxSlope` auf 25–30 senken,
sodass an Steilhängen gar nichts platziert wird, plus ein hangabhängiges
Einsinken im `ObjectPlacer`. Beides ändert die Waldverteilung, also nur
zusammen mit einem bewussten Neuaufbau der Szene angehen.

**Erledigt: Wasser bleibt ohne Collider** (Isor, 2026-08-20). Der Spieler
läuft weiterhin in den See und auf dem Grund weiter. Bewusst so gelassen.

**Erledigt: Häuser-Collider** (Isor, 2026-08-20) — jedes Child trägt bereits
einen Collider, es war nichts zu tun.

**Ordnerstruktur — Dozentin wünscht Umbau, EMPFEHLUNG: nicht vor der
Abgabe.** Gewünscht: oberste Ebene nach Typ (`Scripts/`, `Animation/`,
`Texture/`, `Materials/`), darunter Unterordner je Feature/System — das
Gegenteil der aktuellen, bewusst gewählten Struktur (CODE_GUIDELINES,
Entscheidung 2026-07-19: Feature zuerst, `Entities/<Name>/Scripts/` usw.).
Grund für die Empfehlung: Ein Umbau dieser Größenordnung betrifft
vermutlich alle Scripts im Projekt (83 Dateien laut Fazit-Notiz zu den
namespaces) und muss im Unity-Editor per Drag&Drop erfolgen, nie im
Explorer, sonst brechen die .meta-GUIDs und damit alle Referenzen. Das
ist dasselbe Risiko, das schon den `namespace`-Umbau und
`ObjectPlacer.PlaceType` von der Abgabe ferngehalten hat (siehe „Bewusst
nicht mehr vor der Abgabe" weiter unten). Vorschlag: Feedback so im
Änderungsverlauf vermerken („erkannt, wird nach der Abgabe umgesetzt"),
tatsächlicher Umbau erst in der Phase „Nach der Uni-Abgabe".

### Alte Punkte der 16.08.-Liste (Belege)
11. [x] **Deckblatt richtiggestellt** (Isor, 2026-08-17): Modulname auf
    „Structured Game Development", Semester auf März 2026, Modulnummer auf
    `4FSC0PD003.1`.
12. **Entfallen** — kurze Quellenliste. Ursprünglich: Bridson, Amdahl und
    Perlin werden namentlich genannt, eine knappe Liste am Dokumentende
    genügt.
    **Korrigiert am 2026-08-16 (Isor):** Keine der drei
    Aufgabenstellungen verlangt Quellenangaben, Zitierweise oder ein
    Literaturverzeichnis; die Feedbackelemente fragen nach Codequalität,
    Serialisierung, Bedienbarkeit und nachvollziehbaren Performancedaten.
    Die frühere Forderung stammte aus dem Kontext der S4-Abgabe
    („Arbeiten nach akademischen Standards"), einem eigenen Dokument.
    Das TDD ist ein technisches Dokument, keine Seminararbeit.
13./14. offen — siehe oben unter „Offen geblieben aus der 16.08.-Liste".
15. [x] **Audio-Quellen in Tabelle 9 nachgetragen** (2026-08-17): sieben
    Pakete, alle CC0. Die Herkunft wurde über die .meta-GUIDs gegen Szenen
    und Prefabs geprüft, nicht aus `Audio_Quellen.txt` übernommen — die
    Notiz war an drei Stellen falsch (siehe TDD_NOTES 2026-08-17).
16. [x] **Abschluss erledigt** (Isor, 2026-08-17): Wortanzahl 21366,
    beide Unterschriften als Bild vorhanden, F9 gelaufen, PDF neu
    exportiert und in `Abgabe_Final` gelegt. Das S4-Dokument hat Isor
    selbst überarbeitet und ebenfalls neu exportiert.
17. [x] **Beide READ_ME fertig** (2026-08-17).
18. [x] **Projektkopien nachgezogen** (2026-08-17, zweimal — zuletzt am
    Abend nach dem Platzieren der Bäume).
19. [x] **Gezippt und hochgeladen** (2026-08-17). Die Upload-Grenze war
    kein Thema. Zippen brachte mehr als erwartet, weil `Village.unity` als
    YAML-Text stark komprimiert: 1,32 GB Ordner → 848,5 MB in zwei ZIPs.

### Geprüft am 2026-08-12 — Village-Altlasten
- `Village.unity` enthält **null Kamera-Komponenten** direkt in der
  Szene. Die Notiz „zwei aktive Kameras" vom 2026-08-02 ist erledigt.
- NavMesh-Bake ist auf dem aktuellen Aufbau, `Environment/Village/` hat
  genau ein Prefab, `Environment/Terrain/` nur Texturen (Isor).
- Die zwei Dateien unter `Environment/Torch/Prefab/` (`Torch .prefab` und
  `Torch.prefab`) sind **Absicht** — zwei Fackeln mit unterschiedlichen
  Einstellungen (Isor, 2026-08-12). Keine Dublette, nichts zu tun.
  Die frühere Notiz „Dubletten-Prefab" vom 2026-08-02 war ein Fehlschluss.

Damit sind alle drei Village-Altlasten aus der Notiz vom 2026-08-02
erledigt oder als Absicht geklärt.

### Nicht mehr geplant
Das Village-Prefab neu aufbauen (früherer Punkt 1b). Der bestehende
Aufbau trägt; die Zeit geht stattdessen in Ton, UI und Beleuchtung —
das ist am Bildschirm sichtbar, ein umgebautes Prefab nicht.

### Mo–Do 17.–20.08. — Stand 2
- [ ] **Do 20.08.: Ton-Block** — Inhalt siehe Punkt 1 oben. Der einzige
  große Posten in Stand 2, alles andere sind Kleinigkeiten.

Sonst keine großen Änderungen mehr. In Frage kommen:
- [ ] Politur aus Punkt „Restliste" unten, soweit sie abends passt
- [ ] Falls es Rückmeldungen zur formativen Abgabe gab: zwei Zeilen im
  Änderungsverlauf, was zurückkam und was geändert wurde (Feedbackelement
  *Person* in beiden Aufgabenstellungen)
- [ ] Was beim Durchspielen am Sonntag auffiel
- [ ] Die beiden Fackel-Prefabs sprechend umbenennen (heute `Torch .prefab`
  und `Torch.prefab`, Unterschied nur ein Leerzeichen). Die eine brennt
  ruhig, die andere aggressiver mit mehr Funken (Isor, 2026-08-12).
  Vorschlag: `Torch_Calm` und `Torch_Blazing` — oder die Bezeichner des
  `TorchMode`-Enums, falls die beiden dort schon Werte haben.
  Passiert im Unity-Editor, wenn ohnehin an den Fackeln gearbeitet wird.

### Bewusst nicht mehr vor der Abgabe
- Kapitel 9/10 (Shader/VFX) von Screenshots auf erklärenden Text umbauen
- `namespace`-Umbau über die 83 Dateien
- `ObjectPlacer.PlaceType` zerlegen — die Methode ist das Messobjekt der
  Threading-Abgabe, ein Umbau entwertet die Messreihe
- Schafe schlagbar machen (war ROADMAP 1a): Feature, kein Bewertungspunkt
- Member-Reihenfolge im `TerrainToolPresenter` sortieren — die Regel steht
  seit 2026-08-16 in CODE_GUIDELINES („Member-Reihenfolge"), das Sortieren
  selbst ist vor der Abgabe trotzdem nicht mehr nötig

### Kollision und NavMesh (Isor, 2026-08-16)
**Erledigt am 2026-08-19/20:** Bäume tragen `CapsuleCollider` und
`NavMeshObstacle` mit Carve, die Häuser hatten schon auf jedem Child einen
Collider. Die unten befürchteten Kosten traten nicht ein — Isor hat es im
Spiel gemessen. Offen bleibt nur die Frage für später, ob Carving bei
langsameren Rechnern nach dem Ladescreen als Hänger auftritt; Gegenmittel
wäre `Carve` aus oder ein Bake mit Navigation-Static-Bäumen.
Ursprüngliche Notiz:
- [x] **Schafe laufen durch Häuser und Bäume.** Es fehlen Collider, und die
  platzierten Bäume sind für das NavMesh unsichtbar. Zu klären: Collider an
  die betroffenen Prefabs, und wie die zur Laufzeit platzierten Objekte ins
  NavMesh kommen — jeder Baum als `NavMeshObstacle` wäre bei mehreren tausend
  Bäumen zu teuer, also eher NavMesh-Carving über die Platzierungsdaten oder
  ein Bake nach dem Placement. Hängt an der Frage, wie viel Welt zur Laufzeit
  entsteht (ROADMAP-Punkt 1) und braucht eine eigene Design-Session.
  Am Abgabetag bewusst nicht angefasst.

### Aus dem ersten Abgabe-Build (2026-08-16)
Der Build lief mit **null Fehlern** durch (77 s). Offen blieben Warnungen:
- [ ] **Neun Shader-Warnungen** im `GrassMesh_Shader`: `pow(f, e) will not work
  for negative f, use abs(f)`. Der Shader funktioniert; ein Eingriff im Shader
  Graph war am Abgabetag unnötiges Risiko. Fix: `abs()` vor die Potenz.
- [ ] **Eine `CS0414`-Warnung** bleibt: `SheepDodgeBehaviour._hasDrawPoint`
  wird in `OnDisable`, `Update` und `StartDodgeMovement` gesetzt, aber nur in
  `OnDrawGizmos` gelesen. Kapseln hieße fünf `#if`-Klammern in der
  Ablauflogik — beim nächsten Anfassen der Klasse sauber lösen, etwa indem
  der Zeichenzustand aus dem Agent abgeleitet statt mitgeführt wird.
  Die anderen sieben Gizmo-Felder wurden am 16.08. gekapselt.

## 2026-08-25 — ROADMAP-Punkt „Akademische Texte gegen den Harvard-Leitfaden prüfen"

**Abgelöst durch:** Isors Entscheidung vom 2026-08-25: Das Portfolio ist
seit dem 2026-08-21 final abgegeben, ein rückwirkendes Gegenlesen ändert
die Abgabe nicht mehr. Verlangt die Benotung eine Nachbesserung, wird
die Aufgabe neu geplant — dieser Eintrag ist dann die Vorlage.
**Warum hier:** Der Punkt war Abgabe-Vorbereitung; sein Anlass ist mit
dem Upload entfallen. Er ist überholt, nicht erledigt.

Originaltext, unverändert:

- [ ] **Akademische Texte gegen den Harvard-Leitfaden prüfen.** Maßstab
  ist `01_Uni\_Regelwerk\Leitfaden_Harvard_Zitation.md`. Konkret:
  Kurzbelege und Quellenverzeichnis im TDD gegenlesen und die noch
  fehlende Quelle ergänzen. Gehört zur Teilabgabe „Arbeiten nach
  akademischen Standards" (4FSC0PD004.1). Übernommen aus dem README des
  Datenbaums (2026-08-22) — eine Studiums-Aufgabe, die dort nur lag,
  weil der Leitfaden im Datenbaum liegt.
