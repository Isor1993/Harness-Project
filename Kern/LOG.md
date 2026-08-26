# LOG.md — Chronik Harness

Ownership: Nur was wann passiert ist — datierte Ereignisse, älteste oben.
Eine **Chronik**: Einträge werden nie geändert oder gekürzt, nur ergänzt.
Sie kann daher nicht falsch werden und braucht kein Archiv.
Was als Nächstes kommt, steht in `ROADMAP.md`; warum es so entschieden
wurde, in den DECISIONS dieser Schicht.
Format: `- JJJJ-MM-TT — Ereignis (1–3 Sätze: was, und woran es geprüft
wurde)`. Bei einem Umbau, der viele Dateien auf einmal betrifft, darf
ein Eintrag bis zu einem Absatz lang werden.
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
- 2026-08-22 — Phase 6 der Überholung: die Befehle gebaut. `/harness:sichern`,
  `:wechsel`, `:ende`, `:sonntag` und `:zeugnis` liegen als Auslöser in
  `.claude\commands\harness\`, ihr Ablauf in `Kern/WORKFLOW.md`; der
  Unterordner erzeugt den Namensraum, an dem die eigenen Befehle im
  `/`-Menü erkennbar sind. Der globale Skill `~\.claude\skills\zeugnis`
  ist damit archiviert. Berechtigungen von 314 Allow-Einträgen auf 51
  Muster plus 8 `ask` und 4 `deny`; die alte Fassung liegt im Archiv.
  Prüfung P1 gemessen: Von drei `CLAUDE.md` lädt nur die im Projektstamm
  von selbst, weshalb sie jetzt einen benannten Notkern trägt.
  Geprüft: `/harness:sichern` im selben Zug erstmals gelaufen — die
  Leseordnung führte ohne Zuruf zur Doku-Pflicht.
- 2026-08-22 — Phase 7 der Überholung: der Kern ist vollständig. Die Schicht
  `IsorBackup/` gebaut (RULES, ROADMAP, DECISIONS) und `C:\IsorBackup\README.md`
  von 93 auf 30 Zeilen als Wegweiser gekürzt; der Regeltext hat damit
  Versionsgeschichte. `Kern/GLOSSARY.md` mit 26 Begriffen eingesammelt, jeder
  mit Zeiger auf seinen Besitzer. Beim Aufteilen der acht „Offenen Punkte"
  gehörten drei in andere Schichten, einer war überholt, und einer war gar
  keine Aufgabe, sondern die Regel „beim draw.io-Export *Include a copy of my
  diagram* angehakt lassen" — sie steht jetzt in `Kern/DIAGRAM_RULES.md`.
  Geprüft: INDEX neu erzeugt, 46 Dateien, alle mit Ownership-Zeile.
- 2026-08-22 — Phase 8 der Überholung: die Abnahme. Schlussdurchgang über
  50 Dateien und rund 9.400 Zeilen in sechs Durchgängen, Ergebnis **33
  Befunde** in `_HARNESS_ABNAHME.md` (15 muss · 14 lohnt sich · 4 bei
  Bedarf). Nach Ursache sortiert liegt die größte Gruppe nicht bei den
  Regeln und nicht beim Altbestand, sondern mit 14 Befunden an den
  **Nahtstellen des Umbaus** vom 21./22.08. Drei Haken der Baulisten
  waren nicht gedeckt (Auslieferungs-Ordner, vier Aufgabentexte,
  ARTIFACT_INDEX-Eintrag). **30 der 33 Befunde im selben Zug behoben**;
  die drei übrigen hängen am Archivieren bzw. am ersten Pflegetag.
  Die Befehle haben ein Zuhause im Repo bekommen (`Kern/Befehle/`,
  Arbeitskopie in `.claude\`), das INDEX-Skript führt sie und die beiden
  Wegweiser-`CLAUDE.md` in eigenen Abschnitten. `CODE_GUIDELINES.md`
  beschrieb noch die Ordnerstruktur vor dem 2026-08-20 — neu geschrieben
  gegen den tatsächlichen Assets-Baum. Fünf Regeln geschärft, der Begriff
  „Befund" hat einen Besitzer.
  Geprüft mit zwei eigens gebauten Skripten: alle Datei-Verweise gegen
  den Bestand, Datumsreihenfolge und Pflichtfelder von drei Chroniken und
  zehn Entscheidungsdateien — am Ende null Beanstandungen. Sie fanden 6
  der 33 Befunde allein und stehen deshalb als Aufgabe in
  `Kern/ROADMAP.md`. Nebenbei einen aktiven Datenverlust abgewendet:
  `prefab_status.py` las 34 Prefabs als 33 Einträge, weil `Torch` und
  `Torch ` auf denselben Schlüssel fielen.
- 2026-08-23 — **Version 1.0.0 steht.** Der Tag begann mit einem
  Gegenlese-Durchgang aus eigener Session: Von den 30 als erledigt
  geführten Befunden der Abnahme waren **28 gedeckt, zwei nicht** — bei
  einem hing die Korrektur am falschen DECISIONS-Eintrag, beim anderen
  war nur die Regel geändert, nicht das, was sie vorschrieb. Dazu fünf
  neue Befunde (A34–A40), darunter der Auftrag an die nächste Session,
  der in keiner Leseordnung stand. Alle acht wurden im selben Zug
  entschieden und gebaut: **fünfter Session-Typ „Prüfung"**, die
  **Übergabe in `PLAN.md`** samt Schritt „Plan nachziehen" in `/ende`,
  die Chronik-Ausnahme zur Verweisregel und die Umzugsregeln als
  Abschnitt 11 der `DOC_RULES.md`. Vor dem Archivieren wurden sieben
  Regeln aus den Arbeitsdateien gerettet, die nur dort lebten — darunter
  der Prüfbogen und Isors fünf Grenzen für den Harness. Der erste
  Pflegetag lief (drei Artifact-Funde), die Seiten `⚙️ System · Harness`
  und `📍 Status` wurden gebaut bzw. neu gebaut, und die Artifact-Seiten
  haben eine verbindliche Farbwelt bekommen. Das Backup fällt auf Isors
  Wunsch aus dem Pflegetag heraus. Ausgeliefert nach
  `C:\IsorBackup\05_Werkzeuge\Harness_Auslieferungen\Harness_1.0.0\`,
  als **Vorlage statt Kopie** — 24 Dateien, 3.028 Zeilen.
  Geprüft: INDEX neu erzeugt (44 Dateien, alle mit Ownership-Zeile) ·
  das INDEX-Skript läuft in der Auslieferung eigenständig · nach dem
  Archivieren zeigt kein lebender Verweis mehr auf die drei
  Arbeitsdateien. Nicht geprüft: die rund zwanzig Dateien, die an diesem
  Tag geschrieben wurden — das gehört einer frischen Session.
- 2026-08-23 — **Prüfung der Version 1.0.0**, Gegenstand Harness, in
  frischer Session: die vier neuen Regeln, die geretteten Regeln gegen
  die drei archivierten Arbeitsdateien und ein Durchgang quer über den
  Bestand ergaben **vierzehn Befunde** in `_HARNESS_PRUEFUNG_1_0_0.md`
  (acht muss · vier lohnt sich · einer bei Bedarf · einer ein Beleg ohne
  Auftrag), behoben wurde nichts. Der Beleg ist die Übergabe selbst: Die Session fand
  ihren Auftrag allein über die Leseordnung, ohne Zuruf — der Fall aus
  Befund A34 tritt nicht mehr auf. Die dichteste Stelle war das
  `GLOSSARY.md` mit drei falschen Zeilen aus zwei Bautagen; es ist ein
  von Hand gepflegtes Verzeichnis und steht in keiner Doku-Pflicht.
- 2026-08-23 — **Die vierzehn Befunde behoben und `pruefen.py` gebaut.**
  Alle Befunde der Prüfung sind erledigt; beim Beheben kamen zwei
  weitere Anzahl-Verstöße ans Licht, aus sechs gemeldeten Stellen wurden
  acht behobene. Das neue Werkzeug `Kern/Werkzeuge/pruefen.py` prüft
  Verweise, Chronik-Format, Befehle gegen ihre Arbeitskopie, Zahlwörter
  und das Glossar; es läuft bei jedem `/harness:sichern` und beim
  Session-Start, **meldet nur und ändert nichts**. Der erste Lauf ergab
  **45 Funde, davon rund 40 Fehlalarme** — geplante Dateien, Verweise auf
  fremde Bäume, ein Gegenbeispiel im Regeltext, Zeitangaben statt
  Listenanzahlen. Nach zwei Runden Schärfung: 4 Funde, davon einer echt
  — das Glossar führte „V-Nummer", `VERSIONIERUNG.md` nannte dieselbe
  Sache „Commit-Nummer". Daraus die Bauregel für jeden weiteren Prüfer:
  Ein Fund, den niemand nachprüfen kann, ist Rauschen, und Rauschen macht
  den Prüfer wertlos.
  Dazu aus Isors Einwürfen: Der **Session-Titel trägt jetzt den laufenden
  Abschnitt** in der Klammer, samt der Ruhezustände `zu` und
  `aufgehoben`; `WORKFLOW.md` hat einen Abschnitt **Die Prüfebenen**
  bekommen, weil sieben Stellen ohne Übersicht nicht mehr zu behalten
  waren. Die **Bestandsaufnahme der acht Altbestand-Artifacts** aus einer
  Parallel-Session wurde aus deren Scratchpad ins Repo gerettet — 540
  Zeilen, die an einem Temp-Ordner hingen. Drei Störungen festgehalten,
  darunter zwei eigene Fehlurteile.
  Zum Schluss die Ordnerstruktur zum ersten Mal ganz durchgesehen:
  `Assets\` des Harness-Repos enthält **14 Dateien, alle aus der
  Unity-Vorlage**. Daraus der Bauplan `_HARNESS_UMBAU_STRUKTUR.md` —
  der Harness wird sein eigenes Repo, null Weiterleitungen, der Notkern
  entfällt. Alle betroffenen Zeiger sind darin gesucht und aufgelistet,
  zwei davon liegen in **anderen Repos**.
  Geprüft: `pruefen.py` über 47 Dateien, 0 Funde · INDEX neu erzeugt,
  alle mit Ownership-Zeile · die ROADMAP von 224 auf 132 Zeilen zurück
  auf ihr eigenes Format gebracht.
- 2026-08-23 — **Harness 2.0.0: der Harness ist sein eigenes Repo.**
  Baustein 1 des Bauplans ausgeführt. Wurzel ist jetzt
  `C:\Repos Isor\Harness Project\`; der Inhalt von `Claude\` ist eine
  Ebene hochgezogen, `.git` mit ihm. Der Unity-Anteil ist archiviert —
  `Assets\`, `Library\`, `Logs\`, `Packages\`, `ProjectSettings\`,
  `UserSettings\`, die beiden `.csproj`, `.slnx`, `.vsconfig` und
  `.gitattributes`, dazu die beiden Weiterleitungs-`CLAUDE.md`. Getrackt
  waren vorher 123 Dateien, davon 57 Harness und 66 Ballast; jetzt sind
  es 58. Von der Platte gingen 1.843 MB `Library\`. Nichts gelöscht:
  alles liegt in
  `C:\IsorBackup\99_Archiv\_Zu_Loeschen\2026-08-23_Harness_Umbau_Struktur\`.
  Weggefallen sind der Notkern, die INDEX-Kategorie Wegweiser und zwei
  der drei `CLAUDE.md`. Nachgezogen wurden die zehn Befehlsdateien
  (Original und Arbeitskopie), beide Werkzeuge, `WORKFLOW.md` an zwei
  Stellen, `GLOSSARY.md` und die zwei READMEs in den **anderen beiden
  Repos**. Beim Ausführen kamen vier Dinge dazu, die der Bauplan nicht
  vorhergesehen hatte: `.claude\` lag schon auf der Zielebene, der
  Memory-Umzug entfiel ganz (der geöffnete Ordner blieb derselbe), die
  mitgetrackte PDF war ein bitgleiches Duplikat einer Datei im
  Datenbaum, und beide Skripte hätten `.claude\` und `.git\` künftig
  mitdurchsucht.
  Geprüft nach `DOC_RULES.md` 11.3 — 52 `.md`-Dateien und 8.634
  nicht-leere Zeilen vorher wie nachher · `pruefen.py` danach 0 Funde in
  allen fünf Prüfungen · INDEX neu erzeugt, 47 Dateien, alle mit
  Ownership-Zeile · die zehn Befehlsdateien von Hand gegengelesen, weil
  ihre absoluten Pfade außerhalb des Baums liegen und Prüfung 1 sie
  nicht sieht.
- 2026-08-23 — **Baustein 2: der erste Hook. Erzwingen statt erinnern.**
  `.claude\settings.json` trägt jetzt einen `SessionStart`-Hook, der
  `Kern/Werkzeuge/pruefen.py` beim Session-Start ausführt — Auslöser
  `startup|resume|clear|compact`. Damit hängt die erste der drei
  Skript-Prüfebenen nicht mehr an Claudes Erinnerung. Vor dem Bauen
  wurden die vier offenen Fragen des Bauplans gegen die Hook-Referenz
  geklärt: `SessionStart` kann eine Session **nicht** blockieren (Exit-Code
  und Fehler werden dort ignoriert), einfacher stdout wird **von selbst**
  als Kontext eingelesen, ein Fehlschlag kostet nur eine Meldung, und die
  Auslieferung erfasste den Hook bisher gar nicht.
  Daraus vier Dinge gebaut: die Vorlage `Kern/Vorlagen/settings.json` samt
  `README.md` und viertem Einrichtungs-Handgriff in `VERSIONIERUNG.md` ·
  **Prüfung 6** in `pruefen.py`, die Vorlage gegen Arbeitskopie hält ·
  der Schalter `--hook`, der die Herkunft der Ausgabe kennzeichnet ·
  `Kern/Bilder/` als Ort für Erklärskizzen, mit der ersten darin.
  Nachgezogen: `CLAUDE.md` Punkt 5 (melden statt ausführen, mit
  Rückfallebene), `WORKFLOW.md` an zwei Stellen, `GLOSSARY.md` um **Hook**
  und **Vorlage**.
  Zwei eigene Fehler beim Bauen gefunden und behoben: Die erste Fassung
  benutzte `$CLAUDE_PROJECT_DIR` in der Kommandozeile, was Git Bash
  voraussetzt — ohne Git Bash weicht Claude Code auf PowerShell aus, und
  der Hook wäre stumm kaputt gewesen; jetzt steht `${CLAUDE_PROJECT_DIR}`
  in der `args`-Form, die Claude Code selbst ersetzt. Und die Marker-Zeile
  sagte pauschal „ein zweiter Lauf ist unnötig", was die Läufe bei
  `/harness:sichern` stillgelegt hätte (Isors Einwand).
  Geprüft: `pruefen.py` 0 Funde in allen sechs Prüfungen · Prüfung 6 gegen
  vier nachgestellte Schäden gehalten und jedes Mal angeschlagen (Vorlage
  fehlt, `hooks`-Block entfernt, Matcher gekürzt, `settings.json` kein
  gültiges JSON) · INDEX neu erzeugt, 49 Dateien, alle mit
  Ownership-Zeile · die Kommandozeile in Git Bash gelaufen, Exit 0.
  **Nicht geprüft: ob der Hook wirklich feuert.** Das zeigt erst der
  nächste Session-Start; Erkennungszeichen ist die Zeile
  `[SessionStart-Hook]` **ohne** sichtbaren Werkzeugaufruf.
  Ins Knowledge gingen zwei Seiten: die Hook-Mechanik samt Matcher-Falle
  und Shell-Falle (`Werkzeuge/`) und das Prinzip dahinter,
  „Stille ist mehrdeutig" (`Patterns/`) — eigenes Repo, eigener Commit.
- 2026-08-23 — **Der Hook feuert. Artifact-Seite auf 2.0.0 nachgezogen.**
  Der scharfe Test von Baustein 2 ist bestanden: Beim ersten Session-Start
  nach dem Bau stand die Zeile `[SessionStart-Hook]` ohne sichtbaren
  Werkzeugaufruf im Kontext, Ergebnis 0 Funde bei 48 Dateien. Damit ist
  zugleich belegt, dass Claude Code `${CLAUDE_PROJECT_DIR}` ersetzt und
  `python` im Hook-Prozess erreichbar ist. `_HARNESS_UMBAU_STRUKTUR.md`
  ist daraufhin geschlossen — Kandidat 2 ausdrücklich als *nicht gebaut*
  markiert — und nach
  `C:\IsorBackup\99_Archiv\_Zu_Loeschen\2026-08-23_Harness_Umbau_Arbeitsdateien\`
  archiviert.
  Danach die Seite `⚙️ System · Harness` auf **2.0.0** nachgezogen, gleiche
  URL. Alle Zahlen neu gemessen statt fortgeschrieben: Leseordnung 740
  Zeilen (vorher 574), Bestand rund 10.100, Kopfzeile 48 Dokumente und
  4 Werkzeuge. Neu sind Punkt 5 der Leseordnung, der Hook als oberstes
  Glied im Session-Kreislauf, die Prüfebenen als Tabelle und **Tafel 5**
  nach `Kern/Bilder/hook_sessionstart.svg`. Zwei inhaltliche Fehler der
  alten Fassung gingen mit weg — sie kündigte die Testphase als
  automatische Folge an, und ihre Nummern-Tabelle zeigte ein
  Commit-Format, das es nie gab (`Update V 0126` statt `Update V 0.0049`).
  Zwei Befunde nebenbei, beide nicht behoben: `pruefen.py` Prüfung 1 sieht
  die temporären `_HARNESS_*.md` nicht und meldete deshalb null, als drei
  Verweise durch das Archivieren ins Leere zeigten — steht als Aufgabe in
  der `ROADMAP.md`, samt Isors Einwand, dass ein bloßes Erweitern der
  Liste die absichtlichen Archiv-Verweise mitmelden würde. Dazu eine
  Störung: Typ und Modus wurden zu Abschnittsbeginn nicht gefragt,
  sondern aus `PLAN.md` übernommen (zweiter Vorfall dieser Sorte).
  Geprüft: `pruefen.py` 0 Funde in allen sechs Prüfungen · INDEX neu
  erzeugt, 48 Dateien, alle mit Ownership-Zeile · Glossar-Hinweis zu
  „Störung" und „Vorlage" gegengelesen, beide Definitionen unverändert.
  Nicht geprüft: die veröffentlichte Seite im Browser — Artifact-URLs
  sind ohne Login nicht abrufbar, die Sichtprüfung bleibt bei Isor.
- 2026-08-24 — **Pfad-System gebaut, Auslieferung `Harness_2.0.0` abgelegt.**
  Aus Isors Vorschlag, das Einrichten abzufragen statt zu dokumentieren,
  wurden drei Bausteine: `Kern/PFADE.md` besitzt als einzige Datei die
  absoluten Pfade (Marken `DATENBAUM`, `KNOWLEDGE`, `PROJEKT`) und die
  betroffenen Stellen in Kern, Uni, IsorBackup und Projekt nennen jetzt
  die Marke — die zehn Befehlsdateien sind zugleich auf relative Pfade
  umgestellt, per Skript, UTF-8 ohne BOM, erste Bytes geprüft. Dazu
  **Prüfung 7** in `pruefen.py` (absoluter Pfad außerhalb `PFADE.md` und
  der Chroniken; ihr erster Lauf fand 13 Stellen, danach 0) und der
  Befehl **`/harness:einrichten`** samt Ablauf in `WORKFLOW.md`, der die
  Handgriff-Liste aus `VERSIONIERUNG.md` ersetzt. Dort steht neu auch
  die **Packliste** — vollständig · geleert · fällt weg — je Datei.
  Beim Glossar-Gegenlesen einen Altfehler gefunden: „Harness-Version"
  stand als Reifegrad, `VERSIONIERUNG.md` sagt Verträglichkeit;
  nachgezogen, dazu die neuen Begriffe Marke und Datenbaum (28 Kurzformen).
  Die Auslieferung wurde nach der Packliste im Scratchpad gepackt, im
  Probelauf eingerichtet (Schritte 4 bis 8 des neuen Ablaufs; sechs
  erwartete Schicht-Verweise, sonst 0 Funde) und nach
  `05_Werkzeuge\Harness_Auslieferungen\Harness_2.0.0\` im Datenbaum
  abgelegt — 31 Dateien, 269.233 Bytes, Quelle wie Ziel.
  Geprüft: `pruefen.py` im Repo 0 Funde in allen sieben Prüfungen ·
  INDEX neu erzeugt, 49 Dateien, 6 Befehle · Prüfung 3 bestätigt
  Original gleich Arbeitskopie nach der Pfad-Umstellung.
- 2026-08-24 — **Der Artifact-Altbestand ist nachgezogen — alle acht
  Seiten an einem Tag, der Bestand wuchs dabei auf neun.** Reihenfolge
  wie geplant, billigste zuerst: Terrain-Fallen (Palettentausch, der
  Testlauf der Hausfarbwelt am Altbestand), Multithreading (fünfte Falle
  aus TerrainConfig.cs/ObjectPlacer.cs verifiziert, Anzahl aus der
  Fallen-Überschrift entfernt), Input-Reader (canceled-Aussage
  umgedreht und mit dem echten EnableUI belegt, gehaltene Taste neu,
  normalized-Beispiel in PlayerMotor.cs:86 belegt), Schaf (vierte Frage
  samt Nacht-Zeile, FSM-Lesestellen vier statt sechs, Commander als
  Herdenanker), Poisson (Radius-Wechsel angesagt, Projekt-Kasten belegt
  die Beispiel-Zeile; drei SVGs statt der geschätzten sechs), dann das
  Paar GPU + Terrain & Gras (Zellgrößen-Widerspruch über den
  Engpass-Wechsel aufgelöst, 211.000/190.000 als verschiedene
  Messstände ausgewiesen, EnsureHeightCurveLookup statt OnEnable,
  GrassInteraction/GrassLodLevel ergänzt, Ladebalken als gebaut).
  Zuletzt der **Neubau des Grundgerüsts als zwei Seiten**: „Grundgerüst"
  (Szenenfluss, Pause als Input-Zustand, Spieler, Interaktions-Vertrag)
  und die **neue Seite „Welt & Überleben"** (Uhr→Relay→Listener, elf
  FSM-Zustände — der Code schlägt die geschätzten dreizehn —, Herde,
  Schadens-Verträge; Goblin und Player.cs ehrlich als Platzhalter bzw.
  leere Hülle ausgewiesen). Grundlage je Seite: Abruf der
  veröffentlichten Fassung plus Lesen des echten Codes, darunter alle
  89 Skript-Köpfe des Tower-Repos.
  Geprüft: pruefen.py nach jeder Seite und am Ende 0 Funde in allen
  sieben Prüfungen · INDEX neu erzeugt, 48 Dateien · beide neuen
  Index-Einträge tragen erstmals gefüllte „Seite →"-Zeilen.
  Die Befundliste `_HARNESS_ARTIFACTS_1_0_0.md` wurde mit
  Abschlussvermerk geschlossen und nach
  `99_Archiv\_Zu_Loeschen\2026-08-24_Artifact_Altbestand_Befundliste\`
  archiviert. **Nicht geprüft: die Sichtkontrolle der neun Seiten im
  Browser** — Artifact-URLs sind ohne Login nicht abrufbar, sie bleibt
  bei Isor.
- 2026-08-25 — Sichtprüfung der neun Artifact-Seiten durch Isor: alle am
  23./24.08. neu veröffentlichten Seiten im Browser angesehen, keine
  Beanstandungen („sehen gut aus und passen so erstmal"). Damit ist der
  offene Punkt aus der Übergabe vom 2026-08-24 erledigt; der Stand je
  Seite steht im `ARTIFACT_INDEX.md`.
- 2026-08-25 — GitHub-Repo umbenannt: `Isor1993/My-Harness-Development`
  → `Isor1993/Harness-Project` (Isor über die GitHub-Settings), die
  lokale Remote-URL im selben Zug nachgezogen. Geprüft per
  `git ls-remote` gegen die neue Adresse — sie liefert den letzten
  lokalen Commit `b49e5aa` (Update V 0.0050).
- 2026-08-25 — Prüfung 1 sieht jetzt die temporären Wurzeldateien:
  `_HARNESS_`-Verweise werden nachgeschlagen; eine verschwundene
  Befundliste ohne den Zusatz „(im Archiv)" auf der Zeile oder der
  folgenden ist ein Fund, die Befundlisten selbst werden wie Chroniken
  übersprungen. Der erste scharfe Lauf fand sechs Stellen — fünf ohne
  Kennzeichen (nachgezogen in `Kern/ROADMAP.md` und
  `Kern/DOC_RULES.md`), eine mit dem Zusatz auf der Folgezeile, daraus
  das Zwei-Zeilen-Fenster. Geprüft mit fünf nachgestellten Fällen in
  einer Wegwerfdatei (die zwei erwarteten Funde kamen, die drei Stillen
  blieben still), danach Gesamtlauf 0 Funde; Regel in `DOC_RULES.md`
  Abschnitt 6, Begründung in `DECISIONS.md`.
- 2026-08-25 — E46 geschlossen: Die tote ID `0dd96ec7-…` bekommt keinen
  Nachfolger — Knowledge-Ordner und Harness durchsucht, nichts zeigt
  auf sie; Vermerk in der Gelöscht-Tabelle des `ARTIFACT_INDEX.md`. Die
  „Seite →"-Restzeilen laufen über die Index-Markierung „(noch nicht
  erfasst)" statt über einen ROADMAP-Punkt.
- 2026-08-25 — E61b gebaut: `Kern/Werkzeuge/abgabe_bauen.py` erzeugt
  eine Abgabe-`.docx` per Vollgenerierung aus Markdown (pandoc 3.10.2);
  dazu die Formatvorlage mit nachgerüstetem Seitenumbruch je
  Hauptkapitel und die Erst-Extraktion nach
  `Projekte/Isor_Tower/TDD.md` (185.694 Zeichen) samt 44 Bildern nach
  `TDD_Media` im Datenbaum. Geprüft: Dreifach-Test des Werkzeugs
  (Normal-, Sicherungs-, Sperrfall) und die Kette Ende-zu-Ende mit
  1240 Absätzen gleich der Quelle. Führend bleibt die `.docx`, bis
  Isors Sichttest die Kette abnimmt.
- 2026-08-25 — E61b umgebaut und abgenommen: Der erste Sichttest fiel
  durch (Titelseite zerlegt, Verzeichnisse als Text dupliziert und als
  Kapitel mitgezählt, Tabellen ohne Rahmen). Umbau: Titelteil als fixe
  Datei mit den Verzeichnis-Feldern, Manuskript ab Kapitel 1,
  Tabellen-Style in der Formatvorlage, Beschriftungen als SEQ-Felder
  samt Sprungmarken, Querverweise als REF-Felder, Seitenzählung
  durchgehend arabisch. Geprüft je Runde am gerenderten
  Seitenvergleich Original gegen Neubau, zuletzt 194 interne Sprünge
  maschinell (kein toter); zweiter Sichttest bestanden (Isor).
  Markdown führt seit heute (`Uni/DOCX_RULES.md`).
- 2026-08-26 — **Repo/Git-System geordnet** (Design und Development in
  einer Session). Alle drei Repos vermessen: Harness (3,2 MB) und
  Knowledge (0,2 MB) gesund; im Unity-Repo 119 MB Pack, davon 92 % aus
  75 Szenen-Ständen (1.269 MB roh, `Village.unity` 73 MB je Stand),
  während Texturen, Audio und Modelle seit dem ersten Commit über LFS
  laufen (86 Dateien, 127 MB). Entschieden und geregelt: Szenen und
  NavMesh künftig über LFS (`.gitattributes` des Projekts erweitert),
  die Historien-Migration als ROADMAP-Punkt fürs Wochenende, die
  Repo-Grenze zur Asset-Library und die Sichtbarkeitsregel in
  `CODE_GUIDELINES.md` → „Repo & Git", Build-Ablage und V-Nummer-Lesart
  in `VERSIONIERUNG.md`; vier Einträge in `DECISIONS.md`. Nebenbefunde
  im selben Zug behoben: das GitHub-Token im Klartext aus der
  Remote-URL des Unity-Repos entfernt (Isor hat es widerrufen),
  `Isor-Tower-ProtoTyp-2026` privat gestellt (per API-Abruf geprüft:
  404 ohne Anmeldung, der Harness wie gewollt 200), die toten
  `ThirdAssets`-Zeilen aus der Unity-`.gitignore`, die
  Unity-Vorlagen-`.gitignore` im Knowledge-Repo durch eine schlanke
  ersetzt. Zwei Wissensseiten nach `Werkzeuge/` im Knowledge-Repo.
  Geprüft: `pruefen.py` nach jedem Schreiben, zuletzt 0 Funde in allen
  sieben Prüfungen; INDEX neu erzeugt, 54 Dateien mit Ownership-Zeile.
  Ein eigener Fehler noch in der Session gefunden und behoben: Alle
  neuen Einträge trugen zunächst das Datum der PLAN-Übergabe (25.)
  statt des Kalendertags (26.) — vor dem Commit an sämtlichen Stellen
  korrigiert.
- 2026-08-26 — **LFS-Migration des Unity-Repos durchgeführt**, am selben
  Tag statt am Wochenende. Ergebnis: **Git-Pack 117 MB → 2,2 MB**,
  Rohbytes der Historie 1.372 MB → 32,6 MB, alle 52 Commits
  umgeschrieben; Isor hat committet und force-gepusht, lokal und GitHub
  sind identisch (`56f6d8c`). Vorher gesichert als verifiziertes
  `git bundle` (118,7 MB) im Datenbaum. Drei Dinge fielen beim Prüfen
  auf und wurden behoben, bevor gepusht wurde: **36 Dateien lagen nur
  als 130-Byte-Zeiger im Arbeitsverzeichnis** statt als Inhalt (darunter
  `MainMenu.unity`) — `git lfs checkout` holte alle 122 zurück; das
  Muster `NavMesh*.asset` traf auch die 1-KB-Einstellungsdatei
  `ProjectSettings/NavMeshAreas.asset` und heißt jetzt `NavMesh-*`; das
  Migrationswerkzeug hatte zwei Regelzeilen doppelt angehängt und alle
  Leerzeilen der `.gitattributes` entfernt. Beim ersten Unity-Start
  danach hing der Editor rund zwölf Minuten — Ursache war **keine Folge
  der Migration**, sondern eine verwaiste `bee_backend`-Sperre in
  `Library/` aus einer früheren Sitzung (belegt: nur eine Unity-Instanz,
  14,8 s Rechenzeit in acht Minuten, der erwartete Partnerprozess
  existierte nicht mehr, nur 35 Dateien unter `Assets/` überhaupt
  angefasst). Ein Neustart des Editors löste es.
- 2026-08-26 — **Die offenen Punkte der Harness-ROADMAP abgearbeitet**,
  in einem Design- und einem Development-Abschnitt. Entschieden: Eine
  Artifact-Seite über ein noch ungebautes System wird kein vierter Typ,
  sondern bleibt ⚙️ System im **Zustand** `(geplant)` — Regeln an vier
  Stellen in `ARTIFACT_RULES.md`, neue Glossarzeile „Zustand einer
  Seite", abgegrenzt gegen den Zustandsbegriff beim Befund. Archiviert:
  „Knowledge-Archivierung automatisieren" — per `git log -S` kam heraus,
  dass der Punkt vom 2026-07-14 stammt und das Auslagern aus einer
  Pufferdatei meinte, die am 2026-07-17 verworfen wurde; er stand also
  sechs Wochen ohne Gegenstand und überlebte dabei beide Umbauten und
  die Prüfung mit vierzehn Befunden. Gebaut an seiner Stelle:
  **Prüfung 8** in `pruefen.py` — Artifact-IDs im Knowledge-Ordner gegen
  den `ARTIFACT_INDEX.md`, mit getrennter Meldung für gelöschte und für
  ungeführte Seiten; der Ordner kommt über die Marke `KNOWLEDGE`, fehlt
  sie, schweigt die Prüfung. Geprüft: 0 Funde in allen acht Prüfungen,
  INDEX unverändert (mit `--write` gegengeprüft). Der Bestand des
  Knowledge wurde vor dem Streichen gemessen — 89 Dateien, sieben von
  sieben Themenordnern mit README, keine ohne `Quelle:`-Zeile, vier
  Artifact-IDs und alle gültig; **dass Prüfung 8 überhaupt anschlägt,
  ist deshalb nicht gegen diese Null belegt**, sondern gegen einen
  Wegwerf-Baum mit vier Testfällen im Scratchpad (gültig, gelöscht,
  ungeführt, ohne ID) plus dem Fall „Marke nicht eingerichtet". Zwei
  weitere Punkte geschärft: „ClaudeSetup" hing an der unprüfbaren
  Bedingung „wenn er sicher programmiert" und hängt jetzt an Isors
  Zuruf; der Punkt zum Development-Modus behauptete, der Modus sei
  ungebaut, und heißt jetzt „Review-Seite". Als Störung eingetragen:
  „Später, nur bei Bedarf" ist ein blinder Fleck, den keine Prüfebene
  abdeckt.
- 2026-08-26 — **Nachschlag auf Isors Frage „ist damit alles fertig?"**,
  und die Antwort war nein. Drei Reste, alle vom selben Typ: etwas ist
  erledigt oder hinfällig, aber niemand räumt es weg. **(a)** Die
  Befundliste `_HARNESS_PRUEFUNG_1_0_0.md` lag seit dem 2026-08-23
  archivierbar in der Wurzel — jetzt im Datenbaum unter
  `99_Archiv\_Zu_Loeschen\2026-08-26_Pruefung_1_0_0\` (`Kern/PFADE.md` →
  `DATENBAUM`), Archiv-Eintrag im `_ARCHIV.md`, INDEX von 56 auf 55.
  Der Durchgang vor dem Archivieren (`DOC_RULES.md`, Abschnitt 11) fand
  **einen** Posten, der nur dort lebte: Die Prüfung vom 2026-08-23 hatte
  `CODE_GUIDELINES.md` und die Uni-Schicht ausdrücklich ausgelassen, und
  das stand in keiner ROADMAP — steht jetzt als eigener Punkt.
  **(b)** In `STOERUNGEN.md` lagen drei benannte Gegenmittel, von denen
  keines je eine Aufgabe geworden war; die Doku-Pflicht fragt jetzt beim
  Eintragen danach, und alle drei wurden nachgezogen — Beleg beim
  Abhaken (`DOC_RULES.md`, Abschnitt 7), Datei vor dem Ersetzen erneut
  lesen (`WORKFLOW.md`, Parallele Sessions), eine Frage mehr im
  Prüfbogen für Listendateien. **(c)** Claude hatte zu Beginn dieser
  Session das Session-Thema überschrieben statt nur die Klammer zu
  setzen — als Störung eingetragen, und der ungeregelte Fall „geerbter
  Titel mit Klammer `zu`" ist jetzt in `WORKFLOW.md` beantwortet:
  vorschlagen, nicht setzen. Geprüft: 0 Funde in allen acht Prüfungen,
  INDEX gegengeprüft.
- 2026-08-26 — **`Kern/CODE_GUIDELINES.md` geprüft**, 348 Zeilen, erster
  Prüfbogen für diese Datei überhaupt: **neun Befunde**, fünf davon
  `muss`, festgehalten in `_HARNESS_CODE_GUIDELINES.md`. Geprüft wurde
  gegen den Prüfbogen aus `WORKFLOW.md`, gegen die echte
  `.gitattributes` des Unity-Repos, gegen `git log` und gegen die
  Datumsverweise in `DECISIONS.md`. Härtester Fund: Die Sprachregel
  steht an drei Stellen und sagt zweierlei — `DOC_RULES.md` Abschnitt 9
  erklärt sich zum Besitzer und verbietet die Kopie namentlich, während
  CODE_GUIDELINES sie zweimal ausschreibt und dabei verschärft; formal
  gilt damit die weiche Fassung, die niemand befolgt, und sie wandert in
  jede Auslieferung mit. Fünf der neun Befunde sind **Verfall statt
  Schreibfehler** — die Datei war jeweils richtig und wurde von der
  Wirklichkeit überholt; keine der acht Skript-Prüfungen kann das sehen.
  Die Uni-Schicht, die zweite Hälfte des Punktes, bleibt offen (fremdes
  Revier).
- 2026-08-26 — **Uni-Schicht geprüft**, zwölf Dateien, 1.663 Zeilen:
  **sechs Befunde** in `_HARNESS_UNI_SCHICHT.md`, zwei davon `muss`.
  Damit ist der ROADMAP-Punkt „Die nie geprüfte Fläche nachholen" ganz
  erledigt. Beide `muss`-Befunde sitzen in `Uni/DOCX_RULES.md` und
  stammen aus derselben Umstellung: Seit dem 2026-08-25 führt das
  Markdown und baut Pandoc — die Datei hat das im Fließtext nachgezogen,
  aber nicht in ihrer Ownership-Zeile (sie schickt den TDD-Inhalt noch
  an ROADMAP und LOG statt an `Projekte/Isor_Tower/TDD.md`) und nicht in
  ihrer Prüfliste (Schritt 1 verlangt einen `validate.py`-Lauf, der bei
  Pandoc-Dateien planmäßig rot ist, 88 Fehlalarme — dokumentiert in
  derselben Datei, zwei Abschnitte weiter oben). Die Schicht ist im
  übrigen gesund: Chroniken, Archiv und die sieben ASSIGNMENT-Texte sind
  sauber eingeordnet, und zwei Stellen sind ausdrücklich vorbildlich —
  die Word-Fallen liegen im Knowledge samt Begründung, und die Grenze
  zur Abgabe-Packliste ist in einem Halbsatz geregelt. **Nicht
  geschrieben, sondern gemeldet:** der Behebungspunkt in
  `Uni/ROADMAP.md` und der Satz in `Uni/LOG.md` — fremdes Revier, die
  Texte liegen fertig am Ende der Befundliste.
