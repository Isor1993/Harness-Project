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

## M3 · Gegner (fertig 2026-09-28)

**Zeit:** ~6,7 h gegen 10 h Schätzung (Grindstone: Projekt gesamt
35:04 h minus M2-Stand 28,37 h; Design-Abschnitt enthalten). Erste
Unterschreitung, zwei Gründe ehrlich benannt: Das M1/M2-Fundament
trug (Szenen-Automat, Ein-Puffer-Muster, die Schuss-Schleifen als
Spiegelvorlagen für die Gegner-Schleifen) — und ab Mitte B2 tippte
auf Isors Zuruf Claude Teile des Codes (Regler „Wer schreibt",
Abgabedruck); die Lernarbeit steckt in den Erklär- und
Gegenlese-Runden, nicht in Tipp-Minuten.

**Gebaut:** `CEnemy`-Basisklasse (Lane, Zeile, Leben, Figur;
MoveDown; virtual-Destruktor und Tempo-Hook `GetStepIntervalTicks`)
· `CNormalEnemy` ♟ (1 Leben) und `CTankEnemy` ♜ (2 Leben) als reine
Startwert-Erben · Gegner-Liste `vector<CEnemy*>` mit
delete-vor-erase und Aufräum-Schleife vor jedem Szenen-Ausgang ·
Schrittintervall 3 Ticks/Zeile über den virtual-Hook · Spawner:
fester Abstand (10 Ticks), Lane-Würfel mit Belegt-Wächter,
Typ-Würfel per Rest-Wahrscheinlichkeit, Budget 5/1 als
Zeile-1-Konstanten · `srand`-Saat in main · Durchbruch kostet
1 Leben (`CPlayer`: Start 20, Untergrenze 0,
RemoveLife/AddLife/GetLives) · Tick auf Isors Lesbarkeits-Befund in
fünf benannte Helfer zerlegt (RunSpawner mit drei `int32_t&`).

