# DECISIONS.md — Entscheidungen Game Jam Semester 3

Ownership: Nur Entscheidungen zu Isors Teil am Game Jam Semester 3
(Team-Projekt, 08.–15.10.2026) — was entschieden wurde, warum, und
welche Alternativen verworfen wurden. Kein Plan (das ist die ROADMAP
dieser Schicht), kein Ereignis (das ist das LOG). Die Jam-Termine
besitzt `Uni/Semester_3/STUNDENPLAN.md`; dass der Jam ein unbenotetes
Abhak-Kriterium ist, steht in `Uni/DECISIONS.md` → „2026-10-01 —
Bewertungslage Semester 3".
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.
Überholte Einträge wandern ins Archiv der Schicht (wird beim ersten
Fall angelegt), mit Angabe, wodurch sie abgelöst wurden.

## 2026-10-10 — Eigene Schicht, Team-Repo, Lernmodus

Was: Isors Jam-Anteil bekommt die Schicht `Projekte/GameJam_S3_2026/`;
der Code liegt im Team-Repo (Marke `PROJEKT_GAMEJAM` in `Kern/PFADE.md`),
an dem drei Programmierer arbeiten. Isors Karten: Interface,
Color Bucket, Portal, Scene Change, Enemy-KI. Gearbeitet wird im
**Lernmodus** — Isor entwirft und tippt, Claude gibt Gerüst und Review.
Warum: Der Jam ist zwar unbenotet, aber C#/Unity-Praxis für ein
mögliches Unity-Semesterprojekt; Isor wählte den Lernmodus selbst.
Verworfen: Normal-Modus mit Claude als Schreiber (schneller, aber ohne
Übung) · gemischt nach Baustein.

## 2026-10-10 — IInteractable: drei Methoden, Aufrufer als GameObject

Was: Das Interface trägt `CanInteract()`, `InteractionPrompt()` und
`Interact(GameObject interactor)`. Der Parameter ist der Aufrufer
(meist der Spieler), nicht das Objekt selbst.
Warum: `CanInteract` lässt Objekte selbst sagen, wann sie gesperrt sind
(Portal vor dem Gegner-Tod). Den Prompt-Text will das Team in der UI
zeigen. `GameObject` statt eines Player-Typs hält das Interface frei vom
Player-Skript des anderen Programmierers.
Verworfen: `InteractionPrompt` weglassen (UI-Text ist geplant).

## 2026-10-10 — Farbeimer ohne Farbe, Anmalen als Sprite-Tausch am Objekt

Was: Alle Eimer sind gleich — einer ist **eine Ladung Farbe**; der
Spieler hat nur eine Anzahl. Anmalen heißt: Das Objekt tauscht seine
Skizzen-Sprite gegen die bunte. Dafür kommt ein allgemeines Skript an
jedes anmalbare Objekt (Arbeitsname `Paintable`); es kennt beide
Sprites, der Spieler kennt nur seine Eimerzahl. Der Eimer erreicht das
Inventar später über `interactor`, nicht über ein Inspector-Feld.
Warum: Wer die bunte Sprite kennen muss, dem gehört der Tausch (Isors
Herleitung). Ein Inspector-Feld auf den Spieler ginge bei Prefabs nicht
und müsste je Eimer verdrahtet werden.
Verworfen: Farben je Eimer (das Spiel tauscht nur Sprites) · Anmalen
im Player-Skript.
Offen: `CanInteract()` hat keinen Parameter — ein `Paintable` kann darin
die Eimer des Spielers nicht prüfen. Lösung entwirft Isor, wenn
`Paintable` dran ist. Ob `Paintable` zu Isors Karte gehört, klärt das
Team.
**Fortgeführt am 2026-10-11:** Die offene Frage ist gelöst — siehe
„2026-10-11 — Paintable: Überblenden, Spieler per Tag". `Paintable`
hat Isor selbst gebaut.

## 2026-10-10 — Eine Szene als Filmstreifen, Portalpaar je Gegner

Was: Beide Welten liegen in **einer** Szene übereinander, mit festem
Abstand. Ein sterbender Gegner spawnt **zwei** Portale — an seiner
Position und an derselben Stelle um den Weltabstand versetzt — und gibt
jedem per `Init` die **Position** des anderen. Jedes Portal zerstört
sich nach dem Benutzen, nur das benutzte. Der Weltabstand ist ein Feld
am Gegner.
Warum: Eine Szene heißt, beim Weltwechsel nichts zwischenspeichern
(Team-Entscheid, für eine Jam passend). Position statt Partner-Portal,
weil das benutzte Portal sich zerstört und eine Referenz dann ins Leere
zeigte. `Init` statt Inspector-Feld, weil ein Prefab keine
Szenen-Objekte halten kann.
Verworfen: Zielpunkt-Objekt in der Szene (für gespawnte Portale nicht
erreichbar) · fester Versatz im Portal-Prefab (Vorzeichen je Portal
verschieden) · versteckt vorplatziertes Portal (Isor will das Portal
dort, wo der Gegner stirbt).

