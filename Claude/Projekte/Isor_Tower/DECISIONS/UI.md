# UI.md — Entscheidungen UI, Menüs und HUD

Ownership: Nur Entscheidungen zu UI, Menüs und HUD — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.


## 2026-08-02 — Pause-Menü-Navigation: Hover setzt Selection, Startauswahl im Controller
Was: Maus-Hover setzt die EventSystem-Selection (`SelectOnHover`, `Shared/UI/`),
damit Maus und Tastatur einen Zustand teilen; die Startauswahl beim Öffnen setzt
`GameController.Pause()` per Code. Voller Maus/Tastatur-Moduswechsel (Cursor +
Highlight je Gerät) = Polish.
Warum: Hover-Highlight und Selection sind getrennte Zustände, die auseinanderdriften;
ein Leer-Klick löscht die Selection. Das Inspector-Feld „First Selected" wirkt nur
beim Szenenstart, nicht bei später aktiviertem Menü — die Startauswahl gehört dem
Menü-Besitzer und muss beim Öffnen per Code gesetzt werden. `SelectOnHover` als
eigenes Shared-UI-Script, weil Hover-Verhalten pro Element in Unity auf dem Element
wohnt (kein Smell).
Verworfen: klebrige Re-Selection im GameController-Update als Hauptlösung
(Hover-Sync ist sauberer); Voll-Moduswechsel jetzt (Aufwand → Polish).

## 2026-08-14 — Einstellungen über PlayerPrefs statt Singleton
Was: `GameSettings` liegt in jeder Szene einmal auf einem aktiven Objekt und
liest beim Start aus `PlayerPrefs`. Kein `DontDestroyOnLoad`.
Warum: Nicht das Objekt muss den Szenenwechsel überleben, sondern die Daten —
und die liegen ohnehin auf der Platte. Der `AudioMixer` ist ein Asset und
existiert über beide Szenen hinweg; ihm muss je Szene nur einmal gesagt
werden, was gilt. Deckt sich mit dem Singleton-Verbot in CODE_GUIDELINES.
Verworfen: Singleton mit DontDestroyOnLoad; Einstellungen als
ScriptableObject halten (überlebt den Programmstart nicht).

## 2026-08-14 — Gespeichert wird die Empfindlichkeit, nicht die Reglerstellung
Was: Unter `MouseSensitivity` liegt der fertige Wert (0,02 bis 0,18), nicht
die Sliderposition 0–1. Die Reglerstellung wird beim Öffnen per
`InverseLerp` zurückgerechnet.
Warum: `PlayerLook` soll den Wert benutzen können, ohne den Slider und
dessen Wertebereich zu kennen. Andersherum müsste jede Klasse, die die
Empfindlichkeit liest, die Umrechnung mitschleppen.
Verworfen: Sliderwert speichern und überall umrechnen.

## 2026-08-14 — Umschalt-Container tragen keine Layout Group
Was: Ein Panel, das nur zwischen Ansichten umschaltet (`MainMenuUI`,
`PauseMenuRoot`), bekommt keine Layout Group. Die sitzt jeweils auf dem
Container, dessen Kinder tatsächlich untereinander stehen (`MainMenuPanel`,
`Content`). Hintergrundbilder liegen neben diesem Container, nicht darin.
Warum: Eine Layout Group ordnet **alle** Kinder an — auch ein Vollbild-
Hintergrund wird dann in die Reihe gestellt und verschiebt alles. Genau
daran ist die Ausrichtung des Options-Fensters zunächst gescheitert.
Verworfen: Layout Group aufs Vollbild-Panel legen.

## 2026-08-14 — Options-Panel als geteiltes Prefab trotz szenenspezifischer Verweise
Was: Ein `OptionsPanel`-Prefab für Hauptmenü und Pausenmenü. Die vier
Slider-Verbindungen zum lokalen `GameSettings` und die beiden
Umschalt-Verweise des Zurück-Knopfes werden je Szene als Prefab-Override
gesetzt.
Warum: Das Prefab teilt Aufbau, Layout und Beschriftung — das ist der
Großteil der Pflege. Ohne Prefab müsste jede Layout-Änderung doppelt
gemacht werden, und genau daran war die Ausrichtung vorher gescheitert.
Szenenspezifische Verweise gehören ohnehin in die Szene.
Verworfen: zwei getrennte Options-Fenster.

## 2026-08-15 — Beschädigtes Prefab ersetzen statt reparieren
Was: Das nicht reagierende Options-Panel im Dorf wurde durch eine frische
Kopie aus dem Hauptmenü ersetzt, nicht analysiert und geflickt.
Warum: Vier Stunden Messung hatten alles Erklärbare ausgeschlossen —
Raycast traf, Position stimmte, Click-Action feuerte, `timeScale`, Cursor,
EventSystem und Doppel-Systeme waren ohne Befund. Ein Prefab, das viermal
umgehängt wurde, kann intern Referenzen verlieren, die von außen nicht
sichtbar sind. Der Austausch dauerte fünf Minuten.
Verworfen: weitersuchen bis zur Ursache. Merksatz für künftige Fälle: Bei
unerklärlichem UI-Verhalten früh eine frische Kopie gegentesten.

