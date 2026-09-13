# LERNLOG.md — Isors Lernverlauf

Ownership: Nur das Lern-Log — die laufende Aufzeichnung, was Isor selbst geschafft hat,
wo Gerüste oder Hilfe nötig waren und welche Fehlerbilder auftraten —
das Rohmaterial, aus dem die Zeugnisse lesen (`ASSESSMENT_RULES.md`).
Keine Bewertung und keine Muster-Deutung: Die passiert im Zeugnis, nicht
hier. Kein Projektfortschritt: Das ist das LOG der Schicht.
Format: `- JJJJ-MM-TT · <Kontext> — ` dann bis zu drei benannte
Halbsätze: **Selbst:** … · **Hilfe:** … · **Fehlerbild:** … — nur
belegte Felder, eine bis drei Zeilen. **Älteste oben**, wie in einer
Chronik.

**Wer schreibt:** Claude, laufend während der Arbeit — sobald etwas
selbst gelang, ein Gerüst oder eine Erklärung nötig war oder ein
Fehlerbild auftrat. Die Doku-Pflicht (`WORKFLOW.md`) fragt bei jedem
Sichern nach, ob die Zeilen des Abschnitts geschrieben sind — das Netz
gegen das Einschlafen, nicht der Auslöser.

**Reist nicht mit:** Diese Datei beschreibt eine Person, nicht den
Harness. Die Packliste (`VERSIONIERUNG.md`) und `ausliefern.py` lassen
sie bei jeder Auslieferung weg — wie `Kern/Zeugnisse/`.

---

*Erstbefüllung rückwirkend am 2026-09-04, aus Session-Verlauf, LOG und
Knowledge-Notizen — lückenhaft, weil vor diesem Datum nur festgehalten
wurde, was die Chroniken ohnehin trugen. Ab hier wird laufend geführt.*

- 2026-08-28 · Baustein A, Dienst und Menüwege — **Selbst:**
  `ISessionService` und `RelaySessionService` kleinschrittig selbst
  getippt (Entwurf vor Gerüst). **Fehlerbild:** vier Verdrahtungsfehler
  in der Szene, gefunden per Skript-Audit, nicht beim Bauen. *(aus
  `Projekte/Isor_Tower/LOG.md`)*
- 2026-08-30 · Rückweg-Feld des Menüs — **Fehlerbild:** Zuweisung
  dreimal seitenverkehrt (`_menuPanel = _lobbyBackTarget`) — der
  Inspector-Verweis wäre mit null überschrieben worden; im Review vor dem
  ersten Test gefunden. **Hilfe:** Merksatz „links steht der Empfänger".
  *(aus `Knowledge/CSharp/zuweisung-links-empfaengt.md`)*
- 2026-09-01 · `HostOptionsPanel` getippt — **Selbst:** die ganze Klasse
  nach Gerüst selbst geschrieben; `ChangePlayerLimit` (Clamp plus
  Anzeige) auf Anhieb richtig; Konstanten-Konvention richtig angewandt.
  **Fehlerbild:** vier Review-Runden — Dateiname ≠ Klassenname;
  `GetString` ohne Zuweisung (Rückgabewert verfiel); `SetString` mit der
  Konstante statt des Feldinhalts — dieselbe Quelle-Ziel-Verwechslung,
  einmal je Richtung; `blocksRaycasts` statt `interactable`, und der
  else-Zweig setzte nichts zurück. **Hilfe:** Kontrollfrage „Wer soll
  den Wert am Ende haben?" — saß danach.
- 2026-09-01 · Lobby-Design — **Selbst:** die eigene Scrollbar-Verwerfung
  mit einem neuen Argument widerrufen (Bewertung statt Vorführung) und
  den Spieler-Deckel 6 anhand gerechneter Tafelhöhen entschieden — beides
  Entscheidungen an Zahlen statt am Gefühl.
- 2026-09-02 · Verdrahtung im Menü-Controller — **Selbst:** die Trennung
  GameObject gegen Komponente („Frontend/Backend") ohne Anleitung
  gefunden; `_isPlayingAlone` als nötigen Merker erkannt; gegen doppelten
  Code selbst eine Hilfsmethode gezogen (Instinkt richtig, Zeitpunkt zu
  früh). **Fehlerbild:** `[SerializeField]` fehlte, das Feld stand im
  Laufzeit-Block; Umbenennung ohne die Geschwister, obwohl die eigene
  Regel dazu bereitstand.
- 2026-09-04 · Umzug der Dienst-Aufrufe und Tafelbau — **Selbst:** den
  Umzug in die Bestätigungs-Methode fast vollständig allein entworfen
  (nur das `Create`-Rohr für die Spielergrenze fehlte im Entwurf); die
  Tafel nach Bauplan in die Szene gebaut; `0.4f` selbst als Magic Number
  erkannt und zur Konstante gemacht; den Prefab-Bedarf (Button, Tafel,
  InputRow) selbst vorgeschlagen. **Fehlerbild:** dreimal
  „Editor-Wahrheit gegen Platten-Wahrheit" (VS-Puffer, Nur-aktive-Datei
  gespeichert, ungespeicherte Szene); `playerlimit` statt `playerLimit` —
  Signatur abgetippt statt kopiert. **Hilfe:** Klickpfad-Anleitung für
  die sieben Bauschritte; die Inspector-oder-Code-Regel beim Abfragen im
  Kern richtig, nur mit „Netzwerk" statt „später" begründet.
- 2026-09-05 · Design-Runde UI-Prefabs — **Selbst:** die Stempel-Form
  (Vorlage reinziehen und entpacken) als eigene dritte Option
  eingebracht, die in Claudes Zwei-Wege-Bewertung fehlte; das Ziel
  „einmal richtig aufbauen statt Flickwerk" selbst gesetzt und dabei
  benannt, Kriterien statt Rezepte lernen zu wollen. **Hilfe:** die
  Abgrenzung verbunden · Stempel · kein Prefab kam als Merk-Tabelle von
  Claude, samt Laufzeit-Argument für die `LobbyPlayerRow`.
