# DECISIONS.md — Entscheidungen Pathmakers TD

Ownership: Nur Entscheidungen zum Spielkonzept Pathmakers TD
(Arbeitstitel; Weg-Bau-Tower-Defense, Kandidat für das Semester-Spiel
des Moduls 5FSC0XD101_P) — was entschieden wurde, warum, und welche
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
