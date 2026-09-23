# KE-Texh / TAMARAW — Phase-1 SHELL blueprint pack

Fabricator discussion drawings for the weatherproof shell only: box, over-cab loft, and openings. No interior fit-out.

**STAMP: CONDITIONAL — DISCUSS. NO-GO cut steel until the gates below are signed.**

**PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED.** Prototype only. This pack is not an LTO submission, a weight certificate, or a bolt-grade release.

## Sheet index

| Sheet | File | Content |
|-------|------|---------|
| I-00 | `sheets/I-00_index.svg` | Index, SoR table, release stamp |
| S-01 | `sheets/S-01_side_elevation.svg` | Side elevation, LH, front to left, 1:10 |
| S-02 | `sheets/S-02_plan.svg` | Plan / expansion envelope, 1:10 |
| S-03 | `sheets/S-03_front_elevation.svg` | Front elevation, over-cab nose, 1:10 |
| S-04 | `sheets/S-04_rear_elevation.svg` | Rear elevation, vertical flat back, 1:10 |
| S-05 | `sheets/S-05_section.svg` | Section A–A, over-cab and tail, 1:10 |
| S-06 | `sheets/S-06_rear_intent.svg` | Rear intent: window, lower hatch, ladder, lamps, bumper |
| S-07 | `sheets/S-07_roof_plan.svg` | Roof plan: lounge cutout; Phase-2 solar / AC / awning dashed only |
| D-01 | `sheets/D-01_outriggers.svg` | Bolted outriggers, hole schedule, Jay GO |
| D-02 | `sheets/D-02_landing_legs.svg` | Landing legs under the +1000 tail, blank kg placard |
| D-03 | `sheets/D-03_hose_rain.svg` | Hose / rain joints, FAIL-IF |
| D-04 | `sheets/D-04_hatch_lounge.svg` | Roof hatch and lounge frame, sealed to structure |
| D-05 | `sheets/D-05_ladder_mounts.svg` | Wall-ladder mounts into posts / sills, not a lift |
| D-06 | `sheets/D-06_bumper_splash.svg` | Bumper, splash, hitch vs leg swing under the +1000 tail |
| A-05 | `sheets/A-05_shell_assembly.svg` | Panel assembly P1–P8, 1:15 |

PNG previews of every sheet are in `previews/`. Review copies are in `artifacts/`. The full pack archive is `artifacts/tamaraw-blueprint-pack.tar.gz`.

Each SVG is an A1 landscape sheet. The `viewBox` is in millimetres. Stated dimensions are the cut figures. Do not scale a PDF or PNG.

## SoR cut figures

Single table: `DIMS.md`. Sheets use only these envelope figures:

- Shell floor **3647 × 1911** mm
- OAL **≈ 6300** mm (OEM 5300 + tail 1000)
- OAH **≤ 2500** mm with the roof hatch **closed**
- Over-cab **≈ 1223** mm
- Tail **+1000** mm
- Side growth **+100 mm / side**
- Wheelbase **3085** mm
- Bed **2647 × 1711** mm
- Shell exterior height **≈ 1830** mm (estimate)
- Loft **≈ 700** mm (estimate)
- Clear standing height **1900–2000** mm is a target. It is not closed by the 1830 mm exterior. Do not invent a new envelope to force it.
- Rear past axle **≈ 2015** mm

`4870` mm on S-02 and I-00 is the sum 1223 + 3647. It is not a separate measured datum.

Photo-scale REV A (overall length 5942) is **not a cut value** and is not drawn on any sheet. Do not import it.

## Gates — all unsigned on this revision

1. **As-found tape** — bed, rail spacing, cab roof, overhangs, VIN. Freeze on a shop traveler.
2. **Jay GO rail drill** — D-01 hole schedule signed. No undirected rail drill.
3. **Outriggers, legs, and kg placard on the sheets** — placard stays blank until a post-weigh.
4. **Hose / rain at the extension joint** — D-03, 10 minutes. FAIL-IF wet cabin, trapped water, or wet glands.
5. **Hatch frame** — D-04. FAIL-IF an open cut has no sealed frame, the rail is missing, water enters the lounge, or the hatch is open on the road. Occupied roof is parked only. Hose the closed perimeter before any parked-lounge claim.
6. **Ladder** — D-05. Roof access only. FAIL-IF the ladder is used as a jack or a lift, or the mounts loosen after vibration.
7. **Bumper / splash** — D-06. Keep the weep. Hitch clear of the landing-leg swing. FAIL-IF water is trapped under the occupied tail, or glands are wet at the bumper.
8. **Prototype only.** OAH ≤ 2500 means the hatch is closed. Renders are not farm-ready.

Bolt grade, plate size, weld size, sealant, and max kg are **TBD**. The Jay GO box is drawn empty on every sheet. Do not invent those numbers.

## Roles on D-01 … D-06

- **ENG** — load path, joints, legs, hatch frame, ladder hardpoints, bumper interface.
- **FIELD IoT** — splash, glands, hose test, stands, blank placard, lounge water, road hatch, ladder vibration.
- **FSD** — fabricator shop decision. Do not substitute a grade, a weld size, or a kilogram.

Phase-1 cut list is the shell, the openings, and the mount plates / rails. Seats, table, AC, solar, and awning are Phase-2 and are drawn **dashed on S-07 only**. They are not fab Done. S-06 opening sizes are intent, not a cut freeze.

## Regenerate

```bash
python3 tools/build_pack.py
```

Needs Pillow and CairoSVG, and DejaVu Sans. The script checks that dimension text does not collide and that banned photo-scale and bolt-grade tokens are absent from sheet text. A clean run prints `QA clean` for all fifteen sheets.

Mount notes: `notes/A06_bolt_mount_notes.md`.
