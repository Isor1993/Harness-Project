# ROADMAP.md — Bauplan It's D.O.T

Ownership: Nur was an It's Dungeon Outbreak Time (Kürzel It's D.O.T;
Harness-Schicht Its_DOT) als Nächstes designt oder gebaut
wird — Aufgaben und Verweise auf offene Fragen. Begründungen gehören in
die DECISIONS dieser Schicht, die Design-Absicht ins GDD; die Termine
besitzt `Uni/Semester_3/STUNDENPLAN.md`.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

## Aufgaben

- [x] **G1 · Mini-GDD zur Freigabe** — **erledigt am 2026-10-09:**
  Layout-Runde und Befüllung Block für Block, Manuskript `MINI_GDD.md`,
  als Textdatei per Discord verschickt (DECISIONS → „Mini-GDD:
  Zuschnitt und Versandweg"). Die Freigabe-Antwort kam am 2026-10-12:
  in der Formulierung zu groß, Fokus unklar (`Uni/LOG.md`). Folge:
  zwei GDDs parallel, die Dozentin wählt (`Uni/DECISIONS.md` →
  „2026-10-13 — Zwei Konzepte parallel bis zur Wahl der Dozentin").
- [ ] **G2 · Volles Pitch-GDD und Präsentation** — nächste Session:
  eigene Layout-Runde (Kapitelstruktur nach der Aufgabenstellung),
  dann Punkt für Punkt befüllen; Erstfassung bis zum 18.10.
  (DECISIONS → „Reihenfolge bis zur Abgabe: GDD vor Prototyp").
  Deckblatt als Template aus `TDD Titelteil.docx` übernehmen (nur die
  Felder neu), gebaut wird mit der schlanken Formatvorlage im
  Datenbaum unter `05_Werkzeuge\Vorlagen`
  (`Kern/PFADE.md` → `DATENBAUM`). In der Abgabe minimal,
  Erweiterungen nur als Stichpunkte „modular erweiterbar"; Frist
  Fr 27.11., Präsentation Do 03.12.
  (`Uni/Semester_3/STUNDENPLAN.md`). Seit dem Feedback vom 2026-10-12
  zuerst als Konzept-GDD für die Wahl der Dozentin, zusammen mit dem
  Pathmakers-TD-GDD; die Fragenliste aus dem Feedback (`Uni/LOG.md`)
  dient als Prüfliste, der Umfang wird neu geschnitten (`GDD.md` →
  „Umfang-Feinschnitt", der Rest der Feedback-Frage ist seit dem
  2026-10-14 beantwortet).
  **Stand 2026-10-16:** Die GDD-Erstfassung ist komplett (alle Kapitel
  geschrieben, Abgabe-Teil 2422 Wörter, gemessen; Quellenverzeichnis
  bewusst vertagt, verifizierte Liste im GDD-Entwurf). Die .docx ist
  gebaut und von Isor fertiggestellt: Titel „It's Dungeon Outbreak
  Time" (DECISIONS, 2026-10-16), Deckblatt aus dem Titelteil-Template,
  Verzeichnisse per F9 gefüllt, Wortanzahl aus Word übernommen; die
  Abgabe-Ende-Marke in `abgabe_bauen.py` hält die internen Abschnitte
  draußen. Vertieft wird das GDD erst, wenn das Konzept gewählt und
  verwirklicht wird (Isor, 2026-10-16). Offen in G2: PDF-Export und
  Versand zur Konzept-Wahl (Ziel So 19.10.; der Termin-Nachtrag in
  der Uni-Schicht steht weiter aus) und später die Präsentation am
  03.12.
- [ ] **P1 · Prototyp-Start** — ab dem 18.10., direkt nach der
  GDD-Erstfassung (DECISIONS → „Reihenfolge bis zur Abgabe: GDD vor
  Prototyp"); vorher die Fragen klären, die den ersten Baustein
  betreffen — mindestens Verloren-Kriterium und Slot-Befüllung
  (`GDD.md` → „Offene Design-Fragen").
  **Stand 2026-10-18:** Das Fundament steht — Schicht nach `Its_DOT`
  umgezogen, Repo `Its-DOT` mit Unity-Projekt `ItsDOT` (6.3 LTS,
  URP), MainMenu-Kette migriert und im Play-Test lauffähig, alle
  Startwege zielen auf die leere Testarea-Szene (DECISIONS, Einträge
  vom 2026-10-17/18). Offen vor dem Bauen: den Testarea-Plan
  schneiden und die P1-Fragen klären.
- [x] **Schicht-Ordner bei Projektstart prüfen** — **erledigt am
  2026-10-17:** Umzug nach `Projekte/Its_DOT/` beim P1-Projektstart
  (Beleg: `DECISIONS.md` → „2026-10-17 — Schicht-Umzug nach Its_DOT").
  Ursprünglicher Zuschnitt: Wird das Konzept gewählt und gebaut,
  entscheidet Isor, ob die Schicht von `Isors_Outbreak` auf einen
  It's-D.O.T-Namen umzieht (Zuruf vom 2026-10-16: erst einmal so
  lassen). Falls ja, Umzug nach den Handgriffen aus
  `Kern/DOC_RULES.md` → „Wenn Inhalt umzieht".
- [ ] **T1 · Mengen- und Physik-Budget messen** — im Prototyp:
  Alive-Cap, Ragdoll-Anzahl, Schwarm gefakt gegen Elite voll;
  Richtwerte stehen im GDD → „Entwurf". Messen statt schätzen.
- [x] **Menü-Nachzügler: First Selected je Panel** — **erledigt am
  2026-10-18** (Beleg: Its-DOT-Commit „Update V 0.0003" —
  `PanelFirstSelected` je Panel, `SelectionGuard` am EventSystem,
  Explicit-/Automatik-Verdrahtung; Wissens-Destillat in der
  Knowledge-Seite `eventsystem-menu-navigation`). Bekannter Rest:
  Von Create Lobby führt Links auf Minus statt Back
  (Automatik-Raterei) — von Isor bewusst so gelassen; die
  Eskalationsstufe wäre Laufzeit-Umverdrahtung im Code.
  Ursprünglicher Zuschnitt: beim Panelwechsel verliert das
  EventSystem die Auswahl; je Panel ein First Selected setzen.
- [ ] **Relay-Echttest über zwei Netze** — der Play-Test vom
  2026-10-18 lief lokal; Join-Code über das echte Netz gegen das
  neue UGS-Projekt einmal belegen, bevor der Multiplayer-Test der
  Testarea ansteht. Dabei dem Leave-Weg zusehen: Beim Back aus der
  Lobby warnt `StopAsync: Failed to stop session: session was never
  started` (vermutlich doppelter Stopp über NetworkManager und
  Session; aufgefallen am 2026-10-18, womöglich neu seit Multiplayer
  Services 2.4.1).
- [ ] **Lobby-Panel: Rollen-Flackern beseitigen** — nach Create
  Lobby zeigt das Panel erst den Gast-Zustand (Ready) und springt
  auf Start Game um, sobald der Host registriert ist. Isors
  Vorschlag vom 2026-10-18: das Panel erst zeigen, wenn Verbindung
  und Rolle stehen. Berührt Controller, Dienst-Rückrufe und
  `LobbyPanel.SetRole` — eigener Design-Moment, kein Schnellfix.

## Testarea — Bausteine (Zuschnitt und Schätzungen: DECISIONS → „2026-10-18 — Testarea-Zuschnitt")

- [ ] **B1 · Testarea + Spieler im Netz** — Blockout-Boden,
  Spielerfigur neu: Owner-Movement, Kamera, Springen; dazu der
  NGO-Wiedereinstieg (NetworkManager, NetworkObject, Autorität).
  Startet mit eigener Design-Runde. (~6–8 h)
- [ ] **B2 · Nahkampf + Schaden** — Health-Komponente neu, Host
  entscheidet Treffer, Gegner können sterben. Erster Koop-Test über
  echtes Netz = zugleich der Relay-Echttest von oben. (~4–5 h)
- [ ] **B3 · Simple Gegner-KI** — host-gesteuert: verfolgen,
  zuschlagen, sterben; bewusst dumm. (~5–6 h)
- [ ] **B4 · Dungeon-Portal** — Platzhalter-Portal, spawnt Gegner im
  Takt; ein Portal, von Hand gesetzt. (~2–3 h)
- [ ] **B5 · Loot-Drop + Aufsammeln** — Container beim Tod des
  Gegners, Host schlichtet gleichzeitiges Greifen. (~3–4 h)
- [ ] **B6 · Quick-Slot-HUD** — Hotbar mit Waffen-Slots, Zähler für
  zwei bis drei Loot-Sorten (DECISIONS → „Quick-Slot-HUD statt
  Inventar"). (~4–5 h)
- [ ] **B7 · Fall + Respawn** — Umkippen, 10-s-Timer, Respawn am
  Herzobjekt-Platzhalter, Loot-Container am Todesort (DECISIONS →
  „Fall beim Outbreak"). (~3–4 h)
- [ ] **Reserve · Fernkampfwaffe** — nur wenn B1–B7 schneller gehen
  als geschätzt; Projektil übers Netz ist der Mehrpreis.
