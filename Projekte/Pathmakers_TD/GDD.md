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
