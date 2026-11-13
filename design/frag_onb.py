#!/usr/bin/env python3
"""frag_onb — 4 layar TaskKu: Onboarding Prioritas/Progres + Beranda/Kalender kosong.

Bagian dari kit TaskKu (lihat figkit.py untuk API). build() mengembalikan
(cmds, refs); refs disarangkan per layar: {"18": {"lanjut", "masuk"}, ...}.

build(test=True) menambahkan prelude koleksi variabel "Warna" (Terang/Gelap)
agar fragmen bisa diuji berdiri sendiri di dokumen kosong.
"""
import json
import os

from figkit import Kit, VARS, GRAD, SH_CARD, SH_FLOAT


def _blobs(k, scr):
    """Dua blob gradient blur dekoratif, seperti layar 01 Onboarding."""
    k.F(scr, "Blob1", w=280, h=280, radius=999, fill=GRAD, opacity=0.35,
        effects=[{"type": "layerBlur", "radius": 90, "visible": True}],
        absolute=True, x=190, y=-90, key="blob1")
    k.F(scr, "Blob2", w=240, h=240, radius=999, fill="#9F7AEA", opacity=0.22,
        effects=[{"type": "layerBlur", "radius": 90, "visible": True}],
        absolute=True, x=-80, y=620, key="blob2")


def _footer_masuk(k, body, key):
    row = k.F(body, "MasukRow", layout="horizontal", gap=5, main="center",
              sizingH="fill", key=key)
    k.T("Sudah punya akun?", row, size=13.5, color="text-muted", name=key + "1")
    return k.T("Masuk", row, size=13.5, style="SemiBold", color="primary",
               name=key + "2")


def _dots(k, body, active, key):
    """Tiga indikator slide; `active` = indeks pill 22x8 yang menyala."""
    dots = k.F(body, "Dots", layout="horizontal", gap=7, cross="center",
               main="center", sizingH="fill", key=key)
    for i in range(3):
        if i == active:
            k.F(dots, f"d{i}", w=22, h=8, radius=999, fill={"$var": "primary"},
                key=f"{key}p{i}")
        else:
            k.dot(dots, 8, {"$var": "border"}, key=f"{key}d{i}")