**Warum so:** die vier DECISIONS-Einträge vom 27.09. — Hierarchie
mit globalem Level-Tempo statt Runner-Typ, Level-Budget aus der
15-Zeilen-Tabelle, Zeiger-Liste wegen Slicing und Pflichtthema
Memory Management, Figuren final ♟/♜/♚. Design-Stand als
Artifact-Seite (ARTIFACT_INDEX → „Lane Defender M3-Design").

**Besonderheiten:** Nach verbrauchtem Budget läuft das Feld leer —
der Level-Wechsel ist M6 · Schüsse durchfliegen Gegner noch,
Kollision ist M4 · das HUD ist statisch, die Leben sind bisher nur
im Debugger sichtbar (HUD = M6) · `AddLife` wartet auf seinen
Aufrufer, den M4-Shop-Kauf.

## M4 · Kampf und Upgrades (fertig 2026-09-29)

**Zeit:** ~6 h gegen 8 h Schätzung (Grindstone: zwei M4-Blöcke
3:53 h + 2:00 h; Differenz zum M3-Gesamtstand 41:27 h − 35:04 h ≈
6,4 h, der Design-Abschnitt vom 28.09. ist enthalten). Zweite
Unterschreitung in Folge — das M3-Fundament trug (Gegner-Liste,
Tick-Helfer, delete-vor-erase als eingeübtes Muster), und wieder
tippte Claude Teile auf Zuruf (B2 ab der Gegner-Suche, B3 ab den
Shop-Cases); die Lernarbeit steckt in Erklär-Runde,
Verstehens-Check und Isors Entwürfen.

**Gebaut:** Belohnung als viertes Startwert-Feld im
CEnemy-Konstruktor (Bauer 20 G, Turm 50 G) · `TakeDamage` mit
Null-Klemme, `AddGold` · `HandleCollisions`: rückwärts über die
Schüsse, Index-Suche mit −1, Schaden zur Trefferzeit, Gold vor
delete, delete vor erase, Schuss immer verbraucht — **zweimal je
Tick** gegen die Platztausch-Falle · HUD-Zeile live je Tick aus den
Spieler-Werten (`BuildHudText`) · Feuer-Sperre: Sperr-Wert als Stat
in `CPlayer` (Start 4), Rest-Zähler in der Szene, Leertaste in der
Sperre still geschluckt · Shop-Tasten 1–4 im Eingabe-Drain über
`TryRemoveGold` (bool — Prüfung und Abzug in einem): [1] Schaden +1
für 100 G, [2] Sperre −1 bis Minimum 1 für 120 G (am Minimum
abgelehnt), [3] +1 Leben für 500 G, [4] gesperrt bis M5 ·
`PlayPurchaseSound` als steigendes Gegenstück zum Error-Sound ·
AtkSpeed im HUD als hochzählende Stufe 1–4.

**Warum so:** die vier DECISIONS-Einträge vom 28.09. (Kollision
zweimal je Tick, Feuerrate geschluckt statt bestraft,
Gold/Preise/Wirkungen, HUD-Vorzug) und die zwei vom 29.09.
(Kauf-Kette: ein Try, billige Fragen zuerst · Shop-Feedback:
Kauf-Sound und Stufen-Anzeige — beide auf Isors eigene Befunde am
laufenden Spiel). Design-Stand als Artifact-Seite (ARTIFACT_INDEX →
„Lane Defender M4-Design"), Erklär-Seite „💡 Lernstück ·
Tick-Kollision" aus der B2-Abnahme.

**Besonderheiten:** Die B2-Abnahme lief über einen messbaren
F5-Testbogen mit Soll-Rechnung 130 G je Testlevel (4 × 20 +
1 × 50) · der frühere Doppelschuss-Trick (zwei Schüsse in einem
Tick) ist durch die Feuer-Sperre absichtlich weg · Preise und
Startwerte sind Tuning-Masse für M6 · [4] Multishot wartet auf den
M5-Skill-Slot · Start-Gold ist 0; für Shop-Tests wird
`I_DEFAULT_GOLD` temporär hochgesetzt und zurückgedreht.

## M5 · Boss und Skills (fertig 2026-10-03)

**Zeit:** ~5,2 h gegen 8 h Schätzung (Grindstone: 5,22 h über die
M5-Blöcke — 30.09. Design und B1, 02./03.10. B2; zwischen den
Blöcken zwei Krankheitstage, deshalb lief B2 erst am Samstag).
Dritte Unterschreitung in Folge: Das Startwert-Muster und der
virtual-Hook aus M3 trugen den Boss fast von allein, und in B2
tippte Claude nach Isors CSkill-Alleinbau auf Zuruf (Erkältung plus
Abgabedruck); die Lernarbeit steckt im Review des Alleinbaus und
den Gegenlese-Runden.

**Gebaut:** `CBoss` ♚ als Startwert-Erbe (25 Leben, 500 G,
Durchbruch 5) mit dem ersten Override des Projekts
(`GetStepIntervalTicks`, 6 Ticks) · Boss-Spawn zu Levelbeginn:
zufällige Lane, Sperr-Wächter — die Boss-Lane fliegt aus dem
Lane-Würfel des Spawners (`B_TEST_LEVEL_HAS_BOSS` als
Test-Konstante bis M6) · Durchbruch-Kosten als fünftes
Startwert-Feld in `CEnemy` (Bauer/Turm 1, Boss 5), gelesen vor dem
delete · `Balance.h` als schmale Tuning-Datei (seit B2 auch alle
vier Shop-Preise) · `CSkill` abstrakt: `Fire` rein-virtuell,
virtueller Destruktor · `CMultishotSkill`: Fire-Override feuert
eigene plus rechte Nachbar-Lane, rechts außen fällt der
Zusatzschuss weg · `CPlayer`: Skill-Slot `m_pSkill` (Start
nullptr), `GetSkill`/`EquipSkill` und der erste Destruktor des
Projekts (delete auf nullptr erlaubt, keine if-Prüfung) ·
Feuer-Stelle als Entweder-oder (Slot leer = normaler Schuss, belegt
= Fire übernimmt komplett) · [4]-Kette nach dem Try-Muster: billige
Frage zuerst per &&-Kurzschluss, dann `TryRemoveGold(2000)`, dann
`new CMultishotSkill` plus Kauf-Sound.

**Warum so:** die sechs DECISIONS-Einträge vom 30.09.
(Boss-Zuschnitt mit Verdoppler-Gold 500/1000/2000, Boss-Runde zählt
auch bei Durchbruch, Multishot rechte Nachbar-Lane, Skill-Slot als
Entweder-oder mit Schuss-Besitz, [4]-Kette mit dem vierten delete,
Balance-Datei schmal) plus das Durchbruch-Feld aus dem
B1-Bau-Moment · die alte Idee „Skill-Wahl beim Boss-Sieg,
Skill-Stufen" ist bewusst ersetzt: genau ein Skill per Shop-Kauf
(DECISIONS, 20.09. und 30.09.) · Design-Stand als Artifact-Seite
(ARTIFACT_INDEX → „Lane Defender M5-Design").

**Besonderheiten:** B2-Abnahme über einen Sieben-Punkte-Testbogen,
komplett grün (normaler Schuss vor Kauf, Kauf-Verweigerung ohne
Gold, Kauf, Doppelkauf ohne Goldabzug, rechts außen ein Schuss,
Feuer-Sperre, Neustart) · der gekaufte Multishot überlebt
ESC → neues Spiel — bekannter M6-Merkposten Neustart-Reset
(delete + nullptr), kein B2-Fehler · Boss-Werte und Preise bleiben
Tuning-Masse für M6 · Nahbereichs-Schüsse sind unsichtbar
(Polish-Liste vom 30.09., M7) · die Spawn-Zeile des normalen
Schusses steht bewusst doppelt (Szene und Multishot) — als Preis
des Entweder-oder-Slots akzeptiert (DECISIONS, 30.09.).

## M6 · Level-Lauf (fertig 2026-10-03)

**Zeit:** ~5 h gegen 6 h Schätzung (Grindstone: die M6-Blöcke vom
03.10. — Design-Moment und Bau am selben Tag). Vierte
Unterschreitung in Folge, ehrlich eingeordnet: Das Design kam
krankheitsbedingt als Claude-Vorlage mit Auswahl-Entscheidungen,
und den Code tippte durchgehend Claude auf Zuruf — Isors Anteil
waren die Entscheidungen, das Gegenlesen und beide Testbögen samt
einem eigenen Befund.

**Gebaut:** die 15-Zeilen-Tabelle als sieben const-Felder in
Balance.h (Lanes, Budget, Tanks, Spawn-Abstand, Tempo, Leben-%,
Gold-%; Boss per `Level % 5`) · `SetupLevel` lädt je Zeile und
würfelt die Boss-Lane · Lane-Zahl als Szenen-Variable —
`BuildFrame` nimmt Lane-Zahl und HUD-Text als Parameter, dazu
MoveRight, Lane-Würfel und Multishot-Aufruf · Tempo-Hook nimmt das
Level-Tempo als Parameter (die Basis reicht durch, der Boss
ignoriert es — namenloser Parameter) · `ApplyLevelScaling` nach dem
new: Leben/Gold × Faktor / 100 mit Leben-Untergrenze 1; Boss-Gold
als Verdoppler-Faktor 100/200/400 statt der Gold-Spalte ·
Level-Wechsel mit 2-s-Banner (Lane-Ansage, Schüsse geleert) ·
Niederlage bei 0 Leben sofort, Sieg nach Zeile 15 ·
`CPlayer::Reset()` am Szenen-Start (Werte und Lane auf Start,
Skill-delete, der Name bleibt) · Ergebnis-Transport über
`SetRunResult`/`HasWon`/`GetReachedLevel` — der M1-Platzhalter der
Endszene ist eingelöst, das HUD zählt echt.

**Warum so:** die vier DECISIONS-Einträge vom 03.10. (Tabelle mit
Ganzzahl-Faktoren, Zwischenstand, Reset am Szenen-Start, zwei
Figlet-Schriftzüge — die existierten seit M1 und brauchten nur
echte Werte) plus die Vorentscheidungen aus M3/M5 (Budget-Modell,
globales Tempo, Boss-Regeln, Lane-Progression an den Boss-Runden).

**Besonderheiten:** Isors eigener Befund im Sieg-Test —
`SetRunResult` schrieb die Konstante statt `iLevelIndex + 1`; im
echten Lauf wertgleich, im Test-Dreher sichtbar, gefixt · beide
Testbögen liefen mit Test-Schrauben (Leben 2, Sieg nach Level 2),
beide sauber zurückgedreht · alle Tabellenzahlen bleiben
Tuning-Masse für den M7-Spieltest · „Skill: -" im HUD ist noch
statisch (M7-Polish).

## M7 · Abgabe-Polish (fertig 2026-10-03)

**Zeit:** ~3 h gegen 5 h Schätzung (Grindstone) — fünfte
Unterschreitung in Folge; die laufende Kommentar- und
Konventionspflege je Baustein hat sich hier ausgezahlt: Es gab
kaum Rückstände abzuarbeiten.

**Gebaut/geprüft:** Leak-Bilanz über alle vier new-Stellen gegen
alle sechs delete-Stellen — jeder Gegner endet auf genau einem von
vier Wegen, der Skill in Reset oder Destruktor; keine Leaks ·
cin-Scan: kein `cin >>` im Projekt übrig (alter M1-Punkt damit
erledigt) · Konventions-Pass über alle Dateien, Level4 und /utf-8
in allen vier Build-Konfigurationen verifiziert ·
Datei-für-Datei-Review aller 18 Dateipaare in sieben Runden mit
drei Isor-Befunden (NameInput-Konstanten neu gruppiert,
GameScene-Leerzeilen und Abstände geputzt — Linker-Beleg „0 von
744 Funktionen neu" für reine Ordnung; Tutorial um Shop-Tasten,
ESC und das echte Spielziel ergänzt) · Balance-Finaltuning nach
Voll-Spieltest: Leben-Kurve steiler (flach bis Boss 1, +20 je
Level, +40 nach Boss 2 — gegen die unbegrenzten Käufe), Damage
250 G, Atk Speed 500 G · Easter Egg „geheimer Name" (Startbonus
plus VIP-Marker im HUD, läuft über die fertige Namenseingabe) ·
Release-Build x64 · READ_ME im Abgabe-Stil · Abgabe-Paket in der
Portfolio-Struktur.

**Warum so:** Muss-Liste vor Kür (überfällige Abgabe nach zwei
Krankheitstagen); der BuildFrame-DRY-Befund vom 25.09. bleibt
bewusst stehen — vier parallel lesbare Schleifen, Klarheit vor
Abstraktion, als solches im Review entschieden.

**Besonderheiten:** Offene Kür-Punkte wandern auf die
Polish-Liste der ROADMAP (Sounds, HUD-Farben, Shop-Rot,
Treffer-Blitz, Fenster-Wächter) — nichts davon ist
abgabe-relevant · der eine History-Satz „(TODOs)" im
GameScene-Kopf ist Chronik, kein offenes TODO.
