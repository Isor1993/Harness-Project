# PLAN.md — Arbeitsplan

Ownership: Was in den nächsten ein bis drei Wochen dran ist,
schichtübergreifend — und der Auftrag an die nächste Session. Was
irgendwann kommt, steht in der ROADMAP der jeweiligen Schicht; was
passiert ist, im LOG.
Format: `### <Zeitraum oder Baustein>` mit Aufzählungspunkten, je Punkt
ein Satz. Erledigtes wird abgehakt, nicht gelöscht. Der Abschnitt „Für
die nächste Session" steht oben und hat sein eigenes Format.

**Höchstens ~100 Zeilen.** Ist ein Zeitraum durch, wandert er als
Ereignis ins LOG, erledigte Punkte werden in der ROADMAP abgehakt, und
diese Datei wird **geleert** — nicht archiviert. Die Geschichte steht
im LOG.

---

## Für die nächste Session

Steht **oben**, weil es das Erste ist, was zählt. Wird bei jedem
`/harness:ende` **überschrieben**, nie ergänzt — „gerade nichts offen"
ist ein gültiger Inhalt. Höchstens fünf Zeilen; Ausführliches steht in
der Datei, auf die hier verwiesen wird.

*(überschrieben 2026-11-14 beim `/harness:ende` der Session „P-B6
Ressourcen". P-B5v, P-B6, P-B6a und P-B6b sind fertig und abgehakt —
die Wirtschaft läuft vom Tropf bis zur gelegten Kachel, samt
Weg-Wächter und Rollback; die Delegates-Runde lief am echten System.
Wochen-Soll bis So 15.11. damit erfüllt bis auf den P-B7-Start.)*

**P-B7-Design-Runde, dann bauen — dazwischen der Code-Durchgang:**
1. **Design-Runde P-B7** (braucht Isor frisch): Panel-Form am
   Wächter-Platz, Preisaufteilung Platz/Wahl, Kopfgeld je Monstertyp,
   Turmpreise, `CellContent.Tower` — die offenen Punkte stehen am
   ROADMAP-Eintrag P-B7.
2. **Code-Durchgang** der am 14.11. Claude-getippten Teile
   (ResourceHudUI, P-B6a, P-B6b) Stück für Stück, sobald Isor fit
   ist — vereinbart 2026-11-14, Lernlog.
3. Danach **P-B7 bauen** (~8–10 h) — Feature-Stopp-Linie 18.–20.11.
   im Blick; P-B8 behält sein Streichrecht, der Tropf trägt solange.

---

### Die Testphase läuft — seit 2026-08-27

Sie hat auf Isors Zuruf begonnen, wie es seit dem 2026-08-23 vorgesehen
war (`Kern/DECISIONS.md`). Ab jetzt gilt: **Der Harness wird benutzt,
nicht gebaut.** Claude schlägt von sich aus keine Umbauten mehr vor.

Was im Betrieb nicht trägt, wird als Störung notiert
(`Kern/STOERUNGEN.md`) und über die Doku-Pflicht zu einem ROADMAP-Punkt —
nicht sofort behoben. Ein Befund ist ein Zustand, kein Auftrag.

- [x] **Phase 0 · Netz-Prüfstand** — **erledigt am 2026-08-28**, in fünf
      Tagen statt zwei Wochen. Der Vergleichstest ist bestanden (AMD gegen
      Intel, identische Prüfsummen), die Zeitrechnung des Semesters bleibt
      also wie geplant. Zusätzlich belegt: Relay trägt über zwei Netze,
      getestet bis auf die Philippinen.
- [ ] **Der Datenbaum wartet** (`IsorBackup/ROADMAP.md`, vier Punkte).
      **Kein Termin** — bewusst hinter Phase 0 gestellt, weil nur der
      Prototyp einen Semestertermin hat (Isor, 2026-08-27). Er bleibt
      die geplante Belastungsprobe des Harness im Betrieb.
- [x] **Abgabe-Struktur anlegen**, sobald die Semester-Aufgaben da sind
      (`Uni/ROADMAP.md`) — der Punkt, an dem im zweiten Semester Zeit
      verloren ging. Die Aufgaben sind seit dem 2026-09-07 bestätigt.
      **Erledigt am 2026-09-08** — Beleg: `Uni/ROADMAP.md` →
      „Abgabe-Struktur beim Semesterstart kopieren".

