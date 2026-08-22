# GDD_RULES.md — Regeln für das Game Design Document

Ownership: Aufbau und Pflege eines GDD — was hineingehört, wie mit
offenen Punkten umgegangen wird, wann aus einem Entwurf feste Absicht
wird, in welchem Takt es nachgezogen wird. Das GDD **selbst** liegt beim
Projekt (`Projekte/<Name>/GDD.md`), nicht hier. Gleiche Trennung wie
ARTIFACT_RULES gegenüber ARTIFACT_INDEX.

## Was ein GDD beantwortet

**Was das Spiel sein soll — nicht, wie es gebaut wird.**

| Frage | gehört ins | nicht ins |
|---|---|---|
| Was soll sich für den Spieler anfühlen? | GDD | |
| Warum diese Lösung und nicht jene? | | DECISIONS |
| Wie ist es technisch umgesetzt? | | TDD, TDD_NOTES |
| Wann wird es gebaut? | | ROADMAP, PLAN |
| Wann wurde es gebaut? | | LOG |

Ein GDD, das technische Umsetzung beschreibt, wird bei jeder Umbaumaßnahme
falsch. Ein GDD, das nur die Absicht beschreibt, überlebt sie.

## Aufbau

Feste Reihenfolge, damit zwei Fassungen vergleichbar bleiben:

1. **Pitch** — zwei bis drei Sätze, worum es geht
2. **Kern-Schleife** — was der Spieler immer wieder tut
3. **Welt-Struktur** — wie die Bereiche zueinander stehen
4. **Spieler** — Perspektive, Fortschritt, Größenordnungen
5. **Persistenz** — was gespeichert wird und was nicht
6. Weitere Kapitel nach Bedarf
7. **Offene Design-Fragen** — nummeriert, siehe unten
8. **Entwurf** — noch nicht Einsortiertes, siehe unten

## Der `offen`-Mechanismus

`offen` ist ein **gültiger Eintrag**, kein Mangel. Er markiert die
Stellen, an denen die Architektur eine Tür offenhalten muss — wer sie
verschweigt, baut die Tür zu.

- Ein offener Punkt steht **im Kapitel**, zu dem er gehört, fett als
  `**Offen:**` — und zusätzlich als Zeile im Abschnitt „Offene
  Design-Fragen".
- **Das GDD ist der Besitzer offener Design-Fragen.** Die ROADMAP darf
  sie als Aufgabe aufnehmen, aber nur über einen Verweis
  (Pfad + Überschrift), nie durch Abschreiben.
- **Geschlossen wird so:** Die Entscheidung wandert nach DECISIONS (was,
  warum, verworfene Alternativen). Danach — und erst danach — streicht
  das GDD die Frage und schreibt die Absicht als feste Aussage ins
  Kapitel. Vorher stünde dieselbe Frage an zwei Orten.

## Der Abschnitt „Entwurf"

Ergebnisse aus Brainstorm-/Design-Sessions landen **sofort** hier, roh
und unsortiert. Grund: Ohne diesen Ort gibt es zwischen „gedacht" und
„einsortiert" keine Ablage — und was keine Ablage hat, geht verloren.

- Der Entwurf ist ausdrücklich **noch keine Absicht.** Er bindet nichts.
- Er wird eingeordnet, wenn das zugehörige Kapitel das nächste Mal
  angefasst wird — nicht in einem eigenen Durchgang.
- **Aus Entwurf wird feste Absicht**, sobald Isor sie bestätigt und sie
  in ihr Kapitel wandert. Bis dahin darf sich Claude nicht darauf
  berufen, als wäre sie entschieden.
- Ein Entwurfseintrag trägt sein Datum. Steht er nach drei Monaten noch
  da, ist er entweder Absicht oder überholt — beides wird dann geklärt.

## Takt

Das GDD ist ein **Living Document** und wird an der **Baustein-Grenze**
nachgezogen, nicht nach Kalender: Ein Baustein gilt erst als fertig, wenn
sein Abschnitt geschrieben ist (siehe WORKFLOW.md).

Grund gegen einen Wochenrhythmus: Der Inhalt ändert sich an
Feature-Grenzen, nicht sonntags. Wer über ein halbfertiges System
schreibt, schreibt es zweimal.

## Das GDD als Abgabetext

`Projekte/<Name>/GDD.md` ist zugleich das **Markdown-Manuskript** der
Abgabefassung — es gibt kein zweites Dokument daneben. Die `.docx`
entsteht daraus und ist keine eigene Quelle; ihre Behandlung regelt
DOCX_RULES.

Folge für den Schreibstil: Das GDD wird so geschrieben, dass es ohne
Umbau als Abgabetext taugt — ganze Sätze, keine Stichwortlisten dort, wo
Fließtext erwartet wird.

## Abgrenzung in einem Satz

> Das GDD sagt, **was gelten soll**. DECISIONS sagt, **warum es so
> entschieden wurde**. Das TDD sagt, **wie es gebaut ist**. Die ROADMAP
> sagt, **wann es drankommt**.
