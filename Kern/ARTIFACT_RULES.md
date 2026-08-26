# ARTIFACT_RULES.md — Regeln für die Artifact-Seiten

Ownership: Typen, Benennung, Aufbau, Gestaltung, Symbole und Pflege der
Artifact-Seiten auf claude.ai. Warum eigene Datei: Artifacts sind eine
Ausgabeform wie das Knowledge-Archiv, keine Harness-Dokumente — dieselbe
Trennung wie bei KNOWLEDGE_RULES.md.

Welche Seiten es gibt und woran jede hängt: ARTIFACT_INDEX.md. Diese
Datei besitzt die Regeln, der Index den Bestand.

Zweck der Artifacts: die Handy-Fassung. Führende Quelle bleibt immer die
.md-Datei im Repo; das Artifact ist die lesbare Ansicht davon, unterwegs
und ohne Editor.

## Die Typen

| Typ | Beantwortet | Symbol | Führende Quelle |
|---|---|---|---|
| Status | Wo steht das Projekt, was kommt als Nächstes? | 📍 | `PLAN.md` + ROADMAP der Schicht |
| System | Wie funktioniert *mein* System X? | ⚙️ | LOG und DECISIONS der Schicht |
| Lernstück | Wie funktioniert Konzept Y — auch außerhalb dieses Projekts? | 💡 | `TDD_NOTES.md`, Knowledge-Ordner |

Der Harness selbst ist ein System im Sinne dieser Tabelle:
`⚙️ System · Harness`, führende Quelle sind die Kern-Dateien.

`🗑` ist **kein Typ, sondern ein Zustand** — eine Seite kann veraltet
*sein*, sie ist nicht veraltet *als Sorte*. Siehe Abschnitt Pflege.

**`(geplant)` ist ebenso ein Zustand.** Eine Seite, die ein noch
**ungebautes** System entwirft, stellt dieselbe Frage wie eine
System-Seite, nur im Futur: „Wie *soll* mein System X funktionieren?"
Sie bleibt deshalb ⚙️ System und trägt den Zusatz `(geplant)` im Titel
(siehe Benennung). Ist das System gebaut, fällt der Zusatz weg — Symbol,
Thema und URL bleiben über die ganze Lebenszeit dieselben.

Der **Zustand einer Seite** sagt damit etwas anderes als ihr Typ: Der Typ
nennt die Sorte und bleibt, der Zustand nennt den Lebensabschnitt und
wandert — `(geplant)` vor dem Bau, nichts danach, `🗑` am Ende.

