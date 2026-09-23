# DXF export trial — missing Phase-1 families

**Stamp:** **CONDITIONAL / NO-GO cut.** Files written by this trial are **CONDITIONAL inventory**. They are **not CUT-READY**.
**Watermark:** **PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED**
**Lego:** L1 stays **GREEN**. L2–L6 stay **RED**. This trial does not flip L2.
**Rev:** A · 2026-09-23

Cut steel and fabricator send stay **HOLD**. A file under `cut/dxf/` from this trial is an as-drawn sheet export. It is not a shop-accepted cut profile and it does not close residual 5 on `FABRICATOR-CUT-RELEASE.md`.

---

## Tool

| Candidate | Result |
|-----------|--------|
| `cut/tools/build_fab.py` `write_dxf()` | Present. It writes envelope rectangles for C-01, C-02, C-03, C-04_p4a, C-04_p4c, C-05, C-06 from hard-coded lengths. **Not used** for this trial. Those families are not 1:1 outlines, and copying that writer would invent part geometry. |
| Inkscape | **Not on PATH** in this run. |
| `ezdxf` | **Not installed.** |
| `cut/tools/svg_to_dxf_trial.py` | Used. Stdlib XML reader. Same minimal DXF header as the existing files: `$INSUNITS` = 4 (millimetres), `LINE` / `CIRCLE` / `TEXT`, layer name in group 8. |

Command, from the repo root:

```text
python3 cut/tools/svg_to_dxf_trial.py
```

The script reads the SVG, checks that `width`/`height` in mm equal the `viewBox`, flips Y so CAD Y is up (`y_dxf = viewBox_height - y_svg`), and writes `cut/dxf/<svg-stem>.dxf`. Text is DXF `TEXT` on layer `ANNOTATION`. It is not converted to paths. Solid strokes go to `AS-DRAWN`. Dashed strokes go to `DASHED`. Fill-only symbols go to `FILL`. The page-fill rectangle is omitted. Each file carries group-999 and `STAMP` text: `CONDITIONAL INVENTORY - NOT CUT-READY`.

Non-ASCII on the sheet is folded in TEXT only (`×` → `x`, `—` → `-`, `≈` → `~`, `·` → `.`). Geometry numbers are unchanged.

---

## Scale check

1. Every source SVG is `width="841mm" height="594mm"` with `viewBox="0 0 841 594"`. One user unit is one millimetre **of the A1 sheet**, not one millimetre of the part.
2. Y-up check on the P4-A box in `C-04_p4_overcab.svg`: SVG `rect` at (24, 40), size 150 × 96. DXF top edge is `y = 554.00` (`594 - 40`) from `x = 24.00` to `x = 174.00`. Height stays 96.00 mm.
3. SoR figures that appear as **text** were compared with stroked spans. They do not match. The exporter did **not** rescale the symbol up to the text figure.
4. After export, no `LINE` in the seven new files is within 0.5 mm of 3647, 1911, 4870, 1550, 1223, 1830, 2647, or 700. Those numbers, where the sheet states them, remain `TEXT`.
5. New files do not use layer `ENVELOPE`. That layer is the older outer-envelope DXFs only.

Sheet furniture (border, title block, GO boxes about 168 × 28) is in the file because it is as-drawn. It is not a part.

---

## Pass / fail

`PASS` means the as-drawn sheet DXF was written in sheet millimetres and stamped CONDITIONAL.  
`BLOCKED` means there is no clean cut profile. No geometry was invented to fill the gap.

