> **Update 2026-09-23 ~15:30 Asia/Shanghai:** PL-01…PL-10 BOM gap is patched on [PR #4](https://github.com/centralchaos/ketexh-tamaraw-camper/pull/4) tip `6d5562d` (DRAFT). This verify file still reflects tip `9eb43ea` (pre-fix) unless re-run on #4.

# BOM / Materials verify — tip `9eb43ea`

**Repo / branch:** `centralchaos/ketexh-tamaraw-camper` · `cursor/phase1-fabricator-pack-9315`  
**Tip SHA:** `9eb43ea4dd5e74c2a5274522c3a5349ac8908904`  
**Sources on tip:** `cut/shop/BOM-01_phase1.svg` (+ PNG), `MAT-01_materials.svg` (+ PNG), `FS-01_fasteners.svg` (+ PNG), `cut/C-FR_frame_cut_list.svg`, `cut/C-PL_mount_plates.svg`, `inventory/CUT-FORM-REGISTER.md`, `DIMS.md`  
**Date:** 2026-09-23 Asia/Shanghai  
**Companion QC:** [`QC-REPORT-PR3.md`](QC-REPORT-PR3.md)

---

## 5. Verdict

### **GAPS** (not COMPLETE, not UNSAFE-INVENTED)

- Family coverage on BOM is **rollup-complete** for skins / frame / door / hatches / gen-AC provisions.  
- **No invented** thickness, grade, bolt grade, kW, BTU, or max kg on MAT-01 / FS-01 / BOM-01 / C-FR / C-PL — empty Eng/Jay GO is explicit.  
- **Gaps Jay must decide** (below): BOM plate row omits PL-09/10 tags; many Qtys TBD; nest/shop process sheets are not BOM line items (expected); DXF still missing for frame/plates/door/hatch.

**UNSAFE-INVENTED: No.** Do not treat TBD rows as a buy list.

---

## 1. Parts coverage matrix vs BOM-01

BOM-01 rule printed on sheet: *“A ROW MARKED HOOK IS NOT FAB DONE AND NOT A PURCHASE RELEASE.”*

| Tag / family (register) | On tip drawing | On BOM-01 | Status | Notes |
|-------------------------|----------------|-----------|--------|-------|
| **P1** floor 3647×1911 | `C-01` SVG+PNG+DXF | **Present** — “P1 floor blank · qty 1 · C-01 · Splice TBD” | present | Size matches DIMS |
| **P2** LH wall | `C-02` | **Present** — rolled “P2 / P3 walls · 1+1” | present | H estimate |
| **P3** RH wall | `C-03` | **Present** (same row) | present | |
| **P4** loft A–E | `C-04` | **Present** — “P4 flats A–E · 5 · Estimates” | present / TBD | Not developed; bend TBD |
| **P5** rear | `C-05` | **Present** | present | Openings TBD |
| **P6** roof 4870×1911 | `C-06` | **Present** | present | Splice TBD |
| **P7** entry | not own blank | *(via door row + C-02)* | present (indirect) | 700×1550 field-locate — not a BOM blank |
| **P8** windows | dashed only | **Absent as line** | TBD / gap | Size TBD; correctly not a blank |
| **FR-01…FR-22** | `C-FR` (all 22 rows) | **Present** — rollup “Frame FR-01…FR-22 · See C-FR · Section TBD” | present (rollup) | Detail = C-FR, not exploded on BOM |
| **PL-01…PL-08** | `C-PL` | **Present** — “Plates PL-01…PL-08 · TBD · C-PL · Holes TBD” | present (rollup) | Qty TBD |
| **PL-09** gen isolator | `C-PL` | **Not named as PL-09** | gap / indirect | Covered only as “Gen bay provision · D-07” |
| **PL-10** AC curb cleat | `C-PL` | **Not named as PL-10** | gap / indirect | Covered only as “AC curb provision · D-08” |
| **DR-01** leaf | `door/DR-01` | **Present** — “Door leaf + jamb · 1 · DR-01 DR-02” | present | Overlap TBD; no DXF |
| **DR-02** jamb | `door/DR-02` | **Present** (same row) | present | no DXF |
| **H-01** lounge leaf | `hatch/H-01` | **Present** | present | Size TBD; no DXF |
| **H-02** rear leaf | `hatch/H-02` | **Present** | present | Size TBD; no DXF |
| **H-03** hardware sched | `hatch/H-03` | **Present (rollup)** — “Hardware · TBD · H-03 FS-01 · Not released” | present / TBD | Not a buy release |
| Gen bay provision | `D-07` | **Present** — “NOT THE UNIT” | present | Provision |
| AC curb provision | `D-08` | **Present** — “NOT THE UNIT” | present | Provision |
| Generator **unit** | — | **Present as HOOK ONLY** qty — | hook | Not buy |
| AC **unit** | — | **Present as HOOK ONLY** qty — | hook | Not buy |
| Solar / awning / seats | S-07/S-08 | **HOOK ONLY** | hook | Phase-2 |
| **Nest/shop process** CVR-00, C-00, AS-01, J-01, MAT-01, FS-01, QA-01, I-00, A-05 | SVG present | **Not BOM part rows** | N/A (process) | Correct: binders, not cut parts — do not invent BOM lines |

### C-FR member check (detail behind BOM rollup)

| MK | Length on C-FR | Matches register / DIMS? |
|----|----------------|--------------------------|
| FR-01 / FR-02 | **3647** | Yes |
| FR-03 / FR-04 | 1911 env. | Yes (joint deduct TBD) |
| FR-05 | TBD · qty 2 | Yes (unreleased) |
| FR-06 | TBD · qty TBD · Jay GO | Yes |
| FR-07 | ≈1830 est. · qty 4 | Yes |
| FR-08 | ≈1830 est. · qty TBD | Yes |
| FR-09 / FR-10 | **3647** | Yes |
| FR-11 / FR-12 | **4870** (=1223+3647) | Yes |
| FR-13 / FR-14 | 1911 env. | Yes |
| FR-15 | ≈1223 est. · qty 2 | Yes |
| FR-16 | 1911 env. | Yes |
| FR-17 / FR-18 | TBD | Yes (opening intent) |
| FR-19 | 1550+TBD · qty 2 | Yes |
| FR-20 / FR-21 | 700+TBD | Yes |
| FR-22 | TBD · qty 4 | Yes |
| Gen/AC unit on C-FR | **Explicitly absent** | Pass |

### C-PL plate check

| MK | On C-PL | On BOM-01 by tag? |
|----|---------|-------------------|
| PL-01…PL-08 | Yes (Jay/Eng/status notes) | Yes (rollup PL-01…PL-08) |
| PL-09 Provision | Yes | **No tag** — only D-07 provision row |
| PL-10 Provision | Yes | **No tag** — only D-08 provision row |

All plate sizes / holes / grades: **TBD**. No invented dimensions.

---

## 2. Materials coverage — MAT-01

Sheet title: *MATERIAL SCHEDULE — THICKNESS AND GRADE TBD*  
Banner: *EMPTY ENG GO = THE LINE IS NOT RELEASED. DO NOT SUBSTITUTE A BRAND.*  
Footer note: *NO SANDWICH BRAND. NO BOLT GRADE. NO WELD FILLER SPEC. PHASE-2 UNITS ARE NOT MATERIALS ON THIS SHEET.*

| Buy-class (MAT-01 line) | Role on sheet | Thickness | Grade | GO box | Covers (register link) | Invented? |
|-------------------------|---------------|-----------|-------|--------|------------------------|-----------|
| Outer skin | Weather face | TBD | TBD | Eng | P1–P6 skins | **No — honest TBD** |
| Core | If sandwich used | TBD | TBD | Eng | Optional sandwich | **No** |
| Inner skin | Liner | TBD | TBD | Eng | Cabin liner | **No** |
| Frame tube | F-00 members | TBD | TBD | Eng | FR-01…22 / F-01…F-03 | **No** |
| Angle / sill | Open shapes | TBD | TBD | Eng | Sills / angles | **No** |
| Plate | C-PL | TBD | TBD | Eng | PL-01…10 | **No** |
| Sealant | Joints D-03 | TBD | TBD | Eng | Hose joint | **No** |
| Weatherstrip | Door and hatches | TBD | TBD | Eng | DR / H | **No** |
| Isolation | Dissimilar metals | TBD | TBD | Eng | Pads / isolators | **No** |
| Fastener | FS-01 | TBD | TBD | Eng | H-R…H-C schedule | **No** |

**FS-01 (fastener schedule companion):** symbols H-R, H-B, H-P, H-H, H-S, H-L, H-G, H-N, H-C — all QTY/DIA/EDGE/TORQUE = **TBD**. H-R/H-B gated by Jay; H-N/H-C “do not release the units.” **No invented fastener specs.**

---

## 3. Cross-check inconsistencies

| Issue | Severity | Detail |
|-------|----------|--------|
| BOM plate rollup **PL-01…PL-08** vs C-PL/register **PL-01…PL-10** | **Gap** | PL-09/PL-10 exist on C-PL as provisions but are not named on BOM plate row; BOM instead has separate “Gen bay provision” / “AC curb provision” rows. Risk: shop misses PL-09/10 when exploding BOM → C-PL. |
| BOM qty for plates / hardware / several FR members | **Gap** | Explicit TBD — correct, but not purchasable. |
| P8 windows | **Gap (honest)** | Not on BOM as a blank; size TBD on walls. |
| Gen/AC as buy vs provision | **Pass** | BOM: provisions “NOT THE UNIT”; units “HOOK ONLY”; MAT excludes Phase-2 units; C-FR states no gen/AC on list; C-PL flags PL-09/10 provision. |
| Size mismatch skins vs DIMS | **Pass** | P1 3647×1911; roof 4870; FR longs 3647/4870; entry 700×1550 — consistent. |
| Orphan tags on BOM not in register | **Pass** | No orphan part tags found. |
| Orphan tags on C-PL/C-FR missing from BOM explosion | **Minor gap** | Individual FR/PL tags only via rollup (acceptable if shop always opens C-FR/C-PL); PL-09/10 naming gap as above. |
| Nest/shop sheets absent from BOM | **OK** | Process sheets, not parts. |
| Invented grades / kW / BTU / kg | **Pass (none found)** | |

---

## 4. Exact gaps Jay must decide (no invent)

Do **not** fill these with guessed numbers:

1. **BOM hygiene:** Add explicit BOM lines (or a clear note) for **PL-09** and **PL-10** as provision plates — or formally state “provisions counted only under D-07/D-08 rows.” Pick one so the shop cannot miss them.  
2. **Eng GO:** Release or refuse — outer/inner/core thickness & grade; frame tube section; plate thickness; weld / filler; sealant & weatherstrip product class.  
3. **Jay GO:** Rail-drill H-R / H-B (qty, dia, edge) before any chassis/bed rail hole.  
4. **Qtys still TBD on paper:** FR-06 outriggers, FR-08 mid-post count, all PL-01…10 (except PL-08 qty 2 on C-PL), H-03 hardware, FS-01 all symbols.  
5. **Loft P4:** Develop blanks or stamp “shop-develop forever”; freeze bend allowance; add DXF for B/D/E if machine-cut.  
6. **H-01 / H-02 / door overlap:** Freeze opening sizes with D-04 before leaf cut.  
7. **DXF export:** C-FR, C-PL, DR-01/02, H-01/02 — shop-format gap (drawings exist as SVG).  
8. **Kerf / nest brand / skin splices:** Still open on C-00 / C-01 / C-06.  
9. **Units:** Keep generator and AC as **hooks only** until a separate buy decision — never promote HOOK rows to FAB DONE on BOM-01.

---

## Counts (quick)

| Metric | Value |
|--------|-------|
| Register panel families P1–P6 on BOM | 6/6 present |
| FR-01…22 on C-FR | 22/22 present; BOM rollup present |
| PL-01…10 on C-PL | 10/10 present |
| PL tags named on BOM | PL-01…08 only (**2 tag gaps**) |
| MAT buy-classes | 10; all thickness/grade TBD |
| FS symbols | 9; all TBD |
| Invented unit/spec findings | **0** |
| Verdict | **GAPS** |

---

*End BOM-MAT-VERIFY — tip `9eb43ea4dd5e74c2a5274522c3a5349ac8908904`.*
