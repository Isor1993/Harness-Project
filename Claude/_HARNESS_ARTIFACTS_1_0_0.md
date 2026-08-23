# _HARNESS_ARTIFACTS_1_0_0.md — Bestandsaufnahme der Artifact-Seiten

Ownership: Nur die Befunde **dieses einen Durchgangs** durch die acht
Altbestand-Seiten, geprüft am 2026-08-23 gegen die veröffentlichten Seiten und
den Code von Isor's Tower. Temporär: Was überlebt, sind die Punkte in
`Kern/ROADMAP.md` und die Nachträge im `Kern/ARTIFACT_INDEX.md`, nicht diese
Liste. Danach ins Archiv.
Format: je Seite **Einschätzung** / **belegbar falsch** / **fehlend** /
**Aufwand**. Querbefunde stehen vorne und nur einmal.

**Herkunft.** Entstanden am 2026-08-23 in einer Parallel-Session (Titel
„Design", tatsächlich Typ Prüfung), während in einer anderen Session die
Harness-Prüfung lief. Sie lag zunächst im Scratchpad jener Session und wurde am
selben Tag unverändert ins Repo übernommen — sie ist eine Befundliste und
gehört nach `Kern/WORKFLOW.md` → „Prüfung" hierher, versioniert und im INDEX.
Der Inhalt unterhalb dieser Zeile ist der Originaltext.

**Was in jener Session bewusst NICHT passiert ist:**

- Keine Seite wurde veröffentlicht oder verändert.
- Nichts wurde in `ARTIFACT_INDEX.md` oder eine andere Repo-Datei geschrieben.
- Grund: Die parallel laufende Prüfung hätte überschrieben werden können.
  `ARTIFACT_INDEX.md` ist eine einzelne Datei ohne Merge — wer zuletzt
  schreibt, gewinnt still. Für parallele Sessions hat der Harness bisher keine
  Regel; die Session hat sich selbst eine gegeben (Befund, siehe
  `Kern/ROADMAP.md`).

**Prüfgrundlage.** Jede der acht Seiten wurde als veröffentlichte Fassung
abgerufen (nicht aus der Erinnerung), und die Aussagen wurden gegen den
heutigen Code in `C:\Repos Isor\Isor-Tower-ProtoTyp-2026` gehalten:

- 89 eigene Skripte im Repo (ohne TextMesh Pro), vollständig aufgelistet
- gelesen: `SheepInteractable`, `TamedSheepReference`, `SceneLoader`,
  `GameController`, `TerrainConfig`, `GrassRenderProfile`, `PlayerInputReader`,
  Ausschnitte aus `InstancedRenderer`
- echte Asset-Werte aus
  `Assets/SO_Settings/WorldGeneration/TerrainConfig_Default.asset`
  (nicht die Skript-Defaults — die weichen ab)
- Commit-Verlauf des Tower-Repos seit 04.08.2026 (V 0.0015 → V 0.0023)

---

## 1. Querbefunde — betreffen mehrere Seiten

Diese vier Punkte sind bei jeder Seite mitzunehmen und deshalb nur einmal
aufgeschrieben.

### 1.1 `FEATURE_LOG.md` existiert nicht mehr

Drei Seiten nennen in der Fußzeile `FEATURE_LOG.md` als führende Quelle:
**Grundgerüst**, **Terrain & Gras**, **Multithreading**. Diese Datei gibt es im
Harness nicht. Heute heißt sie `Projekte/Isor_Tower/LOG.md`.

Das ist ein toter Quellverweis auf drei Seiten — genau die Sorte Fehler, die
`ARTIFACT_RULES.md` mit der Fußzeilen-Pflicht verhindern will.

### 1.2 Zwei Lernstücke haben gar keine Quellenzeile

**Poisson-Disc-Sampling** und **GPU-Instancing** nennen in der Fußzeile nur den
Stand und Links auf Nachbarseiten, aber **keine führende .md-Datei**.
`ARTIFACT_RULES.md` → Pflege verlangt beides: „Fußzeile jeder Seite nennt den
Stand (Datum) und die führende .md-Datei."

### 1.3 Die Ordnerstruktur auf der Grundgerüst-Seite ist frei erfunden

Nicht ein einziger Dateipfad auf der Grundgerüst-Seite stimmt. Sie behauptet
ein Schema `Assets/Systems/<Name>/Scripts` bzw. `Assets/Entities/<Name>/Scripts`.
Tatsächlich liegt alles unter `Assets/Scripts/<Bereich>/`:

| Seite behauptet | tatsächlich |
|---|---|
| `Assets/Systems/GameFlow/Scripts/SceneLoader.cs` | `Assets/Scripts/GameFlow/SceneLoader.cs` |
| `Assets/Entities/Player/Scripts/Player.cs` | `Assets/Scripts/Player/Player.cs` |
| `Assets/Shared/Interfaces/IInteractable.cs` | `Assets/Scripts/Interfaces/IInteractable.cs` |
| `Assets/Entities/Sheep/Scripts/SheepInteractable.cs` | `Assets/Scripts/Sheep/SheepInteractable.cs` |
| `Assets/Entities/Player/Input/PlayerInputReader.cs` | `Assets/Scripts/Player/PlayerInputReader.cs` |

Auch die Schaf-Seite ist betroffen: ihre Fußzeile nennt
`Entities/Sheep/SO_Settings/TamedSheepReference.cs`, die Datei liegt in
Wahrheit unter `Assets/Prefabs/Sheep/TamedSheepReference.cs`.

Entweder war das Schema nie umgesetzt, oder es wurde später aufgegeben. So oder
so: Die Grundgerüst-Seite sagt ausdrücklich, die Pfade seien „die tatsächliche
Struktur, nicht mehr eine geplante" — und das ist falsch.

### 1.4 Farbwelt — sieben von acht Seiten sind Altbestand, aber nicht acht von acht

`ARTIFACT_RULES.md` → Gestaltung fordert eine warme dunkle Fassung ohne
Hell-Modus. Der Stand:

| Seite | Grundfarbe | Hell/Dunkel-Umschaltung? |
|---|---|---|
| Grundgerüst | `#f6f4ee` hell, Akzent grün | ja, drei Blöcke |
| Terrain & Gras | `#E6EAEF` hell, kühl blaugrau | ja |
| Nur ein Schaf zähmbar | `#F5F7F2` hell, moosgrün | ja |
| Multithreading | `#E8EBEF` hell, kühl | ja |
| Poisson-Disc | `#f3f6f5` hell, grün | ja |
| GPU-Instancing | `#F2F4EF` hell, warmgrün | ja |
| Input-Reader | `#fbfaf7` hell, warm | ja |
| **Terrain-Fallen** | **`#141916` dunkel** | **nein — im Code steht: „Fest dunkles Theme, bewusste Entscheidung, keine Light-Variante"** |

**Terrain-Fallen ist also kein Altbestand im Farbsinn.** Sie folgt der Regel
bereits, nur in einer eigenen Palette (Grün `#5fae88`) statt der Hausfarbwelt
(Grund `#17130F`, Ember `#D9762B`). Für sie ist der Umbau ein Palettentausch,
kein Neubau — deutlich billiger als bei den anderen sieben.

---

## 2. Seite für Seite

Reihenfolge: erst die drei System-Seiten, dann die fünf Lernstücke.

---

### ⚙️ System · Grundgerüst

`https://claude.ai/code/artifact/761467e7-ed2e-48a9-a237-e208526fae48`
Stand laut Seite: 06.08.2026 · Index-Fund: wurde am 07.08. erneut
veröffentlicht, also nach der letzten Prüfung.

**Einschätzung: die mit Abstand schlechteste Seite des Bestands.** Sie
beschreibt ein Spiel, das es so nicht mehr gibt.

**Belegbar falsch:**

1. **`PauseMenuController` existiert nicht.** Die Seite widmet ihm eine eigene
   Karte samt Pfad und Verhalten. Es gibt im ganzen Repo kein solches Skript.
   Die Pause-Logik sitzt komplett in `GameController` (`Pause()`, `Resume()`,
   `ReturnToMainMenu()`, `QuitGame()`, `HandlePausePressed()`).
2. **`GameController.TogglePause()` gibt es nicht.** Die Seite nennt diese
   Methode zweimal. Der echte Code hat `Pause()` / `Resume()` und einen
   privaten `HandlePausePressed()`.
3. **Die Verdrahtung ist umgedreht.** Seite: „PauseMenuController →
   `_input.PausePerformed` → `GameController.TogglePause()`". Code:
   `GameController` abonniert `PausePerformed` selbst (`OnEnable`/`OnDisable`).
4. **Alle Dateipfade falsch** — siehe Querbefund 1.3.
5. **„Options = toter Button (ok)".** Es gibt heute `GameSettings` und ein
   Options-Panel; `GameController` setzt es beim Öffnen der Pause gezielt
   zurück (History-Eintrag 15.08.).
6. **„Async + Fade: späterer Ausbau"** bei `SceneLoader`. `LoadAsync()` ist am
   19.08. gebaut worden.
7. **Der „geplante Ausbau: Ladebalken" ist fertig.** Es gibt
   `LoadingScreenController.cs`. Die Seite führt ihn noch als Zukunft.
8. **Audio: „AudioManager und SceneMusic, geplant".** Beide existieren nicht
   und wurden offenbar nie so gebaut. Stattdessen gibt es `FootstepPlayer` und
   `RandomIntervalSound`, und `SheepInteractable` hat seit 16.08. eine eigene
   `AudioSource` samt Zähm-Sound. Audio wurde also gelöst, nur anders.

**Was komplett fehlt** (existiert im Code, kommt auf der Seite nicht vor):

- Tag-Nacht-System: `DayNightCycle`, `DayNightCycleEventManager`, `SkyController`,
  `IngameTime`, `TimeFastForward`, `NightVfx`, `IDayNightListener`
- Kampf/Schaden: `Health`, `SheepHealth`, `IDamageable`, `DamageType`,
  `HealthBarDisplay`
- Gegner: `Goblin`
- Herde: `HerdManager`, dazu die komplette `SheepFSM` mit 13 Zuständen
- HUD: `TamedSheepDisplay`, `DayTimeDisplay`, `TargetStatusDisplay`,
  `InteractionPromptView`, `SelectOnHover`, `GameSettings`
- Sonstiges: `RigidbodyPusher`, `Timer`, `IResumeTargetState`

**Aufwand:** hoch. Das ist ein Neubau, kein Nachziehen. Die Seite müsste neu
gegliedert werden, weil das Spiel inzwischen mindestens drei Systeme mehr hat
als damals. Realistisch eine eigene Sitzung.

**Zu klären, bevor gebaut wird:** Bleibt „Grundgerüst" eine Seite, oder wird
daraus Grundgerüst + eine zweite Seite (Tag-Nacht / Herde / Kampf)?
`ARTIFACT_RULES.md` sagt: Eine Seite beantwortet genau eine Frage — beantwortet
sie zwei, wird sie geteilt. Nach heutigem Umfang beantwortet sie mindestens drei.

---

### ⚙️ System · Terrain & Gras

`https://claude.ai/code/artifact/14256389-ed13-4e83-9fe1-e590b96b56d4`
Stand laut Seite: 06.08.2026, Werkzeug-Abschnitt 08.08.2026

**Einschätzung: die beste der drei System-Seiten.** Alle 23 genannten Klassen
existieren noch, und alle nachprüfbaren Zahlen stimmen.

**Gegen `TerrainConfig_Default.asset` verifiziert — alles korrekt:**

| Angabe der Seite | Asset-Wert | Rechenweg |
|---|---|---|
| Terrain-Chunks 256 m, 8 × 8 | `_chunksPerEdge: 8`, `_sizeInMeters: 2048` | 2048 / 8 = 256 ✓ |
| Vertex-Gitter 2 m, 129 × 129 | `_chunkResolution: 129` | 2048 / (8 × 128) = 2 ✓ |
| Placement-Kacheln 8 × 8 = 64 | `_placementTilesPerAxis: 8` | ✓ |
| 1023 Instanzen je Batch | `MAX_INSTANCES_PER_BATCH = 1023` | ✓ |

**Eine zentrale Aussage ist überholt:**

Die Seite schreibt zu `TerrainConfig`: „Baut in `OnEnable` die Höhenkurve als
thread-sichere Tabelle." Am 20.08. kam `EnsureHeightCurveLookup()` dazu, mit
dem Kommentar: *„OnEnable of this asset is not guaranteed to run before the
OnEnable of a scene object that reads it, and the table is not serialized, so
it can still be missing at that point."*

Auf `OnEnable` allein war also gerade **kein** Verlass. Das ist keine
Kleinigkeit: Es ist ein neuer Multithreading-Fund und gehört zusätzlich ins
Lernstück Multithreading (siehe dort).

**Fehlend, aber vorhanden im Code:** `GrassInteraction` (Gras verbiegt sich zum
Spieler), `GrassLodLevel`.

**Überholte offene Punkte** im Abschnitt „Was noch offen ist":
Der Ladebalken steht dort unter „Nach Abgabe" — er ist gebaut.

**Zu prüfen, bevor der Stempel gesetzt wird:**

- `_shoreMargin: 0` im Asset. Die Seite listet ShoreMargin als Regler, und
  unter „Herde" steht „braucht Höhenband, MaxSlope und ShoreMargin". Steht auf 0.
- Die Zellgröße — siehe den Widerspruch beim GPU-Lernstück unten.
- „`SheepSense.Update` allokiert 2 KB je Frame" — nicht nachgeprüft.

**Aufwand:** mittel. Inhaltlich weitgehend tragfähig; es geht um Korrekturen an
zwei, drei Stellen plus Neubau in der Hausfarbwelt.

---

### ⚙️ System · Nur ein Schaf zähmbar

`https://claude.ai/code/artifact/12ef2f34-c7f5-4e79-9798-a60edab85c02`
Stand laut Seite: 03.08.2026, Typ-Kennzeichnung 06.08.2026

**Einschätzung: inhaltlich richtig, aber die Kernaussage ist unvollständig.**

**Belegbar falsch:**

1. **Der Ablauf hat vier Fragen, nicht drei.** Die Seite baut ihr ganzes
   Diagramm und ihren Code-Block auf drei Fragen auf. Der echte Code hat eine
   vierte dazwischen:

   ```csharp
   if (_sheep == null || !_sheep.IsAlive)   // Frage 1
       return false;
   if (_sheep.IsTamed)                      // Frage 2
       return true;
   if (_sheep.IsAsleep)                     // Frage 3  ← fehlt auf der Seite
       return false;
   return _tamedSheep == null || _tamedSheep.Current == null;   // Frage 4
   ```

   Pikant: Die Änderung steht im Datei-Header auf den **06.08.** — dem Tag, an
   dem die Seite zuletzt angefasst wurde. Sie wurde nur nicht mitgenommen. Der
   Kommentar im Code erklärt auch, warum die Reihenfolge so sein muss: Der
   frühe Ausstieg bei `IsTamed` verhindert, dass ein gezähmtes Schaf über
   Nacht im Schlaf-Check hängenbleibt.

2. **„Die FSM liest ihn an sechs Stellen"** — heute sind es **vier**:
   `FollowPlayerState`, `HerdMovingState`, `OnAlertState`, `PatrolState`.
   (Dazu drei Lesestellen in `SheepInteractable` und eine in `HerdManager`,
   aber das ist nicht die FSM.)

3. **Die Durchspiel-Tabelle (Schaf A / Schaf B)** hat keine Zeile für den
   Schlaf-Fall. Sie ist damit unvollständig, nicht falsch.

4. **Pfad in der Fußzeile falsch** — siehe Querbefund 1.3.

**Was stimmt:** Der Code-Block zu `TamedSheepReference.Current` ist **wörtlich
korrekt** — die Drei-Bedingungen-Prüfung beim Lesen steht genau so im Repo. Die
ganze Argumentation „Merkzettel statt Zähler, Validierung beim Lesen" trägt
unverändert.

**Fehlend, aber vorhanden:** Seit 16.08. hat `SheepInteractable` eine
`StatusText`-Property (Gesundheit und Hunger im Prompt) und spielt beim Zähmen
einen Ton ab. `IsCommander` und `HerdManager` sind eine neue Achse — die Seite
sagt „bei mehreren Herden passiert nichts Neues", und es gibt inzwischen einen
HerdManager. Das sollte gegengelesen werden, ob die Aussage noch trägt.

**Aufwand:** niedrig bis mittel. Der Text stimmt zu 90 %; es geht um eine
vierte Frage im Diagramm, eine Zahl, eine Tabellenzeile und den Neubau in der
Hausfarbwelt.

---

### 💡 Lernstück · Multithreading in Unity

`https://claude.ai/code/artifact/f9d2635f-431b-4f60-90fc-dca3151cd51f`
Stand laut Seite: 05.08.2026

**Einschätzung: inhaltlich unverändert gültig.** Alle Messwerte sind in sich
schlüssig und decken sich mit der Terrain-Seite (103,4 s + 13,5 s = 116,9 s
Sampling + Filter; gesamt 122,7 → 12,4 s).

**Der eine echte Nachtrag: eine fünfte Falle.**

Die Seite nennt vier Unity-Fallen (`AnimationCurve.Evaluate`, geteiltes
`System.Random`, Unitys `==` auf Assets, `transform.position`). Am 20.08. kam
eine fünfte dazu, und sie ist die interessanteste, weil sie die Lösung von
Falle 1 selbst betrifft:

> Die Lookup-Tabelle war gebaut — nur zum falschen Zeitpunkt. `OnEnable` eines
> ScriptableObjects läuft nicht garantiert vor dem `OnEnable` eines
> Szenenobjekts, das es liest. Und die Tabelle wird nicht serialisiert. Also
> konnte sie fehlen, obwohl der Code sie korrekt anlegt.
> Fix: `EnsureHeightCurveLookup()`, gerufen vom Main Thread, bevor die Config
> an Worker gereicht wird.

Das passt exakt zum Merksatz der Seite („Was sich nicht ändert, einmal auf dem
Main Thread auflösen") und schärft ihn: *einmal auflösen genügt nicht, es muss
auch nachweislich vorher passiert sein.*

**Sonst:** `FEATURE_LOG.md` in der Fußzeile (Querbefund 1.1).

**Aufwand:** niedrig. Ein neuer Abschnitt, ein präzisierter Merksatz, Neubau in
der Hausfarbwelt. Keine Zahl muss angefasst werden.

---

### 💡 Lernstück · Poisson-Disc-Sampling

`https://claude.ai/code/artifact/2a5340fb-b4de-4326-be1a-c330767d8fdb`
Stand laut Seite: 06.08.2026

**Einschätzung: die stabilste Seite des Bestands.** Reines Algorithmuswissen
(Bridson), das nicht veraltet.

**Alle Zahlen nachgerechnet — korrekt:**

- Gitterzellen `r/√2`: 5 / 1,414 = 3,54 m ✓; 2048 / 3,54 = 579 ✓
- Gras-Fall: r = 0,6 → 0,42 m Zellen; 256 m Kachel / 0,42 = 610 ✓
  (deckt sich mit dem „~610 × 610" auf der Terrain-Seite)
- Nahtlängen: 8×8 → 14 Linien × 2048 m = 28,7 km ✓; 16×16 → 61,4 km ✓;
  32×32 → 127,0 km ✓
- Messreihe 116,9 → 92,6 → 8,8 s deckt sich mit den Nachbarseiten ✓

**Zwei kleine Schwächen:**

1. **Zwei verschiedene Radien ohne Übergang.** Der Kennzahlen-Block oben rechnet
   mit r = 5 m (Bäume), Abschnitt 5 springt ohne Ansage auf r = 0,6 m (Gras).
   Beides ist richtig, aber wer den Block oben im Kopf hat, stolpert unten.
2. **Kein Beleg aus dem Projekt.** Der `ARTIFACT_INDEX` führt `ObjectPlacer` als
   Beispiel — auf der Seite kommt die Klasse gar nicht vor. Entweder Beleg
   ergänzen oder die Indexzeile korrigieren.

**Sonst:** keine Quellenzeile in der Fußzeile (Querbefund 1.2).

**Aufwand:** niedrig. Praktisch nur Farbwelt plus zwei Sätze. **Achtung:** Die
Seite trägt sechs handgebaute SVG-Diagramme (Gitter, Annulus, Nachbar-Check).
Die sind der eigentliche Wert und müssen beim Neubau mitgenommen werden — das
ist die Arbeit, nicht der Text.

---

### 💡 Lernstück · GPU-Instancing

`https://claude.ai/code/artifact/0183966d-3132-4804-af82-83591ffe5f09`
Stand laut Seite: 04.08.2026, überarbeitet 06.08.2026

**Einschätzung: inhaltlich stark, aber es gibt zwei Widersprüche nach außen.**

**Widerspruch 1 — die Zellgröße.**

| Quelle | Wert |
|---|---|
| Dieses Lernstück, hergeleitet | ideal ≈ 143 m, empfohlen **128 m** |
| System · Terrain & Gras | Gras-Zellen **≈ 36 m**, 3 139 Stück |
| `GrassRenderProfile.cs`, Skript-Default | `_cellSize = 32f` |

Der gebaute Wert ist also rund **viermal kleiner** als die Empfehlung der
eigenen Seite. Zwei mögliche Erklärungen, und ich kann sie hier nicht
entscheiden:

- Die Dichte ist seitdem stark gestiegen. Die Faustregel der Seite selbst sagt:
  „Mindestabstand halbieren → vierfache Dichte → optimale Zellenkante halbiert
  sich." Dann wäre 32 m korrekt und die 128-m-Rechnung nur veraltet.
- Oder die Empfehlung wurde nie umgesetzt.

Um das zu klären, braucht es den `_cellSize`-Wert am echten Gras-Prefab und die
heutige Büschelzahl. **Das ist die wichtigste offene Frage des ganzen Bestands**,
weil zwei Seiten sich gegenseitig widersprechen und ein Leser nicht erkennen
kann, welche recht hat.

**Widerspruch 2 — die Menge.**

| Quelle | Zahl |
|---|---|
| GPU-Instancing | 211.000 Halme (die ganze Seite rechnet damit) |
| System · Terrain & Gras | 190.000 Büschel |

Vermutlich meinen beide dasselbe zu verschiedenen Zeitpunkten, aber so
nebeneinander stehend ist es ein Fehler.

**Was verifiziert wurde und stimmt:**

- `Graphics.RenderMeshInstanced` — ja, genau so im `InstancedRenderer` ✓
- 1023 als harte Grenze ✓, samt Kommentar im Code
- 211.000 / 1023 = 207 Batches ✓; 211.000 × 64 Byte = 13,5 MB ✓

**Nicht auf der Seite, aber im Profil einstellbar:** LOD-Distanz 60 m,
Renderdistanz 250 m. Beide Werte tauchen nirgends auf einer Seite auf.

**Sonst:** keine Quellenzeile in der Fußzeile (Querbefund 1.2).

**Aufwand:** mittel. Vier große SVG-Diagramme sind mitzunehmen, und die
Zellgrößen-Frage muss vorher geklärt sein — sonst schreibt man den Widerspruch
nur in neuen Farben fort.

---

### 💡 Lernstück · Terrain-Fallen

`https://claude.ai/code/artifact/6241c560-1893-45ab-9f4f-aa71dbc01da6`
Stand laut Seite: entstanden 19.07.2026, überarbeitet 06.08.2026

**Einschätzung: die einzige Seite, die bereits dunkel gebaut ist** — mit
explizitem Kommentar im Quelltext: „Fest dunkles Theme — bewusste Entscheidung,
keine Light-Variante." Sie hat die Regel vorweggenommen, nur in eigener Palette.

**Die drei Fallen sind übertragbares Wissen und bleiben gültig:**
Plateau-Krater, AnimationCurve-Overshoot unter Null, Beleuchtungsnähte an
Chunk-Grenzen. Alle drei Fix-Träger existieren: `PlateauModifier`,
`HeightmapGenerator`, `MeshBuilder`.

**Die Tuning-Tabelle ist überholt — und sagt das selbst.** Sie trägt bereits
einen „Überholt"-Kasten, der auf Weltgröße 2048 m und HeightMultiplier 700
verweist. Beides stimmt mit dem Asset überein. Der Rest der Tabelle nicht mehr:

| Parameter | Seite (v2) | Asset heute |
|---|---|---|
| `_sizeInMeters` | 2048 | **2048** ✓ |
| `_heightMultiplier` | 700 (im Überholt-Kasten) | **700** ✓ |
| `_octaves` | 5 | **5** ✓ |
| `_noiseScale` | 600 | **461,1** ✗ |
| `_persistence` | 0,5 | **0,273** ✗ |
| `_plateauHeight` | 0,09 | **0,15** ✗ |
| Wasserspiegel (im Diagramm) | ≈ 0,05 | **0,14** ✗ |

**Eine Beobachtung nebenbei, kein Auftrag:** `TerrainConfig.OnValidate` warnt,
wenn bei aktivem Plateau der Wasserspiegel auf oder über der Plateauhöhe liegt
(„das Dorf würde absaufen"). Aktuell: Plateauhöhe 0,15, Wasser 0,14 — die
Warnung greift nicht, aber der Abstand beträgt 0,01. Falle 1 der Seite ist also
heute wieder knapp dran. Ob das Absicht ist, entscheidet Isor.

**Aufwand:** am niedrigsten von allen. Palettentausch statt Neubau, plus vier
Zahlen in der historischen Tabelle. Die drei SVGs sind vorhanden und
theme-fähig gebaut (nutzen bereits CSS-Variablen).

---

### 💡 Lernstück · Input-Reader

`https://claude.ai/code/artifact/20be8fc5-f9bf-4d49-8af5-bab3247bb6e3`
Stand laut Seite: 27.07.2026, Typ-Kennzeichnung 06.08.2026
Ältester Inhaltsstand des Bestands.

**Einschätzung: gute Seite mit einer Aussage, die der Code widerlegt.**

**Belegbar falsch:**

Die Seite schreibt zu `EnableUI()`: „Player-Map aus, nur Pause hört zu. **Beim
Disable feuert Unity `canceled` → MoveInput wird 0.**"

Der Code verlässt sich genau darauf **nicht**:

```csharp
public void EnableUI()
{
    if (_controls == null) return;
    _controls.Player.Disable();

    MoveInput = Vector2.zero;
    LookInput = Vector2.zero;
    IsFastForwarding = false;
}
```

Mit dem Kommentar: *„clears the movement values, so a key held down at the
moment of pausing cannot leak through."* Also das Gegenteil der
Seitenbehauptung — die Werte werden ausdrücklich von Hand genullt, weil auf das
`canceled` kein Verlass war.

**Unvollständig:**

1. **Die Kette zeigt nur eine Map.** Die Seite zeigt
   `_controls.Player.SetCallbacks(this)`. Der Reader implementiert **zwei**
   Interfaces (`IPlayerActions` **und** `IUIActions`) und meldet beide an.
2. **Warum die UI-Map immer läuft, fehlt.** Im Code steht der Grund als
   Kommentar: *„The UI map only carries Pause and has to stay active during
   gameplay, otherwise the game could never be paused in the first place."*
   Das ist genau die Art Einsicht, für die die Seite gemacht ist.
3. **Eine dritte Input-Sorte ist dazugekommen.** Seit 20.08. gibt es
   `IsFastForwarding` / `OnFastForward`. Die Seite kennt zwei Kategorien
   (Zustand → Property, Ereignis → Event). Der neue Fall ist Kategorie 1, nutzt
   aber eine Technik, die die Seite nicht zeigt:
   `context.ReadValueAsButton()` statt eines `performed`-Filters — eine
   gehaltene Taste, die in einem einzigen Callback Drücken und Loslassen
   abdeckt.

**Was stimmt:** Alle übrigen Code-Zeilen sind wörtlich korrekt
(`new PlayerControls()`, `SetCallbacks`, `Enable`, `ReadValue<Vector2>()`,
`if (!context.performed) return;`). Die Frame-Tabelle und die
Property-vs-Event-Begründung tragen unverändert.

**Ungeprüft:** Das `.normalized`-Rechenbeispiel („diagonal 41 % zu schnell").
Im Reader steht kein `.normalized` — das passiert vermutlich im `PlayerMotor`.
Beim Nachziehen dort nachsehen.

**Aufwand:** niedrig bis mittel. Eine falsche Aussage umdrehen, zwei Absätze
ergänzen, Farbwelt.

---

## 3. Vorgeschlagene Reihenfolge

Sortiert nach Aufwand pro gewonnener Richtigkeit — billigste und klarste zuerst.

| # | Seite | Aufwand | warum an dieser Stelle |
|---|---|---|---|
| 1 | Terrain-Fallen | klein | schon dunkel; nur Palette + vier Zahlen. Guter Testlauf für die Hausfarbwelt an einer Seite, die kaum Risiko trägt |
| 2 | Multithreading | klein | ein Nachtrag (fünfte Falle), keine Zahl wackelt |
| 3 | Input-Reader | klein–mittel | eine klar belegte Falschaussage, sonst gesund |
| 4 | Nur ein Schaf zähmbar | klein–mittel | vierte Frage ins Diagramm, eine Zahl, eine Tabellenzeile |
| 5 | Poisson-Disc | mittel | inhaltlich fast fertig, aber sechs SVGs sind zu übertragen |
| 6 | GPU-Instancing | mittel | **erst wenn die Zellgrößen-Frage geklärt ist** |
| 7 | Terrain & Gras | mittel | hängt an derselben Zellgrößen-Frage; sinnvoll direkt nach 6 |
| 8 | Grundgerüst | groß | Neubau, und vorher die Grundsatzfrage: eine Seite oder zwei? |

Zwei Abhängigkeiten sind zu beachten:

- **6 und 7 gehören zusammen.** Sie widersprechen sich heute; wer nur eine
  anfasst, macht den Widerspruch schlimmer.
- **8 braucht vorher eine Entscheidung von Isor**, keine Bauarbeit.

---

## 4. Was Isor entscheiden muss

Vier Punkte, die ich nicht selbst entscheiden kann oder darf:

1. **Wird „Grundgerüst" geteilt?** Nach heutigem Umfang beantwortet die Seite
   mindestens drei Fragen (Spielablauf, Tag-Nacht, Herde/Kampf). Die Regel sagt:
   dann teilen. Teilen heißt: neue URL, neuer Indexeintrag.
2. **Welche Zellgröße gilt?** 32 m (Skript-Default), ~36 m (Terrain-Seite) oder
   128 m (GPU-Lernstück)? Dafür braucht es einen Blick ins Gras-Prefab.
3. **Plateauhöhe 0,15 vs. Wasser 0,14** — Absicht oder Zufall? Betrifft den
   Code, nicht die Seite; fiel nur bei der Prüfung auf.
4. **Wann die Nachträge in `ARTIFACT_INDEX.md` gehen.** Vorschlag: gesammelt,
   erst wenn in der anderen Session Ruhe ist.

## 5. Was diese Bestandsaufnahme nicht abdeckt

Der Vollständigkeit halber, damit niemand mehr hineinliest, als drinsteht:

- **Nicht geprüft:** die drei Seiten außerhalb des Altbestands
  (📍 Status, ⚙️ System · Harness, die Zeugnisse, Menü-Politur).
  Status und Harness wurden heute in der anderen Session angefasst.
- **Nicht geprüft:** Prefab- und Szenen-Inhalte. Alle Aussagen über
  Inspector-Werte stammen aus `TerrainConfig_Default.asset`; das Gras-Prefab
  und die Szenen wurden nicht geöffnet.
- **Nicht geprüft:** ob die Knowledge-Notizen, die auf diese Seiten zeigen
  (`Seite ←` im Index), noch stimmen.
- **Nicht gezählt:** wie viele Grasbüschel heute tatsächlich platziert werden.