## 2026-08-15 — Menüzustand beim Öffnen zurücksetzen
Was: `GameController.Pause()` schaltet die Button-Seite ein und das
Options-Panel aus, bei jedem Öffnen.
Warum: Wer das Menü mit ESC verlässt, während die Optionen offen sind,
bekam beim nächsten Öffnen wieder die Optionen — ohne sichtbaren Weg
zurück. Der Zustand muss beim Öffnen definiert sein, nicht beim Schließen.
Verworfen: beim Schließen aufräumen (greift nicht, wenn über ESC statt
über den Zurück-Knopf geschlossen wird).

## 2026-08-16 — Eine Tafel für alle drei Menüs
Was: Hauptmenü, Pausenmenü und Options bekommen dieselbe zentrierte
Tafel — 760 breit, `17130F` bei Alpha 224, `UISprite` sliced mit Pixels
Per Unit Multiplier 0.5, Buttons 460 × 72.
Warum: Pausenmenü und Options brauchen ohnehin eine Fläche, damit der
Text vor dem laufenden Spielbild lesbar bleibt. Ein Bauteil, dreimal
benutzt, ergibt ein System; einzeln aufgehübschte Teile wirken
zusammengewürfelt (Isors Vorgabe vom 14.08.).
Verworfen: „Randmenü" ohne Kasten, Titel und Einträge linksbündig aufs
Bild gesetzt. Sieht im Hauptmenü besser aus, hätte aber neben der
Pause-Tafel eine zweite Formensprache ergeben.

## 2026-08-16 — Dorf-Screenshot als Menühintergrund
Was: Das blaue `BackgroundPanel` wird durch ein Standbild aus dem Dorf
ersetzt (Abenddämmerung, zwei Fackeln als Rahmen, Mitte frei), über die
Image-Farbe `6E6E6E` abgedunkelt. Dazu ein `Aspect Ratio Fitter` im
Modus `Envelope Parent` mit 1.7778.
Warum: Der Screenshot wird ohnehin für die Abgabe gebraucht
(`Press1–3.png`) — ein Arbeitsgang deckt beides. Der Fitter füllt jedes
Seitenverhältnis, ohne zu verzerren; beschnitten wird am Rand, deshalb
bleibt die Bildmitte für die Tafel frei.
Verworfen: das Farbfeld nur abdunkeln; `Preserve Aspect` (ergäbe Balken).

## 2026-08-16 — Oswald Bold als Titel- und Button-Schrift
Was: `Oswald Bold SDF` für Titel und Buttons, `LiberationSans SDF` bleibt
für Labels und Zahlenwerte. Beide Assets von `TextMesh Pro/Examples &
Extras/` nach `Assets/Shared/UI/Fonts/` verschoben.
Warum: Liegt bereits im Projekt, Open Font License, kein Download und
keine zusätzliche Zeile in der Asset-Tabelle. Zwei Schnitte mit klaren
Rollen genügen. Der Umzug ist nötig, weil der Examples-Ordner zum
Löschen gedacht ist — wäre er weg, blieben alle Texte leer.
Verworfen: eine externe Schrift herunterladen (Lizenzfrage und
Zeitaufwand vor der Abgabe).

## 2026-08-16 — Ein Schleier je Ebene
Was: Genau ein abdunkelndes Vollbild-Image pro blockierender Ebene. Im
Dorf ist das `PauseMenuRoot` (Alpha 120), die Options-Instanz dort steht
auf Alpha 0. Im Hauptmenü ist `OptionsPanel` selbst die blockierende
Ebene und behält Alpha 120. Das unsichtbare Image bleibt als
Klick-Blocker erhalten (Raycast Target an).
Warum: Zwei Schleier übereinander lassen nur rund 28 % des Bildes durch —
daher das fast schwarze Options-Fenster im Dorf. Der Schleier gehört zu
dem, was blockiert, nicht an jedes Panel.
Verworfen: das Options-Panel generell schwächer machen (nimmt dem
Hauptmenü die Trennung); die Abweichung im Dorf ins Prefab applizieren
(schaltete den Schleier auch im Hauptmenü ab).

## 2026-08-16 — HUD mit echten Daten statt gemalter Anzeigen
Was: Das In-Game-HUD bekommt bewusst Anzeigen, für die es noch wenig
Spielinhalt gibt (Spielername, Lebensleiste, Tag und Uhrzeit,
Zähmzähler). Jede Anzeige wird aber an eine echte Datenquelle gehängt —
die Lebensleiste an eine `PlayerHealth` nach dem Muster von
`SheepHealth`, nicht an einen festen Wert.
Warum: Isors Ziel ist Spielgefühl, auch bevor alle Systeme stehen. Eine
fest auf 100 % gemalte Leiste ist im Prüfungsgespräch aber eine
Behauptung; eine echte Komponente erlaubt die Antwort „das System steht,
der Schadensverursacher kommt". Zugleich macht das HUD die vorhandene
Simulation (`SheepHealth`, `SheepHunger`, `DayNightCycle`) erstmals
sichtbar und zahlt damit auf Lernziel S3 ein.
Verworfen: Zustandsbalken frei über jedem Schaf (Weltraum-Anzeige,
Nachführen, Kamera-Ausrichtung, Distanz-Ausblendung — zu teuer); die
Anzeigen ganz weglassen, weil noch wenig dahintersteht.

