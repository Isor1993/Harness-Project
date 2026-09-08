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
