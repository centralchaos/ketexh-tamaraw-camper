# KE-Texh Tamaraw — Phase-1 SHELL

**R&D fabricator pack.** PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED.

**Stamp: CONDITIONAL. Gates unsigned = do not cut.**

A fabricator builds from this paper. A verbal brief is not the SoR. Do not scale a PNG. Renders are not cut geometry.

## How to read

1. [`DIMS.md`](DIMS.md) — the only envelope register.
2. [`blueprint-pack/sheets/I-00_index.svg`](blueprint-pack/sheets/I-00_index.svg) — release stamp and the elevation index.
3. Elevations S-01…S-08, details D-01…D-08, assembly A-05, in [`blueprint-pack/sheets/`](blueprint-pack/sheets/).
4. Patterns, frame, door, and hatches in [`cut/`](cut/).
5. Sequence, joints, holes, materials, BOM, and hose test in [`cut/shop/`](cut/shop/).
6. Gates to sign before any cut: [`notes/commissioning-gates.md`](notes/commissioning-gates.md).

Landscape sheet map: [`mermaid/INDEX.mmd`](mermaid/INDEX.mmd).

## Chassis lock

- Next-Gen Toyota Tamaraw LWB dropside · WB **3085 mm**
- Stock OAL × W × H **5300 × 1800 × 1800** · bed **2647 × 1711**
- Shell floor **3647 × 1911** (+1000 tail · +100/side) · OAL **≈ 6300** · OAH **≤ 2500** hatch closed
- Over-cab **≈ 1223** · shell exterior H **≈ 1830** estimate · clear standing **1900–2000** is a target, not closed by 1830
- Entry field-locate target **700 × 1550** on P2. Not a cut freeze.

Rejected: floor width 1912, over-cab 1215, entry 780 × 1550, photo-scale overall length. See DIMS.md.

## Sheet index

| Sheet | Path | Role |
|-------|------|------|
| CVR-00 | `cut/CVR-00_cover.svg` | Cover, reading order, rejected substitutions |
| I-00 | `blueprint-pack/sheets/I-00_index.svg` | Index, SoR, unsigned gates |
| S-01…S-06 | `blueprint-pack/sheets/` | Elevations and section |
| S-07 | `blueprint-pack/sheets/S-07_roof_plan.svg` | Lounge intent. Solar and awning are dashed hooks. |
| S-08 | `blueprint-pack/sheets/S-08_service_plan.svg` | AC curb and generator bay. Provisions only. |
| D-01…D-06 | `blueprint-pack/sheets/` | Outriggers, legs, hose, hatch, ladder, bumper |
| D-07 | `blueprint-pack/sheets/D-07_generator.svg` | Generator bay. Not the unit. |
| D-08 | `blueprint-pack/sheets/D-08_ac.svg` | AC curb. Not the unit. |
| A-05 | `blueprint-pack/sheets/A-05_shell_assembly.svg` | Panels P1–P8 |
| C-00…C-06 | `cut/` | Nests and flat patterns |
| C-FR, C-PL | `cut/` | Member cut list and plates |
| F-00…F-03 | `cut/frame/` | Frame |
| DR-01, DR-02 | `cut/door/` | Entry leaf and jamb |
| H-01…H-03 | `cut/hatch/` | Hatch leaves and hardware TBD |
| AS-01, J-01, FS-01, MAT-01, BOM-01, QA-01 | `cut/shop/` | Sequence through hose test |

## Residual NO-GO

Do not cut until these are signed: as-found tape, Jay GO rail drill, Eng tube/weld, outriggers and legs, weigh before any kg, hose test, hatch frame, ladder, bumper, and the D-07 / D-08 provision rules. Generator and AC units are hooks, not BOM Done lines. No bolt grade, kW, BTU, or kilogram is released.

## Other trees

| Path | Role |
|------|------|
| [`blueprint-pack/`](blueprint-pack/) | A1 elevation and detail sheets |
| [`cut/`](cut/) | Patterns and shop sheets |
| [`svg/`](svg/) | Authoritative side and plan SoR |
| [`fab-pack/`](fab-pack/) | Earlier fab notes. `reference/` is photo-scale only — do not cut from it. |
| [`mermaid/`](mermaid/) | Sheet index and module diagrams |

Owner: KE-Texh / Jose Carlo Sia (`centralchaos`).
