#!/usr/bin/env python3
"""figkit — helper untuk membangun layar TaskKu di FigCraft secara programatik.

Dipakai modul fragmen (frag_*.py): buat Kit(prefix), bangun layar, lalu
build() mengembalikan (cmds, refs). Lihat contoh di bawah docstring.

Contoh:
    from figkit import Kit
    def build():
        k = Kit("dt")                      # prefix unik per fragmen
        scr = k.screen_frame("12 Detail Tugas", 5203)
        k.statusbar(scr)
        k.T("Judul", scr, size=19, style="SemiBold", ls="-1%")
        return k.cmds, {"back": back_ref}
"""
import json

FONT = "Plus Jakarta Sans"
PHONE_W, PHONE_H = 393, 852

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
SH_CARD = [{"type": "dropShadow", "color": "#13131912", "offset": [0, 4], "radius": 16, "spread": 0, "visible": True, "blend": "normal"}]
SH_FLOAT = [{"type": "dropShadow", "color": "#13131926", "offset": [0, 12], "radius": 32, "spread": 0, "visible": True, "blend": "normal"}]
SH_BTN = [{"type": "dropShadow", "color": "#5B54F059", "offset": [0, 8], "radius": 20, "spread": 0, "visible": True, "blend": "normal"}]
SH_SHEET = [{"type": "dropShadow", "color": "#13131933", "offset": [0, -6], "radius": 24, "spread": 0, "visible": True, "blend": "normal"}]

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
    "trash":         "M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6M10 11v6M14 11v6",
    "pencil":        "M17 3a2.8 2.8 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5z",
    "kebab":         "M12 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM19 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM5 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2z",
    "checksquare":   "M9 11l3 3 8-8M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h9",
    "inbox":         "M22 12h-6l-2 3h-4l-2-3H2M5.5 5h13L22 12v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6z",
}


