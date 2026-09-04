# -*- coding: utf-8 -*-
"""Liest eine Unity-Szene samt UI-Prefabs und meldet Aufbau, Werte und Verdrahtung.

Arbeitsteilung (Kern/DOC_RULES.md, Abschnitt 5):
  Das Skript besitzt den *Ist-Zustand* — Hierarchie, Pivots, Größen,
  Farben samt Alpha, Schriftarten und -größen, jede OnClick-Liste, jede
  Ereignisliste der Eingabefelder, die Feld-Verdrahtung der eigenen
  MonoBehaviours und die Überschreibungen der Prefab-Instanzen. Ob ein
  Wert *richtig* ist, beurteilt der Mensch — gegen die Regeln in
  `Projekte/Isor_Tower/DECISIONS/UI.md`.

  Entstanden am 2026-09-04 beim Szenen-Audit des Hauptmenüs (15 Funde,
  darunter ein Knopf, der die falsche Methode rief). Dieselbe Machart
  wie das Skript-Audit vom 2026-08-28, nur wiederholbar.

Den Projektpfad liest das Skript aus `Kern/PFADE.md`, Marke `PROJEKT` —
kein harter Pfad im Skript, beim Umzug ändert sich eine Zeile.
Die Prefabs entdeckt es selbst: Jede Instanz in der Szene nennt ihre
Quelle, die Quelle wird über die .meta-Dateien gefunden und mitgelesen.

Aufruf:
    python szene_pruefen.py                  prüft MainMenu
    python szene_pruefen.py StarterVillage   prüft eine andere Szene
"""
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.dirname(os.path.dirname(os.path.dirname(HIER)))

# Bekannte Paket-Komponenten: deren .meta liegt nicht unter Assets,
# deshalb hier die ersten acht Zeichen ihrer festen GUIDs.
BEKANNT = {
    "fe87c0e1": "Image", "4e29b1a8": "Button", "f4688fdb": "TMP-Text",
    "2da0c512": "TMP_InputField", "306cc8c2": "LayoutElement",
    "59f81469": "VerticalLayoutGroup", "30649d3a": "HorizontalLayoutGroup",
    "3245ec92": "ContentSizeFitter", "3312d773": "RectMask2D",
    "0cd44c10": "CanvasScaler", "dc42784c": "GraphicRaycaster",
    "25d19c9f": "AspectRatioFitter", "31a19414": "Slider",
    "67db9e8f": "Toggle", "1344c3c8": "Mask",
}


def projektpfad():
    pfade = os.path.join(HARNESS, "Kern", "PFADE.md")
    with io.open(pfade, encoding="utf-8") as f:
        for zeile in f:
            m = re.match(r"\|\s*`PROJEKT`\s*\|\s*`([^`]+)`", zeile)
            if m:
                return m.group(1).rstrip("\\/")
    raise SystemExit("Marke PROJEKT nicht in Kern/PFADE.md gefunden.")


def guid_karte(wurzel):
    karte = {}
    for basis, _, dateien in os.walk(os.path.join(wurzel, "Assets")):
        for d in dateien:
            if not d.endswith(".meta"):
                continue
            try:
                with io.open(os.path.join(basis, d), encoding="utf-8", errors="ignore") as f:
                    m = re.search(r"guid: ([0-9a-f]{32})", f.read(400))
            except OSError:
                continue
            if m:
                karte[m.group(1)] = (d[:-5], os.path.join(basis, d[:-5]))
    return karte


def gname(guid, karte):
    if not guid:
        return "?"
    if guid in karte:
        return karte[guid][0]
    if guid[:8] in BEKANNT:
        return BEKANNT[guid[:8]]
    if guid.startswith("0000000000000000"):
        return "builtin"
    return "?" + guid[:8]


def lade(pfad):
    with io.open(pfad, encoding="utf-8") as f:
        text = f.read()
    doks = {}
    for m in re.finditer(r"^--- !u!(\d+) &(-?\d+)( stripped)?\n(.*?)(?=^--- !u!|\Z)",
                         text, re.M | re.S):
        doks[m.group(2)] = {"cls": int(m.group(1)), "body": m.group(4),
                            "stripped": bool(m.group(3))}
    return doks


def wert(body, key):
    m = re.search(r"^\s*%s: (.*)$" % re.escape(key), body, re.M)
    return m.group(1).strip() if m else None


def verweis(body, key):
    m = re.search(r"%s: \{fileID: (-?\d+)(?:, guid: ([0-9a-f]{32}))?" % re.escape(key), body)
    return (m.group(1), m.group(2)) if m else (None, None)


def farbe(body, key="m_Color"):
    m = re.search(r"%s: \{r: ([\d.e+-]+), g: ([\d.e+-]+), b: ([\d.e+-]+), a: ([\d.e+-]+)\}" % key, body)
    if not m:
        return None
    r, g, b, a = (float(x) for x in m.groups())
    return "#%02X%02X%02X A%d" % (round(r * 255), round(g * 255), round(b * 255), round(a * 255))


