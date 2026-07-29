# GDD.md — Design-Absicht Isor's Tower

Ownership: Design-Absicht des Spiels — was es sein soll, nicht wie es
gebaut wird. Technische Umsetzung gehört in DECISIONS.md / TDD_NOTES.md.

Status: Short GDD, Stand 2026-07-29. Gebaut ist davon noch nichts —
alles hier ist Absicht. Wächst mit; „offen" ist ein gültiger Eintrag und
markiert die Stellen, an denen die Architektur eine Tür offen halten muss.

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
- Floors speichern nichts; abgebaute Ressourcen dort sind mit dem Floor weg.

## Multiplayer
- Koop für 4–5 Spieler, **sehr spät** in der Entwicklung. Zuerst wird das
  Spiel solo aufgebaut.
- Modell: Jeder Spieler besitzt seine eigene Welt; andere joinen als Gäste,
  können dort Quests erfüllen und looten und nehmen Fortschritt und Beute
  in ihre eigene Welt mit.
- Multiplayer ist gesetzt, nicht optional — er wird nicht vorgebaut, aber
  bei Architekturentscheidungen mitgedacht.

## Umfang und Ziel
Isor's Tower ist das durchgehende Studienprojekt: Jedes Semester zahlt auf
dasselbe Spiel ein statt auf getrennte Übungen. Ziel ist ein
veröffentlichungsfähiges Ergebnis, mindestens eine Demo.
Priorität: Erst das laufende Semester abschließen (Portfolio 2026-08-21),
danach das Bestehende am GDD ausrichten.

## Offene Design-Fragen
1. Endgültige Größe des Village — bleibt es bei ~2 km oder wächst es um ein
   Vielfaches? (Entscheidet, ob die Welt streamen muss.)
2. Ein hoher Turm oder mehrere Türme mit eigenen Floor-Spannen?
3. Wie viel eines Floors ist frei generiert, wie viel aus festen Bausteinen
   kombiniert?
4. Größenraster der Floors (klein / mittel / groß in Metern).
5. Wird das Village-Terrain handgebaut, mit einem eigenen Tool erweitert,
   oder einmalig generiert und dann eingefroren?
