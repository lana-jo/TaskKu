#!/usr/bin/env python3
"""Generator desain UI/UX "TaskKu" (todolist mobile) -> build.json untuk figcraft-cli run.

Hasil: file .figcraft dengan 3 halaman (Design System, Screens, Responsive),
variabel warna Terang/Gelap, komponen, dan 7 layar mobile + tablet + desktop.
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


# ---------------------------------------------------------------- palet
VARS = {
    "bg":          ("#F6F6FA", "#15151D"),
    "surface":     ("#FFFFFF", "#1E1E2A"),
    "surface-2":   ("#F0F0F6", "#282836"),
    "text":        ("#17171E", "#F4F4F8"),
    "text-muted":  ("#6F6F7E", "#A0A0B0"),
    "border":      ("#E6E6EF", "#2E2E3C"),
    "primary":     ("#5757D9", "#8585F2"),
    "primary-soft":("#ECECFB", "#2B2B52"),
    "primary-fg":  ("#FFFFFF", "#15151D"),
    "success":     ("#16A34A", "#3DDC84"),
    "warning":     ("#F59E0B", "#FFC043"),
    "danger":      ("#DC2626", "#F26D6D"),
}

# warna statis kategori (soft bg + teks) — sengaja tidak ikut mode gelap
CAT = {
    "Pekerjaan": ("#5757D9", "#E9E9FB"),
    "Pribadi":   ("#0E9F5D", "#E3F5EC"),
    "Belanja":   ("#C77700", "#FDF1DC"),
    "Kesehatan": ("#D24848", "#FBE7E7"),
}

SHADOW_SM = [{"type": "dropShadow", "color": "#17171E17", "offset": [0, 2], "radius": 8, "spread": 0, "visible": True, "blend": "normal"}]
SHADOW_BTN = [{"type": "dropShadow", "color": "#5757D94D", "offset": [0, 6], "radius": 16, "spread": 0, "visible": True, "blend": "normal"}]
SHADOW_FAB = [{"type": "dropShadow", "color": "#5757D966", "offset": [0, 8], "radius": 20, "spread": 0, "visible": True, "blend": "normal"}]
SHADOW_CARD = [{"type": "dropShadow", "color": "#17171E1F", "offset": [0, 4], "radius": 14, "spread": 0, "visible": True, "blend": "normal"}]

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
}


def T(text, parent, size=15, style="Regular", color="text", width=None, name=None,
      align=None, ls=None, lh=None, deco=None, fill_hex=None):
    props = {"fontFamily": "Inter", "fontStyle": style, "fontSize": size,
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
      stroke_top=False, stroke_sides=None, wrap=None):
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
        if stroke_sides: props["strokeSides"] = stroke_sides
        if stroke_top:
            props["strokeTopWeight"] = sw
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


def dot(parent, size, fill, key="dot", opacity=None):
    return F(parent, "dot", w=size, h=size, radius=999, fill=fill, key=key, opacity=opacity)


# ---------------------------------------------------------------- blok umum
def statusbar(parent):
    sb = F(parent, "Status Bar", layout="horizontal", w="fill", h=44,
           pad=[0, 24], main="space-between", cross="center", key="sb")
    T("9:41", sb, size=13, style="SemiBold", name="Waktu")
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


def chip(parent, label, selected=False, key="chip", bg=None, fg=None):
    c = F(parent, f"Chip/{label}", layout="horizontal", pad=[7, 14], radius=999,
          gap=6, cross="center",
          fill={"$var": "primary"} if selected else (bg or {"$var": "surface"}),
          stroke=None if selected else {"$var": "border"}, key=key)
    T(label, c, size=13, style="SemiBold" if selected else "Regular",
      color="primary-fg" if selected else "text-muted", name="label")
    return c


def button(parent, label, kind="primary", h=52, full=True, w=None, key="btn", size=15):
    st = {"primary": dict(fill={"$var": "primary"}, effects=SHADOW_BTN, tc="primary-fg", stroke=None),
          "secondary": dict(fill={"$var": "surface"}, stroke={"$var": "border"}, tc="text"),
          "ghost": dict(fill="none", stroke=None, tc="primary"),
          "danger": dict(fill="none", stroke={"$var": "danger"}, tc="danger"),
          "soft": dict(fill={"$var": "primary-soft"}, stroke=None, tc="primary")}[kind]
    b = F(parent, f"Btn/{label}", layout="horizontal", main="center", cross="center",
          w=w, h=h, radius=16, pad=[0, 20], fill=st["fill"], stroke=st["stroke"],
          effects=st.get("effects"), sizingH="fill" if full and not w else None, key=key)
    T(label, b, size=size, style="SemiBold", color=st["tc"], name="label")
    return b


def toggle(parent, on=True, key="tg"):
    tr = F(parent, "Switch", w=44, h=26, radius=999,
           fill={"$var": "primary" if on else "border"}, pad=[3], main="max" if on else "min",
           cross="center", key=key)
    dot(tr, 20, {"$var": "primary-fg"}, key=key + "k")
    return tr


def field(parent, placeholder, key="fld", h=52, value=None, trailing=None, multiline=False):
    f = F(parent, "Input", layout="horizontal", w="fill", h=h, radius=14,
          pad=[0, 16], cross="center", main="space-between" if trailing else "min",
          fill={"$var": "surface"}, stroke={"$var": "border"}, gap=8, key=key)
    T(value if value else placeholder, f, size=14.5, color="text" if value else "text-muted",
      name="nilai")
    if trailing:
        trail = F(f, "trail", layout="horizontal", gap=8, cross="center", key=key + "tr")
        for t in trailing:
            icon(t, trail, size=18, color="text-muted")
    return f


def taskcard(parent, title, cat, time, prio, done=False, key="card", width=None):
    """Kartu tugas; prio = hex warna statis, cat = kunci CAT."""
    card = F(parent, f"Tugas / {title[:24]}", layout="horizontal", gap=12, pad=[12, 14],
             radius=14, fill={"$var": "surface"}, stroke={"$var": "border"},
             effects=SHADOW_SM, cross="center",
             sizingH="fill" if not width else None, w=width, key=key)
    if done:
        cb = F(card, "Cek", w=22, h=22, radius=999, fill={"$var": "primary"},
               layout="horizontal", main="center", cross="center", key=key + "cb")
        icon("check", cb, size=12, sw=3, fill_hex="#FFFFFF", key=key + "ck")
    else:
        F(card, "Cek", w=22, h=22, radius=999, stroke={"$var": "text-muted"}, sw=1.8, key=key + "cb")
    col = F(card, "Isi", layout="vertical", gap=6, sizingH="fill", key=key + "col")
    T(title, col, size=15, style="SemiBold" if not done else "Regular",
      color="text" if not done else "text-muted",
      deco="strikethrough" if done else None, name="judul")
    meta = F(col, "Meta", layout="horizontal", gap=8, cross="center", key=key + "meta")
    fg, bg = CAT[cat]
    tag = F(meta, "Tag", layout="horizontal", pad=[3, 9], radius=999, fill=bg, key=key + "tag")
    T(cat, tag, size=11, style="SemiBold", fill_hex=fg, name="tagl")
    icon("clock", meta, size=12.5, color="text-muted", sw=2, key=key + "cl")
    T(time, meta, size=11.5, color="text-muted", name="jam")
    dot(card, 8, prio, key=key + "prio")
    return card


def section_header(parent, title, action="Lihat semua", key="sec"):
    r = F(parent, "Bagian", layout="horizontal", w="fill", main="space-between",
          cross="center", key=key)
    T(title, r, size=16, style="SemiBold", name="judul")
    if action:
        T(action, r, size=12, style="SemiBold", color="primary", name="aksi")
    return r


def navbar(parent, active, key="nav"):
    nav = F(parent, "Navigasi Bawah", layout="vertical", w="fill", h=80,
            fill={"$var": "surface"}, stroke={"$var": "border"}, sw=1, stroke_top=True, key=key)
    row = F(nav, "Menu", layout="horizontal", w="fill", h=52, pad=[0, 10], key=key + "r")
    items = [("Beranda", "home"), ("Kalender", "calendar"), ("Statistik", "chart"), ("Profil", "user")]
    for i, (label, ic) in enumerate(items):
        it = F(row, f"Menu/{label}", layout="vertical", gap=3, cross="center", main="center",
               sizingH="fill", h=52, key=f"{key}i{i}")
        act = label == active
        icon(ic, it, size=21, color="primary" if act else "text-muted", sw=2, key=f"{key}ic{i}")
        T(label, it, size=10.5, style="SemiBold" if act else "Regular",
          color="primary" if act else "text-muted", name="lbl")
    F(nav, "Home Indicator", w=120, h=5, radius=999, fill={"$var": "text-muted"},
      opacity=0.4, key=key + "hi")
    return nav


def greeting_header(parent, key="hdr"):
    r = F(parent, "Header", layout="horizontal", w="fill", main="space-between",
          cross="center", key=key)
    col = F(r, "Sapaan", layout="vertical", gap=4, key=key + "c")
    T("Halo, Rian 👋", col, size=22, style="SemiBold", name="halo")
    T("Kamu punya 5 tugas untuk hari ini", col, size=13, color="text-muted", name="sub")
    av = F(r, "Avatar", w=42, h=42, radius=999, fill={"$var": "primary-soft"},
           layout="horizontal", main="center", cross="center", key=key + "av")
    T("R", av, size=16, style="SemiBold", color="primary", name="inisial")
    return r


def progress_card(parent, done=3, total=8, pct=37, key="prog"):
    c = F(parent, "Kartu Progres", layout="vertical", w="fill", pad=16, gap=10,
          radius=16, fill={"$var": "primary-soft"}, key=key)
    r = F(c, "baris", layout="horizontal", w="fill", main="space-between", key=key + "r")
    T("Progres Hari Ini", r, size=13, style="SemiBold", name="lbl")
    T(f"{done}/{total} tugas", r, size=13, style="SemiBold", color="primary", name="nilai")
    tr = F(c, "Track", layout="horizontal", w="fill", h=8, radius=999,
           fill={"$var": "border"}, key=key + "tr")
    F(tr, "Fill", w=int(353 * pct / 100), h=8, radius=999, fill={"$var": "primary"}, key=key + "f")
    T(f"Selesai {pct}% • target pukul 17:00", c, size=11, color="text-muted", name="ket")
    return c


def screen_frame(name, x, y=0, key="scr"):
    return F(None, name, w=PHONE_W, h=PHONE_H, radius=0, fill={"$var": "bg"},
             layout="vertical", clip=True, x=x, y=y, key=key)


# ================================================================ HALAMAN 1
S("page.rename", {"name": "🎨 Design System"})

# --- Variabel warna (koleksi + 2 mode, dibuat sebelum dipakai)
S("variable.createCollection", {"name": "Warna", "modes": ["Terang", "Gelap"]})
for vname, (light, dark) in VARS.items():
    S("variable.create", {"collection": "Warna", "name": vname, "type": "color",
                          "values": {"Terang": light, "Gelap": dark}})

# --- Cover
cv = F(None, "Cover — TaskKu", w=1280, h=400, radius=24,
       fill={"type": "linearGradient", "stops": ["#ECECFB", "#F6F6FA"]},
       layout="vertical", pad=[48, 56], gap=16, main="center", key="cover")
S("shape.rectangle", {"x": 0, "y": 0, "width": 0, "height": 0}) if False else None
logo = F(cv, "Logo", w=64, h=64, radius=18, fill={"$var": "primary"},
         layout="horizontal", main="center", cross="center", effects=SHADOW_BTN, key="logo")
icon("check", logo, size=30, sw=3, fill_hex="#FFFFFF", key="logoic")
T("TaskKu", cv, size=44, style="Bold", name="judul")
T("Aplikasi To-Do List — UI/UX Kit", cv, size=17, color="text-muted", name="sub")
meta = F(cv, "meta", layout="horizontal", gap=10, key="cvmeta")
for i, m in enumerate(["393×852 · Mobile-First", "Terang & Gelap", "7 Layar", "Tablet & Desktop"]):
    chip(meta, m, key=f"cvm{i}")

# --- Warna
cw = F(None, "Warna / Warna Token", w=1280, radius=24, fill={"$var": "surface"},
       stroke={"$var": "border"}, layout="vertical", pad=[28, 32], gap=18, y=460, key="cw")
T("Palet Warna", cw, size=20, style="SemiBold", name="jud")
T("Dua mode pada satu koleksi variabel — setiap layer terikat ke variabel, bukan warna hex.", cw,
  size=13, color="text-muted", name="ket")
grid = F(cw, "Swatch", layout="horizontal", gap=12, wrap="wrap", w="fill", key="swg")
for name, (light, dark) in VARS.items():
    sw = F(grid, f"Token/{name}", layout="vertical", gap=8, w=143, key=f"sw_{name}")
    F(sw, "warna", w=143, h=64, radius=12, fill=light, stroke={"$var": "border"}, key=f"swb_{name}")
    T(name, sw, size=13, style="SemiBold", name=f"swn_{name}")
    T(f"T {light.upper()}\nG {dark.upper()}", sw, size=10.5, color="text-muted", lh="135%",
      name=f"swx_{name}")

# --- Tipografi
tw = F(None, "Tipografi", w=1280, radius=24, fill={"$var": "surface"},
       stroke={"$var": "border"}, layout="horizontal", pad=[28, 32], gap=48,
       y=460 + 330, key="tw")
col1 = F(tw, "Sampel", layout="vertical", gap=14, sizingH="fill", key="tw1")
T("Tipografi — Inter", col1, size=20, style="SemiBold", name="tjud")
T("Display / 28 SemiBold", F(col1, "d1", layout="vertical", gap=2, sizingH="fill", key="td1"),
  size=28, style="SemiBold", name="ts1")
T("Judul / 20 SemiBold", col1, size=20, style="SemiBold", name="ts2")
T("Body / 15 Regular — Catat, atur, dan selesaikan tugasmu setiap hari.", col1, size=15, lh="150%", name="ts3")
T("Kecil / 13 — teks pendukung", col1, size=13, color="text-muted", name="ts4")
T("Caption / 11 — label dan keterangan", col1, size=11, color="text-muted", name="ts5")

# --- Komponen
comp = F(None, "Komponen", w=1280, radius=24, fill={"$var": "surface"},
         stroke={"$var": "border"}, layout="vertical", pad=[28, 32], gap=20,
         y=460 + 330 + 320, key="comp")
T("Komponen", comp, size=20, style="SemiBold", name="cjud")
row1 = F(comp, "Tombol", layout="horizontal", gap=14, w="fill", key="crow1")
for i, (lbl, k) in enumerate([("Tugas Baru", "primary"), ("Kedua", "secondary"), ("Tersier", "ghost"), ("Hapus", "danger")]):
    button(row1, lbl, k, h=46, full=False, w=150, key=f"cb{i}")
row2 = F(comp, "Chip", layout="horizontal", gap=10, w="fill", cross="center", key="crow2")
chip(row2, "Semua", selected=True, key="cch1")
chip(row2, "Pekerjaan", key="cch2")
chip(row2, "Pribadi", key="cch3")
chip(row2, "Belanja", key="cch4")
fldw = F(row2, "Input", w=300, key="cfld")
field(fldw, "Cari tugas…", trailing=["search"], key="cfld1")
tgw = F(row2, "Switch", layout="horizontal", gap=10, cross="center", key="ctg")
toggle(tgw, True, key="ctg1")
toggle(tgw, False, key="ctg2")
row3 = F(comp, "Kartu Tugas", layout="horizontal", gap=16, w="fill", key="crow3")
box1 = F(row3, "K1", w=360, key="cbox1")
taskcard(box1, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#DC2626", key="ctask1", width=360)
box2 = F(row3, "K2", w=360, key="cbox2")
taskcard(box2, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#16A34A", done=True, key="ctask2", width=360)
row4 = F(comp, "Navigasi", layout="horizontal", gap=16, w="fill", cross="max", key="crow4")
navw = F(row4, "Nav", w=360, key="cnavw")
navbar(navw, "Beranda", key="cnav")
fab = F(row4, "FAB", w=56, h=56, radius=999, fill={"$var": "primary"},
        layout="horizontal", main="center", cross="center", effects=SHADOW_FAB, key="cfab")
icon("plus", fab, size=24, sw=2.5, fill_hex="#FFFFFF", key="cfabi")

# --- Ikon
iw = F(None, "Ikon", w=1280, radius=24, fill={"$var": "surface"}, stroke={"$var": "border"},
       layout="horizontal", pad=[24, 32], gap=22, cross="center",
       y=460 + 330 + 320 + 420, key="iw")
T("Ikon", iw, size=16, style="SemiBold", name="iwt")
for i, nm in enumerate(["home", "calendar", "chart", "user", "search", "bell", "clock",
                        "check", "plus", "chevron_right", "chevron_down", "x", "eye",
                        "sliders", "sun", "moon", "logout"]):
    icon(nm, iw, size=22, color="text", key=f"iw{i}")

# Komponen utama (untuk panel Assets)
row3b = F(comp, "Komponen Utama", layout="horizontal", gap=16, w="fill", key="crow5")
T("Komponen utama (Assets): ", row3b, size=13, color="text-muted", name="c5l")
mainc = F(row3b, "M1", w=340, key="cmain1")
mc = taskcard(mainc, "Contoh tugas", "Pribadi", "10:00", "#F59E0B", key="cmainc", width=340)
S("component.create", {"id": mc}, as_name="maincomp")
S("object.rename", {"ids": [mc], "name": "TaskCard/Default"})

# ================================================================ HALAMAN 2
p2 = S("page.add", {"name": "📱 Screens"}, as_name="p2")
S("page.select", {"id": p2})

# ---- 01 Onboarding
scr = screen_frame("01 Onboarding", 0, key="onb")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[24, 28], gap=18,
         main="center", key="onbb")
ill = F(body, "Ilustrasi", w=240, h=240, layout="vertical", main="center", cross="center",
        key="onbill", sizingH="fill")
F(ill, "Lingkaran", w=200, h=200, radius=999, fill={"$var": "primary-soft"}, key="onbcir")
cardill = F(ill, "Kartu", w=150, h=168, radius=18, fill={"$var": "surface"},
            effects=SHADOW_CARD, layout="vertical", pad=16, gap=12, absolute=True, key="onbcard")
for i, (bw, done) in enumerate([(92, True), (72, True), (84, False)]):
    row = F(cardill, f"r{i}", layout="horizontal", gap=10, cross="center", key=f"onbr{i}")
    if done:
        cb = F(row, "cb", w=20, h=20, radius=999, fill={"$var": "primary"},
               layout="horizontal", main="center", cross="center", key=f"onbcb{i}")
        icon("check", cb, size=11, sw=3, fill_hex="#FFFFFF", key=f"onbck{i}")
    else:
        F(row, "cb", w=20, h=20, radius=999, stroke={"$var": "border"}, sw=1.8, key=f"onbcb{i}")
    F(row, "bar", w=bw, h=8, radius=4, fill={"$var": "surface-2"}, key=f"onbbar{i}")
badge = F(ill, "Badge", w=46, h=46, radius=999, fill={"$var": "surface"},
          layout="horizontal", main="center", cross="center", effects=SHADOW_SM,
          absolute=True, key="onbbadge")
icon("bell", badge, size=20, color="primary", key="onbbell")
badge2 = F(ill, "Badge2", w=38, h=38, radius=999, fill={"$var": "surface"},
           layout="horizontal", main="center", cross="center", effects=SHADOW_SM,
           absolute=True, key="onbbadge2")
icon("calendar", badge2, size=16, color="success", key="onbcal")
F(ill, "Titik", w=14, h=14, radius=999, fill={"$var": "warning"}, opacity=0.9,
  absolute=True, key="onbdot")
T("Kelola tugasmu,\ntanpa stres.", body, size=26, style="SemiBold", align="center",
  lh="130%", name="onbjud")
T("Catat, atur prioritas, dan selesaikan tugas harianmu dalam satu aplikasi yang sederhana.",
  body, size=14, color="text-muted", align="center", lh="155%", width=300, name="onbsub")
dots = F(body, "Dots", layout="horizontal", gap=6, cross="center", main="center",
         sizingH="fill", key="onbdots")
F(dots, "d1", w=20, h=8, radius=999, fill={"$var": "primary"}, key="onbd1")
dot(dots, 8, {"$var": "border"}, key="onbd2")
dot(dots, 8, {"$var": "border"}, key="onbd3")
button(body, "Mulai Sekarang", "primary", key="onbbtn")
row = F(body, "MasukRow", layout="horizontal", gap=4, main="center", sizingH="fill", key="onbl")
T("Sudah punya akun?", row, size=13, color="text-muted", name="onbl1")
T("Masuk", row, size=13, style="SemiBold", color="primary", name="onbl2")

# ---- 02 Masuk
scr = screen_frame("02 Masuk", 473, key="log")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[8, 24], gap=16, key="logb")
back = F(body, "Kembali", w=40, h=40, radius=999, fill={"$var": "surface-2"},
         layout="horizontal", main="center", cross="center", key="logback")
icon("chevron_left", back, size=20, key="logbacki")
T("Selamat datang\nkembali 👋", body, size=26, style="SemiBold", lh="130%", name="logjud")
T("Masuk untuk melanjutkan tugasmu hari ini.", body, size=14, color="text-muted",
  lh="150%", name="logsub")
F(body, "jarak", h=8, fill="none", key="logsp")
col = F(body, "Email", layout="vertical", gap=8, sizingH="fill", key="logem")
T("Email", col, size=13, style="SemiBold", name="logeml")
field(col, "nama@email.com", key="logemf")
col = F(body, "Sandi", layout="vertical", gap=8, sizingH="fill", key="logpw")
T("Kata Sandi", col, size=13, style="SemiBold", name="logpwl")
field(col, "••••••••", key="logpwf", trailing=["eye"])
r = F(body, "Ingat", layout="horizontal", w="fill", main="space-between", cross="center", key="logr")
rc = F(r, "kiri", layout="horizontal", gap=8, cross="center", key="logrc")
F(rc, "cb", w=18, h=18, radius=6, fill={"$var": "primary"}, key="logcb")
T("Ingat saya", rc, size=13, name="logrc2")
T("Lupa kata sandi?", r, size=13, style="SemiBold", color="primary", name="loglupa")
button(body, "Masuk", "primary", key="logbtn")
dv = F(body, "Divider", layout="horizontal", w="fill", gap=12, cross="center", key="logdv")
F(dv, "l", h=1, sizingH="fill", fill={"$var": "border"}, key="logdvl")
T("atau", dv, size=12, color="text-muted", name="logdvt")
F(dv, "r", h=1, sizingH="fill", fill={"$var": "border"}, key="logdvr")
btn = F(body, "Google", layout="horizontal", main="center", cross="center", w="fill", h=52,
        radius=16, fill={"$var": "surface"}, stroke={"$var": "border"}, gap=10, key="logg")
gm = F(btn, "G", layout="horizontal", gap=3, key="loggm")
for i, c in enumerate(["#EA4335", "#FBBC05", "#34A853", "#4285F4"]):
    dot(gm, 8, c, key=f"loggd{i}")
T("Lanjutkan dengan Google", btn, size=14.5, style="SemiBold", name="loggt")
row = F(body, "Daftar", layout="horizontal", gap=4, main="center", sizingH="fill", key="logf")
T("Belum punya akun?", row, size=13, color="text-muted", name="logf1")
T("Daftar", row, size=13, style="SemiBold", color="primary", name="logf2")

# ---- 03 Beranda
home_ref = scr = screen_frame("03 Beranda", 946, key="home")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[6, 20], gap=14, key="hb")
greeting_header(body, key="hh")
progress_card(body, key="hp")
chips = F(body, "Filter", layout="horizontal", gap=8, w="fill", key="hc")
chip(chips, "Semua", selected=True, key="hc1")
chip(chips, "Pekerjaan", key="hc2")
chip(chips, "Pribadi", key="hc3")
chip(chips, "Belanja", key="hc4")
section_header(body, "Hari Ini", key="hs1")
taskcard(body, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#16A34A", done=True, key="ht1")
taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#DC2626", key="ht2")
taskcard(body, "Belanja bulanan di pasar", "Belanja", "16:00", "#F59E0B", key="ht3")
section_header(body, "Besok", key="hs2")
taskcard(body, "Kontrol dokter gigi", "Kesehatan", "08:30", "#DC2626", key="ht4")
taskcard(body, "Olahraga pagi: lari 5 km", "Pribadi", "06:00", "#16A34A", key="ht5")
navbar(scr, "Beranda", key="hnav")
fab = F(scr, "FAB", w=56, h=56, radius=999, fill={"$var": "primary"},
        layout="horizontal", main="center", cross="center", effects=SHADOW_FAB,
        absolute=True, x=317, y=700, key="hfab")
icon("plus", fab, size=24, sw=2.5, fill_hex="#FFFFFF", key="hfabi")

# ---- 04 Tugas Baru (sheet)
scr = screen_frame("04 Tugas Baru", 1419, key="add")
statusbar(scr)
body = F(scr, "Konten Redup", layout="vertical", w="fill", sizingV="fill", pad=[6, 20],
         gap=12, key="ab", opacity=0.45)
greeting_header(body, key="ah")
taskcard(body, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#16A34A", done=True, key="at1")
taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#DC2626", key="at2")
navbar(scr, "Beranda", key="anav")
sheet = F(scr, "Sheet", layout="vertical", w="fill", radius=[28, 28, 0, 0],
          fill={"$var": "surface"}, pad=[12, 22, 20, 22], gap=14, effects=SHADOW_CARD, key="asheet")
F(sheet, "Grabber", w=44, h=5, radius=999, fill={"$var": "border"},
  main="center", layout="horizontal", sizingH="fill", key="agrab")
r = F(sheet, "Judul", layout="horizontal", w="fill", main="space-between", cross="center", key="ahr")
T("Tugas Baru", r, size=18, style="SemiBold", name="ah1")
xbtn = F(r, "Tutup", w=32, h=32, radius=999, fill={"$var": "surface-2"},
         layout="horizontal", main="center", cross="center", key="ax")
icon("x", xbtn, size=16, sw=2.2, key="axi")
col = F(sheet, "JudulTugas", layout="vertical", gap=8, sizingH="fill", key="aj")
T("Judul tugas", col, size=13, style="SemiBold", name="ajl")
field(col, "Rapat sprint dengan tim desain", key="ajf", value="Rapat sprint desain")
col = F(sheet, "Catatan", layout="vertical", gap=8, sizingH="fill", key="an")
T("Catatan", col, size=13, style="SemiBold", name="anl")
field(col, "Tambahkan catatan (opsional)", key="anf", h=64)
col = F(sheet, "Kategori", layout="vertical", gap=8, sizingH="fill", key="ak")
T("Kategori", col, size=13, style="SemiBold", name="akl")
chips = F(col, "Chips", layout="horizontal", gap=8, sizingH="fill", key="akc")
chip(chips, "Pekerjaan", selected=True, key="akc1")
chip(chips, "Pribadi", key="akc2")
chip(chips, "Belanja", key="akc3")
chip(chips, "Kesehatan", key="akc4")
col = F(sheet, "Prioritas", layout="vertical", gap=8, sizingH="fill", key="ap")
T("Prioritas", col, size=13, style="SemiBold", name="apl")
seg = F(col, "Segmen", layout="horizontal", gap=8, sizingH="fill", key="apsg")
for i, (lbl, hexc, sel) in enumerate([("Tinggi", "#DC2626", True), ("Sedang", "#F59E0B", False), ("Rendah", "#16A34A", False)]):
    segc = F(seg, f"S/{lbl}", layout="horizontal", main="center", cross="center", h=38,
             radius=12, sizingH="fill", fill=("#FBE7E7" if sel else None) or "none",
             stroke=None if sel else {"$var": "border"}, key=f"aps{i}")
    T(lbl, segc, size=13, style="SemiBold" if sel else "Regular", fill_hex=hexc, name=f"apsl{i}")
r = F(sheet, "Tanggal", layout="horizontal", w="fill", main="space-between", cross="center", key="adt")
tl = F(r, "kiri", layout="vertical", gap=6, key="adtl")
T("Tanggal & waktu", tl, size=13, style="SemiBold", name="adtl1")
tgl = F(tl, "chip", layout="horizontal", gap=8, cross="center", pad=[9, 14], radius=12,
        fill={"$var": "surface-2"}, key="adtch")
icon("calendar", tgl, size=16, color="primary", key="adtci")
T("Besok, 09:00", tgl, size=13, style="SemiBold", name="adtc")
icon("chevron_down", r, size=18, color="text-muted", key="adtch2")
r = F(sheet, "Ingatkan", layout="horizontal", w="fill", main="space-between", cross="center", key="ar")
rl = F(r, "kiri", layout="horizontal", gap=10, cross="center", key="arl")
icon("bell", rl, size=18, color="text-muted", key="arli")
T("Ingatkan saya 10 menit sebelum", rl, size=14, name="arlt")
toggle(r, True, key="art")
button(sheet, "Simpan Tugas", "primary", key="abtn")
F(sheet, "Home Indicator", w=120, h=5, radius=999, fill={"$var": "text-muted"},
  opacity=0.4, layout="horizontal", main="center", sizingH="fill", key="ahi")

# ---- 05 Kalender
scr = screen_frame("05 Kalender", 1892, key="cal")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[6, 20], gap=14, key="cb")
r = F(body, "Header", layout="horizontal", w="fill", main="space-between", cross="center", key="chr")
T("November 2026", r, size=18, style="SemiBold", name="chm")
rr = F(r, "panah", layout="horizontal", gap=8, key="chr2")
for i, icn in enumerate(["chevron_left", "chevron_right"]):
    b = F(rr, f"b{i}", w=32, h=32, radius=999, fill={"$var": "surface-2"},
          layout="horizontal", main="center", cross="center", key=f"chb{i}")
    icon(icn, b, size=16, key=f"chbi{i}")
wk = F(body, "Hari", layout="horizontal", w="fill", key="cwk")
for i, d in enumerate(["Min", "Sen", "Sel", "Rab", "Kam", "Jum", "Sab"]):
    cell = F(wk, f"w{i}", w=45, h=20, layout="horizontal", main="center", cross="center", key=f"cw{i}")
    T(d, cell, size=11.5, style="SemiBold", color="text-muted", name=f"cwd{i}")
grid = F(body, "Tanggal", layout="vertical", gap=2, sizingH="fill", key="cgrid")
HAS_TASKS = {5, 8, 10, 12, 13, 16, 19, 23, 26}
day = 1
for row in range(5):
    rowf = F(grid, f"g{row}", layout="horizontal", gap=2, sizingH="fill", key=f"cg{row}")
    for colx in range(7):
        cell = F(rowf, f"c{day}", w=45, h=48, layout="vertical", gap=3, main="center",
                 cross="center", key=f"cc{day}")
        today = day == 13
        if today:
            circ = F(cell, "hari", w=34, h=34, radius=999, fill={"$var": "primary"},
                     layout="horizontal", main="center", cross="center", key=f"cd{day}")
            T(str(day), circ, size=14, style="SemiBold", color="primary-fg", name=f"ct{day}")
        else:
            T(str(day), cell, size=13.5, style="Regular" if day not in (7, 14, 21, 28) else "Regular",
              color="text" if day in (1, 8, 15, 22, 29) == False else "text", name=f"ct{day}")
        drow = F(cell, "dots", layout="horizontal", gap=2, main="center", key=f"cdd{day}")
        if day in HAS_TASKS:
            dot(drow, 4, {"$var": "primary"} if today else "#B9B9E8", key=f"cdt{day}")
        day += 1
        if day > 30:
            break
    if day > 30:
        break
section_header(body, "Jumat, 13 Nov", "4 tugas", key="cs")
taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#DC2626", key="ct1")
taskcard(body, "Review PR aplikasi mobile", "Pekerjaan", "11:30", "#F59E0B", key="ct2")
taskcard(body, "Belanja bulanan di pasar", "Belanja", "16:00", "#F59E0B", key="ct3")
navbar(scr, "Kalender", key="cnav")

# ---- 06 Profil
scr = screen_frame("06 Profil", 2365, key="prof")
statusbar(scr)
body = F(scr, "Konten", layout="vertical", w="fill", sizingV="fill", pad=[6, 20], gap=14, key="pb")
T("Profil", body, size=18, style="SemiBold", name="pt")
prof = F(body, "Profil", layout="vertical", gap=4, cross="center", sizingH="fill", key="pav")
av = F(prof, "Avatar", w=72, h=72, radius=999, fill={"$var": "primary-soft"},
       layout="horizontal", main="center", cross="center", key="pavc")
T("RP", av, size=24, style="SemiBold", color="primary", name="pavt")
T("Rian Pratama", prof, size=19, style="SemiBold", name="pname")
T("rian.pratama@mail.com", prof, size=13, color="text-muted", name="pmail")
button(prof, "Ubah Profil", "soft", h=36, full=False, w=140, size=13, key="pbtn")
stats = F(body, "Statistik", layout="horizontal", gap=10, sizingH="fill", key="pst")
for i, (val, lbl) in enumerate([("128", "Tugas Selesai"), ("12 hari", "Streak"), ("87", "Skor Fokus")]):
    st = F(stats, f"S/{lbl}", layout="vertical", gap=4, cross="center", main="center",
           radius=14, pad=[12, 0], sizingH="fill", fill={"$var": "surface"},
           stroke={"$var": "border"}, key=f"pst{i}")
    T(val, st, size=18, style="SemiBold", color="primary", name=f"psv{i}")
    T(lbl, st, size=11, color="text-muted", name=f"psl{i}")
T("Pengaturan", body, size=16, style="SemiBold", name="pset")
listw = F(body, "Daftar", layout="vertical", gap=10, sizingH="fill", key="plist")
rows = [("bell", "Notifikasi", "toggle", True),
        ("moon", "Tema Gelap", "toggle", False),
        ("sliders", "Sinkronisasi", "chev", None),
        ("logout", "Bantuan & Masukan", "chev", None)]
for i, (icn, lbl, kind, ton) in enumerate(rows):
    r = F(listw, f"R/{lbl}", layout="horizontal", w="fill", h=52, pad=[0, 14],
          radius=14, cross="center", main="space-between", fill={"$var": "surface"},
          stroke={"$var": "border"}, key=f"pr{i}")
    rr = F(r, "kiri", layout="horizontal", gap=12, cross="center", key=f"prl{i}")
    ic = F(rr, "ikon", w=32, h=32, radius=10, fill={"$var": "surface-2"},
           layout="horizontal", main="center", cross="center", key=f"pri{i}")
    icon(icn, ic, size=17, color="text-muted", key=f"pric{i}")
    T(lbl, rr, size=14, name=f"prt{i}")
    if kind == "toggle":
        toggle(r, ton, key=f"prtg{i}")
    else:
        icon("chevron_right", r, size=16, color="text-muted", key=f"prc{i}")
button(body, "Keluar", "danger", key="pout")
navbar(scr, "Profil", key="pnav")

# ---- 07 Beranda Gelap (duplikat 03)
dup_ref = S("edit.duplicate", {"ids": [home_ref], "dx": 473 * 6, "dy": 0}, as_name="darkdup")
dark_id = {**dup_ref, "field": "ids/0"}
S("object.rename", {"ids": [dark_id], "name": "07 Beranda — Gelap"})
S("variable.setMode", {"ids": [dark_id], "collection": "Warna", "mode": "Gelap"})

# ================================================================ HALAMAN 3
p3 = S("page.add", {"name": "🖥️ Responsive"}, as_name="p3")
S("page.select", {"id": p3})

# ---- Tablet 744×1133
tab = F(None, "Beranda — Tablet", w=744, h=1133, radius=0, fill={"$var": "bg"},
        layout="vertical", clip=True, x=0, y=0, key="tab")
statusbar(tab)
tbody = F(tab, "Isi", layout="horizontal", w="fill", sizingV="fill", key="tb")
rail = F(tbody, "Rail", layout="vertical", w=84, pad=[16, 16, 16, 16], gap=18,
         fill={"$var": "surface"}, stroke={"$var": "border"}, sw=1, cross="center", key="tr")
logo = F(rail, "Logo", w=44, h=44, radius=14, fill={"$var": "primary"},
         layout="horizontal", main="center", cross="center", key="trlogo")
icon("check", logo, size=22, sw=3, fill_hex="#FFFFFF", key="trlogoi")
railitems = [("home", "Beranda"), ("calendar", "Kalender"), ("chart", "Statistik"), ("user", "Profil")]
for i, (icn, lbl) in enumerate(railitems):
    act = i == 0
    it = F(rail, f"M/{lbl}", layout="vertical", gap=4, cross="center", main="center",
           w=56, h=56, radius=14, fill={"$var": "primary-soft"} if act else "none", key=f"tri{i}")
    icon(icn, it, size=20, color="primary" if act else "text-muted", key=f"tric{i}")
    T(lbl, it, size=9.5, style="SemiBold" if act else "Regular",
      color="primary" if act else "text-muted", name=f"tril{i}")
tmain = F(tbody, "Utama", layout="vertical", sizingH="fill", sizingV="fill", pad=[24], gap=16, key="tm")
r = F(tmain, "Header", layout="horizontal", w="fill", main="space-between", cross="center", key="tmh")
gcol = F(r, "Sapaan", layout="vertical", gap=4, key="tmhc")
T("Halo, Rian 👋", gcol, size=24, style="SemiBold", name="tmh1")
T("Jumat, 13 November 2026", gcol, size=13, color="text-muted", name="tmh2")
srch = F(r, "Cari", layout="horizontal", gap=10, cross="center", w=220, h=42, radius=999,
         fill={"$var": "surface"}, stroke={"$var": "border"}, pad=[0, 16], key="tms")
icon("search", srch, size=16, color="text-muted", key="tmsi")
T("Cari tugas…", srch, size=13, color="text-muted", name="tmst")
progress_card(tmain, key="tmp")
chips = F(tmain, "Filter", layout="horizontal", gap=8, sizingH="fill", key="tmc")
chip(chips, "Semua", selected=True, key="tmc1")
chip(chips, "Pekerjaan", key="tmc2")
chip(chips, "Pribadi", key="tmc3")
chip(chips, "Belanja", key="tmc4")
chip(chips, "Kesehatan", key="tmc5")
gridw = F(tmain, "Tugas", layout="vertical", gap=10, sizingH="fill", sizingV="fill", key="tmg")
gr = F(gridw, "Baris1", layout="horizontal", gap=12, sizingH="fill", key="tmg1")
boxa = F(gr, "A", layout="horizontal", sizingH="fill", key="tmg1a")
taskcard(boxa, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00", "#DC2626", key="tmt1")
boxb = F(gr, "B", layout="horizontal", sizingH="fill", key="tmg1b")
taskcard(boxb, "Belanja bulanan di pasar", "Belanja", "16:00", "#F59E0B", key="tmt2")
gr = F(gridw, "Baris2", layout="horizontal", gap=12, sizingH="fill", key="tmg2")
boxc = F(gr, "C", layout="horizontal", sizingH="fill", key="tmg2a")
taskcard(boxc, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#16A34A", done=True, key="tmt3")
boxd = F(gr, "D", layout="horizontal", sizingH="fill", key="tmg2b")
taskcard(boxd, "Olahraga pagi: lari 5 km", "Pribadi", "06:00", "#16A34A", key="tmt4")

# ---- Desktop 1440×1024
desk = F(None, "Beranda — Desktop", w=1440, h=1024, radius=0, fill={"$var": "bg"},
         layout="horizontal", clip=True, x=844, y=0, key="desk")
side = F(desk, "Sidebar", layout="vertical", w=264, sizingV="fill", pad=20, gap=8,
         fill={"$var": "surface"}, stroke={"$var": "border"}, sw=1, key="dside")
logo = F(side, "Logo", layout="horizontal", gap=10, cross="center", pad=[4, 4, 16, 4], key="dlogo")
mark = F(logo, "m", w=38, h=38, radius=12, fill={"$var": "primary"},
         layout="horizontal", main="center", cross="center", key="dlogom")
icon("check", mark, size=20, sw=3, fill_hex="#FFFFFF", key="dlogoi")
T("TaskKu", logo, size=20, style="Bold", name="dlogot")
for i, (icn, lbl, act) in enumerate([("home", "Beranda", True), ("calendar", "Kalender", False),
                                     ("chart", "Statistik", False), ("user", "Profil", False)]):
    it = F(side, f"M/{lbl}", layout="horizontal", gap=12, cross="center", w="fill", h=44,
           radius=12, pad=[0, 12], fill={"$var": "primary-soft"} if act else "none", key=f"dm{i}")
    icon(icn, it, size=19, color="primary" if act else "text-muted", key=f"dmi{i}")
    T(lbl, it, size=14, style="SemiBold" if act else "Regular",
      color="primary" if act else "text", name=f"dml{i}")
prog = F(side, "Progres", layout="vertical", gap=8, w="fill", radius=14, pad=14,
         fill={"$var": "primary-soft"}, key="dprog")
T("Progres minggu ini", prog, size=12, style="SemiBold", name="dprog1")
tr = F(prog, "Track", layout="horizontal", w="fill", h=8, radius=999, fill={"$var": "border"}, key="dprogtr")
F(tr, "Fill", w=96, h=8, radius=999, fill={"$var": "primary"}, key="dprogf")
T("24 dari 40 tugas selesai", prog, size=11, color="text-muted", name="dprog2")
usr = F(side, "Pengguna", layout="horizontal", gap=10, cross="center", w="fill", h=52,
        radius=12, pad=[0, 10], fill={"$var": "surface-2"}, key="dusr")
av = F(usr, "Avatar", w=34, h=34, radius=999, fill={"$var": "primary-soft"},
       layout="horizontal", main="center", cross="center", key="dusrav")
T("R", av, size=13, style="SemiBold", color="primary", name="dusri")
ucol = F(usr, "nama", layout="vertical", gap=2, sizingH="fill", key="dusrc")
T("Rian Pratama", ucol, size=13, style="SemiBold", name="dusun")
T("Paket Pro", ucol, size=10.5, color="text-muted", name="dusup")
icon("chevron_right", usr, size=14, color="text-muted", key="dusrc2")
dmain = F(desk, "Utama", layout="vertical", sizingH="fill", sizingV="fill", pad=[28], gap=20, key="dmn")
top = F(dmain, "Atas", layout="horizontal", w="fill", main="space-between", cross="center", key="dtop")
tcol = F(top, "Judul", layout="vertical", gap=4, key="dtopc")
T("Hari Ini", tcol, size=26, style="SemiBold", name="dtop1")
T("Kamis? Jumat, 13 November 2026 — 5 tugas aktif", tcol, size=13, color="text-muted", name="dtop2")
srch = F(top, "Cari", layout="horizontal", gap=10, cross="center", w=320, h=42, radius=999,
         fill={"$var": "surface"}, stroke={"$var": "border"}, pad=[0, 16], key="dsrch")
icon("search", srch, size=16, color="text-muted", key="dsrchi")
T("Cari tugas, kategori, atau catatan…", srch, size=13, color="text-muted", name="dsrcht")
kanban = F(dmain, "Kanban", layout="horizontal", gap=16, sizingH="fill", sizingV="fill", key="dkan")
cols = [("Hari Ini", "#5757D9", [("Kirim laporan mingguan", "Pekerjaan", "08:00", True),
                                 ("Rapat sprint dengan tim desain", "Pekerjaan", "09:00", False),
                                 ("Belanja bulanan di pasar", "Belanja", "16:00", False)]),
        ("Terjadwal", "#F59E0B", [("Kontrol dokter gigi", "Kesehatan", "Besok 08:30", False),
                                  ("Olahraga pagi: lari 5 km", "Pribadi", "Besok 06:00", False)]),
        ("Selesai", "#16A34A", [("Setor sampah & pilah", "Pribadi", "07:00", True),
                                ("Bayar tagihan internet", "Belanja", "10:00", True)])]
for ci, (title, dotc, cards) in enumerate(cols):
    col = F(kanban, f"Kolom/{title}", layout="vertical", gap=12, sizingH="fill", key=f"dkc{ci}")
    head = F(col, "Judul", layout="horizontal", w="fill", gap=8, cross="center", key=f"dkh{ci}")
    dot(head, 10, dotc, key=f"dkd{ci}")
    T(title, head, size=15, style="SemiBold", name=f"dkhl{ci}")
    pill = F(head, "hitung", layout="horizontal", pad=[2, 9], radius=999,
             fill={"$var": "surface-2"}, key=f"dkp{ci}")
    T(str(len(cards)), pill, size=11.5, style="SemiBold", color="text-muted", name=f"dkpl{ci}")
    for ki, (t, c, tm, dn) in enumerate(cards):
        taskcard(col, t, c, tm, dotc, done=dn, key=f"dk{ci}{ki}")

# ---------------------------------------------------------------- tulis
with open(OUT, "w") as f:
    json.dump(cmds, f, ensure_ascii=False)
print(f"{len(cmds)} perintah -> {OUT}")
