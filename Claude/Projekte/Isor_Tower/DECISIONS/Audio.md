# Audio.md — Entscheidungen Audio

Ownership: Nur Entscheidungen zu Audio — was entschieden wurde, warum,
und welche Alternativen verworfen wurden. Kein Plan (das ist die
ROADMAP), kein Ereignis (das ist das LOG), keine ausformulierte Regel
(die steht in der jeweiligen Regeldatei; hier steht nur, warum sie gilt).
Nicht hier: die Bedienoberfläche der Lautstärkeregler (`UI.md`) und die
Herkunft der Klangdateien als Lizenzfrage (`Uni/DECISIONS.md`).
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**,
je ein bis zwei Zeilen. **Älteste oben**, wie in einer Chronik.

Überholte Einträge wandern nach `_ARCHIV.md` der Schicht, mit Angabe,
wodurch sie abgelöst wurden. Ein neuer Eintrag nennt, welchen er ablöst.

Gilt eine Begründung weiter und ist nur ihre Ausführung überholt, bleibt
der Eintrag stehen und bekommt eine Zeile **Fortgeführt am `<Datum>`**
mit Zeiger auf die geltende Fassung — dann geht die Herleitung nicht ins
Archiv verloren.



## 2026-08-14 — AudioMixer mit drei Gruppen statt Lautstärke je Quelle
Was: Ein `MainMixer`-Asset mit Master → Music/SFX; jede AudioSource wählt
ihre Gruppe. Die Optionen setzen später drei exponierte Parameter.
Warum: Ein Regler, der jede Quelle einzeln kennen müsste, vergisst jede
neu hinzugefügte. Über die Gruppe folgt alles automatisch.
Verworfen: Regler greift direkt auf `AudioSource.volume` zu; Sub-Mixer je
Kategorie (versehentlich zuerst gebaut — für drei Regler überdimensioniert).

## 2026-08-14 — Kein AudioManager
Was: Es gibt keine zentrale Audio-Klasse. Der Mixer ist ein Asset und wird
dort per `[SerializeField]` verdrahtet, wo er gebraucht wird.
Warum: Ein AudioManager wäre ein Singleton, und die sind in
CODE_GUIDELINES ausgeschlossen. Das Asset erfüllt denselben Zweck über
Inspector-Wiring — dasselbe Muster wie `PlayerInputReader` und `SceneLoader`.
Verworfen: die auf der Artifact-Seite „System · Grundgerüst" vorgemerkten
Klassen `AudioManager` und `SceneMusic`.

## 2026-08-14 — Wer den Klang auswählt, hält ihn auch
Was: Gibt es nichts auszuwählen, liegt der Clip in der AudioSource (Musik,
Fackel). Wählt ein Skript aus mehreren, liegen die Clips im Skript und das
Feld der Quelle bleibt leer (Schritte, Schafe, Wind).
Warum: Zwei gefüllte Stellen für dieselbe Sache — man weiß später nicht
mehr, welche gilt.
Verworfen: Clips grundsätzlich in der Quelle halten und im Skript nur
umschalten.

## 2026-08-14 — Der Interaktionsklang gehört zum Interactable
Was: Kein gemeinsamer Klang im `PlayerInteractor`. Jedes `IInteractable`
bringt seine eigene Rückmeldung mit — die Fackel über das startende Feuer,
das Schaf über einen Antwortlaut.
Warum: Der Interactor weiß bewusst nicht, was er vor sich hat; ein Klang
dort wäre für jedes Ziel derselbe. So bringt jedes neue Interactable seinen
Klang mit, ohne dass der Interactor angefasst wird.
Verworfen: ein generischer Interaktionslaut am Spieler. Die Quelle
`Audio_Interaction` bleibt bestehen, aber für Menügeräusche.

## 2026-08-14 — Eigener Timer je Quelle statt Event-Channel
Was: `RandomIntervalSound` hängt an jedem Objekt und zählt selbst.
Warum: Ein zentraler Sender, der tickt und Events verteilt, ließe alle
Schafe gleichzeitig blöken — aus einer Herde würde ein Chor. Die
Einsatzregel für Event-Channels („X passiert, unabhängige Systeme
reagieren") trifft nicht zu: Es gibt kein gemeinsames X.
Verworfen: Observer/Event-Channel mit zentralem Taktgeber.

## 2026-08-14 — Schrittfrequenz über Strecke statt Zeit
Was: `FootstepPlayer` addiert zurückgelegte Meter und löst bei 2 m aus,
statt einen Zeittakt zu verwenden.
Warum: Die Schrittfrequenz hängt damit ohne Umrechnung am Tempo — wer
langsamer läuft, legt langsamer 2 m zurück. Ein Zeittakt müsste die
Geschwindigkeit erst umrechnen, sobald es Sprinten gibt.
Verworfen: fester Zeitabstand; Tonhöhe an die Geschwindigkeit koppeln
(falsch — Tempo ändert die Frequenz der Schritte, nicht ihre Tonhöhe).

## 2026-08-14 — Alle verwendeten Klänge unter CC0
Was: Nur CC0-Material im Projekt. Das einzige CC-BY-Paket (Yo Frankie!,
Blender Foundation) wurde zurückgestellt; sein Ordner trägt `_CC-BY` im
Namen, die Belegzeile liegt fertig in seiner `_Quelle.txt`.
Warum: Es liegt ohnehin nur als FLAC vor, das Unity nicht importiert, und
der Wind wird von einem CC0-Paket abgedeckt. Damit braucht Tabelle 9 im TDD
keine Attributionsformel, nur Quelle und Lizenz je Zeile.
Verworfen: FLAC umwandeln und die Nennungspflicht in Kauf nehmen.

## 2026-08-14 — Audio-Library zweistufig
Was: `_Pakete\` hält die Originalpakete vollständig mit `_Quelle.txt`,
`Sortiert\` die nach Zweck einsortierten Kopien mit dem Paketnamen als
Dateipräfix. `_Katalog.md` verbindet beide.
Warum: Ein Paket deckt viele Zwecke ab (95 Dateien für Kampf, Inventar,
Interface). Nach Zweck zerlegt geht die Herkunft verloren, als Paket
belassen findet man nichts. Das Präfix macht jede sortierte Datei
rückverfolgbar.
Verworfen: nur nach Zweck sortieren; nur Pakete belassen; nach Lizenz
sortieren (man sucht einen Schritt-Sound, nicht „alle CC0-Dateien").

## 2026-08-14 — AudioSource.Priority gesetzt statt Voice-Limit erhöht
Was: Musik 0, Ambience 32, Schritte 100, Schafe 150, Fackeln 200.
Warum: Unity spielt nur 32 Quellen wirklich ab (`Max Real Voices`) und
virtualisiert den Rest nach Lautstärke und Priorität. Bei vielen Fackeln
fiel die leise Musik aus. Prioritäten opfern im Zweifel eine von zwanzig
Fackeln, was niemand merkt.
Verworfen: `Max Real Voices` hochsetzen — kostet Rechenzeit und behebt die
Rangfolge nicht.
