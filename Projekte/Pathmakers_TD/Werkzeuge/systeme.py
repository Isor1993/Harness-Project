# -*- coding: utf-8 -*-
"""Erzeugt SYSTEME.md aus dem Unity-Projekt von Pathmakers TD.

Angepasste Kopie von Projekte/Isor_Tower/Werkzeuge/systeme.py
(2026-11-04), erweitert um zwei Abschnitte aus dem Ordnungssystem-
Beschluss (Kern/DECISIONS.md, 2026-11-04):
  * die oberste Assets-Ebene (Gewerk-Modell sichtbar machen) und
  * die Wurzel-Objekte jeder Szene (Zonen sichtbar machen) —
    .unity-Dateien sind Text, die Wurzeln werden direkt gelesen.

Arbeitsteilung (Kern/DOC_RULES.md, Abschnitt 5):
  Das Skript besitzt die *Listen* — System-Ordner, Skriptzahlen,
  Assets-Ebene, Szenen-Wurzeln. Isor besitzt die *Beschreibung* je
  System; sie wird über den Ordnernamen aus der alten Fassung
  übernommen. Neue Ordner erscheinen als `⚠ fehlt`, verschwundene als
  `⚠ nicht mehr vorhanden` — nichts wird stillschweigend entfernt.

Den Projektpfad liest das Skript aus `Kern/PFADE.md`, Marke
`PROJEKT_PATHMAKERS`; das Unity-Projekt liegt darunter im Ordner
`PathmakersTD`.

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
UNITY_UNTERORDNER = "PathmakersTD"

KOPF = u"""# SYSTEME.md — Was gerade im Projekt steckt

Ownership: Nur die erzeugten Listen — System-Ordner unter
`Assets/Scripts/` (plus `Assets/Editor/`), die oberste Assets-Ebene
und die Wurzel-Objekte jeder Szene. Keine Aufgaben (ROADMAP), keine
Ereignisse (LOG), keine Begründungen (DECISIONS).

**Diese Datei wird erzeugt** — die Listen kommen aus dem Projekt, die
Beschreibung je System kommt von Hand und wird bei jedem Lauf
übernommen. Erzeugt mit `Werkzeuge/systeme.py`; den Projektpfad nennt
`Kern/PFADE.md` → `PROJEKT_PATHMAKERS`.

## Spickzettel — die Ordnungs-Regeln

Kurzform; die Regeln besitzt `Kern/CODE_GUIDELINES.md`.

1. **Ordner:** Gewerk oben (`Art/`, `Audio/`, `Scripts/` …), Typ
   darunter, je ein Ordner pro System. Scripts sortieren nach der
   System-Frage (*welches Spielsystem?*), Canvas-Zeug nach Schicht
   (`UI/` Menü, `HUD/` ingame).
2. **Namen:** erst was, dann wie — `Präfix_Name_Variante` (T_, M_,
   SM_, P_, SO_, TL_, Brush_, Music_, SFX_). Englisch, PascalCase,
   nie Leerzeichen.
3. **Szene:** Zonen in Strich-Optik — `--- SYSTEM ---` (Etikett, lose
   Dienste), `--- World ---` und `--- UI ---` (echte Parents auf
   0/0/0, nie bewegen). Prüfsatz: *beschreibt die Position die Welt,
   oder ist sie egal?*
"""

SCRIPTS_TABELLE_KOPF = u"""
## Scripts — die Systeme

