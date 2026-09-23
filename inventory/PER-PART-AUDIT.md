# Per-part audit — Phase-1 SHELL (Lego columns)

**Bar:** part ID + rev → material + qty → developed geometry → process/join → mating location → measurable AC.  
**Legend:** PASS | GAP | TBD | N/A (process sheet) | HOOK (not cut)  
**Stamp:** CONDITIONAL / NO-GO cut · SVG present alone never = PASS on geometry.

| Part ID | Rev | Material + qty | Developed geometry | Process / join | Mate location | Measurable AC | Verdict |
|---------|-----|----------------|--------------------|----------------|---------------|---------------|---------|
| P1 floor | A | GAP (MAT TBD) | SVG+DXF present; splice TBD | GAP | A-05 / floor | GAP | GAP |
| P2 LH wall | A | GAP | SVG; H est. | GAP | A-05 | GAP | GAP |
| P3 RH wall | A | GAP | SVG; H est. | GAP | A-05 | GAP | GAP |
| P4 loft A–E | A | GAP | **Not developed** (bend TBD) | GAP | over-cab | GAP | **RED** |
| P5 rear | A | GAP | SVG; openings TBD | GAP | A-05 | GAP | GAP |
| P6 roof | A | GAP | SVG; splice TBD | GAP | A-05 | GAP | GAP |
| P7 entry | A | N/A blank | field-locate 700×1550 | GAP | C-02 / DR | GAP | GAP |
| P8 windows | A | HOOK | dashed only | HOOK | S-* | HOOK | HOOK |
| FR-01…FR-22 | A | GAP (section TBD) | C-FR SVG; **no DXF** | GAP weld | D-01 / rails | GAP | **RED** |
| PL-01…PL-08 | A | GAP (t/grade TBD) | C-PL SVG; **no DXF**; holes TBD | GAP | D-01 mounts | GAP | **RED** |
| PL-09 gen pad | A | provision | C-PL; not unit | HOOK | D-07 | HOOK | HOOK |
| PL-10 AC cleat | A | provision | C-PL; not unit | HOOK | D-08 | HOOK | HOOK |
| DR-01 / DR-02 | A | GAP | SVG; **no DXF**; overlap TBD | GAP | entry | GAP | **RED** |
| H-01 / H-02 | A | GAP (size TBD) | SVG; **no DXF** | GAP | roof/rear | GAP | **RED** |
| H-03 hardware | A | TBD not released | sched only | TBD | hatches | TBD | TBD |
| Gen / AC **unit** | — | HOOK | — | HOOK | D-07/D-08 | HOOK | HOOK |

**Envelope (L1):** PASS — see `DIMS.md` / FAB-HANDOFF-GATE L1.  
**Fill next:** walk each GAP against tip files; do not invent thickness, grade, weld, kW, BTU, or kg.

*Seed Rev A · 2026-09-23 — tighten after ChatGPT review; expand with file evidence on land PR.*