| Family | Master | DXF | Sheet export | Cut profile |
|--------|--------|-----|--------------|-------------|
| C-FR | `cut/C-FR_frame_cut_list.svg` | `cut/dxf/C-FR_frame_cut_list.dxf` | **PASS** — 66 LINE, 182 TEXT. Table box **516.00 × 335.80** sheet mm. | **BLOCKED.** Lengths are TEXT (`3647`, `1911 env.`, `TBD`, estimates). No member profile. Miter and holes stay TBD. |
| C-PL | `cut/C-PL_mount_plates.svg` | `cut/dxf/C-PL_mount_plates.dxf` | **PASS** — 57 LINE, 4 CIRCLE, 88 TEXT. Table **520.00 × 198.00**. Generic plate symbol **240.00 × 140.00**. | **BLOCKED.** Plate size, hole diameter, and edge distance are unreleased. Circles are **r = 4.00** drawn symbols. The sheet says the symbol is not a pattern. |
| DR-01 | `cut/door/DR-01_leaf.svg` | `cut/dxf/DR-01_leaf.dxf` | **PASS** — 50 LINE, 33 TEXT. Outer symbol **150.00 × 300.00**. Dashed inner **118.00 × 268.00**. | **BLOCKED.** Clear target **700 × 1550** is TEXT. Overlap has no millimetre. Sheet says do not scale this leaf. |
| DR-02 | `cut/door/DR-02_jamb.svg` | `cut/dxf/DR-02_jamb.dxf` | **PASS** — 43 LINE, 32 TEXT. Wall symbol **200.00 × 280.00**. Dashed opening **160.00 × 220.00**. | **BLOCKED.** Stile and head are text (`1550+TBD`, `700+TBD`). The sheet does not set X or Z. |
| H-01 | `cut/hatch/H-01_lounge.svg` | `cut/dxf/H-01_lounge.dxf` | **PASS** — 40 LINE, 31 TEXT. Closed symbol **280.00 × 120.00**. Dashed inner **160.00 × 70.00**. | **BLOCKED.** Hatch size is TBD. Dashed open-leaf lines are the sketch, not a developed leaf. No cut size added. |
| H-02 | `cut/hatch/H-02_rear.svg` | `cut/dxf/H-02_rear.dxf` | **PASS** — 38 LINE, 30 TEXT. Outer symbol **220.00 × 250.00**. Dashed intent **150.00 × 80.00**. | **BLOCKED.** Sheet says no cut size and “NOT A CUT” on the dashed rect. Hinge edge TBD. |
| P4-B | none | — | **BLOCKED.** No separate SVG master. `P4-B` is a label on `C-04_p4_overcab.svg` and a nest-index row. | **BLOCKED.** Developed flat not drawn. Bend allowance not applied. |
| P4-D | none | — | **BLOCKED.** No separate SVG master. | **BLOCKED.** Same undeveloped rule. |
| P4-E | none | — | **BLOCKED.** No separate SVG master. | **BLOCKED.** Same undeveloped rule. |
| P4 A–E sheet | `cut/C-04_p4_overcab.svg` | `cut/dxf/C-04_p4_overcab.dxf` | **PASS** as-drawn, **undeveloped**. 70 LINE, 47 TEXT. Five boxes, each **150.00 × 96.00** sheet mm. | **BLOCKED** as blanks. Labels (`≈1223 × 1911`, `1911 × ≈1830`, `≈1223 × ≈1830`) are TEXT estimates. Sheet says the plot is not to scale and flats are not developed. |

Existing envelope DXFs (`C-01`, `C-02`, `C-03`, `C-04_p4a`, `C-04_p4c`, `C-05`, `C-06`) were not rewritten.

---

## Residual risks

- **Text-as-paths.** Not done. Cut lengths that live in SVG `<text>` are DXF `TEXT` on `ANNOTATION`. A cutter that explodes text, or that cuts every layer, would cut words and the title block.
- **Overlapping annotation.** Table rules, title block, GO boxes, and notes share the sheet with the symbols. They are as-drawn. They are not a nest.
- **Undeveloped P4.** `C-04_p4_overcab.dxf` is the undeveloped sheet. Bend allowance is empty. Do not treat 150 × 96 as the flat.
- **Hatch size TBD.** H-01 and H-02 symbols are not opening sizes. D-04 / F-03 / FR-17 / FR-18 / FR-22 are still unfrozen.
- **Stroke width dropped.** DXF lines have no width. That is not a kerf.
- **NTS door and plate symbols.** DR-01 / DR-02 / C-PL geometry is paper size. Scaling it to a SoR sentence would invent the part.
- **Fill-only pads** (door hinge marks, grain arrows) are closed outlines on layer `FILL`, not a hole schedule.

---

## What this does not do

- Does not mark any part CUT-READY.
- Does not turn L2 GREEN.
- Does not release kerf, overlap, plate size, tube section, or hatch cut size.
- Does not authorize a fabricator send.

*End DXF-EXPORT-TRIAL Rev A. CONDITIONAL inventory. NOT CUT-READY. L2–L6 RED. HOLD.*
