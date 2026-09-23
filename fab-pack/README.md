# KE-Texh Tamaraw — Phase-1 SHELL fab-pack

**Status stamp:** Architect **CONDITIONAL** · SoR = `svg/` pack only  
**Watermark (every sheet/note):** PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED

Phase-1 = **SHELL ONLY**: weatherproof box + over-cab room + roof + openings.  
No interior fit-out, cabinetry, or wet systems beyond placeholders.

---

## Locked dim table (cut / envelope)

| Datum | Value |
|-------|-------|
| Chassis | Next-Gen Toyota Tamaraw LWB dropside |
| WB | **3085 mm** |
| Stock OAL × W × H | **5300 × 1800 × 1800** |
| Bed | **2647 × 1711** |
| Camper OAL | **≈ 6300** (OEM + TAIL EXT 1000) |
| Shell floor | **3647 × 1911** |
| OAH | **≤ 2500** |
| Over-cab | **≈ 1223** |
| Tail / side | **+1000** / **+100 per side** |

Full table + notes: [`DIMS.md`](./DIMS.md).

**NOT ADOPTED for cut:** photo-scale `plans/clean` REV A (OAL 5942 / OAH 2342). Kept under [`reference/`](./reference/) as ratio/orthographic study only.

---

## Sheet index

| Path | Role |
|------|------|
| [`00_COVER.md`](./00_COVER.md) | One-page fabricator brief |
| [`DIMS.md`](./DIMS.md) | Single-source dimensions |
| [`sheets/tamaraw_shell_side.svg`](./sheets/tamaraw_shell_side.svg) | Side elevation (SoR) |
| [`sheets/shell_side.png`](./sheets/shell_side.png) | Side PNG preview |
| [`sheets/tamaraw_shell_plan.svg`](./sheets/tamaraw_shell_plan.svg) | Plan / expansion (SoR) |
| [`sheets/shell_plan.png`](./sheets/shell_plan.png) | Plan PNG preview |
| [`A05_shell_assembly.png`](./A05_shell_assembly.png) | Panel assembly P1–P8 |
| [`A05_shell_assembly.svg`](./A05_shell_assembly.svg) | Assembly vector source |
| [`A06_bolt_mount_notes.md`](./A06_bolt_mount_notes.md) | Outriggers, legs, placard, weep |
| [`reference/`](./reference/) | Clean REV A A00–A04 — **not cut values** |

---

## Fab notes (short)

1. Bolt shell via **outriggers to bed/chassis rails** — not GI dropside skin alone.
2. Landing legs hard points when occupied.
3. Weep / drain at floor and openings.
4. Post-weigh **max-kg placard**; freeze as-found VIN/tape before cut.
5. Field-verify all dims on the actual vehicle.

## Watermark rules

- Place once per sheet in title block (not over geometry).
- Exact string: **PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED**
- Do not remove for shop prints.

## QA checklist

- [x] SoR dims from `svg/` only (6300 / 3647×1911)
- [x] REV A photo pack isolated in `reference/`
- [x] No overlapping labels on A05 (P1–P8 leaders clear)
- [x] Watermark on cover, DIMS, A06, A05

Source regenerator for side/plan: `/workspace/tamaraw-camper/svg/build_svgs.py`
