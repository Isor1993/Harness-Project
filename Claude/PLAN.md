# PLAN.md — Arbeitsplan

Ownership: Nur was in den nächsten ein bis drei Wochen dran ist,
schichtübergreifend. Was irgendwann kommt, steht in der ROADMAP der
jeweiligen Schicht; was passiert ist, im LOG.
Format: `### <Zeitraum oder Baustein>` mit Aufzählungspunkten, je Punkt
ein Satz. Erledigtes wird abgehakt, nicht gelöscht.

**Höchstens ~100 Zeilen.** Ist ein Zeitraum durch, wandert er als
Ereignis ins LOG, erledigte Punkte werden in der ROADMAP abgehakt, und
diese Datei wird **geleert** — nicht archiviert. Die Geschichte steht
im LOG.

---

### Laufend: Harness-Überholung auf Version 1.0.0

Entwurf vollständig (25 Dateien, 86 Entscheidungen) — Befunde in
`_HARNESS_REVIEW.md`, Handgriffe in `_HARNESS_UMSETZUNG.md`.
Reihenfolge: Regeln → Struktur → Inhalt → Automatik.

- [x] **Phase 1 — Regeln:** DOC_RULES, GDD_RULES, VERSIONIERUNG gebaut
      und durchgesprochen
- [x] **Phase 2 — Struktur:** Schicht-Ordner angelegt, PLAN.md und
      Kern/STOERUNGEN.md gebaut, 17 Dateien in ihre Schicht verschoben,
      INDEX nach Schichten neu geschrieben, `_split_check.txt` archiviert
- [ ] **Phase 3 — Umzüge**, kleinste zuerst: ASSESSMENT_LOG (2) →
      FEATURE_LOG (73) → ROADMAP (546 Zeilen Vergangenheit) →
      TDD_NOTES (85) → DECISIONS (133). Commit nach jedem Schritt.
- [ ] **Phase 4 — Einzeldateien nachziehen** (14 Stück)
- [ ] **Phase 5 — Skripte:** INDEX, PREFAB_STATUS, Backup
- [ ] **Phase 6 — Befehle:** `/sichern`, `/wechsel`, `/ende`;
      Berechtigungen eindampfen
- [ ] **Phase 7 — Nachlauf:** IsorBackup-Dateien, Glossar einsammeln,
      Auslieferung `Harness_1.0.0`

### Danach

- [ ] **Testphase beginnt.** Erste Aufgabe: `C:\IsorBackup` aufräumen,
      in Viererpaketen. Zugleich die erste Belastungsprobe des neuen
      Harness — Störungen kommen in `Kern/STOERUNGEN.md`.
- [ ] Danach zurück ins Projekt Isor's Tower, Harness im laufenden
      Betrieb erproben.
- [ ] Semesterbeginn in rund zwei Wochen (Stand 2026-08-22).
