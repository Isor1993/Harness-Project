# ABGABE_NOTIZEN.md — Roh-Material für die Abgabe-Doku

Ownership: Nur das Roh-Material für die Abgabe-Doku von Lane Defender —
je Meilenstein Zeiten, Gebautes und Begründungen, festgehalten direkt
nach dem Baustein. Der ausformulierte Abgabetext entsteht daraus am
Projektende (DECISIONS → „Doku-Input je Baustein statt Abgabetext
sofort"); wie ausführlich, entscheidet sich dort. Die Zeiten-Tabelle
selbst besitzt der ZEITPLAN.
Format: `## <Meilenstein>` mit Stichpunkt-Blöcken Zeit · Gebaut ·
Warum so · Besonderheiten.

## M1 · Gerüst (fertig 2026-09-20)

**Zeit:** 20 h gegen 6 h Schätzung (Grindstone: Projekt gesamt
20:50 h, davon ~0:46 h Anfangs-Design; Lern-Vorlauf L1–L3 und alle
Design-Runden enthalten — das Projekt ist zugleich der C++-Kurs).

**Gebaut:** Console-Toolbox (VT-Escape, UTF-8, Einzeltasten samt
Pfeilen) · Zeichentest-Szene hinter Taste T · Szenen-Zustandsautomat
in main · Hauptmenü mit Linien-Schrift-Titel, Balken-Marker und
Gelb-Fokus · Namenseingabe als Dialogfenster mit Zeichen-Schleife
(Whitelist, Backspace, 16er-Grenze, roter Fehlerzeile, Tipp-Cursor,
Schnellweg Enter–Enter) · Player-Klasse (erste eigene C++-Klasse) ·
Tutorial- und Endszene (Figlet-Schriftzüge, Name und Level) ·
Sound-Feedback (Move/Confirm/Error) · Output-Helfer (PrintMessage,
BuildEmptyNextline, BuildCenteredText).

**Warum 20 statt 6 Stunden:** Bewusst besser ausdesignt statt
„langweiliges Konsolensystem" — grafische Screens (Linien-Schrift,
Dialogfenster, Farbsprache Gelb/Hellrot, Sounds) und das Gerüst so
vorbereitet, dass die folgenden Meilensteine schneller gehen und
leichter einzupflegen sind: Ein-Puffer-Rendering, Home-Frame-Muster,
Auswahl- und Färbungs-Bausteine, Szenen-Automat und Toolboxen sind
wiederverwendbar. Dazu echte Lernzeit (erste Klasse, Fallthrough,
Referenzen, Byte-Fallen — Lernweg in `Kern/LERNLOG.md`).

**Besonderheiten:** Titel-Einblendung bewusst gestrichen
(DECISIONS, 20.09.) · Warnstufe stand bis zum 20.09. auf /W3, seither
real /W4 und warnungsfrei (`Kern/STOERUNGEN.md`, 20.09.) ·
Raster-Zeichentest als Fundament aller Rahmen- und Symbol-Wahlen ·
Level in der Endszene ist Platzhalter bis M6.

## M2 · Lanes und Spieler (fertig 2026-09-26)

**Zeit:** ~7,5 h gegen 7 h Schätzung (Grindstone: Projekt gesamt
28,37 h minus M1-Stand 20:50 h; Design-Abschnitt vom 20.09.
enthalten). Nach M1s 20-gegen-6 eine Punktlandung — der M1-Invest
ins Gerüst (Ein-Puffer-Muster, Toolboxen, Szenen-Automat) zahlt
messbar aus.

**Gebaut:** Tick-Schleife in der GameScene (Eingabe-Drain über den
gelieferten `ReadKeyNonBlocking`-Wächter, Update, Ein-Puffer-Zeichnen
ab Cursor-Home, 200-ms-Takt über `WaitMilliseconds`) · `BuildFrame`:
der komplette Screen als ein String — HUD-Kasten, zentrierte
Korridore je Lane-Zahl (Zeile schneidet durch alle Lanes),
Spieler-Zeilen, Shop-Kasten · CPlayer-Ausbau (Lane-Index, geklemmte
MoveLeft/MoveRight) und Sprung-Steuerung A/D plus Pfeile · `CShot`
mit Konstruktor als eigenes Dateipaar, `std::vector` als
Schuss-Beutel (erster Container des Projekts), Leertaste spawnt auf
der Spieler-Lane, Aufstieg per Range-for, Entfernen per
Rückwärts-erase · Schuss `||` cyan, Spieler-T gelb.

**Warum so:** Alles aus dem M2-Design-Abschnitt vom 20.09. (sieben
DECISIONS-Einträge: Screen „Gerahmt" nach Isors Skizze, Live-Shop
statt Zwischen-Level-Screen, Progression 2/3/4 an Boss-Siegen,
Sprung-Modell mit Überdruck-Argument, Sprite B, Schuss-Symbol,
Tick-Reihenfolge) · Breiten-Feinmessung vom 21.09.: Schachfiguren
rücken 1 Zelle vor, Glyphe malt ~1,5 — der Zeilenbauer zählt Figuren
als normale Zeichen mit Pflicht-Luftzelle rechts (DECISIONS,
Fortführung am Zeichentest-Ergebnis) · DRY-Umbau der vier
Zeilen-Schleifen bewusst nach M3 verschoben — erst wenn die
Zellen-Frage stillsteht (ROADMAP-Aufgabe vom 25.09.).

**Besonderheiten:** Der fallende Bauer ist noch Platzhalter-Testlauf
in Lane 0 — echte Gegner kommen mit M3 · Schuss und Gegner
durchfliegen sich noch, die Kollision ist M4 · HUD- und Shop-Werte
sind statische Texte bis M4/M6, der Shop-Kasten ist aber gezeichnet
und die Kauf-Tasten laufen später im selben Eingabe-Drain.
