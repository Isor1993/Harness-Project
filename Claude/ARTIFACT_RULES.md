# ARTIFACT_RULES.md — Regeln für die Artifact-Seiten

Ownership: Typen, Benennung, Symbole und Pflege der Artifact-Seiten auf
claude.ai. Warum eigene Datei: Artifacts sind eine Ausgabeform wie das
Knowledge-Archiv, keine Harness-Dokumente — dieselbe Trennung wie bei
KNOWLEDGE_RULES.md.

Zweck der Artifacts: die Handy-Fassung. Führende Quelle bleibt immer die
.md-Datei im Repo; das Artifact ist die lesbare Ansicht davon, unterwegs
und ohne Editor.

## Die drei Typen

| Typ | Beantwortet | Symbol | Führende Quelle |
|---|---|---|---|
| Status | Wo steht das Projekt, was kommt als Nächstes? | 📍 | ROADMAP.md |
| System | Wie funktioniert *mein* System X in diesem Projekt? | ⚙️ | FEATURE_LOG.md, DECISIONS.md |
| Lernstück | Wie funktioniert Konzept Y — auch außerhalb dieses Projekts? | 💡 | TDD_NOTES.md, Knowledge-Ordner |
| (veraltet) | — | 🗑 | — |

**Trennlinie System ↔ Lernstück:** System ist projektspezifisch („so ist
mein Placement aufgebaut"), Lernstück ist übertragbar („so funktioniert
Poisson-Disc-Sampling"). Ein Artifact beantwortet genau eine der Fragen —
beantwortet es zwei, wird es geteilt.

**Beim Teilen behält das Lernstück die URL.** Das Übertragbare veraltet
nicht, die Projektbeschreibung schon; der gemerkte Link soll am
Stabileren hängen.

## Benennung

Titel-Schema: `<Symbol> <Typ> · <Thema>`

    📍 Status · Wo das Projekt steht
    ⚙️ System · Terrain & Gras
    💡 Lernstück · Poisson-Disc-Sampling
    🗑 Löschen · Village spielbar

Symbol **und** Wort: Das Symbol allein ist in der Galerie zu klein zum
Scannen, das Wort allein sagt es erst beim Lesen.

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
- Fußzeile jeder Seite nennt den Stand (Datum) und die führende .md-Datei.
- Aphantasie berücksichtigen: erklären über Zahlen und Tabellen, nicht über
  „stell dir vor". Diagramme sind erwünscht — sie sind extern, nicht
  vorgestellt.
