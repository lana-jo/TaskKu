#!/usr/bin/env python3
"""Integrasi: base generator + 4 fragmen + wiring prototyping -> build_all.json."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_design as g          # menjalankan build base (menulis build.json)
import frag_auth, frag_detail, frag_lists, frag_onb

cmds = g.cmds
idx = next(i for i, c in enumerate(cmds)
           if c["command"] == "page.add" and "Responsive" in json.dumps(c.get("params", {})))

frag_cmds, refs = [], {}
for m in (frag_detail, frag_lists, frag_auth, frag_onb):
    c, r = m.build()
    frag_cmds += c
    refs.update(r)

cmds = cmds[:idx] + frag_cmds + cmds[idx:]

_n = [0]


def nav(a, b, tag):
    _n[0] += 1
    return {"command": "proto.interaction.add",
            "params": {"id": a, "action": {"type": "navigate", "dest": b},
                       "transition": {"type": "dissolve"}, "durationMs": 250},
            "as": f"px_{tag}_{_n[0]}"}


d12 = refs["12"]["frame"]
d13 = refs["13"]["frame"]
d14 = refs["frame14"]
d15 = refs["frame15"]
d16 = refs["16"]["frame"]
d17 = refs["17"]["frame"]
d18 = refs["18"]["frame"]
d19 = refs["19"]["frame"]

navs = []
# Kartu tugas -> Detail Tugas
for card in (g.ht1_ref, g.ht2_ref, g.ht3_ref, g.ct1_ref, g.ct2_ref, g.ct3_ref):
    navs.append(nav(card, d12, "card"))
# Lihat semua / Semua -> Daftar Tugas
navs.append(nav(g.hs1_ref, d14, "seeall"))
navs.append(nav(g.cs_ref, d14, "seeall2"))
# Footer masuk -> Daftar Akun; lupa sandi -> 17
navs.append(nav(g.logf_ref, d16, "register"))
navs.append(nav(g.loglupa_ref, d17, "forgot"))
# Pencarian (tablet & desktop)
for s in (g.dsrch_ref, g.tms_ref, g.sms_ref):
    navs.append(nav(s, d15, "search"))
# Detail: kembali / hapus / edit
navs.append(nav(refs["12"]["back"], g.home_ref, "dtback"))
navs.append(nav(refs["12"]["hapus"], d13, "dtdelete"))
navs.append(nav(refs["12"]["edit"], g.add_ref, "dtedit"))
# Dialog hapus
navs.append(nav(refs["13"]["batal"], d12, "dlgbatal"))
navs.append(nav(refs["13"]["hapus"], g.home_ref, "dlgyes"))
navs.append(nav(refs["13"]["scrim"], d12, "dlgscrim"))
# Dock layar 14 & 15
for i, dst in enumerate((g.home_ref, g.cal_ref, g.stat_ref, g.prof_ref)):
    navs.append(nav(refs["dock"][i], dst, f"dock14{i}"))
    navs.append(nav(refs["dock15"][i], dst, f"dock15{i}"))
navs.append(nav(refs["back"], g.home_ref, "back14"))
navs.append(nav(refs["batal"], g.home_ref, "batal15"))
# Auth
navs.append(nav(refs["16"]["back"], g.log_ref, "regback"))
navs.append(nav(refs["16"]["masuk"], g.log_ref, "regmasuk"))
navs.append(nav(refs["16"]["daftar"], g.home_ref, "regdaftar"))
navs.append(nav(refs["16"]["google"], g.home_ref, "reggoogle"))
navs.append(nav(refs["17"]["back"], g.log_ref, "fgback"))
navs.append(nav(refs["17"]["masuk"], g.log_ref, "fgmasuk"))
navs.append(nav(refs["17"]["kirim"], g.log_ref, "fgkirim"))
# Onboarding slide 2 & 3
navs.append(nav(refs["18"]["lanjut"], d19, "ob2next"))
navs.append(nav(refs["18"]["masuk"], g.log_ref, "ob2masuk"))
navs.append(nav(refs["19"]["mulai"], g.log_ref, "ob3mulai"))
navs.append(nav(refs["19"]["masuk"], g.log_ref, "ob3masuk"))

cmds += navs
with open("build_all.json", "w") as f:
    json.dump(cmds, f, ensure_ascii=False)
print(f"total {len(cmds)} perintah (fragmen {len(frag_cmds)}, interaksi baru {len(navs)})")
