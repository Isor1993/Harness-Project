<!--
Ownership: Design-Absicht des Spiels Pathmakers TD (Arbeitstitel) —
was es sein soll, nicht wie es gebaut wird — und zugleich das
Markdown-Manuskript, aus dem `Kern/Werkzeuge/abgabe_bauen.py` die
.docx-Abgabefassung baut (Formatvorlage und Titelteil im Datenbaum,
`Kern/PFADE.md` → `DATENBAUM`; den Umgang mit der .docx regelt
`Uni/DOCX_RULES.md`). Begründungen gehören in die DECISIONS dieser
Schicht, Aufgaben in die ROADMAP, Technik ins spätere TDD. Aufbau und
Pflege regelt `Kern/GDD_RULES.md`.
Format: feste Kapitelfolge nach `Kern/GDD_RULES.md`, Kapitel als `#`
und Unterkapitel als `##` (Abgabe-Ebenen wie beim TDD); die
Abgabe-Kapitel der Aufgabenstellung
(`Uni/Semester_3/ASSIGNMENT_GAME_PITCH.md`) stehen als „weitere
Kapitel nach Bedarf" dahinter; offene Punkte als `**Offen:**` im
Kapitel und gesammelt unter „Offene Design-Fragen"; Rohes datiert im
Abschnitt „Entwurf". Alles ab der Marke `abgabe-ende` ist intern und
bleibt beim Bauen draußen. Dieser Kommentar wird beim Bauen verworfen.
-->

# Pitch

Pathmakers TD ist ein Tower-Defense-Spiel für bis zu vier Spieler, die
gegeneinander antreten und den Weg der Monster selbst bauen: Wegkacheln
sind die wichtigste Ressource, und das eigene Weg-Layout ist die halbe
Verteidigung. Jeder Spieler verteidigt sein eigenes Gebiet derselben
Karte gegen die Monster, die ihm seine Gegner schicken, und greift
mit dem eigenen Einkommen zurück an: Automatische Wellen gibt es
nicht, jede Welle besteht aus den Sends der Spieler. Gebaut wird mit einer Figur in dritter
Person, die über das Feld läuft, Wege verlegt und Türme aufrüstet; wer
allein spielt, übt dieselbe Partie als Sandbox und schickt seine
gesendeten Monster ins eigene Gebiet.

# Kern-Schleife

## Die Schleife

Eine Partie läuft in Runden. Jede Runde beginnt mit einer Bauphase:
Ein Timer von etwa einer Minute zählt herunter; wer früher fertig
ist, meldet sich bereit, und sind alle bereit, startet die Welle
sofort. Mit dem Wellenstart laufen bei jedem Spieler alle
Monster los, die ihm per Send in die Warteschlange gelegt wurden.
Automatische Wellen gibt es nicht: Die Sends der Spieler sind die
Welle, und hat niemand geschickt, ist die Karte sofort leer und die
nächste Bauphase beginnt direkt. Die Kampfphase endet, wenn die
ganze Karte leer ist; erst dann beginnt der nächste Timer. So hat jeder Spieler vor jeder Welle
garantiert dieselbe Bauzeit.

Wegkacheln dürfen verlegt oder geändert werden, solange im eigenen
Gebiet keine Monster unterwegs sind, also in der Bauphase und nach
dem eigenen Rundenende, während andere noch kämpfen: Wer sein Gebiet
früh leerkämpft, erspielt sich zusätzliche Bauzeit. Alles andere geht
jederzeit: Türme bauen und aufrüsten, Arbeiter kaufen und Monster in
die Sende-Warteschlange legen sind auch mitten im Kampf erlaubt.

Jeder Spieler beginnt mit einem Vorrat an Leben, als Richtwert 20.
Ein Monster, das sein Ziel erreicht, verschwindet und kostet ein
Leben, der Boss etwa fünf. Bei null Leben scheidet der Spieler aus;
der letzte Überlebende gewinnt die Partie. Wer allein spielt, kann
nicht gewinnen: Die Solo-Partie läuft endlos, bis die Leben
aufgebraucht sind, und gemessen wird die erreichte Runde. Eine feste
Partielänge gibt es nicht: Weil jeder Send das Einkommen dauerhaft
erhöht, schaukeln sich die Wellen im Wettrüsten von selbst hoch, bis
eine Verteidigung bricht; gezielt wird auf etwa 15 bis 25 Minuten.

## Wirtschaft und Senden

Es gibt drei Ressourcen, jede mit genau einer Quelle. Gold gibt es
für getötete Monster; es bezahlt Türme und ihre Stufen. Diamanten
kommen als Einkommen mit jedem Wellenstart, in dem Moment, in dem der
Timer auf null geht; das Grundeinkommen ist null und wächst nur durch
das Senden. Alle Spieler starten mit demselben Diamanten- und
Gold-Vorrat, damit die ersten Türme schon vor dem ersten Send stehen
können; die Startwerte stellt der Spieltest ein. Wegkacheln liefern die Arbeiter, die
mit Diamanten gekauft werden.

Wer Monster schickt, bezahlt sie mit Diamanten und erhöht damit
dauerhaft sein eigenes Einkommen: Jeder Monstertyp trägt neben dem
Preis einen festen Einkommens-Wert, der sich beim Senden aufaddiert.
Angriff ist zugleich eine Investition, ein früh gesendetes Monster
verdient seinen Preis über die folgenden Runden zurück. Zugleich werfen gesendete Monster beim Verteidiger Gold
ab, wer viel schickt, füttert also auch die Türme des Gegners. Hinter
jedem Diamanten steht damit dieselbe Entscheidung: angreifen, den
eigenen Weg ausbauen oder sparen. Wer nie angreift, baut kein
Einkommen auf und fällt im Wettrüsten zurück; Passivität bestraft
sich selbst.

Das Senden kennt keine Zielwahl: Die Spieler stehen in einer festen
Reihenfolge, die der Anordnung der Gebiete im Uhrzeigersinn folgt,
und jeder schickt immer an den Nächsten in der Liste. Scheidet ein
Spieler aus, rückt dessen Nachfolger als Ziel nach. Wer allein
spielt, schickt an sich selbst: Die gesendeten Monster kommen ins
eigene Gebiet, und Senden bleibt auch solo eine echte Entscheidung
zwischen Einkommen und Risiko.

## Weg-Bau

Wegkacheln kommen aus der Mine: Arbeiter bauen sie laufend ab, und
Arbeiter werden mit Diamanten gekauft. Zu Partiebeginn liegt in jedem
Gebiet ein vorgegebener Standardweg vom Start- zum Endpunkt; dazu
startet jeder Spieler mit einem kleinen Kachel-Vorrat und einem
Arbeiter, die genauen Startwerte werden im Spieltest eingestellt.
Auch die Kacheln des Standardwegs dürfen abgebaut und versetzt
werden: Der vorgegebene Weg ist nur die erste Fassung, aus der jeder
Spieler sein eigenes Layout formt. Wann der Weg geändert werden darf,
steht unter „Die Schleife".

