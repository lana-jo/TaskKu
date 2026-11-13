#!/usr/bin/env python3
"""frag_lists.py — fragmen layar TaskKu: "14 Daftar Tugas" & "15 Pencarian".

build(test=False) -> (cmds, refs). Saat test=True, PRELUDE (koleksi variabel
"Warna" + 12 variable.create dari figkit.VARS) disisipkan di awal agar file
uji mandiri. __main__ menulis frag_lists.json dari build(test=True).
"""
import json
import os

from figkit import Kit, VARS, SH_CARD

PRELUDE = [
    {"command": "variable.createCollection",
     "params": {"name": "Warna", "modes": ["Terang", "Gelap"]}},
]
for _n, (_l, _d) in VARS.items():
    PRELUDE.append({"command": "variable.create",
                    "params": {"collection": "Warna", "name": _n, "type": "color",
                               "values": {"Terang": _l, "Gelap": _d}}})


def build(test=False):
    k = Kit("ls")
    refs = {}

    # ================= 14 Daftar Tugas =================
    scr = k.screen_frame("14 Daftar Tugas", 6149, key="ls14")
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[2, 24, 112, 24], gap=12, key="lsb")

    # Header: tombol back + judul + pill hitung + spacer
    hdr = k.F(body, "Header", layout="horizontal", w="fill", gap=10,
              cross="center", key="lshdr")
    back = k.F(hdr, "Kembali", w=44, h=44, radius=999, fill={"$var": "surface"},
               effects=SH_CARD, layout="horizontal", main="center", cross="center",
               key="lsback")
    k.icon("chevron_left", back, size=20, key="lsbacki")
    k.T("Semua Tugas", hdr, size=19, style="SemiBold", ls="-1%", name="lsjudul")
    pill = k.F(hdr, "Hitung", layout="horizontal", pad=[3, 10], radius=999,
               fill={"$var": "surface-2"}, cross="center", key="lspill")
    k.T("9", pill, size=11.5, style="SemiBold", color="text-muted", name="lspillt")
    k.F(hdr, "Spacer", sizingH="fill", h=1, key="lssp")

    # Chips filter
    chips = k.F(body, "Filter", layout="horizontal", gap=8, w="fill", key="lsch")
    k.chip(chips, "Semua", selected=True, key="lsch1")
    k.chip(chips, "Hari Ini", key="lsch2")
    k.chip(chips, "Terjadwal", key="lsch3")
    k.chip(chips, "Selesai", key="lsch4")

    # Seksi: Hari Ini
    k.micro(body, "HARI INI — 3 TUGAS", key="lsm1")
    k.taskcard(body, "Kirim laporan mingguan", "Pekerjaan", "08:00", "#12B76A",
               done=True, key="lst1")
    k.taskcard(body, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00",
               "#E5484D", key="lst2")
    k.taskcard(body, "Belanja bulanan di pasar", "Belanja", "16:00", "#F79009",
               key="lst3")

    # Seksi: Terjadwal
    k.micro(body, "TERJADWAL — 2 TUGAS", key="lsm2")
    k.taskcard(body, "Kontrol dokter gigi", "Kesehatan", "Besok 08:30", "#E5484D",
               key="lst4")
    k.taskcard(body, "Olahraga pagi: lari 5 km", "Pribadi", "Besok 06:00",
               "#12B76A", key="lst5")

    # Seksi: Selesai
    k.micro(body, "SELESAI — 1 TUGAS", key="lsm3")
    k.taskcard(body, "Setor sampah & pilah", "Pribadi", "07:00", "#12B76A",
               done=True, key="lst6")

    _, drefs = k.dock_bar(scr, "Beranda", key="lsd", x=16, y=774)
    refs["back"] = back
    refs["frame14"] = scr
    refs["dock"] = drefs  # dock layar 14 (list 4 item)

    # ================= 15 Pencarian =================
    scr2 = k.screen_frame("15 Pencarian", 6622, key="ls15")
    k.statusbar(scr2)
    body2 = k.F(scr2, "Konten", layout="vertical", w="fill", sizingV="fill",
                pad=[2, 24, 112, 24], gap=12, key="lsb2")

    # Baris pencarian: field pill + tombol Batal
    srow = k.F(body2, "Pencarian", layout="horizontal", w="fill", gap=10,
               cross="center", key="lssr")
    fld = k.F(srow, "Field", layout="horizontal", h=46, radius=999,
              fill={"$var": "surface-2"}, pad=[0, 16], gap=8, cross="center",
              sizingH="fill", key="lsfld")
    k.icon("search", fld, size=17, color="text-muted", key="lsfldi")
    k.T("rap", fld, size=15, style="Medium", color="text", name="lsq")
    clr = k.F(fld, "Clear", w=22, h=22, radius=999, fill={"$var": "border"},
              layout="horizontal", main="center", cross="center", key="lsclr")
    k.icon("x", clr, size=12, fill_hex="#FFFFFF", sw=2.5, key="lsclri")
    batal = k.T("Batal", srow, size=13.5, style="SemiBold", color="primary",
                name="lsbatal")

    # Riwayat pencarian
    k.micro(body2, "PENCARIAN TERAKHIR", key="lsm4")
    hist = k.F(body2, "Riwayat", layout="vertical", pad=[8, 14], radius=20,
               fill={"$var": "surface"}, effects=SH_CARD, gap=2, sizingH="fill",
               key="lsrw")
    for i, q in enumerate(["rapat sprint", "laporan mingguan", "review PR"]):
        row = k.F(hist, f"Riwayat{i + 1}", layout="horizontal", h=44, w="fill",
                  gap=10, cross="center", key=f"lsrw{i}")
        k.icon("clock", row, size=16, color="text-muted", key=f"lsrwi{i}")
        k.T(q, row, size=14, name=f"lsrwt{i}")
        k.F(row, "Spacer", sizingH="fill", h=1, key=f"lsrws{i}")
        k.icon("chevron_right", row, size=14, color="text-muted", key=f"lsrwc{i}")
        if i < 2:
            k.F(hist, "Divider", w="fill", h=1, fill={"$var": "border"},
                key=f"lsdv{i}")

    # Hasil pencarian
    k.micro(body2, "HASIL — 2 TUGAS", key="lsm5")
    k.taskcard(body2, "Rapat sprint dengan tim desain", "Pekerjaan", "09:00",
               "#E5484D", key="lst7")
    k.taskcard(body2, "Siapkan ruang rapat", "Pekerjaan", "10:30", "#F79009",
               key="lst8")

    _, drefs2 = k.dock_bar(scr2, "Beranda", key="lss", x=16, y=774)
    refs["field"] = srow
    refs["batal"] = batal
    refs["frame15"] = scr2
    # "dock" di spec kedua layar akan saling menimpa pada satu dict refs;
    # dock layar 15 disimpan sebagai "dock15" agar keduanya tetap tersedia.
    refs["dock15"] = drefs2  # dock layar 15 (list 4 item)

    cmds = (PRELUDE if test else []) + k.cmds
    return cmds, refs


if __name__ == "__main__":
    _cmds, _ = build(test=True)
    _out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frag_lists.json")
    with open(_out, "w", encoding="utf-8") as _f:
        json.dump(_cmds, _f, ensure_ascii=False, indent=1)
    print(f"frag_lists.json: {len(_cmds)} command")