class Welt(object):
    """Ein geladenes YAML-Dokumentbündel: eine Szene oder ein Prefab."""

    def __init__(self, doks, karte):
        self.doks, self.karte = doks, karte
        self.gos, self.tr = {}, {}
        for fid, d in doks.items():
            if d["stripped"]:
                continue
            if d["cls"] == 1:
                comps = re.findall(r"component: \{fileID: (-?\d+)\}", d["body"])
                self.gos[fid] = {"name": wert(d["body"], "m_Name"),
                                 "aktiv": wert(d["body"], "m_IsActive") == "1",
                                 "comps": comps}
            elif d["cls"] in (224, 4):
                go, _ = verweis(d["body"], "m_GameObject")
                vater, _ = verweis(d["body"], "m_Father")
                teil = d["body"].split("m_Children:")[-1].split("m_Father")[0] \
                    if "m_Children:" in d["body"] else ""
                kinder = re.findall(r"- \{fileID: (-?\d+)\}", teil)
                self.tr[fid] = {"go": go, "vater": vater, "kinder": kinder, "body": d["body"]}

    def pfad(self, gofid):
        tfid = None
        for fid, t in self.tr.items():
            if t["go"] == gofid:
                tfid = fid
                break
        teile = []
        while tfid in self.tr:
            teile.append(self.gos.get(self.tr[tfid]["go"], {}).get("name", "?"))
            tfid = self.tr[tfid]["vater"]
        return "/".join(reversed(teile))

    def name(self, fid):
        d = self.doks.get(fid)
        if not d:
            return "extern:" + str(fid)
        if d["stripped"]:
            _, g = verweis(d["body"], "m_CorrespondingSourceObject")
            return "PREFABTEIL(%s)" % gname(g, self.karte)
        if d["cls"] == 1:
            return self.pfad(fid)
        go, _ = verweis(d["body"], "m_GameObject")
        basis = self.pfad(go) if go else "?"
        if d["cls"] == 114:
            _, sg = verweis(d["body"], "m_Script")
            return "%s[%s]" % (basis, gname(sg, self.karte))
        return basis

    def ruf(self, callbody):
        tgt, tg = verweis(callbody, "m_Target")
        methode = wert(callbody, "m_MethodName")
        modus = wert(callbody, "m_Mode")
        arg = ""
        if modus == "3":
            arg = "(%s)" % (wert(callbody, "m_IntArgument") or "?")
        elif modus == "6":
            arg = "(AN)" if wert(callbody, "m_BoolArgument") == "1" else "(AUS)"
        elif modus == "5":
            m = re.search(r"m_StringArgument: (.*)", callbody)
            arg = "('%s')" % m.group(1).strip() if m else ""
        ziel = self.name(tgt) if tgt and tgt != "0" else "asset:" + gname(tg, self.karte)
        return "%s.%s%s" % (ziel, methode, arg)

    def rufe(self, body, key):
        if key + ":" not in body:
            return []
        teil = body.split(key + ":", 1)[1][:4000]
        return [self.ruf(m.group(0)) for m in
                re.finditer(r"- m_Target: \{fileID: (-?\d+).*?(?=- m_Target|\Z)", teil, re.S)][:12]


