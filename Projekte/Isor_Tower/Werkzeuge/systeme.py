# -*- coding: utf-8 -*-
"""Erzeugt SYSTEME.md aus den Script-Ordnern des Unity-Projekts.

Arbeitsteilung (Kern/DOC_RULES.md, Abschnitt 5):
  Das Skript besitzt die *Liste* — welche System-Ordner es unter
  `Assets/Scripts/` gibt (plus `Assets/Editor/`), wie viele Skripte
  jeder trägt und wann zuletzt einer geändert wurde. Isor besitzt die
  *Beschreibung*; sie wird über den Ordnernamen aus der alten Fassung
  übernommen.

  Neue Ordner erscheinen als `⚠ fehlt`, verschwundene als
  `⚠ nicht mehr vorhanden` — nichts wird stillschweigend entfernt.

Den Projektpfad liest das Skript aus `Kern/PFADE.md`, Marke `PROJEKT` —
kein harter Pfad im Skript, beim Umzug ändert sich eine Zeile
(Entscheidung in Kern/DECISIONS.md, 2026-08-25).

Die letzte Änderung kommt aus dem Dateisystem (LastWriteTime), nicht aus
git — im Ein-Rechner-Betrieb identisch, nach einem frischen Clone nicht.

Aufruf:
    python systeme.py            Probelauf
    python systeme.py --write    schreibt SYSTEME.md
"""
import datetime
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
ZIEL = os.path.join(os.path.dirname(HIER), "SYSTEME.md")
PFADE = os.path.normpath(os.path.join(HIER, "..", "..", "..", "Kern", "PFADE.md"))

KOPF = u"""# SYSTEME.md — Was gerade im Projekt steckt

Ownership: Nur die erzeugte Systemliste — welche System-Ordner es unter
`Assets/Scripts/` gibt (plus `Assets/Editor/`), wie viele Skripte jeder
trägt und wozu er da ist. Keine Aufgaben (die ROADMAP der Schicht),
keine Ereignisse (das LOG), keine Begründungen (die DECISIONS).

**Diese Datei wird erzeugt** — die Liste kommt aus dem Projekt, die
Beschreibung je System kommt von Hand und wird bei jedem Lauf
übernommen. Erzeugt mit `Werkzeuge/systeme.py`; den Projektpfad nennt
`Kern/PFADE.md` → `PROJEKT`.

| System | Skripte | Letzte Änderung | Beschreibung |
|---|---|---|---|
"""


def projekt_pfad():
    """Liest die PROJEKT-Marke aus Kern/PFADE.md."""
    if not os.path.exists(PFADE):
        sys.exit("Abbruch: %s nicht gefunden." % PFADE)
    with io.open(PFADE, encoding="utf-8") as fh:
        for z in fh:
            m = re.match(r"^\|\s*`PROJEKT`\s*\|\s*`([^`]+)`", z)
            if m:
                pfad = m.group(1)
                if not os.path.isdir(pfad):
                    sys.exit("Abbruch: PROJEKT-Pfad existiert nicht: %s" % pfad)
                return pfad
    sys.exit("Abbruch: Marke PROJEKT in Kern/PFADE.md nicht gefunden "
             "oder nicht eingerichtet.")


def alte_eintraege():
    """name -> beschreibung aus der bestehenden Datei."""
    if not os.path.exists(ZIEL):
        return {}
    alt = {}
    with io.open(ZIEL, encoding="utf-8") as fh:
        for z in fh:
            m = re.match(r"^\|\s*([^|]+?)\s*\|\s*[^|]*\|\s*[^|]*\|\s*(.*?)\s*\|\s*$", z)
            if not m:
                continue
            name = m.group(1)
            if name in ("System", "---"):
                continue
            if name in alt:
                print("  ! doppelter Schluessel, Beschreibung wuerde "
                      "verloren gehen:", repr(name))
            alt[name] = m.group(2)
    return alt


def vermessen(ordner):
    """(anzahl .cs, juengstes Aenderungsdatum als Text) — rekursiv."""
    anzahl = 0
    juengste = 0
    for wurzel, _, dateien in os.walk(ordner):
        for d in dateien:
            if not d.endswith(".cs"):
                continue
            anzahl += 1
            t = os.path.getmtime(os.path.join(wurzel, d))
            if t > juengste:
                juengste = t
    if anzahl == 0:
        return 0, u"—"
    datum = datetime.date.fromtimestamp(juengste).isoformat()
    return anzahl, datum


def gefundene(projekt):
    """name -> (anzahl, datum) fuer jeden System-Ordner plus Editor."""
    scripts = os.path.join(projekt, "Assets", "Scripts")
    if not os.path.isdir(scripts):
        sys.exit("Abbruch: %s nicht gefunden — falsches Projekt?" % scripts)

    systeme = {}
    for name in sorted(os.listdir(scripts)):
        voll = os.path.join(scripts, name)
        if os.path.isdir(voll):
            systeme[name] = vermessen(voll)

    lose = [d for d in os.listdir(scripts)
            if d.endswith(".cs") and os.path.isfile(os.path.join(scripts, d))]
    if lose:
        print("  ! liegen lose in Assets/Scripts statt in einem "
              "System-Ordner:", ", ".join(lose))

    editor = os.path.join(projekt, "Assets", "Editor")
    if os.path.isdir(editor):
        if "Editor" in systeme:
            print("  ! Schluessel-Kollision: Scripts/Editor und "
                  "Assets/Editor fielen zusammen — Assets/Editor gewinnt.")
        systeme["Editor"] = vermessen(editor)
    return systeme


def main():
    projekt = projekt_pfad()
    alt = alte_eintraege()
    neu = gefundene(projekt)

    verschwunden = [n for n in alt if n not in neu]
    dazu = [n for n in neu if n not in alt]
    skripte = sum(a for a, _ in neu.values())

    print("System-Ordner im Projekt: %d, Skripte gesamt: %d"
          % (len(neu), skripte))
    print("Eintraege in der alten Fassung: %d" % len(alt))
    if dazu:
        print("NEU (Beschreibung fehlt noch):")
        for n in dazu:
            print("   +", n)
    if verschwunden:
        print("NICHT MEHR VORHANDEN (bleiben mit Warnung stehen):")
        for n in verschwunden:
            print("   -", n)
    if not dazu and not verschwunden:
        print("Keine Abweichung zur alten Fassung.")

    zeilen = [KOPF]
    for name in sorted(neu):
        anzahl, datum = neu[name]
        beschreibung = alt.get(name, u"⚠ fehlt")
        zeilen.append(u"| %s | %d | %s | %s |\n"
                      % (name, anzahl, datum, beschreibung))

    if verschwunden:
        zeilen.append(u"\n## Nicht mehr im Projekt\n\n")
        zeilen.append(u"Beschreibungen zu Ordnern, die es nicht mehr gibt — sie werden\n"
                      u"nicht stillschweigend entfernt, weil sie noch etwas erklären können.\n\n")
        zeilen.append(u"| System | Beschreibung |\n|---|---|\n")
        for name in sorted(verschwunden):
            zeilen.append(u"| %s ⚠ nicht mehr vorhanden | %s |\n"
                          % (name, alt[name]))

    if "--write" in sys.argv:
        with io.open(ZIEL, "w", encoding="utf-8") as fh:
            fh.write("".join(zeilen).rstrip("\n") + "\n")
        print("geschrieben:", ZIEL)
    else:
        print("\n(Probelauf. Mit --write wird geschrieben.)")


if __name__ == "__main__":
    main()
