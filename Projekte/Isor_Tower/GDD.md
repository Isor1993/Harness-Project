# GDD.md — Design-Absicht Isor's Tower

Ownership: Design-Absicht des Spiels — was es sein soll, nicht wie es
gebaut wird. Technische Umsetzung gehört in `DECISIONS/` und `TDD_NOTES.md`;
Aufbau und Pflege dieser Datei regelt `Kern/GDD_RULES.md`.

Short GDD, wächst mit. **`offen` ist ein gültiger Eintrag** und markiert
die Stellen, an denen die Architektur eine Tür offen halten muss — wer
sie verschweigt, baut die Tür zu. Kein Stand-Stempel: Es gibt keine
Prüfung, die ihn kontrollieren würde (`Kern/DOC_RULES.md`, Abschnitt 7).

Vom eigentlichen Design ist bisher nichts gebaut — Bauen mit Grid,
kaufbare Häuser, Turm, Portale, Handwerk, Quests stehen alle noch aus.
Was existiert (Village-Szene, Terrain, Gras, Schafe, Menüs), ist die
technische Grundlage darunter.

## Pitch
Ein RPG mit zwei Hälften: ein bleibendes Zuhause im Dorf, das der Spieler
aufbaut, und ein Turm, in dem er kämpft, levelt und erkundet. Was im Turm
erbeutet wird, fließt ins Dorf zurück.

## Kern-Schleife
Im Village vorbereiten (schmieden, kochen, Ausrüstung verbessern, Quests
bei der Adventure Guild holen) → durch ein Portal in einen Tower-Floor →
Mobs und Boss bekämpfen, Ressourcen sammeln, Gebiet erkunden → mit Beute
zurück ins Village → Zuhause ausbauen, Ausrüstung verbessern → nächster
oder derselbe Floor.

Der Spieler verbringt die meiste Zeit im Village (bauen, dekorieren,
schmieden, brauen); der Turm ist der Motor, der das Material dafür liefert.