Als Weg zählt, was zusammenhängend am Startpunkt beginnt; Kacheln
ohne Verbindung dorthin sind Vorrat auf dem Feld, kein Weg. Endet der
Weg vor dem Ziel, etwa mitten in einem Umbau, laufen die Monster vom
Wegende in gerader Linie zum Endpunkt weiter. Der Weg darf sich
gabeln; wie sich Monster an einer Gabelung verhalten, steht unter
„Wellen und Gegner".

## Türme und Upgrades

Vier Türme, jeder mit genau einer Rolle: Der Pfeilturm schießt
schnell auf Einzelziele und ist günstig. Der Kanonenturm trifft
Gruppen mit Flächenschaden bei langsamem Takt. Der Frostturm
verlangsamt alle Monster in seinem Umkreis und macht selbst kaum
Schaden. Der Scharfschütze schießt selten, dafür sehr hart und über
große Reichweite. Die Rollen greifen ineinander: Frost vor dem
Scharfschützen verlängert dessen Wirkung, die Kanone beantwortet
Massen-Sends. Türme stehen nie auf Wegkacheln, sondern auf der freien
Fläche neben dem Weg.

Jeder Turm hat drei Stufen. Eine höhere Stufe macht denselben Turm
besser: mehr Schaden, etwas mehr Reichweite, beim Frostturm stärkeres
Verlangsamen. Verzweigte Ausbauten sind eine mögliche Erweiterung
späterer Versionen, ebenso Ausbauten für die Spielfigur selbst.

## Wellen und Gegner

Vier Gegnertypen tragen das Spiel, und alle vier sind das
Sende-Sortiment mit Preisen in Diamanten: Normal ist der günstige
Allrounder. Schnell hat wenig Leben und hohes Tempo. Der Tank hat
viel Leben und ist langsam. Der Boss ist sehr zäh, der teuerste von
allen und trägt eine Aura, die die Monster um ihn herum beeinflusst;
ob die Aura sie zäher oder schneller macht, entscheidet der
Spieltest. Fliegende Gegner gibt es bewusst nicht: Der Weg ist die
Verteidigung, und ein Gegner, der ihn ignoriert, würde den Kern des
Spiels aushebeln.

Die Monster haben feste Werte und werden nicht von selbst stärker:
Dass die Wellen wachsen, liegt allein am steigenden Einkommen der
Spieler, die mehr und teurere Monster schicken. Stärkere Varianten
der vier Typen sind eine mögliche Erweiterung späterer Versionen.

Alle Monster laufen vom Startpunkt ihres Gebiets zum Ziel und bleiben
dabei auf den Wegkacheln. An einer Gabelung teilen sie sich strikt
abwechselnd auf, eines links, eines rechts; so bleibt jedes Layout
berechenbar. Eine Zufallsvariante wird später geprüft.

# Welt-Struktur

Gespielt wird auf einer zusammenhängenden Welt, die in vier Gebiete
geteilt ist. Die Gebiete sind immer gleich groß und funktional
identisch: gleiche Kachelfläche, gleiche Lage von Start- und
Endpunkt. Nur im Aussehen unterscheiden sie sich leicht, damit man
sich auf der Karte zurechtfindet. Jeder Spieler baut und bewegt sich
ausschließlich in seinem eigenen Gebiet, sieht aber die Nachbarn
spielen: Wer eine Welle schickt, kann zusehen, wie sie drüben
ankommt.

Jedes Gebiet hat einen festen Startpunkt, an dem die Monster
erscheinen, und einen festen Endpunkt, den sie erreichen wollen;
dazwischen liegt die freie Kachelfläche für Weg und Türme, dazu ein
Wirtschaftsbereich mit Mine und Sende-Gebäude. Bei
weniger als vier Spielern bleiben die übrigen Gebiete leer; die
Karte ändert ihre Größe nicht, und am Balancing ändert sich dadurch
nichts. Die genaue Gebietsgröße in Kachelplätzen wird im Prototyp
eingestellt.

# Spieler

## Perspektive und Kamera

Die Spielfigur wird in dritter Person gespielt; die Kamera blickt
schräg von oben auf das Geschehen. Es gibt zwei Kamera-Zustände:
Beim Laufen hängt die Kamera an der Figur, daneben lässt sich der
Blick mit der Maus frei über das eigene Gebiet bewegen, um das
Layout zu planen. Das genaue Verhalten und die Übergänge zwischen
beiden Zuständen werden im Prototyp eingestellt.

## Steuerung

Gespielt wird mit Tastatur und Maus: Die Figur läuft direkt per
Tastatur, gebaut wird mit der Maus. Beim Platzieren von Kacheln und
Türmen hängt ein halbtransparentes Vorschaubild an der Mausposition;
der Linksklick bestätigt, und die Figur läuft selbst zur Baustelle
und beginnt dort zu bauen. Laufwege bleiben dadurch Teil des Spiels:
Was weit weg ist, dauert länger. Wie Aufrüsten und Senden bedient
werden, beschreibt das Kapitel zur Benutzeroberfläche; die genaue
Tastenbelegung legt der Prototyp fest.

# Persistenz

Jede Partie steht für sich. Zwischen den Partien bleiben nur die
Einstellungen erhalten; es gibt keine Freischaltungen, keinen
Spielerfortschritt, kein Inventar und keine Charakterwerte. Laufende
Partien werden nicht gespeichert: Eine Partie wird zu Ende gespielt
oder verlassen. Freischaltbare Inhalte wie neue Türme oder
Statistiken sind eine mögliche Erweiterung späterer Versionen.

# Benutzeroberfläche

Das HUD zeigt die Ressourcen (Gold, Diamanten, Kacheln, Leben) samt
dem Diamanten-Einkommen pro Runde, dazu die Rundennummer, den Timer
der Bauphase mit dem Bereit-Knopf und die Lebensstände aller
Spieler. Ein angeklickter Turm zeigt ein kleines Feld mit Stufe,
Aufrüst-Knopf und Preis.

Die Spielfigur trägt unten eine Aktionsleiste mit ihren Handlungen,
allen voran dem Bauen. Ob die Leiste als sichtbare Quick-Slots, als
Befehlsfeld oder als Radialmenü bedient wird, entscheidet der
Prototyp; die Quick-Slots sind der Favorit.

Jedes Gebiet hat einen Wirtschaftsbereich: Dort stehen die Mine mit
den Arbeitern und das Sende-Gebäude. Beides wird jederzeit direkt
mit der Maus bedient, ohne dass die Figur hinlaufen muss. Am
Sende-Gebäude wählt der Spieler aus den vier Monstern mit ihren
Diamanten-Preisen, an der Mine kauft er Arbeiter; die Figur selbst
ist allein fürs Bauen von Wegen und Türmen zuständig. Welche Monster
ein Gegner einem geschickt hat, zeigt das Spiel bewusst nicht an;
was mit dem Wellenstart ankommt, bleibt bis dahin eine Überraschung.

Die Menüfolge ist kurz: Hauptmenü (Spielen, Einstellungen, Beenden),
eine Lobby mit Join-Code (der Host erstellt die Partie, Mitspieler
treten per Code bei; wer allein spielt, startet die Partie direkt
aus der Lobby) und ein Endbildschirm mit der Platzierung, nach einer
Solo-Partie mit der erreichten Runde.

