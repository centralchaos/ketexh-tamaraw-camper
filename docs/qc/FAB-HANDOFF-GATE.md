# FAB handoff gate — KE-Texh Tamaraw Phase-1 SHELL

**Stamp:** CONDITIONAL / **NO-GO cut** until every Lego row below is **GREEN**.  
**Repo:** https://github.com/centralchaos/ketexh-tamaraw-camper (public)  
**SoR dims:** `DIMS.md` · floor **3647×1911** · entry **700×1550** · over-cab **≈1223** · OAL **≈6300** · F-01 tail **+1000** · watermark `PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED`  
**Rule:** SVG/PNG *present* ≠ fabrication-ready. Promotion requires the six columns on `inventory/PER-PART-AUDIT.md` for that part ID.

---

## Lego test (shop self-sufficiency)

| # | Question | Current | Clears when |
|---|----------|---------|-------------|
| L1 | Can the shop identify the overall envelope? | **GREEN** | Locked floor, entry target, over-cab, OAL, tail on SoR + elevations agree (no dual OAL). |
| L2 | Can it cut every Phase-1 part from controlled patterns? | **RED** | DXF (or shop-accepted equivalent) for C-FR, C-PL, DR-*, H-*, loft B/D/E; P4 flats **developed** after bend allowance locked; kerf on C-00. |
| L3 | Can it select stock and make structural joints without asking Eng? | **RED** | Tube section, plate thickness/grade, weld size, skin splice signed on MAT-01 / C-FR / C-PL (no invented defaults). |
| L4 | Can it drill and attach the body to the vehicle? | **RED** | As-found chassis tape filed; Jay **rail-drill GO** signed; hole schedule on D-01/C-PL released. |
| L5 | Can it build and verify hatch + Phase-1 provisions? | **RED** | Hatch frame sizes frozen; H-* DXF; gen/AC remain **provisions/hooks only** with named conditions resolved (still NOT THE UNIT). |
| L6 | Can it declare the completed vehicle acceptable? | **RED** | Commissioning gates in `notes/commissioning-gates.md` signed (weigh, stability, hose, height, FAIL-IFs). |

**Cut steel / send fabricator pack:** blocked while any of L2–L6 is RED.  
**Merge to `main` / public ChatGPT review:** does **not** clear this gate.

---

## What QC-REPORT establishes (and does not)

| Establishes | Does **not** establish |
|-------------|------------------------|
| Dim consistency vs DIMS | Developed flat patterns for every blank |
| 45/45 expected SVG **families present** | Dimensionally complete manufacturing drawings |
| Stamps / watermarks / CONDITIONAL language | Stock, kerf, weld, bolt grade |
| Gen/AC provision-only wording | Unit buy / kW / BTU / max kg |
| Sampled text check | Full visual print QA of every sheet |

Companion: `docs/qc/QC-REPORT-PR3.md`, `docs/qc/BOM-MAT-VERIFY.md`, `inventory/PER-PART-AUDIT.md`.

---

## Residual named gates (do not improvise beside fabricator)

1. As-found tape on chassis / rails  
2. Jay rail-drill GO  
3. Eng: tube section, plate t/grade, weld size  
4. Bend allowance → develop P4 A–E  
5. DXF release: C-FR, C-PL, DR, H, loft B/D/E  
6. Hatch frame freeze  
7. Kerf + skin splice decision on C-00 / BOM  
8. Commissioning: weigh placard, hose FAIL-IF, OAH closed, stability support  

---

## Per-part promotion rule

A part ID may move from **R&D** → **CUT-READY** only when all six are filled and signed:

1. Part ID + revision  
2. Material + quantity (MAT / BOM; no invented grade)  
3. Developed geometry (flat / DXF / nest ref)  
4. Process + joining instructions  
5. Mating location (assembly map / mate face)  
6. Measurable acceptance criteria  

Until then: **CONDITIONAL inventory only.**

*Rev A · 2026-09-23 · Lilu-G / KE-Texh — bar tightened after ChatGPT Lego review.*
