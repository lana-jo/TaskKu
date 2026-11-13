#!/usr/bin/env python3
"""frag_auth — 2 layar TaskKu: 16 Daftar Akun + 17 Lupa Kata Sandi.

Bagian dari kit TaskKu (lihat figkit.py untuk API). build() mengembalikan
(cmds, refs); refs disarangkan per layar:
  {"16": {"back", "daftar", "google", "masuk"},
   "17": {"back", "kirim", "masuk"}}.

build(test=True) menambahkan prelude koleksi variabel "Warna" (Terang/Gelap)
agar fragmen bisa diuji berdiri sendiri di dokumen kosong.
"""
import json
import os

from figkit import Kit, FONT, VARS, GRAD, SH_CARD, SH_BTN


def _wrap_text(k, parent, text, size, color, lh, name):
    """Teks auto-layout yang mengisi lebar sisa (sizingH fill) dan membungkus."""
    return k.S("text.create", {
        "text": text, "x": 0, "y": 0, "parent": parent, "name": name,
        "props": {"fontFamily": FONT, "fontStyle": "Regular", "fontSize": size,
                  "fill": {"$var": color}, "lineHeight": lh, "sizingH": "fill"},
    })


def _back_button(k, parent, key):
    """Tombol kembali lingkaran 44 dengan chevron_left 20."""
    back = k.F(parent, "Kembali", w=44, h=44, radius=999,
               fill={"$var": "surface"}, effects=SH_CARD, layout="horizontal",
               main="center", cross="center", key=key)
    k.icon("chevron_left", back, size=20, key=key + "i")
    return back


def _footer_masuk(k, body, label, key):
    """Footer "…? Masuk" — mengembalikan ref teks Masuk."""
    row = k.F(body, "MasukRow", layout="horizontal", gap=5, main="center",
              sizingH="fill", key=key)
    k.T(label, row, size=13.5, color="text-muted", name=key + "1")
    return k.T("Masuk", row, size=13.5, style="SemiBold", color="primary",
               name=key + "2")


def build(test=False):
    k = Kit("au")
    refs = {}
    if test:
        k.S("variable.createCollection", {"name": "Warna", "modes": ["Terang", "Gelap"]})
        for vname, (light, dark) in VARS.items():
            k.S("variable.create", {"collection": "Warna", "name": vname,
                                    "type": "color",
                                    "values": {"Terang": light, "Gelap": dark}})

    # ---- 16 Daftar Akun
    scr = k.screen_frame("16 Daftar Akun", 7095, key="s16")
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[6, 26], gap=14, key="b16")
    refs["16"] = {"back": _back_button(k, body, "bk16"), "frame": scr}
    logo = k.F(body, "Logo", w=62, h=62, radius=20, fill=GRAD,
               layout="horizontal", main="center", cross="center", effects=SH_BTN,
               key="lg16")
    k.icon("check", logo, size=28, sw=3, fill_hex="#FFFFFF", key="lgi16")
    k.T("Buat akun baru", body, size=26, style="SemiBold", ls="-2%", name="j16")
    k.T("Mulai kelola tugasmu dengan TaskKu.", body, size=14, color="text-muted",
        lh="150%", name="sbt16")
    k.F(body, "jarak", h=8, fill="none", key="sp16")
    k.labeled_field(body, "Nama Lengkap", "Nama lengkap", key="fn16",
                    placeholder=True)
    k.labeled_field(body, "Email", "nama@email.com", key="fe16", placeholder=True)
    k.labeled_field(body, "Kata Sandi", "Minimal 8 karakter", key="fp16",
                    placeholder=True, trailing=["eye"])
    agr = k.F(body, "Setuju", layout="horizontal", w="fill", gap=9, cross="center",
              key="ag16")
    k.F(agr, "cb", w=19, h=19, radius=6, fill={"$var": "primary"}, key="cb16")
    k.T("Saya menyetujui ", agr, size=13, color="text-muted", name="ag1_16")
    k.T("Syarat & Ketentuan", agr, size=13, style="SemiBold", color="primary",
        name="ag2_16")
    refs["16"]["daftar"] = k.button(body, "Daftar", "primary", key="btn16")
    dv = k.F(body, "Divider", layout="horizontal", w="fill", gap=14,
             cross="center", key="dv16")
    k.F(dv, "l", h=1, sizingH="fill", fill={"$var": "border"}, key="dvl16")
    k.T("atau", dv, size=12, color="text-muted", name="dvt16")
    k.F(dv, "r", h=1, sizingH="fill", fill={"$var": "border"}, key="dvr16")
    google = k.F(body, "Google", layout="horizontal", main="center",
                 cross="center", w="fill", h=54, radius=27,
                 fill={"$var": "surface"}, stroke={"$var": "border"}, gap=12,
                 key="gg16")
    gm = k.F(google, "G", layout="horizontal", gap=3, key="ggm16")
    for i, c in enumerate(["#EA4335", "#FBBC05", "#34A853", "#4285F4"]):
        k.dot(gm, 9, c, key=f"ggd{i}16")
    k.T("Lanjutkan dengan Google", google, size=14.5, style="SemiBold",
        name="ggt16")
    refs["16"]["google"] = google
    refs["16"]["masuk"] = _footer_masuk(k, body, "Sudah punya akun?", "ft16")

    # ---- 17 Lupa Kata Sandi
    scr = k.screen_frame("17 Lupa Kata Sandi", 7568, key="s17")
    k.statusbar(scr)
    body = k.F(scr, "Konten", layout="vertical", w="fill", sizingV="fill",
               pad=[6, 26], gap=16, key="b17")
    refs["17"] = {"back": _back_button(k, body, "bk17"), "frame": scr}
    k.F(body, "jarak", h=10, fill="none", key="sp1_17")
    k.T("Atur ulang kata sandi", body, size=24, style="SemiBold", ls="-2%",
        name="j17")
    k.T("Masukkan email kamu — kami akan mengirim tautan untuk membuat kata "
        "sandi baru.", body, size=14, color="text-muted", lh="155%",
        width=320, name="sbt17")
    k.F(body, "jarak2", h=10, fill="none", key="sp2_17")
    k.labeled_field(body, "Email", "nama@email.com", key="fe17", placeholder=True)
    info = k.F(body, "Info", layout="horizontal", w="fill", radius=14, pad=12,
               gap=10, cross="center", fill={"$var": "surface-2"}, key="in17")
    k.icon("clock", info, size=16, color="primary", sw=2, key="ini17")
    _wrap_text(k, info,
               "Tautan berlaku 30 menit. Periksa folder spam bila tidak datang.",
               12, "text-muted", "145%", "int17")
    refs["17"]["kirim"] = k.button(body, "Kirim Tautan", "primary", key="btn17")
    k.F(body, "isi", w=1, sizingV="fill", fill="none", key="fill17")
    refs["17"]["masuk"] = _footer_masuk(k, body, "Ingat kata sandi?", "ft17")

    return k.cmds, refs


if __name__ == "__main__":
    cmds, _ = build(test=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frag_auth.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(cmds, f, ensure_ascii=False)
    print(f"{len(cmds)} command ditulis ke {out}")
