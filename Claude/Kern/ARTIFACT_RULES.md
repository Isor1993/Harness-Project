# ARTIFACT_RULES.md — Regeln für die Artifact-Seiten

Ownership: Typen, Benennung, Aufbau, Symbole und Pflege der
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

Titel-Schema: `<Symbol> <Typ> · <Thema>`

    📍 Status · Wo das Projekt steht
    ⚙️ System · Terrain & Gras
    💡 Lernstück · Poisson-Disc-Sampling
    🗑 Löschen · Village spielbar

Symbol **und** Wort: Das Symbol allein ist in der Galerie zu klein zum
Scannen, das Wort allein sagt es erst beim Lesen.

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

Beide Farbwelten bedienen (hell und dunkel), breite Tabellen und
Diagramme in einen eigenen Scroll-Bereich — sonst schiebt sich die ganze
Seite auf dem Handy seitwärts.

## Wann geschaut wird

- **Bevor man sich auf eine Seite stützt:** die echte Seite aufrufen, nie
  aus der Erinnerung oder aus einer älteren Fassung zitieren. Seiten
  altern zwischen zwei Sessions.
- **Vor dem Coden:** Der Artifact-Check ist Punkt 5 des Review-Gate in
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
- **Inhalt aus einer alten Seite übernehmen:** gegen den Code prüfen,
  nicht abschreiben. Was auf einer Seite steht, war zum Stand-Datum wahr.

## Symbole an zwei Stellen

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
- Jede Änderung am Bestand — neue Seite, Teilung, Umbenennung, Löschung —
  wird im ARTIFACT_INDEX.md nachgetragen. Gelöschte Seiten kommen dort in
  die Tabelle „Gelöschte Seiten", damit eine tote ID erklärbar bleibt.
- **Vor dem Löschen oder Teilen** im Knowledge-Ordner nach der ID der
  Seite suchen. Notizen verlinken Seiten in ihrer Quellenzeile; wird das
  vergessen, bleiben Zettel mit Adressen zurück, hinter denen nichts
  mehr steht. Genau so sind am 2026-08-09 fünfzehn tote Links aufgefallen.
- Fußzeile jeder Seite nennt den Stand (Datum) und die führende .md-Datei.
  Der Stand-Stempel ist hier ausdrücklich erlaubt, weil ihn der
  Sonntagsabgleich kontrolliert (`DOC_RULES.md`, Abschnitt 7).
- **Zeigen statt vorstellen lassen** — die Regel steht in
  `WORKFLOW.md`. Für Seiten heißt das: Diagramme und Zahlen ja,
  „stell dir vor" nie.
