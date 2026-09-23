# cut/ — Phase-1 shell patterns

**PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED**

**CONDITIONAL. Gates unsigned = do not cut.**

Do not scale a PNG. Cut only text figures marked as cut. Dashed geometry is field locate or intent. Kerf, bend allowance, and edge allowance are TBD.

Register: [`../DIMS.md`](../DIMS.md). Sequence: [`shop/AS-01_sequence.svg`](shop/AS-01_sequence.svg).

## Panel → sheet

| Panel | Sheet | Figure | Opening rule |
|-------|-------|--------|----------------|
| P1 floor | `C-01_p1_floor.svg` | 3647 × 1911 | Splice TBD. Not the chassis joint. |
| P2 side LH | `C-02_p2_lh.svg` | 3647 × H ≈ 1830 est. | P7 700 × 1550 dashed, field locate. P8 size TBD. |
| P3 side RH | `C-03_p3_rh.svg` | Mirror. No entry. | Window symbol size TBD. |
| P4 loft | `C-04_p4_overcab.svg` | Envelope ≈ 1223 × 1911, flats A–E | Estimates. Not developed blanks. |
| P5 rear | `C-05_p5_rear.svg` | 1911 × H ≈ 1830 est. | Window and lower hatch intent, no size. |
| P6 roof | `C-06_p6_roof.svg` | 4870 × 1911 | Lounge dashed, not a cut. Solar / AC / awning not cut. |
| P7 entry | on C-02, DR-01, DR-02 | 700 × 1550 target | Not a separate blank. |
| P8 windows | dashed on the walls | Size TBD | Not a blank. |

Nest index, qty, stock, leftover: `C-00_nest_index.svg`.

Frame cut list: `C-FR_frame_cut_list.svg`. Plates: `C-PL_mount_plates.svg`.

Frame drawings: `frame/`. Door: `door/`. Hatches: `hatch/`. Shop: `shop/`.

DXF files in `dxf/` for C-01, C-02, C-03, C-04_p4a, C-04_p4c, C-05, and C-06 are outer envelopes only. They omit field-locate openings.

`C-FR_frame_cut_list`, `C-PL_mount_plates`, `DR-01_leaf`, `DR-02_jamb`, `H-01_lounge`, `H-02_rear`, and `C-04_p4_overcab` in `dxf/` are as-drawn A1 sheet exports. CONDITIONAL inventory, not part-scale cut profiles. See [`../docs/qc/DXF-EXPORT-TRIAL.md`](../docs/qc/DXF-EXPORT-TRIAL.md).

## Not on these sheets

Generator unit and AC unit. Provisions are `blueprint-pack/sheets/D-07_generator.svg` and `D-08_ac.svg`. PL-09 and PL-10 are pad and cleat provisions, not a purchase of the units.
