# QC Report — KE-Texh Tamaraw Phase-1 SHELL fabricator pack

**Repo:** `centralchaos/ketexh-tamaraw-camper` (private)  
**PR:** [#3](https://github.com/centralchaos/ketexh-tamaraw-camper/pull/3) — `cursor/phase1-fabricator-pack-9315`  
**Tip SHA verified:** `9eb43ea4dd5e74c2a5274522c3a5349ac8908904`  
**Tip author:** Jose Carlo Sia (`centralchaos`) — 2026-09-23 15:15 Asia/Shanghai (07:15Z)  
**QC date:** 2026-09-23 Asia/Shanghai  
**Auditor:** Lilu-G executor (evidence from GitHub tip + SVG text extract)  
**Companion:** [`BOM-MAT-VERIFY.md`](BOM-MAT-VERIFY.md) (parts/materials deep-dive)

**Audience:** Jay (internal GO) and any public reviewer Jay hands this to.  
**Stamp reminder:** CONDITIONAL / NO-GO cut until gates. Watermark: PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED.

---

## Verdict

**Conditionally OK as an R&D fabricator paper pack — not a cut release.**  
SoR dims, family SVG completeness, stamps, and gen/AC provisions-only language hold on tip `9eb43ea`. Residual NO-GO gates remain unsigned; DXF / loft / Eng / rail-drill gaps are honest. **Do not send to fabricator for steel cut.** PR #3 is already **MERGED** to `main` (merge `890c3ab`) despite PR body “Do not merge” — treat as archive-on-main, not as cut authorization.

---

## Pass / Fail / Conditionally OK

| # | Check | Result | Evidence |
|---|--------|--------|----------|
| 1 | Dim consistency vs `DIMS.md` / register | **PASS** | Floor **3647×1911** on `DIMS.md`, `C-01`, `F-01`, register; entry **700×1550** on `C-02`, `S-01`, SoR side SVG label; over-cab **≈1223**; OAL **≈6300**; F-01 tail **+1000** (not +2200). Rejected literals 1912 / 1215 / 780×1550 / +2200 **absent as labels** on sampled sheets. |
| 2 | Completeness — every register family has SVG on tip | **PASS** | 45/45 expected SVG paths present (CVR/C-00…C-06/C-FR/C-PL/F-00…F-03/DR/H/shop + I-00/S-01…S-08/D-01…D-08/A-05 + `svg/tamaraw_shell_{side,plan}.svg`). |
| 3 | Stamp/watermark on ≥6 representative sheets | **PASS** | Titleblock watermark + `REV CONDITIONAL` on **I-00, C-01, C-00, F-01, S-01, D-07**; also verified CVR-00, C-FR, C-PL, DR-01, H-01, F-02, D-01, S-08, BOM-01, MAT-01, FS-01. |
| 4 | Gen/AC provisions-only (D-07/D-08/S-08) | **PASS** | Titles: “NOT THE UNIT”; explicit **NO kW / NO BTU / NO bolt grade**; units “HOOK ONLY / NOT CUT DONE”; FAIL-IFs present. No invented unit specs. |
| 5 | Gaps honestly listed | **PASS** | Register §5 + `notes/commissioning-gates.md` + sheet callouts match residual list below (DXF C-FR/C-PL/DR/H; loft not developed; Eng tube/weld TBD; rail-drill unsigned). |
| 6 | Drafting cleanliness (SVG markup) | **Conditionally OK** | Heuristic close-baseline text scan on I-00, C-00, C-FR, S-01, D-07, F-01, C-01: **0 overlap candidates**. PNG visual pass still recommended before any shop print. |
| 7 | PR health (draft / mergeable / author lock) | **Conditionally OK / note** | Tip SHA matches PR head. Author lock: `centralchaos`. **Not draft** — PR **state=MERGED** 2026-09-23 15:18 Asia/Shanghai by `centralchaos` (merge commit `890c3ab`). Mergeable N/A post-merge. Body said “Do not merge”; merge happened anyway — process note, not a dim defect. |
| 8 | Parts/materials lists (Jay add-on) | **GAPS (honest TBD)** | See `BOM-MAT-VERIFY.md`. No invented grades; BOM plate row stops at PL-08 while C-PL has PL-09/10. |

---

## Critical defects

**None that invent cut sizes or unit specs.**

Process / inventory notes (not cut-geometry defects):

1. **PR merged despite “Do not merge”** — pack is on `main`; still CONDITIONAL / NO-GO cut.  
2. **BOM-01 plate rollup says PL-01…PL-08** while `C-PL` / register list **PL-01…PL-10** (PL-09/10 appear only as gen/AC provision rows on BOM). See BOM-MAT-VERIFY.  
3. **`svg/tamaraw_shell_side.svg`** uses drawing-space coordinates including numeric `780` (window rect widths / path points). Entry **label** is correctly **700×1550**. Do not misread coordinate `780` as the rejected entry substitution.

---

## Residual NO-GO list

Do **not** cut steel until signed / closed:

1. As-found tape (bed L×W, rail spacing, cab roof H, VIN) — freezes heights / 1830 est.  
2. Jay GO — rail drill (D-01; FS-01 H-R / H-B).  
3. Eng GO — tube section, plate thickness, weld size (F-02 / J-01 / MAT-01 / C-FR).  
4. Outriggers + landing legs + weigh before any max-kg placard.  
5. Hose / rain test (D-03 + closed hatch; closed AC curb if built).  
6. Hatch frame freeze (D-04 / H-01 / H-02 sizes still TBD).  
7. Ladder = roof access only (D-05); bumper/splash weep (D-06).  
8. D-07 provision FAIL-IFs (exhaust/CO, mass not on +1000 skin only, wet glands, parked-only).  
9. D-08 provision FAIL-IFs (curb not skin-only, condensate to weep, road sealed/blanked; OAH ≤2500 hatch closed + curb).  
10. Shop-format gaps: **DXF missing** for C-FR, C-PL, DR-01/02, H-01/02; loft P4 **B/D/E** DXF missing; P4 flats **not developed** (bend allowance TBD).  
11. Kerf / brand / splice TBD on nest and skins.

---

## Dim lock snapshot (SoR — do not invent)

| Datum | Locked value | Checked on tip |
|-------|--------------|----------------|
| Chassis | TMP LWB dropside; WB **3085**; stock **5300×1800×1800**; bed **2647×1711** | `DIMS.md`, I-00, S-01 |
| Floor | **3647×1911** (+1000 tail, +100/side) | DIMS, C-01, F-01, register |
| OAL / OAH | **≈6300** / **≤2500** | DIMS, S-01, I-00 |
| Over-cab / shell H | **≈1223** / **≈1830** est. | DIMS, C-04, S-01/S-02 |
| Entry | **700×1550** field-locate | C-02, S-01, SoR side label |
| F-01 tail | **+1000** (not +2200) | F-01 text |

---

## Recommended ChatGPT review prompts (3)

1. **SoR vs sheets:** “Using only `DIMS.md` and the text extracted from `C-01`, `C-02`, `F-01`, `S-01`, and `svg/tamaraw_shell_side.svg` at commit `9eb43ea`, confirm floor is 3647×1911 (not 1912), entry is 700×1550 (not 780), over-cab ≈1223, OAL ≈6300, and F-01 tail is +1000. List any contradictory figure.”  

2. **Provisions vs buys:** “From `D-07`, `D-08`, `S-08`, and `BOM-01` at `9eb43ea`, confirm generator and AC appear only as structure provisions / hooks — no kW, BTU, bolt grade, or max-kg release. Flag any sentence that could be read as a purchase order.”  

3. **Cut readiness:** “Given `notes/commissioning-gates.md` and `inventory/CUT-FORM-REGISTER.md`, produce a one-page NO-GO checklist a shop foreman can sign. Do not invent tube size, weld size, kerf, or hatch cut size.”  

---

## File index — what a public reviewer needs

Hand these (SVG preferred; PNG twin OK for screen review). Do **not** treat PNG as cut geometry.

### Truth / gates
| Path | Role |
|------|------|
| `DIMS.md` | Sole envelope register |
| `README.md` | Reading order + chassis lock |
| `notes/commissioning-gates.md` | Unsigned gates |
| `inventory/CUT-FORM-REGISTER.md` | Panels / frame / plates audit |

### Elevations & details (`blueprint-pack/sheets/`)
| Sheet | File |
|-------|------|
| I-00 | `I-00_index.svg` |
| S-01…S-08 | `S-01_side_elevation.svg` … `S-08_service_plan.svg` |
| D-01…D-08 | `D-01_outriggers.svg` … `D-08_ac.svg` |
| A-05 | `A-05_shell_assembly.svg` |

### Cut / form / shop (`cut/`)
| Family | Paths |
|--------|-------|
| Cover / nest | `CVR-00_cover.svg`, `C-00_nest_index.svg` |
| Panels | `C-01_p1_floor.svg` … `C-06_p6_roof.svg` |
| Frame list / plates | `C-FR_frame_cut_list.svg`, `C-PL_mount_plates.svg` |
| Frame views | `frame/F-00_index.svg` … `F-03_roof_ring.svg` |
| Door / hatch | `door/DR-01_leaf.svg`, `DR-02_jamb.svg`; `hatch/H-01_lounge.svg` … `H-03_hardware.svg` |
| Shop | `shop/AS-01_sequence.svg`, `J-01_joinery.svg`, `FS-01_fasteners.svg`, `MAT-01_materials.svg`, `BOM-01_phase1.svg`, `QA-01_hose.svg` |

### Authoritative SoR drawings
| Path |
|------|
| `svg/tamaraw_shell_side.svg` |
| `svg/tamaraw_shell_plan.svg` |

### DXF present on tip (partial)
`cut/dxf/C-01`, `C-02`, `C-03`, `C-04_p4a`, `C-04_p4c`, `C-05`, `C-06` only.  
**Missing DXF:** C-FR, C-PL, DR-*, H-*, loft P4-B/D/E.

### Out of scope for public cut review
- `fab-pack/reference/` (photo-scale — not cut figures)  
- Any verbal brief  
- This QC does **not** authorize fabricator send, LTO, or repo publicize

---

## Method notes

- Sources: GitHub MCP + `gh` against tip `9eb43ea`; local extracts under `/workspace/tamaraw-inventory/`.  
- Tree: 171 blobs; **49 SVG / 84 PNG / 7 DXF**.  
- Overlap check: text x/y proximity heuristic only — not a full graphic layout engine.  
- Related deep-dive: `/workspace/tamaraw-inventory/BOM-MAT-VERIFY.md`.

---

*End QC-REPORT-PR3 — tip `9eb43ea4dd5e74c2a5274522c3a5349ac8908904`.*