Barrierefreiheit: Bedeutung wird nie allein über Rot und Grün
getragen. Die Spielerfarben sind ein farbfehlsichtig-taugliches Set,
und wichtige Zustände tragen zusätzlich Form oder Text.

# Thema, Aussehen und Story

Pathmakers TD spielt in einer freundlichen Fantasy-Welt und sieht
stilisiert aus: einfache Cartoon-Formen, kräftige Farben und ein
Toon-Shading über allen Assets, angelehnt an Anime-Looks wie den von
Genshin Impact. Der einheitliche Stil entsteht dabei weniger in den
einzelnen Modellen als im gemeinsamen Shading, das alle Assets auf
einen Look zusammenzieht.

Der Ton ist entspannt und beruhigend. Die Monster sind nichts zum
Fürchten, sondern putzige Fantasy-Wesen, die in Grüppchen über die
Wege ziehen, und auch eine Niederlage bleibt freundlich: Der
Wettstreit ist das Thema, nicht der Untergang.

Die Türme sind Spielfiguren, keine Bauwerke: Wächter, die neben dem
Weg Stellung beziehen und die vier Turmrollen sichtbar verkörpern.
Welche Wesen die Wächter und die Monster genau sind, entscheidet die
Asset-Auswahl im Prototyp; Kandidaten stehen im „Entwurf".

Eine Geschichte erzählt Pathmakers TD bewusst nicht. Der Rahmen ist
der Wettstreit der Spieler selbst, und mehr braucht eine Partie
nicht; das Genre trägt ohne Hintergrundgeschichte.

# Audio und Musik

Die Musik bleibt ruhig und freundlich im Hintergrund und wechselt
zwischen Bau- und Kampfphase nur leicht, damit der entspannte Ton
trägt. Klar hörbar sind dafür die Ereignisse: Wellenstart,
Bereit-Meldung, Kachel legen, Turmschuss und der Lebensverlust am
Endpunkt. Die Klänge kommen aus freien Audio-Bibliotheken;
ausgewählt wird im Prototyp.

# Vergleichbare Produkte und Referenzen

Pathmakers TD steht in der Tradition der Warcraft-3-Karten
Wintermaul Wars und Legion TD. Von Wintermaul Wars übernimmt es das
Wellenmodell: Es gibt keine automatischen Wellen, jede Welle besteht
aus den Monstern, die die Spieler einander schicken. Von Legion TD
stammt das Einkommens-Modell, in dem jeder Send das eigene Einkommen
dauerhaft erhöht. Von beiden unterscheidet es sich an zwei Stellen:
Der Weg wird nicht durch Turm-Mauern geformt oder vorgegeben,
sondern aus Kacheln selbst verlegt und ist dabei die knappste
Ressource, und gespielt wird nicht aus der Befehlssicht, sondern mit
einer Figur in dritter Person mitten im eigenen Gebiet.

Unter den neueren Spielen teilen drei je einen Baustein: Isle of
Arrows legt Wege aus Kacheln, zieht sie aber zufällig wie in einem
Brettspiel und bleibt ein Solo-Spiel. In Rogue Tower wächst der Weg
von selbst und wird nur in der Richtung gelenkt, nicht frei verlegt.
Thronefall spielt sich ähnlich entspannt mit einer eigenen Figur,
die baut und verteidigt, kennt aber keinen Wettstreit unter
Spielern. Die Kombination aus Wettstreit-Senden, eigener Spielfigur
und dem frei verlegten Weg als knapper Ressource ist in dieser Form
nicht besetzt.

# USP

Drei Dinge machen Pathmakers TD besonders. Erstens ist der Weg die
Verteidigung: Wegkacheln sind die knappste Ressource, und das eigene
Layout entscheidet mehr als jeder einzelne Turm. Zweitens hat jeder
Diamant drei Richtungen: angreifen, ausbauen oder sparen, und jeder
Angriff ist zugleich eine Investition ins eigene Einkommen, füttert
aber die Türme des Gegners mit Gold. Drittens wird schnelles Spielen
belohnt: Wer sein Gebiet früh leerkämpft, baut schon weiter, während
die anderen noch kämpfen.

# Zielpublikum

Pathmakers TD richtet sich an Spieler, die Tower Defense mögen und
im Wettstreit mit Freunden mehr sehen als im Alleinspiel: kurze
Partien von 15 bis 25 Minuten, bis zu vier Spieler per Join-Code.
Die zweite Gruppe sind Tüftler, die solo in der Sandbox Layouts und
Builds ausprobieren. Der freundliche Look und die einfache Steuerung
halten die Einstiegshürde niedrig; Vorwissen aus anderen
Tower-Defense-Spielen hilft, ist aber nicht nötig.

# Ziel und Umfang

Ziel ist eine vollständig spielbare, releasefähige erste Version:
eine Karte mit vier Gebieten, vier Wächter mit je drei Stufen, vier
Gegnertypen, Partien für bis zu vier Spieler per Join-Code und die
Solo-Sandbox. Dieser Umfang ist bewusst klein geschnitten. Alles
Weitere ist modular erweiterbar und im Dokument als mögliche
Erweiterung markiert: verzweigte Turm-Ausbauten, Ausbauten für die
Spielfigur, die Zufalls-Gabelung an Wegverzweigungen und
freischaltbare Inhalte.

# Zeitplan

Der Zeitplan ist als Meilenstein-Folge angelegt, bewusst ohne
Kalenderdaten; Daten bekommt er, sobald das Projekt startet.

1. **Konzept:** Das Design-Dokument steht (dieser Stand).
2. **Fundament** (etwa ein bis zwei Wochen): Die erprobte
   Netz-Grundlage wird übernommen, die Karte mit vier Gebieten
   entsteht als Blockout, die Figur läuft und legt Kacheln.
3. **Weg-System** (etwa eine Woche): Standardweg, Wegfolge mit
   Gabelung und gerader Linie, der erste Gegnertyp läuft vom Start
   zum Ziel.
4. **Wächter und Kampf** (etwa ein bis zwei Wochen): die vier
   Wächter mit drei Stufen; Monster sterben, Gold fließt, Leben
   gehen verloren.
5. **Wirtschaft und Senden** (etwa zwei Wochen): Mine, Arbeiter,
   Sende-Gebäude mit Warteschlange und Einkommen; der volle
   Rundenzyklus läuft, die Partie lässt sich verlieren und gewinnen.
6. **Messrunden** (etwa eine Woche): Startvorräte, Preise,
   Einkommens-Werte, Aura-Wirkung und Partielänge werden gespielt
   und gemessen.
7. **Feinschliff und Präsentationsfassung** (etwa eine Woche): die
   erste vorzeigbare Fassung; das Dokument wird nachgeführt, Bilder
   und kurze Videos entstehen aus dem Spiel.

Jeder Meilenstein ist mit Reserve geplant: Was kippt, fällt in die
Erweiterungsliste, statt den Plan zu sprengen.

# Technische Daten

