# DECISIONS.md — Entscheidungen Entities und KI

Ownership: Nur Entscheidungen zu Entities und KI — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

## 2026-08-02 — Herde als platzierbares Prefab: Injektion statt Szenen-Referenzen
Was: `HerdManager.Awake` injiziert sich selbst und den Graveyard-Marker per
`Sheep.Init(herd, graveyard)` in alle Pool-Mitglieder; die Schafe halten keine
serialisierten Referenzen auf HerdManager oder Graveyard mehr. Der Graveyard ist
ein eigener Marker im Prefab jeder Herde, kein geteiltes Szenen-Objekt.
Warum: Die Herde soll wie das Village ein platzierbares Prefab sein —
serialisierte Referenzen auf Szenen-Objekte überleben das Instanziieren nicht.
Ein geteilter Graveyard hätte genau die Szenen-Abhängigkeit zurückgebracht, die
das Prefab vermeiden soll; die geteilte Variante bräuchte ein
`RuntimeReference<T>`-SO (Werkzeug-Kriterium „Service über Szenengrenze").
Verworfen: geteilter Graveyard für alle Herden; Szenen-Verdrahtung von
HerdManager und Graveyard an jedem einzelnen Schaf.
## 2026-08-02 — Commander als Herdenführer, RVO-Priorität nach Rolle
Was: Nur das Zähmen des Commanders löst `SetAllSheepHerdMoving(true)` aus —
ein gezähmtes Normal-Schaf folgt dem Spieler allein, ohne die Herde in Bewegung
zu setzen. Der Commander bekommt `avoidancePriority = 0`, Normal-Schafe
`Random.Range(30, 70)`.
Warum: Die Herde braucht einen Anker, der sich nicht wegschieben lässt — in
Unitys RVO gewinnt die niedrigere Zahl. Gestreute Prioritäten für die
Normal-Schafe verhindern, dass zwei gleichrangige sich gegenseitig blockieren.
Ein einzelner Herdenführer macht das Zähmen zur Entscheidung statt zur
Sammelaktion.
Verworfen: jedes gezähmte Schaf startet die Herdenbewegung (die Herde wäre nicht
mehr gezielt steuerbar); gleiche Priorität für alle (Deadlocks zwischen Schafen).
## 2026-08-02 — Dodge nur im Patrol, Tie-Break per EntityId
Was: `TryEnterDodge` wird nur noch aus `PatrolState` gerufen (aus Regroup,
HerdMoving und FollowPlayer entfernt). Treffen zwei Schafe aufeinander, weicht
nur das mit der höheren `EntityId` aus; dazu ein Cooldown nach jedem Dodge und
ein `HasReachedDestination`-Guard. `SheepFSM.ChangeState(SheepStateBase)` ist
public, `DodgeState` kehrt über den gemerkten `_returnState` zurück statt über
einen Typ-Switch.
Warum: Ohne Tie-Break weichen beide Schafe gleichzeitig aus und spiegeln sich
endlos. Schaf-gegen-Schaf löst Unitys RVO ohnehin schon; der eigene Dodge ist
für feste Hindernisse da und stört in Formation mehr, als er hilft. Die
generische Rückkehr macht `DodgeState` unabhängig davon, welche States es gibt —
ein neuer Bewegungs-State braucht dort keine Änderung.
Verworfen: Dodge in allen Bewegungs-States; Typ-Switch in `DodgeState`; elegante
Crowd-Avoidance jetzt bauen (vorgemerkt für nach der Abgabe).
## 2026-08-03 — Nur ein gezähmtes Schaf, gemerkt in einem SO-Asset
Was: Der Spieler kann projektweit nur ein Schaf zugleich führen.
`TamedSheepReference` (ScriptableObject in `Entities/Sheep/SO_Settings/`) hält den
Zeiger auf das gezähmte Schaf; `SheepInteractable.CanInteract` verweigert das
Zähmen, solange der Zeiger belegt ist — ein bereits gezähmtes Schaf lässt sich
dagegen immer freilassen. Der Zeiger wird beim Lesen validiert
(`!= null && IsAlive && IsTamed`) statt von außen aufgeräumt.
Warum: Die Herdenformation ist um einen Anker gebaut, zwei folgende Schafe
streiten sich um dieselben Slots — die Sperre verhindert den Fehler, statt ihn
später zu reparieren. Vom Spielgefühl gehört „mein Schaf" zum Spieler, technisch
geht das nicht: Schafe sind Prefabs und können keine Szenen-Referenz halten, und
`IInteractable.CanInteract` bekommt den Interactor nicht — eine rein
spielerseitige Regel hätte den Tastendruck blockiert und den Prompt trotzdem
stehen gelassen. Auf ein Asset darf ein Prefab zeigen. Die Prüfung beim Lesen
macht einen Zähler überflüssig, der bei Zähmen, Freilassen, Tod und Respawn
mitgepflegt werden müsste; der Merkzettel bleibt ein Zeiger auf `Sheep._isTamed`,
keine zweite Wahrheit.
Verworfen: Zähler im HerdManager (vier Pflegepfade, bei einem vergessenen still
falsch); Regel pro Herde (heute identisch, bräche still bei der zweiten Herde);
`CanInteract` um den Interactor erweitern (änderte den Vertrag für alle
Implementierer, gegen DECISIONS 2026-08-02 „Interface minimal").
## 2026-08-06 — Zähmen wirkt sofort, schlafende Schafe sind nicht zähmbar
Was: `Sheep.ToggleTame()` schaltet das Flag um und erzwingt beim Zähmen den
Wechsel in `FollowPlayerState`; das Freilassen bleibt ungezwungen.
`SheepInteractable.CanInteract` liefert für ein schlafendes, ungezähmtes Schaf
`false` — der Interactor verwirft das Ziel, der Prompt erscheint gar nicht.
Dreht die Absicht vom 27.07.2026 um, den Zeitpunkt bewusst der FSM zu überlassen.
Warum: Nur `PatrolState` und `OnAlertState` prüfen das Tame-Flag von sich aus;
`Eating`, `Sleeping`, `Idle`, `Regroup`, `HerdMoving` und `Dodge` gar nicht. Ein
fressendes Schaf reagierte erst beim Sattwerden, ein patrouillierendes erst am
Wegpunkt, und in `OnAlert` kam die Reaktionszeit obendrauf — der Spieler wartete
auf seinen eigenen Tastendruck. Das Freilassen braucht keinen Zwang, weil
`FollowPlayerState.Tick()` `!IsTamed` ohnehin je Frame prüft; damit bleibt die
ziehende FSM erhalten und nur der Eintritt wird gedrückt.
Tragend ist die Reihenfolge in `CanInteract`: Die Schlafprüfung steht **hinter**
dem `IsTamed`-Early-Return. Das Schlaf-Flag folgt der Tageszeit, nicht dem
Zustand des Schafs — stünde die Prüfung davor, hinge ein gezähmtes Schaf bei
Einbruch der Nacht bis zum Morgen am Spieler fest.
Verworfen (Zähmen): Zähmen weckt ein schlafendes Schaf (berührte `_isSleeping`,
`SleepingState` und die Hunger-Pause — drei Stellen für einen seltenen Fall);
jedem State eine eigene Tame-Prüfung geben (verteilt dieselbe Logik auf sechs
Dateien und muss bei jedem neuen State mitgepflegt werden); zusätzliche
`IsCurrentState<DeadState>()`-Absicherung (`IsAlive` fängt es bereits zweifach
ab, in `CanInteract` und in `ToggleTame`).
## 2026-08-16 — `Health` als Komponente statt Basisklasse
Was: Neue allgemeine `Health`-Komponente unter `Shared/Health/Scripts/`,
die an jedes Wesen gehängt wird. `SheepHealth` bleibt unangetastet.
Warum: Komposition statt Vererbung — der Goblin bekommt sein Leben später
ohne eine Zeile neuen Code (Isor). `SheepHealth` blieb, weil es im TDD
beschrieben ist; ein Umbau hätte den Abgabetext falsch gemacht.
Verworfen: eine gemeinsame Basisklasse, von der beide erben (mein
Vorschlag — Komposition ist in Unity der übliche Weg); `PlayerHealth` als
eigene Klasse (hätte den Namen an den Spieler gebunden).
Nebenbefund: Der Merker `_hasDied` aus `SheepHealth` wurde weggelassen. Der
Guard `if (!IsAlive) return;` verhindert bereits, dass ein Toter nochmal
Schaden nimmt — damit kann `OnDied` nicht doppelt feuern.
## 2026-08-20 — Ball als Bedrohungs-Attrappe statt Gegner
Was: Ein roter Ball auf Layer `Enemy` mit Rigidbody, anschiebbar durch den
Spieler über die neue `RigidbodyPusher`-Komponente.
Warum: Das Fluchtverhalten der Schafe ist gebaut und bewertet, aber ohne
Gegner im Spiel nicht vorführbar. Der Ball löst es aus, ohne dass am
Abgabetag eine Gegner-KI entstehen muss. Technisch nötig war die Komponente,
weil ein `CharacterController` beim Bewegen keinen Impuls an Rigidbodies
weitergibt — Unity macht das absichtlich nicht von selbst.
Nebenbefund, korrigiert: Isor hatte dem Spieler zusätzlich einen `Rigidbody`
gegeben. Zusammen mit dem `CharacterController` steuern beide die Position
und arbeiten gegeneinander; der Rigidbody kam wieder herunter.
Verworfen: Gegner-KI bauen (kein Zeitrahmen); Spieler auf Rigidbody-Bewegung
umstellen (Umbau am bewerteten Bewegungssystem).
