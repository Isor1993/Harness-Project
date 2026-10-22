# ROADMAP.md — Bauplan Pathmakers TD

Ownership: Nur was an Pathmakers TD als Nächstes designt oder gebaut
wird — Aufgaben und Verweise auf offene Fragen. Begründungen gehören in
die DECISIONS dieser Schicht, die Design-Absicht ins GDD; die Termine
besitzt `Uni/Semester_3/STUNDENPLAN.md`.
Format: `- [ ] **<Kürzel> · Titel** — Inhalt in Stichworten.` Abgehakt
wird mit Beleg (LOG-Eintrag oder Datei).

## Aufgaben

- [x] **G1 · Volles GDD** — **erledigt am 2026-10-17** (Beleg: die
  Einträge vom 2026-10-17 in `DECISIONS.md` und die gebaute Abgabe im
  Datenbaum unter `01_Uni\Semester_3\Arbeitsdateien`,
  `Kern/PFADE.md` → `DATENBAUM`). Ursprünglicher Zuschnitt: startet,
  sobald das Outbreak-GDD steht;
  Ziel für beide: Do/Fr 15./16.10. Eigene Layout-Runde (Kapitel stehen als
  Platzhalter in `GDD.md`), dann Punkt für Punkt befüllen, beginnend
  mit Pitch und Kern-Schleife aus dem „Entwurf". Die Fragenliste aus
  dem Freigabe-Feedback vom 2026-10-12 (`Uni/LOG.md`) dient als
  Prüfliste: Jede Frage soll das GDD beantworten oder bewusst
  ausschließen. Geht zusammen mit dem Outbreak-GDD an die Dozentin
  (`Uni/DECISIONS.md` → „2026-10-13 — Zwei Konzepte parallel bis zur
  Wahl der Dozentin").
  **Stand 2026-10-17:** Das GDD ist inhaltlich komplett — Durchgang
  aller sechs Kapitel (größter Fund: Wellenmodell auf „nur Sends"
  umgestellt, keine automatischen Wellen), Thema-Kapitel samt
  Turm-Entscheidung (Wächter-Figuren), Sackgassen-Regel geschlossen,
  alle Restkapitel gefüllt; offene Design-Fragen: keine; neun neue
  Einträge in `DECISIONS.md`. Gleichentags gebaut und versandt:
  Manuskript auf Abgabe-Konvention gebracht (Kommentar-Kopf,
  `#`-Kapitel, Abgabe-Ende-Marke, Quellenverzeichnis-Satz), .docx mit
  Titelteil gebaut, beide GDDs als PDF per Discord an die Dozentin.
  Die Konzept-Entscheidung ist am 2026-10-20 gefallen: Pathmakers TD
  wird das Semester-Spiel (`Uni/DECISIONS.md` → „2026-10-20 —
  Semester-Spiel: Pathmakers TD; It's D.O.T wird privates Projekt").
  Die Schicht ist damit die aktive; die Aufgaben darunter sind neu.
- [x] **P1 · Prototyp-Start** — **erledigt am 2026-10-20** (Beleg: die
  DECISIONS-Einträge vom 2026-10-20 und der Baustein-Abschnitt unten).
  Ursprünglicher Zuschnitt: zuerst eine Brainstorm-Runde zum
  Vorgehen und zum Schnitt der ersten Bausteine (Isor, 2026-10-20),
  danach der Blockout. Übernehmbar aus dem Its-DOT-Prototyp, weil
  Pathmakers ebenfalls vier Spieler über Relay braucht: Netz-Grundlage
  (NGO, Relay, Lobby mit Join-Code), die Menü-Kette und die
  Spielerfigur samt Kamera.
  **Stand 2026-10-20:** Die Brainstorm-Runde ist gelaufen — Netz von
  Anfang an, Reihenfolge und Schnitt stehen; der Blockout selbst ist
  jetzt Teil der Bausteine P-B1 und P-B3 unten.
- [ ] **P2 · Playtests und Erkenntnis-PDF** — Testrunden über das
  echte Netz und das Abgabe-PDF des Prototyps (mind. 500 Wörter:
  ursprüngliche Idee, was ändern, was übernehmen —
  `Uni/Semester_3/VORJAHR_AUFGABEN.md` → „3 · Spieleprototyp").
  Bekommt fest die letzte Woche vor dem 27.11., nicht den Rest.
- [ ] **A1 · Pitch-Abgabe und Präsentation** — das GDD liegt fertig;
  nötig sind die Präsentationsfassung und der PDF-Export. Termine in
  `Uni/Semester_3/STUNDENPLAN.md`.
- [ ] **G2 · GDD-Nachzug nach der Präsentation** — die
  Aufgabenstellung verlangt das GDD mit eingearbeitetem Feedback
  (`Uni/Semester_3/ASSIGNMENT_GAME_PITCH.md`). Einzuarbeiten sind die
  Zweck-Kette der Mechaniken und die im Discord-Durchgang vom
  2026-10-20 gegebenen Antworten (`Uni/LOG.md`); das Rohmaterial steht
  in `GDD.md` → „Entwurf", Eintrag vom 2026-10-20. Dazu der
  Steuerungs-Nachzug: Steuerungs- und Kamera-Kapitel sowie der
  Vergleichs-Halbsatz („nicht aus der Befehlssicht") auf das
  Befehlsklick-Modell bringen (DECISIONS → „2026-10-21 — Steuerung:
  Befehlsklick statt Direktsteuerung").

## Prototyp — Bausteine

Zuschnitt und Begründung: DECISIONS → „2026-10-20 — Prototyp-Schnitt:
Isors Reihenfolge, Wächter spät". Schätzungen von Isor, bewusst mit
Multiplayer-Aufschlag; P-B1 bis P-B7 füllen das Bau-Budget bis zum
27.11. komplett, nach P-B4 steht der Prüfpunkt zum Wächter-Vorziehen.

- [x] **P-B1 · Fundament im Netz** — **erledigt am 2026-10-22** (Beleg:
  LOG-Einträge vom 2026-10-20 bis 22, Zeiten und Gebautes in
  `ABGABE_NOTIZEN.md` → „P-B1 · Fundament im Netz"; Zwei-Instanzen-
  Test über Relay bestanden). Ursprünglicher Zuschnitt: Repo
  `Pathmakers-TD` samt
  Unity-Projekt `PathmakersTD`, NGO/Relay/Lobby und Menü-Kette
  übernehmen, Kachel-Boden als Testfläche, Figur mit Kamera als
  Owner-Movement (B1-Movement-Design aus `Projekte/Its_DOT/`).
  (~12–14 h)
  **Stand 2026-10-21:** Repo, Unity-Projekt, eigenes UGS-Projekt und
  die Übernahme aus Its-DOT stehen (LOG; Commits V 0.0001/0.0002),
  das Testarea-Gym ist mitübernommen. Offen: Spielerfigur samt
  Kamera — Steuerungsmodell neu entschieden (DECISIONS → „2026-10-21
  — Steuerung: Befehlsklick statt Direktsteuerung"): NavMeshAgent
  statt Owner-Movement-Motor. Die Figur-Design-Runde ist
  abgeschlossen (drei DECISIONS-Einträge vom 2026-10-21,
  Rest-Schätzung ~8–9 h). Tafeln: Status
  https://claude.ai/artifact/5JZCpkKe2MVnCC9R2ScuvJ · Steuerung
  https://claude.ai/artifact/DztjtxavWXmwrMP3YxZoET
- [ ] **P-B2 · Weg-Bau** — Kachelraster, Geisterbild an der Maus,
  Figur läuft zur Baustelle, Kacheln legen und abbauen,
  Weg-Zusammenhang ab Startpunkt — netzsynchron. (~10–12 h)
- [ ] **P-B3 · Karte + Spawns** — Blockout der echten Karte: vier
  Gebiete, Größe einstellen, Start- und Endpunkte. (~7–8 h)
- [ ] **P-B4 · Gegner laufen** — ein Gegnertyp, host-gesteuert:
  Wegfolge, Gabelung abwechselnd, gerade Linie am Wegende,
  Leben-Abzug am Endpunkt. Danach der Prüfpunkt. (~10 h)
- [ ] **P-B5 · Takt + Senden** — Timer mit Bereit-Knopf, Sende-Gebäude
  mit Warteschlange, Sends laufen mit dem Wellenstart, fester
  Sende-Ring. (~5–6 h)
- [ ] **P-B6 · Ressourcen** — Gold, Diamanten, Kacheln als Werte;
  Einkommen bei Timer null; Preise verdrahtet; Minimal-HUD. (~3–4 h)
- [ ] **P-B7 · Erster Wächter** — Pfeilturm: über die Figur
  platzieren, Ziel in Reichweite, schießen, Monster sterben, Gold
  fließt — der Spaß-Test der Abgabe. (~8–10 h)
- [ ] **P-B8 · Mine + Arbeiter** — Streichkandidat, faktisch
  Alpha-Material; Notlösung ist ein Kachel-Kauf-Knopf. (~7–8 h)
- [ ] **P3 · Polish-Merkliste** — gesammelt beim Bauen, fällig
  frühestens mit den Messrunden: Menü-Branding tauschen (trägt noch
  das Isor's-Tower-Logo aus der Übernahme-Kette); Wand-Klick-Filter
  (der Klick-Strahl ignoriert Wände und trifft den Boden dahinter);
  Tick-Rate und Interpolation messen (Latenz,
  `Knowledge/Unity/netzwerk-latenz-anatomie.md`); Settings-Anbindung
  der Schalter (Edge-Pan, Freiflug-Grenze, Kamera-Dauerfolgen als
  Option).