Zielplattform ist der PC. Gespielt wird online: Die Verbindung läuft
über einen Relay-Dienst mit Beitritts-Code, ein eigener Server ist
nicht nötig; die Solo-Sandbox läuft ohne Verbindung. Die
Hardware-Anforderungen bleiben bescheiden, der stilisierte
Low-Poly-Look hält das Spiel auch auf schwächeren Rechnern
lauffähig. Genaue Mindestanforderungen werden am Ende der
Entwicklung gemessen statt geschätzt.

# Entwicklungsumgebung

Das Spiel entsteht in Unity (C#). Der Mehrspieler-Teil baut auf
einer vorhandenen, erprobten Grundlage auf: Netcode for GameObjects
mit Relay und Beitritts-Code, Lobby und netzsynchronem Laden,
getestet über getrennte Netze. 3D-Assets, Musik und Sounds kommen
aus fertigen, frei lizenzierten Packs; eigene Inhalte entstehen bei
Bedarf in Blender. Die Versionsverwaltung läuft über Git.

# Vorgehensweise und Qualitätssicherung

Pathmakers TD ist ein Ein-Personen-Projekt: Design und Code liegen
in einer Hand. Gebaut wird System für System; jeder Baustein wird
gebaut, in kleinen Zwischentests geprüft und dokumentiert, erst dann
beginnt der nächste. So gibt es zu jedem Zeitpunkt einen
funktionierenden Stand statt vieler halbfertiger Baustellen.

Design-Entscheidungen werden mit Begründung festgehalten, dieses
Dokument wird laufend nachgeführt, und der Umfang der ersten Version
bleibt bewusst klein. Vier Dinge sind die Messlatte jeder Fassung:
klarer Fokus, spürbares Gameplay-Feedback, einheitlicher Stil und
passender Sound. Balance-Werte des Wettrüstens, von den
Startvorräten bis zu den Einkommens-Werten, werden in Test-Plays mit
anderen Spielern gemessen statt geschätzt; getestet wird doppelt, im
Mehrspieler über das echte Netz und solo in der Sandbox. Bei Assets
zählen drei Prüfungen vor dem Einsatz: die Lizenz, die Passung zum
Stil und der Preis.

# Quellenverzeichnis

Das Quellenverzeichnis wird mit der Endfassung des Dokuments
nachgetragen.

<!-- abgabe-ende -->

# Offene Design-Fragen

*(derzeit keine — die bisherigen Fragen sind entschieden und stehen
in ihren Kapiteln)*

# Entwurf

*(2026-10-12, Isors Grundidee aus der Ideen-Vergleichsrunde — roh,
bindet nichts)*

- 3D-Welt, Figur in dritter Person, Kamera schräg von oben.
- Feste Start- und Endpunkte; die Monster laufen vom Start zum Ziel und
  dürfen nur auf Wegkacheln laufen.
- Den Weg baut der Spieler selbst: Wegkacheln werden abgebaut oder als
  Belohnung verdient und nach und nach verlegt; über das Layout findet
  man eigene Strategien.
- Gegner-KI im Kern nur eine: von A nach B auf den Kacheln. An
  Gabelungen teilt sich die Gruppe (etwa 50:50 oder zufällig).
- Die Figur läuft selbst hin, legt Wege, baut Türme und rüstet sie auf.
- Multiplayer denkbar: größeres Spielfeld, das man als Team bebauen
  muss.
- Wellensystem wie in einer klassischen Tower Defense.
- Isors Einschätzung: geringer in der Umsetzung, flexibel, leicht um
  Content erweiterbar, trägt schon mit minimalistischen Systemen.
- Referenz-Kandidaten (Claude, unbestätigt): Isle of Arrows
  (Weg-Kacheln und Türme auf einer Insel), Rogue Tower (Pfad wächst
  pro Welle, aber automatisch), Thronefall (minimalistisches 3D, Figur
  läuft herum und baut), Maze-TDs aus Warcraft 3 (Weg durch Bauen
  formen). Die Kombination aus Koop, eigener Figur und Weg als
  Ressource wirkt unbesetzt — bei der Recherche prüfen.
- Art-Kandidat: Kenney Tower Defense Kit (frei, Kacheln und Türme).
- *(2026-10-16)* Senden-Vorbilder von Isor benannt: Wintermaul Wars
  (Warcraft-3-Mod, sein Haupt-Vorbild) und Legion TD. Vorgemerkt für
  „Vergleichbare Produkte und Referenzen" — dort offensiv nennen:
  steht in der Tradition von X, unterscheidet sich durch Y.
- *(2026-10-16)* Beschleunigung übriger Monster gegen zähe
  Kampfphasen (Claudes Vorschlag) von Isor vorerst herausgenommen;
  nur wieder prüfen, falls Playtests Endlos-Runden zeigen.
- *(2026-10-17)* Thema-Kapitel entschieden: Stil stilisiert mit
  Toon-Shading, Türme als Wächter-Figuren, bewusst keine Story.
  Asset-Kandidaten dazu, alle frei: Quaternius-Monster-Packs (CC0,
  animiert) für die Gegner, Bug Knight Tower Defense Pack (itch.io,
  frei gegen Namensnennung, cel-shaded) für die Wächter, Kenney
  Tower Defense Kit (CC0) für Kacheln und Umgebung. Der eigene
  Toon-Shader (Semesterziel) soll die Mischung vereinheitlichen.
- *(2026-10-17)* Wellenmodell klargestellt: keine automatischen
  Wellen, die Wellen bestehen aus den Sends der Spieler
  (Wintermaul-Modell). Dazu entschieden: ein Timer (Income bei Timer
  null), Gold-Startvorrat gegen Früh-Rush, feste Monster-Werte
  (Eskalation nur übers Einkommens-Wettrüsten), Passivität wird
  bewusst allein über die Wirtschaft bestraft.
- *(2026-10-17)* Verifizierte Quellen fürs spätere Quellenverzeichnis
  (Recherche zum Referenz-Kapitel): Isle of Arrows (MobyGames,
  Entwicklerbeschreibung: zufällig gezogene Kacheln, Solo), Rogue
  Tower (Steam-Seite: Weg wächst je Level in gewählter Richtung),
  Thronefall (Reviews: Tag-Nacht-Schleife, König reitet und baut,
  kein Versus), Legion TD 2 (Einsteiger-Guide: jeder Send erhöht das
  Einkommen dauerhaft). Wintermaul Wars nach Isors eigener
  Spielerfahrung, ohne Schriftquelle.
- *(2026-10-20)* **Zweck-Kette fehlt im Abgabetext** — Befund aus dem
  Discord-Durchgang mit der Dozentin (`Uni/LOG.md`): Das Dokument sagt
  dreimal, *dass* der Weg die Verteidigung ist, nennt aber nirgends den
  Mechanismus. Beim Nachziehen hinein: Ein längerer Weg heißt mehr Zeit
  unter Beschuss, und Weg und Türme teilen dieselbe Fläche, weil Türme
  nie auf Wegkacheln stehen. Weg-Bau ist damit die Entscheidung
  zwischen Laufzeit und Feuerkraft, mit einem Optimum in der Mitte.
  Isors Bild dafür: erst die gerade Linie von A nach B, später eine
  Spirale, in der Monster zweimal am selben Turm vorbeilaufen.
- *(2026-10-20)* **Der Fall „alle halten still"** — der Satz
  „Passivität bestraft sich selbst" gilt nur für einen Passiven unter
  Aktiven. Halten alle still, bewegt sich nur die Mine, und die Partie
  endet nie. An die Dozentin ging das Argument, dass der Pakt
  Einstimmigkeit braucht und der erste Abweichler dauerhaft vorn liegt.
  Kandidaten für eine Absicherung (Claude, unbestätigt): ein Taktgeber,
  der nur bei Stillstand greift; ein hartes Rundenlimit.
- *(2026-10-20)* **Turtle-Befund** (Isor): Wer nur verteidigt, lebt vom
  Gold, das ihm die Angreifer mit ihren Sends liefern, und wird dafür
  kaum bestraft. Seine Decke ist der feste Kachelvorrat ohne Arbeiter
  und Stufe 3 als Maximum; das Einkommen des Angreifers hat keine.
  Gegenmaßnahme, falls der Spieltest das Fenster zu lang zeigt:
  stärkere Kopplung zwischen Gold und Diamanten in Richtung WMW
  (Arbeiter über Diamanten, Senden früh über Gold, Gold-Überschuss
  wandert ins Diamanten-Einkommen). Der genaue Mechanismus ist noch
  nicht ausformuliert.
- *(2026-10-20)* **Solo als Endlos-Sandbox** — Vorschlag der Dozentin:
  ein Modus, in dem man nicht verlieren kann (unendlich Leben oder
  Ressourcen). Isor dazu: eher viele Einstellungen selbst setzbar,
  falls Zeit bleibt.
- *(2026-10-20)* **Im Chat beantwortet, gehört in den Abgabetext:** der
  Grund für den festen Sende-Ring (Balancing einfach halten, freie
  Zielwahl wäre schwerer auszubalancieren), dass die Nachbarn mit der
  Kamera dauerhaft sichtbar sind, und der Grund für die Spielerfigur
  (nostalgisches Gefühl statt Handy-Spiel, Laufzeit als Spannung, Bauen
  soll sich wie Bauen anfühlen).
- *(2026-10-23)* **Aktionsleisten-Frage entschieden** (P-B2-Design-
  Runde): Die Leiste wird eine Quick-Slot-Leiste mit Kategorien
  (Kacheln, Wächter); welcher Wächter es wird, entscheidet sich am
  gebauten Platz über dessen Panel — dasselbe Panel, das Abbauen und
  Aufrüsten trägt (Sockel-Muster nach Wintermaul Wars). Fürs Kapitel
  „Benutzeroberfläche" beim G2-Nachzug: Der Satz „ob Quick-Slots,
  Befehlsfeld oder Radialmenü, entscheidet der Prototyp" ist damit
  beantwortet. Offen für die P-B7-Runde: Panel-Form am Platz (alle
  vier Wächter sofort oder neutraler Sockel) und die Preisaufteilung
  zwischen Platz und Wahl. Begründungen in `DECISIONS.md`, Einträge
  vom 2026-10-23.
- *(2026-10-29/30)* **Karten-Blockout und Zeitplan entschieden**
  (P-B3-Design-Runde): Die Karte steht als Blockout — vier gleiche
  Gebiete à 50×70 Zellen, im 2×2 angeordnet, getrennt durch ein
  10 Zellen breites Fluss-Kreuz, zusammen 220×300 m auf einem
  Unity-Terrain; Gebiete per Zahl gekennzeichnet statt per Farbe.
  Fürs Kapitel „Welt-Struktur" beim G2-Nachzug. Der Zeitplan hat
  jetzt Kalenderdaten: Der Meilenstein-Plan (Fertig-Linien und
  Inhalte je Abgabe, `ROADMAP.md` → „Meilenstein-Plan") ersetzt beim
  G2-Nachzug die datumlose Meilenstein-Folge im Kapitel „Zeitplan";
  die Fertig-Linien gehen als Pufferzeiten hinein, der interne
  Vorsprung bleibt bewusst draußen. Begründungen in `DECISIONS.md`,
  Einträge vom 2026-10-29 und 2026-10-30.
- *(2026-11-08)* **Takt + Senden entschieden** (P-B5-Design-Runde),
  drei Abweichungen vom Abgabetext für den G2-Nachzug: **(1)** Die
  Bauphase ist fest kurz (Richtwert 10 Sekunden) statt „etwa eine
  Minute", und den Bereit-Knopf gibt es nicht mehr — gebaut wird
  ohnehin jederzeit im leeren Gebiet, die Bauphase ist nur die
  Atempause („Die Schleife" anpassen). **(2)** Das Einkommen tickt
  auf einer eigenen Uhr alle 30 Sekunden ab Spielstart, phasen-
  unabhängig — nicht mehr beim Wellenstart („Wirtschaft und Senden"
  anpassen). **(3)** Das Drei-Ressourcen-Modell steht in Frage: Der
  Prototyp fährt vorerst nur Gold; ob Diamanten kommen, entscheidet
  eine eigene Design-Runde vor P-B6 — das Kapitel „Wirtschaft und
  Senden" wird danach nachgezogen. Dazu als Regeln bestätigt: Sends
  sammeln sich im Pool (Einzahlen jederzeit), beim Wellenstart zählt
  ein Schnappschuss, Späteres läuft in der nächsten Welle;
  ausgeschiedene und leere Plätze werden im Sende-Ring übersprungen,
  der letzte Aktive schickt an sich selbst. Begründungen in
  `DECISIONS.md`, sechs Einträge vom 2026-11-08.
- *(2026-11-08)* **Vorab-Gedanken zur Ressourcen-Runde P-B5v** (Isor,
  aus der Reflexionsrunde — roh, bindet nichts): Kandidat **„Gold
  kauft, Diamant verbessert"** — Monster *und* Tower kosten Gold
  (eine Kauf-Währung = jede Münze stellt dieselbe
  Angriff-oder-Verteidigung-Frage, leichter zu balancen); die Mine
  arbeitet **Diamanten** ab statt Kacheln, Diamanten kaufen Arbeiter
  und Upgrades. Alternativ angedacht: Währungen nicht separieren,
  sondern tauschbar machen. Offene Upgrade-Flächen gesammelt: Tower
  (Stufen wie im GDD oder anders?), Sende-Gebäude (Ausbau schaltet
  neue Mob-Typen frei? einzelne Mobs verbessern? globale Buffs wie
  +2 % Tempo?), Tiles, Arbeiter. Leitfragen für die Runde: woran
  hängt das Sende-Einkommen im Gold-Modell (Schneeball-Prüfung);
  wer liefert Kacheln, wenn die Mine Diamanten liefert; Folgen für
  P-B8 (bisher Streichkandidat, würde zur Diamanten-Quelle);
  welche der vier Upgrade-Flächen bleibt fürs Semester überhaupt
  offen.
  **Nachtrag aus derselben Runde** (Isor, konkretisiert): **Gold** —
  Monster senden, Türme bauen, Türme upgraden; das Einkommen zahlt
  Gold. **Diamanten** — werden in der Mine abgearbeitet; kaufen
  Kacheln (!), Sende-Gebäude-/Mob-Upgrades und (wahrscheinlich) die
  Minenarbeiter; Start mit einem Arbeiter. Die Mine hält er
  inzwischen für machbar in der Zeit („nicht so kompliziert") — das
  rüttelt am Streichkandidaten-Status von P-B8. Die Upgrade-Flächen
  bleiben bewusst offen („nur Ideen, sehen ob sie reinpassen").
  Für die Runde bleiben damit: Arbeiter-Währung (Gold oder Diamant),
  die Schneeball-Prüfung des Gold-Einkommens, der P-B8-Status und
  die Startwerte.
- *(2026-11-10)* **Ressourcen entschieden** (P-B5v-Design-Runde) —
  löst die offenen Punkte vom 2026-11-08 auf: Zwei Währungen. **Gold
  kämpft** — Senden, Türme bauen und aufrüsten; das Einkommen zahlt
  Gold, fester Einkommens-Wert je Typ addiert sich beim Senden,
  Kopfgeld für Kills bleibt. **Diamanten bauen aus** — Kacheln,
  Arbeiter (mit Maximalgrenze), Upgrades; einzige Quelle ist die
  Mine, bis P-B8 ersatzweise ein Tropf. Sende-Vorrat je Monstertyp
  (10 Stück, +1 alle 5 s) als Spam-, Performance- und
  Schneeball-Bremse; höhere Monster mit besserem Einkommen je Gold —
  Partieende durch Durchbruch. Mine = Wirtschafts-Panel (Arbeiter
  kaufen/upgraden, Kacheln kaufen), Sendegebäude bleibt pur Senden;
  Monster-Upgrades in der Mine als Idee notiert. Richtwerte: Normal
  25 Gold / +5, Leiter 50–200; Start 100 Gold, 0 Diamanten,
  5 Kacheln, Kachel-Preis 5 Diamanten, Tropf 1 Diamant / 10 s.
  Vertagt: Kopfgeld-Wert und Turmpreise in die P-B7-Runde, die
  Einkommens-Werte der höheren Typen an den Einbau der Typen.
  Begründungen in `DECISIONS.md`, vier Einträge vom 2026-11-10. Das
  Kapitel „Wirtschaft und Senden" wird beim G2-Nachzug entsprechend
  umgebaut.
- *(2026-11-15)* **Wächter entschieden** (P-B7-Design-Runde) — löst
  die vertagten Punkte vom 2026-11-10 auf und ändert den Kaufweg
  des Turm-Sets: Gekauft wird eine **Grundfigur** (Dorfschütze —
  schwacher Allrounder mit Bogen, kämpft selbst), die **am
  stehenden Turm** über das Objekt-Panel in eine von vier
  Richtungen spezialisiert wird; die Richtungen tragen die vier
  bekannten Funktionen (Ranger · Krieger als Rundumschlag im
  Nahkreis · Magier · Armbrustschütze), darüber die drei linearen
  Stufen. Namen weich bis zur Beta-Asset-Runde, Funktionen fest;
  eine zweite Spezialisierungs-Ebene (Elemente, Assassine) ist
  benannte Erweiterung nach dem Semester. Richtwerte: Preisleiter
  50 / 75 / 100 / 150, Kopfgeld rund 20 % des Sende-Preises
  (5 / 10 / 20 / 40). Dazu die Bau-Regel: Türme nur bei gültigem
  Weg — der Weg-Rollback fasst damit nie Türme an. Begründungen in
  `DECISIONS.md`, vier Einträge vom 2026-11-15. Das Kapitel „Türme
  und Upgrades" wird beim G2-Nachzug auf das Grundfigur-Modell
  umgebaut.
- *(2026-11-18)* **Zielbild Menü** (große Design-Runde, Topic 1 von 13):
  Das Menü-System bleibt wie gebaut (MainMenu → Lobby/Join-Code →
  Spiel), kein Umbau geplant. Dazu kommen: Einstiegs-Auswahl
  **Solo/Multiplayer** (beides existiert schon, erwartet werden nur
  minimale Differenzen) · **Settings** (Kandidaten: die drei
  Kamera-Schalter der Polish-Merkliste — Edge-Pan, Freiflug-Grenze,
  Kamera-Dauerfolgen —, später Audio-Lautstärke, dazu Tutorial
  an/aus) · **Credits** als fester Punkt, Inhalt aus `ASSETS.md`
  (bei CC-BY-Assets ist Namensnennung Lizenzpflicht). **Tutorial**
  ist als Tooltip-Reihe gemeint: Panels, die beim ersten Start in
  fester Reihenfolge aufgehen und weggeklickt werden; der Schalter
  schaltet sie ab. Minimal gehalten, ganz am Schluss gebaut, Umfang
  nach Restzeit — es soll nur existieren, der Ausbau kommt später.
  **Rejoin** und das optische Final-Design sind bewusst nach hinten
  geschoben (eher nächstes Semester; Rejoin-Entscheid bleibt beim
  Goldmaster-Stand, `DECISIONS.md` → „Verbindungsverlust");
  Notfall-Regel „Menü bleibt simpel" ist akzeptiert.
- *(2026-11-18)* **Zielbild Game Scene / Welt** (große Design-Runde,
  Topic 2 von 13): Die Welt wird **einmal von Hand gebaut, gebacken,
  fertig** — keine Generierung, kein Placement-Algorithmus (kleine
  Flächen, Einmalaufwand schlägt Werkzeugbau). Je Spieler-Gebiet drei
  Zonen: **Bauregion** (das PathGrid-Raster) · **Wirtschaftsraum**
  (Mine, pendelnde Arbeiter, Sendegebäude) · **Wald** als Rand. Der
  Wald ist eine echte Sperre: Die Bäume bekommen **Collider**, damit
  die Spielfläche abgegrenzt aussieht und niemand hindurchläuft —
  und als Tür für spätere Interaktion. **Fluss-Shader:** eigener,
  wenn Zeit bleibt, sonst Isors vorhandener. **Kamera-Rand:** Terrain
  an den Rändern um ein gutes Stück erweitern statt Nebelwand —
  auflösungs- und seitenverhältnis-unabhängig sieht die Kamera nie
  die Weltkante; die Kamera-Grenzen werden auf den Spielbereich
  geeicht (Settings-Schalter Freiflug-Grenze siehe Polish-Merkliste).
  Asset-Bedarf vorgemerkt für die Optik-Phase: 2–3 Baum-Assets,
  1–2 Gras-Assets, von Hand verstreut. **Offen:** Wald-Placement
  spiegeln/kopieren oder je Gebiet frei verstreuen — wird beim Bauen
  entschieden. Vorgemerkt: Beim Refactor ändern sich Bedeutungen
  einzelner Szenen-Bestandteile (Isors Ansage, Details dort).
- *(2026-11-18)* **Zielbild Spielerfigur & Steuerung** (große
  Design-Runde, Topic 3 von 13): Der Bestand ist bestätigt — Third
  Person mit Top-Down-Diagonale, Befehlsklick statt Direktsteuerung,
  Kamera mit Folgen/Edge-Pan/Freiflug, Nachbarn dauerhaft einsehbar.
  Die Figur **bleibt ein reiner Bauer**: laufen, Wege legen, Türme
  setzen, Panels bedienen — kein Kampf, keine aktiven Fähigkeiten;
  der Refactor braucht an der Spielerfigur keine Kampf-Schnittstellen.
  Benannte Tür nach dem Semester (unsicher, bindet nichts): wählbare
  Figur-Typen/Rassen (z. B. Mensch, Ork) — bis dahin bewusst eine
  einzige Spielfigur. Steuerungselemente wachsen nach Spielgefühl
  (Slot-Tasten-Anzahl offen); die Details gehören in die
  UI-Design-Runde der Polish-Merkliste (vor M4).
- *(2026-11-18)* **Zielbild HUD** (große Design-Runde, Topic 4
  von 13): **Look simpel.** Oben rechts die Ressourcen-Reihe (von
  außen nach innen: Kacheln · Gold · Diamanten); daneben der
  Wave-Timer plus **neu** ein Wellen-Zähler — Monster der Welle
  gesamt/übrig als grober Überblick, gespeist aus dem
  Wellenstart-Schnappschuss des Sende-Pools. Oben links Spieler-Info,
  mindestens der eigene Name. Unten die **runden Werkzeug-Slots**
  mit Shortcuts: Move · Kacheln · Türme · Senden · Abreißen
  (bestätigt den Refactor-Posten Werkzeug-Zustand statt Bools —
  fünf Modi brauchen einen Zustands-Wert). **Panels je Objektart:**
  Kachel-Panel (Bild, Schließen-X, Abriss mit sichtbarer
  70-%-Erstattung) · Basis-Tower-Panel (Bild, Standardtext,
  Spezialisierungs-Buttons mit Tower-Bildern — danach nur noch
  Level Up) · fertiges Tower-Panel (Bild, Werte, Level Up /
  Destroy/Sell, Hover auf Level Up zeigt die Wert-Änderung).
  **Tower-Bild als Live-Kamera:** Render Texture auf einen
  Showroom-Spot in der Welt (Tower-Figuren außerhalb der
  Spielfläche); rendert nur bei offenem Panel, kleine Auflösung —
  Fallback statisches Bild, falls die Zeit kippt. **Offen:**
  Panel-Position (seitlich, mittig oder gemischt) · weitere Inhalte
  oben links · Slot-Anzahl. Sende-Panels beim Topic Senden.
- *(2026-11-18)* **Zielbild Kacheln** (große Design-Runde, Topic 5
  von 13): Der gebaute Bestand ist als Zielbild bestätigt —
  Kachel-Kasse (5 Diamanten, Abriss erstattet 70 %), Halte-Bauen mit
  Geisterbildern, Gültigkeits-Färbung, Rollback beim Wellenstart,
  gesperrte Ein-/Austritts-Zellen, Türme nur bei gültigem Weg. Als
  Design-Aussage fürs GDD bekräftigt: Die Kacheln sind **die freie
  Gestaltungs-Mechanik** des Spiels — der Spieler bestimmt über das
  Weg-Layout, wie die Monster laufen, und baut seine Strategien aus
  Wegführung plus Turm-Platzierung (deckt sich mit der Zweck-Kette
  vom 2026-10-20, die beim G2-Nachzug in den Abgabetext geht). Neu
  dazu nur das Kachel-Panel aus dem HUD-Zielbild (Topic 4).
- *(2026-11-18)* **Zielbild Tower** (große Design-Runde, Topic 6
  von 13 — die vorgemerkte Wächter-Runde ist damit verhandelt):
  Fünf Figuren im Prototyp — Basis (Village Archer, levelt nicht)
  plus vier Spezialisierungen mit je **einem Skill-Profil**: Krieger
  = Rundumschlag im Nahkreis (AOE) · Magier = Verlangsamung ·
  Archer/Ranger = Multischuss (Stufen-Ausbau Richtung Triple) ·
  vierte Richtung = hoher Einzelschaden auf ein Ziel (Name offen,
  „Armbrustschütze" nur Platzhalter — Funktionen fest, Namen weich).
  Stufen verbessern Attribute und ab einer Stufe den Skill selbst
  (AOE größer, Multi → Triple). **Stufenzahl offen** — Kandidat:
  unbegrenzt mit Skalierungs-Formel (Basiswert × Wachstumsfaktor je
  Level für Werte und Preis, getragen von den Steckbrief-Assets);
  ersetzt die „drei linearen Stufen" aus der P-B7-Runde, der
  Abgabetext („drei Stufen je Wächter") zieht beim G2-Nachzug nach.
  Verschiedene Kaufpreise je Richtung (Leiter 50/75/100/150 bleibt
  Richtwert). **Cut fürs Semester:** nur Level Up — Spezialklassen
  als zweite Ebene (Krieger → Warrior/Paladin, Magier →
  Fire/Ice/Storm, Archer → Richtung Assassine) und Kachel-Upgrades
  sind benannte Erweiterung nächstes Semester. **Architektur-Zielbild
  für den Refactor** (löst die vertagte Wächter-Frage vom
  2026-11-15): Basisklasse „Sucher" (Ziel finden, Reichweite,
  Schuss-Takt, Stufen, Panel-Anbindung — bei allen gleich) plus
  austauschbares **Austeil-Verhalten** (Strategy Pattern:
  Einzel · Fläche · Mehrfach · Slow), Werte aus Steckbrief-Assets —
  ein neuer Turm-Typ ist dann ein Asset plus ggf. ein Verhalten,
  kein neuer Turm-Code.
- *(2026-11-18)* **Zielbild Monster** (große Design-Runde, Topic 7
  von 13): Der gebaute Bestand ist bestätigt (Steckbrief-Assets,
  Host-Simulation, Distanzfeld-Lauf). **16 Monster-Typen noch dieses
  Semester** (Isors Entscheid gegen Claudes Vier-bleiben-Empfehlung;
  überschreibt den M4-Inhalt „vier Gegnertypen" — ROADMAP-Nachzug
  beim Sichern): Auswahl offen, Richtung Slimes/Golems/Orks, ggf.
  1–2 Modelle von einem befreundeten Artist (Quellen-/
  Namensnennungs-Eintrag nötig). Normale Monster unterscheiden sich
  über **eigene Steckbrief-Attribute** (viel Leben, schneller …);
  **vier der 16 sind Boss-Monster** mit zusätzlich je einem
  Spezial-Skill, der über das Monster selbst hinauswirkt oder extrem
  ausschlägt (Aura auf Nachbarn, Extrem-Tempo, Extrem-Leben —
  Auswahl offen), dafür deutlich teurer, mehr Einkommens-Wert, mehr
  Kopfgeld. Architektur-Zielbild analog zu den Türmen: Spezial-Skill
  als optionales austauschbares Verhalten am Steckbrief —
  Normal-Monster haben keins, Bosse eins. Income/Preise über eine
  Formel-Kurve statt Handtabelle, kalibriert in den Messrunden
  (P2/M5). **Nächstes Semester** (Richtung offen): Monster-Upgrades
  — einzeln, übers Sendegebäude oder ein zweites Gebäude mit neuen
  Typen.
- *(2026-11-18)* **Zielbild Senden** (große Design-Runde, Topic 8
  von 13): Das System ist als Zielbild bestätigt — Senden immer im
  Uhrzeigersinn, ausgeschiedene Plätze werden übersprungen (sind 1,
  2, 3 im Spiel und 4 raus, sendet 3 an 1), Sende-Pool mit
  Schnappschuss beim Wellenstart, Einkommens-Wert addiert sich beim
  Senden. **Sende-Panel:** Titelzeile (Richtung „Send Monster"),
  Schließen-X, darunter die 16 Monster als **statische Bilder**
  (bewusst keine Live-Renderer — die Kür bleibt dem Tower-Panel);
  Hover auf ein Monster füllt ein Info-Feld: kleines Bild,
  Spezialitäten, Kosten, Income-Gewinn — dieselbe Hover-Logik wie
  die Level-Up-Vorschau im Tower-Panel. Für die UI-Runde vorgemerkt
  (kein Entscheid): 4×4-Raster, Bosse visuell abgesetzt (Form, nicht
  nur Farbe), nicht Leistbares ausgrauen, Klick-Verhalten samt
  Mehrfach-Komfort.
- *(2026-11-18)* **Zielbild Rundentakt & Wellenmodell** (große
  Design-Runde, Topic 9 von 13): Bewusst **kein neuer Entscheid** —
  der gebaute Takt (Rundentakt ohne Bereit-Knopf, kurze Bauphase,
  Karte-leer-Tor, Einkommens-Uhr) ist Arbeitsstand; ob er hält,
  entscheiden die Playtests mit der bestehenden
  Stellschrauben-Reihenfolge aus dem P2-Posten (erst Monster-Tempo /
  Ausschüttungs-Takt / Wegstrecken, Modell-Umbau fester Wellentakt
  nur als letztes Mittel). Konsequenz für den Refactor: Das
  Wellenende-Kriterium bleibt eine **offene Tür** — so bauen, dass
  Karte-leer-Tor gegen festen Takt tauschbar ist, ohne das
  Drumherum anzufassen.
- *(2026-11-18)* **Zielbild Ressourcen** (große Design-Runde,
  Topic 10 von 13): Das Zwei-Währungen-Modell der P-B5v-Runde ist
  als Zielbild bestätigt — **Gold kämpft** (Senden, Türme bauen und
  upgraden; Einkommen steigt durchs Senden und zahlt im Takt aus),
  **Diamanten bauen aus** (aus der Mine über Arbeiter; kaufen
  Arbeiter und Kacheln — hauptsächlich die Upgrade-Währung).
  **Neu:** Das **Income wird im HUD angezeigt**, beim
  Spieler-Info-Bereich oben links (zweiter Inhalt neben dem Namen —
  schließt die offene Stelle aus Topic 4); endgültige Platzierung
  nach Design. **Kacheln** erscheinen in der Ressourcen-Reihe als
  reine Bestandsanzeige (wie viele man hat/setzen kann); gekauft
  wird in der Mine, evtl. zusätzlich ein Schnellkauf-Button — wird
  beim Bauen entschieden. **Nächstes Semester** (offen): Diamanten
  schalten weitere Dinge frei — Kandidaten: extra Sende-Slot/-Area,
  Verbesserung spezieller Monster/Bosse.
- *(2026-11-18)* **Zielbild Mine + Arbeiter** (große Design-Runde,
  Topic 11 von 13): Die Mine ist ein **sichtbares Gebäude** im
  Wirtschaftsraum; die Arbeiter pendeln als sichtbare Figuren
  zwischen Mine und Sendegebäude, und **die Diamanten-Gutschrift
  erfolgt bei Ankunft am Sendegebäude** — die Einkommensrate ergibt
  sich aus Pendelstrecke × Arbeiterzahl, nicht aus einem Timer
  (ersetzt das Tropf-Modell; für den Refactor bleibt die
  Diamanten-Quelle eine austauschbare Komponente). Das Minen-Panel
  trägt die Wirtschafts-Funktionen: Kacheln kaufen, Arbeiter kaufen,
  Arbeiter upgraden, später weitere Upgrades. Dazu als
  system-übergreifender Polish-Posten (später): ein
  **Floating-Text-/Effekt-System** — +Gold beim Monster-Kill,
  +Diamanten bei Arbeiter-Ankunft, Effekte bei Verkauf und
  Level-Up.
- *(2026-11-18)* **Zielbild Solo-Modus** (große Design-Runde,
  Topic 12 von 13): Solo ist **kein eigenes System**, sondern der
  Sonderfall des Sende-Rings — man schickt sich die eigenen Sends
  selbst (Regel „letzter Aktiver sendet an sich selbst" greift
  schon). Dazu zwei Lernhilfen, **beide nur im Solo**: die
  Tutorial-Tooltips aus dem Menü-Zielbild (Panel-Reihe beim
  Einstieg, an-/abschaltbar — präzisiert Topic 1: das Tutorial lebt
  im Solo-Modus) und später **Richtungspfeile**, die anzeigen, in
  welche Richtung die Monster laufen. Im Multiplayer gibt es bewusst
  beides nicht.
- *(2026-11-18)* **Zielbild Endscreen, Leben & Win/Lose** (große
  Design-Runde, Topic 13 von 13): Win/Lose bleibt wie im M3-Plan
  (Leben null → ausgeschieden, letzter Aktiver gewinnt), **aber der
  Endscreen wird schon im Semester die Statistik-Tabelle**: eine
  eigene Endscreen-Szene mit den Werten aller Spieler, die eigene
  Reihe hervorgehoben, je Wert der Beste markiert, Platzierung
  dazu. Werte-Kandidaten (Liste offen): Gesamtspieldauer, höchstes
  Income, höchstes Diamanten-Income, Kacheln gekauft/gesetzt,
  meistgesendete Monster, meiste Kills. **Ablauf:** Ein
  Ausgeschiedener kann zuschauen oder jederzeit gehen (auch per
  Escape → Leave); wer geht, sieht in der Endscreen-Szene den
  Schnappschuss zum Leave-Zeitpunkt (Szenenwechsel = Partie
  verlassen, bewusst einfach). Endet die Partie, kommen alle
  automatisch in die Endscreen-Szene; von dort über die Lobby
  zurück ins Hauptmenü (Fluss-Details offen). **Konsequenz fürs
  Refactor-Zielbild:** eine Statistik-Sammelstelle je Spieler, in
  die die Systeme ihre Ereignisse melden (Kills, Sends, Käufe …) —
  die Zähler laufen ab dem Refactor mit, nicht nachgerüstet.
  **Nächstes Semester** (offen): mehr Werte, Diagramme, evtl.
  Spielerprofil mit Rängen.