## 2026-10-10 — Gegner: IDamageable, Patrol ab Spawnpunkt, Raycast

Was: `IDamageable` mit `TakeDamage(int damage)`. Patrol als **eine
Strecke ab dem Spawnpunkt** (Gizmo zeigt sie), Umdrehen bei „erreicht
oder überschritten". Sicht per Raycast in Laufrichtung, gefiltert auf
den Layer Player; Attack läuft schneller auf den Spieler zu, ohne Sicht
zurück in Patrol. Kontaktschaden einmal pro Berührung, nur am Tag
Player. J5a hat Isor getippt, J5b/J5c (Bewegung) hat Claude auf Isors
Wunsch geschrieben (Erkältung).
Warum: Isors Entwurf. Eine Strecke wandert mit, wenn der Gegner im
Editor verschoben wird; ein Raycast filtert nur nach Layer, nicht nach
Tag.
Verworfen: Endposition als Weltkoordinate · Kontaktschaden in beide
Richtungen (jeder Zusammenstoß tötete den Gegner) — wie der Spieler
trifft (Taste oder Draufspringen), entscheidet der Player-Programmierer.

## 2026-10-11 — Alles mit Physik bekommt 2D-Komponenten

Was: Spieler und Gegner kommen als 3D-Modelle, Boden und Umgebung als
2D-Sprites (Isors Abfrage beim Art-Team). Physik läuft trotzdem überall
über `Rigidbody2D`/`Collider2D`. Layer Player (6) und Enemy (7) und
das Paket *2D Sprite* sind angelegt und gepusht. Empfohlen: Modell als
Kind-Objekt, Physik am Eltern-Objekt.
Warum: 2D- und 3D-Physik sehen sich nicht — der Gegner-Code
(`Physics2D.Raycast`, `OnCollisionEnter2D`) erreicht nur 2D-Collider.
Passt zum gewünschten „2D-Feeling".
Verworfen: 3D-Physik mit gesperrter Z-Achse.

## 2026-10-11 — SceneLoader: zwei Szenen, Lade-Panel optional

Was: Menü- und Spielszene, je Szene ein `SceneLoader` mit
`LoadGameScene` und `LoadMenuScene` über einen gemeinsamen Helfer,
geladen **async**. Das Lade-Panel ist nur im Menü zugewiesen — die
Null-Prüfung ersetzt jede Sonderregel für den Rückweg. `Menu` ist
Szene 0. Die Optik baut der dritte Programmierer.
Warum: Jam-einfach; synchron geladen würde das Panel nie gezeichnet.
Verworfen: eigene Lade-Szene · Menü-Sonderregel im Code.

## 2026-10-11 — Paintable: Überblenden, Spieler per Tag

Was: Die bunte Sprite liegt als Kind-SpriteRenderer über der Skizze,
startet unsichtbar und blendet über eine einstellbare Dauer ein. Das
Paintable sucht den Spieler in `Awake` per Tag; Eimer-Prüfung in
`CanInteract` und Abzug in `Interact` folgen als TODO, sobald das
Inventar steht. `IInteractable` bleibt unverändert.
Warum: Isors Idee — kennt das Objekt den Spieler, kann `CanInteract`
das Inventar selbst prüfen, ohne Interface-Änderung. Tag statt
Inspector-Feld, weil sonst jedes Objekt von Hand verdrahtet würde.
Verworfen: `CanInteract(GameObject interactor)` (zöge `InteractionPrompt`
und drei Skripte nach) · Prüfung nur in `Interact` (Prompt auch ohne
Eimer) · Sofort-Tausch und Drübermalen per Maske.

## 2026-10-11 — Lokale Sandbox im Team-Repo

Was: `Assets/Scripts/Sandbox_Eric/` mit Test-Spieler, Test-Kamera,
Test-Sprites und Testszene, ausgeschlossen über `.git/info/exclude` —
nicht über die Team-`.gitignore`. Bleibt bestehen (Isor, 2026-10-11).
Warum: Testen, bevor der echte Player existiert, ohne dem Team Dateien
oder fehlende Skripte unterzuschieben.
Verworfen: Test in `DEV_Eric` (würde gepusht und verwiese auf Skripte,
die beim Team fehlen).

## 2026-10-15 — Abgabetext folgt Isors Bericht, Ablage im Harness

Was: Der Reflexionstext für die Game-Jam-Review entsteht aus Isors
mündlichem Bericht; Schicht-Doku und Team-Repo liefern nur Zahlen und
Belege dazu. Er liegt als `ABGABE_REFLEXION.txt` in dieser Schicht,
nicht im Team-Repo.
Warum: Der Text enthält Isors Urteil über Teamarbeit und Personen, das
kann nur er liefern. Im Team-Repo läge der Abschnitt „Was besser werden
muss" offen beim Team.
Verworfen: Text aus der Schicht-Doku bauen und von Isor gegenlesen
lassen (kostete am 2026-10-15 drei Korrekturrunden — `Kern/STOERUNGEN.md`)
· Ablage in `GameJam_S3_2026\Docs\` neben den Discord-Texten.
