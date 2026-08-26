# Welt.md — Entscheidungen Welt, Szene und Interaktion

Ownership: Nur Entscheidungen zu Welt, Szene und Interaktion — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Nicht hier: alles, was das Terrain-Tool erzeugt — Gelände, Wasserspiegel,
Weltbegrenzung (`Terrain_Mesh.md`) —, die Darstellung von Weltzuständen
im HUD (`UI.md`) und der Szenenwechsel über ein Portal, sobald mehrere
Spieler beteiligt sind (`Multiplayer.md`).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

Gilt eine Begründung weiter und ist nur ihre Ausführung überholt, bleibt
der Eintrag stehen und bekommt eine Zeile **Fortgeführt am `<Datum>`**
mit Zeiger auf die geltende Fassung — dann geht die Herleitung nicht ins
Archiv verloren.



## 2026-07-30 — Abgabe-Szene, Spielbar-Definition, Village als eigenes Prefab
Was: `Village.unity` (die generierte Szene) ist die Abgabe-Szene;
`Scene_StartEntry_Village` wird nur noch Fundgrube (VFX, Global Volume,
HerdManager). „Spielbar" heißt für die Abgabe: Menü → Village → laufen →
bevölkerte Welt → einige Dinge reagieren → Pause/Quit, Konsole fehlerfrei —
kein Kampf, keine Quests. Alles Handgebaute im Dorf wird **ein** `Village`-
Prefab, das neben dem Tool-Ast in der Szene liegt.
Warum: Die generierte Szene zeigt Tool und Pipeline im echten Einsatz — das
ist der benotete Teil; die alte Szene aufzuwerten hieße, das generierte
Terrain gegen handgebautes zu tauschen (Doppelarbeit). Kampf steht in keinem
Feedbackelement beider Aufgaben. Ein Prefab ist eine Wahrheit, überlebt Szene
und Terrain-Rebuild, erlaubt verschachtelte Haus-Prefabs und Varianten
(„Village klein" für die Abgabe) und trifft die GDD-Trennung „festes Dorf,
prozedurale Bepflanzung darauf".
Verworfen: alte Szene als Abgabe; beide Szenen pflegen (zwei NavMesh-Bakes,
zwei Bug-Quellen); volle Gameplay-Schleife; reine Tech-Demo ohne Player
(verschenkt Lernziel S3); Dorf als lose Objektsammlung in der Szene.

## 2026-07-30 — Hierarchie-Vertrag: generierter Ast gegen handgebauten Ast
Was: Was unter „Generated …" liegt, gehört dem Tool und ist jederzeit
wegwerfbar; Handgesetztes liegt **daneben, nie darunter**. Szenen-Wurzeln:
`Generated Terrain` (Tool), `Village` (Prefab), `Navigation`, `Player`, `Game`.
Warum: `TerrainToolPresenter` sucht den Terrain-Root, löscht ihn per
`DestroyImmediate` und legt ihn neu an (Zeile 74–79) — bewusst so, damit
veraltete Platzierung automatisch verschwindet. Genau deshalb löscht ein
einziger Generate-Klick alles, was versehentlich darunter liegt.
Verworfen: Häuser/NPCs unter dem Terrain-Root; Aufräumen statt Neuanlegen im
Presenter (der Rebuild ist gewollt, siehe DECISIONS 2026-07-19).

## 2026-07-30 — NavMeshSurface raus aus dem generierten Ast
Was: Der `NavMeshSurface` zieht von „Generated Terrain" auf ein eigenes
Szenen-Objekt `Navigation` (kein Prefab). Reihenfolge festgezurrt:
Weltgröße/Verteilung final → NavMesh backen → NPCs setzen.
Warum: Fund dieser Session — der Surface sitzt heute auf genau dem Objekt,
das jedes Generate zerstört; danach ist die gebackene NavMesh an niemanden
mehr angeschlossen und jeder `NavMeshAgent` steht auf nichts, ohne Fehler in
der Konsole. Backen ist zudem teuer und skaliert quadratisch: bei Voxelgröße
0,1667 m sind es auf 2048 m Kante ~151 Mio Voxelspalten, auf 512 m nur
~9,4 Mio (16×) — jede spätere Terrain-Änderung wirft die Bake weg. Ins
Village-Prefab kann der Surface nicht, weil der begehbare Boden (das
generierte Terrain) außerhalb des Prefabs liegt.
Verworfen: Surface im Village-Prefab; NPCs vor der finalen Weltgröße setzen;
NavMesh-Bake nach jedem Generate automatisch mitlaufen lassen (Minuten pro
Klick beim Tunen).

## 2026-07-30 — NPC-Platzierung: die Ortsbindung entscheidet, nicht die Gattung
Was: Was an einem **bestimmten** Ort stehen muss (Herde beim Dorf, später
Händler), wird von Hand ins Village-Prefab gesetzt. Was nur **irgendwo
passend** stehen muss (Goblins im Umland), streut der ObjectPlacer als
`Placeable`-Zeile. Für NPC-Placeables gilt: `alignToGround` aus, Scale fix
(1,0), sonst kippen und stauchen sie wie Deko.
Warum: Lernziel S3 der PCG-Aufgabe verlangt ausdrücklich eine „generierte
Bevölkerung"; der Placer ist prefab-blind, ein Goblin kostet ihn keine Zeile
neuen Code. Handgesetzt bleibt, was Komposition braucht — dafür ist ein
Zufallsstreuer das falsche Werkzeug. Ein Kriterium („muss es dort stehen?")
statt zweier Gewohnheiten hält die Grenze überprüfbar.
Verworfen: alles per Placer (Dorfbild dem Zufall überlassen); alles von Hand
(S3 ungenutzt); Trennung nach Gattung (Schafe hier, Goblins dort).

## 2026-07-30 — Erster Baustein: Interaktion anschließen, Fackel als zwei Klassen
Was: Nächster Baustein ist nicht das Dorf, sondern das Interaktionssystem in
Betrieb nehmen: Layer `Interactable` anlegen, `PlayerInteractor` und
`InteractionPromptView` samt Prompt-UI ins Player-Prefab, dann `Torch`
(Fähigkeit: `IsLit`, schaltet VFX und Light) + `TorchInteractable` (Adapter,
liefert den Prompt und leitet weiter), danach die Schafe.
Warum: `IInteractable`, `PlayerInteractor`, `InteractionPromptView` und
`SheepInteractable` existieren seit 27.07., sind aber **nirgends verdrahtet** —
die Script-GUIDs kommen weder im Player-Prefab noch in `Village.unity` vor.
Es fehlt kein Code, sondern der Anschluss. Zwei Klassen für die Fackel, weil
der `DayNightCycleEventManager` sie abends schalten muss, ohne dass jemand
auf sie zielt: zwei Aufrufer für dieselbe Fähigkeit = Fähigkeit und Adapter
trennen, genau wie `Sheep` / `SheepInteractable`.
Verworfen: eine Klasse für Fackel und Interaktion zugleich; das bestehende
System zum Lernen neu schreiben (es läuft, und die Zeit bis 2026-08-21 ist
knapp — gelernt wird am neuen Stück).

## 2026-08-02 — Interaction-Prompt: statisch serialisiert, dynamisch berechnet, Interface minimal
Was: `IInteractable.InteractionPrompt` bleibt ein reiner Getter; wie ein
Implementierer den Text herstellt, ist seine Sache. Statische Prompts aus einem
serialisierten Feld (Inspector, kein Hardcoding), dynamische aus einer berechneten
Property. Die Fackel hält zwei serialisierte Texte (`_promptWhenLit`/
`_promptWhenUnlit`) und wählt live nach `IsLit`.
Warum: Ein einzelnes serialisiertes Feld kann einen zustandsabhängigen Prompt nicht
abbilden (fror den Text ein — derselbe „gespeicherter Wert veraltet"-Fehler). Das
Interface schlank zu halten erlaubt beide Wege ohne Vertrags-Aufblähung.
Verworfen: Prompt-Pflichtserialisierung im Interface (unmöglich, erzwingt statisch);
ein einzelnes serialisiertes Feld auch für dynamische Prompts.

## 2026-08-02 — TorchMode-Enum statt zwei Bools
Was: Zyklus-Kopplung + Startzustand der Fackel als ein Enum `TorchMode`
(FollowDayNight / StartLit / StartUnlit), nicht zwei unabhängige Bools.
Warum: Zwei Bools erlauben vier Kombinationen, eine widersprüchlich (folgt +
Startzustand). Das Enum macht den ungültigen Zustand undarstellbar — der
Inspector-Picker bietet nur die drei gültigen Modi. Folgt der Projekt-Linie
„falschen Wert an der Eingabe verhindern" (DECISIONS 2026-07-18) statt Runtime-Guard.
Verworfen: zwei Bools + OnValidate-Guard; reiner Runtime-Check.

## 2026-08-02 — Celestial-Rig getrennt vom Logik-Objekt; Aufräum-Funde
Was: Sonne + Mond hängen unter einem eigenen `ClestialPivot` (den `SkyController`
dreht), getrennt vom DayNightCycle-Logik-Prefab. Nebenbei behoben: freistehende
Szenen-`Main Camera` gelöscht (Player-Prefab bringt Kamera + AudioListener mit —
sonst zwei aktive Kameras/Listener), Raycast-Target am unsichtbaren HUD-Container aus.
Warum: SRP — Logik-Objekt macht Logik, Pivot ist die physische Rig; Sonne/Mond müssen
unter dem gedrehten Objekt hängen (ein Elternteil dreht sich nicht mit dem Pivot).
Deckt den Aufräumpunkt „zwei Kameras" aus DECISIONS 2026-07-30.
Verworfen: Sonne/Mond direkt unters Logik-Objekt (funktioniert, vermischt aber das
wiederverwendbare Logik-Prefab mit szenen-spezifischen Lichtern).

## 2026-08-12 — Village-Prefab nicht neu aufbauen
Was: Der geplante Neuaufbau des Village-Prefabs (Häuser, Props, NavMesh) fällt
vor der Abgabe weg. Stattdessen Ton, UI und Beleuchtung.
Warum: Der bestehende Aufbau trägt und der NavMesh-Bake ist aktuell (geprüft
2026-08-12: `Village.unity` enthält null Kamera-Komponenten, die Notiz vom
2026-08-02 war überholt). Ein umgebautes Prefab sieht man im Build nicht,
fehlender Ton hört man sofort.
Verworfen: Village-Neuaufbau am Freitag als großen Block.

## 2026-08-16 — Prefab-Aufräumen wird aufgeschoben
Was: Die Menü-Prefabs sind verschachtelt; `Apply All` an der
Szenen-Instanz schreibt alles ins äußere Prefab. Für das Hauptmenü wurde
das über den Prefab-Modus korrigiert, für `PauseMenuRoot` bewusst nicht.
Warum: Das Spiel lädt aus den Szenen, nicht aus den Vorlagen — der Build
ist korrekt. Ein Struktur-Umbau am Abgabetag ist das falsche Risiko.
Befunde stehen in PREFAB_STATUS.md, die Aufgabe in ROADMAP.md unter
„Prefab-Struktur prüfen und aufräumen“.
Verworfen: alle Prefab-Instanzen löschen und neu einsetzen (reißt die
OnClick-Zuweisungen und die GameController-Referenzen ab).

## 2026-08-20 — Vorspulen statt Zeitsprung, und ein Tag dauert 20 Minuten
Was: Gehaltene Taste `T` setzt `IngameTime.TimeScale` auf das 60-fache. Kein
Sprung per `SetHour`. Zusätzlich läuft die Uhr grundsätzlich schneller: ein
Tag dauert 20 Minuten statt 24 Stunden.
Warum: Beim Nachlesen fiel auf, dass der Tag-Nacht-Zyklus im Build praktisch
unsichtbar war. Mit `_realSecondsPerIngameSecond: 1` und 60/60/24 dauerte ein
Tag 86.400 echte Sekunden; das Spiel startet fest um 06:00, in fünf Minuten
Spielzeit drehte sich die Sonne also um 1,25 Grad. Ein System, das im TDD
steht, die Schafe steuert und im HUD als Uhr und Tagesphase angezeigt wird,
war damit nie zu sehen. Vorspulen zeigt den Übergang, ein Sprung überspringt
ihn — und gezeigt werden soll gerade das, was bewertet wird.
Richtigstellung meinerseits: Ich hatte gegen die TimeScale-Variante
eingewandt, sie beschleunige auch Physik und Animationen. Das gilt für Unitys
`Time.timeScale`; `IngameTime.TimeScale` ist der eigene Multiplikator des
Systems und rührt nichts davon an. Der Einwand war falsch.
Verworfen: fester Sprung über `SetHour` (Isors und mein erster Gedanke);
Grundgeschwindigkeit bei 24 Stunden lassen; anklickbare HUD-Schaltfläche —
im Spiel ist der Mauszeiger gesperrt (`PlayerLook.cs:58`), eine Schaltfläche
wäre nur im Pausenmenü erreichbar und dort sieht man den Sonnenlauf nicht.
Deshalb Taste plus Anzeige statt Schaltfläche.
