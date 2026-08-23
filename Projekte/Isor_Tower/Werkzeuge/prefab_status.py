# -*- coding: utf-8 -*-
"""Erzeugt PREFAB_STATUS.md aus den tatsächlich vorhandenen .prefab-Dateien.

Arbeitsteilung (Kern/DOC_RULES.md, Abschnitt 5):
  Das Skript besitzt die *Liste* — welche Prefabs es gibt und wie sie
  gruppiert sind. Isor besitzt *Status* und *Befund*; beide werden über
  den Prefab-Namen aus der alten Fassung übernommen.

  Neu aufgetauchte Prefabs erscheinen als `offen`, verschwundene als
  `⚠ nicht mehr vorhanden` — sie werden nicht stillschweigend entfernt,
  weil ein Befund zu einem gelöschten Prefab noch etwas erklären kann.

  Endet ein Prefabname auf ein Leerzeichen (`Torch .prefab`), wird es in
  der Tabelle als `␣` geschrieben. Sonst sind zwei Zeilen optisch
  identisch, und beim Rücklesen fällt die eine auf die andere: Am
  2026-08-22 wären so 34 Prefabs zu 33 Einträgen geworden und ein von
  Hand geschriebener Befund verloren gegangen (Befund A32 der Abnahme).

Aufruf:
    python prefab_status.py            Probelauf
    python prefab_status.py --write    schreibt PREFAB_STATUS.md
"""
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
ZIEL = os.path.join(os.path.dirname(HIER), "PREFAB_STATUS.md")
ASSETS = r"C:\Repos Isor\Isor-Tower-ProtoTyp-2026\Assets"

SICHTBAR = u"␣"   # ␣ — Leerzeichen am Namensrand, sonst unsichtbar

KOPF = u"""# PREFAB_STATUS.md — Prüfstand der Prefabs

Ownership: Nur der Prüfstand jedes Prefabs — welche schon durchgesehen
sind und was dabei auffiel. **Keine Aufgabenplanung** (das ist
`Projekte/Isor_Tower/ROADMAP.md` → „Prefab-Struktur prüfen und
aufräumen"), **keine Begründungen** (`Projekte/Isor_Tower/DECISIONS/`),
**kein Fertiges** (`Projekte/Isor_Tower/LOG.md`).

**Diese Datei wird erzeugt** — die Liste kommt aus dem Projekt, Status
und Befund kommen von Hand und werden bei jedem Lauf übernommen.
Erzeugt mit `Werkzeuge/prefab_status.py`.

Zweck: Beim Aufräumen soll kein Prefab zweimal angefasst werden. Ist
jedes `geprüft`, wandern offene Befunde als Aufgaben in die ROADMAP und
diese Datei ins Archiv — sie ist eine Arbeitsliste mit Ende.

Status-Werte:
- `offen` — noch nicht angesehen
- `berührt` — inhaltlich geändert, Struktur aber nicht geprüft
- `geprüft` — Aufbau und Ablage angesehen, Befund notiert, nichts offen
- `Befund` — angesehen, etwas stimmt nicht (steht in der Spalte)

Ein `␣` im Namen steht für ein Leerzeichen am Rand des Dateinamens —
`Torch␣` ist die Datei `Torch .prefab`, nicht `Torch.prefab`.

"""


def anzeigen(name):
    """Leerzeichen am Rand sichtbar machen — innere bleiben, wie sie sind."""
    gezeigt = name
    if gezeigt.startswith(" "):
        gezeigt = SICHTBAR + gezeigt.lstrip(" ")
    if gezeigt.endswith(" "):
        gezeigt = gezeigt.rstrip(" ") + SICHTBAR
    return gezeigt


def alte_eintraege():
    """name -> (status, befund) aus der bestehenden Datei."""
    if not os.path.exists(ZIEL):
        return {}
    alt = {}
    with io.open(ZIEL, encoding="utf-8") as fh:
        for z in fh:
            m = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(.*?)\s*\|\s*$", z)
            if not m:
                continue
            name = m.group(1)
            if name in ("Prefab", "---"):
                continue
            if name in alt:
                # Darf nicht vorkommen: Ein Schluessel steht fuer genau ein
                # Prefab. Frueher fielen `Torch` und `Torch ` hier zusammen.
                print("  ! doppelter Schluessel, Befund wuerde verloren gehen:",
                      repr(name))
            alt[name] = (m.group(2), m.group(3))
    return alt


def gefundene():
    """(gruppe, name) fuer jede .prefab-Datei, ohne TextMeshPro."""
    treffer = []
    for wurzel, ordner, dateien in os.walk(ASSETS):
        if "TextMesh" in wurzel:
            continue
        for d in dateien:
            if not d.endswith(".prefab"):
                continue
            rel = os.path.relpath(os.path.join(wurzel, d), ASSETS)
            gruppe = os.path.dirname(rel).replace("\\", "/")
            treffer.append((gruppe, d[:-len(".prefab")]))
    return sorted(treffer)


def main():
    alt = alte_eintraege()
    neu = gefundene()
    namen_neu = set(anzeigen(n) for _, n in neu)

    gruppen = {}
    for gruppe, name in neu:
        gruppen.setdefault(gruppe, []).append(name)

    verschwunden = [n for n in alt if n not in namen_neu]
    dazu = [anzeigen(n) for _, n in neu if anzeigen(n) not in alt]

    print("Prefabs im Projekt: %d in %d Gruppen" % (len(neu), len(gruppen)))
    print("Eintraege in der alten Fassung: %d" % len(alt))
    if dazu:
        print("NEU (erscheinen als offen):")
        for n in dazu:
            print("   +", n)
    if verschwunden:
        print("NICHT MEHR VORHANDEN (bleiben mit Warnung stehen):")
        for n in verschwunden:
            print("   -", n)
    if not dazu and not verschwunden:
        print("Keine Abweichung zur alten Fassung.")

    zeilen = [KOPF]
    for gruppe in sorted(gruppen):
        zeilen.append(u"## %s\n\n" % gruppe)
        zeilen.append(u"| Prefab | Status | Befund |\n|---|---|---|\n")
        for name in sorted(gruppen[gruppe]):
            gezeigt = anzeigen(name)
            status, befund = alt.get(gezeigt, (u"offen", u""))
            zeilen.append(u"| %s | %s | %s |\n" % (gezeigt, status, befund))
        zeilen.append(u"\n")

    if verschwunden:
        zeilen.append(u"## Nicht mehr im Projekt\n\n")
        zeilen.append(u"Befunde zu Prefabs, die es nicht mehr gibt — sie werden nicht\n"
                      u"stillschweigend entfernt, weil ein Befund noch etwas erklären kann.\n\n")
        zeilen.append(u"| Prefab | Status | Befund |\n|---|---|---|\n")
        for name in sorted(verschwunden):
            status, befund = alt[name]
            zeilen.append(u"| %s | ⚠ nicht mehr vorhanden | %s |\n" % (name, befund))
        zeilen.append(u"\n")

    if "--write" in sys.argv:
        with io.open(ZIEL, "w", encoding="utf-8") as fh:
            fh.write("".join(zeilen).rstrip("\n") + "\n")
        print("geschrieben:", ZIEL)
    else:
        print("\n(Probelauf. Mit --write wird geschrieben.)")


if __name__ == "__main__":
    main()
