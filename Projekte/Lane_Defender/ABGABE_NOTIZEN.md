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
