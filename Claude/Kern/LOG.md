# LOG.md — Chronik Harness

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste oben.
Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur ergänzt.
Sie kann daher nicht falsch werden und braucht kein Archiv.
Was als Nächstes kommt, steht in `ROADMAP.md`; warum es so entschieden
wurde, in den DECISIONS dieser Schicht.
Format: `- JJJJ-MM-TT — Ereignis (1–3 Sätze: was, und woran es geprüft wurde)`.
Ein Eintrag darf einen Ablageort nennen — er beschreibt den Stand von
damals, nicht den von heute.

- 2026-07-14 — Kern des Harness angelegt: `INDEX.md`, `ROADMAP.md` und
  eine minimale `CLAUDE.md`. Geprüft per Übergabetest — eine frische
  Session sollte allein aus den Dateien arbeitsfähig werden.
- 2026-07-17 — `WORKFLOW.md` gebaut: Grundregeln und alle vier
  Session-Typen (Brainstorm/Design, Development, Art, später Zeugnis).
- 2026-07-17 — Knowledge-System eingeführt: externer Ordner
  `C:\Repos Isor\Knowledge\` mit Themen-Unterordnern, dazu
  `KNOWLEDGE_RULES.md`. Extern, weil Wissen das Projekt überlebt.
- 2026-07-17 — `FEATURE_LOG.md` und `DECISIONS.md` angelegt — Gebautes
  und Begründungen bekommen getrennte Dateien.
- 2026-07-17 — `CODE_GUIDELINES.md` als Rohmaterial: Uni-Conventions und
  gefilterte Dozenten-Regeln in der Zwei-Block-Struktur.
- 2026-08-05 bis 2026-08-08 — Artifact-Seiten nach den drei Typen
  sortiert: zehn Seiten mit Symbol, Kind-Badge und Favicon; Regeln in
  `ARTIFACT_RULES.md`, Bestand in `ARTIFACT_INDEX.md`.
- 2026-08-08 — Diagramm-Werkzeug hält jetzt die gesamte Handarbeit über
  Neuerzeugungen hinweg: Kastenpositionen (über den Klassennamen statt der Id),
  Linien-Wegpunkte, Andockpunkte und die Lage der Multiplizitäts-Beschriftungen.
  Andockpunkte an Member-Zeilen werden auf den Kasten umgerechnet (pixelgleich).
  Neu `linienstaerke_setzen.py` für handgezeichnete Diagramme. Geprüft: zweiter
  Lauf erzeugt alle sieben Dateien byte-identisch.
- 2026-08-09 — Ablaufplan-Formen im Diagramm-Werkzeug (`uml_drawio.py`, +95
  Zeilen): sechs Sinnbilder nach DIN 66001 (`start`, `ende`, `prozess`,
  `entscheidung`, `unterprogramm`, `ein_aus`) über `knoten()`, Ablauflinien mit
  Zweigbeschriftung über `pfeil()`, `ablauf_lesen()` liest Lage **und** Größe
  zurück. Sinnbilder laufen über ihre Id statt über den Text — „Ende" kommt
  mehrfach vor. Klassendiagramme bleiben unberührt (nachgewiesen: kein
  Klassendiagramm hat einen Nicht-Swimlane-Kasten auf oberster Ebene, alle
  sieben Dateien nach dem Umbau byte-identisch).
- 2026-08-11 — Zwei Fehler im Diagramm-Werkzeug behoben, beide fielen erst an
  einem von Hand angeordneten Diagramm auf: (1) `knoten()` schrieb die Geometrie
  als Ganzzahl und verschob Kästen, die auf halben Pixeln sitzen — jetzt `%g`
  über `_zahl()`. (2) Ein bewusst frei gelassenes Linienende wurde von der
  Skript-Vorgabe überschrieben; Gegenmittel ist, die Vorgabe für diese Kante zu
  entfernen (jetzt Bedienregel 5 in DIAGRAM_RULES). Neu außerdem `SPRUNG =
  jumpStyle=arc` als zentrale Vorgabe: Bogensprung an jeder Kreuzung.
  Geprüft: 13 Kästen und 31 Kanten der Handanordnung unverändert, zweiter Lauf
  byte-identisch.
- 2026-08-11 — Session-Typ „Zeugnis" gebaut: vierter Typ in WORKFLOW.md,
  eigene Regeln in ASSESSMENT_RULES.md, Auslöser `/zeugnis`. Erstes
  Zeugnis am selben Tag geschrieben.
- 2026-08-22 — Harness auf die Schichten-Struktur umgebaut (Phasen 1–5 der
  Überholung). Neu: DOC_RULES, GDD_RULES, VERSIONIERUNG, PLAN, STOERUNGEN.
  Vier Schicht-Ordner angelegt, 17 Dateien einsortiert. Fünf Bestände
  aufgeteilt und jeder vor dem Archivieren geprüft: Zeugnisse (2 Dateien),
  FEATURE_LOG (3 Chroniken), ROADMAP (708 → 204 Zeilen Planung + 521
  Archiv), TDD_NOTES (10 Themenblöcke), DECISIONS (133 Einträge → 9
  Dateien). Vierzehn Regeldateien nachgezogen, alle toten Verweise
  repariert. Drei Skripte gebaut: INDEX und PREFAB_STATUS werden ab jetzt
  erzeugt, dazu die Sicherung auf die externe Platte.
  Leseordnung je Session-Start damit von 847 auf rund 250 Zeilen.