class Kit:
    """Kumpulan perintah FigCraft untuk satu fragmen layar."""

    def __init__(self, prefix):
        self.prefix = prefix
        self.cmds = []
        self.n = 0

    def S(self, cmd, params=None, as_name=None):
        d = {"command": cmd}
        if params:
            d["params"] = params
        if as_name:
            self.n += 1
            d["as"] = f"{self.prefix}_{as_name}_{self.n}"
            self.cmds.append(d)
            return {"$ref": d["as"]}
        self.cmds.append(d)
        return None

    def T(self, text, parent, size=14.5, style="Regular", color="text", width=None,
          name=None, align=None, ls=None, lh=None, deco=None, fill_hex=None):
        props = {"fontFamily": FONT, "fontStyle": style, "fontSize": size,
                 "fill": fill_hex if fill_hex else {"$var": color}}
        if align: props["textAlign"] = align
        if ls is not None: props["letterSpacing"] = ls
        if lh is not None: props["lineHeight"] = lh
        if deco: props["textDecoration"] = deco
        p = {"text": text, "x": 0, "y": 0, "parent": parent, "props": props,
             "name": name or (text[:28] if text else "Teks")}
        if width: p["width"] = width
        return self.S("text.create", p, as_name="t")

    def F(self, parent=None, name="Frame", layout=None, w=None, h=None, fill="none",
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
        return self.S("frame.create", p, as_name=key)

    def icon(self, name, parent, size=24, color="text", sw=2, key="ic",
             fill_hex=None, opacity=None):
        props = {"stroke": fill_hex if fill_hex else {"$var": color},
                 "strokeWeight": sw, "strokeCap": "round", "strokeJoin": "round"}
        if opacity is not None: props["opacity"] = opacity
        return self.S("vector.create", {"path": ICONS[name], "parent": parent,
                                        "width": size, "props": props,
                                        "name": f"i/{name}"}, as_name=key)

    def dot(self, parent, size, fill, key="dot", opacity=None, absolute=False, x=0, y=0):
        return self.F(parent, "dot", w=size, h=size, radius=999, fill=fill, key=key,
                      opacity=opacity, absolute=absolute, x=x, y=y)

    def micro(self, parent, text, color="text-muted", key="mic"):
        return self.T(text.upper(), parent, size=10, style="SemiBold", color=color,
                      ls="8%", name=key)

    def statusbar(self, parent):
        sb = self.F(parent, "Status Bar", layout="horizontal", w="fill", h=47,
                    pad=[6, 24, 0, 24], main="space-between", cross="center", key="sb")
        self.T("9:41", sb, size=14, style="SemiBold", name="Waktu")
        right = self.F(sb, "Sistem", layout="horizontal", gap=6, cross="center", key="sbr")
        bars = self.F(right, "Sinyal", layout="horizontal", gap=1.5, cross="max", key="sig")
        for i, hgt in enumerate([4, 6, 8, 11]):
            self.F(bars, "bar", w=3, h=hgt, radius=1, fill={"$var": "text"}, key=f"sig{i}")
        self.icon("wifi", right, size=15, sw=2)
        bat = self.F(right, "Baterai", layout="horizontal", gap=1.5, cross="center", key="bat")
        body = self.F(bat, "b", w=23, h=12, radius=4, stroke={"$var": "text-muted"}, sw=1,
                      pad=[2, 2, 2, 2], key="batb")
        self.F(body, "lvl", w=14, h=6, radius=2, fill={"$var": "text"}, key="batl")
        self.F(bat, "tip", w=1.5, h=4, radius=1, fill={"$var": "text-muted"}, key="batt")
        return sb

    def chip(self, parent, label, selected=False, key="chip"):
        c = self.F(parent, f"Chip/{label}", layout="horizontal", pad=[8, 16], radius=999,
                   cross="center",
                   fill={"$var": "primary"} if selected else {"$var": "surface"},
                   stroke=None if selected else {"$var": "border"}, key=key)
        self.T(label, c, size=13, style="SemiBold" if selected else "Regular",
               color="primary-fg" if selected else "text-muted", name="label")
        return c

    def button(self, parent, label, kind="primary", h=54, full=True, w=None,
               key="btn", size=15):
        st = {"primary": dict(fill=GRAD, effects=SH_BTN, tc="primary-fg", stroke=None),
              "secondary": dict(fill={"$var": "surface"}, stroke={"$var": "border"}, tc="text"),
              "ghost": dict(fill="none", stroke=None, tc="primary"),
              "danger": dict(fill={"$var": "danger"}, stroke=None, tc="primary-fg"),
              "danger-outline": dict(fill="none", stroke={"$var": "danger"}, tc="danger"),
              "soft": dict(fill={"$var": "primary-soft"}, stroke=None, tc="primary")}[kind]
        b = self.F(parent, f"Btn/{label}", layout="horizontal", main="center", cross="center",
                   w=w, h=h, radius=h / 2, pad=[0, 24], fill=st["fill"], stroke=st["stroke"],
                   effects=st.get("effects"), sizingH="fill" if full and not w else None, key=key)
        self.T(label, b, size=size, style="SemiBold", color=st["tc"], ls="-1%", name="label")
        return b

    def toggle(self, parent, on=True, key="tg"):
        tr = self.F(parent, "Switch", w=46, h=27, radius=999,
                    fill={"$var": "primary" if on else "border"}, pad=[3],
                    main="max" if on else "min", cross="center", key=key)
        self.dot(tr, 21, "#FFFFFF", key=key + "k")
        return tr

    def fieldbox(self, parent, value, key="fld", h=56, placeholder=False, trailing=None):
        f = self.F(parent, "Input", layout="horizontal", w="fill", h=h, radius=16,
                   pad=[0, 18], cross="center",
                   main="space-between" if trailing else "min",
                   fill={"$var": "surface-2"}, gap=8, key=key)
        self.T(value, f, size=14.5, style="Medium" if not placeholder else "Regular",
               color="text" if not placeholder else "text-muted", name="nilai")
        if trailing:
            trail = self.F(f, "trail", layout="horizontal", gap=8, cross="center", key=key + "tr")
            for t in trailing:
                self.icon(t, trail, size=18, color="text-muted")
        return f

    def labeled_field(self, parent, label, value, key="lf", h=56, placeholder=False,
                      trailing=None):
        col = self.F(parent, f"Field/{label}", layout="vertical", gap=8, sizingH="fill", key=key)
        self.T(label, col, size=12.5, style="SemiBold", color="text-muted", name=key + "l")
        self.fieldbox(col, value, key=key + "f", h=h, placeholder=placeholder, trailing=trailing)
        return col

    def taskcard(self, parent, title, cat, time, prio, done=False, key="card", width=None):
        card = self.F(parent, f"Tugas / {title[:24]}", layout="horizontal", gap=13,
                      pad=[13, 16], radius=20, fill={"$var": "surface"}, effects=SH_CARD,
                      cross="center", sizingH="fill" if not width else None, w=width, key=key)
        if done:
            cb = self.F(card, "Cek", w=24, h=24, radius=999, fill={"$var": "success"},
                        layout="horizontal", main="center", cross="center", key=key + "cb")
            self.icon("check", cb, size=13, sw=3, fill_hex="#FFFFFF", key=key + "ck")
        else:
            self.F(card, "Cek", w=24, h=24, radius=999, stroke={"$var": "border"}, sw=2,
                   key=key + "cb")
        col = self.F(card, "Isi", layout="vertical", gap=7, sizingH="fill", key=key + "col")
        self.T(title, col, size=15, style="Medium" if not done else "Regular",
               color="text" if not done else "text-muted", lh="135%",
               deco="strikethrough" if done else None, name="judul")
        meta = self.F(col, "Meta", layout="horizontal", gap=10, cross="center", key=key + "meta")
        fg, bg = CAT[cat]
        tag = self.F(meta, "Tag", layout="horizontal", gap=5, cross="center", pad=[4, 10],
                     radius=999, fill=bg, key=key + "tag")
        self.dot(tag, 5, fg, key=key + "tagd")
        self.T(cat, tag, size=11, style="SemiBold", fill_hex=fg, name="tagl")
        self.icon("clock", meta, size=12.5, color="text-muted", sw=2, key=key + "cl")
        self.T(time, meta, size=11.5, color="text-muted", name="jam")
        self.icon("flag", card, size=15, fill_hex=prio, sw=2, key=key + "prio")
        return card

    def section_header(self, parent, title, count=None, action=None, key="sec"):
        r = self.F(parent, "Bagian", layout="horizontal", w="fill", gap=8, cross="center", key=key)
        self.T(title, r, size=16.5, style="SemiBold", ls="-1%", name="judul")
        if count:
            pill = self.F(r, "hitung", layout="horizontal", pad=[3, 9], radius=999,
                          fill={"$var": "surface-2"}, key=key + "p")
            self.T(str(count), pill, size=11, style="SemiBold", color="text-muted", name=key + "pl")
        if action:
            self.F(r, "spacer", sizingH="fill", h=1, key=key + "s")
            self.T(action, r, size=12.5, style="SemiBold", color="primary", name="aksi")
        return r

    def ring(self, parent, pct, key="ring", size=62, lblsize=13, track="border", fill=None):
        box = self.F(parent, "Ring", w=size, h=size, key=key)
        self.S("shape.ellipse", {"x": 0, "y": 0, "width": size, "height": size,
                                 "parent": box,
                                 "props": {"fill": {"$var": track}, "arcSweep": 360,
                                           "arcInner": 0.74}}, as_name=key + "tr")
        sweep = round(360 * pct / 100)
        self.S("shape.ellipse", {"x": 0, "y": 0, "width": size, "height": size,
                                 "parent": box,
                                 "props": {"fill": fill or {"$var": "primary"},
                                           "arcStart": -90, "arcSweep": sweep,
                                           "arcInner": 0.74}}, as_name=key + "ar")
        lab = self.F(box, "lbl", w=size, h=size, layout="horizontal", main="center",
                     cross="center", key=key + "lb")
        self.T(f"{pct}%", lab, size=lblsize, style="SemiBold", name=key + "lt")
        return box

    def hero_card(self, parent, key="hero", wide=False):
        c = self.F(parent, "Hero", layout="vertical", w="fill", radius=26, fill=GRAD,
                   pad=[20, 20], gap=14, effects=SH_BTN, key=key)
        r = self.F(c, "atas", layout="horizontal", w="fill", main="space-between",
                   cross="min", key=key + "r")
        col = self.F(r, "sapaan", layout="vertical", gap=5, key=key + "c")
        self.T("Selamat pagi, Rian 👋", col, size=20 if not wide else 22, style="SemiBold",
               fill_hex="#FFFFFF", ls="-1%", name=key + "t1")
        self.T("Jumat, 13 November 2026", col, size=12.5, fill_hex="#FFFFFFB0", name=key + "t2")
        av = self.F(r, "Avatar", w=44, h=44, radius=999, fill="#FFFFFF2E",
                    layout="horizontal", main="center", cross="center", key=key + "av")
        self.T("R", av, size=16, style="SemiBold", fill_hex="#FFFFFF", name=key + "avt")
        pills = self.F(c, "pil", layout="horizontal", gap=8, w="fill", key=key + "p")
        p1 = self.F(pills, "Streak", layout="horizontal", gap=6, cross="center", pad=[7, 12],
                    radius=999, fill="#FFFFFF2B", key=key + "p1")
        self.icon("zap", p1, size=13, fill_hex="#FFD66B", sw=2, key=key + "p1i")
        self.T("12 hari streak", p1, size=11.5, style="SemiBold", fill_hex="#FFFFFF",
               name=key + "p1l")
        p2 = self.F(pills, "Sisa", layout="horizontal", pad=[7, 12], radius=999,
                    fill="#FFFFFF2B", key=key + "p2")
        self.T("3 tugas hari ini", p2, size=11.5, style="SemiBold", fill_hex="#FFFFFF",
               name=key + "p2l")
        return c

    def progress_card(self, parent, key="prog", pct=37, done=3, total=8, note=None):
        c = self.F(parent, "Progres", layout="horizontal", w="fill", radius=20,
                   fill={"$var": "surface"}, pad=[16, 18], gap=16, cross="center",
                   effects=SH_CARD, key=key)
        self.ring(c, pct, key=key + "ring")
        col = self.F(c, "info", layout="vertical", gap=4, sizingH="fill", key=key + "c")
        self.micro(col, "Progres hari ini", key=key + "m")
        self.T(f"{done} dari {total} selesai", col, size=16, style="SemiBold", ls="-1%",
               name=key + "v")
        self.T(note or "3 tugas lagi sebelum pukul 17:00", col, size=11.5,
               color="text-muted", name=key + "k")
        return c

    def screen_frame(self, name, x, y=0, key="scr"):
        return self.F(None, name, w=PHONE_W, h=PHONE_H, fill={"$var": "bg"},
                      layout="vertical", clip=True, x=x, y=y, key=key)

    def dock_items(self, parent, active, key="dock"):
        refs = []
        items = [("Beranda", "home"), ("Kalender", "calendar"), ("Statistik", "chart"),
                 ("Profil", "user")]
        for i, (label, ic) in enumerate(items):
            act = label == active
            it = self.F(parent, f"Menu/{label}", layout="horizontal", gap=6, cross="center",
                        main="center", pad=[10, 14] if act else [10, 6], radius=999,
                        fill={"$var": "primary-soft"} if act else "none", key=f"{key}i{i}")
            self.icon(ic, it, size=20, color="primary" if act else "text-muted", sw=2,
                      key=f"{key}ic{i}")
            self.T(label, it, size=11, style="SemiBold" if act else "Regular",
                   color="primary" if act else "text-muted", name=f"{key}l{i}")
            refs.append(it)
        return refs

    def dock_bar(self, parent, active, key="dk", x=16, y=774, w=361):
        d = self.F(parent, "Dock", layout="horizontal", w=w, h=64, radius=999,
                   fill={"$var": "surface"}, pad=[0, 10], main="space-between",
                   cross="center", effects=SH_FLOAT, absolute=True, x=x, y=y, key=key)
        refs = self.dock_items(d, active, key=key + "i")
        return d, refs

    def fab(self, parent, key="fab", x=311, y=698, size=58, ic="plus"):
        f = self.F(parent, "FAB", w=size, h=size, radius=999, fill=GRAD,
                   layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
                   absolute=True, x=x, y=y, key=key)
        self.icon(ic, f, size=26, sw=2.5, fill_hex="#FFFFFF", key=key + "i")
        return f
