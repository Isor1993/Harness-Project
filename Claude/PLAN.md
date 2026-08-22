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
- [x] **Phase 3 — Umzüge**, alle fünf durch und jeder einzeln geprüft:
      ASSESSMENT_LOG → 2 Zeugnisdateien · FEATURE_LOG → 3 Chroniken ·
      ROADMAP → 3 ROADMAPs + 2 Archive (708 → 204 Zeilen Planung) ·
      TDD_NOTES → 10 Themenblöcke · DECISIONS → 9 Dateien + Archiv
- [x] **Phase 4 — Einzeldateien nachgezogen.** WORKFLOW neu gefasst ·
      KNOWLEDGE_RULES, ARTIFACT_RULES, ARTIFACT_INDEX, DIAGRAM_RULES,
      DOCX_RULES, ASSESSMENT_RULES, CODE_GUIDELINES, GDD, PREFAB_STATUS
      nachgezogen · XML-Fallen ins Knowledge ausgelagert · sieben
      READMEs im Knowledge-Repo · alle toten Verweise repariert
- [x] **Phase 5 — Skripte gebaut** und in der Schicht abgelegt, deren
      Dateien sie bearbeiten: `Kern/Werkzeuge/index_bauen.py` ·
      `Projekte/Isor_Tower/Werkzeuge/prefab_status.py` ·
      `IsorBackup/Werkzeuge/sichern.ps1`. Alle drei mit Probelauf als
      Voreinstellung; INDEX und PREFAB_STATUS werden ab jetzt erzeugt.
- [x] **Phase 6 — Befehle:** `/sichern`, `/wechsel`, `/ende` und als
      vierter `/sonntag` gebaut — Ablauf in `Kern/WORKFLOW.md`, die
      Dateien unter `.claude\commands\` sind nur Auslöser.
      Berechtigungen 314 → 51 Allow + 8 Ask + 4 Deny. P1 gemessen:
      nur die oberste `CLAUDE.md` lädt von selbst.
- [x] **Phase 7 — Nachlauf:** IsorBackup-Schicht gebaut (RULES, ROADMAP,
      DECISIONS), `C:\IsorBackup\README.md` auf einen Wegweiser gekürzt,
      `Kern/GLOSSARY.md` mit 26 Begriffen eingesammelt. Drei Punkte in
      ihre Schicht umgesetzt, eine verlorengehende Diagramm-Regel
      gerettet. Das Archivieren der Review-Dateien wandert ans Ende von
      Phase 8 — bis dahin wird die Befundliste gebraucht.
- [ ] **Phase 8 — Abnahme:** Schlussdurchgang über alle Dateien,
      Haken gegenprüfen, Empfehlungen einholen, Artifact-Seite
      `⚙️ System · Harness` bauen, dann Auslieferung `Harness_1.0.0`

### Danach

- [ ] **Testphase beginnt.** Erste Aufgabe: `C:\IsorBackup` aufräumen,
      in Viererpaketen. Zugleich die erste Belastungsprobe des neuen
      Harness — Störungen kommen in `Kern/STOERUNGEN.md`.
- [ ] Danach zurück ins Projekt Isor's Tower, Harness im laufenden
      Betrieb erproben.
- [ ] Semesterbeginn in rund zwei Wochen (Stand 2026-08-22).