def gib_baum(welt, zeilen):
    wurzeln = [f for f, t in welt.tr.items()
               if t["vater"] in (None, "0") or t["vater"] not in welt.tr]

    def gib(tfid, tiefe):
        t = welt.tr[tfid]
        go = welt.gos.get(t["go"])
        if not go:
            return
        rand = "  " * tiefe
        zeilen.append("%s%s%s" % (rand, go["name"], "" if go["aktiv"] else "  [INAKTIV]"))
        b = t["body"]
        piv = re.search(r"m_Pivot: \{x: ([\d.e+-]+), y: ([\d.e+-]+)\}", b)
        gr = re.search(r"m_SizeDelta: \{x: ([\d.e+-]+), y: ([\d.e+-]+)\}", b)
        if piv and gr:
            zeilen.append("%s  rect %sx%s pivot %s/%s" % (rand, gr.group(1), gr.group(2),
                                                          piv.group(1), piv.group(2)))
        for cfid in go["comps"]:
            cd = welt.doks.get(cfid)
            if not cd or cd["cls"] in (224, 4) or cd["stripped"]:
                continue
            cb = cd["body"]
            if cd["cls"] == 225:
                zeilen.append("%s  CanvasGroup alpha=%s interactable=%s"
                              % (rand, wert(cb, "m_Alpha"), wert(cb, "m_Interactable")))
                continue
            if cd["cls"] != 114:
                continue
            _, sg = verweis(cb, "m_Script")
            s = gname(sg, welt.karte)
            if s == "Image":
                _, spr = verweis(cb, "m_Sprite")
                typen = {"0": "Simple", "1": "Sliced", "2": "Tiled", "3": "Filled"}
                zeilen.append("%s  Image %s sprite=%s %s ppu=%s"
                              % (rand, farbe(cb), gname(spr, welt.karte) if spr else "KEINS",
                                 typen.get(wert(cb, "m_Type") or "0", "?"),
                                 wert(cb, "m_PixelsPerUnitMultiplier")))
            elif s == "TMP-Text":
                _, fg = verweis(cb, "m_fontAsset")
                txt = (wert(cb, "m_text") or "").replace("\\n", " ")[:36]
                zeilen.append("%s  TMP '%s' font=%s size=%s %s"
                              % (rand, txt, gname(fg, welt.karte), wert(cb, "m_fontSize"),
                                 farbe(cb, "m_fontColor")))
            elif s == "Button":
                for r in (welt.rufe(cb, "m_OnClick") or ["(leer)"]):
                    zeilen.append("%s  OnClick -> %s" % (rand, r))
            elif s == "TMP_InputField":
                still = True
                for ev in ("m_OnValueChanged", "m_OnEndEdit", "m_OnSelect", "m_OnSubmit"):
                    for r in welt.rufe(cb, ev):
                        zeilen.append("%s  InputField.%s -> %s" % (rand, ev, r))
                        still = False
                if still:
                    zeilen.append("%s  InputField (Listen leer)" % rand)
            elif s == "Slider":
                for r in welt.rufe(cb, "m_OnValueChanged"):
                    zeilen.append("%s  Slider.OnValueChanged -> %s" % (rand, r))
            elif s.endswith(".cs"):
                felder = list(re.finditer(r"^\s\s(_\w+): \{fileID: (-?\d+)", cb, re.M))
                if felder:
                    zeilen.append("%s  [%s] Felder:" % (rand, s))
                    for fm in felder:
                        ziel = welt.name(fm.group(2)) if fm.group(2) != "0" else "LEER"
                        zeilen.append("%s      %s -> %s" % (rand, fm.group(1), ziel))
                else:
                    zeilen.append("%s  [%s]" % (rand, s))
        for k in t["kinder"]:
            if k in welt.tr:
                gib(k, tiefe + 1)

    for w in wurzeln:
        gib(w, 0)


def main():
    szene = sys.argv[1] if len(sys.argv) > 1 else "MainMenu"
    projekt = projektpfad()
    szenenpfad = os.path.join(projekt, "Assets", "Scenes", szene + ".unity")
    if not os.path.exists(szenenpfad):
        raise SystemExit("Szene nicht gefunden: " + szenenpfad)
    karte = guid_karte(projekt)

    zeilen = ["=== SZENE %s ===" % szene]
    szenen_doks = lade(szenenpfad)
    welt = Welt(szenen_doks, karte)
    gib_baum(welt, zeilen)

    # Prefab-Instanzen: Quelle entdecken, Überschreibungen melden, Quelle mitlesen.
    quellen = []
    zeilen.append("")
    zeilen.append("=== PREFAB-INSTANZEN: Überschreibungen (ohne Transform-Werte) ===")
    for fid, d in szenen_doks.items():
        if d["cls"] != 1001:
            continue
        _, pg = verweis(d["body"], "m_SourcePrefab")
        name = gname(pg, karte)
        if pg in karte and karte[pg][1] not in quellen:
            quellen.append(karte[pg][1])
        zeilen.append("")
        zeilen.append("--- Instanz von %s ---" % name)
        pdoks = lade(karte[pg][1]) if pg in karte else {}
        for mm in re.finditer(
                r"- target: \{fileID: (-?\d+), guid: [0-9a-f]+, type: 3\}\n"
                r"\s+propertyPath: (.+)\n\s+value: (.*)\n"
                r"\s+objectReference: \{fileID: (-?\d+)", d["body"]):
            tgt, prop, v, obj = mm.groups()
            if re.search(r"m_(LocalPos|LocalRot|LocalScale|Anchor|SizeDelta|Pivot"
                         r"|RootOrder|LocalEuler)", prop):
                continue
            traeger = ""
            td = pdoks.get(tgt)
            if td:
                tg_go, _ = verweis(td["body"], "m_GameObject")
                traeger = (wert(pdoks[tg_go]["body"], "m_Name") if tg_go in pdoks
                           else wert(td["body"], "m_Name")) or "?"
                traeger += ": "
            objtxt = " => " + welt.name(obj) if obj and obj != "0" else ""
            zeilen.append("  %s%s = %s%s" % (traeger, prop, v.strip() or "-", objtxt))

    for q in quellen:
        zeilen.append("")
        zeilen.append("=== PREFAB %s ===" % os.path.basename(q))
        gib_baum(Welt(lade(q), karte), zeilen)

    out = "\n".join(zeilen)
    try:
        print(out)
    except UnicodeEncodeError:
        sys.stdout.buffer.write(out.encode("utf-8"))


if __name__ == "__main__":
    main()