## Welt-Struktur
Hub und Spokes, keine durchgehende Open World: Das Village ist der Hub,
jeder Tower-Floor ein eigenes, abgeschlossenes Gebiet („Paralleldimension").
Übergänge laufen ausnahmslos über Portale mit Ladevorgang — Village und
Floor sind nie gleichzeitig aktiv.

### Village (Hauptwelt)
- Dauerhaft, wird gespeichert. Der Spieler baut, dekoriert, pflanzt an,
  baut ab.
- Terrain fest, nicht bei jedem Start neu generiert. Prozedural ist hier
  höchstens die Bepflanzung / Objektplatzierung, nicht das Gelände selbst.
- Bauen auf einem Grid mit Snapping; Häuser sind kaufbar. Die bebaubare
  Fläche wächst in Stufen.
- Größe: zunächst in der Größenordnung des jetzigen Uni-Terrains
  (~2 km Kante). **Offen:** kann später um ein Vielfaches wachsen.
- Ressourcen respawnen über einen Pool mit Timer und einer Obergrenze,
  wie viele gleichzeitig in der Welt liegen dürfen.

### Tower-Floors
- Ein Turm mit mehreren Floors; jeder Floor ist ein eigenes Environment
  (z. B. Grasland mit Wald, Wüste).
- Inhalt je Floor: normale Mobs, Spezial-Monster, ein Boss. Boss besiegt =
  Floor freigeschaltet, der nächste öffnet sich.
- Ein freigeschalteter Floor ist dauerhaft betretbar (Grinden), wird aber
  bei **jedem** Betreten neu generiert und beim Verlassen verworfen.
  Gespeichert wird nur der Fortschritt, nie der Weltzustand.
- Nebenräume, Geheim-Floors und Easter Eggs sind vorgesehen.
- Größe variiert bewusst: kleine Floors zum Einstieg, später große, dazu
  mittlere. **Offen:** konkrete Größen.
- **Offen:** Anzahl der Floors nach oben offen — ein sehr hoher Turm oder
  mehrere Türme mit je eigener Floor-Spanne.
- **Offen:** Anteil freier Generierung gegenüber dem Kombinieren fester
  Bausteine. Vorstellung bisher: einige wenige Grund-Layouts, die
  variieren, plus prozedurale Platzierung darauf.

## Spieler
- Perspektive First und Third Person, im Spiel umschaltbar.
- Progression: Level, Ausrüstung, Handwerk (Schmieden, Kochen/Tränke),
  Quests über die Adventure Guild.
- Sichtweite groß — Open-World-Anmutung. Berge bleiben aus großer
  Entfernung sichtbar, nahe Details (Gras) dürfen in der Ferne stark
  vereinfacht werden.
- Größenordnung gleichzeitig sichtbarer Gegner: 40–50.

## Persistenz
- Gespeichert wird ausschließlich der Village-Zustand plus der
  Spielerfortschritt (Level, Ausrüstung, Inventar, freigeschaltete Floors).
- Beides wird **getrennt** gespeichert, weil beides verschieden weit
  reicht: Der Spielerfortschritt begleitet den Spieler in jede Welt, der
  Village-Zustand bleibt bei seinem Besitzer. Siehe „Multiplayer".
- Floors speichern nichts; abgebaute Ressourcen dort sind mit dem Floor weg.

## Multiplayer
- Koop für 4–5 Spieler. Der Koop ist **nicht mehr ein später Zusatz,
  sondern der Rahmen**, in dem alles Weitere entsteht: Ab dem dritten
  Semester wird jedes System von Anfang an netzwerkfähig gebaut. *(Diese
  Umkehr ersetzt die frühere Absicht „sehr spät, zuerst solo aufbauen" —
  Begründung in `DECISIONS/Multiplayer.md`.)*
- Jeder Spieler besitzt seine eigene Welt. Andere joinen als Gäste und
  dürfen dort kämpfen, looten, Ressourcen abbauen, bauen und das Handwerk
  mitbenutzen.
- **Der Charakter gehört dem Spieler, nicht der Welt.** Level, Erfahrung,
  Inventar, Ausrüstung, Rezepte, Quest-Fortschritt und freigeschaltete
  Floors reisen mit ihm in jede fremde Welt und wieder zurück. Was in der
  Welt bleibt, ist die Welt selbst: das Dorf mit allem, was darin gebaut,
  abgebaut oder gezähmt wurde.
- **Wer die Welt besitzt, hält sie.** Verlässt der Besitzer die Runde,
  endet sie für alle; die Gäste landen in ihrer eigenen Welt und behalten,
  was sie gesammelt haben.
- Gespielt wird als Gruppe: Ein Portal nimmt nach Bestätigung alle
  gemeinsam mit, sodass immer nur eine Welt aktiv ist. Wer fällt, liegt am
  Boden und kann von einem Mitspieler wieder aufgerichtet werden. Beute
  fällt für jeden Spieler getrennt — niemand nimmt einem anderen etwas weg.
- **Solo bleibt vollwertig.** Es ist dieselbe Welt mit einem einzigen
  Spieler, nicht eine abgespeckte zweite Spielart.

## Umfang und Ziel
Isor's Tower ist das durchgehende Studienprojekt: Jedes Semester zahlt auf
dasselbe Spiel ein statt auf getrennte Übungen. Ziel ist ein
veröffentlichungsfähiges Ergebnis, mindestens eine Demo.
Priorität: Das dritte Semester ist ein **Neustart desselben Projekts** —
neue Szenen, von Anfang an koop-fähig, im selben Repo. Was aus dem
zweiten Semester dasteht, wird nicht pauschal übernommen, sondern
Baustein für Baustein entschieden, wenn er gebraucht wird. Reihenfolge in
`Projekte/Isor_Tower/ROADMAP.md`, Abschnitt „Semester 3 — der
Koop-Prototyp"; der Bestand samt seiner Befunde in
`Projekte/Isor_Tower/ALTSTAND.md`; die Daten dazu im `LOG.md` derselben
Schicht.

## Offene Design-Fragen

**Dieses Dokument besitzt die offenen Design-Fragen.** Jede trägt eine
fettgedruckte Stichzeile als Namen, keine Nummer — beantwortete Fragen
werden gestrichen, und Nummern würden dabei rutschen. Die ROADMAP darf
sie als Aufgabe aufnehmen, aber nur über einen Verweis auf die
Stichzeile — nie durch Abschreiben. Beantwortet wird eine Frage in den DECISIONS; erst danach
wird sie hier gestrichen und die Absicht als feste Aussage ins Kapitel
geschrieben. Sonst stünde dieselbe Frage an zwei Orten.

- **Village-Größe:** bleibt es bei ~2 km oder wächst es um ein Vielfaches?
  (Entscheidet, ob die Welt streamen muss.)
- **Turmzahl:** ein hoher Turm oder mehrere Türme mit eigenen
  Floor-Spannen?
- **Generierungsanteil:** Wie viel eines Floors ist frei generiert, wie
  viel aus festen Bausteinen kombiniert?
- **Floor-Größenraster:** klein / mittel / groß in Metern.
- **Village-Terrain:** handgebaut, mit einem eigenen Tool erweitert, oder
  einmalig generiert und dann eingefroren?

## Entwurf — noch nicht einsortiert

Ergebnisse aus Brainstorm- und Design-Abschnitten landen hier sofort, roh
und unsortiert. Ein Eintrag hier ist **noch keine Absicht** — er bindet
nichts, und Claude darf sich nicht darauf berufen, als wäre er
entschieden. Einsortiert wird, wenn das zugehörige Kapitel das nächste
Mal angefasst wird; aus Entwurf wird feste Absicht, sobald Isor sie
bestätigt und sie in ihr Kapitel wandert.

Jeder Eintrag trägt sein Datum. Steht einer nach drei Monaten noch hier,
ist er entweder Absicht oder überholt — dann wird geklärt, welches.

Regeln dazu: `Kern/GDD_RULES.md`.

*(zurzeit leer)*
