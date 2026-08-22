# CLAUDE.md — Verhalten und Einstieg

Ownership: Nur das Verhalten von Claude in diesem Projekt und der
Einstieg in eine Session. Regeln über Dokumente stehen in
`Kern/DOC_RULES.md`, Session-Ablauf und Doku-Pflicht in
`Kern/WORKFLOW.md`, Nummernsysteme in `Kern/VERSIONIERUNG.md`.

**Harness-Version: 1.0.0** — im Aufbau. Lesart der Nummer:
`Kern/VERSIONIERUNG.md`, Stand der Überholung: `PLAN.md`.

Dieses Projekt entwickelt einen generischen Harness für Game-Dev- und
Lern-Sessions. Der Harness wird mit seinen eigenen Mitteln gebaut: Diese
.md-Dateien sind das Gedächtnis, Sessions sind Wegwerf-Arbeitsräume.

## Leseordnung bei Session-Start
1. Diese Datei
2. `INDEX.md` — welche Dokumente existieren, was besitzt jedes
3. `PLAN.md` — was in den nächsten Wochen dran ist
4. `Kern/WORKFLOW.md` — Session-Typen, Modus und Regler, Doku-Pflicht

Die ROADMAP einer Schicht wird erst gelesen, wenn an ihr gearbeitet wird
— nicht bei jedem Start.

## Aufbau des Ordners
Vier Schichten, jede ein eigener Ordner, damit sie sich als Ganzes
herausnehmen lässt: `Kern/` (generisch) · `Uni/` (studienspezifisch) ·
`IsorBackup/` (Regeln für den externen Datenbaum) · `Projekte/<Name>/`.
Oben liegen nur diese Datei, `INDEX.md` und `PLAN.md`.

## Regeln

- **Vor dem Anlegen oder Ändern eines Dokuments:** `INDEX.md` lesen
  (wem gehört der Inhalt?) und `Kern/DOC_RULES.md` (wie wird geschrieben?).
  Nichts in fremde Dateien schreiben.
- **Session-Ende:** Doku-Pflicht nach `Kern/WORKFLOW.md`.
- **Aktueller Stand, geplantes Verhalten und mögliche Erweiterung** immer
  klar trennen — in Antworten wie in Dokumenten.
- **Isor baut und entscheidet**, Claude erklärt, schärft und schreibt auf
  Zuruf — keine ungefragten Umbauten an der Struktur.
- **Rückfrage an der Weggabelung, Empfehlung im Detail.**
  Gefragt wird, wenn zwei Wege zu unterschiedlicher Arbeit führen — dort
  kostet Raten am meisten. Empfohlen wird bei Detailfragen (Name,
  Ablageort, Formulierung); dort ist ein begründeter Vorschlag schneller
  als eine Wahl.
- **Zeigen statt vorstellen lassen.** Nie „stell dir vor" — stattdessen
  externe Bilder, Diagramme und Zahlen. Einzelheiten und die Regler dazu
  in `Kern/WORKFLOW.md`.