## 2026-08-16 — Ein Schalter fürs ganze HUD, nur auf dem Root
Was: Alle HUD-Teile liegen unter `HudRoot`. Der `GameController` schaltet
beim Pausieren ausschließlich dieses Objekt, nie die einzelnen Anzeigen.
Warum: `SetActive(false)` auf dem Root versteckt alles darunter, lässt die
Kinder aber unangetastet. Ein späterer `HudController` kann die einzelnen
Anzeigen nach Spielereinstellungen schalten, ohne dass sich beide in die
Quere kommen — sonst würde das Fortsetzen Anzeigen wieder einschalten, die
der Spieler bewusst ausgeschaltet hat (Isor).
Verworfen: jedes Element einzeln schalten; den Root-Schalter im Skript auf
dasselbe Objekt legen, auf dem das Skript sitzt (schaltet sich selbst ab
und wacht nie wieder auf — Fehler, der beim `TamedSheepDisplay` auftrat).

## 2026-08-19 — Ladescreen als Panel im Hauptmenü statt eigener Szene
Was: Der Ladescreen ist ein viertes Kind im `MainMenuUI`-Canvas, keine eigene
`Loading.unity`. Der `LoadingScreenController` sitzt auf dem immer aktiven
Canvas-Root, nicht auf dem Panel.
Warum: Der Vorteil einer eigenen Ladeszene ist, dass die alte Szene vor der
neuen aus dem Speicher fliegt — das Hauptmenü ist aber nur ein Panel und ein
Hintergrundbild. Dagegen stünden vier zusätzliche Stellen zwei Tage vor der
Frist: neue Szene, dritter `SceneId`-Wert, `_sceneNames`, und die Ladeszene
müsste sich das Ziel merken. Der Controller gehört auf das Root, weil ein
abgeschaltetes Objekt kein `Update()` bekommt und sich nie selbst einschalten
könnte.
Verworfen: eigene Ladeszene (Isors erster Vorschlag); Canvas mit
`DontDestroyOnLoad`, das auch die Zeit nach der Aktivierung abdecken würde —
das wird erst gebraucht, wenn die Laufzeit-Platzierung kommt.

## 2026-08-19 — Echter Ladefortschritt, nur weich nachgezogen
Was: Angezeigt wird `operation.progress / 0.9`, geglättet über
`Mathf.MoveTowards` mit `_fillSpeed` (0,5 Balkenlängen pro Sekunde, also
mindestens zwei Sekunden von 0 auf voll). Umgeschaltet wird, wenn der
**angezeigte** Wert 1 erreicht — nicht wenn `progress` 0,9 erreicht.
Warum: Unity hält einen zurückgehaltenen Ladevorgang von selbst bei 0,9 an;
die letzten 0,1 sind die Aktivierung. Die von Isor vermutete Wartestelle ist
also schon eingebaut und muss nicht erfunden werden. Der Fortschritt kommt
aber ruckartig, deshalb die Glättung. Und weil `isDone` mit angezogener
Handbremse nie `true` wird, ist der eigene Anzeigewert die einzige brauchbare
Umschalt-Bedingung — sonst springt das Bild weg, während der Balken noch bei
60 % steht.
Verworfen: erfundener Balken bis 80 % plus Fertigmeldung (Isors erster
Vorschlag — zwei Systeme statt einem und eine erfundene Zahl); `isDone` als
Bedingung; Coroutine statt `Update` (dasselbe Verhalten mit einem
Sprachkonstrukt mehr, das im Projekt sonst nirgends vorkommt).
`Time.unscaledDeltaTime` statt `deltaTime`, damit ein vergessenes
`timeScale = 0` den Balken nicht einfriert.

## 2026-08-19 — Eigenes weißes Sprite für Fortschrittsbalken
Was: `Shared/UI/Textures/UI_WhitePixel.png`, 8×8 Pixel reines Weiß, selbst
erzeugt. Liegt unter dem `BarFill` des Ladebalkens.
Warum: Bei `Image Type = Filled` behandelt Unity das Sprite wie `Simple` und
zieht es auf die volle Fläche — 9-Slice-Ränder werden ignoriert. Alle
Unity-Standardsprites sind abgerundet, und bei 752 × 16 Pixeln wird aus einem
8-Pixel-Eckenradius eine 188 Pixel lange, 4 Pixel flache Rundung: der Balken
sieht aus wie eine Linse. Ein weißes Sprite nimmt zudem die Image-Farbe
unverfälscht an. Selbst erzeugt heißt außerdem keine Zeile in der
Asset-Tabelle.
Verworfen: `Background` und `UISprite` (beide rund, gleiches Problem); `Knob`
(ein Kreis, ergab die erste Linsenform); ganz ohne Source Image — dann
zeichnet Unity ein volles Rechteck und ignoriert `fillAmount`, und das Feld
`Image Type` erscheint gar nicht erst.