Woran der Zustand hängt: **nicht** daran, ob jede Zeile steht, sondern
daran, ob die Seite überwiegend Absicht beschreibt. Den Schnitt macht
der Pflegetag, nicht der erste Commit („Wann geschaut wird").

Warum kein eigener Typ: Der Typ sagt, *worauf* eine Seite blickt, und
darauf blickt eine Absichtsseite genauso wie die spätere System-Seite —
sie ist dasselbe Ding zu einem früheren Zeitpunkt. Derselbe Maßstab hat
schon `🗑` und `🎓 Zeugnis` aus der Typ-Tabelle herausgehalten.
*(Entschieden 2026-08-26, Begründung und Alternativen in `DECISIONS.md`.)*

**Trennlinie System ↔ Lernstück:** System ist projektspezifisch („so ist
mein Placement aufgebaut"), Lernstück ist übertragbar („so funktioniert
Poisson-Disc-Sampling"). Ein Artifact beantwortet genau eine der Fragen —
beantwortet es zwei, wird es geteilt.

**Wann überhaupt eine Seite entsteht:** auf Zuruf, und bei Wissensseiten
dann, wenn das Thema visuell ist (`KNOWLEDGE_RULES.md`). Reiner Text
braucht keine zweite Fassung.

**Beim Teilen behält das Lernstück die URL.** Das Übertragbare veraltet
nicht, die Projektbeschreibung schon; der gemerkte Link soll am
Stabileren hängen.

**Nicht von dieser Datei geregelt: die Zeugnis-Seiten (🎓).** Sie sind
kein vierter Typ — die drei Typen sagen, *worauf* eine Seite blickt, ein
Zeugnis bewertet dagegen. Aufbau und Darstellung folgen den Regeln hier,
die Pflege nicht: Jedes Zeugnis behält seine eigene URL und wird nie
aktualisiert. Diese Ausnahme besitzt ASSESSMENT_RULES.md, geführt werden
die Seiten trotzdem im ARTIFACT_INDEX.

## Benennung

Titel-Schema: `<Symbol> <Typ> · <Thema>`, hinten optional `(<Zustand>)`

    📍 Status · Wo das Projekt steht
    ⚙️ System · Terrain & Gras
    ⚙️ System · Multiplayer (geplant)
    💡 Lernstück · Poisson-Disc-Sampling
    🗑 Löschen · Village spielbar

Symbol **und** Wort: Das Symbol allein ist in der Galerie zu klein zum
Scannen, das Wort allein sagt es erst beim Lesen.

**Die Klammer trägt den Zustand, nicht das Symbol** — außer bei `🗑`,
dessen Zustand das Ende der Lebenslinie ist und die Seite deshalb aus
ihrem Typ herausnimmt. `(geplant)` steht dagegen am Anfang: Die Seite
lebt weiter, nur ohne Klammer. Bisher gibt es diesen einen Zustand;
kommt je ein zweiter dazu, gehört er in denselben Klammerplatz.

## Aufbau einer Seite

Von oben nach unten, immer gleich — damit jede Seite gleich zu lesen ist
und man beim Überfliegen weiß, wo was steht.

1. **Kopf**: Kind-Badge mit Symbol und Typwort, daneben eine Zeile, die
   das Thema einordnet. Darunter die Überschrift (Thema allein, ohne
   Symbol und Typ — die stehen schon im Badge).
2. **Vorspann**: ein Satz, was die Seite beantwortet.
3. **Stand-Stempel**: Datum, gegen das geprüft wurde. Wurde nur ein Teil
   frisch geprüft, wird das getrennt hingeschrieben („Stand 06.08.,
   Werkzeug-Abschnitt 08.08.") statt alles auf das neue Datum zu heben.
4. **Abschnitte**: nummeriert nur, wenn die Reihenfolge etwas bedeutet
   (Ablauf, Stufen). Sonst ohne Nummern.
5. **Fußzeile**: Stand, führende .md-Datei, Links auf verwandte Seiten.

Breite Tabellen und Diagramme kommen in einen eigenen Scroll-Bereich —
sonst schiebt sich die ganze Seite auf dem Handy seitwärts.

## Gestaltung

**Alle Seiten teilen eine Farbwelt.** Sie ist warm und dunkel, und es
gibt sie **nur in einer Fassung** — kein Hell-Modus, keine zweite
Farbtabelle. Grund: Eine Seite mit Stimmung soll nicht in zwei Versionen
zerfallen, gelesen wird auf dem Handy, und die zweite Fassung wird
ohnehin nie ernsthaft geprüft. Jede Farbe wird ausgeschrieben, damit die
Seite auf jedem Grund gleich aussieht.

**Fest sind Palette, Schriftrollen und der Aufbau oben. Alles andere
entscheidet der Inhalt** (Isor, 2026-08-23) — wie viel visualisiert wird,
welche Diagrammform passt, wie dicht die Seite ist. Abweichen ist
erlaubt und erwünscht, solange die Seite als Teil der Familie erkennbar
bleibt.

### Palette

| Rolle | Wert | wofür |
|---|---|---|
| Grund | `#17130F` | Seitenhintergrund |
| Grund tief | `#120F0C` | abgesetzte Abschnitte |
| Fläche | `rgba(43,35,28,0.62)` | Tafeln, Karten, Tabellen — **durchscheinend** |
| Linie | `rgba(239,228,210,0.13)` | Kanten, Trenner |
| Text | `#EFE4D2` | Pergament, der Grundton |
| Text gedämpft | `#A2947F` | Beschreibungen, Bildunterschriften |
| Text schwach | `#756758` | Tafelnummern, Spaltenköpfe |
| **Ember** | `#D9762B`, hell `#F2A64B` | der eine Akzent — Marken, Hervorhebung |

Dazu die **Kategorie-Farben**. Sie sind nicht Dekoration, sondern
tragen Bedeutung: Wer eine Seite mit Kategorien baut (Schichten, Typen,
Zustände), gibt jeder eine davon und benutzt sie durchgehend — im
Diagramm, in der Tabelle, im Abschnittsstrich.

| Name | Wert |
|---|---|
| Verdigris | `#7FBBA6` |
| Amber | `#E9A44C` |
| Blau | `#8FA1D8` |
| Ton | `#DE7A63` |

### Schrift — die Rollen

| Rolle | Familie | wofür |
|---|---|---|
| Anzeige | eine Serif mit Charakter (`Newsreader`, ersatzweise Palatino) | Titel, Überschriften, Merksätze |
| Text | eine humanistische Sans (`IBM Plex Sans`) | Fließtext — Lesbarkeit vor Charakter |
| Technik | eine Mono (`IBM Plex Mono`) | Pfade, Zahlen, Marken, Tafelnummern |

Nur Google Fonts oder Systemschriften — andere Quellen lädt die
Artifact-Umgebung nicht, und die Seite fällt dann still auf Arial zurück.

### Bauteile

- **Rundungen überall**: 18 px an Tafeln und Merksätzen, 11 px an
  Karten, Pillenform an Marken und Sprungmarken. Nichts wird hart
  abgeschnitten.
- **Lichtschein statt Flächen**: Jeder Abschnitt trägt oben links einen
  weichen Farbverlauf in seiner Kategorie-Farbe. Das ist der Unterschied
  zwischen „lebendig" und „flach" — ohne ihn sehen alle Abschnitte gleich
  aus, egal wie viele Farben sonst vorkommen.
- **Wechselnder Grund**: Abschnitte laufen über die volle Breite und
  wechseln zwischen `Grund` und `Grund tief`. Beim Scrollen soll etwas
  passieren.
- **Tafeln** für Diagramme: eigene Fläche, Nummer und Kurztitel oben
  (`Tafel 3 — Ownership an einem Beispiel`), Bildunterschrift darunter.
  So lässt sich im Text darauf verweisen.
- **Diagramme hochkant** bauen, Breite höchstens 460 px. Ein
  querformatiges Diagramm schrumpft auf dem Handy so weit, dass die
  Beschriftung unlesbar wird.
- **Kennzahlen groß**: Eine Zahl, die etwas belegt, gehört in eine eigene
  Kachel mit Anzeigeschrift, nicht in den Fließtext.

### Wie viel visualisiert wird

Der Inhalt entscheidet, nicht die Regel. Als Anhalt:

| Die Seite erklärt … | dann braucht sie … |
|---|---|
| einen Ablauf oder Kreislauf | ein Flussdiagramm, hochkant |
| eine Aufteilung oder Rangfolge | ein Schichtbild oder eine Verzweigung |
| ein Verhältnis oder eine Größe | einen Balken plus die Zahl daneben |
| Werte und Grenzen | eine Tabelle — kein Bild |
| eine Regel | einen Merksatz, groß gesetzt |

Die Untergrenze aus `WORKFLOW.md` gilt auch hier: nie auf inneres
Vorstellen ausweichen. Was kein Bild bekommt, bekommt Zahlen.

### Seiten als Muster

- `⚙️ System · Harness` — der Bauplan dieser Regeln, mit vier Tafeln.
- `Isor's Tower Menü-Politur` — die Seite, aus der die Farbwelt stammt;
  dort auch, wie man eine Bühne mit Verlauf, Schleier und
  durchscheinender Tafel baut.

Beide stehen mit URL im `ARTIFACT_INDEX.md`.

### Der Altbestand

Sieben der acht älteren Seiten stehen in einer kühlen hellen Fassung
(Stand 2026-08-06/08). Sie werden **nicht eigens nachgezogen**, sondern
beim nächsten inhaltlichen Anfassen mitgenommen — sie sind ohnehin
überholt, und wer sie aktualisiert, baut sie gleich neu. Bis dahin ist
die Sammlung zweigeteilt, und das ist bekannt.

**Die Ausnahme ist `💡 Lernstück · Terrain-Fallen`:** Sie ist bereits
dunkel gebaut und trägt im Quelltext den Kommentar „Fest dunkles Theme —
bewusste Entscheidung, keine Light-Variante". Sie hat die Regel
vorweggenommen, nur in eigener Palette (Grün `#5fae88`). Für sie ist der
Umbau ein **Palettentausch statt Neubau** — die billigste Seite des
Bestands und deshalb der sinnvolle Testlauf für die Hausfarbwelt.
*(Nachgetragen am 2026-08-23: Die ursprüngliche Fassung sagte pauschal
„die älteren Seiten", ohne dass jemand die Seiten dafür abgerufen
hatte.)*

## Wann geschaut wird

- **Bevor man sich auf eine Seite stützt:** die echte Seite aufrufen, nie
  aus der Erinnerung oder aus einer älteren Fassung zitieren. Seiten
  altern zwischen zwei Sessions.
- **Vor dem Coden:** Der Artifact-Check ist ein Punkt des Review-Gate in
  `CODE_GUIDELINES.md`. Dort steht er vollständig — eine Checkliste
  gehört dem Moment, an dem sie abgearbeitet wird, nicht den Themen ihrer
  Punkte.
- **Sonntags, am Pflegetag:** Claude gleicht den ARTIFACT_INDEX gegen die
  Änderungen der Woche **und** gegen die Liste der tatsächlich
  veröffentlichten Seiten ab und legt eine Vorschlagsliste vor — welche
  Seite veraltet ist, was drinsteht, was sich geändert hat. Isor
  entscheidet, welche nachgezogen werden; Claude ändert nichts von selbst.
  Der Abgleich gegen die echte Veröffentlichungsliste ist die zweite,
  unabhängige Quelle: Ein falscher Stand-Stempel blieb sonst zehn Tage
  unbemerkt.
  **Dazu, seit 2026-08-25, eine Seite gründlich:** Der Abgleich sieht
  nur Metadaten — am 2026-08-23 meldete er drei Funde, eine gründliche
  Durchsicht derselben acht Seiten fand rund dreißig. Deshalb wird je
  Pflegetag zusätzlich genau **eine** Seite inhaltlich geprüft: die
  echte Seite abrufen, jede Aussage und Zahl gegen Code und führende
  Quelle halten, Befunde in die Vorschlagsliste. **Dran ist die
  lebendige Seite mit dem ältesten Stand-Datum im `ARTIFACT_INDEX.md`.**
  Das braucht keinen eigenen Zeiger und heilt sich selbst: Eine beim
  Coden nachgezogene Seite (Review-Gate) trägt ein frisches Datum und
  rückt von allein ans Ende. Außerhalb des Turnus stehen die Seiten,
  die der Index als nicht-nachziehbar führt — Zeugnisse, die
  Muster-Seite und die Harness-Seite (ihr Stand hängt an der
  Versionsnummer). Der Metadaten-Abgleich bleibt daneben bestehen: Er
  ist die Prüfung, die die Stand-Stempel erlaubt macht (`DOC_RULES.md`,
  Abschnitt 7).
  **Eine Seite im Zustand `(geplant)` bleibt im Turnus**, wird aber gegen
  ihre führende Quelle geprüft statt gegen Code — den gibt es noch nicht.
  Zwei Fragen kommen dazu: Gilt die Absicht noch, oder hat eine spätere
  Entscheidung sie überholt? Und beschreibt die Seite inzwischen
  überwiegend Zustand statt Absicht — dann greift der Handgriff unten
  unter „Pflege". Sie aus dem Turnus zu nehmen wäre falsch: Eine Absicht
  veraltet schneller als ein gebautes System, weil sie nichts festhält,
  was man nachmessen könnte.
- **Inhalt aus einer alten Seite übernehmen:** gegen den Code prüfen,
  nicht abschreiben. Was auf einer Seite steht, war zum Stand-Datum wahr.

## Wo das Symbol steht

- **Favicon** beim Publish — erscheint im Browser-Tab und auf der
  Galerie-Karte.
- **Kind-Badge im Seitenkopf** (`.kindbadge` im Eyebrow), damit der Typ
  auch beim Lesen sichtbar bleibt.

Beides trägt dasselbe Symbol wie der Titel. Favicon bei Updates **nie
ändern** — der Nutzer findet seinen Tab am Icon wieder.

## Pflege

- Bestehende Seite **aktualisieren statt neu anlegen**: beim Publish die
  vorhandene URL mitgeben, sonst entsteht ein zweiter Link zum selben Thema.
- Veraltete Seiten nicht löschen, sondern auf `🗑 Löschen · …` umbenennen —
  so bleibt nachvollziehbar, was einmal galt.
- **Ist das Geplante gebaut, fällt `(geplant)` aus dem Titel** — gleiche
  URL, gleiches Symbol, gleiches Thema; nur die Klammer geht weg, und im
  ARTIFACT_INDEX wird aus dem Sonderfall-Vermerk eine gewöhnliche
  Skripte-Zeile. Ausgelöst wird der Handgriff am Pflegetag (oben, „Wann
  geschaut wird"), nicht vom ersten Commit: Ob eine Seite noch Absicht
  beschreibt, sieht man ihr an, nicht der Versionsgeschichte.
- Jede Änderung am Bestand — neue Seite, Teilung, Umbenennung, Löschung —
  wird im ARTIFACT_INDEX.md nachgetragen. Gelöschte Seiten kommen dort in
  die Tabelle „Gelöschte Seiten", damit eine tote ID erklärbar bleibt.
- **Vor dem Löschen oder Teilen** im Knowledge-Ordner nach der ID der
  Seite suchen. Notizen verlinken Seiten in ihrer Quellenzeile; wird das
  vergessen, bleiben Zettel mit Adressen zurück, hinter denen nichts
  mehr steht. Genau so sind am 2026-08-09 fünfzehn tote Links aufgefallen.
  Seit dem 2026-08-26 fängt `pruefen.py`, Prüfung 8, denselben Fall auch
  nachträglich ab: Sie meldet jede Knowledge-ID, die hier nicht als
  lebende Seite geführt ist. Die Handregel bleibt trotzdem stehen — das
  Skript findet den Schaden erst, wenn er entstanden ist.
- Fußzeile jeder Seite nennt den Stand (Datum) und die führende .md-Datei.
  Der Stand-Stempel ist hier ausdrücklich erlaubt, weil ihn der
  Sonntagsabgleich kontrolliert (`DOC_RULES.md`, Abschnitt 7).
- **Zeigen statt vorstellen lassen** — die Regel steht in
  `WORKFLOW.md`. Für Seiten heißt das: Diagramme und Zahlen ja,
  „stell dir vor" nie.