- 2026-09-06 · Prefab-Umzug des Hauptmenüs — **Selbst:** die vier
  HostOptions-Knöpfe gegen Claudes Positions-Ansage richtig als
  Layout-Fall erkannt und mit LayoutElement gebaut („wie es davor war")
  — die angesagten Koordinaten waren nur das gespeicherte Ergebnis der
  HorizontalLayoutGroup; dazu den Join-Code-Winzling eigenständig auf
  200×50 vergrößert. **Fehlerbild:** an Back- und Confirm-Knopf die
  OnClick-Verdrahtung vergessen — vom Skript-Abgleich gefunden, nicht
  beim Bauen. **Hilfe:** Verdrahtungs-Ansagen je Knopf aus dem
  Vorher-Protokoll.
- 2026-09-06 · Schritt 5, Panel und Zeilen-View — **Selbst:**
  Spawner-Handler samt `SpawnWithOwnership` allein; `OnReadyClicked`
  auf Anhieb fehlerfrei; `TryGetValue` nach einem Hinweis sauber
  übernommen; eigene Funde: fehlendes LayoutElement am neuen
  Start-Knopf, das MPPM-Namens-Wettrennen korrekt auf geteilte
  PlayerPrefs getippt, den Bereit-Haken zur Sichtbarkeits- statt
  Farbfrage umentschieden, MaxPlayers-Doppelpflege als Wartungsfalle
  erkannt (führte zur Service-Property); beim API-Streit dreimal auf
  dem Editor-Befund beharrt — Auflösung durchs Lesen der
  Obsolete-Meldung, beide lagen halb daneben. **Fehlerbild:** zweimal
  Objekt statt Komponente erzeugt (Roster — Merksatz:
  Hierarchy-Rechtsklick baut Objekte, Add Component baut Fähigkeiten);
  Fallthrough nach if zweimal; im Dictionary gesucht statt
  nachgeschlagen (`row == player` über zwei Typen); Ping-Kette Quelle
  vor Ziel plus vertauschte Farbstufen. **Hilfe:**
  Existenz-gegen-Zustand als Antwort auf die eigene
  Awake/Start-Regel-Frage; `.Values`/`.gameObject`-Griffe; Gerüste mit
  vordeklarierter NGO-Syntax.
- 2026-09-06 · Erste Netz-Klasse (`LobbyPlayer`) — **Selbst:** Entwurf zu
  drei Vierteln richtig (Werte, Lebenszyklus, ein-Objekt-je-Spieler);
  beide RPC-Rümpfe und `OnNetworkSpawn` auf Anhieb, PlayerPrefs-Key
  eigenständig zur Konstante gezogen; den Spawner-Handler samt
  `SpawnWithOwnership` gefüllt, erster Live-Test erfolgreich.
  **Fehlerbild:** im Ping-Takt zuerst Schreiben vor Messen — dieselbe
  Quelle-Ziel-Verwechslung wie am 01.09., über die eigene Kontrollfrage
  („Wer soll den Wert am Ende haben?") selbst aufgelöst; beim Entwurf
  Owner-Schreibrecht statt Host-Schreibrecht angesetzt (am Ping-Argument
  verstanden). **Hilfe:** NetworkVariable-Deklarationssyntax und
  RPC-Attribute als Gerüst, Cast-Hinweis ulong→int, Sortier-Fragen statt
  Lösung.
  Claudes Datei-Befund dreimal auf dem eigenen Inspector-Blick bestanden
  („da ist nichts drin") und recht behalten — der Parser las verwaiste
  Listen-Overrides als wirksam, obwohl `Array.size = 0` sie aufhebt;
  dazu zweimal die Stil-Ansage mit bestandskonformeren Werten
  überstimmt (Zähler in LiberationSans nach der Value-Konvention,
  Caption im Feld-Label-Stil). **Fehlerbild:** Objektname „Roaster",
  drei leere Rest-Images im Roster, ein Speicherstand-Versatz
  (Stern-Regel). **Hilfe:** Klickpfade je Runde, Häkchen-Sprite von
  Claude generiert, Maß-Nachträge aus dem Audit.
- 2026-09-06 · Lobby-Chat, Abendabschnitt (Regler: Claude schreibt) —
  **Selbst:** die Chat-UI nach Schrittliste in der Szene gebaut und
  dabei vorgegriffen (ScrollRect samt Clamped und Verdrahtung, Rich
  Text aus, Character Limit 100 — vor der jeweiligen Ansage); beim
  Font-Zwischenfall das Muster „kommt wieder, egal was ich tippe"
  präzise gemeldet — der Schlüssel zur Diagnose; Polishing-Befunde
  eigenständig gesammelt (Scroll zu flott, Feldgrößen,
  Fullscreen-Frage, Namensgrenze) und die Semester-Reihenfolge aus dem
  Kopf richtig rekonstruiert (deckte sich mit der ROADMAP).
  **Fehlerbild:** im Debug-Inspector einen leeren Persistent-Call
  angelegt (Rohansicht nicht als solche erkannt); das Eingabefeld
  zunächst als Kind in den Scroll-Verlauf gehängt (Umhäng-Versatz
  Pos Y 131 blieb stehen). **Hilfe:** Hierarchie-Soll als Diagramm,
  nachgerechnete Anker-Werte, onSubmit-Abo in den Code verlegt. Das
  Gegenlesen der RPC-Kette ist bewusst auf morgen vertagt.
- 2026-09-06 · Abend-Abfrage, sechs Fragen auf Isors Wunsch —
  **Selbst:** Host-Stempel-Begründung vollständig richtig (Manipulation,
  Name aus dem Netzobjekt); Event-Abo-Muster samt Ansammlungs-Argument;
  die Chat-Kette ohne Code-Lektüre zu gut der Hälfte hergeleitet
  (Objekt je Spieler, Weg über den Host); Unsicherheiten präzise selbst
  markiert — die Markierungen deckten sich mit den echten Lücken.
  **Fehlerbild:** Kernmuster Zustand-gegen-Ereignis nicht abrufbar (auf
  die Wann-Frage kam Syntax statt Kriterium; Späteinsteiger- und
  Rundreise-Teilfragen blieben unbeantwortet); `IsOwner`/Besitz nicht
  als Werkzeug genannt, obwohl selbst verbaut; die Zerlege-Aufgabe als
  „Aufgabe unklar" blockiert, während das Konzept (Kamera lokal, nur
  Positionen reisen) im selben Diktat richtig kam — die eigene
  Diagnose „Zerlegen ist die Baustelle" damit doppelt bestätigt.
  **Hilfe:** Schneide-Schablone nachgereicht (Normalfall → Weiche →
  Aufräumen → Beweis) plus Drei-Gewohnheiten-Plan für wenig Zeit
  (eigene Schrittliste vor jeder Claude-Liste, eine
  Wiederhol-Frage je Session-Start, Fragerunde je Baustein-Ende —
  Ritualisierung offen, Isor entscheidet bei der nächsten Sicherung).
- 2026-09-06 · Design-Session Gras-Assets (Blender) —
  **Selbst:** Die Design-Session geführt und ihre Grenze verteidigt —
  den Bau zweimal gestoppt, als Claude vor der Entscheidung zu
  modellieren begann. Formfehler am Bild eigenständig erkannt und
  benannt („zu arg geknickt"), was auf eine echte Konstruktionsursache
  führte (Krümmung auf zwei Segmente gedrängt). Nach dreimaligem
  Danebenliegen die entscheidende Abhilfe selbst geliefert:
  Referenzbilder, aus denen sich Proportionen messen ließen. Alle
  Design-Entscheidungen selbst getroffen, darunter der Umschwenk vom
  großen Büschel auf viele kleine.
  **Hilfe:** Übersetzung des Vorbilds in Zahlen (Seitenverhältnisse,
  Biegewinkel, Halmzahl), die Messverfahren für Deckung und Pixelgröße.
- 2026-09-07 · Noten-Auswertung und Stack-Entscheidung — **Selbst:** die
  D004-Lücke eigenständig diagnostiziert (zu wenig Spielmechaniken, weil
  einzelne Systeme zu komplex — Tiefe fraß das Breite-Budget) und die
  Berufslogik C++ → C# selbst hergeleitet; die Engine-Entscheidung trotz
  benannter Angst getroffen und den Anker samt Notausgang selbst
  eingefordert; eigene Ängste präzise benannt (C++, KI-Abhängigkeit,
  Veränderung). **Fehlerbild:** Entscheidungs-Schleife — jedes „Aber"
  lud das nächste nach, zwei abgebrochene Auswahlfelder, bis die Punkte
  einzeln beantwortet waren. **Hilfe:** Fakten-Gegenlese je Angst
  (Modul verlangt C++ ohnehin, Kommentar-Zitate, Beispiel-Spiele) und
  der DECISIONS-Eintrag mit Kontrollpunkt als Anker gegen die
  Grübelschleife.
- 2026-09-08 · Werkzeug-Setup C++/Unreal — **Selbst:** beide neuen Repos
  über GitHub Desktop committet und veröffentlicht (Lane-Defender samt
  Push, Isor-Tower-Unreal privat) und Unreal 5.6.1 samt Bridge- und
  Fab-Plugin-Warteschlange installiert — alles ohne Klickanleitung.
  **Hilfe:** Einordnung des hängenden „Überprüfen 99 %"
  (Task-Manager-Datenträger statt Launcher-Anzeige prüfen) und der
  Toolchain-Frage VS 2026 gegen UE 5.6.
- 2026-09-08 · C++-Unterricht Chapter 1 (Stoff nur gehört, nicht
  getippt — alle Code-Screenshots stammen vom Beamer) — **Selbst:**
  `argc` als Elementzahl und `return 0` als Exit-Code ans
  Betriebssystem richtig eingeordnet, die Literale-Regel des Dozenten
  sinngemäß wiedergegeben (nicht nur Zahlen, auch Strings), die
  Vorinitialisierungs-Pflicht behalten. Stärkster eigener Beitrag: der
  Einwand, der 3D-Model-Viewer sei doch ebenfalls ein Konsolenprojekt —
  daraus wurde eine echte Lücke in `Kern/CODE_GUIDELINES.md` und ein
  ROADMAP-Punkt. **Fehlerbild:** drei Übertragungsfehler aus C#, alle
  vom selben Muster — bekannte Wörter auf neue Bedeutung gelesen:
  `a_` als „Member" gedeutet statt als Parameter (Member ist `m_`,
  lokale Variablen tragen gar kein Rollenpräfix); C → C++ → C# als
  Versionsreihe gelesen statt als drei eigenständige Sprachen; „Vector"
  aus `argv` auf `std::vector` übertragen, obwohl das eine ein festes
  Array und das andere der Listen-Container ist. **Hilfe:** der
  Adress-gegen-Inhalt-Vergleich in Zahlen aufgeschrieben, die
  Präfix-Tabelle aus den CODE_GUIDELINES gegen seine Deutung gehalten.
  Dazu ein Hemmnis abgeräumt, das kein Wissenslücken-Problem war: Die
  Lesbarkeit der Systems-Hungarian-Notation hatte die Lust am
  Konsolenprojekt spürbar gedrückt („ich mag es nicht") und drohte auf
  den Stack überzugehen. Getrennt wurde beides über die belegte Zahl
  aus `Projekte/Lane_Defender/ZEITPLAN.md` — 36 h, danach gilt die
  Notation nirgends mehr — und den Vergleich mit dem Epic-Standard, der
  bis auf `b` für bool ohne Typkürzel auskommt. Die Stack-Entscheidung
  wurde dabei nicht neu aufgemacht (Anker vom 2026-09-07,
  Kontrollpunkt Ende November).
- 2026-09-09 · L1, erstes eigenes C++-Projekt — **Selbst:** VS-Projekt
  nach Anleitung angelegt, kompiliert und den Debugger bedient
  (Breakpoint, F5, Locals gelesen); die SAE-Konvention unaufgefordert
  selbst eingefordert („wir sind doch im Konsolenprojekt") — einen Tag
  nach „ich mag es nicht"; Commit V 0.0002 mit sauberem Inhalt selbst
  gebaut. **Fehlerbild:** Wiederholung vom 2026-09-08, andere Richtung:
  `a_ILive` für eine lokale Variable — das Rollenpräfix `a_` (Parameter)
  diesmal auf eine Lokale gesetzt statt auf einen Member gedeutet, dazu
  Typkürzel `I` groß statt klein. Das Rollenpräfix-System ist als System
  noch nicht verankert. **Hilfe:** Präfix-Tabelle erneut, Strg+R,R als
  Umbenennen-Werkzeug, Einordnung des Locals-Werts 0 (frisch genullter
  Stack, keine Garantie — der gelebte Grund für SAE-Regel 7).
- 2026-09-09 · L2 Ü1, Typen nach SAE — **Selbst:** den eigenen Lernraum
  verteidigt („keine Lösung zeigen, will es selber erst machen"), dann
  alle vier Variablennamen beim ersten Selbstversuch SAE-korrekt
  (`iLives`, `fSpeed`, `bIsRoundRunning`, `sPlayerName`) — das
  Rollenpräfix-Fehlerbild vom Vormittag trat nicht wieder auf; das
  Float-Suffix `f` aus C# richtig übertragen; die bool-Überraschung
  (Ausgabe 1 statt true) selbst gefunden und präzise gemeldet.
  **Fehlerbild:** `#include <string>` weggelassen, obwohl vorab
  angesagt — kompilierte nur, weil MSVCs iostream den Header transitiv
  mitliefert. **Hilfe:** Auflösung bool = kleine Zahl samt
  `std::boolalpha` als Werkzeug; Datei-Header und Ausgabetext-Korrekturen
  übernahm Claude nach Arbeitsteilung.
- 2026-09-09 · L2 Ü2, Kontrollfluss — **Selbst:** die drei Pflichtstücke
  (for, if/else, while) eigenständig zu einer verschachtelten
  Runden-Spielschleife komponiert statt sie einzeln abzuliefern; Literale
  von sich aus in benannte Werte gezogen (vor Behandlung von SAE-Regel
  11); alle Folge-Fixes selbst gebaut — Lane-Offset samt treffender
  Umbenennung, Rundenzähler durch Verschieben des Inkrements, Guard
  Clause mit `break` am Schleifenkopf und dabei defensiv `<=` statt `==`
  gewählt; beim Konstanten-Umbau Regel gegen Zustand sauber getrennt und
  MACRO_CASE samt großem Typkürzel fehlerfrei angewandt; testet
  Änderungen jetzt selbst, bevor er sie abgibt. C#-Transfer der
  Trainingsfrage 2/3: beide Compiler-Reaktionen auf `if (iLives)`
  korrekt vorhergesagt. **Fehlerbild:** die Zahl-als-Wahrheit-Regel
  falsch gedeutet („solange es 3 ist" statt „0 ist die einzige falsche
  Zahl"); das while als Dauer-Wächter verstanden statt als Prüfung nur
  am Kopf — deshalb am Vergleich (`>=`) experimentiert statt am
  Zeitpunkt; Lane-Ausgabe 0-basiert (Off-by-one); in der Verlust-Meldung
  den Reststand statt des Verlusts ausgegeben (bekanntes
  Quelle-Ziel-Muster); Game Over eine Runde zu hoch gezählt.
  **Hilfe:** Zahlen-Trace der Runde 2 plus Ablauf-Diagramm der
  Prüf-Zeitpunkte (Türsteher gegen blinde Zone); Zielbild mit
  Erfolgskriterium (bekannte Eingabe 5 → „Game Over in Round 2", nie
  −1); Konstanten-Aufgabe als Regel-gegen-Zustand-Frage gestellt.
- 2026-09-10 · C++-Unterricht UE 1, Praxisübung Formelrechner (45-min-
  Zeitbox, erste selbst getippte Übung im Unterricht) — **Selbst:**
  `GetInput()` samt Eingabe-Validierung nach Gerüst gebaut — deckt die
  offenen L2-Themen Funktionen und Validierung vorweg; erster Lauf mit
  den Kontrollzahlen exakt richtig (31.4159 / 78.5398). Für den
  vorgewarnten ignore-Hänger eine **eigene** Lösung gebaut (Aufräumen
  ans Schleifenende verlegt statt Claudes if-Vorschlag) — robuster als
  der Vorschlag, weil sie auch Restzeichen wie `.7` mit ausräumt;
  `numeric_limits<streamsize>::max()` statt Literal verbaut; SAE-Namen
  durchgängig korrekt (`bInputHasFailed`, `iRadius`, `dArea`).
  Verständnisfrage selbst gestellt (warum `int32_t` statt `int`).
  **Fehlerbild:** die Linker-Stufe war unbekannt — LNK2005 (doppelte
  `main`) nicht einordnen können und die Error List nicht als Stand des
  letzten Builds erkannt (Datei gelöscht, Fehler „blieb");
  Wiederholung vom 2026-09-09: benutzter Header nicht selbst included
  (`<limits>`, damals `<string>`) — kompilierte nur über MSVCs
  transitive Includes; `system("cls")` direkt nach der Ausgabe wischte
  das Ergebnis weg. **Hilfe:** Compiler-gegen-Linker-Zweistufigkeit
  samt Lese-Regel (LNK- vs. C-Präfix); Vorwarnung, dass `ignore()` vor
  der ersten Eingabe blockiert; Typbreiten-Erklärung (int ohne
  Größengarantie, `_t`-Familie, Brücke zu Unreals `int32`).
- 2026-09-11 · Lane Defender Ü3 Funktionen (L2, erste Funktions-Übung
  ohne Gerüst) — **Selbst:** PrintMessage-Überladungsfamilie und
  LoseLives entworfen; die Signatur-Lücke (aktueller Lebensstand fehlt)
  nach sokratischer Rückfrage selbst geschlossen; `int32_t` gegen die
  SAE-Beispiel-Praxis selbst begründet (explizite Breite) und
  konsequent durchgezogen; statt der empfohlenen float-Umstellung
  eigenständig getrennte int32/float-Überladungen gebaut — die bessere
  Lösung; `I_ADD_ROUND` ungefragt zur Konstante gemacht; C2084 über
  Semikolon-Prototypen behoben, Default-Werte korrekt nur in die
  Prototypen gesetzt; Überladungswahl („billigster Weg") danach in
  eigenen Worten richtig erklärt. **Fehlerbild:** „kompiliert" mit
  „fertig" verwechselt — Regressionslauf ausgelassen (Unterbrechung im
  Alltag) und Warnungen in der Error List ausgeblendet, dadurch
  float→int32-Abschneiden (C4244) und bool→1 unbemerkt;
  `iLives -= LoseLives(...)` — Abzug doppelt gerechnet, Spiel endete
  nie; Prototypen zunächst als Leer-Definitionen `{}` getippt (C2084
  als Schwester des LNK2005 aus UE 1); boolalpha zunächst als
  Umwandlungs-Zwang gedeutet statt als Anzeige-Schalter. **Hilfe:**
  Überladungsauflösung (Anzahl, dann billigste Umwandlung) als
  Diagramm; Deklaration gegen Definition am Semikolon erklärt; Regel
  für Default-Argumente (nur im Prototyp); cout-eigener bool-Weg.
- 2026-09-12 · Lane Defender Ü4 Eingabe-Validierung (L2, letzter
  Übungspunkt vor L3) — **Selbst:** die ganze Übung ohne Gerüst gebaut —
  eigene Funktion `ReadValueInput` mit Warteschleife, `fail`/`clear`/
  `ignore` in der richtigen Reihenfolge, Bereichsprüfung als zweite
  Ebene, `<limits>` wie beauftragt selbst included (das
  Include-Fehlerbild vom 09./10.09. trat nicht auf); das
  Nur-Enter-Verhalten eigenständig entdeckt und präzise gemeldet
  („fail merkt es nicht, wenn leer"); nach der Parameter-Erklärung den
  Umbau (Signatur auf `a_iMinLives` geschrumpft, Arbeitsvariablen in die
  Funktion, `continue` gegen die Doppel-Meldung) komplett selbst
  getippt; die leere Eingabe bewusst als Standardverhalten belassen
  (stilles Warten, kein Umbau). Testreihe `abc`/`-3`/`0`/`5` bestanden —
  je Fehleingabe genau eine Meldung, 5 startet das Spiel; belegt durch
  Claudes Gegenlauf, kompiliert warnungsfrei unter /W4.
  **Fehlerbild:** Parameter als Zugriffsweg gedeutet („die Funktion kommt
  nicht an mains Variablen, also gebe ich sie mit") — Arbeitsvariablen
  durch die Parameterliste gereicht statt lokal angelegt; beim Umzug in
  die Funktion beide Lokale erneut mit `a_`-Präfix (`a_iInput`,
  `a_bValidInput`) — dritte Auflage des Rollenpräfix-Fehlerbilds vom
  2026-09-08/09, das System ist weiter nicht verankert; Doppel-Meldung
  bei `abc` übersehen (Fallthrough nach dem if, bekanntes Muster vom
  2026-09-06). **Hilfe:** Whitespace-Regel von `>>` erklärt (Enter ist
  Whitespace — Warten, kein Fehlerzustand; peek/getline als Wege
  gezeigt); Merksatz „Parameter ist eine Tür für Wissen des Aufrufers,
  eine lokale Variable ist Werkzeug der Funktion" samt Diagramm;
  `continue` als Schnitt gegen den Fallthrough.
- 2026-09-12 · Lane Defender L3 Ü1, Adressen im Debugger — **Selbst:**
  die Übung nach Zettel durchgeführt (Breakpoint, Watch mit `&`,
  Frame-Wechsel über den Call Stack) und die Abnahme-Erklärung im Kern
  richtig: zwei Variablen, zwei Container, darum zwei Adressen
  (`0x…ee6fefa0` gegen `0x…ee6ff0a4`); dazu den Müllwert eines noch
  nicht zugewiesenen `iLives` eigenständig entdeckt und präzise
  gemeldet. **Fehlerbild:** Breakpoint zunächst am return der falschen
  Funktion (ReadValueInput statt LoseLives); die Frame-Bindung des
  Watch-Fensters unbekannt — „identifier is undefined" als Defekt statt
  als „wohnt hier nicht" gelesen; in der Erklärung den Parameter „nur
  eine lokale Variable" genannt (Karton-Verhalten richtig, der
  Tür-Begriff vom Vormittag noch nicht angewandt). **Hilfe:** Klickpfad
  samt Ebenen-Diagramm (der Watch fragt die markierte
  Call-Stack-Ebene); Einordnung des Müllwerts als gelebter Grund der
  Vorinitialisierungs-Regel.
- 2026-09-12 · Lane Defender L3 Ü2, erster Pointer — **Selbst:** das
  Snippet komplett ohne Gerüst gebaut (nullptr-Start, `&`-Verbindung,
  Wächter mit Fehler-Rückgabe, Schreiben über `*`), eigenständig
  getestet (beide Ausgaben 1) und daraus die richtige Kernregel selbst
  formuliert: „überschreibt nicht die Adresse, sondern schreibt in die
  Adresse rein"; SAE-`p`-Präfix auf Anhieb; die Sinnfrage („warum nicht
  direkt in die Variable?") selbst gestellt — und das Urteil dahinter
  stimmt: Neben dem sichtbaren Namen ist ein Pointer ein Umweg.
  **Fehlerbild:** in der Trainingsfrage das Umhängen übersehen —
  `p = &iRounds` nicht als Zustandswechsel des Pointers gelesen und
  die 7 gedanklich ans alte Ziel geschrieben; die Ebene „wohin zeigt
  er" war als Einmal-Setup verbucht, während die Ebene „was liegt
  dort" sicher saß. Dazu die Sprach-Unschärfe „der Pointer hat 7" (ein
  Pointer hat nie den Wert, nur die Hausnummer). Vorab die Rückmeldung
  „zu wenig visuell, ich habe noch nie einen Pointer gesehen" —
  berechtigt, der Theorie-Happen vor dem Entwurf war übersprungen.
  **Hilfe:** interaktives Karton-Modell (Zeigen/Lesen/Schreiben/nullptr
  samt Wächter-Toggle), der Skill-Slot aus den eigenen DECISIONS als
  Antwort auf die Sinnfrage, Zahlen-Trace und ein zweites Modell mit
  zwei Zielkartons zum Umhängen.
- 2026-09-12 · Lane Defender L3 Ü3, const-Referenzen an PrintMessage —
  **Selbst:** zwei der drei string-Überladungen im ersten Anlauf an
  beiden Orten (Prototyp und Definition) korrekt umgestellt, die dritte
  nach Claudes Befund selbst nachgezogen; Regressionslauf eigenständig
  gefahren und im Gegenlauf bestätigt (Eingabe 5 → „Game Over in
  Round 2", /W4 warnungsfrei); am Hover die richtige Detektiv-Frage
  gestellt (const char[36] vorher wie nachher — gemessen an der einen
  Station, die sich nie ändert) und die Wortfragen (Adressoperator,
  Referenz, Literal) aktiv eingefordert. **Fehlerbild:** das const
  zunächst weggelassen (non-const-Referenz hätte an den
  Literal-Aufrufen den Build gebrochen); die Referenz hartnäckig als
  Speichern-Vorgang modelliert („schreibt die Zeichen in die Adresse
  rein, immer die gleiche") — dass die Zeichen schon am Ziel liegen und
  nur gelesen wird, brauchte zwei Anläufe; zwischenzeitlich Frust
  („weiß nicht, ob ich doof bin") — Auslöser war Claudes
  Stapel-Erklärung (Temporär, Literal, Lebensdauer in einem Zug statt
  einer einzigen Unterscheidung). **Hilfe:** der Vergleich „zwei
  Adressen gegen eine Adresse — kopieren oder Hausnummer durchreichen"
  als Auflösung; Referenz als „Pointer im Autopilot" an das
  Ü2-Wissen gehängt; Vokabeltafel zu `*`/`&` nach Ort und die
  Literal-Definition an seinen eigenen Codebeispielen.
- 2026-09-12 · Lane Defender M1, Design-Auftakt — **Selbst:** den
  Programmablauf eigenständig als Szenen-Modell entworfen (Hauptmenü →
  Namenseingabe → Spiel → Endszene, hergeleitet aus der
  Unity-Szenen-Analogie) samt Bedienkonzept (Pfeile/W+S,
  Auswahlmarker) — trägt direkt den Zustandsautomaten des M1-Gerüsts;
  dazu die Highscore-Idee, die sich mit Ausbau A2 der ROADMAP deckt;
  beim Gegenlesen des Ablaufs die fehlende Steuerungs-Anzeige selbst
  bemerkt und als Zwischenszene nachgezogen.
- 2026-09-12 · Lane Defender M1, Abnahme Console-Baustein — **Selbst:**
  den Header ohne Anleitung als „Versprechen, Definition in der .cpp"
  gedeutet (Transfer aus den Ü3-Prototypen), `&lConsoleMode` als
  Schreiben über die Adresse gelesen (L3-Transfer),
  `INVALID_HANDLE_VALUE` korrekt als −1 getippt, Guard-Struktur und
  die Scan-Code-Übersetzung erkannt; Includes selbst mit C#-usings
  verknüpft. **Fehlerbild:** „if-Schleife" als Wort; die Prefix-Codes
  224/0 zunächst als „nicht legitime" Tasten gedeutet statt als
  Ankündigung des zweiten Codes; `#define`, Header-Rolle und `flush`
  unbekannt — neuer Stoff, kein Verwechsler. **Hilfe:**
  Compiler/Linker-Diagramm (C- gegen LNK-Fehler an den eigenen Fällen
  C2084/LNK2005), define = Textersetzung, flush = Sammelmappe leeren,
  Out-Parameter als Tür für die Antwort. Transferfrage danach: .h/.cpp-
  Zuordnung sicher; die fehlende Einlösung aber als Compiler- statt
  Linker-Fehler getippt (LNK2005 aus UE 1 nicht mehr abrufbar). Dazu
  offen benannter Motivationsknick: der WinAPI-Teil wirkt „kryptisch,
  in C# würde ich das verstehen" — Auslöser ist die
  Betriebssystem-Schicht des gelieferten Bausteins, nicht der eigene
  C++-Code (dieselbe Quelle wie das SAE-Hemmnis vom 2026-09-08).
- 2026-09-12 · Lane Defender M1, Vertiefung InitConsole (interaktive
  Stationen-Maschine) — **Selbst:** den Out-Parameter präzise erklärt
  („Adresse ist der Ort, an den GetConsoleMode schreiben soll, keine
  Kopie") und dazu eigenständig das richtige API-Schnittstellen-Bild
  gebildet; den Zweck des VT-Bits in eigenen Worten („Befehle bleiben
  unsichtbar und wirken"); die Fail-Pfade der Guards korrekt gelesen.
  **Fehlerbild:** Bit-Wert mit Bit-Position verwechselt („Bit 4" als
  viertes Bit gelesen); die Codepage als weiteres Modus-Bit
  einsortiert, obwohl sie ein eigener Schalter ist; den bool-Rückgabewert
  an „alle Bits gesetzt" geknüpft statt an „alle Handgriffe geklappt";
  führende Null in 0111 unklar. Teils von Claudes Lampen-Beschriftung
  und einer verunglückten Rechenfrage mitverursacht. **Hilfe:**
  Stellenwert-Tafel 8/4/2/1 samt 007-Vergleich für die führende Null,
  Trennung der zwei Ebenen (Handgriff-Erfolg gegen Schalter-Inhalt),
  Bytes-Brille für die Codepage (226/148/140 als Ôöî gegen ┌).
- 2026-09-12 · Lane Defender M1, Bit-Oder an InitConsole — **Selbst:**
  2 | 4 = 6 samt richtigen Lampen; nach der Spalten-Erklärung offen
  gesagt „ich verstehe | nicht" — präzises Selbst-Markieren der Lücke.
  **Fehlerbild:** | zunächst als + gedeutet (ging bei getrennten Bits
  zufällig auf); 4 binär als 0011 geschrieben (das wäre 3); die
  Folge-Antwort „bzw 0110" blieb mehrdeutig (Korrektur der eigenen
  Binärdarstellung oder 7|4-Versuch mit verrutschter 1er-Spalte).
  **Hilfe:** Spaltentafel mit Stellenwerten 8/4/2/1, Merksatz „an oder
  an = an", und das Plus-lügt-Beispiel 7+4 = 1011 (Übertrag verstellt
  Schalter, die niemand angefasst hat). Auflösung danach: die
  Kern-Einsicht „7 | 4 bleibt 7" selbst gezogen; hartnäckig blieb nur
  die Binär-Schreibweise — 7 zweimal als 0110 notiert, die 1er-Spalte
  fällt wiederholt weg. Gegenmittel: Merksatz „ungerade Zahl = letzte
  Stelle 1".
- 2026-09-12 · Lane Defender M1, SetConsoleMode-Zeile selbst zerlegt —
  **Selbst:** `ENABLE_VIRTUAL_TERMINAL_PROCESSING` = 0x0004 eigenständig
  in VS nachgeschlagen und richtig als „da kommt immer 4 raus" gedeutet;
  die Kette „SetConsoleMode gibt bool, darf nicht FALSE sein, sonst
  Abbruch" korrekt nacherzählt; die eigene Unsicherheit präzise benannt
  („was gerade im Modus drinsteht, weiß ich ja nicht") — genau die
  Lücke, die das Lesen-Oder-Zurückschreiben-Muster schließt.
  **Fehlerbild:** Rollen kurz vertauscht (Handle als „das Ausgelesene"
  statt als Ansprechpartner); `SetConsoleOutputCP` als „.cpp" gehört
  (Diktat); der Dreifachschritt der return-Zeile (Aufruf, Vergleich,
  return in einem) unklar. **Hilfe:** Wer/Was-Trennung
  (Handle = welche Konsole, Mode = was eingestellt ist),
  Hex-Kurzerklärung zu 0x, Get/Set-Anker an C#-Properties, die
  return-Zeile in Langform, BOOL als Zahl-Wahrheit an Ü2 angebunden.
  Fortsetzung nach eigener Gesamt-Nacherzählung: Ablauf Ausweis → Guard
  → Karton füllen sowie „dritte Stelle dazu, von 3 auf 7" jetzt korrekt
  wiedergegeben, „0 heißt automatisch false zurück" selbst gefolgert,
  und das eigene Nicht-Sitzen ehrlich markiert. Hartnäckig zwei
  Lese-Fehler mit derselben Wurzel (mehrere Schritte in einer Zeile):
  das `|` im if als Vergleich gelesen und `return X != FALSE` als
  bedingtes return („sonst gebe ich gar nichts zurück"); der Handle
  blieb „irgendwas von Windows". Gegenmittel: Zeitlupen-Langform beider
  Zeilen, Garderoben-Marke als Handle-Bild, Umleitung `> log.txt` als
  echter Fall, in dem die Guards greifen.
- 2026-09-12 · Lane Defender M1, ClearScreen und ReadKey — **Selbst:**
  das Tempo selbst gedrosselt („Halt, stopp, du bist zu schnell") —
  wie am 09.09. den eigenen Lernraum verteidigt; ClearScreen-Zweck
  (leeren plus Cursor setzen) und den ReadKey-Grundablauf samt
  Guard-Rückgabe und Neu-Mapping korrekt erklärt. **Fehlerbild:**
  `flush` mit dem Bildschirm-Löschen vermengt („sammelt und cleart
  dann alles") — das Wort „leeren" war doppelt belegt (Bildschirm
  gegen Mappe); der Zweck der Prefix-Werte 224/0 unklar („für was habe
  ich die?"). **Hilfe:** WhatsApp-Bild (cout tippt den Entwurf, flush
  drückt Senden, endl ist Enter mit Auto-Senden), 224/0 als „Achtung,
  Durchsage"-Ankündigung samt Pflicht zum zweiten _getch gegen
  liegengebliebene Geistertasten (Anker: das liegengebliebene \n bei
  cin). Nachgang: die Geistertasten-Folge im Kern selbst formuliert
  („der nächste Lesevorgang bekäme den falschen Wert in iKey") — die
  Ursache dabei an der Variablen-Adresse verortet statt in der
  Tastatur-Warteschlange; Auflösung über das Bild der Warteschlange,
  aus der jedes _getch nur den vordersten Wert nimmt. Zur
  flush-Kontrollfrage kam „der Befehl würde gelöscht, aber die Message
  kommt noch" (Diktat, mehrdeutig) — die Hälfte „kommt später noch an"
  stimmt; klargestellt, dass dabei nichts verloren geht: Der Entwurf
  wartet und reist mit dem nächsten Auto-Senden mit. Nach einer Pause
  das Ansammeln-Modell selbst sauber formuliert (Container füllt sich,
  gesendet erst bei endl oder flush) und die Restlücke präzise benannt:
  Unterschied endl gegen flush — Vermutung „flush macht mehr", richtig
  ist das Gegenteil. Auflösung: endl = "\n" + flush, flush sendet nur;
  ClearScreen darf gerade keinen Umbruch anhängen, weil der den frisch
  gesetzten Cursor eine Zeile nach unten schöbe.
- 2026-09-12 · Lane Defender M1, Abschluss-Siegel Console-Baustein
  (je ein Satz je Funktion, frei formuliert) — **Selbst:** ClearScreen
  fehlerfrei (leeren, Cursor an den Start, mit flush senden); das
  ReadKey-Konzept richtig (normale gegen Spezialtasten, Scan-Codes auf
  eigene Konstanten ummappen, Unbekanntes als I_KEY_UNKNOWN);
  eigenständig beschlossen, die M1-Arbeitszeit ab jetzt mit Grindstone
  zu tracken — deckt genau die Ist-Spalte des ZEITPLANs.
  **Fehlerbild:** InitConsole als „stoppt mein Programm automatisch"
  erklärt — Melden mit Entscheiden verwechselt (die Funktion gibt nur
  bool zurück, der Aufrufer entscheidet; derselbe Ebenen-Mix wie bei
  bool gegen Bits), dazu „guckt, ob die Konsole ausgeben kann" statt
  „stellt sie um"; im ReadKey-Satz iKey und iScanCode einmal verdreht
  (Konzept dahinter stimmte). **Hilfe:** Merksatz „Funktionen melden,
  Aufrufer entscheiden"; Dreizeiler-Ablauf zum Geradeziehen der
  Variablenrollen. Console.h/.cpp hatte er zu diesem Zeitpunkt bereits
  eigenständig in VS eingebunden und gebaut, ohne den Klickpfad zu
  brauchen.
- 2026-09-12 · Lane Defender M1, Entwurf Zeichentest-Szene (Entwurf
  vor Gerüst) — **Selbst:** über die Vorgabe hinaus einen eigenen,
  zweiten Test erfunden: ein Symbol läuft Tick für Tick eine Mini-Lane
  mit Wänden hinab, um die Stabilität beim Neuzeichnen zu prüfen —
  nimmt exakt die M2-Rendering-Situation vorweg; die Lane-Breite mit
  zwei Plätzen deckt sich ungeplant mit der beschlossenen
  Doppelzellbreite; C#-Brücke Console.SetCursorPosition selbst
  gezogen. **Fehlerbild:** das Symbol einzeln per Cursor setzen wollen
  statt des beschlossenen Ein-Puffer-Renderings (ganzer Frame als ein
  String, Cursor-Home, einmal senden); ein Feld-Array angesetzt, wo
  als Zustand eine einzige Zahl reicht. **Hilfe:** Merksatz „der
  Zustand ist die Zahl, das Bild wird jeden Tick frisch daraus
  gebaut"; Home-statt-Löschen als Flacker-Schutz aus den DECISIONS.
- 2026-09-13 · Lane Defender M1, Output-Umzug (erster eigener Header) —
  **Selbst:** die Datei-Trennung selbst eingefordert und mit der
  eigenen C#-Regel begründet (eine Zuständigkeit je Klasse → in C++ je
  .h/.cpp-Paar); die Kontrollfrage zu LoseLives richtig beantwortet
  (Spiellogik, keine Ausgabe) und es konsequent ganz entfernt statt es
  herrenlos liegen zu lassen; beide Dateien über VS angelegt
  (Projekteintrag automatisch); Default-Argumente beim Umzug korrekt
  nur im Header belassen. **Fehlerbild:** beim Ausschneiden
  Nachbarzeilen mitgerissen — das Console-Include und die
  LoseLives-Definition verschwanden still, und der Build blieb grün,
  weil die leere main nichts ruft („kompiliert ist nicht fertig" in
  neuer Form: Der Linker sucht nur Gerufenes); Includes zunächst
  weiter über die Console.h-Textkopie geliehen. **Hilfe:** Erklärung
  der stillen Grün-Falle; SAE-Köpfe und Summaries übernahm Claude —
  nach Isors berechtigter Rüge, sie standen fälschlich in seiner
  Aufgabenliste (Arbeitsteilung aus CODE_GUIDELINES).
- 2026-09-13 · Lane Defender M1, Zeichentest gebaut und gemessen —
  **Selbst:** Init-Guard mit Meldung und Fehler-Rückgabe allein, dazu
  unaufgefordert die Design-Frage nach benannten Exit-Codes (eigene
  Fehlerliste ab 1000) — nach Bewertung selbst auf eine lokale
  Konstante mit Wert 1 entschieden; die Array-Klammer-Position über
  den Compiler-Fehler gefunden; die Doppelschleifen-Struktur (Wände
  außen, zehnmal innen) stand im ersten Entwurf; das foreach nach der
  Zerlegung korrekt eingebaut; am laufenden Test die Schach-Doppelbreite
  selbst vermessen („braucht 2 Zellen") und daraus live ein
  Lane-Layout entworfen (Wand + vier Leerzellen, Figur mittig, Schuss
  zwei Zellen breit — als M2-Merker in der ROADMAP). **Fehlerbild:**
  `S_SYMBOL_CANDIDATES->length()` — das Array zerfiel still zum
  Pointer aufs erste Element, gemessen wurde die Textlänge von „A",
  die Schleife endete nach zwei Zeilen; die Bewerberliste zunächst als
  „je Rolle ein String" gebündelt und die Kommentar-Aufzählung als
  Unicode-Bauteile gedeutet; PrintMessage ohne zweites Argument — der
  Default machte je Symbol einen Umbruch; Überforderungs-Frust, als
  Meta-Umbauten und neuer Stoff sich stapelten („bin komplett
  draußen") — Auslöser war die Menge zugleich, nicht der Stoff.
  **Hilfe:** die foreach-Zeile zerlegt mit C#-Spiegel (foreach/in ↔
  for/Doppelpunkt); die Bewerberliste als Tabelle (drei Kandidaten je
  Rolle, einer gewinnt); Rest-Feinschliff (Lineal, Literal-Wände,
  ReadKey) übernahm Claude auf Zuruf; Step-für-Step-Modus mit
  Einzelvorlage je Schritt eingeführt.
- 2026-09-13 · Lane Defender M1, SymbolTest-Auslagerung (unaufgefordert,
  am Abschnittsende) — **Selbst:** die Test-Szene komplett
  selbstständig in ein eigenes Paar `SymbolTest.h`/`SymbolTest.cpp`
  ausgelagert — die Dateipaar-Regel vom Vormittag aus eigenem Antrieb
  angewandt und damit die Szenen-Struktur von M2 vorweggenommen; alle
  vier Includes der neuen .cpp selbst getragen (das Include-Fehlerbild
  trat nicht wieder auf); Prototyp samt Summary korrekt mitgezogen.
  **Fehlerbild:** die Exit-Konstante von main im SymbolTest-Header
  geparkt (fremde Zuständigkeit — die Utils-Falle im Kleinen), dadurch
  lieh sich der Header int32_t über die Include-Kette; der eigene
  Header fehlte als erster Include der .cpp (Signatur-Abgleich
  entfällt). **Hilfe:** beide Funde über Isors eigene Dateipaar-Regel
  erklärt, Rückverlegung und Köpfe im Kommentar-Pass durch Claude.
