# DECISIONS.md — Entscheidungen Pathmakers TD

Ownership: Nur Entscheidungen zum Spielkonzept Pathmakers TD
(Arbeitstitel; Weg-Bau-Tower-Defense, seit dem 2026-10-20 das
Semester-Spiel des Moduls 5FSC0XD101_P) — was entschieden wurde,
warum, und welche
Alternativen verworfen wurden. Kein Plan (ROADMAP), keine
Design-Absicht (GDD), kein Ereignis. Die Wahl zwischen den
Semester-Konzepten gehört der Uni-Schicht.
Format: `## JJJJ-MM-TT — Titel` mit **Was** / **Warum** / **Verworfen**.
Älteste oben, wie in einer Chronik.

## 2026-10-13 — Eigene Schicht und Arbeitstitel „Isor's Detour"

Was: Die Weg-Bau-TD bekommt eine eigene Projekt-Schicht
`Projekte/Isors_Detour/` mit GDD, DECISIONS und ROADMAP. Arbeitstitel
ist **Isor's Detour**; der Store-Name wird erst vor einem Release
entschieden.
Warum: Das Konzept wird parallel zu Isor's Outbreak bis zum vollen GDD
ausgearbeitet (`Uni/DECISIONS.md` → „2026-10-13 — Zwei Konzepte
parallel bis zur Wahl der Dozentin"); ein eigenes Konzept braucht eine
eigene Schicht (`Kern/DOC_RULES.md`, Abschnitt 10). „Detour" (Umweg)
beschreibt den Kern: Die Spieler bauen den Monstern den Umweg selbst.
Der Name stellt das Spiel in die Reihe „Isor's …".
Verworfen: das Konzept als Variante in der Outbreak-Schicht führen
(zwei Spiele in einer Schicht wären nicht getrennt herausnehmbar).

## 2026-10-16 — Versus mit Income-Senden als Kernmodus

Was: Isor's Detour ist ein Versus-Spiel für bis zu vier Spieler: Jeder
baut nur auf seinem eigenen Gebiet derselben Karte, feste Wellen laufen
bei allen, und mit verdientem Einkommen schicken sich die Spieler
zusätzliche Monster. Solo ist ein Übungsmodus — dieselbe Partie gegen
eine einfache Sende-KI. Team-Varianten (2v2) sind mögliche Erweiterung,
nicht Teil der ersten Version. Gebaut wird von Anfang an
multiplayer-tauglich.
Warum: Den Wiederspielwert erzeugt der Gegner — eine Karte trägt viele
Partien, der Content-Bedarf bleibt klein. Als reines Solo-Spiel hätte
das Konzept nach Isors Einschätzung zu wenig Spielspaß und bräuchte
viel Hand-Content (es müsste eher wie Isle of Arrows gebaut werden).
Die Gebiets-Trennung vermeidet Baukonflikte zwischen Spielern und hält
den Netzwerk-Teil überschaubar; Netzwerk nachträglich einzubauen wäre
teurer, als von Anfang an so zu bauen. Income-Senden ist
Genre-Konvention (Wintermaul Wars als Isors Vorbild, dazu Legion TD),
keine Kopie: Der USP — laufende Figur und der Weg selbst als
Ressource — bleibt eigen.
Verworfen: Koop mit gemeinsamen Leben als Kern (die Wellen müssten
allein fordern — mehr Hand-Content und eine zweite Balancing-Fläche);
beide Modi zugleich (genau die „zu vielen ineinandergreifenden
Systeme" aus dem Dozentinnen-Feedback vom 2026-10-12, `Uni/LOG.md`);
Solo als reiner Festwellen-Modus ohne Sende-KI (ohne Senden übt man
das Kernspiel nicht).

## 2026-10-16 — Gebaut wird über die laufende Figur

Was: Alles Bauen läuft über die Figur in dritter Person: Sie läuft zum
Bauplatz, verlegt Wegkacheln, baut Türme und rüstet sie auf. Kein
Cursor-Bauen aus der Draufsicht.
Warum: Die Figur ist Teil des USP — keines der Vergleichsprodukte
kombiniert laufende Figur, Weg als Ressource und Versus-TD. Dazu Isors
Einschätzung: Über die Figur lassen sich kleine Features und Upgrades
leichter andocken, und das Bausystem bleibt einfacher, weil der Bauort
immer an der Position der Figur hängt.
Verworfen: Bauen per Cursor und Menü ohne Figur — schneller zu bauen,
aber der sichtbare Unterschied zu Wintermaul Wars und Legion TD fiele
weg.

## 2026-10-16 — Arbeitstitel neu: Pathmakers TD

Was: Der Arbeitstitel wechselt von Isor's Detour zu **Pathmakers TD**;
die Schicht heißt jetzt `Projekte/Pathmakers_TD/`. Der Store-Name wird
weiterhin erst vor einem Release entschieden. Löst den Arbeitstitel-Teil
des Eintrags „2026-10-13 — Eigene Schicht und Arbeitstitel ‚Isor's
Detour'" ab; die Schicht-Entscheidung daraus gilt unverändert.
Warum: Der alte Name gefiel Isor nicht (2026-10-16). Der neue trägt
Mechanik und Genre im Namen — die Spieler bauen den Weg selbst — und
legt kein Setting fest, solange das Kapitel „Thema, Aussehen und
Story" noch offen ist.
Verworfen: Waylay, Road to Ruin, Maze Rivals (Claudes weitere
Vorschläge); am alten Namen festhalten.

## 2026-10-16 — Rundentakt und Bauregeln

Was: Eine Partie läuft in Runden. Die Bauphase hat einen festen Timer
(Richtwert ~60 Sekunden; der genaue Wert ist Balancing und fällt im
Test). Danach starten die feste Welle und alle Monster aus den
Sende-Queues bei allen Spielern zugleich; die nächste Bauphase beginnt
erst, wenn die ganze Karte leer ist. Wegkacheln werden nur in der
Bauphase gelegt oder geändert; alles andere — Türme bauen und
aufrüsten, Monster in die Sende-Queue legen — geht jederzeit, auch
während des Kampfes.
Warum: Die Karte-leer-Bedingung garantiert jedem Spieler dieselbe
Bauzeit vor der nächsten Welle (Isors Kernargument). Der eine
synchronisierte Wellenstart ist zudem netzwerkfreundlich. Der feste Weg
während des Kampfes hält die Figur beschäftigt, ohne dass sich der Weg
unter laufenden Monstern ändert — die offene Sackgassen-Frage
schrumpft damit auf den Zustand beim Wellenstart. Vorbild der
Rundenstruktur: Legion TD 2.
Verworfen: durchlaufende Wellen im festen Takt wie in WMW (bestraft
die Laufwege der Figur); Bauen nur in der Bauphase (die Figur stünde
im Kampf nutzlos herum); freies Weg-Ändern auch im Kampf (bräuchte
sofort eine Regel für Monster auf dem geänderten Weg).

## 2026-10-16 — Wirtschaft: Gold, Diamanten, Kacheln

Was: Drei Ressourcen, jede mit genau einer Quelle. **Gold** kommt aus
getöteten Monstern und bezahlt Türme und Upgrades. **Diamanten**
kommen als Einkommen zu Beginn jeder Bauphase; alle starten mit
demselben Betrag. Senden kostet Diamanten und erhöht dauerhaft das
eigene Diamanten-Einkommen; außerdem kaufen Diamanten Arbeiter.
**Kacheln** bauen die Arbeiter laufend in der Mine ab; der Weg ist
ihre einzige Senke. Startwerte (kleiner Kachel-Vorrat, ein Arbeiter)
sind Richtwerte und fallen im Test. Builder-Upgrades sind keine
Diamanten-Senke der ersten Version; sie bleiben als Idee im
GDD-Entwurf.
Warum: Getrennte Systeme mit je einem Regler lassen sich einzeln
balancen (Isors Kernargument). Gegen den Income-Schneeball wirkt ein
eingebautes Gegengewicht: Gesendete Monster werfen beim Verteidiger
Gold ab — Aggression füttert dessen Türme mit. Die Kette Diamanten →
Arbeiter → Kacheln macht den Weg-Ausbau zur Investitionsentscheidung
gegen das Senden.
Verworfen: Kacheln als feste Rundenzuteilung und Senden ohne
Income-Effekt (Claudes Vereinfachungsvorschläge — weniger Systeme,
aber auch weniger Strategie, und nicht Isors Modell); Kacheln direkt
für Diamanten kaufen (die Arbeiter-Kette ist die interessantere
Entscheidung); Abbau durch die Spielfigur selbst (zöge Bauzeit vom
Puzzle ab).

## 2026-10-16 — Turm-Set der ersten Version

Was: Vier Türme, je genau eine Rolle: Pfeilturm (schnelles Einzelziel,
günstig), Kanonenturm (Flächenschaden, langsamer Takt), Frostturm
(verlangsamt im Umkreis, kaum Schaden), Scharfschütze (sehr hoher
Schaden, sehr langsamer Takt, große Reichweite). Upgrades linear in
drei Stufen — mehr Schaden, etwas Reichweite, beim Frost stärkeres
Verlangsamen —, keine Verzweigungen. Fliegende Gegner gibt es in der
ersten Version nicht, damit auch keinen Anti-Luft-Turm. Ob Türme als
Bauwerke oder als Spielfiguren dargestellt werden (wie in WMW), bleibt
offen und entscheidet sich im Thema-Kapitel an der Asset-Lage (GDD →
„Turm-Darstellung").
Warum: Vier Rollen erzeugen Kombinationsspiel (Frost vor
Scharfschütze, Kanone gegen Massen-Sends), bleiben aber klein genug
für Zeit- und Asset-Budget: vier Türme mal drei Stufen sind zwölf
Zustände, über Aufsätze und Farben lösbar statt über eigene Modelle.
Drei spürbare Stufen schlagen zehn unmerkliche. Flieger ignorieren
den Weg und hebeln damit den Kern aus — der Weg ist die Verteidigung.
Verworfen: großes Turm-Sortiment wie in WMW (zu viele Assets, zu viel
Balancing); verzweigte Upgrade-Pfade (benannte Erweiterung statt
Version eins); fliegende Gegner samt Anti-Luft-Turm.

## 2026-10-16 — Gegnertypen der ersten Version

Was: Vier Typen: Normal (Allrounder der festen Wellen), Schnell
(wenig Leben, hohes Tempo), Tank (viel Leben, langsam), Boss (sehr
zäh, mit einer Aura, die die Monster um ihn herum stärkt). Der Boss
läuft nicht in den festen Wellen, sondern kommt nur als Send — um
einiges teurer als alles andere. Die festen Wellen eskalieren pro
Runde über Anzahl und Leben von Normal, Schnell und Tank; das
Sende-Sortiment sind alle vier Typen mit Preisen in Diamanten. Keine
Flieger (siehe „2026-10-16 — Turm-Set der ersten Version").
Warum: Die Typen spiegeln die Turm-Rollen — Masse bestraft fehlende
Fläche, Tank und Boss fehlenden Einzelschaden, Schnelle fehlendes
Verlangsamen; so bleibt kein Turm nutzlos und keine Lücke unbestraft.
Ein Sortiment für Wellen und Sends zugleich halbiert Assets und
Balancing-Fläche.
Verworfen: eigene Send-Einheiten getrennt von den Wellen-Gegnern
(doppelte Assets und doppeltes Balancing); ein eigener Schwarm-Typ
(Masse entsteht schon über die Anzahl normaler Gegner); der Boss als
fester Wellen-Meilenstein, etwa jede fünfte Runde (Claudes Vorschlag —
Isor will den Boss als Druckmittel der Spieler, nicht als
Kalenderereignis).

## 2026-10-16 — Sende-Ziel und Gabelungs-Regel

Was: Niemand wählt sein Sende-Ziel: Die Spieler stehen in einer festen
Reihenfolge, jeder schickt immer an den Nächsten in der Liste.
Scheidet ein Spieler aus, rückt dessen Nachfolger als Ziel nach. An
Gabelungen teilen sich die Monster in der ersten Version strikt
abwechselnd — eines links, eines rechts; eine Zufallsvariante wird
später geprüft.
Warum: Ohne Zielwahl gibt es kein Zusammenrotten gegen den Führenden
und keinen Ziel-Dialog in der Oberfläche — Senden bleibt ein Knopf.
Das Nachrücken hält den Ring geschlossen, solange mehr als ein
Spieler lebt. Die abwechselnde Teilung ist vorhersagbar (der Spieler
kann sein Layout durchrechnen), trivial umzusetzen und im Netzwerk
deterministisch; Zufall würde gute Planung bestrafen und bräuchte
synchronisierte Würfe.
Verworfen: freie Zielwahl beim Senden (Oberflächen-Aufwand und
Gang-up-Dynamik); Gruppenteilung 50:50 (läuft bei ungeraden Zahlen
ohnehin auf Abwechseln hinaus); Zufall an der Gabelung schon in
Version eins (als spätere Ergänzung notiert).

## 2026-10-16 — Siegbedingung: letzter Überlebender

Was: Jeder Spieler hat einen Lebensvorrat (Richtwert 20). Ein Monster,
das sein Ziel erreicht, verschwindet und kostet ein Leben; der Boss
kostet deutlich mehr (Richtwert 5). Bei null Leben scheidet der
Spieler aus, der letzte Überlebende gewinnt. Es gibt keine feste
Partielänge: Die Wellen-Eskalation begrenzt jede Partie von selbst,
Zielwert 15 bis 25 Minuten.
Warum: Das Ausscheiden war in Isors Sende-Ring schon angelegt (das
Nachrücken des Ziels setzt es voraus). Die Eskalation beantwortet die
Dozentinnen-Frage nach der Partielänge, ohne ein eigenes
Punktesystem zu brauchen.
Verworfen: feste Partielänge mit Punktwertung (bräuchte ein
Wertungssystem und nähme dem Ausscheiden die Schärfe).

## 2026-10-16 — Welt-Struktur: eine Karte, vier gleiche Gebiete

Was: Eine zusammenhängende Welt, aufgeteilt in vier Gebiete. Die
Gebiete sind immer gleich groß und funktional identisch (gleiche
Kachelfläche, gleiche Lage von Start- und Endpunkt) und unterscheiden
sich nur kosmetisch leicht. Jeder Spieler baut und bewegt sich nur in
seinem Gebiet; die Monster laufen vom festen Startpunkt des Gebiets
zu dessen Endpunkt. Bei weniger als vier Spielern bleiben die
übrigen Gebiete leer; die Karte ändert ihre Größe nicht. Die
Gebietsgröße in Kachelplätzen fällt im Prototyp.
Warum: Funktional identische Gebiete sind im Versus Pflicht, sonst
entscheidet die Karte statt der Spieler. Eine gemeinsame Welt statt
getrennter Platten lässt die Spieler die Nachbarn sehen — man sieht
die eigene gesendete Welle drüben ankommen, das trägt die
Schadenfreude des Sendens. Die feste Größe hält das Balancing
unabhängig von der Spielerzahl; die offene Spielfeldgröße-Frage ist
damit beantwortet.
Verworfen: vier getrennte Platten (nimmt dem Versus die
Sichtbarkeit); ein Feld, das mit der Spielerzahl wächst (verändert
das Balancing je Besetzung).

## 2026-10-16 — Kamera und Bausystem

Was: Zwei Kamera-Zustände: Beim Laufen hängt die Kamera an der Figur
(dritte Person, schräg von oben); daneben ein freier Blick, der sich
mit der Maus über das eigene Gebiet bewegen lässt. Gebaut wird per
Geisterbild: Ein halbtransparentes Vorschaubild hängt an der Maus,
der Linksklick bestätigt, und die Figur läuft selbst zur Baustelle
und baut dort. Übergänge, Zoom und Feinverhalten fallen im Prototyp.
Warum: Die Folgekamera trägt das Körperliche der Figur, der freie
Blick das Puzzle — aus der Schulterperspektive plant sich kein
Layout (Isors Modell; Vorbild fürs Geisterbild: WMW). Der
Hinlauf-Zwang hält die Laufwege als Spielelement am Leben, obwohl
mit der Maus gezielt wird: Zielen ist bequem, Bauen bleibt
Wegstrecke.
Verworfen: nur eine Folgekamera (die Übersicht fürs Planen fehlt);
Bauen am Standort der Figur ohne Maus-Vorschau (präzise, aber zäh);
Sofort-Bau an der Mausposition ohne Hinlaufen (entwertete die
Figur).

## 2026-10-16 — Persistenz: jede Partie für sich

Was: Zwischen den Partien bleibt nichts außer den Einstellungen.
Keine Freischaltungen, kein Spielerfortschritt, kein Inventar, keine
Charakterwerte; laufende Partien werden nicht gespeichert.
Freischaltbares (neue Türme, Skins, Statistiken) ist eine benannte
Erweiterung, falls nach der Alpha Luft ist.
Warum: Hält den Umfang klein (Dozentinnen-Feedback vom 2026-10-12:
Qualität vor Umfang) und beantwortet die Prüflisten-Fragen nach
Inventar und Stats als bewussten Ausschluss statt als Lücke.
Verworfen: Meta-Fortschritt schon in der ersten Version (ein zweites
Speichersystem und eine weitere Balancing-Fläche ohne Gewinn für den
Kern).

## 2026-10-16 — Oberfläche: Sende-Gebäude, Aktionsleiste, verdeckte Sends

Was: Jedes Gebiet hat einen Wirtschaftsbereich nach
Legion-TD-Vorbild: Dort stehen die Mine mit den Arbeitern und das
Sende-Gebäude, und beides wird jederzeit direkt per Mausklick
bedient — kein Hinlaufen. Am Sende-Gebäude stehen die vier Monster
mit ihren Diamanten-Preisen, an der Mine werden Arbeiter gekauft;
die Spielfigur ist allein fürs Bauen von Wegen und Türmen
zuständig. Die Figur hat unten eine Aktionsleiste; ob als sichtbare
Quick-Slots (Isors Favorit, im Outbreak-GDD schon erprobt), als
Befehlsfeld nach WMW-Art oder als Radialmenü, entscheidet der
Prototyp. Eingehende Sends werden nicht angezeigt: Was ein Gegner
geschickt hat, sieht man erst, wenn es mit dem Wellenstart
losläuft. Der Rest des HUD: Ressourcen samt Einkommen,
Rundenanzeige mit Timer und Bereit-Knopf, Turm-Feld mit
Aufrüst-Knopf, Lebensstände aller Spieler; Menüfolge Hauptmenü →
Lobby mit Join-Code → Endbildschirm mit Platzierung.
Warum: Klare Rollentrennung — die Wirtschaft (Senden, Arbeiter) ist
Management und läuft per Maus, das Bauen bleibt das körperliche
Spiel der Figur. Senden muss jederzeit sofort gehen, gerade mitten
im Kampf; ein Hinlauf-Zwang stünde dem im Weg. Verdeckte Sends
halten die Spannung hoch (Isor).
Verworfen: Sende-Leiste im HUD (Claudes Vorschlag — das Gebäude
verortet die Wirtschaft sichtbar in der Welt); Hinlaufen zum
Sende-Gebäude (Claudes Lesart — zäh und im Kampf unpraktisch);
Anzeige der eingehenden Sende-Queue (nähme die Überraschung).

## 2026-10-17 — Wellenmodell: nur Sends, keine automatischen Wellen

Was: Es gibt keine automatischen Wellen. Die Welle, die bei Timer null
startet, besteht ausschließlich aus den Monstern, die die Gegner per
Send in die Queue gelegt haben. Löst die Festwellen-Teile der Einträge
„2026-10-16 — Versus mit Income-Senden als Kernmodus", „2026-10-16 —
Rundentakt und Bauregeln" und „2026-10-16 — Gegnertypen der ersten
Version" ab; Rundenstruktur (Karte-leer-Tor), Sende-Ring und Typen-Set
gelten unverändert.
Warum: So war das Spiel von Isor von Anfang an gemeint (Wintermaul
Wars als Haupt-Vorbild); das Festwellen-Modell stand als
Missverständnis im GDD und fiel beim gemeinsamen Kapitel-Durchgang
auf. Ohne automatische Wellen gibt es nur eine Monster-Quelle und eine
Balancing-Fläche — Druck, Eskalation und Partie-Ende kommen aus dem
Einkommens-Wettrüsten der Spieler selbst.
Verworfen: feste Wellen plus Sends (Legion-TD-Modell — stand im GDD,
war nie Isors Absicht); eine kleine automatische Grundwelle als
Druckquelle (verwässerte das reine Send-Modell).

## 2026-10-17 — Stillstand wird wirtschaftlich bestraft, nicht per Regel

Was: Schickt niemand, passiert nichts — die Karte ist bei Timer null
sofort leer, die nächste Bauphase beginnt direkt. Es gibt keine
Zwangsregel gegen Passivität. Dafür neu: ein Gold-Startvorrat neben
dem Diamanten-Vorrat, damit die ersten Türme vor dem ersten Send
stehen; beide Startwerte fallen im Spieltest.
Warum: Wer nie schickt, baut kein Einkommen auf und verliert das
Wettrüsten — Passivität bestraft sich selbst, eine Regel wäre doppelt.
Ohne Gold-Startvorrat träfe ein Früh-Rush auf ein turmloses Gebiet,
weil Gold sonst nur aus Kills kommt.
Verworfen: eine Mindest-Send-Pflicht (Regelballast); eine automatische
Grundwelle (siehe „Wellenmodell: nur Sends").

## 2026-10-17 — Einkommen: fester Wert je Monstertyp, ein Timer

Was: Das Grundeinkommen ist null. Jeder Monstertyp trägt neben dem
Preis einen festen Einkommens-Wert, der sich beim Senden dauerhaft
aufaddiert. Ausgezahlt wird bei Timer null, im selben Moment wie der
Wellenstart; es gibt genau einen Timer. Monster haben feste Werte —
die Eskalation kommt allein aus dem Wettrüsten, stärkere Varianten
sind benannte Erweiterung. Löst die Auszahlung „zu Beginn jeder
Bauphase" aus „2026-10-16 — Wirtschaft: Gold, Diamanten, Kacheln" ab.
Warum: Isors Modell aus der WMW/Legion-Tradition; Legion TD bestätigt
das dauerhafte Einkommen je Send (Recherche 2026-10-17). Ein Timer
heißt ein scharfer Moment pro Runde und eine Uhr im HUD; Ansparen und
Wellen-Aussetzen funktionieren darin bereits, weil die Auszahlung am
Timer hängt, nicht am eigenen Send.
Verworfen: ein separater, freilaufender Income-Timer (Isors Idee, nach
gemeinsamer Abwägung zurückgezogen — zwei Uhren, und lange
Kampfphasen würden zu Income-Farmen); Auszahlung zu Beginn der
Bauphase (das andere Ende derselben Phase, aber gegen die Konvention
der Vorbilder und ohne eigenen Vorteil).

## 2026-10-17 — Solo: Sandbox mit Selbst-Senden, ohne Sieg

Was: Wer allein spielt, startet dieselbe Partie als Sandbox: Gesendete
Monster kommen ins eigene Gebiet, die Sende-KI entfällt. Solo kann man
nicht gewinnen — die Partie läuft endlos, bis die Leben aufgebraucht
sind; der Endbildschirm zeigt die erreichte Runde statt der
Platzierung. Löst den Solo-Teil („Übungsmodus gegen eine einfache
Sende-KI") aus „2026-10-16 — Versus mit Income-Senden als Kernmodus"
ab.
Warum: Selbst-Senden hält die komplette Send-Mechanik solo erlebbar
(Queue, Income, Timing) und macht den Modus zum Testfeld für Builds
(Isors Idee). Im reinen Send-Modell wäre eine KI zudem die einzige
Monster-Quelle — sie zu bauen stünde in keinem Verhältnis zum Zweck.
Einfach halten (Isor).
Verworfen: die Sende-KI (ein Baustein mehr, deckt den Testzweck
schlechter); eine Solo-Siegbedingung (bräuchte künstliche
Wellenziele, die es ohne automatische Wellen nicht gibt).

## 2026-10-17 — Weg: Standardweg ab Start, Zusammenhang, gerade Linie

Was: Zu Partiebeginn liegt in jedem Gebiet ein vorgegebener
Standardweg vom Start- zum Endpunkt; auch dessen Kacheln dürfen
abgebaut und versetzt werden. Als Weg zählt nur, was zusammenhängend
am Startpunkt beginnt — Kacheln ohne Verbindung sind Vorrat auf dem
Feld. Endet der Weg vor dem Ziel, laufen Monster vom Wegende in
gerader Linie zum Endpunkt. Die Kachel-Sperre hängt nicht mehr an der
Bauphase, sondern am eigenen Gebiet: Verlegt wird, solange dort keine
Monster unterwegs sind — wer früh leerkämpft, erspielt sich Bauzeit.
Schließt die offene Sackgassen-Frage; löst „Wegkacheln nur in der
Bauphase" aus „2026-10-16 — Rundentakt und Bauregeln" ab.
Warum: Der vorverlegte Standardweg gibt Runde eins einen vollständigen
Weg und neuen Spielern ein funktionierendes Vorbild — ohne eigene
Logik, denn er besteht aus denselben Kacheln wie alles andere (Isors
Idee, von der Prioritäts-Variante auf vorverlegte Kacheln
vereinfacht). Die gerade Linie bestraft sich selbst (kurzer Weg heißt
weniger Beschuss) und braucht deshalb weder Ausnahmen noch Zwang; die
Zusammenhang-Regel macht eindeutig, was die Monster nehmen. Die neue
Kachel-Sperre macht aus dem Warten auf den Langsamsten eine Belohnung
und kollidiert mit nichts, weil nach dem eigenen Rundenende nichts
Neues ins Gebiet kommt (Sends starten erst mit dem Wellenstart).
Verworfen: der Standardweg als eigene Wegfindung mit priorisierten
Spieler-Kacheln (Isors Vorbehalt: Trick-Gefahr, dazu doppelte Logik);
Monster warten am unfertigen Wegende (ein nie fertiger Weg würde
Monster blockieren — Exploit); lose Kachel-Inseln als Weg (nicht
definiert, welche die Monster nehmen).

## 2026-10-17 — Türme nie auf Kacheln; Sende-Ring im Uhrzeigersinn

Was: Türme stehen nie auf Wegkacheln, nur auf der freien Fläche
daneben. Die feste Sende-Reihenfolge folgt der Anordnung der Gebiete
im Uhrzeigersinn.
Warum: Türme auf dem Weg vermengten Weg-Bau und Turm-Bau und
belasteten die Wegfolge-Logik. Der Uhrzeigersinn macht den „Nächsten
in der Liste" auf der Karte ablesbar — das Sende-Ziel ist immer ein
sichtbarer Nachbar, die eigene Welle kommt in Sichtweite an.
Verworfen: Türme auf Kacheln als Blockade-Mechanik (ein anderes
Spiel); eine zufällige Ring-Reihenfolge (nicht ablesbar).

## 2026-10-17 — Boss-Aura bleibt bewusst ein Spieltest-Regler

Was: Der Boss trägt eine Aura, die Monster um ihn herum beeinflusst;
ob sie zäher oder schneller macht, entscheidet der Spieltest. Im GDD
als geplanter Regler formuliert, nicht als offene Frage.
Warum: Isor will die Wirkung nicht festlegen, bevor sie spielbar ist;
die Regler-Formulierung beantwortet die Prüfliste trotzdem als
Entscheidung.
Verworfen: die jetzige Festlegung auf „weniger Schaden in der Aura"
(Claudes Vorschlag).

## 2026-10-17 — Thema: stilisiert und entspannt, Wächter, keine Story

Was: Freundliche Fantasy-Welt, stilisierter Cartoon-Look mit
Toon-Shading, an Anime-Looks wie Genshin Impact angelehnt; der Ton ist
entspannt und beruhigend. Türme sind Spielfiguren („Wächter"), keine
Bauwerke — die offene Turm-Darstellung aus „2026-10-16 — Turm-Set der
ersten Version" ist damit entschieden. Eine Story gibt es bewusst
nicht. Der eigene Toon-Shader bleibt Absicht im GDD-Entwurf, steht
aber nicht als Zusage im Abgabetext (Isor noch unsicher);
Asset-Kandidaten (alle frei) sind im Entwurf datiert notiert.
Warum: Stilisiert wie Isors übrige Spiele (Wiedererkennung im
Portfolio), die beste freie Asset-Lage, und Figuren-Packs mit
Animationen gibt es frei (Quaternius CC0, Bug Knight TD Pack) — die
Asset-Lage trägt die Figuren-Entscheidung. „Bewusst keine Story"
beantwortet die Prüflisten-Frage als Entscheidung: Das Genre trägt
ohne Hintergrundgeschichte (Isor).
Verworfen: ein Story-Rahmen „Wettstreit der Wegmacher" (Claudes
Vorschlag — unnötig); ein echter Anime-Charakter-Look aus
Kauf-Assets (Kaufschwelle, freie Lage dünn); Türme als Bauwerke
(Figuren-Packs sind größer in der Auswahl und lebendiger).

## 2026-10-17 — Restkapitel spiegeln den Aufbau des Outbreak-GDDs

Was: Zeitplan (Meilensteine ohne Kalenderdaten), Technische Daten,
Entwicklungsumgebung und Vorgehensweise/Qualitätssicherung folgen
bewusst Aufbau und Ton der entsprechenden Outbreak-Kapitel; die vier
Messlatten aus dem Freigabe-Feedback (klarer Fokus,
Gameplay-Feedback, einheitlicher Stil, passender Sound) stehen
wörtlich in der Vorgehensweise.
Warum: Die Dozentin vergleicht zwei Dokumente — gleiche Struktur
macht die Wahl zum Inhaltsvergleich statt zum Formatvergleich, und
die erprobte Netz-Grundlage samt Werkzeugkette ist tatsächlich
dieselbe.
Verworfen: ein eigener Aufbau je Dokument (Mehraufwand ohne Nutzen
für die Wahl).

## 2026-10-20 — Prototyp von Anfang an im Netz

Was: Der Spieleprototyp (Abgabe 27.11., `Uni/Semester_3/STUNDENPLAN.md`)
wird von Beginn an als Multiplayer gebaut: Übernommen wird die erprobte
Its-DOT-Grundlage — NGO mit Relay und Join-Code, Lobby, Menü-Kette —,
und die Spielerfigur entsteht als Owner-Movement nach dem fertigen
B1-Movement-Design (`Projekte/Its_DOT/DECISIONS.md`, Einträge vom
2026-10-18/19). Konkretisiert fürs Prototyp-Vorgehen, was „2026-10-16 —
Versus mit Income-Senden als Kernmodus" mit „von Anfang an
multiplayer-tauglich" schon festhielt.
Warum: Multiplayer ist Isors erklärtes Lernziel — seine Spiele sollen
Multiplayer werden —, und der Prototyp ist laut Aufgabe der Ort zum
Ausprobieren. Die erprobte Basis macht den Aufpreis klein; Movement und
Bauen nachträglich netzfähig zu machen wäre genau das technische
Risiko, vor dem der Aufgabentext warnt („kreative Risiken ja,
technische Risiken nein" — `Uni/Semester_3/VORJAHR_AUFGABEN.md` →
„3 · Spieleprototyp").
Verworfen: erst solo bauen und das Netz vor der Alpha nachrüsten
(schneller am ersten fühlbaren Weg-Bau, und die Solo-Sandbox wäre als
Abgabe zulässig — aber Umbau-Risiko, und der Wettrüst-Test mit echten
Mitspielern fehlte im Erkenntnis-PDF).

## 2026-10-20 — Prototyp-Schnitt: Isors Reihenfolge, Wächter spät

Was: Der Prototyp wird in Bausteine geschnitten (P-B1 Fundament im
Netz bis P-B8 Mine; Liste und Schätzungen in der ROADMAP → „Prototyp —
Bausteine"). Die Reihenfolge ist Isors Entwurf: Figur, Weg-Bau, Karte,
Gegner, Takt und Senden, Ressourcen; der erste Wächter bewusst erst
als P-B7, die Mine als Streichkandidat zuletzt. Fester Prüfpunkt nach
P-B4: Liegt der Stand hinter der Schätzung, wird das Vorziehen des
Wächters besprochen.
Warum: Reihenfolge und Schätzungen stammen von Isor; die Schätzungen
tragen bewusst einen Multiplayer-Aufschlag (Beleg: die ehrliche
B1-Nachschätzung bei It's D.O.T). Der Turm ist nach Isors Einschätzung
ein eigener, risikoarmer Baukasten, der die Systeme davor braucht, um
richtig benutzbar und sichtbar zu sein. Der benannte Preis: Der
Spaß-Test — Weg-Länge gegen Feuerkraft, das Testziel des Prototyps —
wird erst mit P-B7 möglich; dafür steht der Prüfpunkt. P-B1 bis P-B7
füllen mit ~55–64 h das Bau-Budget bis zum 27.11. komplett, deshalb
ist die Mine faktisch Alpha-Material (Notlösung: Kachel-Kauf-Knopf),
und Playtests samt Erkenntnis-PDF bekommen fest die letzte Woche.
Verworfen: den Wächter direkt nach dem Gegner-Baustein ziehen (Claudes
Vorschlag — der Spaß-Test käme früher, aber gegen Isors
Baukasten-Argument); die Mine als Pflichtteil des Prototyps.

## 2026-10-20 — Projekt-Start: frisches Repo, gezielte Übernahme

Was: Neues Repo `Pathmakers-TD` mit frischem Unity-Projekt
`PathmakersTD`; in `Kern/PFADE.md` kommt dafür die Marke
`PROJEKT_PATHMAKERS`. Die Netz- und Menü-Teile werden gezielt aus dem
Its-DOT-Projekt übernommen, das Projekt wird nicht kopiert.
Warum: Namens-Muster wie `Its-DOT`/`ItsDOT`; die gezielte Übernahme
ist der am 2026-10-17 erprobte Weg (MainMenu-Migration, Its-DOT) und
schleppt keine Outbreak-Reste mit (Testarea, Movement-Rohbau).
Verworfen: das Its-DOT-Projekt als Kopie weiterführen (schneller am
Start, aber toter Bestand im Semester-Repo).

## 2026-10-21 — Steuerung: Befehlsklick statt Direktsteuerung

Was: Die Spielerfigur wird per Befehlsklick gesteuert
(Warcraft-3-Modell): Rechtsklick aufs Feld setzt das Laufziel, die
Figur läuft selbst hin; WASD bewegt die freie Kamera, eine
Rückfokus-Taste holt sie zur Figur (Taste und Kamera-Details fallen in
der Design-Runde). Bewegung über Unitys NavMeshAgent; kein Sprung,
kein Sprint — nur Beschleunigen und Bremsen, ein Tempo-Upgrade bleibt
benannte Erweiterung. Löst die Direktsteuerung („Figur läuft per
Tastatur") und die Folgekamera aus „2026-10-16 — Kamera und
Bausystem" ab; Geisterbild-Bauen per Linksklick, Hinlauf-Zwang und
der freie Planungs-Blick gelten unverändert.
Warum: Das Steuerungs-Kapitel hatte Isors Absicht nie getroffen — wie
beim Wellenmodell stand ein Missverständnis im GDD und fiel beim
Baustein-Design auf (Isor: „ich habe gemeint, dass wir Modell B schon
immer machen"). Direktsteuerung fühlt sich mit der schrägen
Draufsicht nach Isors Einschätzung schlecht an, und die Maus gehört
dem Bauen. NavMeshAgent statt Eigenbau: simpel und effektiv (Isor),
weicht Gebäuden von Haus aus aus, der Aufgabentext erlaubt im
Prototyp ausdrücklich zweckdienliche Werkzeuge
(`Uni/Semester_3/VORJAHR_AUFGABEN.md` → „3 · Spieleprototyp"), und
der Pathfinding-Unterricht folgt am 17.12. ohnehin.
Verworfen: die dokumentierte Direktsteuerung per WASD samt
Folgekamera (Modell A — kollidiert mit der Bau-Maus und dem
Kamera-Gefühl der Draufsicht); ein eigener Klick-Motor ohne NavMesh
(spart nichts und verliert das Ausweichen); das
Rigidbody-Movement-Design aus Its-DOT B1 (für Physik-Slapstick
begründet, den Pathmakers nicht hat — übernommen wird nur die
Schichten-Trennung Input/Befehl/Bewegung).

## 2026-10-21 — Spielerfigur V1: Klick-Befehl, Agent-Werte, Marker

Was: Der Laufbefehl ist ein Strahl von der Kamera durch den
Mauszeiger auf den Ground-Layer; nur ein Boden-Treffer wird zum Ziel,
ungültige Klicks verpuffen still, über der Oberfläche blockt das
EventSystem den Befehl. Rechtsklick-Halten zieht das Ziel gedrosselt
nach — gleich in V1. Am Treffer blitzt ein Klick-Ring auf (V1). Die
Agent-Werte leben direkt am NavMeshAgent im Inspector; Startwerte
speed 5, acceleration 16, angularSpeed 720, stoppingDistance 0,1,
autoBraking an. Im Befehls-Code sitzt von Anfang an die Prüfung „ist
dieses Ziel erlaubt?", die in V1 immer ja sagt — die Gebietsgrenze
selbst fällt in P-B3 (Richtung: Befehls-Filter plus Grenz-Collider,
NavMesh-Areas nur bei Pfad-Ausreißern).
Warum: Das Warcraft-Verhalten hält den Code klein, weil nur gültige
Treffer überhaupt Befehle werden; Halten und Marker sind Komfort mit
kleinem Preis (Isors Abwägung: lieber gleich fertig). Werte am
Agenten statt gespiegelt: ein Besitzer je Zahl, und Tuning im
Play-Mode wirkt sofort — Isors Spiegel-Sorge beruhte auf der
Verwechslung von NavMesh (geteilte Fläche) und Agent
(Instanz-Komponente je Figur). Ein Sammel-SO nach dem
Awake-Seed-Muster kommt, sobald der erste Nicht-Agent-Wert auftaucht.
Verworfen: Fehlerton oder Meldung bei ungültigem Klick (Rauschen);
das Spiegeln der Agent-Werte im Player-Skript (zweiter Besitzer
derselben Zahl, dazu die stille Laufzeit-Falle der Awake-Kopie); die
Grenz-Technik schon in V1 (im Gym gibt es keine Gebiete).

## 2026-10-21 — Kamera V1: fester Blick, Komfort mit Schaltern

Was: Eigenes Kamera-Skript (StrategyCamera): fester Blickwinkel ~55°
nach unten, Starthöhe 14 m, keine Drehung. WASD schiebt parallel zum
Boden, das Mausrad zoomt die Höhe zwischen Min und Max, die Leertaste
springt beim Tippen zur eigenen Figur und klebt an ihr, solange sie
gehalten wird. Freiflug-Grenze und Edge-Pan sind gleich eingebaut,
beide mit An/Aus-Schalter im Inspector, Start: aus.
Warum: Der feste Blick hält das Layout lesbar (WC3-Vorbild), und die
Maus dreht die Kamera nicht, weil sie dem Bauen gehört. Die Schalter
sind Isors Settings-Vorsorge — heute Inspector-Haken, später die
fertigen Andockstellen fürs Einstellungs-Menü; Edge-Pan bleibt beim
Editor-Testen aus, weil die Kamera sonst wegläuft, sobald die Maus
Richtung Inspector wandert. Bewusster Budget-Aufschlag von rund einer
Stunde für vier kleine Komfort-Teile (Isor).
Verworfen: Cinemachine (Blackbox — dieselbe Linie wie in der
B1-Runde); eine Orbit-Kamera mit Maus-Drehung (kollidiert mit der
Bau-Maus); den Komfort auf die Ausbauliste schieben (Isor: jedes
Teil ist unter einer halben Stunde, und dann ist es fertig).

## 2026-10-21 — Figur im Netz und Skript-Zuschnitt

Was: Gespawnt wird über einen PlayerSpawner in der Spielszene nach
dem LobbyPlayerSpawner-Muster — der Host erzeugt je verbundenem
Client eine Figur am Spawn-Punkt und übergibt die Ownership; das
PlayerPrefab-Feld am NetworkManager bleibt leer. Owner-Weiche in
OnNetworkSpawn: ClickCommandInput und NavMeshAgent laufen nur beim
Owner, Fremde bekommen die Position über das NetworkTransform mit
Owner-Autorität; die Kamera ist rein lokal. Skripte: PlayerMotor
(kapselt den Agent, MoveTo), ClickCommandInput und ClickMarker unter
Scripts/Player/, StrategyCamera unter Scripts/CameraControl/,
PlayerSpawner unter Scripts/NetWorking/, Prefab Player unter
Prefabs/Player/. Eingaben laufen über die neue Action-Map „Gameplay"
(Command, CameraMove, CameraZoom, FocusPlayer). Bau-Reihenfolge:
NavMesh und Prefab-Rohbau → Spawner und Netz-Gerüst → Motor und
Klick-Befehl → Kamera → Marker und Komfort → Netz-Test mit zwei
Instanzen.
Warum: Auto-Spawn über das PlayerPrefab-Feld stellte die Figur schon
in die Lobby; das Spawner-Muster ist erprobt, und Isor kennt es aus
dem eigenen Code. Die Schichten-Trennung Input → Befehl → Bewegung
ist die übernommene Versicherung aus dem B1-Design, falls der
Unterbau je wechselt. Die Action-Map ist die Controller-Vorsorge:
Support ist Polish-Ziel — später kommen Bindings dazu statt
Code-Umbau (Isor: ohne Support drohen Minuspunkte, und manche
Eingaben brauchen je Gerät eigene Lösungen).
Verworfen: der NGO-Auto-Spawn über das PlayerPrefab-Feld; harte
Tasten-Abfragen statt Actions; Sprint- oder Dash-Felder auf Vorrat
(das Tempo-Upgrade ist später genau ein Agent-Feld).

## 2026-10-23 — Kacheln als Objekte auf flachem Baubereich

Was: Der Baubereich jedes Gebiets ist flach; Hügel sind Kulisse
außenrum und gehören zum Karten-Blockout (ROADMAP → „P-B3 · Karte +
Spawns"). Jede Wegkachel ist ein eigenes flaches Prefab mit echter
Dicke (Richtwert 5–10 cm), die Oberseite liegt leicht über dem Boden.
Das Prefab wird bei einem Meter Kantenlänge gebaut; der Grid-Manager
skaliert es beim Erzeugen auf die Zellgröße. Die Belegung lebt als
Tabelle im Grid-Manager — die Kachel-Objekte sind reine Optik, die
Daten sind die Wahrheit.
Warum: Auf flachem Boden ist das Raster reine Mathematik (Mausstrahl
auf den Boden, Zellindex aus X und Z, konstante Höhe) — kein
Anschmiegen, kein schiefes Geisterbild. Kacheln als Objekte tragen
alles, was das GDD verlangt: das Geisterbild (dasselbe Prefab,
halbtransparent), die lose Vorratskachel auf dem Feld (ein Anstrich
kann kein Ding sein), den Abbau und die Asset-Pläne (Kenney-Kacheln
sind Meshes). Die Dicke verhindert Z-Fighting zweier deckungsgleicher
Flächen. Die Trennung Daten gegen Optik hält das Netz klein (nur
Zellindizes reisen) und gibt der Wegfolge in P-B4 eine Tabelle statt
Objekte; einige hundert simple Platten-Meshes sind für Unity
unkritisch.
Verworfen: der Weg als Textur oder Splatmap im Boden (Laufzeit-Malen
ist Shader-Territorium, lose Kacheln und Geisterbild passen nicht ins
Modell, fertige Kachel-Assets blieben ungenutzt); papierdünne Flächen
exakt auf Bodenhöhe (Z-Fighting); unebener Baubereich.

## 2026-10-23 — Bau-Erlebnis: Kategorie-Leiste und Objekt-Panel

Was: Die Aktionsleiste der Figur ist eine Quick-Slot-Leiste mit
Kategorien statt Produkten — zwei Slots auf Dauer: Kacheln und Wächter
(ab P-B7). Die Slots entstehen datengetrieben aus einer
Kategorie-Liste, tragen Zifferntasten, Esc oder Rechtsklick verlässt
den Bau-Modus. Bauen: Slot wählen → Geisterbild snappt aufs Raster →
Linksklick erteilt den Auftrag, Shift-Klicks hängen weitere an;
ausstehende Aufträge bleiben als nummerierte Geisterbilder stehen, die
Figur arbeitet sie in Bestell-Reihenfolge ab und baut in V1 sofort bei
Ankunft (eine Bauzeit je Kachel bleibt vorgemerkter Tuning-Regler).
Verwalten: Klick auf ein liegendes Objekt öffnet dessen Panel — bei
Kacheln „Abbauen" (sofort, ohne Hinlauf, Vorrat plus eins), später
Aufrüsten und die Wächter-Wahl am gebauten Platz (Sockel-Muster).
Panel-Form am Platz und Preisaufteilung entscheidet die
P-B7-Design-Runde. Entscheidet die offene Leisten-Frage aus
„2026-10-16 — Oberfläche: Sende-Gebäude, Aktionsleiste, verdeckte
Sends" (Quick-Slots); Geisterbild und Hinlauf-Zwang aus „2026-10-16 —
Kamera und Bausystem" gelten fürs Legen unverändert.
Warum: Die häufigste Aktion des Spiels ist das Weg-Legen — Slot plus
Shift-Reihe kostet für einen Weg von 40 Kacheln rund 41 Handgriffe,
ein Kontextmenü am Feld über 80 (Isors eigener Modell-Vergleich,
Claudes Rechnung). Kategorien statt Produkte lösen Isors
Skalierungs-Sorge: Die Leiste wächst nie, die Auswahl wandert in das
Objekt-Panel, das fürs Abbauen und Aufrüsten ohnehin entsteht — ein
Muster für alles Liegende, zugleich das Vorbild aus Wintermaul Wars
(Basis bauen, am Gebäude spezialisieren). Abbauen ohne Hinlauf ist
Isors Entscheidung und konsequent: Verwalten ist Fernbedienung wie
Mine und Sende-Gebäude, der Hinlauf ist der Preis fürs Erschaffen.
Mausrad-Slotwechsel kollidiert mit dem Kamera-Zoom; der Controller
läuft später über die Action-Map (eine Rad-Darstellung der Slots
bleibt dort denkbar).
Verworfen: ein Kreismenü per Linksklick aufs Feld als Bau-Einstieg
(Isors zweites Modell — fürs Massen-Legen doppelt so teuer und kippte
die Geisterbild-Entscheidung); ein Slot je Produkt (skaliert nicht,
Isors eigener Einwand); Abbauen mit Hinlauf (Claudes
Konsistenz-Vorschlag — Isor: im Panel wegmachen ist schöner;
Playtest-Merkposten in ROADMAP → „P2 · Playtests und Erkenntnis-PDF");
Mausrad zum Slot-Blättern.

## 2026-10-23 — Raster: Zellgröße als Wert, Rig als Prefab

Was: Die Zellgröße (Startwert 2 m) ist ein serialisiertes Feld am
Grid-Manager — genau ein Besitzer, jeder Verbraucher fragt ihn. Das
ganze Weg-Bau-System ist ein Prefab („Rig"): Grid-Manager mit
Start-Marker als Kind und Kachel-Prefab als Referenz; die
Welt-zu-Zelle-Rechnung zieht die eigene Transform-Position ab, Breite
und Höhe der Rasterfläche in Zellen stehen im Inspector. Testarea:
eine Instanz, frei hingestellt; echte Karte (P-B3): vier Instanzen, je
Gebiet eine. Ungültig in P-B2: belegte Zelle, außerhalb der Fläche,
Vorrat null — das Geisterbild färbt um, der Klick verpufft still;
keine Reichweiten-Grenze, weit bestellen bestraft der Hinlauf von
selbst. Verbundene und lose Kacheln sehen in V1 gleich aus (Isor); die
Zusammenhang-Prüfung ab dem Start-Marker läuft trotzdem und zeigt sich
nur als Editor-Gizmo. Die Farbwahl gültig/ungültig fällt am echten
Bild — nie Rot gegen Grün, und ein zweiter Träger (Form oder Symbol)
ist Pflicht nach dem Barrierefreiheits-Absatz des GDD.
Warum: Der Inspector-Wert ist Isors Tuning-Linie aus P-B1 (Werte am
Besitzer, Live-Drehen im Play-Mode); das Kachel-Prefab bei einem Meter
plus Skalierung durch den Manager hält die Zellgröße an einer Stelle.
Der Ursprung an der eigenen Position macht das Rig frei verschiebbar —
Isors Anforderung, das System aus der Testarea unverändert in neue
Szenen zu übernehmen — und die vier funktional gleichen Gebiete der
Karte werden zu vier Instanzen statt zu Sonderlogik. Stilles Verpuffen
ist die Linie des Klick-Befehls aus P-B1. Das Gizmo hält die Prüfung
testbar, ohne die vertagte Spieler-Optik festzulegen.
Verworfen: das Raster ab Weltursprung (nicht verschiebbar); die
Zellgröße je Verbraucher gespiegelt (zweiter Besitzer derselben Zahl);
eine sichtbare Verbunden-gegen-lose-Optik schon in V1 (Claudes
Vorschlag — Isor: erstmal gleich lassen, Optik später; Merkposten in
ROADMAP → „P3 · Polish-Merkliste"); Fehlerton oder Meldung bei
ungültigem Klick.

## 2026-10-23 — Netz: Host als Buchhalter, Verkündung an alle, Vorhersage als Erweiterung

Was: Die Belegungstabelle gehört dem Host — sein Exemplar ist das
Original, jede Änderung läuft über ihn. Durchs Netz reisen nur
Zellindizes plus die ClientId des Legers je Kachel (fürs Gebiets-Recht
ab P-B3); Kacheln sind keine NetworkObjects. Ablauf: Die Anfrage reist
erst im Ankunftsmoment der Figur (ServerRpc), der Host prüft Tabelle
und Vorrat, trägt ein und verkündet per ClientRpc an alle — auch an
den Absender; jeder Rechner baut die Kachel-Optik aus derselben
Verkündung. Clients halten eine lokale Tabellen-Kopie nur für die
Geisterbild-Vorprüfung; ist die Zelle bei Ankunft belegt, verpufft der
Auftrag still. Als Sofort-Feedback dient eine rein lokale Quittung im
Bau-Moment (Geisterbild rastet sichtbar ein, später ein Bau-Sound).
Abbauen läuft denselben Weg. Benannte Erweiterung: Client-Vorhersage —
der Owner zeigt die Kachel sofort, der Host verifiziert, eine
Ablehnung rollt zurück (Kachel weg, Vorrat zurück). Auslöser wäre
spürbares Zögern beim Nahbau in den Playtests; Umbau-Schätzung 2–4 h,
begrenzt auf PathGridNet und die Auftragsliste. Skript-Zuschnitt:
PathGrid (Tabelle, Welt-zu-Zelle, Zusammenhang, Gizmo), PathGridNet
(Anfrage, Host-Prüfung, Verkündung), BuildModeController (Slot-Zustand,
Geisterbild, Klicks — nur Owner) und TileGhost unter Scripts/Building/;
BuildOrderQueue (Auftragsliste der Figur, ruft PlayerMotor.MoveTo)
unter Scripts/Player/; BuildBarUI und TileInfoPanelUI unter
Scripts/UI/. Die Action-Map „Gameplay" wächst um Slot-Tasten und
Abbrechen. Bau-Reihenfolge: Grid und Legen rein lokal im Gym →
Geisterbild und Leiste → Auftragskette mit dem Motor → Netz-RPCs →
Abbau-Panel → Zwei-Instanzen-Test über Relay.
Warum: Bauen ist geteilter Weltzustand — anders als das Owner-Movement
braucht er eine Instanz, deren Reihenfolge gilt: Klicken zwei Spieler
zugleich dieselbe Zelle, entscheidet die Eingangs-Reihenfolge beim
Host, statt dass zwei Rechner zwei verschiedene Welten zeigen. Über
Relay läuft ohnehin jedes Paket durch den Host (Stern-Topologie) —
„jeder verkündet selbst" spart kein Paket und kauft das Desync-Risiko.
Die Verkündung an alle inklusive Absender heißt ein einziger Code-Pfad
ohne Vorläufig-Zustand und ohne Rückrollen. Die Netz-Antwort
(0,06–0,15 s über Relay) versteckt der Hinlauf der Figur; im Nahbau
trägt die lokale Quittung — Klick sofort beantwortet, Ergebnis kurz
danach, das Muster aus Warcraft 3. Das RPC-Paar statt NGO-NetworkList:
drei nachvollziehbare Schritte statt Sync-Blackbox (dieselbe Linie wie
gegen Cinemachine), und einen Late-Join gibt es im Spiel nicht.
Verworfen: Client-Vorhersage schon in V1 (Isors eigene Herleitung —
korrekt samt Cheat-Einschätzung, aber sie löst ein Problem, das der
Hinlauf schon löst, und kostet einen Rückroll-Pfad an jeder Kachel);
Verkündung an alle außer dem Absender (zweiter Code-Pfad ohne
Ersparnis); ein NetworkObject je Kachel (Overhead für Objekte, die
sich nie bewegen); NetworkList für die Belegung.

## 2026-10-25 — Leiste: Grundzustands-Panel, Tasten-Zuordnung, HUD-Ordner

Was: Die Leiste trägt drei runde Panels (Isors Entwurf): links das
Grundzustands-Panel — es leuchtet von selbst, wenn kein Werkzeug in der
Hand ist, und wirkt per Klick als Alles-aus-Knopf; es ist nie ein
anwählbarer Pflicht-Modus. Daneben Kacheln und Wächter als
Werkzeug-Toggles. Die Zifferntasten folgen den Werkzeugen (1 Kacheln,
2 Wächter ab P-B7), nicht der Panel-Anordnung; das Grundzustands-Panel
hat keine Taste, sein Tasten-Äquivalent ist Esc; eine dritte
Slot-Action liegt ungenutzt als Reserve. Ingame-UI-Skripte liegen
unter Scripts/HUD/ (BuildBarUI, später TileInfoPanelUI); Scripts/UI/
behält Menü-Kette und generische UI-Helfer. Präzisiert Leisten- und
Skript-Zuschnitt aus „2026-10-23 — Bau-Erlebnis: Kategorie-Leiste und
Objekt-Panel" und „2026-10-23 — Netz: Host als Buchhalter, Verkündung
an alle, Vorhersage als Erweiterung".
Warum: Laufen geht laut Steuerungs-Entscheidung immer (Rechtsklick) —
ein Bewegen-Modus mit Klickzwang widerspräche ihr; als Anzeige erhält
das linke Panel Isors Drei-Panel-Bild trotzdem. Das häufigste Werkzeug
gehört auf die schnellste Taste. Die HUD-gegen-Menü-Trennung ist Isors
Ordner-Entscheidung: Die Ingame-Anzeigen wachsen (Ressourcen, Timer,
Objekt-Panel) und bleiben so sauber von der Menü-Kette getrennt.
Verworfen: „Bewegen" als anwählbarer Modus (Klickzwang vor der
häufigsten Handlung); Taste 1 für das linke Panel (Anordnung schlüge
Werkzeug); BuildBarUI unter Scripts/UI (Claudes Zuschnitt — von Isor
mit der Ingame-gegen-Menü-Grenze begründet überstimmt).

## 2026-10-28 — Szenen-Ordnung: drei Körbe, SYSTEM als Trennstrich

Was: Drei Ordnungs-Fragen mit je eigenem Zuhause: Der Skript-Ordner
sortiert nach Fachgebiet (Building/Player/HUD/NetWorking/GameFlow), die
Szene nach der Frage „beschreibt es diese Welt, oder bietet es einen
Dienst?", der Netz-Besitz bestimmt den Träger (Persönliches aufs
Spieler-Prefab, Gemeinsames auf ein Szenen-Objekt). Die Szene hybrid:
`---SYSTEM ---` ist nur ein Trennstrich, die Dienste (Kamera, Licht,
PlayerSpawner, TestareaBootstrap, GameNetwork) bleiben Wurzel-Objekte;
World und UI sind echte Parents, die nie bewegt oder skaliert werden.
Das Rig heißt jetzt PathBuildingRig und bleibt als Ganzes versetzbar —
die benannte Ausnahme unter World.
Warum: Isors Anforderung „sauber, von Namen her verstehen, nicht quer
verteilt" — mit Blick auf die Erweiterung (Türme). Echte Parents
vererben ihre Transform: Ein verschobenes SYSTEM-Parent nähme Kamera
und Dienste mit, Netz-Identitäten in Kind-Ebenen geraten in
Transform-Sync-Fallen, und der NetworkManager koppelt sich ohnehin
selbst von jedem Parent ab. World und UI dagegen gruppieren Inhalte,
die zusammen stehen bleiben.
Verworfen: SYSTEM als echtes Parent (Isors eigener Verdacht „da könnte
es Probleme geben" — bestätigt); NavMesh unter SYSTEM (Isors
Selbstkorrektur: es beschreibt die Welt, keinen Dienst).

## 2026-10-28 — Netz-Träger GameNetwork, ein Skript je gemeinsamem System

Was: PathGridNet wohnt auf GameNetwork — einem leeren Szenen-Objekt mit
NetworkObject an der Wurzel der Testarea —, nicht auf dem
Spieler-Prefab. Folgen des Trägers für das RPC-Paar Brief/Durchsage:
Das Objekt gehört dem Host, der Brief steht deshalb auf
InvokePermission Everyone und liest den
Absender aus dem Netcode-Stempel (SenderClientId); die Durchsage ist
auf InvokePermission Server verriegelt. Erweiterungsregel: ein
Netz-Skript je gemeinsamem System — Türme reisen später als weiteres
Reisegepäck (int für den Bau-Typ) durch dasselbe Methodenpaar, kein
TowerNet je Bau-Sorte. API-Stand dazu: Seit NGO 2.7 gilt das
universelle [Rpc(SendTo…)]-Attribut (Namen enden auf Rpc,
InvokePermission statt RequireOwnership); ServerRpc/ClientRpc aus der
Design-Runde vom 2026-10-23 sind Alt-Bestand, das Projekt läuft auf
NGO 2.13.
Warum: Isors eigener Träger-Entwurf („ein separates Objekt, da drauf
alles, was Netzwerk tut"): Der Spieler existiert beim Szenenstart noch
nicht und gehört genau einem Client — die Belegung ist aber
Gemeinschaftszustand; Besitz bestimmt den Träger. Ein Skript je System
hält das Gemüse im richtigen Korb, wenn die Systeme wachsen.
Verworfen: PathGridNet auf dem Spieler-Prefab (falscher Besitz, falsche
Lebenszeit); ein Netz-Skript je Bau-Typ (verteilt ein System über
viele Dateien).

## 2026-10-28 — Gym-Testweg: NetworkManager-Prefab und TestareaBootstrap

Was: Der NetworkManager ist jetzt ein Prefab
(Assets/Prefabs/Networking) — eine Konfigurations-Quelle für Menü-Weg
und Testarea. TestareaBootstrap (Scripts/GameFlow, Script Execution
Order −100) instanziiert es beim Play direkt in der Testarea und ruft
StartHost; der Singleton-Guard lässt den Menü-Weg unberührt, dort
existiert der Manager schon. Regel daraus: Verdrahten in der
Awake-Phase, Netz-Dienste starten in der Start-Phase — Netcode
registriert seine Nachrichtentypen zwischen OnEnable und Start.
Warum: Menü-freier Play-Klick macht jede Netz-Iteration billig, und
der Host ist selbst Client — der Solo-Lauf im Gym deckt damit den
kompletten RPC-Pfad ab, nur den zweiten Bildschirm nicht (dafür bleibt
der Relay-Test). StartHost im Awake wirft die ILPP-Ausnahme „Allowed
Count: 0" (GitHub-Issue #2986) — Claudes Awake-Rat war falsch, Isors
Umsetzung jeweils korrekt.
Verworfen: der NetworkManager fest in der Testarea-Szene (zweite
Konfigurations-Quelle, Duplikat beim Menü-Weg); StartHost im Awake
(gemessen am ILPP-Fehler); ein StartClient-Knopf im Gym (Mehr-Spieler
testet erst der Multiplayer Play Mode ab P-B3 — ROADMAP).

## 2026-10-29 — Lauf-Konflikt: manueller Befehl storniert die Bestellungen

Was: Ein manueller Laufbefehl (Rechtsklick) leert die komplette
Bestell-Warteschlange — CancelAllOrders in der Kasse zerstört die
Quittungs-Geister, leert Schlange und Auftrags-Flag; der
ClickCommandInput ruft es vor jedem MoveTo. Kein Rückkehr-Zwang.
Anlass: Isors Exploit-Fund im Gym — Bestellung plus Wegklicken baute
bei Ankunft fern, weil HasArrived zielbezogen ist (am aktuellen
Laufziel angekommen), die Kasse es aber auftragsbezogen las (an der
Baustelle angekommen). Bekannter Nebeneffekt: Auch im Bau-Modus
storniert der Rechtsklick die Shift-Reihe, weil der Laufbefehl immer
gilt; der P3-Merkposten „Rechtsklick legt das Werkzeug weg" zieht das
später glatt.
Warum: Die Figur gehorcht dem letzten Befehl — eine Figur, die sich
nach dem Umweg eigenmächtig zur Baustelle zurückzieht, fühlt sich wie
Kontrollverlust an (Isors Spielgefühl-Urteil gegen Claudes
Rückkehr-Empfehlung), zugleich die RTS-Konvention. Nur den aktuellen
Auftrag abzubrechen ginge nicht: Die Kasse zöge im nächsten Frame den
nächsten aus der Schlange und überschriebe den Spieler-Befehl sofort.
Verworfen: das Rückkehr-Modell (Kasse prüft bei Ankunft die Zelle und
schickt die Figur zurück — der kleinste Fix, aber das falsche Gefühl);
Dulden als P3-Merkposten (der geschenkte Hinlauf hätte die
P2-Messrunde zum Fern-Abbau verfälscht); Abbruch nur des aktuellen
Auftrags.

## 2026-10-29 — Abbau-Weg: Grundzustand-Klick, Layer-Erkennung, kein Besitz-Check

Was: Der Verwalten-Klick gilt nur im Grundzustand (kein Werkzeug in
der Hand); im Bau-Modus bleibt Linksklick der Bau-Auftrag. Kacheln
liegen auf dem eigenen Layer PathTile (den BoxCollider trug das Prefab
schon); die Zelle kommt aus der Transform-Position des getroffenen
Objekts, nicht aus dem Treffpunkt — Seitenwand-Treffer liegen auf der
Zellgrenze und runden sonst in die freie Nachbarzelle. TileInfoPanelUI
wohnt auf dem immer aktiven HUD-Objekt und schaltet das Panel-Kind
über eine Referenz; der Abriss-Brief prüft beim Host nur „besetzt?" —
einen Besitz-Check gibt es in P-B2 nicht (ein gemeinsames Gym-Grid;
das Gebiets-Recht kommt mit P-B3, voraussichtlich als Gebiets- statt
Kachel-Prüfung). Die mitreisende Absender-Id bleibt ungenutzt (TODO
im Code).
Warum: Layer sind die grobe Klick-Kategorie, die Feinheit liefert der
Treffer selbst (Objekt samt Komponenten) — das skaliert, ohne je
Objekt-Sorte einen der 29 Layer zu verbrauchen (Isors Sorge); ein
Skript auf dem Panel, das es selbst abschaltet, könnte sich nie wieder
einschalten (Fehlerbild aus Isor's Tower, `Kern/STOERUNGEN.md`-Umfeld
2026-09-01).
Verworfen: selbstgebaute Id-Komponenten fürs Erkennen (der Raycast
liefert das getroffene Objekt gratis); ein Sicherheits-Reset der
gemerkten Zelle auf (0,0) — (0,0) ist eine gültige Zelle, ein Reset,
der Gültigkeit vortäuscht, ist gefährlicher als keiner; eine
Besitz-Tabelle je Kachel schon jetzt (Beschluss vom 2026-10-23:
Gebiets-Recht ab P-B3); Panel-Öffnen auch im Bau-Modus
(P3-Merkposten, Spielgefühl).

## 2026-10-29 — Karten-Blockout: vier gleiche Gebiete, Fluss-Kreuz, ein Terrain

Was: Ein Gebiet ist 50 × 70 Zellen (Zelle 2 m): 10 Zellen Baumring
ringsum (Deko, unbegehbar), darin das Bau-Raster 30 × 30, direkt
darunter der Wirtschaftsbereich 20 × 30 (vorerst unbegehbar — ob die
Figur ihn je betritt, ist offen). Vier Gebiete im 2×2, getrennt durch
ein 10 Zellen breites Fluss-Kreuz; gesamt 110 × 150 Zellen =
220 × 300 m. Alle vier Gebiete **identisch ausgerichtet**: Start-Marker
rechts mittig am Raster (Monster und Figuren-Spawn, leicht versetzt),
Ziel-Marker links mittig, Standardweg als gerade Linie — die Rigs sind
reine verschobene Prefab-Instanzen, nie rotiert oder gespiegelt. Die
Szene heißt **GameWorld** (Haupt-Spielszene; Testarea bleibt das Gym).
Boden ist **ein** Unity-Terrain: Der Fluss ist eine modellierte Senke,
das NavMesh zerfällt beim Backen in vier Inseln (Böschung steiler als
Max Slope, zusätzlich ein NavMesh Modifier Volume „Not Walkable" über
dem Wasser als doppelter Boden) — keine Zonen-Zuweisung nötig, der
Agent kommt schlicht nicht rüber. Blockout-Texturen je **Zone** (Wasser
blau, Wald dunkelgrün, Bau-Raster Gras, Wirtschaft Stein); die
GDD-Zeile „Gebiete optisch leicht verschieden" bleibt bewusst der
Optik-Phase. Alle Maße sind Inspector-Regler; Prüfwert für die
Messrunden: Raster-Querung ~17 s bei 3,5 m/s Agententempo.
Warum: Quadratisches Raster baut Formen leichter nach; 50×50 empfand
Isor als zu groß. Der Fluss ist sichtbare und technische Grenze in
einem. Identische Ausrichtung ist maximal fair, erfüllt die
GDD-Vorgabe „gleiche Lage von Start und Ziel" wörtlich und vermeidet
nie getestete Rig-Rotationen (Isor: „gespiegelt fühlt sich komisch
an"). Ein Terrain statt vier heißt ein Bake und eine Fläche; die
Gebietsgröße war laut GDD ausdrücklich im Prototyp zu bestimmen.
Verworfen: 50×50-Bau-Raster (zu groß); vier Terrains oder Planes;
zur Karten-Mitte gespiegelte Gebiete; NavMesh-Zonen je Spieler
zuweisen (das Insel-Prinzip erledigt es); Gebiets-Unterscheidungs-Optik
schon im Blockout.

## 2026-10-29 — Spielstart: zufällige Game-Id, MatchSetup, Lade-Timeout

Was: Beim Spielstart würfelt der Host einmal die Zuordnung
Spieler → Game-Id 1–4 (Gebiete im Uhrzeigersinn: 1 oben links, 2 oben
rechts, 3 unten rechts, 4 unten links) und verkündet sie an alle.
Gebiet, Figuren-Spawn und Kamera-Start hängen an der Game-Id, nicht an
der Beitritts-Reihenfolge. Träger ist ein eigenes Netz-Skript
**MatchSetup** auf GameNetwork (Ein-Skript-je-System-Regel). Verankert
wird die Zuordnung an der **stabilen UGS-PlayerId**; die flüchtige
ClientId ist nur Laufzeit-Zweitschlüssel. Lade-Phase: Verliert ein
Spieler beim Laden die Verbindung, warten die anderen bis zu einer
Minute, dann wird er entfernt und das Spiel startet ohne ihn
(Umsetzung, sobald der Menü-Weg auf GameWorld zeigt). Sichtbar wird
die Game-Id simpel: als Zahl über der Spielerfigur und einmal im
Gebiet platziert — bewusst keine Farb-Codierung (Isors Farbsehen;
Nachentscheid vom selben Abend).
Warum: Der Zufall entkoppelt die Kartenposition von der
Lobby-Reihenfolge — niemand kennt sein Gebiet vorab, fair für alle
(Isors Entwurf). Netcode vergibt die ClientId in Beitritts-Reihenfolge
und bei jedem Reconnect **neu** — wer je einen Rejoin will, braucht
von Anfang an einen stabilen Schlüssel, und die PlayerId der
UGS-Anmeldung ist genau das.
Verworfen: Gebietszuordnung nach Lobby-Reihenfolge (vorhersehbar,
unfair); die Game-Id nur an die ClientId hängen (stirbt beim ersten
Reconnect).

## 2026-10-29 — Verbindungsverlust: Gebiet friert ein, Rejoin als vorbereitete Erweiterung

Was: Fliegt ein Spieler mitten im Spiel raus, läuft das Spiel weiter;
seine Figur despawnt, sein Gebiet friert ein — die Kacheln bleiben,
denn die Belegung lebt beim Host. Ein Rejoin ist im Prototyp **nicht
gebaut, aber vorbereitet**: Das „Original-Datenpaket" (Isors Wort)
existiert als Host-Belegungstabelle ohnehin, die Durchsage-Empfänger
sind tolerant (Schon-vorhanden-Wächter), und die Game-Id hängt an der
stabilen PlayerId. Der spätere Anbau wäre ein **Willkommenspaket**:
ein gezielter Zustands-Brief des Hosts an den Rückkehrer mit allen
belegten Zellen samt Leger-Id; Schätzung 2–4 h. Gebaut wird er — wenn
überhaupt — erst, wenn das Spiel ansonsten so gut wie fertig ist
(Isors Nachentscheid vom selben Abend); bis dahin gilt nur die
Vorsorge.
Warum: Durchsagen sind Ereignisse — wer sie verpasst hat, erfährt sie
nie; ohne die PlayerId-Verankerung wäre ein Rejoin ein
Architektur-Umbau, mit ihr ein Anbau. Anlass ist Isors Sorge, ein
fehlender Wiedereinstieg könnte in der Bewertung negativ auffallen —
ob das stimmt, klärt eine Unterrichts-Frage, nicht eine Vorab-Baustelle.
Präzisiert den Netz-Entscheid vom 2026-10-23: „Late-Join gibt es
nicht" gilt für den laufenden Prototyp-Spielstand, nicht als Verbot
der Erweiterung.
Verworfen: Rejoin sofort bauen (Prototyp-Budget); das Spiel bei
Verbindungsverlust anhalten oder abbrechen (bestraft die drei
Verbliebenen).

## 2026-10-29 — Meilenstein-Plan: immer eine Version voraus

Was: Interne Fertig-Ziele je Uni-Meilenstein, jeweils rund eine
Version vor dem Abgabetermin (Termine besitzt
`Uni/Semester_3/STUNDENPLAN.md`): Zur Prototyp- und Pitch-Abgabe
(27.11., Präsentation 03.12.) ist der Stand Alpha-nah — Bausteine bis
P-B7 gebaut, Slides und Erkenntnis-PDF deutlich vor dem Termin. Die
Alpha (fällig 08.01.) ist intern Ende November bis Mitte Dezember
fertig — zusätzlich zur Prototyp-Latte heißt das Win-/Lose-Condition,
Core-Feature-complete, stabil. Die Weihnachtslücke (18.12.–03.01.,
kein Unterricht) ist die Optik-Phase: Assets, Shader, Effekte, GUI,
Sound — genau der Beta-Inhalt. Die Beta (fällig 29.01.) ist intern
Anfang Januar fertig, der Goldmaster (fällig 12.02.) Ende Januar; der
Februar ist Feinschliff, Projektreflexion (19.02.) und Portfolio
(26.02.) — und Puffer für Steuer, Stream und Harness. Die benotete
Zwischenprüfung „Projektplanung" (18.12.) speist sich direkt aus
diesem Plan. Ins Pitch-GDD kommen die offiziellen Uni-Termine samt
Pufferzeiten; der interne Vorsprung steht bewusst nicht im GDD.
Warum: Der Vorsprung ist der Puffer für Notfälle, Extras und das
echte Leben — „lieber ausbauen als verlieren" (Isor); dieselbe Linie
wie Fertig-vor-fällig im Semesterplan. Die Krankschreibungs-Tage bis
zum 04.11. sind das Fenster, in dem der Vorsprung wachsen soll. Die
GDD-Vorgabe verlangt realistische Zeitabläufe mit Pufferzeiten — der
interne Plan ist genau dieser Puffer.
Verworfen: auf die Uni-Termine planen (kein Puffer, jede Störung
schlägt durch); den internen Vorsprung ins GDD schreiben (das GDD
trägt die offiziellen Zusagen, nicht die private Latte).

## 2026-10-30 — Meilenstein-Etappen: Fertig-Linien, Inhalte, Wochenplan-Ritual

Was: Die fünf Abgabe-Milestones in Etappen durchentschieden (voller
Zuschnitt: ROADMAP → „Meilenstein-Plan"). Die tragenden Beschlüsse:
**Fertig heißt rund eine Woche vor der Abgabe** — die Fertig-Linien
sind 20.11. (Feature-Stopp Prototyp; gilt nicht für
Core-Loop-Essentielles), 11.12. (benotete GDD-Fassung), 26.12.
(Alpha; Isors Wahl statt 19.12. — zwei Wochen Puffer, die Rest-Ferien
gehören der Optik), 22.01. (Beta), 05.02. (Gold), 16.02./21.02.
(Reflexion/Portfolio). Diese Linien samt Inhalts-Milestones gehen ins
Pitch-GDD — sie sind die verlangten „realistischen Zeitabläufe mit
Pufferzeiten"; privat bleibt nur die Ambition „eine Version voraus".
P-B8 wird gebaut (nicht mehr Default-Streichkandidat), als letzter
Prototyp-Baustein mit Streichrecht im Notfall. Die benotete
Projektplanung bekommt den festen Abschnitt **„Plan gegen
Wirklichkeit"**: Schätzung gegen Grindstone-Messung je Baustein.
Alpha: Win/Lose simpel (Leben null → raus, letzter gewinnt, zurück
ins Menü), erste Spur Audio/Asset als Pipeline-Test. Beta: die
GDD-Zusage „vier Wächter × drei Stufen, vier Gegnertypen" **bleibt**
— Stufen sind Wert-Ausbauten übers Objekt-Panel, Assets kommen aus
den im GDD benannten freien Packs; ins G2 kommt der
Absicherungs-Satz, dass die Stufen-Feinabstimmung in den Messrunden
liegt. Sound: Grundvertonung aus Bibliotheken, der
Audio-Unterricht (ab 18.01.) veredelt. Gold: Messrunden, P3-Polish,
Code-Aufräum-Pass, finale GDD-Fassung; Rejoin-Entscheidung erst am
05.02.-Stand. Dazu das **Wochenplan-Ritual**: sonntags (im
Pflegetag-Takt) wird der Wochenplan aufgestellt und lebt als
oberster Abschnitt der Status-Tafel — was diese Woche gebaut wird,
was schon fertig ist.
Warum: Etappen-Vorgehen auf Isors Wunsch — ein Milestone je
Chat-Block, gezielt beantwortbar. Die Pufferwoche ist zugleich die
Abgabe-Fabrik (Playtests, PDF, Slides, Build entstehen erst mit
fertigem Spiel). Die 4×3-Stufen-Zusage bleibt, weil die Stufen im
eigenen Design Zahlen sind, keine Content-Stücke — der Panel-Weg
existiert seit P-B2.
Verworfen: Alpha-Fertig-Linie 19.12. (Claudes Vorschlag — Isor: zwei
Wochen Puffer reichen, drei wären zu viel); Statistiken, Spielerprofil
und Rematch im GDD (Zusatz-Ideen, sonst wird der Umfang
unrealistisch); ein Trailer für die Gold-Präsentation (gehört nicht
zum Semesterprojekt, vielleicht später); die Wächter-Stufen aufs GDD
kürzen (unnötig — Stufen sind leichtgewichtig).

## 2026-10-30 — Werkzeug-Politik: Tools und Formeln schreibt die AI

Was: Editor-Tools werden gemeinsam designt, aber von der AI **komplett
fertig** geschrieben — kein Block-für-Block; ebenso die Herleitung und
Umsetzung mathematischer Algorithmen (etwa das Monster-Routing).
Selbst getippt werden Tools nur, wenn ein Semesterprojekt es fordert.
Jedes so entstandene Skript wird im Datei-Header deklariert
(`Author: … (design), Claude AI (code)` plus Description-Zeile).
Tool-Skripte tragen das Präfix `Tool_` — eine bewusste Abweichung vom
reinen PascalCase, damit sie im Project-Fenster als Werkzeuge erkennbar
sind. Erstes Stück: `Tool_MapLayout.cs`, ein Gizmo-Zeichner als
GameObject-Komponente statt EditorWindow, alle Inspector-Felder mit
Tooltip. Normaler Spiel-Code bleibt unberührt Isors Lernstoff
(Gerüst plus TODOs, Isor tippt).
Warum: Isors Lernzeit gehört der Spiel-Logik, die er verteidigen und
wiederverwenden muss; Tool- und Formel-Code selbst zu tippen ist ihm
Zeitverschwendung. Die GameObject-Form statt EditorWindow, weil das
Tool nur zeichnet und Werte hält — ein Fenster brächte Editor-API ohne
Nutzen. Die Deklaration, damit bei Abgaben nie Unklarheit entsteht,
was von wem stammt.
Verworfen: Tools Block für Block wie Spiel-Code (übt nichts, was Isor
üben will); EditorWindow-Form (Mehraufwand ohne Mehrwert).

## 2026-10-30 — GameWorld-Anker: Terrain und Kreuz-Mitte

Was: Feste Welt-Anker der Szene GameWorld: Fluss-Kreuz-Mitte bei
(100, 0, 150) — dort sitzt das MapLayout-Tool —, Terrain 250×320 m auf
Position (−25, −100, −10) mit 600 m Höhenspielraum, Spielfeld
x −10…210 / z 0…300. Bau-Raster-Ecken (SW, zugleich Rig-Positionen):
G1 (10, 0, 220) · G2 (130, 0, 220) · G3 (130, 0, 60) · G4 (10, 0, 60),
je 30×30 Zellen à 2 m. Rig-Kinder: EnemySpawnPoint lokal (60, 0, 30)
rechts mittig, EnemyDespawnPoint lokal (0, 0, 30) links mittig — leere
GameObjects ohne Collider, Anzeige kommt per Gizmo.
Warum: Das Terrain größer als das Spielfeld, damit der Rand nie ins
Leere fällt; die krummen Anker folgen aus Kreuz-Mitte minus halber
Terrain-Größe. Marker ohne Collider, damit Bau- und Klick-Raycasts
nichts Fremdes treffen. Die Zahlen stehen hier, damit keine Session
sie aus der Szene zurückrechnen muss.
Verworfen: Marker als sichtbare Primitive (Collider im Raycast-Weg).

## 2026-10-30 — Monster-Lauf: Wander-Modell, Rollback, Solo-Lernraum

Was: Das Lauf- und Gültigkeits-Design des Kern-Systems, in sieben
Punkten. **(1)** Monster laufen ausschließlich auf Kacheln, nie auf
Gras; sie nutzen kein NavMesh, sondern folgen vorberechneten
Wegpunkten (Zellmittelpunkte, Höhe Kachel-Oberkante) — das NavMesh
gehört allein der Spielfigur. **(2) Wander-Modell:** Jedes Monster
merkt sich besuchte Kacheln; an echten Gabelungen splitten die Monster
abwechselnd, auch in längere Arme; betreten wird nur, was das Ziel ohne
besuchte Kacheln noch erreicht. Sackgassen und Ringe bleiben
unbetretener Vorrat. Beweisbar: kein Kreisel, jede Ankunft, kein
verbotenes Layout — flächig geklebte Kacheln („Klumpen") zählen als
eine Kreuzung und werden auf kürzestem Weg durchquert. **(3)
Gültigkeit:** Spawn-Zelle und Ziel-Zelle verbunden, geprüft nach jedem
Legen/Entfernen; ungültig → alle Kacheln färben sich (vorerst Rot,
Farbwahl in den Settings als benannte Erweiterung), gebaut werden darf
weiter. **(4) Rollback („Last known good"):** Beim Wellenstart gültig →
Stand wird neuer Rückfallpunkt (Kopie der Belegungstabelle beim Host,
nur im Arbeitsspeicher); ungültig → letzter gültiger Stand wird
wiederhergestellt, Türme im Weg entfernt und voll erstattet (Kauf plus
Upgrades), überzählige Kacheln 1:1 in den Vorrat. Der Standardweg
garantiert Runde 1 — per Induktion existiert immer ein Rückfallpunkt.
**(5)** Feste Eintritts- und Austritts-Zelle neben Spawn- und
Ziel-Marker; der Standardweg ist die gerade Kachel-Linie dazwischen.
**(6)** Routen-Anzeige (Pfeile auf den Kacheln: sieben
Richtungs-Kombinationen, per Drehung vier Sprites) nur im Solo, dort
per Schaltfläche an- und abschaltbar; Multiplayer zeigt nur die
Warnfärbung. **(7)** Solo fragt beim Start einmal „Tutorial — ja/nein?"
für Info-Tipps; die Architektur dazu: eine zentrale Weg-Rechnung
(Ausbau von `PathConnectivity`) rechnet einmal pro Kachel-Änderung und
hält das Ergebnis, alle Leser (Gizmo, Warnfärbung, Rollback,
Monster-Routen) fragen nur ab. Gebaut wird in Ausbaustufen entlang der
Abhängigkeiten: erst Flood Fill plus Gizmo (P-B3), dann Gültigkeit und
Rollback, zuletzt das Routing.
**Ersetzt:** die Gerade-Linie-Regel aus „2026-10-17 — Weg: Standardweg
ab Start, Zusammenhang, gerade Linie" (Monster betreten nie mehr Gras;
Standardweg und Kachel-Sperre bleiben) und die Gabelungs-Teilung aus
„2026-10-16 — Sende-Ziel und Gabelungs-Regel" (das Abwechselnd lebt im
Wander-Modell weiter, die Sende-Ziel-Regel bleibt unberührt).
Warum: Isors Kernargument — die Karte ist zu groß zum Abzählen; wenn
Monster eine gebaute Abzweigung grundlos ignorieren, ist das
unerklärlicher Frust, also nehmen sie jede echte Gabelung. Das
Wander-Modell gibt maximale Baufreiheit (Verlängerungen und Schleifen
sind Strategie, keine Fehler) und bleibt deterministisch
netzwerk-synchron, weil alles aus denselben Host-Kacheldaten
vorberechnet wird. Rollback statt Bestrafung: Die Warnung ist die
ganze Bauphase sichtbar, die Strafe ist nur verlorene Bauzeit — volle
Erstattung hält sie mild. Solo/Multiplayer-Trennung: Im Sandkasten
lernen, im Versus Können zeigen.
Verworfen: Monster warten oder laufen gerade Linie bei unfertigem Weg
(ersetzt — die Welle startet nie auf ungültigem Stand); lokale
Raycast-KI je Monster (kann „kürzer" nicht wissen, Physik-Abfragen für
eine Frage, die die Datentabelle beantwortet); reines
Kürzeste-Route-Modell (ignoriert ungleich lange Gabelungen — Isors
Frust-Szenario); Wasser-Modell „nur Richtung Ziel" (ignoriert
Umweg-Arme, dasselbe Problem); 2×2-Bauverbot (unnötig, sobald Klumpen
als eine Kreuzung zählen); Zufalls-Split (bestraft Planung, bräuchte
synchronisierte Würfe — bleibt Prüf-Variante); Schritt-/Zeitlimit
gegen Ringe (würde auch ehrliche lange Wege treffen); Routen-Anzeige
auch im Multiplayer (nähme dem Versus die Könnens-Probe).

## 2026-10-31 — Bau-Regel: gebaut wird nur bei vollem Weg

Was: Ein Bau-Auftrag wird bei Ankunft nur ausgeführt, wenn der
NavMeshAgent seinen Weg vollständig gehen konnte — der Motor bekommt
neben `HasArrived` die zweite Eigenschaft `HasFullPath`
(`pathStatus == PathComplete`), und die Queue baut nur, wenn beide
wahr sind; Verwerfen räumt trotzdem auf (Geist weg, nächster
Auftrag). Kein eigener Reichweiten-Regler: „kurz davor" ist die
`stoppingDistance` des Agents, einstellbar am Player-Prefab.
Verworfen wird still; ein „geht nicht"-Feedback und die
Vorab-Prüfung beim Hovern (Geist gar nicht erst zeigen, wenn kein
Weg hinführt) stehen auf der P3-Merkliste.
Warum: Der Agent klemmt unerreichbare Ziele auf den Inselrand und
meldet dort „angekommen" — ohne das Tor entstand die Kachel trotzdem
(gefunden beim ersten GameWorld-Lauf, sichtbar gemacht durch den
Falsch-Rig-Bug). Das Wissen über Wege gehört dem Motor („the only
place that talks to the NavMeshAgent"), die Queue fragt nur —
deshalb kein Abstandsmessen in der Queue.
Verworfen: eigenes `_buildReach`-Feld in der Queue (doppelter
Besitzer neben stoppingDistance); Distanz messen statt den
NavMesh fragen (pathStatus beantwortet genau diese Frage).

## 2026-10-31 — Rig-Zuweisung: Brett statt Brief, Zuweisung statt Suche

Was: Die beim Spielstart gewürfelte Zuordnung Game-Id → Spieler
(Beschluss „Spielstart", 2026-10-29) wird als **Schwarzes Brett**
geteilt: MatchSetup schreibt sie host-seitig in einen
Netzwerk-Zustand (NetworkVariable/NetworkList), den Netcode auf
alle Rechner spiegelt; jeder liest, wann er bereit ist. Befüllt wird
das Brett per **Losbeutel**: alle ClientIds in eine lokale Liste, je
Runde einen zufälligen Index ziehen, den Gezogenen hinten ans Brett
anhängen (Platz = Game-Id) und aus dem Beutel entfernen — Zufall ohne
Dopplung, lokal gemischt, weil jede Brett-Änderung gefunkt würde. MatchSetup
ist Szenen-Objekt auf GameNetwork und hält die vier Rigs als
Inspector-Felder — gespawnte Figuren (BuildOrderQueue u. a.) holen
ihr Rig per Anfrage an MatchSetup, nie mehr per Szenen-Suche
(`FindFirstObjectByType` ist in der GameWorld mit vier Rigs
grundsätzlich falsch und obendrein deprecated — Instance-ID-Ordnung,
nicht Hierarchie). Grid und View gehören paarweise zum Rig.
Warum: Durchsagen sind Ereignisse — wer beim Senden nicht bereit
ist, erfährt sie nie (dasselbe Argument wie im
Verbindungsverlust-Beschluss); das Brett löst das Spawn-Timing von
selbst und ist zugleich die Rejoin-Vorsorge. Auslöser war der
Falsch-Rig-Bug vom 2026-10-31: Die Suche lieferte Rig 4, Laufziel
und Quittungs-Geist lagen im fremden Gebiet.
Verworfen: RPC-Durchsage als Transport (verpassbar); eine bessere
Suchfunktion (FindAnyObjectByType — „irgendeins von vier" kann nie
richtig sein); Rig-Suche per GameObject-Name (String-Kopplung).

## 2026-10-31 — Bau-Input gehört dem Spieler: ein BuildModeController

Was: Der BuildModeController zieht vom Rig-Prefab auf ein einzelnes
Szenen-Objekt (`BuildMode` unter `---SYSTEM---`) — es gibt eine Maus,
einen Spieler, ein aktives Werkzeug, also einen Controller. Sein Grid
holt er zur Laufzeit von MatchSetup (gleiches Muster wie die
BuildOrderQueue); der TileGhost wird ebenfalls eine einzelne
Szenen-Instanz statt ein Kind je Rig. Die Testarea bekommt dieselbe
Struktur (MatchSetup mit Ein-Rig-Array), damit beide Szenen eine
Architektur teilen. Dazu Isors fester Maßstab, ab jetzt Leitlinie:
Architektur-Sauberkeit hat Vorrang vor Umbaugröße — Besitzfrage
zuerst, bewusste Ausbaustufen sind erlaubt, werden aber als Naht
benannt.
Warum: In der Vier-Rig-GameWorld lauschten vier Controller auf
dieselben globalen Input-Actions; ihre Baumodus-Zustände liefen beim
ersten Platzieren auseinander (nur der gültige legt das Werkzeug weg),
wonach fremde Controller im Verwalten-Modus Panels mit fremden
Zellindizes öffneten. Vier Kopien, von denen drei schlafen, würden die
falsche Aussage „Input ist Rig-Sache" einbetonieren — der Kopf des
Skripts sagt selbst „Local only, like the camera".
Verworfen: vier Controller mit Selbst-Abschaltung der fremden
(Minimal-Änderung, aber falscher Besitz); den Controller auf die
Spielerfigur legen (gespawntes Prefab kann Ghost, Panel und Actions
nicht halten — dasselbe Szenen-Referenz-Problem wie bei der Queue).

## 2026-11-02 — Standardweg: lokal gebaut, Startzustand ist Szenen-Wissen

Was: Die gerade Start-Linie (Beschluss „Monster-Lauf", Punkt 5) baut
jeder Rechner beim Szenen-Start **selbst**: das neue
`DefaultPathBuilder`-Skript am Rig holt die Eintritts-/Austritts-Zelle
von `PathConnectivity` (dort wurde die Marker-Rechnung öffentlich und
bekam das Austritts-Geschwister) und legt je Zelle das bekannte Paar
Grid-Belegen plus View-Kachel — in `Start`, weil Grid und View ihre
Tabellen in `Awake` bauen. Dabei wird die Ein-Schreibstelle-Regel
**präzisiert**, nicht gebrochen: „Die Durchsage ist die einzige
Stelle, die Grid und View schreibt" gilt für **Laufzeit-Änderungen
durch Spieler**; Anfangszustand ist Szenen-Wissen und wird lokal
geschrieben — wie das Terrain, das auch niemand funkt.
Warum: Die Linie leitet sich vollständig aus Daten ab, die jeder
Rechner identisch besitzt (Szene, Marker, Rastermaße) — dieselbe
Rechnung ergibt überall dasselbe Ergebnis, es gibt nichts zu
übertragen. Der Netz-Weg hätte die PathGridNet-Vier-Rig-Naht sofort
fällig gemacht und Ereignisse für Anfangszustand benutzt — exakt die
Verpassbarkeit, gegen die das Brett gebaut wurde.
Verworfen: Host verkündet jede Start-Kachel per Durchsage (dreißig
Nachrichten für etwas, das jeder selbst weiß; verpassbar; zieht die
Vier-Rig-Naht vor); Linie ins Brett legen (Brett ist für Zustand, der
sich je Match unterscheidet — die Linie ist immer gleich).

## 2026-11-02 — Kachel-Sperre: nur Eintritts- und Austritts-Zelle

Was: Gesperrt gegen Abriss sind genau **zwei** Zellen je Gebiet — die
Eintritts- und die Austritts-Zelle der Start-Linie. Das Wissen wohnt
im `PathGrid` (Daten-Besitzerin: Liste `_lockedCells`, `LockCell`,
`IsLocked`, kein Unlock — die Sperre gilt das ganze Match), gesetzt
vom `DefaultPathBuilder` nach dem Legen, geprüft host-seitig als
zweiter Wächter in `RequestRemoveTileRpc` — formgleich mit dem
`IsOccupied`-Wächter, Ablehnung still. Die Kacheln **dazwischen**
bleiben abreißbar: Umbauen ist die Strategie, Gültigkeits-Warnung und
Rollback fangen den Rest. Bauen auf gesperrte Zellen blockt schon der
vorhandene Belegt-Wächter, da gesperrte Zellen immer belegt sind.
Warum: Ohne Eintritt oder Austritt gibt es keinen gültigen Weg mehr,
den Umbauen retten könnte — der Rollback hätte keinen Rückfallpunkt
mit diesen Zellen, wenn sie je frei würden. Alles darüber hinaus zu
sperren würde dem Spieler Strategie wegnehmen.
Verworfen: die ganze Start-Linie sperren (nimmt das Umbauen, also das
Spiel); Sperre im Netz-Skript halten (PathGridNet ist Transport, das
Grid ist die Daten-Besitzerin); Spieler-Feedback beim abgelehnten
Abriss (P3-Merkliste, zusammen mit dem Panel-Verhalten der End-Zellen
— Playtest entscheidet, ob sie Panel und Upgrades bekommen).

## 2026-11-02 — Monster: der Host simuliert, alle anderen zeigen an

Was: Monster sind host-gespawnte NetworkObjects. Die **Simulation**
(Bewegung Zellmitte zu Zellmitte, Ankunfts-Prüfung, Leben-Abzug,
Despawn) läuft ausschließlich beim Host hinter einer `IsServer`-Wache —
das Spiegelbild der `IsOwner`-Wache der Spielerfigur; die
**Darstellung** (Mesh, später Healthbar und Effekte) läuft überall.
Positionen reisen per NetworkTransform mit Server-Autorität (dort die
Werkseinstellung — nichts umzustellen). Keine Physik, kein NavMesh:
Der Host schiebt die Position selbst, das NavMesh bleibt den
Spielerfiguren.
Warum: Ein laufendes Monster ist laufender Weltzustand, und jeder
geteilte Zustand hat bei uns genau einen Schreiber („Host als
Buchhalter", 2026-10-23 — dasselbe Prinzip wie Kachel-Durchsage und
Game-Id-Brett). Lokale Simulation driftet, weil Frames nie gleich
getaktet sind; sobald Folgenreiches an der Position hängt
(Turmschuss, Leben-Abzug), kippen die Stände in verschiedene
Ergebnisse, und keiner wäre „der richtige". Der Host-Weg heilt
Abweichungen von selbst: Das nächste Positions-Paket überschreibt mit
der Wahrheit. Abgrenzung zum Standardweg-Beschluss: Die Linie ist
einmaliges Szenen-Wissen, ein Monster lebt durch Zeit — die
Prüffrage „könnte ein Rechner das Ergebnis falsch haben?" trennt die
beiden.
Verworfen: Monster lokal auf jedem Rechner (Drift, vier Wahrheiten);
Lockstep (alle simulieren bitgleich, nur Eingaben reisen — braucht
festen Tick, deterministische Ganzzahl-Mathematik und identische
Reihenfolge von allem, eine Abweichung spaltet die Partie ohne
Reparaturweg; kauft Bandbreite, die erst bei Einheiten-Massen à la
RTS fehlt, nicht bei ein paar Dutzend Monstern). Client-Vorhersage
bleibt benannte Erweiterung wie beim Netz-Beschluss vom 2026-10-23.

## 2026-11-02 — Monster-Typen: Steckbrief-Assets statt Klassen-Pyramide

Was: Es gibt **ein** Monster-Skript (den Läufer) und je Monster-Typ
ein ScriptableObject als Steckbrief: Tempo, Leben, Diamant-Preis,
Einkommens-Plus, Leben-Kosten am Ziel, Optik. Ein neuer Typ ist ein
neues Asset, null Zeilen Code; der Boss ist dieselbe Klasse mit
dickeren Zahlen (Leben-Kosten 5, Siegbedingungs-Beschluss
2026-10-16). Übers Netz reist nur die Typ-Nummer — die Steckbriefe
sind Szenen-Wissen, identisch auf jedem Rechner; ein Array der
Steckbriefe macht den Index zur Bedeutung (dasselbe
Platz-ist-Bedeutung-Muster wie SceneId und Game-Id). Vererbung
entsteht erst beim ersten echten **Verhaltens**-Unterschied (das
fliegende Monster: anderes Laufen) — dann an der Stelle, die der
Unterschied verlangt.
Warum: Klassen folgen Verhalten, Assets folgen Zahlen. Grunt und Boss
unterscheiden sich nur in Zahlen; eine Klasse, deren Inhalt „andere
Werte im Konstruktor" ist, trägt kein Verhalten und ist bei der
Abgabe schwer zu verteidigen. Neue Typen ohne Code-Änderung können
nichts Bestehendes brechen (Isors Maßstab „nicht tausendmal
anfassen"), Balancing läuft im Inspector zwischen zwei Play-Läufen —
konsequente Fortsetzung des Awake-Seed-Musters.
Verworfen: MonsterBase-Hierarchie auf Vorrat (die Trennstelle würde
heute geraten statt vom echten Unterschied diktiert — eine falsch
sitzende Hierarchie umzubauen ist teurer als eine richtige später
einzuziehen); Zahlen je Typ im Prefab statt im SO (je Typ ein
Prefab-Klon, Werte doppelt gepflegt).

## 2026-11-02 — HUD-Panels: eine abstrakte Basisklasse

Was: Alle Info-Panels erben von `InfoPanelUI` (abstrakt): Die Basis
besitzt den Panel-Root und das Paar `ShowPanel`/`OnCloseClicked`,
jeder Erbe seinen Kontext und seine Knöpfe — `TileInfoPanelUI` die
Zelle samt Abriss, `SendBuildingPanelUI` den Sende-Knopf. Braucht ein
Erbe Kontext beim Öffnen, überlädt er `ShowPanel` (gleicher Name,
andere Parameter) und ruft das geerbte Zeigen. Kein „Base"-Suffix im
Namen: `abstract` ist das Compiler-Gesetz, der Name bleibt der
Ist-ein-Satz (`TileInfoPanelUI : InfoPanelUI`).
Warum: Isors eigener Vorschlag vor dem zweiten Panel — geteiltes
Verhalten plus ein konkreter zweiter Fall ist der richtige Zeitpunkt
für Vererbung; der zweite Erbe war danach fast gratis. Merksatz:
gemeinsamer **Code** → Basisklasse, gemeinsame **Fähigkeit** ohne
Code → Interface (das kommt später z. B. als IDamageable über
Monster, Gebäude und Türme hinweg).
Verworfen: Interface statt Basisklasse (hätte Panel-Root und beide
Methodenkörper in jeden Erben kopiert — genau das Duplikat, das weg
sollte); Kachel-Wissen in der Basis (`_net`/`_cellPos` gehören dem
Kachel-Erben — Besitzfrage); Name „InfoPanelBase" (Namens-Bitte statt
Compiler-Gesetz).
Nachtrag 2026-11-03/04: Die Überlade-Lösung ist abgelöst — von außen
klopft man an die Namens-Tür des Erben (`OpenForTile(cell, rigId)`,
`OpenForBuilding()`), das geerbte `ShowPanel` ist **protected**: das
Zeigen bleibt Familiensache (Türen-Regel; Auslöser war Isors zweimal
angemahnte Namenskritik an der Doppelbedeutung von ShowPanel).
Schließen bleibt public für den X-Knopf. Dazu kamen die
Ein-Panel-Regel in die Basis (statisches Feld `_currentOpenPanel` —
die Datenstruktur erzwingt die Regel) samt `CloseOpenPanel` als
statischem Dienst, und das Ziehen des Kachel-Werkzeugs schließt das
offene Panel („die letzte Absicht gewinnt"). Diese Spezialfälle sind
Zwischenstand: Die Bühne (Eintrag 2026-11-04) löst sie ab, sobald sie
fertig gebaut ist.

## 2026-11-02 — Sende-Panel: zwei Wege hinein, nur das eigene Gebäude

Was: Das Sende-Panel öffnet auf **zwei** Wegen — HUD-Knopf (OnClick →
geerbtes `ShowPanel`, null neuer Code) und Welt-Klick aufs
Sendegebäude. Der Welt-Klick läuft im neuen `SendBuildingSelector`
(Spieler-Eingabe, wohnt beim BuildModeController-Objekt): Raycast nur
auf die **generische** Layer `Clickable`, dann Ausweis-Kontrolle per
`TryGetComponent<SendBuilding>`, dann Game-ID-Vergleich — das
`SendBuilding` am Würfel trägt seine Besitzer-Game-ID als
Szenen-Wissen (wie die Rig-Reihenfolge), der Selector vergleicht mit
der eigenen aus MatchSetup. Die UI-Wache ist Komfort; die echte Wache
steht host-seitig im Brief-Empfänger.
Warum: Beide Wege sind beschlossenes UX (Isor: Spieler wollen beides).
Layer sind knapp (32, Bitmaske vor dem Treffer) — sie bleiben grobe
Türsteher-Kategorien; **was** getroffen wurde, sagt die Komponente:
Compiler-geprüft statt vertippbarer Tag-String, und sie liefert das
Objekt gleich mit, das die Game-ID sowieso tragen muss.
Verworfen: eine Layer je Objektsorte (skaliert nicht über 32);
Tag-Vergleich (String, liefert nichts in die Hand); Klick-Code im
BuildModeController (Auswählen ist kein Bauen — anderer Besitzer).
Benannte Nähte, Aufräum-Runde auf grünem Stand beschlossen: die
Ein-Panel-Regel in der Basis (heute können zwei Panels zugleich
offen stehen) und der Klick-Verteiler — ein Ray, der per Ausweis
verteilt — fällig ab dem **dritten** Klickbaren (Türme). Eingelöst
am 2026-11-03/04: Die Ein-Panel-Regel steht in der Basis, und der
Klick-Verteiler-Entscheid ist bestätigt — er kommt mit P-B7.

## 2026-11-03 — Sende-Brief: nur die Typ-Nummer reist

Was: Der `MonsterSpawner` (GameNetwork, bei den gemeinsamen Systemen)
empfängt `RequestSendMonsterRpc(int monsterTypeIndex)` — der Brief
trägt **nur die Typ-Nummer**. Der Katalog (`MonsterDefinition[]`,
Platz = Nummer, Grunt = 0) ist Szenen-Wissen. Der Host wacht
(Nummer im gültigen Fenster, Absender auf dem Brett — die ClientId
liefert der RPC selbst), baut die Route selbst (V1: Eintritts- bis
Austritts-Zelle des eigenen Rigs über PathConnectivity und
TranslateToWorldPos; das Ring-Ziel kommt mit P-B5) und spawnt in
drei Schritten: Instantiate, `InitializeMonster` (lokal füttern),
`NetworkObject.Spawn()`. **Spawn ist die Durchsage** — ein eigenes
Announce-RPC gibt es nicht. Wegpunkte, Steckbrief und Lebenspunkte
bleiben host-lokal; kein `SpawnWithOwnership`, Monster gehören dem
Server.
Warum: Dem Host nichts erzählen, was er selbst nachschlagen kann
(dieselbe Regel wie beim Kachel-Brief); die Gäste simulieren nicht
und brauchen die Daten nicht — die Spawn-Durchsage trägt nur
Katalognummer, Netz-ID und Position, die Hülle entsteht je Rechner
aus der eigenen Prefab-Liste. Die spätere Diamanten-Wache gehört
genau hierhin: Das Konto wird Host-Brett, das UI graut nur aus —
UI höflich, Host misstrauisch.
Verworfen: Wegpunkte oder Werte im Brief (Host weiß sie selbst, ein
Client könnte lügen); eigenes Announce-RPC (der NGO-Spawn ist die
Durchsage schon); Kosten-Prüfung nur im Client (veraltete Kopie,
Doppelklick-Rennen, manipulierbar).

## 2026-11-04 — Spawn-Reise: der Spawner fragt das NavMesh, platziert wird per Warp-Brief

Was: Der `PlayerSpawner` prüft jeden Spawnpunkt mit
`NavMesh.SamplePosition` (Suchradius als Inspector-Feld; Fehlschlag =
Editor-LogError, kein Spawn), instanziiert am Treffer und schickt dem
Owner **nach** dem Spawn einen Warp-Brief: `WarpToSpawnRpc(Vector3)`
mit `SendTo.Owner`, der Motor ruft `_agent.Warp(...)` — die einzige
legale Platzierung eines NavMeshAgents. Die Wurzel des Player-Prefabs
steht auf 0/0/0 (Isor genullt, sie stand bei −404/1/31). Grundlage
ist der NGO-Quellcode statt Spekulation: `NetworkSpawnManager.cs`
Zeile 935 instanziiert **ohne** Position, Zeile 946 setzt sie erst
danach — auf Gast-Rechnern wird ein Spieler in der Prefab-Pose
geboren, und bei Owner-Autorität zählt danach allein der Stand des
Owner-Rechners. Der Warp-Brief setzt deshalb genau dort an, wo die
Wahrheit wohnt. Doppeltest Host + Client danach grün.
Warum: Die Spawn-Jagd vom 2026-11-03 fand drei gestapelte Ursachen
(Spawnpunkte auf Y=0 unterm NavMesh, Prefab-Wurzel weit abseits,
Agent klemmt nach rohem Versetzen) — jede Einzelmaßnahme wirkte nur
halb, und erst der Quelltext-Beweis erklärte, warum der Client-Spieler
„halb in der Erde" hing, obwohl der Inspector richtige Werte zeigte
(zwei Zeitpunkte: Geburt gegen Abgleich).
Verworfen: Y-Werte von Hand nachsetzen (heilt das Symptom, nicht die
Geburt in der Prefab-Pose); auf Synchronize Transform vertrauen (läuft
einmalig beim Spawn und verliert gegen die Owner-Autorität);
Transform direkt setzen ohne Warp (der Agent schnappt zurück).

## 2026-11-04 — Rig-Naht gezogen: Variante A, der Brief nennt sein Rig

Was: Alle vier Bau-Briefe im `PathGridNet` tragen als ersten Parameter
`int rigId` — Anfragen wie Durchsagen. Der Host wacht als
Revier-Wache: `GetGameId(SenderClientId) != rigId` → stille Ablehnung;
danach holt er Grid und View aus dem Rig-Register des Bretts
(`MatchSetup.GetRigGrid` und neu `GetRigView` samt `_rigViews`-Feld).
`rigId == gameId` ist Spielregel, keine Namensdopplung: das Brett sagt
*wer*, der Brief *wo*. Sender halten ihre Id als Feld (der
BuildModeController löst sie mit dem Grid auf, die Queue über
`OwnerClientId`); das Kachel-Panel bekommt sie beim Öffnen mitgegeben
(`OpenForTile(cell, rigId)`), weil es kein NetworkBehaviour ist. Eine
`IsInside`-Wache im Controller schließt zugleich das Leck, dass sich
Panels fremder Kacheln öffnen ließen. Ergebnis im Doppeltest: Jeder
baut nur noch auf dem eigenen Feld. Der `MonsterSpawner` war bereits
rig-richtig und blieb unangetastet.
Warum: Vorgezogen aus der benannten Naht vom 2026-10-31 („bis dahin
von Hand auf Rig_1 verdrahtet"), weil der Multiplayer-Doppeltest sonst
gegen ein falsch verdrahtetes Brett getestet hätte. Variante A behält
die eine Mailbox und macht die Adresse zum Briefinhalt — dieselbe
Host-misstrauisch-Linie wie alle bisherigen Wachen.
Verworfen: Variante B, ein Netz-Skript je Rig (vier Mailboxen, mehr
Szenen-Verdrahtung, kein Gewinn bei vier Rigs); Grid und View je
Aufruf frisch suchen statt Register (wiederholte Suche — und die
Zuordnung gehört dem Brett, Besitzfrage); den Parameter nach gameId
umbenennen (der Brief adressiert ein Rig; dass der Wert der Game-Id
gleicht, ist Spielregel und steht im Glossar).

## 2026-11-04 — Bühne statt Spezialfälle: IUiMode und ActiveUiMode (Bau gestartet)

Was: Die UI-Exklusivität wird verallgemeinert. Jeder UI-Modus — die
Info-Panels, das Kachel-Werkzeug, später der Sende-Ring — implementiert
`IUiMode { void ExitMode(); }`; eine statische Registratur
`ActiveUiMode` (`Claim`/`Release`) hält, wer auf der Bühne steht, und
lässt beim Claim den Vorgänger abtreten. Ablage nach der neuen
Interface-Regel: `Scripts/Interfaces/UiMode/IUiMode.cs` (**gebaut am
2026-11-04, Block 1**) und `Scripts/UiMode/ActiveUiMode.cs`
(Block 2, offen). Nach dem Umbau fallen die Spezialfälle: das statische
`_currentOpenPanel` samt `CloseOpenPanel` in der Panel-Basis und das
Panel-Schließen im `ToggleTileTool`.
Warum: Isors Befund — Panel-gegen-Panel und Werkzeug-gegen-Panel waren
schon zwei Paar-Spezialfälle, und jeder neue Modus hätte weitere Paare
erzeugt („unsere Architektur wird grad schlechter"). Die Bühne macht
Exklusivität zu einer Regel mit genau einem Besitzer.
Verworfen: Observer-Events zwischen den Beteiligten (mehr Verdrahtung,
Reihenfolge unklar, und es blieben Paare); beim Zwischenstand bleiben
(trägt nicht über P-B5 hinaus).
Nachtrag 2026-11-05/07: Blocks 2 und 3 sind gebaut, die
Alt-Spezialfälle (`_currentOpenPanel`, `CloseOpenPanel`,
Panel-Schließen im Werkzeug) sind gelöscht — Sichtprüfung sechs
Punkte grün (LOG). Korrektur zum Block-1-Halbsatz oben: Das `public`
am Interface-Vertrag **bleibt bewusst stehen** (Isor, 2026-11-05: es
zeigt direkt, was es ist — Lesbarkeit schlägt die Redundanz-Regel);
die ursprüngliche Fassung dieses Eintrags behauptete das Gegenteil.

## 2026-11-04 — Aufräum-Durchgang: das Ordnungssystem angewandt

Was: Das neue Kern-Ordnungssystem (`Kern/DECISIONS.md` 2026-11-04,
Regeln in `CODE_GUIDELINES.md`) in einem Durchgang auf den ganzen
Bestand angewandt — Isor im Editor, Claude mit Arbeitsliste und
Datei-Kontrolle. Projektspezifische Festlegungen dabei:
**`Scripts/Sending/`** ist eigenes System (SendBuilding +
SendBuildingSelector; der Sende-Ring aus P-B5 kommt dazu) — das
Wort „Building" im Namen macht das Sendegebäude nicht zum Bausystem.
`MonsterSpawner` → `Monsters/` (Netz ist sein Werkzeug, nicht sein
Fach), `BuildOrderQueue` → `Building/` (liegt nur netz-bedingt auf
dem Spieler-Prefab). Beide Szenen tragen die drei Zonen; die
NavMesh-Blocker heißen englisch (`NavBlock_River_…`) und wohnen in
World — die Sperre liegt an einem Ort. `MatchSetup` bleibt auf
GameNetwork: NetworkBehaviour braucht einen gespawnten Netz-Träger,
ein eigenes Empty hätte die Brett-Synchronisation still beendet.
Funde des Kontroll-Laufs: Material mit Textur-Kürzel
(`T_ClickMarkerRing.mat` → `M_`), LobbyPlayer-Prefab war beim
Umbenennen zu „P_NetworkManager" geworden (Skript-Beweis per GUID,
Namenstausch in zwei Schritten, nichts gebrochen — Unity referenziert
GUIDs, nicht Namen). Play-Test Host + Client danach sauber.
Warum: Isors Stopp vor der Weiterarbeit — zu viele Baustellen ohne
sichtbares Ordnungssystem; Regeln standen verstreut und der Bestand
wich ab. Die System-Frage statt Träger-Frage löst genau die Fälle,
die ihn störten (Send-Zeug unter Player, Spawner unter Networking).
Verworfen: Sendegebäude in `Building/` lassen (Wortgleichheit ist
kein Sortierkriterium) · MatchSetup auf ein eigenes Szenen-Empty
(sichtbarer, aber funktional tot) · Testarea von den Regeln
ausnehmen (gerade dort wird umgebaut).
Offen als Merkposten: `Settings/`-Template-Reste (SampleSceneProfile,
Mobile_*) erst nach Graphics-Prüfung anfassen · Testarea-Wandnamen
(„WallVerical", Leerzeichen) bei Gelegenheit · `Assets/Editor/`
entsteht erst mit dem ersten reinen Editor-Skript ·
MainMenu-Zonen erst bei der Menü-Überarbeitung (Isor, 2026-11-04).

## 2026-11-07 — Werkzeug-Politik präzisiert: Formeln ja, Code nein

Was: Der Algorithmen-Teil der Werkzeug-Politik vom 2026-10-30 ist
geändert: Bei mathematischen Algorithmen (etwa dem Monster-Routing)
liefert Claude **nur Herleitung und Formeln** — den Code tippt Isor,
wie allen übrigen Spiel-Code. Komplett von Claude geschrieben (und im
Header deklariert) werden weiterhin ausschließlich Editor-Tools. Löst
aus dem Eintrag „2026-10-30 — Werkzeug-Politik" den Halbsatz „ebenso
die Herleitung und **Umsetzung** mathematischer Algorithmen" ab; der
Tool-Teil samt `Tool_`-Präfix und Deklaration gilt unverändert.
Warum: Isors Einspruch beim Routing-Start — ein Algorithmus ist
Spiel-Logik, die er bei der Abgabe verteidigen muss, kein Werkzeug
neben dem Spiel. „Du gibst mir Formeln, an die ich mich halte; ich
tippe trotzdem."
Verworfen: das Routing komplett von Claude schreiben lassen (stand so
in ROADMAP und Politik — übt genau das nicht, was das Semester prüft).

## 2026-11-07 — Zellinhalt statt Belegt-Bit: CellContent, zwei Fragen

Was: Die Bau-Tabelle im `PathGrid` speichert je Zelle ein
`CellContent`-Enum statt eines bool: `Empty` (zwingend Mitglied 0 — ein
frisches Enum-Array ist lauter Nullen, die Tabelle startet gratis
leer), `Tile`, `Tower` (vorgemerkt, erster Schreiber kommt mit P-B7);
Reihenfolge für immer fix (Enum-Sicherheit), Neues hängt hinten an.
Darauf zwei Fragen mit zwei Besitzern: `IsOccupied` ist die
**Bau-Frage** (belegt?, außerhalb zählt als belegt — Vertrag
unverändert), neu `HasTile` die **Lauf-Frage** (trägt die Zelle eine
Kachel?, außerhalb zählt als nein — da läuft niemand). `SetContent`
ersetzt `SetOccupied`; alles Laufende (`CollectReachableCells`,
`CanReachExit`) fragt `HasTile`. Ablage: eigener Ordner
`Scripts/Enums/<System>/`, **eine Datei je Enum** — spiegelt die
Interface-Regel vom 2026-11-04.
Warum: Türme sind sicher, und ein bool kann „belegt" nicht von
„begehbar" trennen — das Routing wäre später über Turm-Zellen
gelaufen. Isors Forderung an der richtigen Stelle: Wir brauchen die
Unterscheidung **jetzt** (das Routing ist ihr erster Verbraucher),
also wird sie richtig gebaut statt als Fassade über dem bool —
Architektur-Sauberkeit vor Umbaugröße. Der zentrale Enums-Ordner mit
System-Unterordnern ist Isors Vorschlag, analog zu den Interfaces.
Verworfen: `HasTile` als Fassade über dem bool (Claudes erster
Vorschlag — nach Umbaugröße statt Zuständigkeit sortiert, von Isor
gekippt); alle Enums gesammelt in einer Datei (beim Suchen und in der
Versionsgeschichte unhandlich); das Enum in `PathGrid.cs` deklarieren
(fachlich gleichwertig, gegen die Ordner-Einheitlichkeit).

## 2026-11-07 — Wander-Routing: Planen beim Spawn, Zähler je Gabelungszelle

Was: Das Wander-Modell (Beschluss 2026-10-30) wird so umgesetzt:
**(1)** Der neue `WanderRouter` (ein Skript je Rig, `Building/`) baut
die **komplette Route beim Spawn** auf dem Host; das Monster läuft
stumpf seine fertige Wegpunktliste ab wie bisher — es denkt unterwegs
nicht. Sicher ist das durch die bestehende Kachel-Sperre „verlegt wird
nur, solange keine Monster im Gebiet unterwegs sind" (2026-10-17): Das
Gitter ist während des Laufs eingefroren. **(2)** An jeder Zelle
entsteht die **Kandidatenliste frisch** (Nachbar hat Kachel + nicht
besucht + `CanReachExit` ohne die Besucht-Liste sagt Ja) — einen
gespeicherten Kacheltyp gibt es nicht, der „Typ" liegt in den
Nachbarn. **(3)** Das Abwechseln an Gabelungen trägt ein
**Zähler je Gabelungszelle** (`Dictionary<Vector2Int, int>`, Schlüssel
= Zelladresse): Wahl = `zähler % kandidatenzahl`, danach +1; gefragt
wird nur bei mehr als einem Kandidaten, und der Zähler lebt die ganze
Partie — so verteilt sich der Monsterstrom an jeder Gabelung
zuverlässig auf alle Arme, die Dreier-Kreuzung gratis mit. Ein Nein
von `CanReachExit` ist eine normale Antwort (Sackgassen-Arm steht
nicht zur Wahl), kein Fehler. Benannte Naht: Live-Umplanen bei
Kachel-Änderung als Ausbaustufe (Router rechnet Restrouten auf ein
Umbau-Ereignis neu) — mit der Einfrier-Regel in V1 ohne Anwendungsfall.
Warum: Besitz-Trennung — der Router besitzt das Planen, das Monster
das Laufen; `Monster` frisst heute schon eine Wegpunktliste, nur der
Absender wechselt. Der Zähler je Zelle ist die einzige geprüfte
Variante ohne Parity-Falle: Ein globaler Zähler (und ebenso einer je
Kreuzungs-Typ) kommt bei zwei Gabelungen auf der Strecke an der ersten
immer mit demselbem Rest an — alle Monster biegen gleich ab, die
Verteilung friert ein. Ein Richtungs-Enum als gespeicherter Wert
scheitert daran, dass das Angebot einer Zelle je Ankunftsrichtung und
Besucht-Liste anders ausfällt.
Verworfen: Entscheiden beim Schritt statt beim Spawn (Monster würde
Planer und Läufer zugleich, Flutfüllungen in jedem Schritt — als
Live-Reaktion durch die Einfrier-Regel ohnehin unnötig); ein globaler
0/1-Wechsler und ein Zähler je Kacheltyp (Isors Kandidaten — beide
Parity-Falle, dazu beruhte die Typ-Zählung „12 Varianten" auf einer
festen Laufrichtung, die es auf Schlängelwegen nicht gibt);
gespeicherte letzte Richtung je Gabelung (veraltet je Besucher).

## 2026-11-08 — Lauf-Regel: Distanzfeld statt Abwechseln an jeder Gabelung

Was: Die Monster laufen nur noch **kürzeste Wege zum Ausgang**; das
Abwechseln (Zähler je Gabelungszelle, Beschluss 2026-11-07) greift nur
noch bei **Gleichstand** mehrerer gleich kurzer Arme. Umsetzung:
**(1)** `PathConnectivity` bekommt ein **Distanzfeld** (*flow field*) —
eine Flutfüllung vom Ausgang, die jeder Wegzelle ihre Schrittzahl bis
zum Ziel gibt. **(2)** Das Sieb in `WanderRouter.CollectCandidates`
schrumpft auf einen Vergleich: Kandidat ist ein Nachbar genau dann,
wenn seine Distanz um 1 kleiner ist als die der aktuellen Zelle.
Besucht-Liste und `CanReachExit`-Aufruf fliegen aus dem Sieb —
zahl-abwärts kann weder kreisen noch in Sackgassen laufen
(`CanReachExit` bleibt für Bau-Regel und Gizmo bestehen). **(3)** Das
Feld wird **gecacht mit Dirty-Flag**: `PathGrid` zählt bei jedem
Legen/Abreißen einen Änderungszähler hoch; `PathConnectivity` merkt
sich Feld samt Zählerstand und rechnet nur neu, wenn der Zähler
abweicht. Mit der Einfrier-Regel (kein Bauen, solange Monster laufen)
rechnet so faktisch das erste Monster jeder Runde einmal, der Rest
liest gratis — Isors „einmalig zu Rundenbeginn", ohne an den
P-B5-Takt gekoppelt zu sein und ohne Reset-Pflicht. Benannte Nähte:
Live-Umplanen bei Kachel-Änderung (durch die Einfrier-Regel in V1
ohne Anwendungsfall) und Monster, die live am Feld laufen statt mit
gebackener Wegpunktliste (erst bei Einheitenzahlen, die die Liste
teuer machen).
Warum: Der erste Routing-Sichttest (2026-11-08) zeigte: Abwechseln an
**jeder** Gabelung erzeugt Umwege, die vom Ziel wegführen — kein
Spieler kann den Lauf vorhersehen, Wege „ergeben keinen Sinn" (Isors
Befund samt Soll-Skizzen). Spieler-Erwartung im TD ist der kürzeste
Weg; Splitten soll es nur zwischen gleich kurzen Wegen geben. Das
Distanzfeld ist dafür das Genre-Standardmuster und macht den Code
einfacher statt komplexer (ein Vergleich statt drei Prüfungen, ein
Zustand weniger). Besitz-Trennung bleibt: `PathConnectivity` liefert
Fakten (Zahlen), `WanderRouter` trifft die Wahl (Zähler bei
Gleichstand), Spawner und Monster bleiben unberührt.
Verworfen: Abwechseln an jeder Gabelung beibehalten (gespielt
widerlegt, s. o.); Distanzfeld frisch pro Spawn ohne Cache (Claudes
V1-Vorschlag — funktional gleichwertig und simpler, aber „einmal pro
Runde" ist das richtige Modell, und der Zähler-Cache kostet nur drei
Zeilen im PathGrid); Rundenbeginn-Condition im `MonsterSpawner`
(Isors erster Kandidat — hängt am P-B5-Takt, den es noch nicht gibt,
braucht eine Reset-Pflicht, die vergessen werden kann, und zieht
Feld-Pflege in den Spawner, dem sie nicht gehört); A*-Pfadsuche je
Monster (teurer und fehleranfälliger, wenn alle Einheiten zum selben
Ziel wollen).

## 2026-11-08 — Monster-Höhe: Brett besitzt die Kacheldicke, Steckbrief den Körper

Was: Wegpunkte liegen auf der **Lauffläche**: `PathGrid` bekommt
`_tileHeight` (Inspector, 0,1 — die gemessene Kacheldicke) und
`TranslateToSurfacePos` (Zellmitte plus Kacheldicke);
`WanderRouter.BuildRoute` übersetzt damit. Das Monster hebt sich
**selbst**: `HeightOffset` im Monster-Steckbrief (halbe Körperhöhe,
Grunt 1,0), beim Spawn einmal und an jedem Wegpunkt-Ziel angewandt.
`TranslateToWorldPos` bleibt unverändert — Geisterbild, Gizmos und
Platzierung rechnen weiter mit dem Boden.
Warum: Zwei Besitzer, zwei Werte — ein Monster soll die Kacheldicke
nicht kennen (dickere Kacheln hießen sonst alle Steckbriefe
nachziehen), das Brett nicht die Körpergröße. Die Hand-Eichung
(0,85/0,9) entpuppte sich als „halbe Kapselhöhe minus
TileHeight-Irrtum"; nach der Korrektur auf 0,1/1,0 tragen beide
Zahlen wörtliche Bedeutung (Regel fürs nächste Monster: HeightOffset
= halbe Körperhöhe, fertig).
Verworfen: ein kombinierter Offset je Monster-SO inklusive
Kacheldicke (Isors erster Gedanke, von ihm selbst zur
Zwei-Werte-Trennung geschärft); `TranslateToWorldPos` anheben (hätte
Geisterbild und Platzierung mit verschoben).

## 2026-11-08 — Prüfpunkt P-B4: Plan halten, Bau-Komfort als P-B6a vorgezogen

Was: Der im Meilenstein-Plan vorgesehene Prüfpunkt nach P-B4 ist
entschieden: **P-B7 (erster Wächter) wird nicht vorgezogen** — es
bleibt bei P-B5 → P-B6 → P-B7. Neu eingeschoben wird **P-B6a
„Bau-Komfort"** (~2–3 h) zwischen P-B6 und P-B7: Halte-Bauen (bei
gehaltener Maustaste ziehen, Geisterbilder zeigen die Reihe,
Loslassen baut) und der Abriss-Modus als drittes Werkzeug — beide von
der P3-Merkliste vorgezogen.
Warum: Das Vorzieh-Argument (früher Spaß-Test) ist schwach geworden —
das Risiko-Stück des Prototyps war das Routing, und es läuft seit
heute; der Wächter braucht Gold und Preise aus P-B6, um sinnvoll
testbar zu sein. Bau-Komfort rückt vor, weil jede Testrunde bis zur
Abgabe Wege baut und abreißt — das Werkzeug verzinst sich ab dem
ersten Playtest (Isors Testschmerz vom 08.11.: „alles zu löschen ist
echt schwer").
Verworfen: P-B7 vorziehen (s. o.); Bau-Komfort sofort vor P-B5
(hätte den P-B5-Start am Soll-Sonntag gekostet); Bau-Komfort auf P3
lassen (der Testschmerz bliebe bis zur Pufferwoche).