def build(test=False):
    k = Kit("ob")
    refs = {}
    if test:
        k.S("variable.createCollection", {"name": "Warna", "modes": ["Terang", "Gelap"]})
        for vname, (light, dark) in VARS.items():
            k.S("variable.create", {"collection": "Warna", "name": vname, "type": "color",
                                    "values": {"Terang": light, "Gelap": dark}})

    # ---- 18 Onboarding — Prioritas
    scr = k.screen_frame("18 Onboarding — Prioritas", 8041, key="s18")
    _blobs(k, scr)
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[10, 28], gap=20, main="center", cross="center", key="b18")
    ill = k.F(body, "Ilustrasi", w=340, h=250, layout="horizontal", main="center",
              cross="center", key="i18")
    k.F(ill, "Lingkaran", w=220, h=220, radius=999, fill={"$var": "primary-soft"},
        key="cir18")
    card = k.F(ill, "Kartu", w=200, h=190, radius=24, fill={"$var": "surface"},
               effects=SH_CARD, layout="vertical", pad=[16, 18], gap=12,
               absolute=True, x=70, y=30, key="card18")
    hd = k.F(card, "hd", layout="horizontal", w="fill", main="space-between",
             cross="center", key="hd18")
    k.T("Prioritas", hd, size=12.5, style="SemiBold", name="hd18t")
    pill = k.F(hd, "n", layout="horizontal", pad=[2, 9], radius=999,
               fill={"$var": "primary-soft"}, key="pil18")
    k.T("3", pill, size=11, style="SemiBold", color="primary", name="pil18t")
    for i, (bw, col) in enumerate([(104, "#E5484D"), (88, "#F79009"), (76, "#12B76A")]):
        row = k.F(card, f"r{i}", layout="horizontal", gap=10, cross="center",
                  key=f"r18{i}")
        k.icon("flag", row, size=16, fill_hex=col, sw=2, key=f"fl18{i}")
        k.F(row, "bar", w=bw, h=9, radius=5, fill={"$var": "surface-2"},
            key=f"bar18{i}")
    badge = k.F(ill, "Badge", w=54, h=54, radius=999, fill={"$var": "surface"},
                layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
                absolute=True, x=228, y=10, key="bd18")
    k.icon("flag", badge, size=22, color="primary", key="bdi18")
    badge2 = k.F(ill, "Badge2", w=44, h=44, radius=999, fill={"$var": "surface"},
                 layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
                 absolute=True, x=10, y=178, key="bd218")
    k.icon("zap", badge2, size=18, fill_hex="#F79009", key="bd2i18")
    k.dot(ill, 16, "#FFD66B", absolute=True, x=252, y=28, key="dt118")
    k.dot(ill, 10, "#5B54F0", absolute=True, x=28, y=204, key="dt218")
    k.T("Tetapkan prioritas,\ntepat waktu.", body, size=28, style="SemiBold",
        align="center", ls="-2%", lh="128%", name="j18")
    k.T("Tandai yang penting, pantau deadline dengan penanda prioritas.", body,
        size=14.5, color="text-muted", align="center", lh="160%", width=310,
        name="sbt18")
    _dots(k, body, active=1, key="dots18")
    refs["18"] = {
        "lanjut": k.button(body, "Lanjut", "secondary", h=52, key="btn18"),
        "masuk": _footer_masuk(k, body, "fm18"),
    }
    refs["18"]["frame"] = scr

    # ---- 19 Onboarding — Progres
    scr = k.screen_frame("19 Onboarding — Progres", 8514, key="s19")
    _blobs(k, scr)
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[10, 28], gap=20, main="center", cross="center", key="b19")
    ill = k.F(body, "Ilustrasi", w=340, h=250, layout="horizontal", main="center",
              cross="center", key="i19")
    k.F(ill, "Lingkaran", w=220, h=220, radius=999, fill={"$var": "primary-soft"},
        key="cir19")
    card = k.F(ill, "Kartu", w=200, h=190, radius=24, fill={"$var": "surface"},
               effects=SH_CARD, layout="vertical", pad=[18, 18], gap=14,
               main="center", absolute=True, x=70, y=30, key="card19")
    k.ring(card, 37, key="ring19", size=72, lblsize=14)
    k.F(card, "bar1", w=120, h=9, radius=5, fill={"$var": "surface-2"},
        key="bar19a")
    k.F(card, "bar2", w=90, h=9, radius=5, fill={"$var": "surface-2"},
        key="bar19b")
    badge = k.F(ill, "Badge", w=44, h=44, radius=999, fill={"$var": "surface"},
                layout="horizontal", main="center", cross="center", effects=SH_FLOAT,
                absolute=True, x=10, y=178, key="bd19")
    k.icon("calendar", badge, size=18, color="primary", key="bdi19")
    k.dot(ill, 16, "#FFD66B", absolute=True, x=252, y=28, key="dt119")
    k.dot(ill, 10, "#5B54F0", absolute=True, x=28, y=204, key="dt219")
    k.T("Pantau progresmu,\nsetiap hari.", body, size=28, style="SemiBold",
        align="center", ls="-2%", lh="128%", name="j19")
    k.T("Streak, statistik, dan capaian harian tersaji dalam satu ringkasan.",
        body, size=14.5, color="text-muted", align="center", lh="160%", width=310,
        name="sbt19")
    _dots(k, body, active=2, key="dots19")
    refs["19"] = {
        "mulai": k.button(body, "Mulai Sekarang", "primary", h=54, key="btn19"),
        "masuk": _footer_masuk(k, body, "fm19"),
    }
    refs["19"]["frame"] = scr

    # ---- 20 Beranda — Kosong
    scr = k.screen_frame("20 Beranda — Kosong", 8987, key="s20")
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[2, 24, 112, 24], gap=14, key="b20")
    k.hero_card(body, key="hero20")
    k.progress_card(body, key="ep20", pct=0, done=0, total=0,
                    note="Mulai hari pertamamu dengan satu tugas.")
    chips = k.F(body, "Filter", layout="horizontal", gap=8, w="fill", key="ch20")
    k.chip(chips, "Semua", selected=True, key="ch20a")
    empty = k.F(body, "Kosong", layout="vertical", w="fill", sizingV="fill",
                main="center", cross="center", gap=12, key="em20")
    circ = k.F(empty, "Lingkaran", w=150, h=150, radius=999,
               fill={"$var": "primary-soft"}, layout="horizontal", main="center",
               cross="center", key="cir20")
    k.icon("inbox", circ, size=52, color="primary", sw=1.75, key="in20")
    k.T("Belum ada tugas", empty, size=18, style="SemiBold", name="e20t")
    k.T("Ketuk tombol + untuk membuat\ntugas pertamamu.", empty, size=13.5,
        color="text-muted", align="center", lh="150%", name="e20s")
    _, drefs20 = k.dock_bar(scr, "Beranda", key="dk20", x=16, y=774)
    refs["20"] = {"fab": k.fab(scr, key="fab20", x=311, y=698), "dock": drefs20, "frame": scr}

    # ---- 21 Kalender — Kosong
    scr = k.screen_frame("21 Kalender — Kosong", 9460, key="s21")
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[2, 24, 112, 24], gap=12, key="b21")
    hdr = k.F(body, "Header", layout="horizontal", w="fill", main="space-between",
              cross="center", key="h21")
    k.T("November 2026", hdr, size=19, style="SemiBold", ls="-1%", name="h21t")
    nav = k.F(hdr, "panah", layout="horizontal", gap=8, key="nav21")
    for i, icn in enumerate(["chevron_left", "chevron_right"]):
        b = k.F(nav, f"b{i}", w=36, h=36, radius=999, fill={"$var": "surface"},
                effects=SH_CARD, layout="horizontal", main="center", cross="center",
                key=f"nv21{i}")
        k.icon(icn, b, size=16, key=f"nvi21{i}")
    wk = k.F(body, "Hari", layout="horizontal", w="fill", key="wk21")
    for i, dd in enumerate(["MIN", "SEN", "SEL", "RAB", "KAM", "JUM", "SAB"]):
        cell = k.F(wk, f"w{i}", w=45, h=20, layout="horizontal", main="center",
                   cross="center", key=f"wk21{i}")
        k.T(dd, cell, size=9.5, style="SemiBold", color="text-muted", ls="6%",
            name=f"wkt{i}")
    grid = k.F(body, "Tanggal", layout="vertical", gap=2, sizingH="fill", key="gr21")
    day = 1
    for rowi in range(5):
        rowf = k.F(grid, f"g{rowi}", layout="horizontal", gap=2, sizingH="fill",
                   key=f"g21{rowi}")
        for colx in range(7):
            cell = k.F(rowf, f"c{day}", w=45, h=44, layout="horizontal",
                       main="center", cross="center", key=f"c21{day}")
            if day <= 30:
                k.T(str(day), cell, size=13, color="text", name=f"t21{day}")
            day += 1
    empty = k.F(body, "Kosong", layout="vertical", w="fill", sizingV="fill",
                main="center", cross="center", gap=12, key="em21")
    circ = k.F(empty, "Lingkaran", w=140, h=140, radius=999,
               fill={"$var": "surface-2"}, layout="horizontal", main="center",
               cross="center", key="cir21")
    k.icon("calendar", circ, size=48, color="text-muted", sw=1.75, key="cal21")
    k.T("Tidak ada tugas pada tanggal ini", empty, size=16, style="SemiBold",
        align="center", name="e21t")
    k.T("Pilih tanggal lain atau buat tugas baru lewat tombol +.", empty, size=13,
        color="text-muted", align="center", width=280, lh="150%", name="e21s")
    _, drefs21 = k.dock_bar(scr, "Kalender", key="dk21", x=16, y=774)
    refs["21"] = {"fab": k.fab(scr, key="fab21", x=311, y=698), "dock": drefs21, "frame": scr}

    return k.cmds, refs


if __name__ == "__main__":
    cmds, _ = build(test=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frag_onb.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(cmds, f, ensure_ascii=False)
    print(f"{len(cmds)} command ditulis ke {out}")
