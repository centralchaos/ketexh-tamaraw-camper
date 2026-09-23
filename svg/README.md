# Tamaraw Phase-1 shell — scalable SVG silhouettes

Fabricator-readable vector drawings for the **KE-Texh Tamaraw camper SHELL**
(Phase-1: box + **over-cab ROOM** + roof + simple openings). Not photoreal. Not LTO-certified.

| File | Content |
|------|---------|
| [`tamaraw_shell_side.svg`](./tamaraw_shell_side.svg) | Side elevation — chassis/cab + shell silhouette + openings + dims |
| [`tamaraw_shell_plan.svg`](./tamaraw_shell_plan.svg) | Plan — stock bed vs Phase-1 exterior + over-cab projection |
| [`shell_side.png`](./shell_side.png) / [`shell_plan.png`](./shell_plan.png) | 150 dpi PNG previews (side 1:20 sheet, plan 1:10 sheet) |
| [`build_svgs.py`](./build_svgs.py) | Regenerator |

## Drafting quality rules (enforced in generator)

1. No overlapping dimension lines with each other or with geometry.
2. No text overlapping other text, dims, or geometry.
3. No redundant guide lines that double the shell polygon stroke.
4. Opening labels use **leader lines outside** openings (never centered inside door/window rects).
5. Horizontal dims **below** the vehicle only, stacked with ≥120 mm clear vertical gaps.
6. Vertical dims to the **right** only; shell ext. H / loft clear / WB live in the **DIM TABLE** (title block).
7. Over-cab length dim **above** the roof only, clear of title text.
8. Title + watermark + notes **only** in a reserved title-block band (separator + empty margin from silhouette).
9. Shape preserved: tall over-cab room, continuous roof, long rear, entry + 2 body windows + over-cab window.
10. Watermark once: **PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED**.

## Shape alignment (KE-TEXH concept board)

1. **Over-cab ROOM** — loft over full cab roof (~x 780 mm). Continuous high roof ≤ **2500 mm**. Loft floor ≈ **1800 mm AGL**; loft clear ≈ **700 mm**. Over-cab length ≈ **1223 mm**.
2. **Extended rear (Carlo GO)** — shell floor = bed **2647** + **TAIL EXT 1000** = **3647 mm** (body beyond dropside). Rear past axle ≈ **2015 mm**, vertical flat back. Overall ≈ **6300** (OEM 5300 + TAIL EXT).
3. **Openings** — entry behind cab; two main side windows; over-cab side window; optional front-face window (dashed).
4. Public LWB dims: WB **3085**, bed **2647×1711**, OEM overall ≈ **5300**, SHELL_W **1911** (+100/side), H ≤ **2500**. Weight / rear overhang / LTO risk — **NOT LTO-CERTIFIED**.

## How these were derived

**Method: hand-constructed geometric SVG** — not a pixel auto-trace.

1. Public-press LWB dims (verify on VIN): bed **2647 × 1711 mm**, WB **3085 mm**, OEM ≈ **6300 × 1800 × 1800 mm**.
2. Phase-1 envelope: SHELL_W **1911 mm** (bed 1711 + 2×100; Carlo-locked, replaces old 2000 hard cap), shell floor = bed + TAIL EXT **3647 mm**, H ≤ **2500 mm**, clear H **1900–2000 mm**.
3. Side proportions aligned to KE-TEXH concept board. Openings are simple rectangles.
4. Millimetre `viewBox` SVG polygons/rects.

### Key callouts

- Side: shell floor L ≈ 3647 (bed 2647 + TAIL EXT 1000); over-cab ≈ 1223; overall L ≈ 6300; H ≤ 2500; shell ext. H ≈ 1830; loft clear ≈ 700; rear past axle ≈ 2015; WB 3085 (DIM TABLE).
- Plan: stock bed 1711 W × 2647 L vs shell 1911 W × 3647 L; TAIL EXT +1000; +100 mm/side (EXPAND=100); over-cab ≈ 1223 mm.
- Disclaimer: body extension beyond dropside — PRELIMINARY; VERIFY ON VEHICLE; NOT LTO-CERTIFIED; weight / overhang / LTO risk.

## Rebuild

```bash
cd /workspace/tamaraw-camper
.venv/bin/pip install cairosvg   # if needed
.venv/bin/python svg/build_svgs.py
```

## Disclaimer

PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED. Field-measure before cutting steel. R&D fabricator pack. Gates unsigned = do not cut.
