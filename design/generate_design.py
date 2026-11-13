#!/usr/bin/env python3
"""TaskKu v2 — UI/UX kit to-do list untuk FigCraft.

Referensi desain (riset online, Nov 2026):
- Things 3 (MacStories): whitespace lega, tipografi berani, aksen warna terbatas
- Upper (Tubik Studio): micro-label uppercase untuk metadata, streak/progres, aksi utama di bawah
- Tren mobile 2025-2026 (Fuselab): kartu radius besar, soft shadow, dark mode, color coding

Output: build.json -> figcraft-cli run --out TaskKu.figcraft
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build.json")

cmds = []
_n = [0]


def S(cmd, params=None, as_name=None):
    d = {"command": cmd}
    if params:
        d["params"] = params
    if as_name:
        _n[0] += 1
        d["as"] = f"{as_name}_{_n[0]}"
        cmds.append(d)
        return {"$ref": d["as"]}
    cmds.append(d)
    return None


FONT = "Plus Jakarta Sans"

VARS = {
    "bg":          ("#F4F4F9", "#0F0F15"),
    "surface":     ("#FFFFFF", "#1C1C24"),
    "surface-2":   ("#F0F0F6", "#27272F"),
    "text":        ("#131319", "#F5F5FA"),
    "text-muted":  ("#74748A", "#9C9CB1"),
    "border":      ("#E7E7EF", "#2B2B36"),
    "primary":     ("#5B54F0", "#9089FF"),
    "primary-soft":("#ECEBFE", "#2C2A55"),
    "primary-fg":  ("#FFFFFF", "#FFFFFF"),
    "success":     ("#12B76A", "#34D399"),
    "warning":     ("#F79009", "#FBBF24"),
    "danger":      ("#E5484D", "#F87171"),
}

CAT = {
    "Pekerjaan": ("#5B54F0", "#ECEBFE"),
    "Pribadi":   ("#0E9F6E", "#E5F6EF"),
    "Belanja":   ("#DC8A0E", "#FDF2E1"),
    "Kesehatan": ("#E5484D", "#FDEBEB"),
}

GRAD = {"type": "linearGradient", "stops": ["#6C5CE7", "#9F7AEA"], "from": [0, 0], "to": [1, 1]}
GRAD_COVER = {"type": "linearGradient", "stops": ["#191933", "#2A2170"], "from": [0, 0], "to": [1, 1]}

SH_CARD = [{"type": "dropShadow", "color": "#13131912", "offset": [0, 4], "radius": 16, "spread": 0, "visible": True, "blend": "normal"}]
SH_FLOAT = [{"type": "dropShadow", "color": "#13131926", "offset": [0, 12], "radius": 32, "spread": 0, "visible": True, "blend": "normal"}]
SH_BTN = [{"type": "dropShadow", "color": "#5B54F059", "offset": [0, 8], "radius": 20, "spread": 0, "visible": True, "blend": "normal"}]
SH_SHEET = [{"type": "dropShadow", "color": "#13131933", "offset": [0, -6], "radius": 24, "spread": 0, "visible": True, "blend": "normal"}]

PHONE_W, PHONE_H = 393, 852

ICONS = {
    "chevron_right": "M9 18l6-6-6-6",
    "chevron_left":  "M15 18l-6-6 6-6",
    "chevron_down":  "M6 9l6 6 6-6",
    "plus":          "M12 5v14M5 12h14",
    "check":         "M20 6L9 17l-5-5",
    "clock":         "M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6.5v5.5l3.5 2",
    "calendar":      "M8 2v4M16 2v4M3.5 9.5h17M5.5 4h13a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z",
    "home":          "M3 10.2L12 3l9 7.2V19.5a2 2 0 0 1-2 2h-14a2 2 0 0 1-2-2zM9.2 21.5v-6.2h5.6v6.2",
    "user":          "M12 12.5a4.2 4.2 0 1 0 0-8.4 4.2 4.2 0 0 0 0 8.4zM19.8 21.5v-1a5.8 5.8 0 0 0-5.8-5.8h-4a5.8 5.8 0 0 0-5.8 5.8v1",
    "chart":         "M5.5 20.5v-7M12 20.5v-13M18.5 20.5v-10",
    "search":        "M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.35-4.35",
    "bell":          "M6.2 9.3a5.8 5.8 0 0 1 11.6 0c0 5.7 2.4 7.2 2.4 7.2H3.8s2.4-1.5 2.4-7.2zM10.3 20.3a2 2 0 0 0 3.4 0",
    "x":             "M18 6L6 18M6 6l12 12",
    "eye":           "M2.5 12s3.4-6.8 9.5-6.8S21.5 12 21.5 12s-3.4 6.8-9.5 6.8S2.5 12 2.5 12zM12 14.8a2.8 2.8 0 1 0 0-5.6 2.8 2.8 0 0 0 0 5.6z",
    "sliders":       "M4 6.5h16M4 12h16M4 17.5h16M14 4.5v4M8 10v4M16.5 15.5v4",
    "sun":           "M12 16.5a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9zM12 1.5v2.4M12 20.1v2.4M4.6 4.6l1.7 1.7M17.7 17.7l1.7 1.7M1.5 12h2.4M20.1 12h2.4M4.6 19.4l1.7-1.7M17.7 6.3l1.7-1.7",
    "moon":          "M20.8 13.1A8.8 8.8 0 1 1 10.9 3.2a6.9 6.9 0 0 0 9.9 9.9z",
    "logout":        "M9.5 21H5.5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 16.5l4.5-4.5-4.5-4.5M20.5 12H9.5",
    "wifi":          "M2.5 9a15.5 15.5 0 0 1 19 0M5.2 12.4a11 11 0 0 1 13.6 0M8.3 15.6a6.3 6.3 0 0 1 7.4 0",
    "zap":           "M13 2L4.5 13.5h6.5L9.5 22l10-12.5H13L13 2z",
    "flag":          "M5 21V4M5 4.5c4-2 7 2 12 .5v8c-5 1.5-8-2.5-12-.5",
    "star":          "M12 3l2.7 5.6 6.3.9-4.6 4.3 1.1 6.2L12 17.2l-5.5 3 1-6.2L2.9 9.5l6.4-.9z",
    "tag":           "M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42zM7.5 7.5h.01",
}


def T(text, parent, size=14.5, style="Regular", color="text", width=None, name=None,
      align=None, ls=None, lh=None, deco=None, fill_hex=None):
    props = {"fontFamily": FONT, "fontStyle": style, "fontSize": size,
             "fill": fill_hex if fill_hex else {"$var": color}}
    if align: props["textAlign"] = align
    if ls is not None: props["letterSpacing"] = ls
    if lh is not None: props["lineHeight"] = lh
    if deco: props["textDecoration"] = deco
    p = {"text": text, "x": 0, "y": 0, "parent": parent, "props": props,
         "name": name or (text[:28] if text else "Teks")}
    if width: p["width"] = width
    return S("text.create", p, as_name="t")


def F(parent=None, name="Frame", layout=None, w=None, h=None, fill="none",
      radius=None, pad=None, gap=None, main=None, cross=None, sizingH=None,
      sizingV=None, stroke=None, sw=1, effects=None, absolute=False, x=0, y=0,
      opacity=None, grid=None, cgap=None, rgap=None, key="f", clip=False,
      stroke_top=False, wrap=None):
    if w == "fill":
        sizingH, w = "fill", None
    if h == "fill":
        sizingV, h = "fill", None
    if layout:
        if w is None and sizingH is None:
            sizingH = "hug"
        if h is None and sizingV is None:
            sizingV = "hug"
    props = {}
    if isinstance(fill, dict) and "type" in fill:
        props["fills"] = [fill]
    else:
        props["fill"] = fill
    if radius is not None: props["cornerRadius"] = radius
    if layout: props["layout"] = layout
    if pad is not None: props["padding"] = pad
    if gap is not None: props["gap"] = gap
    if main: props["mainAlign"] = main
    if cross: props["crossAlign"] = cross
    if sizingH: props["sizingH"] = sizingH
    if sizingV: props["sizingV"] = sizingV
    if stroke is not None:
        props["stroke"] = stroke
        props["strokeWeight"] = sw
        props["strokeAlign"] = "inside"
    if stroke_top:
        props["stroke"] = stroke or {"$var": "border"}
        props["strokeTopWeight"] = sw
        props["strokeAlign"] = "inside"
    if effects: props["effects"] = effects
    if absolute: props["absolute"] = True
    if opacity is not None: props["opacity"] = opacity
    if grid is not None: props["gridColumns"] = grid
    if cgap is not None: props["columnGap"] = cgap
    if rgap is not None: props["rowGap"] = rgap
    if wrap: props["wrap"] = True
    if clip: props["clip"] = True
    p = {"x": x, "y": y, "name": name, "props": props}
    if parent: p["parent"] = parent
    if w: p["width"] = w
    if h: p["height"] = h
    return S("frame.create", p, as_name=key)


def icon(name, parent, size=24, color="text", sw=2, key="ic", fill_hex=None, opacity=None):
    props = {"stroke": fill_hex if fill_hex else {"$var": color},
             "strokeWeight": sw, "strokeCap": "round", "strokeJoin": "round"}
    if opacity is not None: props["opacity"] = opacity
    return S("vector.create", {"path": ICONS[name], "parent": parent, "width": size,
                               "props": props, "name": f"i/{name}"}, as_name=key)


def dot(parent, size, fill, key="dot", opacity=None, absolute=False, x=0, y=0):
    return F(parent, "dot", w=size, h=size, radius=999, fill=fill, key=key,
             opacity=opacity, absolute=absolute, x=x, y=y)


def micro(parent, text, color="text-muted", key="mic"):
    """Label metadata uppercase ala Upper/Tubik."""
    return T(text.upper(), parent, size=10, style="SemiBold", color=color, ls="8%", name=key)


def statusbar(parent):
    sb = F(parent, "Status Bar", layout="horizontal", w="fill", h=47,
           pad=[6, 24, 0, 24], main="space-between", cross="center", key="sb")
    T("9:41", sb, size=14, style="SemiBold", name="Waktu")
    right = F(sb, "Sistem", layout="horizontal", gap=6, cross="center", key="sbr")
    bars = F(right, "Sinyal", layout="horizontal", gap=1.5, cross="max", key="sig")
    for i, hgt in enumerate([4, 6, 8, 11]):
        F(bars, "bar", w=3, h=hgt, radius=1, fill={"$var": "text"}, key=f"sig{i}")
    icon("wifi", right, size=15, sw=2)
    bat = F(right, "Baterai", layout="horizontal", gap=1.5, cross="center", key="bat")
    body = F(bat, "b", w=23, h=12, radius=4, stroke={"$var": "text-muted"}, sw=1,
             pad=[2, 2, 2, 2], key="batb")
    F(body, "lvl", w=14, h=6, radius=2, fill={"$var": "text"}, key="batl")
    F(bat, "tip", w=1.5, h=4, radius=1, fill={"$var": "text-muted"}, key="batt")
    return sb


def chip(parent, label, selected=False, key="chip"):
    c = F(parent, f"Chip/{label}", layout="horizontal", pad=[8, 16], radius=999,
          cross="center",
          fill={"$var": "primary"} if selected else {"$var": "surface"},
          stroke=None if selected else {"$var": "border"}, key=key)
    T(label, c, size=13, style="SemiBold" if selected else "Regular",
      color="primary-fg" if selected else "text-muted", name="label")
    return c


def button(parent, label, kind="primary", h=54, full=True, w=None, key="btn", size=15):
    st = {"primary": dict(fill=GRAD, effects=SH_BTN, tc="primary-fg", stroke=None),
          "secondary": dict(fill={"$var": "surface"}, stroke={"$var": "border"}, tc="text"),
          "ghost": dict(fill="none", stroke=None, tc="primary"),
          "danger": dict(fill="none", stroke={"$var": "danger"}, tc="danger"),
          "soft": dict(fill={"$var": "primary-soft"}, stroke=None, tc="primary")}[kind]
    b = F(parent, f"Btn/{label}", layout="horizontal", main="center", cross="center",
          w=w, h=h, radius=h / 2, pad=[0, 24], fill=st["fill"], stroke=st["stroke"],
          effects=st.get("effects"), sizingH="fill" if full and not w else None, key=key)
    T(label, b, size=size, style="SemiBold", color=st["tc"], ls="-1%", name="label")
    return b


def toggle(parent, on=True, key="tg"):
    tr = F(parent, "Switch", w=46, h=27, radius=999,
           fill={"$var": "primary" if on else "border"}, pad=[3], main="max" if on else "min",
           cross="center", key=key)
    dot(tr, 21, "#FFFFFF", key=key + "k")
    return tr


def fieldbox(parent, value, key="fld", h=56, placeholder=False, trailing=None):
    f = F(parent, "Input", layout="horizontal", w="fill", h=h, radius=16,
          pad=[0, 18], cross="center", main="space-between" if trailing else "min",
          fill={"$var": "surface-2"}, gap=8, key=key)
    T(value, f, size=14.5, style="Medium" if not placeholder else "Regular",
      color="text" if not placeholder else "text-muted", name="nilai")
    if trailing:
        trail = F(f, "trail", layout="horizontal", gap=8, cross="center", key=key + "tr")
        for t in trailing:
            icon(t, trail, size=18, color="text-muted")
    return f


def labeled_field(parent, label, value, key="lf", h=56, placeholder=False, trailing=None):
    col = F(parent, f"Field/{label}", layout="vertical", gap=8, sizingH="fill", key=key)
    T(label, col, size=12.5, style="SemiBold", color="text-muted", name=key + "l")
    fieldbox(col, value, key=key + "f", h=h, placeholder=placeholder, trailing=trailing)
    return col


def taskcard(parent, title, cat, time, prio, done=False, key="card", width=None):
    """prio = hex statis; cat = kunci CAT."""
    card = F(parent, f"Tugas / {title[:24]}", layout="horizontal", gap=13, pad=[13, 16],
             radius=20, fill={"$var": "surface"}, effects=SH_CARD, cross="center",
             sizingH="fill" if not width else None, w=width, key=key)
    if done:
        cb = F(card, "Cek", w=24, h=24, radius=999, fill={"$var": "success"},
               layout="horizontal", main="center", cross="center", key=key + "cb")
        icon("check", cb, size=13, sw=3, fill_hex="#FFFFFF", key=key + "ck")
    else:
        F(card, "Cek", w=24, h=24, radius=999, stroke={"$var": "border"}, sw=2, key=key + "cb")
    col = F(card, "Isi", layout="vertical", gap=7, sizingH="fill", key=key + "col")
    T(title, col, size=15, style="Medium" if not done else "Regular",
      color="text" if not done else "text-muted", lh="135%",
      deco="strikethrough" if done else None, name="judul")
    meta = F(col, "Meta", layout="horizontal", gap=10, cross="center", key=key + "meta")
    fg, bg = CAT[cat]
    tag = F(meta, "Tag", layout="horizontal", gap=5, cross="center", pad=[4, 10],
            radius=999, fill=bg, key=key + "tag")
    dot(tag, 5, fg, key=key + "tagd")
    T(cat, tag, size=11, style="SemiBold", fill_hex=fg, name="tagl")
    icon("clock", meta, size=12.5, color="text-muted", sw=2, key=key + "cl")
    T(time, meta, size=11.5, color="text-muted", name="jam")
    icon("flag", card, size=15, fill_hex=prio, sw=2, key=key + "prio")
    return card


def section_header(parent, title, count=None, action="Lihat semua", key="sec"):
    r = F(parent, "Bagian", layout="horizontal", w="fill", gap=8, cross="center", key=key)
    T(title, r, size=16.5, style="SemiBold", ls="-1%", name="judul")
    if count:
        pill = F(r, "hitung", layout="horizontal", pad=[3, 9], radius=999,
                 fill={"$var": "surface-2"}, key=key + "p")
        T(str(count), pill, size=11, style="SemiBold", color="text-muted", name=key + "pl")
    if action:
        F(r, "spacer", sizingH="fill", h=1, key=key + "s")
        T(action, r, size=12.5, style="SemiBold", color="primary", name="aksi")
    return r


def ring(parent, pct, key="ring", size=62, lblsize=13):
    """Donut progres: track + arc + persentase."""
    box = F(parent, "Ring", w=size, h=size, key=key)
    S("shape.ellipse", {"x": 0, "y": 0, "width": size, "height": size, "parent": box,
                        "props": {"fill": {"$var": "border"}, "arcSweep": 360,
                                  "arcInner": 0.74}}, as_name=key + "tr")
    sweep = round(360 * pct / 100)
    S("shape.ellipse", {"x": 0, "y": 0, "width": size, "height": size, "parent": box,
                        "props": {"fill": {"$var": "primary"}, "arcStart": -90,
                                  "arcSweep": sweep, "arcInner": 0.74}}, as_name=key + "ar")
    lab = F(box, "lbl", w=size, h=size, layout="horizontal", main="center", cross="center",
            key=key + "lb")
    T(f"{pct}%", lab, size=lblsize, style="SemiBold", name=key + "lt")
    return box


def hero_card(parent, key="hero", wide=False):
    c = F(parent, "Hero", layout="vertical", w="fill", radius=26, fill=GRAD,
          pad=[20, 20], gap=14, effects=SH_BTN, key=key)
    r = F(c, "atas", layout="horizontal", w="fill", main="space-between", cross="min", key=key + "r")
    col = F(r, "sapaan", layout="vertical", gap=5, key=key + "c")
    T("Selamat pagi, Rian 👋", col, size=20 if not wide else 22, style="SemiBold",
      fill_hex="#FFFFFF", ls="-1%", name=key + "t1")
    T("Jumat, 13 November 2026", col, size=12.5, fill_hex="#FFFFFFB0", name=key + "t2")
    av = F(r, "Avatar", w=44, h=44, radius=999, fill="#FFFFFF2E",
           layout="horizontal", main="center", cross="center", key=key + "av")
    T("R", av, size=16, style="SemiBold", fill_hex="#FFFFFF", name=key + "avt")
    pills = F(c, "pil", layout="horizontal", gap=8, w="fill", key=key + "p")
    p1 = F(pills, "Streak", layout="horizontal", gap=6, cross="center", pad=[7, 12],
           radius=999, fill="#FFFFFF2B", key=key + "p1")
    icon("zap", p1, size=13, fill_hex="#FFD66B", sw=2, key=key + "p1i")
    T("12 hari streak", p1, size=11.5, style="SemiBold", fill_hex="#FFFFFF", name=key + "p1l")
    p2 = F(pills, "Sisa", layout="horizontal", pad=[7, 12], radius=999,
           fill="#FFFFFF2B", key=key + "p2")
    T("3 tugas hari ini", p2, size=11.5, style="SemiBold", fill_hex="#FFFFFF", name=key + "p2l")
    return c


def progress_card(parent, key="prog"):
    c = F(parent, "Progres", layout="horizontal", w="fill", radius=20,
          fill={"$var": "surface"}, pad=[16, 18], gap=16, cross="center",
          effects=SH_CARD, key=key)
    ring(c, 37, key=key + "ring")
    col = F(c, "info", layout="vertical", gap=4, sizingH="fill", key=key + "c")
    micro(col, "Progres hari ini", key=key + "m")
    T("3 dari 8 selesai", col, size=16, style="SemiBold", ls="-1%", name=key + "v")
    T("3 tugas lagi sebelum pukul 17:00", col, size=11.5, color="text-muted", name=key + "k")
    return c


def screen_frame(name, x, y=0, key="scr"):
    return F(None, name, w=PHONE_W, h=PHONE_H, fill={"$var": "bg"},
             layout="vertical", clip=True, x=x, y=y, key=key)


def dock_items(parent, active, key="dock"):
    refs = []
    items = [("Beranda", "home"), ("Kalender", "calendar"), ("Statistik", "chart"), ("Profil", "user")]
    for i, (label, ic) in enumerate(items):
        act = label == active
        it = F(parent, f"Menu/{label}", layout="horizontal", gap=6, cross="center", main="center",
               pad=[10, 14] if act else [10, 6], radius=999,
               fill={"$var": "primary-soft"} if act else "none", key=f"{key}i{i}")
        icon(ic, it, size=20, color="primary" if act else "text-muted", sw=2, key=f"{key}ic{i}")
        T(label, it, size=11, style="SemiBold" if act else "Regular",
          color="primary" if act else "text-muted", name=f"{key}l{i}")
        refs.append(it)
    return refs


def dock_bar(parent, active, key="dk", x=16, y=774, w=361):
    d = F(parent, "Dock", layout="horizontal", w=w, h=64, radius=999,
          fill={"$var": "surface"}, pad=[0, 10], main="space-between", cross="center",
          effects=SH_FLOAT, absolute=True, x=x, y=y, key=key)
    refs = dock_items(d, active, key=key + "i")
    return d, refs


def fab(parent, key="fab", x=311, y=698, size=58, ic="plus"):
    f = F(parent, "FAB", w=size, h=size, radius=999, fill=GRAD,
          layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
          absolute=True, x=x, y=y, key=key)
    icon(ic, f, size=26, sw=2.5, fill_hex="#FFFFFF", key=key + "i")
    return f


# ================================================================ HALAMAN 1: DS
S("page.rename", {"name": "🎨 Design System"})
S("variable.createCollection", {"name": "Warna", "modes": ["Terang", "Gelap"]})
for vname, (light, dark) in VARS.items():
    S("variable.create", {"collection": "Warna", "name": vname, "type": "color",
                          "values": {"Terang": light, "Gelap": dark}})

# --- Paint styles (terikat variabel) & text styles
for vname, (light, dark) in VARS.items():
    ps = S("style.create", {"type": "paint", "name": f"Warna/{vname}", "value": light},
           as_name=f"ps_{vname}")
    S("style.bind", {"style": ps, "field": "fill", "variable": vname})
TEXT_STYLES = [
    ("Teks/Display", {"fontFamily": FONT, "fontStyle": "SemiBold", "fontSize": 28,
                      "letterSpacing": "-2%", "lineHeight": "128%"}),
    ("Teks/Judul", {"fontFamily": FONT, "fontStyle": "SemiBold", "fontSize": 22,
                    "letterSpacing": "-1.5%", "lineHeight": "130%"}),
    ("Teks/Section", {"fontFamily": FONT, "fontStyle": "SemiBold", "fontSize": 16.5,
                      "letterSpacing": "-1%", "lineHeight": "140%"}),
    ("Teks/Body", {"fontFamily": FONT, "fontStyle": "Regular", "fontSize": 14.5,
                   "lineHeight": "155%"}),
    ("Teks/Body-Medium", {"fontFamily": FONT, "fontStyle": "Medium", "fontSize": 14.5,
                          "lineHeight": "135%"}),
    ("Teks/Kecil", {"fontFamily": FONT, "fontStyle": "Regular", "fontSize": 13,
                    "lineHeight": "150%"}),
    ("Teks/Micro", {"fontFamily": FONT, "fontStyle": "SemiBold", "fontSize": 10,
                    "letterSpacing": "8%", "lineHeight": "120%"}),
]
for nm, val in TEXT_STYLES:
    S("style.create", {"type": "text", "name": nm, "value": val})

# --- Cover gelap
cv = F(None, "Cover — TaskKu", w=1280, h=440, radius=28, fill=GRAD_COVER,
       layout="vertical", pad=[52, 60], gap=14, main="center", key="cover")
logo = F(cv, "Logo", w=68, h=68, radius=22, fill=GRAD,
         layout="horizontal", main="center", cross="center", effects=SH_BTN, key="logo")
icon("check", logo, size=32, sw=3, fill_hex="#FFFFFF", key="logoic")
T("TaskKu", cv, size=46, style="Bold", fill_hex="#FFFFFF", ls="-2%", name="judul")
T("Aplikasi To-Do List — UI/UX Kit", cv, size=17, fill_hex="#C9C5F5", name="sub")
meta = F(cv, "meta", layout="horizontal", gap=10, key="cvmeta")
for i, m in enumerate(["Plus Jakarta Sans", "393 × 852", "Terang & Gelap", "21 Layar", "Tablet & Desktop"]):
    pill = F(meta, f"m{i}", layout="horizontal", pad=[8, 14], radius=999,
             fill="#FFFFFF14", key=f"cvm{i}")
    T(m, pill, size=12, style="SemiBold", fill_hex="#D9D6FA", name=f"cvml{i}")

# --- Warna
cw = F(None, "Warna Token", w=1280, radius=24, fill={"$var": "surface"},
       layout="vertical", pad=[28, 32], gap=18, y=500, key="cw")
T("Palet Warna", cw, size=20, style="SemiBold", ls="-1%", name="jud")
T("Satu koleksi variabel \"Warna\" dengan mode Terang & Gelap — setiap layer terikat variabel, bukan hex.", cw,
  size=13, color="text-muted", name="ket")
grid = F(cw, "Swatch", layout="horizontal", gap=12, wrap=True, w="fill", key="swg")
for name, (light, dark) in VARS.items():
    sw = F(grid, f"Token/{name}", layout="vertical", gap=8, w=148, key=f"sw_{name}")
    F(sw, "warna", w=148, h=66, radius=14, fill=light, stroke={"$var": "border"}, sw=1, key=f"swb_{name}")
    T(name, sw, size=12.5, style="SemiBold", name=f"swn_{name}")
    T(f"T {light.upper()}   G {dark.upper()}", sw, size=9.5, color="text-muted", name=f"swx_{name}")

# --- Tipografi
tw = F(None, "Tipografi", w=1280, radius=24, fill={"$var": "surface"},
       layout="horizontal", pad=[28, 32], gap=56, y=960, key="tw")
col1 = F(tw, "Sampel", layout="vertical", gap=16, sizingH="fill", key="tw1")
T("Tipografi — Plus Jakarta Sans", col1, size=18, style="SemiBold", ls="-1%", name="tjud")
T("Display / 28 SemiBold", col1, size=28, style="SemiBold", ls="-2%", name="ts1")
T("Judul / 18 SemiBold", col1, size=18, style="SemiBold", ls="-1%", name="ts2")
T("Body / 14.5 Regular — Catat, atur, dan selesaikan tugasmu setiap hari dengan tenang.", col1,
  size=14.5, lh="155%", name="ts3")
T("Kecil / 13 — teks pendukung dan keterangan", col1, size=13, color="text-muted", name="ts4")
T("MICRO LABEL / 10 SEMIBOLD", col1, size=10, style="SemiBold", color="text-muted", ls="8%", name="ts5")
col2 = F(tw, "Skala", layout="vertical", gap=10, w=300, key="tw2")
for i, s in enumerate(["28 / SemiBold / Display", "18 / SemiBold / Judul", "16.5 / SemiBold / Section",
                       "14.5 / Regular+Medium / Body", "13 / Regular / Kecil", "10 / SemiBold / Micro"]):
    T(s, col2, size=12, color="text-muted", name=f"tw2_{i}")

# --- Komponen
comp = F(None, "Komponen", w=1280, radius=24, fill={"$var": "surface"},
         layout="vertical", pad=[28, 32], gap=20, y=1300, key="comp")
T("Komponen", comp, size=20, style="SemiBold", ls="-1%", name="cjud")
row1 = F(comp, "Tombol", layout="horizontal", gap=14, w="fill", key="crow1")
for i, (lbl, k) in enumerate([("Tugas Baru", "primary"), ("Kedua", "secondary"), ("Tersier", "ghost"), ("Hapus", "danger")]):
    button(row1, lbl, k, h=50, full=False, w=160, key=f"cb{i}")
row2 = F(comp, "Chip & Input", layout="horizontal", gap=14, w="fill", cross="center", key="crow2")
chip(row2, "Semua", selected=True, key="cch1")
chip(row2, "Pekerjaan", key="cch2")
chip(row2, "Pribadi", key="cch3")
chip(row2, "Belanja", key="cch4")
fldw = F(row2, "Input", w=280, layout="horizontal", key="cfldw")
fieldbox(fldw, "Cari tugas…", key="cfld1", placeholder=True, trailing=["search"])
tgw = F(row2, "Switch", layout="horizontal", gap=10, cross="center", key="ctg")
toggle(tgw, True, key="ctg1")
toggle(tgw, False, key="ctg2")
row3 = F(comp, "Kartu Tugas", layout="horizontal", gap=16, w="fill", key="crow3")
box1 = F(row3, "K1", w=380, key="cbox1")
taskcard(box1, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", key="ctask1", width=380)
box2 = F(row3, "K2", w=380, key="cbox2")
taskcard(box2, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", done=True, key="ctask2", width=380)
row4 = F(comp, "Navigasi & Progres", layout="horizontal", gap=20, w="fill", key="crow4")
progbox = F(row4, "ProgresKartu", w=330, layout="horizontal", key="cprogw")
progress_card(progbox, key="cprog")
navw = F(row4, "DockSampel", w=380, h=64, layout="horizontal", radius=999, fill={"$var": "surface"},
         pad=[0, 10], main="space-between", cross="center", effects=SH_FLOAT, key="cdocko")
dock_items(navw, "Beranda", key="cdock")
fab(comp, key="cfab", x=1180, y=252, size=58)

# --- Ikon
iw = F(None, "Ikon", w=1280, radius=24, fill={"$var": "surface"},
       layout="horizontal", pad=[24, 32], gap=22, cross="center",
       y=1840, key="iw")
T("Ikon", iw, size=16, style="SemiBold", name="iwt")
for i, nm in enumerate(["home", "calendar", "chart", "user", "search", "bell", "clock", "check",
                        "plus", "chevron_right", "chevron_down", "x", "eye", "sliders", "sun",
                        "moon", "logout", "zap", "flag", "star"]):
    icon(nm, iw, size=22, color="text", key=f"iw{i}")

# --- Komponen utama
mainrow = F(comp, "Komponen Utama", layout="horizontal", gap=16, w="fill", key="crow5")
m1box = F(mainrow, "M1", w=360, key="cm1")
mc = taskcard(m1box, "Contoh tugas", "Pribadi", "10:00", "#F79009", key="cmainc", width=360)

# ---- Component set (variants) di kanvas halaman DS
def _variant(frame_ref, x, y, name):
    S("node.set", {"id": frame_ref, "x": x, "y": y})
    S("component.create", {"id": frame_ref})
    S("object.rename", {"ids": [frame_ref], "name": name})
    return frame_ref


def _combine(ids, set_name):
    st = S("component.combineVariants", {"ids": ids}, as_name="set")
    S("object.rename", {"ids": [st], "name": set_name})


# TaskCard: Default & Done
v1 = taskcard(None, "Contoh tugas", "Pribadi", "10:00", "#F79009", key="vcard1", width=360)
v2 = taskcard(None, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", done=True,
              key="vcard2", width=360)
_combine([_variant(v1, 0, 2060, "State=Default"), _variant(v2, 430, 2060, "State=Done")],
         "TaskCard")
# Chip: Default & Selected
c1 = F(None, "Chip/Default", layout="horizontal", pad=[8, 16], radius=999, cross="center",
       fill={"$var": "surface"}, stroke={"$var": "border"}, key="vchip1")
T("Label", c1, size=13, color="text-muted", name="cl1")
c2 = F(None, "Chip/Selected", layout="horizontal", pad=[8, 16], radius=999, cross="center",
       fill={"$var": "primary"}, key="vchip2")
T("Label", c2, size=13, style="SemiBold", color="primary-fg", name="cl2")
_combine([_variant(c1, 0, 2210, "State=Default"), _variant(c2, 200, 2210, "State=Selected")],
         "Chip")
# Checkbox: Empty & Checked
cb1 = F(None, "Cek/Empty", w=24, h=24, radius=999, stroke={"$var": "border"}, sw=2, key="vcb1")
cb2 = F(None, "Cek/Checked", w=24, h=24, radius=999, fill={"$var": "primary"},
        layout="horizontal", main="center", cross="center", key="vcb2")
icon("check", cb2, size=13, sw=3, fill_hex="#FFFFFF", key="vcb2i")
_combine([_variant(cb1, 0, 2290, "State=Empty"), _variant(cb2, 80, 2290, "State=Checked")],
         "Checkbox")
# Button: 4 tipe
btn_ids = []
for i, (lbl, kind) in enumerate([("Primary", "primary"), ("Secondary", "secondary"),
                                 ("Ghost", "ghost"), ("Danger", "danger")]):
    b = button(None, "Label", kind, h=50, full=False, w=170, key=f"vbtn{i}")
    btn_ids.append(_variant(b, i * 350, 2360, f"Type={lbl}"))
_combine(btn_ids, "Button")
# Input: Default / Focus / Error
i1 = F(None, "Input/Default", layout="horizontal", w=345, h=56, radius=16, pad=[0, 18],
       cross="center", fill={"$var": "surface-2"}, stroke={"$var": "border"}, key="vinp1")
T("Placeholder", i1, size=14.5, color="text-muted", name="vinp1t")
i2 = F(None, "Input/Focus", layout="horizontal", w=345, h=56, radius=16, pad=[0, 18],
       cross="center", fill={"$var": "surface-2"}, stroke={"$var": "primary"}, sw=2, key="vinp2")
T("Menulis…", i2, size=14.5, style="Medium", name="vinp2t")
i3 = F(None, "Input/Error", layout="vertical", gap=6, sizingH=None, w=345, key="vinp3")
i3f = F(i3, "Field", layout="horizontal", w="fill", h=56, radius=16, pad=[0, 18],
        cross="center", fill={"$var": "surface-2"}, stroke={"$var": "danger"}, sw=2, key="vinp3f")
T("nama@email", i3f, size=14.5, style="Medium", name="vinp3t")
T("Email tidak valid", i3, size=11, color="danger", name="vinp3h")
_combine([_variant(i1, 0, 2440, "State=Default"), _variant(i2, 390, 2440, "State=Focus"),
          _variant(i3, 780, 2440, "State=Error")], "Input")

# ================================================================ HALAMAN 2: SCREENS
p2 = S("page.add", {"name": "📱 Screens"}, as_name="p2")
S("page.select", {"id": p2})

# ---- 01 Onboarding
onb_ref = scr = screen_frame("01 Onboarding", 0, key="onb")
F(scr, "Blob1", w=280, h=280, radius=999, fill=GRAD, opacity=0.35,
  effects=[{"type": "layerBlur", "radius": 90, "visible": True}],
  absolute=True, x=190, y=-90, key="onbblob1")
F(scr, "Blob2", w=240, h=240, radius=999, fill="#9F7AEA", opacity=0.22,
  effects=[{"type": "layerBlur", "radius": 90, "visible": True}],
  absolute=True, x=-80, y=620, key="onbblob2")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[10, 28], gap=20,
         main="center", cross="center", key="onbb")
ill = F(body, "Ilustrasi", w=340, h=250, layout="horizontal", main="center", cross="center", key="onbill")
F(ill, "Lingkaran", w=220, h=220, radius=999, fill={"$var": "primary-soft"}, key="onbcir")
cardill = F(ill, "Kartu", w=200, h=190, radius=24, fill={"$var": "surface"},
            effects=SH_CARD, layout="vertical", pad=[16, 18], gap=11, absolute=True, x=70, y=30, key="onbcard")
hd = F(cardill, "hd", layout="horizontal", w="fill", main="space-between", cross="center", key="onbhd")
T("Hari Ini", hd, size=12.5, style="SemiBold", name="onbhd1")
pilln = F(hd, "n", layout="horizontal", pad=[2, 9], radius=999, fill={"$var": "primary-soft"}, key="onbhn")
T("4", pilln, size=11, style="SemiBold", color="primary", name="onbhnl")
for i, (bw, done) in enumerate([(116, True), (92, True), (104, False)]):
    row = F(cardill, f"r{i}", layout="horizontal", gap=10, cross="center", key=f"onbr{i}")
    if done:
        cb = F(row, "cb", w=24, h=24, radius=999, fill={"$var": "primary"},
               layout="horizontal", main="center", cross="center", key=f"onbcb{i}")
        icon("check", cb, size=12, sw=3, fill_hex="#FFFFFF", key=f"onbck{i}")
    else:
        F(row, "cb", w=24, h=24, radius=999, stroke={"$var": "border"}, sw=2, key=f"onbcb{i}")
    F(row, "bar", w=bw, h=9, radius=5, fill={"$var": "surface-2"}, key=f"onbbar{i}")
badge = F(ill, "Badge", w=54, h=54, radius=999, fill={"$var": "surface"},
          layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
          absolute=True, x=228, y=10, key="onbbadge")
icon("bell", badge, size=22, color="primary", key="onbbell")
badge2 = F(ill, "Badge2", w=44, h=44, radius=999, fill={"$var": "surface"},
           layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
           absolute=True, x=10, y=178, key="onbbadge2")
icon("calendar", badge2, size=18, color="success", key="onbcal")
dot(ill, 16, "#FFD66B", absolute=True, x=252, y=28, key="onbdot1")
dot(ill, 10, "#5B54F0", absolute=True, x=28, y=204, key="onbdot2")
T("Kelola tugasmu,\ntanpa stres.", body, size=28, style="SemiBold", align="center",
  lh="128%", ls="-2%", name="onbjud")
T("Catat, atur prioritas, dan selesaikan tugas harianmu dalam satu aplikasi yang sederhana dan tenang.",
  body, size=14.5, color="text-muted", align="center", lh="160%", width=310, name="onbsub")
dots = F(body, "Dots", layout="horizontal", gap=7, cross="center", main="center",
         sizingH="fill", key="onbdots")
F(dots, "d1", w=22, h=8, radius=999, fill={"$var": "primary"}, key="onbd1")
dot(dots, 8, {"$var": "border"}, key="onbd2")
dot(dots, 8, {"$var": "border"}, key="onbd3")
onbbtn_ref = button(body, "Mulai Sekarang", "primary", key="onbbtn")
row = F(body, "MasukRow", layout="horizontal", gap=5, main="center", sizingH="fill", key="onbl")
T("Sudah punya akun?", row, size=13.5, color="text-muted", name="onbl1")
onbmasuk_ref = T("Masuk", row, size=13.5, style="SemiBold", color="primary", name="onbl2")

# ---- 02 Masuk
log_ref = scr = screen_frame("02 Masuk", 473, key="log")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[6, 26], gap=16, key="logb")
back = F(body, "Kembali", w=44, h=44, radius=999, fill={"$var": "surface"},
         effects=SH_CARD, layout="horizontal", main="center", cross="center", key="logback")
icon("chevron_left", back, size=20, key="logbacki")
F(body, "jarak", h=6, fill="none", key="logsp1")
logo = F(body, "Logo", w=62, h=62, radius=20, fill=GRAD,
         layout="horizontal", main="center", cross="center", effects=SH_BTN, key="loglogo")
icon("check", logo, size=28, sw=3, fill_hex="#FFFFFF", key="loglogoi")
T("Selamat datang\nkembali 👋", body, size=27, style="SemiBold", lh="130%", ls="-2%", name="logjud")
T("Masuk untuk melanjutkan tugasmu hari ini.", body, size=14, color="text-muted",
  lh="150%", name="logsub")
F(body, "jarak2", h=10, fill="none", key="logsp2")
labeled_field(body, "Email", "nama@email.com", key="logem", placeholder=True)
labeled_field(body, "Kata Sandi", "••••••••", key="logpw", placeholder=True, trailing=["eye"])
r = F(body, "Ingat", layout="horizontal", w="fill", main="space-between", cross="center", key="logr")
rc = F(r, "kiri", layout="horizontal", gap=9, cross="center", key="logrc")
F(rc, "cb", w=19, h=19, radius=6, fill={"$var": "primary"}, key="logcb")
T("Ingat saya", rc, size=13, color="text-muted", name="logrc2")
loglupa_ref = T("Lupa kata sandi?", r, size=13, style="SemiBold", color="primary", name="loglupa")
logbtn_ref = button(body, "Masuk", "primary", key="logbtn")
dv = F(body, "Divider", layout="horizontal", w="fill", gap=14, cross="center", key="logdv")
F(dv, "l", h=1, sizingH="fill", fill={"$var": "border"}, key="logdvl")
T("atau", dv, size=12, color="text-muted", name="logdvt")
F(dv, "r", h=1, sizingH="fill", fill={"$var": "border"}, key="logdvr")
logg_ref = btn = F(body, "Google", layout="horizontal", main="center", cross="center", w="fill", h=54,
        radius=27, fill={"$var": "surface"}, stroke={"$var": "border"}, gap=12, key="logg")
gm = F(btn, "G", layout="horizontal", gap=3, key="loggm")
for i, c in enumerate(["#EA4335", "#FBBC05", "#34A853", "#4285F4"]):
    dot(gm, 9, c, key=f"loggd{i}")
T("Lanjutkan dengan Google", btn, size=14.5, style="SemiBold", name="loggt")
logf_ref = row = F(body, "Daftar", layout="horizontal", gap=5, main="center", sizingH="fill", key="logf")
T("Belum punya akun?", row, size=13.5, color="text-muted", name="logf1")
T("Daftar", row, size=13.5, style="SemiBold", color="primary", name="logf2")

# ---- 03 Beranda
home_ref = scr = screen_frame("03 Beranda", 946, key="home")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[2, 24, 112, 24],
         gap=14, key="hb")
hero_card(body, key="hh")
progress_card(body, key="hp")
chips = F(body, "Filter", layout="horizontal", gap=8, w="fill", key="hc")
chip(chips, "Semua", selected=True, key="hc1")
chip(chips, "Pekerjaan", key="hc2")
chip(chips, "Pribadi", key="hc3")
chip(chips, "Belanja", key="hc4")
hs1_ref = section_header(body, "Hari Ini", count=3, key="hs1")
ht1_ref = taskcard(body, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", done=True, key="ht1")
ht2_ref = taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", key="ht2")
ht3_ref = taskcard(body, "Belanja bulanan di pasar", "Belanja", "16:00", "#F79009", key="ht3")
section_header(body, "Besok", count=1, action="Semua", key="hs2")
taskcard(body, "Kontrol dokter gigi", "Kesehatan", "08:30", "#E5484D", key="ht4")
_, hd_refs = dock_bar(scr, "Beranda", key="hd", x=16, y=774)
hfab_ref = fab(scr, key="hfab", x=311, y=698)

# ---- 04 Tugas Baru
add_ref = scr = screen_frame("04 Tugas Baru", 1419, key="add")
statusbar(scr)
bgc = F(scr, "Konten Redup", layout="vertical", w="fill", sizingV="fill", pad=[2, 24],
        gap=14, key="ab", opacity=0.32)
hero_card(bgc, key="ah")
taskcard(bgc, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", done=True, key="at1")
taskcard(bgc, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", key="at2")
sheet = F(scr, "Sheet", layout="vertical", w="fill", radius=[30, 30, 0, 0],
          fill={"$var": "surface"}, pad=[12, 24, 26, 24], gap=14, effects=SH_SHEET, key="asheet")
F(sheet, "Grabber", w=44, h=4.5, radius=999, fill={"$var": "border"},
  main="center", layout="horizontal", sizingH="fill", key="agrab")
r = F(sheet, "Judul", layout="horizontal", w="fill", main="space-between", cross="center", key="ahr")
T("Tugas Baru", r, size=18, style="SemiBold", ls="-1%", name="ah1")
ax_ref = xbtn = F(r, "Tutup", w=34, h=34, radius=999, fill={"$var": "surface-2"},
         layout="horizontal", main="center", cross="center", key="ax")
icon("x", xbtn, size=15, sw=2.2, key="axi")
labeled_field(sheet, "Judul tugas", "Rapat sprint desain", key="aj")
labeled_field(sheet, "Catatan", "Tambahkan catatan (opsional)", key="an", h=64, placeholder=True)
col = F(sheet, "Kategori", layout="vertical", gap=9, sizingH="fill", key="ak")
T("Kategori", col, size=12.5, style="SemiBold", color="text-muted", name="akl")
chips = F(col, "Chips", layout="horizontal", gap=8, sizingH="fill", key="akc")
for i, cat in enumerate(["Pekerjaan", "Pribadi", "Belanja", "Kesehatan"]):
    fg, bg = CAT[cat]
    sel = i == 0
    ch = F(chips, f"K/{cat}", layout="horizontal", gap=5, cross="center", pad=[8, 13],
           radius=999, fill=bg if sel else {"$var": "surface-2"}, key=f"akc{i}")
    dot(ch, 6, fg, key=f"akcd{i}")
    T(cat, ch, size=12.5, style="SemiBold" if sel else "Regular",
      fill_hex=fg if sel else None, color=None if sel else "text-muted", name=f"akcl{i}")
col = F(sheet, "Prioritas", layout="vertical", gap=9, sizingH="fill", key="ap")
T("Prioritas", col, size=12.5, style="SemiBold", color="text-muted", name="apl")
seg = F(col, "Segmen", layout="horizontal", gap=8, sizingH="fill", key="apsg")
for i, (lbl, hexc) in enumerate([("Tinggi", "#E5484D"), ("Sedang", "#F79009"), ("Rendah", "#12B76A")]):
    sel = i == 0
    segc = F(seg, f"S/{lbl}", layout="horizontal", gap=6, main="center", cross="center", h=42,
             radius=14, sizingH="fill",
             fill="#FDEBEB" if sel else {"$var": "surface-2"}, key=f"aps{i}")
    dot(segc, 8, hexc, key=f"apsd{i}")
    T(lbl, segc, size=13, style="SemiBold" if sel else "Regular",
      fill_hex=hexc if sel else None, color=None if sel else "text-muted", name=f"apsl{i}")
r = F(sheet, "Tanggal", layout="horizontal", w="fill", main="space-between", cross="center", key="adt")
tl = F(r, "kiri", layout="vertical", gap=8, key="adtl")
T("Tanggal & waktu", tl, size=12.5, style="SemiBold", color="text-muted", name="adtl0")
tgl = F(tl, "chip", layout="horizontal", gap=8, cross="center", pad=[10, 14], radius=14,
        fill={"$var": "surface-2"}, key="adtch")
icon("calendar", tgl, size=16, color="primary", key="adtci")
T("Besok, 09:00", tgl, size=13, style="SemiBold", name="adtc")
icon("chevron_down", tgl, size=14, color="text-muted", key="adtch2")
rr = F(r, "kanan", layout="vertical", gap=8, cross="max", key="arr")
T("Ingatkan saya", rr, size=12.5, style="SemiBold", color="text-muted", name="arrt")
toggle(rr, True, key="art")
abtn_ref = button(sheet, "Simpan Tugas", "primary", h=54, key="abtn")
F(sheet, "Home Indicator", w=120, h=5, radius=999, fill={"$var": "text-muted"},
  opacity=0.4, layout="horizontal", main="center", sizingH="fill", key="ahi")

# ---- 05 Kalender
cal_ref = scr = screen_frame("05 Kalender", 1892, key="cal")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[2, 24, 112, 24],
         gap=12, key="cb")
r = F(body, "Header", layout="horizontal", w="fill", main="space-between", cross="center", key="chr")
T("November 2026", r, size=19, style="SemiBold", ls="-1%", name="chm")
rr = F(r, "panah", layout="horizontal", gap=8, key="chr2")
for i, icn in enumerate(["chevron_left", "chevron_right"]):
    b = F(rr, f"b{i}", w=36, h=36, radius=999, fill={"$var": "surface"},
          effects=SH_CARD, layout="horizontal", main="center", cross="center", key=f"chb{i}")
    icon(icn, b, size=16, key=f"chbi{i}")
wk = F(body, "Hari", layout="horizontal", w="fill", key="cwk")
for i, dd in enumerate(["MIN", "SEN", "SEL", "RAB", "KAM", "JUM", "SAB"]):
    cell = F(wk, f"w{i}", w=45, h=20, layout="horizontal", main="center", cross="center", key=f"cw{i}")
    T(dd, cell, size=9.5, style="SemiBold", color="text-muted", ls="6%", name=f"cwd{i}")
grid = F(body, "Tanggal", layout="vertical", gap=2, sizingH="fill", key="cgrid")
HAS_TASKS = {5, 8, 10, 12, 13, 16, 19, 23, 26}
day = 1
for rowi in range(5):
    rowf = F(grid, f"g{rowi}", layout="horizontal", gap=2, sizingH="fill", key=f"cg{rowi}")
    for colx in range(7):
        cell = F(rowf, f"c{day}", w=45, h=46, layout="vertical", gap=3, main="center",
                 cross="center", key=f"cc{day}")
        today = day == 13
        if today:
            circ = F(cell, "hari", w=34, h=34, radius=999, fill=GRAD,
                     layout="horizontal", main="center", cross="center", key=f"cd{day}")
            T(str(day), circ, size=13.5, style="SemiBold", fill_hex="#FFFFFF", name=f"ct{day}")
        else:
            T(str(day), cell, size=13, color="text", name=f"ct{day}")
        drow = F(cell, "dots", layout="horizontal", gap=2, main="center", key=f"cdd{day}")
        if day in HAS_TASKS:
            dot(drow, 4, {"$var": "primary"} if today else "#B9B9E8", key=f"cdt{day}")
        day += 1
        if day > 30:
            break
    if day > 30:
        break
cs_ref = section_header(body, "Jumat, 13 November", count=4, action="Semua", key="cs")
ct1_ref = taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", key="ct1")
ct2_ref = taskcard(body, "Review PR aplikasi mobile", "Pekerjaan", "11:30", "#F79009", key="ct2")
ct3_ref = taskcard(body, "Belanja bulanan di pasar", "Belanja", "16:00", "#F79009", key="ct3")
_, cd_refs = dock_bar(scr, "Kalender", key="cd", x=16, y=774)
cfab2_ref = fab(scr, key="cfab2", x=311, y=698)

# ---- 06 Profil
prof_ref = scr = screen_frame("06 Profil", 2365, key="prof")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[2, 24, 112, 24],
         gap=14, key="pb")
T("Profil", body, size=19, style="SemiBold", ls="-1%", name="pt")
hero = F(body, "Kartu Profil", layout="horizontal", w="fill", radius=24, fill=GRAD,
         pad=[20, 20], gap=14, cross="center", effects=SH_BTN, key="phero")
av = F(hero, "Avatar", w=60, h=60, radius=999, fill="#FFFFFF2E",
       layout="horizontal", main="center", cross="center", key="pav")
T("RP", av, size=20, style="SemiBold", fill_hex="#FFFFFF", name="pavt")
pcol = F(hero, "nama", layout="vertical", gap=4, sizingH="fill", key="pcol")
T("Rian Pratama", pcol, size=17, style="SemiBold", fill_hex="#FFFFFF", ls="-1%", name="pname")
T("rian.pratama@mail.com", pcol, size=12, fill_hex="#FFFFFFB0", name="pmail")
ppill = F(pcol, "pro", layout="horizontal", gap=5, cross="center", pad=[5, 11], radius=999,
          fill="#FFFFFF2E", key="ppill")
icon("star", ppill, size=12, fill_hex="#FFD66B", key="ppilli")
T("PAKET PRO", ppill, size=9.5, style="SemiBold", fill_hex="#FFFFFF", ls="8%", name="ppilll")
stats = F(body, "Statistik", layout="horizontal", gap=10, sizingH="fill", key="pst")
for i, (val, lbl) in enumerate([("128", "SELESAI"), ("12", "HARI STREAK"), ("87", "SKOR FOKUS")]):
    st = F(stats, f"S/{lbl}", layout="vertical", gap=5, cross="center", main="center",
           radius=18, pad=[14, 0], sizingH="fill", fill={"$var": "surface"},
           effects=SH_CARD, key=f"pst{i}")
    T(val, st, size=19, style="Bold", color="primary", ls="-1%", name=f"psv{i}")
    T(lbl, st, size=9, style="SemiBold", color="text-muted", ls="7%", name=f"psl{i}")
T("Pengaturan", body, size=16.5, style="SemiBold", ls="-1%", name="pset")
listcard = F(body, "Daftar", layout="vertical", w="fill", radius=20,
             fill={"$var": "surface"}, effects=SH_CARD, key="plist")
rows = [("bell", "Notifikasi", "toggle", True),
        ("moon", "Tema Gelap", "toggle", False),
        ("sliders", "Sinkronisasi", "chev", None),
        ("logout", "Bantuan & Masukan", "chev", None)]
for i, (icn, lbl, kind, ton) in enumerate(rows):
    r = F(listcard, f"R/{lbl}", layout="horizontal", w="fill", h=54, pad=[0, 16],
          cross="center", main="space-between", key=f"pr{i}")
    rr = F(r, "kiri", layout="horizontal", gap=12, cross="center", key=f"prl{i}")
    ic = F(rr, "ikon", w=32, h=32, radius=11, fill={"$var": "surface-2"},
           layout="horizontal", main="center", cross="center", key=f"pri{i}")
    icon(icn, ic, size=16, color="text-muted", key=f"pric{i}")
    T(lbl, rr, size=14, name=f"prt{i}")
    if kind == "toggle":
        toggle(r, ton, key=f"prtg{i}")
    else:
        icon("chevron_right", r, size=16, color="text-muted", key=f"prc{i}")
    if i < len(rows) - 1:
        F(listcard, "divider", h=1, sizingH="fill", fill={"$var": "border"}, key=f"pd{i}")
pout_ref = button(body, "Keluar", "danger", h=52, key="pout")
_, pd_refs = dock_bar(scr, "Profil", key="pd", x=16, y=774)

# ---- 07 Statistik
stat_ref = scr = screen_frame("07 Statistik", 2838, key="stat")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[2, 24, 112, 24],
         gap=14, key="stb")
T("Statistik", body, size=19, style="SemiBold", ls="-1%", name="stt")
chips = F(body, "Periode", layout="horizontal", gap=8, w="fill", key="stc")
chip(chips, "Harian", selected=True, key="stc1")
chip(chips, "Mingguan", key="stc2")
chip(chips, "Bulanan", key="stc3")
ringc = F(body, "RingCard", layout="horizontal", w="fill", radius=20,
          fill={"$var": "surface"}, pad=[18, 20], gap=18, cross="center",
          effects=SH_CARD, key="string")
ring(ringc, 37, key="stringr", size=92, lblsize=15)
scol = F(ringc, "info", layout="vertical", gap=5, sizingH="fill", key="stcol")
micro(scol, "Progres hari ini", key="stm")
T("3 dari 8 tugas", scol, size=17, style="SemiBold", ls="-1%", name="stv")
T("+12% dari kemarin", scol, size=11.5, style="SemiBold", color="success", name="std")
ach = F(body, "Aktivitas", layout="vertical", w="fill", radius=20,
        fill={"$var": "surface"}, pad=[16, 18], gap=12, effects=SH_CARD, key="stach")
ahr = F(ach, "kepala", layout="horizontal", w="fill", main="space-between", cross="center", key="stahr")
T("Aktivitas 7 Hari", ahr, size=14.5, style="SemiBold", name="staht")
apill = F(ahr, "hitung", layout="horizontal", pad=[3, 9], radius=999,
          fill={"$var": "primary-soft"}, key="stahp")
T("28 tugas", apill, size=11, style="SemiBold", color="primary", name="stahpl")
arow = F(ach, "Grafik", layout="horizontal", w="fill", h=118, gap=10, cross="max", key="staar")
BAR_VALS = [5, 7, 4, 8, 6, 3, 7]
for bi, v in enumerate(BAR_VALS):
    today_bar = bi == 4
    F(arow, f"bar{bi}", sizingH="fill", h=v * 13, radius=8,
      fill=GRAD if today_bar else {"$var": "primary-soft"}, key=f"stab{bi}")
alab = F(ach, "Label", layout="horizontal", w="fill", gap=10, key="stal")
for bi, d in enumerate(["SEN", "SEL", "RAB", "KAM", "JUM", "SAB", "MIN"]):
    lc = F(alab, f"l{bi}", layout="horizontal", main="center", sizingH="fill", key=f"stal{bi}")
    T(d, lc, size=9, style="SemiBold" if bi == 4 else "Regular",
      color="primary" if bi == 4 else "text-muted", ls="4%", name=f"stald{bi}")
kac = F(body, "Kategori", layout="vertical", w="fill", radius=20,
        fill={"$var": "surface"}, pad=[16, 18], gap=12, effects=SH_CARD, key="stkc")
khr = F(kac, "kepala", layout="horizontal", w="fill", main="space-between", cross="center", key="stkhr")
T("Berdasarkan Kategori", khr, size=14.5, style="SemiBold", name="stkht")
T("Bulan ini", khr, size=11, color="text-muted", name="stkhs")
for ki, (nm, hexc, n, total) in enumerate([("Pekerjaan", "#5B54F0", 12, 28), ("Pribadi", "#0E9F6E", 8, 28),
                                           ("Belanja", "#DC8A0E", 5, 28), ("Kesehatan", "#E5484D", 3, 28)]):
    kr = F(kac, f"K/{nm}", layout="horizontal", gap=9, cross="center", w="fill", key=f"stkr{ki}")
    dot(kr, 9, hexc, key=f"stkd{ki}")
    T(nm, kr, size=13.5, name=f"stkl{ki}")
    F(kr, "spacer", sizingH="fill", h=1, key=f"stks{ki}")
    ktr = F(kr, "Track", layout="horizontal", w=72, h=5, radius=999, fill={"$var": "surface-2"}, key=f"stktr{ki}")
    F(ktr, "Fill", w=round(72 * n / total), h=5, radius=999, fill=hexc, key=f"stkf{ki}")
    T(str(n), kr, size=12, style="SemiBold", color="text-muted", name=f"stkn{ki}")
_, sd_refs = dock_bar(scr, "Statistik", key="sd", x=16, y=774)
sfab_ref = fab(scr, key="sfab", x=311, y=698)

# ---- 08 Beranda Gelap (duplikat 03)
dup_ref = S("edit.duplicate", {"ids": [home_ref], "dx": 473 * 7, "dy": 0}, as_name="darkdup")
dark_id = {**dup_ref, "field": "ids/0"}
S("object.rename", {"ids": [dark_id], "name": "08 Beranda — Gelap"})
S("variable.setMode", {"ids": [dark_id], "collection": "Warna", "mode": "Gelap"})

# ---- 09 Beranda — FAB Terbuka (speed dial)
sfx_ref = scr = screen_frame("09 Beranda — FAB Terbuka", 3784, key="sfx")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[2, 24], gap=14, key="sfb")
hero_card(body, key="sfh")
taskcard(body, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", done=True, key="sft1")
taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", key="sft2")
_, sfd_refs = dock_bar(scr, "Beranda", key="sfd", x=16, y=774)
sfscr_ref = F(scr, "Scrim", w=PHONE_W, h=PHONE_H, fill="#13131966", absolute=True, x=0, y=0, key="sfscr")
ACTIONS = [("Pengingat", "bell", False), ("Kategori Baru", "tag", False), ("Tugas Baru", "plus", True)]
sfx_rows = []
for i, (lbl, icn, prim) in enumerate(ACTIONS):
    row = F(scr, f"Aksi/{lbl}", layout="horizontal", gap=10, cross="center", main="max",
            w=329, h=48, absolute=True, x=40, y=512 + i * 62, key=f"sfxr{i}")
    sfx_rows.append(row)
    pill = F(row, "Label", layout="horizontal", pad=[9, 14], radius=999,
             fill={"$var": "surface"}, effects=SH_CARD, key=f"sfxp{i}")
    T(lbl, pill, size=12.5, style="SemiBold",
      color="primary" if prim else "text", name=f"sfxl{i}")
    circ = F(row, "Tombol", w=48, h=48, radius=999,
             fill={"$var": "primary"} if prim else {"$var": "surface"},
             layout="horizontal", main="center", cross="center", effects=SH_FLOAT, key=f"sfdc{i}")
    if prim:
        icon(icn, circ, size=20, sw=2.5, fill_hex="#FFFFFF", key=f"sfxi{i}")
    else:
        icon(icn, circ, size=20, color="text", key=f"sfxi{i}")
sffab_ref = fab(scr, key="sffab", x=311, y=698, ic="x")

# ---- 10 Kategori Baru (sheet)
kat_ref = scr = screen_frame("10 Kategori Baru", 4257, key="kat")
statusbar(scr)
bgc = F(scr, "Konten Redup", layout="vertical", w="fill", sizingV="fill", pad=[2, 24],
        gap=14, key="kb", opacity=0.32)
hero_card(bgc, key="kh")
taskcard(bgc, "Belanja bulanan di pasar", "Belanja", "16:00", "#F79009", key="kt1")
sheet = F(scr, "Sheet", layout="vertical", w="fill", radius=[30, 30, 0, 0],
          fill={"$var": "surface"}, pad=[12, 24, 26, 24], gap=14, effects=SH_SHEET, key="ksheet")
F(sheet, "Grabber", w=44, h=4.5, radius=999, fill={"$var": "border"},
  main="center", layout="horizontal", sizingH="fill", key="kgrab")
r = F(sheet, "Judul", layout="horizontal", w="fill", main="space-between", cross="center", key="khr")
T("Kategori Baru", r, size=18, style="SemiBold", ls="-1%", name="kh1")
kx_ref = xbtn = F(r, "Tutup", w=34, h=34, radius=999, fill={"$var": "surface-2"},
                  layout="horizontal", main="center", cross="center", key="kx")
icon("x", xbtn, size=15, sw=2.2, key="kxi")
labeled_field(sheet, "Nama kategori", "Belanja mingguan", key="kf")
col = F(sheet, "Warna", layout="vertical", gap=9, sizingH="fill", key="kw")
T("Warna", col, size=12.5, style="SemiBold", color="text-muted", name="kwl")
crows = F(col, "Dots", layout="horizontal", gap=12, cross="center", sizingH="fill", key="kwd")
for i, hexc in enumerate(["#5B54F0", "#0E9F6E", "#DC8A0E", "#E5484D", "#0E7490"]):
    sel = i == 2
    if sel:
        ringw = F(crows, f"p{i}", w=36, h=36, radius=999, layout="horizontal",
                  main="center", cross="center", stroke=hexc, sw=2, pad=[4], key=f"kwp{i}")
        dot(ringw, 22, hexc, key=f"kwdot{i}")
    else:
        dot(crows, 28, hexc, key=f"kwdot{i}")
col = F(sheet, "Pratinjau", layout="vertical", gap=9, sizingH="fill", key="kp")
T("Pratinjau", col, size=12.5, style="SemiBold", color="text-muted", name="kpl")
prev = F(col, "Chip", layout="horizontal", gap=6, cross="center", pad=[10, 16], radius=999,
         fill="#FDF2E1", key="kprev")
dot(prev, 8, "#DC8A0E", key="kprevd")
T("Belanja mingguan", prev, size=13.5, style="SemiBold", fill_hex="#DC8A0E", name="kprevl")
kbtn_ref = button(sheet, "Simpan Kategori", "primary", h=54, key="kbtn")
F(sheet, "Home Indicator", w=120, h=5, radius=999, fill={"$var": "text-muted"},
  opacity=0.4, layout="horizontal", main="center", sizingH="fill", key="khi")

# ---- 11 Pengingat Cepat (sheet)
rem_ref = scr = screen_frame("11 Pengingat Cepat", 4730, key="rem")
statusbar(scr)
bgc = F(scr, "Konten Redup", layout="vertical", w="fill", sizingV="fill", pad=[2, 24],
        gap=14, key="rb", opacity=0.32)
hero_card(bgc, key="rh")
taskcard(bgc, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", key="rt1")
sheet = F(scr, "Sheet", layout="vertical", w="fill", radius=[30, 30, 0, 0],
          fill={"$var": "surface"}, pad=[12, 24, 26, 24], gap=14, effects=SH_SHEET, key="rsheet")
F(sheet, "Grabber", w=44, h=4.5, radius=999, fill={"$var": "border"},
  main="center", layout="horizontal", sizingH="fill", key="rgrab")
r = F(sheet, "Judul", layout="horizontal", w="fill", main="space-between", cross="center", key="rhr")
T("Pengingat Cepat", r, size=18, style="SemiBold", ls="-1%", name="rh1")
px_ref = xbtn = F(r, "Tutup", w=34, h=34, radius=999, fill={"$var": "surface-2"},
                  layout="horizontal", main="center", cross="center", key="rx")
icon("x", xbtn, size=15, sw=2.2, key="rxi")
labeled_field(sheet, "Pengingat", "Minum air putih", key="rf")
col = F(sheet, "Waktu", layout="vertical", gap=8, sizingH="fill", key="rw")
T("Waktu", col, size=12.5, style="SemiBold", color="text-muted", name="rwl")
tgl = F(col, "chip", layout="horizontal", gap=8, cross="center", pad=[11, 14], radius=14,
        fill={"$var": "surface-2"}, key="rwch")
icon("calendar", tgl, size=16, color="primary", key="rwci")
T("Hari ini, 17:00", tgl, size=13, style="SemiBold", name="rwc")
icon("chevron_down", tgl, size=14, color="text-muted", key="rwcch")
col = F(sheet, "Ulangi", layout="vertical", gap=9, sizingH="fill", key="ru")
T("Ulangi", col, size=12.5, style="SemiBold", color="text-muted", name="rul")
rch = F(col, "Chips", layout="horizontal", gap=8, sizingH="fill", key="ruch")
for i, lbl in enumerate(["Sekali", "Harian", "Mingguan"]):
    chip(rch, lbl, selected=(i == 0), key=f"ruc{i}")
r = F(sheet, "Notifikasi", layout="horizontal", w="fill", main="space-between", cross="center", key="rnr")
rl = F(r, "kiri", layout="horizontal", gap=10, cross="center", key="rnrl")
icon("bell", rl, size=18, color="text-muted", key="rnri")
T("Notifikasi pengingat", rl, size=14, name="rnrt")
toggle(r, True, key="rnt")
pbtn_ref = button(sheet, "Atur Pengingat", "primary", h=54, key="pbtn")
F(sheet, "Home Indicator", w=120, h=5, radius=999, fill={"$var": "text-muted"},
  opacity=0.4, layout="horizontal", main="center", sizingH="fill", key="rhi")

# ================================================================ HALAMAN 3: RESPONSIVE
p3 = S("page.add", {"name": "🖥️ Responsive"}, as_name="p3")
S("page.select", {"id": p3})

# ---- Tablet 744×1133
tab = F(None, "Beranda — Tablet", w=744, h=1133, fill={"$var": "bg"},
        layout="vertical", clip=True, x=0, y=0, key="tab")
statusbar(tab)
tmain = F(tab, "Utama", layout="vertical", w="fill", sizingV="fill", pad=[6, 28, 118, 28], gap=16, key="tm")
r = F(tmain, "Header", layout="horizontal", w="fill", main="space-between", cross="center", key="tmh")
gcol = F(r, "Judul", layout="vertical", gap=4, key="tmhc")
T("Halo, Rian 👋", gcol, size=24, style="SemiBold", ls="-1.5%", name="tmh1")
T("Jumat, 13 November 2026", gcol, size=13, color="text-muted", name="tmh2")
tms_ref = srch = F(r, "Cari", layout="horizontal", gap=10, cross="center", w=230, h=44, radius=999,
         fill={"$var": "surface-2"}, pad=[0, 16], key="tms")
icon("search", srch, size=16, color="text-muted", key="tmsi")
T("Cari tugas…", srch, size=13, color="text-muted", name="tmst")
hero_card(tmain, key="tmhero", wide=True)
progress_card(tmain, key="tmprog")
chips = F(tmain, "Filter", layout="horizontal", gap=8, sizingH="fill", key="tmc")
chip(chips, "Semua", selected=True, key="tmc1")
chip(chips, "Pekerjaan", key="tmc2")
chip(chips, "Pribadi", key="tmc3")
chip(chips, "Belanja", key="tmc4")
chip(chips, "Kesehatan", key="tmc5")
gridw = F(tmain, "Tugas", layout="vertical", gap=12, sizingH="fill", sizingV="fill", key="tmg")
gr = F(gridw, "Baris1", layout="horizontal", gap=12, sizingH="fill", key="tmg1")
boxa = F(gr, "A", layout="horizontal", sizingH="fill", key="tmg1a")
taskcard(boxa, "Rapat sprint tim desain", "Pekerjaan", "09:00", "#E5484D", key="tmt1")
boxb = F(gr, "B", layout="horizontal", sizingH="fill", key="tmg1b")
taskcard(boxb, "Belanja bulanan di pasar", "Belanja", "16:00", "#F79009", key="tmt2")
gr = F(gridw, "Baris2", layout="horizontal", gap=12, sizingH="fill", key="tmg2")
boxc = F(gr, "C", layout="horizontal", sizingH="fill", key="tmg2a")
taskcard(boxc, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", done=True, key="tmt3")
boxd = F(gr, "D", layout="horizontal", sizingH="fill", key="tmg2b")
taskcard(boxd, "Olahraga pagi: lari 5 km", "Pribadi", "06:00", "#12B76A", key="tmt4")
dock_bar(tab, "Beranda", key="td", x=112, y=1055, w=520)
fab(tab, key="tfab", x=662, y=984)

# ---- Desktop 1440×1024
desk = F(None, "Beranda — Desktop", w=1440, h=1024, fill={"$var": "bg"},
         layout="horizontal", clip=True, x=844, y=0, key="desk")
side = F(desk, "Sidebar", layout="vertical", w=272, sizingV="fill", pad=24, gap=10,
         fill={"$var": "surface"}, stroke={"$var": "border"}, sw=1, key="dside")
logo = F(side, "Logo", layout="horizontal", gap=11, cross="center", pad=[2, 2, 14, 2], key="dlogo")
mark = F(logo, "m", w=42, h=42, radius=14, fill=GRAD,
         layout="horizontal", main="center", cross="center", key="dlogom")
icon("check", mark, size=22, sw=3, fill_hex="#FFFFFF", key="dlogoi")
T("TaskKu", logo, size=21, style="Bold", ls="-1%", name="dlogot")
for i, (icn, lbl, act) in enumerate([("home", "Beranda", True), ("calendar", "Kalender", False),
                                     ("chart", "Statistik", False)]):
    it = F(side, f"M/{lbl}", layout="horizontal", gap=12, cross="center", w="fill", h=46,
           radius=14, pad=[0, 14], fill={"$var": "primary-soft"} if act else "none", key=f"dm{i}")
    icon(icn, it, size=19, color="primary" if act else "text-muted", key=f"dmi{i}")
    T(lbl, it, size=14.5, style="SemiBold" if act else "Regular",
      color="primary" if act else "text", name=f"dml{i}")
T("PROYEK", side, size=9.5, style="SemiBold", color="text-muted", ls="8%", name="dproj", width=220)
for i, (nm, hexc, n) in enumerate([("Pekerjaan", "#5B54F0", 12), ("Pribadi", "#0E9F6E", 8),
                                   ("Belanja", "#DC8A0E", 5), ("Kesehatan", "#E5484D", 3)]):
    it = F(side, f"P/{nm}", layout="horizontal", gap=10, cross="center", w="fill", h=40,
           radius=12, pad=[0, 14], key=f"dp{i}")
    dot(it, 9, hexc, key=f"dpd{i}")
    T(nm, it, size=13.5, name=f"dpl{i}", width=None)
    pill = F(it, "n", layout="horizontal", pad=[2, 8], radius=999,
             fill={"$var": "surface-2"}, key=f"dpn{i}")
    T(str(n), pill, size=11, style="SemiBold", color="text-muted", name=f"dpnl{i}")
prog = F(side, "Progres", layout="vertical", gap=10, w=224, radius=16, pad=16,
         fill={"$var": "surface-2"}, absolute=True, x=24, y=848, key="dprog")
micro(prog, "Progres", key="dprogm")
for pi, (plbl, pval, ppct) in enumerate([("HARI INI", "3/8", 37), ("MINGGU INI", "24/40", 60),
                                         ("BULAN INI", "96/140", 69)]):
    pc = F(prog, f"P/{plbl}", layout="vertical", gap=5, w="fill", key=f"dpp{pi}")
    pr = F(pc, "atas", layout="horizontal", w="fill", main="space-between", cross="center", key=f"dppr{pi}")
    T(plbl, pr, size=9.5, style="SemiBold", color="text-muted", ls="7%", name=f"dppl{pi}")
    T(pval, pr, size=11.5, style="SemiBold", name=f"dppv{pi}")
    ptr = F(pc, "Track", layout="horizontal", w="fill", h=5, radius=999, fill={"$var": "border"}, key=f"dpptr{pi}")
    F(ptr, "Fill", w=round(192 * ppct / 100), h=5, radius=999, fill={"$var": "primary"}, key=f"dppf{pi}")
dmain = F(desk, "Utama", layout="vertical", sizingH="fill", sizingV="fill", pad=[30], gap=22, key="dmn")
top = F(dmain, "Atas", layout="horizontal", w="fill", main="space-between", cross="center", key="dtop")
tcol = F(top, "Judul", layout="vertical", gap=5, key="dtopc")
T("Hari Ini", tcol, size=27, style="SemiBold", ls="-2%", name="dtop1")
T("Jumat, 13 November 2026 — 5 tugas aktif, 3 selesai", tcol, size=13.5, color="text-muted", name="dtop2")
tright = F(top, "kanan", layout="horizontal", gap=10, cross="center", key="dtr")
dsrch_ref = srch = F(tright, "Cari", layout="horizontal", gap=10, cross="center", w=330, h=46, radius=999,
         fill={"$var": "surface-2"}, pad=[0, 16], key="dsrch")
icon("search", srch, size=16, color="text-muted", key="dsrchi")
T("Cari tugas, kategori, atau catatan…", srch, size=13, color="text-muted", name="dsrcht")
bellb = F(tright, "Notif", w=46, h=46, radius=999, fill={"$var": "surface"},
          effects=SH_CARD, layout="horizontal", main="center", cross="center", key="dbell")
icon("bell", bellb, size=18, key="dbelli")
av = F(tright, "Avatar", w=46, h=46, radius=999, fill=GRAD,
       layout="horizontal", main="center", cross="center", key="dav")
T("R", av, size=16, style="SemiBold", fill_hex="#FFFFFF", name="davt")
icon("chevron_down", tright, size=14, color="text-muted", key="davc")
dd = F(desk, "Dropdown Profil", layout="vertical", w=264, radius=16,
       fill={"$var": "surface"}, stroke={"$var": "border"}, effects=SH_FLOAT,
       pad=[10, 10, 12, 10], gap=4, absolute=True, x=1146, y=88, key="ddd")
dh = F(dd, "Kepala", layout="horizontal", gap=10, cross="center", w="fill",
       pad=[8, 8, 12, 8], key="ddh")
dav = F(dh, "Avatar", w=40, h=40, radius=999, fill=GRAD,
        layout="horizontal", main="center", cross="center", key="ddh av".replace(" ", ""))
T("R", dav, size=14, style="SemiBold", fill_hex="#FFFFFF", name="ddhi")
dhc = F(dh, "nama", layout="vertical", gap=2, sizingH="fill", key="ddhc")
T("Rian Pratama", dhc, size=13.5, style="SemiBold", name="ddhn")
T("rian.pratama@mail.com", dhc, size=10.5, color="text-muted", name="ddhe")
F(dd, "divider", h=1, w="fill", fill={"$var": "border"}, key="dddv")
for i, (icn, lbl, danger) in enumerate([("user", "Lihat Profil", False), ("logout", "Keluar", True)]):
    mi = F(dd, f"Menu/{lbl}", layout="horizontal", gap=10, cross="center", w="fill", h=40,
           radius=10, pad=[0, 10], key=f"ddm{i}")
    icon(icn, mi, size=16, color="danger" if danger else "text-muted", key=f"ddmi{i}")
    T(lbl, mi, size=13.5, style="SemiBold" if danger else "Regular",
      color="danger" if danger else "text", name=f"ddml{i}")
kanban = F(dmain, "Kanban", layout="horizontal", gap=14, sizingH="fill", sizingV="fill", key="dkan")
cols = [("Hari Ini", "#5B54F0", [("Kirim laporan mingguan", "Pekerjaan", "08:00", True),
                                 ("Rapat sprint dengan tim desain", "Pekerjaan", "09:00", False),
                                 ("Belanja bulanan di pasar", "Belanja", "16:00", False)]),
        ("Terjadwal", "#F79009", [("Kontrol dokter gigi", "Kesehatan", "Besok 08:30", False),
                                  ("Olahraga pagi: lari 5 km", "Pribadi", "Besok 06:00", False),
                                  ("Review PR aplikasi mobile", "Pekerjaan", "Besok 11:30", False)]),
        ("Selesai", "#12B76A", [("Setor sampah & pilah", "Pribadi", "07:00", True),
                                ("Bayar tagihan internet", "Belanja", "10:00", True)])]
for ci, (title, dotc, cards) in enumerate(cols):
    col = F(kanban, f"Kolom/{title}", layout="vertical", gap=10, sizingH="fill", sizingV="fill",
            radius=20, fill={"$var": "surface-2"}, pad=12, key=f"dkc{ci}")
    head = F(col, "Judul", layout="horizontal", w="fill", gap=8, cross="center",
             pad=[4, 8], key=f"dkh{ci}")
    dot(head, 10, dotc, key=f"dkd{ci}")
    T(title, head, size=14.5, style="SemiBold", name=f"dkhl{ci}")
    pill = F(head, "hitung", layout="horizontal", pad=[2, 9], radius=999,
             fill={"$var": "surface"}, key=f"dkp{ci}")
    T(str(len(cards)), pill, size=11, style="SemiBold", color="text-muted", name=f"dkpl{ci}")
    icon("plus", head, size=16, color="text-muted", key=f"dkplus{ci}")
    for ki, (t, c, tm, dn) in enumerate(cards):
        taskcard(col, t, c, tm, dotc, done=dn, key=f"dk{ci}{ki}")

# ---- Tablet kecil 600×1024 (kelas tablet terkecil)
stab = F(None, "Beranda — Tablet Kecil", w=600, h=1024, fill={"$var": "bg"},
         layout="vertical", clip=True, x=844, y=1124, key="stab")
statusbar(stab)
smain = F(stab, "Utama", layout="vertical", w="fill", sizingV="fill", pad=[6, 24, 112, 24], gap=16, key="smn")
r = F(smain, "Header", layout="horizontal", w="fill", main="space-between", cross="center", key="smh")
gcol = F(r, "Judul", layout="vertical", gap=4, key="smhc")
T("Halo, Rian 👋", gcol, size=22, style="SemiBold", ls="-1.5%", name="smh1")
T("Jumat, 13 November 2026", gcol, size=12.5, color="text-muted", name="smh2")
sms_ref = srch = F(r, "Cari", layout="horizontal", gap=10, cross="center", w=190, h=42, radius=999,
         fill={"$var": "surface-2"}, pad=[0, 16], key="sms")
icon("search", srch, size=16, color="text-muted", key="smsi")
T("Cari…", srch, size=13, color="text-muted", name="smst")
hero_card(smain, key="smhero", wide=True)
progress_card(smain, key="smprog")
chips = F(smain, "Filter", layout="horizontal", gap=8, sizingH="fill", key="smc")
chip(chips, "Semua", selected=True, key="smc1")
chip(chips, "Pekerjaan", key="smc2")
chip(chips, "Pribadi", key="smc3")
chip(chips, "Belanja", key="smc4")
chip(chips, "Kesehatan", key="smc5")
for i, (t, c, tm, pr, dn) in enumerate([
        ("Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A", True),
        ("Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#E5484D", False),
        ("Belanja bulanan di pasar", "Belanja", "16:00", "#F79009", False),
        ("Kontrol dokter gigi", "Kesehatan", "Besok 08:30", "#E5484D", False)]):
    taskcard(smain, t, c, tm, pr, done=dn, key=f"smt{i}")
dock_bar(stab, "Beranda", key="sd", x=70, y=946, w=460)
fab(stab, key="sfab", x=518, y=874)

# ---- Anotasi aturan responsive
note = F(None, "Aturan Responsive", w=700, radius=16, fill={"$var": "surface"},
         stroke={"$var": "border"}, layout="vertical", pad=[18, 22], gap=10,
         x=0, y=1190, key="rnote")
T("Aturan Responsive", note, size=15, style="SemiBold", name="rnt")
T("\u2022  < 600px (ponsel): bottom nav mengambang, daftar 1 kolom; tombol Keluar ada di halaman Profil.",
  note, size=12.5, color="text-muted", lh="150%", width=650, name="rn1")
T("\u2022  600\u20131023px (tablet kecil\u2013besar): bottom nav mengambang; daftar 1 kolom di bawah 720px, 2 kolom mulai 720px; Keluar tetap di halaman Profil.",
  note, size=12.5, color="text-muted", lh="150%", width=650, name="rn2")
T("\u2022  \u2265 1024px (desktop): navigasi sidebar; Profil & Keluar ada di dropdown avatar pada header; halaman Profil tanpa tombol Keluar.",
  note, size=12.5, color="text-muted", lh="150%", width=650, name="rn3")

# ================================================================ HALAMAN 4: HANDOFF
p4 = S("page.add", {"name": "\U0001F4D0 Handoff"}, as_name="p4")
S("page.select", {"id": p4})
hsp = F(None, "Spasi & Radius", w=1100, radius=24, fill={"$var": "surface"},
        layout="vertical", pad=[28, 32], gap=20, x=0, y=0, key="hsp")
T("Spasi & Radius", hsp, size=20, style="SemiBold", ls="-1%", name="hsp1")
T("Grid 4pt — semua jarak kelipatan 4. Radius: kartu 20, sheet 30, tombol pill, chip 999.",
  hsp, size=13, color="text-muted", name="hsp2")
srow = F(hsp, "Skala", layout="horizontal", gap=18, w="fill", key="hsp3")
for i, v in enumerate([4, 8, 12, 16, 20, 24, 28, 32]):
    it = F(srow, f"s{v}", layout="vertical", gap=6, cross="center", key=f"hsps{i}")
    F(it, "sq", w=v, h=v, radius=4, fill={"$var": "primary-soft"}, key=f"hspsq{i}")
    T(f"{v}pt", it, size=10.5, color="text-muted", name=f"hspl{i}")
rrow = F(hsp, "Radius", layout="horizontal", gap=18, w="fill", key="hsp4")
for i, (v, lbl) in enumerate([(10, "10"), (14, "14"), (16, "16"), (20, "20"), (26, "26"), (999, "pill")]):
    it = F(rrow, f"r{lbl}", layout="vertical", gap=6, key="hspr%s" % i)
    F(it, "rc", w=120, h=64, radius=v if v != 999 else 32, fill={"$var": "surface-2"},
      stroke={"$var": "border"}, key="hsprc%s" % i)
    T(lbl, it, size=10.5, color="text-muted", name="hsprl%s" % i)
mot = F(None, "Motion & Aksesibilitas", w=1100, radius=24, fill={"$var": "surface"},
        layout="vertical", pad=[28, 32], gap=14, x=0, y=430, key="hmot")
T("Motion & Aksesibilitas", mot, size=20, style="SemiBold", ls="-1%", name="hmot1")
for i, txt in enumerate(["Navigasi antar layar — dissolve 250ms easeOut",
                         "Bottom sheet — slideIn dari bawah 300ms",
                         "Speed dial FAB — smartAnimate 250ms"]):
    r = F(mot, f"m{i}", layout="horizontal", gap=10, w="fill", cross="center", key=f"hmotr{i}")
    dot(r, 8, {"$var": "primary"}, key=f"hmotd{i}")
    T(txt, r, size=14, name=f"hmott{i}")
F(mot, "divider", h=1, w="fill", fill={"$var": "border"}, key="hmotdv")
for i, txt in enumerate(["Target sentuh minimal 44\u00d744px",
                         "Kontras teks body \u2265 4.5:1 (token text di atas bg)",
                         "Ikon stroke 2px pada ukuran 16/20/24"]):
    r = F(mot, f"a{i}", layout="horizontal", gap=10, w="fill", cross="center", key=f"hmota{i}")
    dot(r, 8, {"$var": "success"}, key=f"hmota{i}d")
    T(txt, r, size=14, name=f"hmota{i}t")
strw = F(None, "Struktur & Gaya File", w=1100, radius=24, fill={"$var": "surface"},
         layout="vertical", pad=[28, 32], gap=14, x=0, y=860, key="hstr")
T("Struktur & Gaya File", strw, size=20, style="SemiBold", ls="-1%", name="hstr1")
for i, txt in enumerate([
        "Halaman: \U0001F3A8 Design System \u2022 \U0001F4F1 Screens (21 layar) \u2022 \U0001F5A5\ufe0f Responsive (4 artefak) \u2022 \U0001F4D0 Handoff (halaman ini)",
        "Koleksi variabel Warna — 12 token \u00d7 mode Terang/Gelap",
        "12 paint styles (Warna/*) terikat variabel \u2022 7 text styles (Teks/*)",
        "Component set: TaskCard (State), Chip (State), Checkbox (State), Button (Type), Input (State)",
        "71 interaksi prototyping \u2014 mulai present dari layar 01 Onboarding"]):
    r = F(strw, f"s{i}", layout="horizontal", gap=10, w="fill", cross="center", key=f"hstrr{i}")
    dot(r, 8, {"$var": "warning"}, key=f"hstrd{i}")
    T(txt, r, size=14, lh="145%", name=f"hstrt{i}")

# ================================================================ PROTOTYPING
_pn = [0]


def nav(a, b, key="nav"):
    _pn[0] += 1
    return S("proto.interaction.add",
             {"id": a, "action": {"type": "navigate", "dest": b},
              "transition": {"type": "dissolve"}, "durationMs": 250},
             as_name=f"{key}_{_pn[0]}")


# Onboarding -> Masuk -> Beranda
nav(onbbtn_ref, log_ref); nav(onbmasuk_ref, log_ref)
nav(logbtn_ref, home_ref); nav(logg_ref, home_ref)
# Beranda: dock & FAB
nav(hd_refs[1], cal_ref); nav(hd_refs[2], stat_ref); nav(hd_refs[3], prof_ref)
nav(hfab_ref, sfx_ref)
# FAB terbuka: aksi & tutup
nav(sfx_rows[2], add_ref); nav(sfx_rows[1], kat_ref); nav(sfx_rows[0], rem_ref)
nav(sffab_ref, home_ref); nav(sfscr_ref, home_ref)
# Sheet tugas
nav(ax_ref, home_ref); nav(abtn_ref, home_ref)
# Kalender
nav(cd_refs[0], home_ref); nav(cd_refs[2], stat_ref); nav(cd_refs[3], prof_ref)
nav(cfab2_ref, sfx_ref)
# Statistik
nav(sd_refs[0], home_ref); nav(sd_refs[1], cal_ref); nav(sd_refs[3], prof_ref)
nav(sfab_ref, sfx_ref)
# Profil: dock + keluar (logout ke onboarding)
nav(pd_refs[0], home_ref); nav(pd_refs[1], cal_ref); nav(pd_refs[2], stat_ref)
nav(pout_ref, onb_ref)
# Sheet kategori & pengingat
nav(kx_ref, sfx_ref); nav(kbtn_ref, home_ref)
nav(px_ref, sfx_ref); nav(pbtn_ref, home_ref)

# ---------------------------------------------------------------- tulis
with open(OUT, "w") as f:
    json.dump(cmds, f, ensure_ascii=False)
print(f"{len(cmds)} perintah -> {OUT}")