| System | Skripte | Letzte Änderung | Beschreibung |
|---|---|---|---|
"""


def projekt_pfad():
    """Liest die PROJEKT_PATHMAKERS-Marke aus Kern/PFADE.md."""
    if not os.path.exists(PFADE):
        sys.exit("Abbruch: %s nicht gefunden." % PFADE)
    with io.open(PFADE, encoding="utf-8") as fh:
        for z in fh:
            m = re.match(r"^\|\s*`PROJEKT_PATHMAKERS`\s*\|\s*`([^`]+)`", z)
            if m:
                pfad = os.path.join(m.group(1), UNITY_UNTERORDNER)
                if not os.path.isdir(pfad):
                    sys.exit("Abbruch: Unity-Projekt nicht gefunden: %s" % pfad)
                return pfad
    sys.exit("Abbruch: Marke PROJEKT_PATHMAKERS in Kern/PFADE.md "
             "nicht gefunden.")


def alte_eintraege():
    """name -> beschreibung aus der bestehenden Scripts-Tabelle."""
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


def gefundene_systeme(projekt):
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


def assets_ebene(projekt):
    """[(ordnername, dateizahl ohne .meta)] der obersten Assets-Ebene."""
    assets = os.path.join(projekt, "Assets")
    ebene = []
    for name in sorted(os.listdir(assets)):
        voll = os.path.join(assets, name)
        if not os.path.isdir(voll):
            continue
        anzahl = 0
        for wurzel, _, dateien in os.walk(voll):
            anzahl += sum(1 for d in dateien if not d.endswith(".meta"))
        ebene.append((name, anzahl))
    return ebene


def szenen_wurzeln(projekt):
    """szenenname -> [(wurzelname, kinderzahl)] in Hierarchie-Reihenfolge.

    Liest die .unity-Datei als Text: GameObjects (!u!1) liefern Namen,
    Transforms (!u!4/224) Eltern und Kinder, PrefabInstances (!u!1001)
    ihre Namens-Uebersteuerung. Die Reihenfolge kommt aus dem
    SceneRoots-Block; was er nicht nennt, haengt in Dateireihenfolge an.
    Gestrippte Bloecke (Prefab-Innereien) werden uebersprungen.
    """
    szenen_ordner = os.path.join(projekt, "Assets", "Scenes")
    ergebnis = {}
    for datei in sorted(os.listdir(szenen_ordner)):
        if not datei.endswith(".unity"):
            continue
        pfad = os.path.join(szenen_ordner, datei)
        bloecke = []
        aktueller = None
        with io.open(pfad, encoding="utf-8", errors="replace") as fh:
            for zeile in fh:
                m = re.match(r"--- !u!(\d+) &(\d+)( stripped)?", zeile)
                if m:
                    aktueller = {"klasse": int(m.group(1)),
                                 "id": int(m.group(2)),
                                 "stripped": bool(m.group(3)),
                                 "zeilen": []}
                    bloecke.append(aktueller)
                elif aktueller is not None:
                    aktueller["zeilen"].append(zeile.rstrip("\n"))

        def greife(block, muster):
            for z in block["zeilen"]:
                m = re.search(muster, z)
                if m:
                    return m.group(1)
            return None

        go_name = {}
        transforms = {}
        wurzel_reihenfolge = []
        prefab_wurzeln = []
        kinder_von = {}

        for b in bloecke:
            if b["stripped"]:
                continue
            if b["klasse"] == 1:
                go_name[b["id"]] = greife(b, r"m_Name: (.*)$") or u"?"
            elif b["klasse"] in (4, 224):
                go = greife(b, r"m_GameObject: \{fileID: (\d+)\}")
                vater = greife(b, r"m_Father: \{fileID: (-?\d+)\}")
                transforms[b["id"]] = {"go": int(go) if go else 0,
                                       "vater": int(vater) if vater else 0}
            elif b["klasse"] == 1001:
                vater = greife(b, r"m_TransformParent: \{fileID: (-?\d+)\}")
                name = None
                for i, z in enumerate(b["zeilen"]):
                    if "propertyPath: m_Name" in z and i + 1 < len(b["zeilen"]):
                        m = re.search(r"value: (.*)$", b["zeilen"][i + 1])
                        if m:
                            name = m.group(1)
                            break
                eintrag = {"id": b["id"], "vater": int(vater) if vater else 0,
                           "name": name or u"(Prefab)"}
                if eintrag["vater"] == 0:
                    prefab_wurzeln.append(eintrag)
                else:
                    kinder_von.setdefault(eintrag["vater"], []).append(eintrag)
            elif b["klasse"] == 1660057539:
                for z in b["zeilen"]:
                    m = re.search(r"- \{fileID: (\d+)\}", z)
                    if m:
                        wurzel_reihenfolge.append(int(m.group(1)))

        for tid, info in transforms.items():
            kinder_von.setdefault(info["vater"], []).append({"id": tid})

        def kinderzahl(tid):
            return len(kinder_von.get(tid, []))

        wurzeln = []
        gesehen = set()
        datei_reihenfolge = ([tid for tid, i in transforms.items() if i["vater"] == 0]
                             + [p["id"] for p in prefab_wurzeln])
        for wid in wurzel_reihenfolge + datei_reihenfolge:
            if wid in gesehen:
                continue
            if wid in transforms and transforms[wid]["vater"] == 0:
                gesehen.add(wid)
                name = go_name.get(transforms[wid]["go"], u"?")
                wurzeln.append((name, kinderzahl(wid)))
            else:
                for p in prefab_wurzeln:
                    if p["id"] == wid:
                        gesehen.add(wid)
                        wurzeln.append((p["name"] + u" (Prefab)", 0))
        ergebnis[datei[:-6]] = wurzeln
    return ergebnis


def main():
    projekt = projekt_pfad()
    alt = alte_eintraege()
    neu = gefundene_systeme(projekt)

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

    zeilen = [KOPF, SCRIPTS_TABELLE_KOPF]
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

    zeilen.append(u"\n## Assets — oberste Ebene\n\n")
    zeilen.append(u"| Ordner | Dateien |\n|---|---|\n")
    for name, anzahl in assets_ebene(projekt):
        zeilen.append(u"| %s | %d |\n" % (name, anzahl))

    zeilen.append(u"\n## Szenen — Wurzel-Objekte\n\n")
    zeilen.append(u"Reihenfolge wie im Hierarchie-Panel; Zahl = direkte Kinder.\n")
    for szene, wurzeln in sorted(szenen_wurzeln(projekt).items()):
        zeilen.append(u"\n### %s\n\n" % szene)
        for name, kinder in wurzeln:
            if kinder == 1:
                zeilen.append(u"- %s (1 Kind)\n" % name)
            elif kinder:
                zeilen.append(u"- %s (%d Kinder)\n" % (name, kinder))
            else:
                zeilen.append(u"- %s\n" % name)

    if "--write" in sys.argv:
        with io.open(ZIEL, "w", encoding="utf-8") as fh:
            fh.write("".join(zeilen).rstrip("\n") + "\n")
        print("geschrieben:", ZIEL)
    else:
        print("\n(Probelauf. Mit --write wird geschrieben.)")


if __name__ == "__main__":
    main()
