# What we cut and what we form — Tamaraw Phase-1 shell

**Status:** CONDITIONAL. Gates unsigned = do not cut steel.  
**Watermark on every sheet:** PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED  
**One truth for sizes:** `DIMS.md`  
**Pack lives on:** [PR #3](https://github.com/centralchaos/ketexh-tamaraw-camper/pull/3)  
**Plane audit tickets:** TAMARAW-7 through TAMARAW-18  
**This note:** draft A, humanized — 23 Sep 2026

This is the single place to walk the shop pack and ask: do we have a real drawing for every panel we mean to cut, and every frame member we mean to form? If a line is thin, it is marked. Nothing here invents a tube size, weld size, bolt grade, kilowatt, BTU, or kilogram.

---

## How to read this

Start with the panels (skin you put on the saw). Then the frame (tube and rings you form and weld). Then the plates. Context elevations are listed at the end so you know what the cut pieces are building toward.

“Present” means the SVG (and its PNG twin) is already on PR #3. A missing DXF is a shop-format gap, not “we never drew it.” Dashed openings on a sheet are field-locate or intent — not a freeze for the plasma.

Fabricator send still waits for your GO after visual QA and the signed gates.

---

## Nest and shop rollup (the binder front)

These are not blanks. They tell the shop how the blanks fit together.

| Sheet | Where | What it does | On the PR? |
|-------|-------|--------------|------------|
| Cover | `cut/CVR-00_cover.svg` | Reading order and rejected wrong sizes | Yes |
| Nest index | `cut/C-00_nest_index.svg` | Which blank on which stock, leftovers | Yes — kerf and brand still open |
| Materials | `cut/shop/MAT-01_materials.svg` | What to buy (grades still TBD) | Yes |
| Fasteners | `cut/shop/FS-01_fasteners.svg` | Hardware schedule (grades still TBD) | Yes |
| Master BOM | `cut/shop/BOM-01_phase1.svg` | Everything Phase-1 claims | Yes |
| Sequence | `cut/shop/AS-01_sequence.svg` | Build order | Yes |
| Joinery | `cut/shop/J-01_joinery.svg` | Splices and corners (weld size TBD) | Yes |
| Hose test | `cut/shop/QA-01_hose.svg` | Water test before you call it tight | Yes |
| Index | `blueprint-pack/sheets/I-00_index.svg` | Elevation set and unsigned gates | Yes |
| Assembly map | `blueprint-pack/sheets/A-05_shell_assembly.svg` | Where P1–P8 sit on the shell | Yes |

Audit ticket for this rollup: **TAMARAW-17**.

---

## 1. Panels we cut

These are the flat skins. Cut only the stated figures. Do not scale a PNG.

### Floor, walls, loft, roof

**P1 — Floor pan**  
Size **3647 × 1911**. Drawing `cut/C-01_p1_floor.svg` (PNG yes, DXF yes). On the nest. Ticket **TAMARAW-7**.  
We have the sheet. Splice along length/width and kerf are still TBD — do not invent them.

**P2 — Side wall, left (entry side)**  
Size **3647 × about 1830** (height is an estimate; tape on the truck wins). Drawing `cut/C-02_p2_lh.svg`. Ticket **TAMARAW-8**.  
Entry **700 × 1550** is dashed and field-located — not a freeze. Window cut size is still TBD. Entry is **not** a separate blank; it lives on this wall plus the door sheets.

**P3 — Side wall, right**  
Same size as P2, mirrored, no entry. Drawing `cut/C-03_p3_rh.svg`. Ticket **TAMARAW-9**. Window symbols only — size TBD.

**P4 — Over-cab loft flats (A through E)**  
Envelope about **1223 × 1911**. One sheet `cut/C-04_p4_overcab.svg` holds five flats. Ticket **TAMARAW-10**.  
Honest gap: these are **estimates, not developed blanks**. Bend allowance is not released. DXF only exists for loft floor (A) and front (C). B, D, and E still need DXF if the shop wants machine files.

**P5 — Rear wall**  
**1911 × about 1830** estimate. Drawing `cut/C-05_p5_rear.svg`. Ticket **TAMARAW-11**. Window and lower hatch are intent only — no cut size.

**P6 — Roof**  
**4870 × 1911** (that is 1223 + 3647 from the SoR, not a new tape). Drawing `cut/C-06_p6_roof.svg`. Ticket **TAMARAW-12**. Lounge opening dashed. Solar, AC unit, and awning are Phase-2 hooks — not cut Done. Splice TBD.

**P7 — Entry**  
Not its own panel. Target **700 × 1550**, field-locate on P2. See door sheets below. Ticket **TAMARAW-15**.

**P8 — Body windows**  
Dashed on the walls. Size TBD. Not a blank.

### Door we cut

**DR-01 — Door leaf** — `cut/door/DR-01_leaf.svg` · present · no DXF yet · overlap and seal TBD  
**DR-02 — Door jamb** — `cut/door/DR-02_jamb.svg` · present · no DXF yet · works with frame members FR-19…21

### Hatches we cut

**H-01 — Lounge hatch leaf** — `cut/hatch/H-01_lounge.svg` · present · size still TBD · no DXF  
**H-02 — Rear hatch leaf** — `cut/hatch/H-02_rear.svg` · present · size still TBD · no DXF  
**H-03 — Hardware schedule** — `cut/hatch/H-03_hardware.svg` · present · not a buy release yet  

Ticket for door: **TAMARAW-15**. Hatches: **TAMARAW-16**.

---

## 2. Frame we form

Load path is skin → stiffeners → posts and sills → outriggers → bed rails. Not hanging the shell from GI sheet alone.

### Form layouts (pictures of the cage)

| Sheet | What you see | Path | Status |
|-------|--------------|------|--------|
| F-00 | Index of members and gates | `cut/frame/F-00_index.svg` | Present |
| F-01 | Floor plan, +1000 tail, outriggers | `cut/frame/F-01_floor.svg` | Present — holes TBD, needs your rail-drill GO |
| F-02 | Posts, sills, roof rails, over-cab ring | `cut/frame/F-02_posts.svg` | Present — tube section TBD |
| F-03 | Roof ring and lounge hatch frame | `cut/frame/F-03_roof_ring.svg` | Present — opening size TBD |
| C-FR | Cut list that matches F-01…F-03 | `cut/C-FR_frame_cut_list.svg` | Present — miters and holes TBD; **no DXF yet** |
| J-01 | How splices and corners meet | `cut/shop/J-01_joinery.svg` | Present — weld size TBD |
| D-01 | Rail drill / outriggers detail | `blueprint-pack/sheets/D-01_outriggers.svg` | Present — your GO box empty |

Ticket: **TAMARAW-13**.

### Members on the cut list (FR-01 through FR-22)

Lengths below follow the SoR where we know them. “1911 env.” means the shell width envelope — deduct the joint before you cut blind. Heights marked ≈ are estimates until as-found tape.

| Tag | What it is | Length | Qty | Notes |
|-----|------------|--------|-----|-------|
| FR-01 | Floor long, left | **3647** | 1 | Rail + tail; not skin |
| FR-02 | Floor long, right | **3647** | 1 | Mirror of FR-01 |
| FR-03 | Floor cross, front | 1911 env. | 1 | Joint deduct TBD |
| FR-04 | Floor cross, rear | 1911 env. | 1 | Tail end |
| FR-05 | Bed–tail fishplate | TBD | 2 | Size unreleased; see J-01 / PL-08 |
| FR-06 | Outrigger | TBD | TBD | Pitch from as-found rails; needs your GO |
| FR-07 | Corner post | ≈1830 est. | 4 | Cut to as-found height |
| FR-08 | Mid post | ≈1830 est. | TBD | Count is Eng’s call |
| FR-09 | Sill, left | **3647** | 1 | Entry is field-locate |
| FR-10 | Sill, right | **3647** | 1 | No entry by default |
| FR-11 | Roof long, left | **4870** | 1 | 1223+3647; splice TBD |
| FR-12 | Roof long, right | **4870** | 1 | Mirror |
| FR-13 | Roof cross, nose | 1911 env. | 1 | Joint deduct TBD |
| FR-14 | Roof cross, rear | 1911 env. | 1 | Joint deduct TBD |
| FR-15 | Over-cab long | ≈1223 est. | 2 | Confirm on vehicle |
| FR-16 | Over-cab cross | 1911 env. | 1 | At the cab face |
| FR-17 | Hatch frame long | TBD | 2 | Opening is still intent (D-04) |
| FR-18 | Hatch frame cross | TBD | 2 | Closed ring with FR-17 |
| FR-19 | Door stile | 1550 + TBD | 2 | Plus buildup; see DR-02 |
| FR-20 | Door head | 700 + TBD | 1 | Field-locate on P2 |
| FR-21 | Door threshold | 700 + TBD | 1 | Weep outward |
| FR-22 | Rear hatch frame | TBD | 4 | H-02 size still unreleased |

No generator unit and no AC unit on this list. Structure provisions live on D-07 and D-08.

---

## 3. Plates we cut (mounts and pads)

All on one sheet: `cut/C-PL_mount_plates.svg`. Ticket **TAMARAW-14** (and **TAMARAW-18** for the last two). Hole centers and edge distance are TBD. Do not drill the chassis rail until your GO on D-01. No DXF yet for this sheet.

| Tag | What it is | Lands on | Note |
|-----|------------|----------|------|
| PL-01 | Outrigger backing | Bed / chassis rail | Needs your GO |
| PL-02 | Outrigger top | Outrigger + floor | Needs Eng GO |
| PL-03 | Ladder stand-off | Post or sill (D-05) | Roof access only — not a jack |
| PL-04 | Hatch hinge | Hatch frame (F-03) | Not skin-only |
| PL-05 | Hatch strut | Hatch frame | Not skin-only |
| PL-06 | Landing-leg pad | Tail frame (D-02) | Max-kg placard stays blank |
| PL-07 | Door hinge reinforcer | Jamb post | Not skin-only |
| PL-08 | Bed–tail fishplate | Floor longs (J-01) | Weld TBD |
| PL-09 | Gen isolator pad | Sill / outrigger | **Provision — not a generator buy** |
| PL-10 | AC curb cleat | Roof rail (D-08) | **Provision — not an AC buy** |

---

## 4. Context drawings (you form toward these)

Not cut blanks. They keep the elevations and FAIL-IFs honest while you build the cage and skin.

- Side, plan, front, rear, section, rear intent: `blueprint-pack/sheets/S-01` … `S-06`
- Roof lounge intent (solar/awning dashed): `S-07`
- Gen bay and AC curb as **provisions**: `S-08`, `D-07`, `D-08`
- Legs, hose, hatch frame, ladder, bumper: `D-02` … `D-06`
- Authoritative side and plan SoR: `svg/tamaraw_shell_side.svg`, `svg/tamaraw_shell_plan.svg`

Ticket for gen/AC provisions: **TAMARAW-18**.

---

## 5. Straight answer — do we have the drawings?

**Yes for the families.** Every Phase-1 panel we mean to cut (P1–P6, door leaf, hatch leaves) and every frame family we mean to form (F-00…F-03, the FR-01…22 list, the plate sheet) already has an SVG on PR #3.

**No for the saw.** Nothing is released to cut steel. Stamp stays CONDITIONAL until the gates are signed.

What still blocks “build from paper alone”:

1. As-found tape for wall and post heights  
2. Eng GO on tube section and weld size  
3. Your GO on rail drill (D-01 / outriggers)  
4. Real developed loft blanks (or a clear shop-develop note forever)  
5. Frozen hatch and door opening sizes after the hatch frame is designed  
6. DXF for frame list, plates, door, hatch, and the rest of the loft flats  

---

## 6. Fill order (when you are ready)

1. Tape the truck — freeze heights for sides, posts, over-cab.  
2. Eng stamps tube and weld on C-FR / J-01 / F-02.  
3. You sign rail drill on D-01.  
4. Develop or explicitly shop-develop P4 A–E.  
5. Freeze H-01 / H-02 with D-04.  
6. Export the missing DXFs.  
7. Re-walk this register, visual-QA the sheets, then decide fabricator send.

---

*End. Same facts as the spreadsheet draft — written so a person can audit it without decoding a matrix.*
