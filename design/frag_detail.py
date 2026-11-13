#!/usr/bin/env python3
"""frag_detail.py — fragmen layar TaskKu: "12 Detail Tugas" & "13 Hapus Tugas".

build(test=False) -> (cmds, refs). Saat test=True, PRELUDE (koleksi variabel
"Warna" + 12 variable.create dari figkit.VARS) disisipkan di awal agar file
uji mandiri. __main__ menulis frag_detail.json dari build(test=True).
"""
import json
import os

from figkit import Kit, VARS, SH_CARD, SH_FLOAT, PHONE_W, PHONE_H

PRELUDE = [
    {"command": "variable.createCollection",
     "params": {"name": "Warna", "modes": ["Terang", "Gelap"]}},
]
for _n, (_l, _d) in VARS.items():
    PRELUDE.append({"command": "variable.create",
                    "params": {"collection": "Warna", "name": _n, "type": "color",
                               "values": {"Terang": _l, "Gelap": _d}}})


def build(test=False):
    k = Kit("dt")
    refs = {}

    # ================= 12 Detail Tugas =================
    scr = k.screen_frame("12 Detail Tugas", 5203, key="s12")
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[6, 24, 10, 24], gap=14, key="b12")

    # Header: tombol back + spacer + tombol kebab
    hdr = k.F(body, "Header", layout="horizontal", w="fill", main="space-between",
              cross="center", key="h12")
    back = k.F(hdr, "Kembali", w=44, h=44, radius=999, fill={"$var": "surface"},
               effects=SH_CARD, layout="horizontal", main="center", cross="center",
               key="back12")
    k.icon("chevron_left", back, size=20, key="backi12")
    k.F(hdr, "Spacer", sizingH="fill", h=1, key="hsp12")
    kebab = k.F(hdr, "Menu", w=44, h=44, radius=999, fill={"$var": "surface"},
                effects=SH_CARD, layout="horizontal", main="center", cross="center",
                key="kebab12")
    k.icon("kebab", kebab, size=20, color="text-muted", key="kebabi12")

    # Judul + baris meta
    k.T("Rapat sprint dengan tim desain", body, size=22, style="SemiBold",
        ls="-1.5%", name="judul12")
    meta = k.F(body, "Meta", layout="horizontal", gap=8, cross="center", key="m12")
    cat = k.F(meta, "Chip/Kategori", layout="horizontal", gap=5, cross="center",
              pad=[4, 10], radius=999, fill="#ECEBFE", key="mcat12")
    k.dot(cat, 5, "#5B54F0", key="mcatd12")
    k.T("Pekerjaan", cat, size=11, style="SemiBold", fill_hex="#5B54F0",
        name="mcatl12")
    prio = k.F(meta, "Chip/Prioritas", layout="horizontal", cross="center",
               pad=[4, 10], radius=999, fill="#FDEBEB", key="mpri12")
    k.T("Tinggi", prio, size=11, style="SemiBold", fill_hex="#E5484D",
        name="mpril12")
    waktu = k.F(meta, "Waktu", layout="horizontal", gap=5, cross="center",
                key="mwk12")
    k.icon("clock", waktu, size=12.5, color="text-muted", sw=2, key="mwki12")
    k.T("Hari ini, 09:00", waktu, size=11.5, color="text-muted", name="mwkl12")

    # Kartu deskripsi
    dcard = k.F(body, "Kartu Deskripsi", layout="vertical", w="fill", radius=20,
                fill={"$var": "surface"}, pad=16, gap=8, effects=SH_CARD, key="dc12")
    k.micro(dcard, "DESKRIPSI", key="dcm12")
    k.T("Menyiapkan materi sprint review: progres desain, umpan balik pengguna, "
        "dan rencana iterasi berikutnya.", dcard, size=14, lh="150%", color="text",
        width=313, name="dct12")  # lebar konten kartu (345 - pad 16*2)

    # Kartu subtugas
    scard = k.F(body, "Kartu Subtugas", layout="vertical", w="fill", radius=20,
                fill={"$var": "surface"}, pad=14, gap=10, effects=SH_CARD, key="sc12")
    shead = k.F(scard, "Kepala", layout="horizontal", w="fill",
                main="space-between", cross="center", key="sch12")
    k.micro(shead, "SUBTUGAS", key="scm12")
    pill = k.F(shead, "Hitung", layout="horizontal", pad=[2, 8], radius=999,
               fill={"$var": "surface-2"}, cross="center", key="scp12")
    k.T("1/3", pill, size=10.5, style="SemiBold", color="text-muted", name="scpl12")
    subtasks = [
        ("Siapkan deck terbaru", True),
        ("Review umpan balik desain", False),
        ("Kirim undangan rapat", False),
    ]
    for i, (label, done) in enumerate(subtasks):
        row = k.F(scard, f"Sub{i}", layout="horizontal", gap=10, cross="center",
                  key=f"scr{i}12")
        if done:
            cb = k.F(row, "Cek", w=22, h=22, radius=999, fill={"$var": "primary"},
                     layout="horizontal", main="center", cross="center",
                     key=f"scc{i}12")
            k.icon("check", cb, size=12, sw=3, fill_hex="#FFFFFF", key=f"scck{i}12")
        else:
            cb = k.F(row, "Cek", w=22, h=22, radius=999, stroke={"$var": "border"},
                     sw=2, key=f"scc{i}12")
        k.T(label, row, size=14, style="Regular" if done else "Medium",
            color="text-muted" if done else "text",
            deco="strikethrough" if done else None, name=f"sct{i}12")

    # Kartu pengingat
    rcard = k.F(body, "Kartu Pengingat", layout="horizontal", w="fill", radius=20,
                fill={"$var": "surface"}, pad=14, main="space-between",
                cross="center", effects=SH_CARD, key="rc12")
    rleft = k.F(rcard, "Kiri", layout="horizontal", gap=12, cross="center",
                key="rcl12")
    rbox = k.F(rleft, "Kotak", w=32, h=32, radius=10, fill={"$var": "surface-2"},
               layout="horizontal", main="center", cross="center", key="rcb12")
    k.icon("bell", rbox, size=16, color="text-muted", key="rcbi12")
    k.T("Pengingat 10 menit sebelumnya", rleft, size=14, name="rclt12")
    k.toggle(rcard, True, key="rt12")

    # Spacer pengisi
    k.F(body, "Spacer", sizingV="fill", fill="none", key="bsp12")

    # Baris aksi bawah
    aksi = k.F(body, "Aksi", layout="horizontal", w="fill", gap=12, key="ak12")
    edit = k.F(aksi, "Btn/Edit", layout="horizontal", h=52, radius=999,
               stroke={"$var": "border"}, fill={"$var": "surface"}, main="center",
               cross="center", gap=8, sizingH="fill", key="ed12")
    k.icon("pencil", edit, size=17, color="primary", key="edi12")
    k.T("Edit", edit, size=15, style="SemiBold", color="primary", name="edt12")
    hapus = k.F(aksi, "Btn/Hapus", layout="horizontal", h=52, radius=999,
                stroke="#E5484D", sw=1, main="center", cross="center", gap=8,
                sizingH="fill", key="hp12")
    k.icon("trash", hapus, size=17, fill_hex="#E5484D", key="hpi12")
    k.T("Hapus", hapus, size=15, style="SemiBold", fill_hex="#E5484D",
        name="hpt12")

    # Home indicator
    k.F(body, "Home Indicator", w=120, h=5, radius=999, fill={"$var": "text-muted"},
        opacity=0.4, layout="horizontal", main="center", sizingH="fill", key="hi12")

    # refs disarangkan per layar agar "hapus" (12) dan "hapus" (13) tak saling
    # menimpa — pola sama dengan frag_onb.py
    refs["12"] = {"back": back, "kebab": kebab, "edit": edit, "hapus": hapus, "frame": scr}

    # ================= 13 Hapus Tugas =================
    scr2 = k.screen_frame("13 Hapus Tugas", 5676, key="s13")
    k.statusbar(scr2)

    # Konten redup di belakang dialog
    bgc = k.F(scr2, "Konten Redup", layout="vertical", w="fill", sizingV="fill",
              pad=[2, 24], gap=14, opacity=0.32, key="b13")
    k.hero_card(bgc, key="hero13")
    k.taskcard(bgc, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00",
               "#E5484D", key="tc13")

    # Scrim digambar setelah konten
    scrim = k.F(scr2, "Scrim", w=PHONE_W, h=PHONE_H, fill="#13131966",
                absolute=True, x=0, y=0, key="scrim13")

    # Kartu dialog konfirmasi
    dlg = k.F(scr2, "Dialog Hapus", layout="vertical", w=321, radius=24,
              fill={"$var": "surface"}, pad=[24, 24, 20, 24], gap=14,
              effects=SH_FLOAT, cross="center", absolute=True, x=36, y=320,
              key="dlg13")
    dico = k.F(dlg, "Kotak Ikon", w=60, h=60, radius=999, fill="#FDEBEB",
               layout="horizontal", main="center", cross="center", key="dico13")
    k.icon("trash", dico, size=26, fill_hex="#E5484D", key="dtri13")
    k.T("Hapus tugas?", dlg, size=18, style="SemiBold", align="center",
        name="djt13")
    k.T("Tugas \u201cRapat sprint dengan tim desain\u201d akan dihapus permanen. "
        "Tindakan ini tidak bisa dibatalkan.", dlg, size=13, color="text-muted",
        align="center", lh="150%", width=273, name="dbt13")  # 321 - pad 24*2
    drow = k.F(dlg, "Tombol", layout="horizontal", gap=10, w="fill", key="drow13")
    refs["13"] = {"batal": k.button(drow, "Batal", "secondary", h=46, key="batal13"),
                  "hapus": k.button(drow, "Hapus", "danger", h=46, key="hapus13")}

    # Home indicator (absolut agar tidak terdorong konten fill)
    k.F(scr2, "Home Indicator", w=120, h=5, radius=999,
        fill={"$var": "text-muted"}, opacity=0.4, absolute=True, x=136.5, y=839,
        key="hi13")

    refs["13"]["scrim"] = scrim
    refs["13"]["frame"] = scr2

    cmds = (PRELUDE if test else []) + k.cmds
    return cmds, refs


if __name__ == "__main__":
    _cmds, _ = build(test=True)
    _out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frag_detail.json")
    with open(_out, "w", encoding="utf-8") as _f:
        json.dump(_cmds, _f, ensure_ascii=False)
    print(f"frag_detail.json: {len(_cmds)} command")
