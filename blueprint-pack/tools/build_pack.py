"""Generate the KE-Texh Tamaraw Phase-1 SHELL blueprint pack.

Cut / envelope figures come only from the Architect CONDITIONAL SoR.
Photo-scale overall length is not drawn. Bolt grade, plate size, weld size,
and max-kg stay TBD with Jay-GO boxes.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from sheetlib import TITLE_TOP, Sheet, qa_sheet  # noqa: E402

# --- Locked SoR (mm). Do not replace these with photo-scale figures. ---
WB = 3085
STOCK_OAL = 5300
STOCK_W = 1800
STOCK_H = 1800
BED_L = 2647
BED_W = 1711
TREAD = 1510
TAIL = 1000
SIDE = 100
SHELL_L = BED_L + TAIL  # 3647
SHELL_W = BED_W + 2 * SIDE  # 1911
OAL = STOCK_OAL + TAIL  # 6300
OAH = 2500
OVERCAB = 1223
REAR_PAST = 2015
EXT_H = 1830
LOFT = 700
CLEAR_LO = 1900
CLEAR_HI = 2000
ENVELOPE_L = OVERCAB + SHELL_L  # 4870, sum of locked lengths — not a new datum

BED_REAR = STOCK_OAL
BED_FRONT = BED_REAR - BED_L
NOSE = BED_FRONT - OVERCAB
REAR_X = OAL
REAR_AXLE = REAR_X - REAR_PAST
FRONT_AXLE = REAR_AXLE - WB
ROOF_Z = OAH
FLOOR_Z = ROOF_Z - EXT_H
CAB_ROOF_Z = ROOF_Z - LOFT

# Opening sizes are the uploaded side-elevation schematics — field locate, not a cut freeze.
DOOR = (BED_FRONT + 80, FLOOR_Z + 40, 700, 1550)  # x, z_bottom, w, h
WIN1 = (BED_FRONT + 920, 1750, 780, 520)
WIN2 = (BED_FRONT + 1860, 1750, 780, 520)
WIN_OC = (NOSE + 180, 1980, 700, 320)

WHEEL_R = 300  # schematic only — not a cut dimension

assert SHELL_L == 3647
assert SHELL_W == 1911
assert OAL == 6300
assert ENVELOPE_L == 4870
assert REAR_X - REAR_AXLE == REAR_PAST
assert REAR_AXLE - FRONT_AXLE == WB
assert BED_REAR - BED_FRONT == BED_L
assert REAR_X - BED_FRONT == SHELL_L
assert REAR_X - BED_REAR == TAIL
assert BED_FRONT - NOSE == OVERCAB
assert ROOF_Z - FLOOR_Z == EXT_H
assert ROOF_Z - CAB_ROOF_Z == LOFT

SHEETS_DIR = ROOT / "sheets"
PREVIEWS = ROOT / "previews"
ARTIFACTS = ROOT / "artifacts"

WM = "PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED"


def _assert_fits(sheet: Sheet, text: str, size: float, max_w: float, weight: str = "normal"):
    w = sheet.text_width(text, size, weight)
    if w > max_w:
        raise SystemExit(f"{sheet.sid}: text too wide ({w:.1f}>{max_w:.1f}): {text}")


def finish(sheet: Sheet) -> Sheet:
    sheet.border()
    sheet.title_block()
    return sheet


def hatch_defs(sheet: Sheet):
    sheet.defs.append(
        """
<pattern id="hatch" patternUnits="userSpaceOnUse" width="3.2" height="3.2" patternTransform="rotate(45)">
  <line x1="0" y1="0" x2="0" y2="3.2" stroke="#6a6a6a" stroke-width="0.25"/>
</pattern>
<pattern id="hatch-red" patternUnits="userSpaceOnUse" width="3.2" height="3.2" patternTransform="rotate(45)">
  <line x1="0" y1="0" x2="0" y2="3.2" stroke="#9b1c1c" stroke-width="0.3"/>
</pattern>
"""
    )


# ---------------------------------------------------------------------------
# Shared side geometry (1:10). Front bumper at real x = 0.
# ---------------------------------------------------------------------------

S = 0.1
OX = 48.0
GY = 332.0  # sheet y of ground


def X(real: float) -> float:
    return OX + real * S


def Y(z: float) -> float:
    return GY - z * S


def draw_end_tire(sheet: Sheet, cx: float, ground: float):
    """End-view tire. Width is schematic and is not a cut dimension."""
    tw = 16.0
    th = WHEEL_R * 2 * S
    sheet.rect(cx - tw / 2, ground - th, tw, th, fill="#1a1a1a", stroke="#141414", sw=0.35)
    sheet.circle(cx, ground - th / 2, 3.2, fill="#d5d5d5", stroke="#141414", sw=0.25)


def draw_side_vehicle(sheet: Sheet):
    """Cab, wheels, rail, and the shell side outline."""
    # Ground
    sheet.line(30, GY, X(REAR_X) + 16, GY, sw=0.45, layer="geom")

    # Cab — schematic, not a shell cut part
    cab = [
        (0, 520),
        (220, 560),
        (680, 740),
        (1000, 1080),
        (1340, CAB_ROOF_Z),
        (BED_FRONT, CAB_ROOF_Z),
        (BED_FRONT, 1020),
        (2350, 780),
        (1680, 690),
        (920, 650),
        (260, 580),
        (0, 520),
    ]
    sheet.polygon([(X(x), Y(z)) for x, z in cab], fill="#efefef", stroke="#141414", sw=0.45)
    # Cab side glass — unlabeled, so it is not read as a shell opening
    sheet.rect(X(1500), Y(1620), 620 * S, 460 * S, fill="#ffffff", stroke="#141414", sw=0.3)

    for axle in (FRONT_AXLE, REAR_AXLE):
        sheet.circle(X(axle), Y(WHEEL_R), WHEEL_R * S, fill="#1a1a1a", stroke="#141414", sw=0.4)
        sheet.circle(X(axle), Y(WHEEL_R), WHEEL_R * S * 0.40, fill="#d0d0d0", stroke="#141414", sw=0.3)

    # Bed rails under the stock bed only (not under the tail cantilever)
    sheet.rect(X(BED_FRONT), Y(FLOOR_Z), BED_L * S, 80 * S, fill="#4d4d4d", stroke="#141414", sw=0.3)

    shell = [
        (BED_FRONT, FLOOR_Z),
        (REAR_X, FLOOR_Z),
        (REAR_X, ROOF_Z),
        (NOSE, ROOF_Z),
        (NOSE, CAB_ROOF_Z),
        (BED_FRONT, CAB_ROOF_Z),
    ]
    sheet.polygon([(X(x), Y(z)) for x, z in shell], fill="#fbfbfb", stroke="#141414", sw=0.7)
    dx, dz, dw, dh = DOOR
    sheet.rect(X(dx), Y(dz + dh), dw * S, dh * S, fill="#ffffff", stroke="#141414", sw=0.4, dash="3.2 1.8")
    for win in (WIN1, WIN2, WIN_OC):
        wx, wz, ww, wh = win
        sheet.rect(X(wx), Y(wz + wh), ww * S, wh * S, fill="#ffffff", stroke="#141414", sw=0.4)


def draw_section_panels(sheet: Sheet):
    """Exaggerated cut panels. Thickness is graphic only — gauge is TBD."""
    t = 90  # real-mm graphic thickness (9 mm on sheet). Not a cut gauge.
    # Roof, hanging below the roof line
    sheet.rect(X(NOSE), Y(ROOF_Z), (REAR_X - NOSE) * S, t * S, fill="url(#hatch)", stroke="#141414", sw=0.4)
    # Floor, hanging below the floor line
    sheet.rect(X(BED_FRONT), Y(FLOOR_Z), SHELL_L * S, t * S, fill="url(#hatch)", stroke="#141414", sw=0.4)
    # Rear wall, inboard of the rear face
    sheet.rect(X(REAR_X - t), Y(ROOF_Z), t * S, (ROOF_Z - FLOOR_Z) * S, fill="url(#hatch)", stroke="#141414", sw=0.4)
    # Over-cab nose wall
    sheet.rect(X(NOSE), Y(ROOF_Z), t * S, (ROOF_Z - CAB_ROOF_Z) * S, fill="url(#hatch)", stroke="#141414", sw=0.4)
    # Loft underside / cab-roof joint panel
    sheet.rect(X(NOSE), Y(CAB_ROOF_Z + t), (BED_FRONT - NOSE) * S, t * S, fill="url(#hatch)", stroke="#141414", sw=0.4)
    # Living-box front wall, behind the cab
    sheet.rect(X(BED_FRONT), Y(CAB_ROOF_Z), t * S, (CAB_ROOF_Z - FLOOR_Z) * S, fill="url(#hatch)", stroke="#141414", sw=0.4)


def bubble(sheet: Sheet, x, y, letter: str):
    sheet.circle(x, y, 4.2, fill="#ffffff", stroke="#141414", sw=0.45)
    sheet.text(x, y + 1.15, letter, 3.3, anchor="middle", weight="bold")


def stack_dims_below(sheet: Sheet, rows: list[tuple], first_y: float, step: float = 18.0):
    """rows: (x1, x2, label, ext_y) in sheet mm."""
    for i, (x1, x2, label, ext_y) in enumerate(rows):
        sheet.dim_h(x1, x2, first_y + i * step, label, ext_y)


# ---------------------------------------------------------------------------
# S-01 Side elevation
# ---------------------------------------------------------------------------

def _sheet_s01_clean() -> Sheet:
    s = Sheet("S-01", "SIDE ELEVATION — LH, FRONT TO LEFT", "SCALE 1:10", 2)
    draw_side_vehicle(s)

    oc_x, oc_z, oc_w, oc_h = WIN_OC
    # Leader jogs left of the nose, above the roof, clear of the loft dim.
    x_jog = X(NOSE) - 28
    s.circle(X(oc_x + oc_w / 2), Y(oc_z + oc_h), 0.9, fill="#141414", stroke="none")
    s.polyline(
        [
            (X(oc_x), Y(oc_z + oc_h / 2)),
            (x_jog, Y(oc_z + oc_h / 2)),
            (x_jog, 42),
        ],
        sw=0.28,
        layer="dim",
    )
    s.text(x_jog - 2, 38, "OVER-CAB WIN", 3.05, anchor="end")

    door_x, door_z, door_w, door_h = DOOR
    s.line(X(door_x + door_w / 2), Y(door_z + door_h), X(door_x + door_w / 2), 44, sw=0.28, layer="dim")
    s.circle(X(door_x + door_w / 2), Y(door_z + door_h), 0.9, fill="#141414", stroke="none")
    s.text(X(door_x + door_w / 2), 38, "ENTRY 700×1550", 3.05, anchor="middle")

    for win, extra in ((WIN1, 0), (WIN2, 0)):
        wx, wz, ww, wh = win
        cx = X(wx + ww / 2)
        s.line(cx, Y(wz + wh), cx, 44, sw=0.28, layer="dim")
        s.circle(cx, Y(wz + wh), 0.9, fill="#141414", stroke="none")
        s.text(cx, 38, "WINDOW", 3.05, anchor="middle")

    # Over-cab length, above the roof
    s.dim_h(X(NOSE), X(BED_FRONT), 62, "OVER-CAB ≈ 1223 mm", Y(ROOF_Z))
    # Loft, left of the nose
    s.dim_v(Y(ROOF_Z), Y(CAB_ROOF_Z), X(NOSE) - 16, "LOFT ≈ 700 mm", X(NOSE), side="left")
    # Shell exterior height and overall height, right of the rear face
    s.dim_v(Y(ROOF_Z), Y(FLOOR_Z), X(REAR_X) + 22, "SHELL EXT H ≈ 1830 mm", X(REAR_X), side="right")
    s.dim_v(Y(ROOF_Z), GY, X(REAR_X) + 52, "H TARGET ≤ 2500 mm", X(REAR_X), side="right")

    rows = [
        (X(FRONT_AXLE), X(REAR_AXLE), "WB 3085 mm", Y(WHEEL_R)),
        (X(BED_FRONT), X(BED_REAR), "BED L 2647 mm", Y(FLOOR_Z)),
        (X(REAR_AXLE), X(REAR_X), "REAR PAST AXLE ≈ 2015 mm", GY),
        (X(BED_REAR), X(REAR_X), "TAIL EXT +1000 mm", Y(FLOOR_Z)),
        (X(BED_FRONT), X(REAR_X), "SHELL FLOOR L = 3647 mm", Y(FLOOR_Z)),
        (X(0), X(REAR_X), "OAL ≈ 6300 mm  (OEM 5300 + TAIL EXT)", GY),
    ]
    stack_dims_below(s, rows, GY + 16, 17.5)

    s.text(36, 468, "OPENINGS ARE FIELD LOCATE — NOT A CUT FREEZE.  WHEELS, CAB, AND RAIL HEIGHT ARE SCHEMATIC — NOT CUT DIMS.", 2.7)
    s.text(36, 480, "CLEAR STANDING H TARGET 1900–2000 IS NOT CLOSED BY SHELL EXT H ≈ 1830.  AS-FOUND TAPE GOVERNS.", 2.7)
    s.text(36, 492, "PHASE-2 ROOF HOOKS (SOLAR / AC / AWNING) ARE DASHED ON S-07.   SECTION A–A: SEE S-02 AND S-05.", 2.7)
    return finish(s)


# ---------------------------------------------------------------------------
# S-02 Plan
# ---------------------------------------------------------------------------

def sheet_s02() -> Sheet:
    s = Sheet("S-02", "PLAN — LOOKING DOWN, FRONT TO LEFT, NEAR EDGE = LH", "SCALE 1:10", 3)
    hatch_defs(s)

    nose_x = 168.0
    bed_x = nose_x + OVERCAB * S
    rear_x = bed_x + SHELL_L * S
    top = 78.0
    bot = top + SHELL_W * S
    bed_top = top + SIDE * S
    bed_bot = bot - SIDE * S
    bed_rear_x = bed_x + BED_L * S

    # Over-cab (dashed) full shell width, then floor.
    s.rect(nose_x, top, OVERCAB * S, SHELL_W * S, fill="#f4f4f4", stroke="#141414", sw=0.55, dash="3 1.6")
    s.rect(bed_x, top, SHELL_L * S, SHELL_W * S, fill="#ffffff", stroke="#141414", sw=0.7)
    # Width-growth bands on the floor only
    s.rect(bed_x, top, SHELL_L * S, SIDE * S, fill="url(#hatch)", stroke="#141414", sw=0.25)
    s.rect(bed_x, bed_bot, SHELL_L * S, SIDE * S, fill="url(#hatch)", stroke="#141414", sw=0.25)
    # Stock bed
    s.rect(bed_x, bed_top, BED_L * S, BED_W * S, fill="none", stroke="#141414", sw=0.4, dash="2.4 1.4")

    # Internal labels, above the centerline so section A–A can run through mid-depth.
    mid = (top + bot) / 2.0
    s.text((nose_x + bed_x) / 2, top + 28, "OVER-CAB", 3.4, anchor="middle", weight="bold")
    s.text((nose_x + bed_x) / 2, top + 40, "ROOM ≈ 1223 mm", 3.1, anchor="middle")
    s.text((bed_x + bed_rear_x) / 2, top + 36, "STOCK BED", 3.4, anchor="middle", weight="bold")
    s.text((bed_x + bed_rear_x) / 2, top + 48, "1711 W × 2647 L mm", 3.1, anchor="middle")
    s.text((bed_rear_x + rear_x) / 2, top + 36, "TAIL EXT", 3.4, anchor="middle", weight="bold")
    s.text((bed_rear_x + rear_x) / 2, top + 48, "+1000 mm", 3.1, anchor="middle")

    # Section A–A on centerline
    s.line(nose_x - 8, mid, rear_x + 8, mid, sw=0.45, dash="6 2.2 1.2 2.2", layer="dim")
    s.text(nose_x - 12, mid + 1.2, "A", 4.0, anchor="end", weight="bold")
    s.text(rear_x + 12, mid + 1.2, "A", 4.0, anchor="start", weight="bold")
    s.text(bed_x + 8, mid - 8, "SECTION A–A  →  S-05", 2.8)

    # Entry on the near (LH / bottom) edge, field locate
    door_x = bed_x + 8
    s.rect(door_x, bot - 6, 70 * S, 6, fill="#ffffff", stroke="#141414", sw=0.4, dash="2 1.2")
    s.line(door_x + 20, bot, door_x + 20, bot + 12, sw=0.28, layer="dim")
    s.text(door_x + 22, bot + 16, "ENTRY (LH) · FIELD LOCATE", 2.9)

    # Phase-2 roof gear is drawn dashed on S-07 only. This plan does not cut it.
    s.text(rear_x + 12, mid + 16, "PHASE-2 ROOF GEAR", 2.6)
    s.text(rear_x + 12, mid + 26, "SEE S-07 — DASHED", 2.6)
    s.text(rear_x + 12, mid + 36, "NOT A CUT ON S-02", 2.6)

    # Dimensions
    s.dim_h(nose_x, bed_x, bot + 36, "OVER-CAB ≈ 1223 mm", bot)
    s.dim_h(bed_x, rear_x, bot + 58, "SHELL FLOOR L = 3647 mm", bot)
    s.dim_h(bed_rear_x, rear_x, bot + 80, "TAIL EXT +1000 mm", bot)
    s.dim_h(nose_x, rear_x, bot + 102, "OVER-CAB + FLOOR = 4870 mm", bot)
    s.dim_v(top, bot, rear_x + 58, "SHELL W = 1911 mm (+100/SIDE)", rear_x, side="right")
    s.dim_v(bed_top, bed_bot, nose_x - 22, "BED W = 1711 mm", nose_x, side="left")

    s.text(36, 458, "HATCHED BANDS = +100 mm / SIDE ON THE FLOOR ONLY.  DASHED BOX = OVER-CAB ROOM.", 2.7)
    s.text(36, 470, "4870 mm IS THE SUM OF LOCKED LENGTHS (1223 + 3647), NOT A SEPARATE MEASURED DATUM.", 2.7)
    s.text(36, 482, "OEM CHASSIS WIDTH ≈ 1800 mm IS A CHASSIS REF (SEE I-00).  IT IS NOT A SHELL CUT WIDTH.", 2.7)
    s.text(36, 494, "DO NOT SCALE.  ENTRY AND WINDOWS: FIELD LOCATE.  SEE D-01 FOR RAILS UNDER THIS PLAN.", 2.7)
    return finish(s)


# ---------------------------------------------------------------------------
# S-03 Front
# ---------------------------------------------------------------------------

def sheet_s03() -> Sheet:
    s = Sheet("S-03", "FRONT ELEVATION — OVER-CAB NOSE", "SCALE 1:10", 4)
    # Center the shell width in the right-hand drawing field.
    left = 360.0
    right = left + SHELL_W * S
    cx = (left + right) / 2.0
    ground = 430.0
    roof = ground - OAH * S
    cab_roof = ground - CAB_ROOF_Z * S
    cab_left = cx - (STOCK_W * S) / 2.0
    cab_w = STOCK_W * S

    s.line(left - 40, ground, right + 70, ground, sw=0.45)
    # Loft nose — the only Phase-1 shell face at the front
    s.rect(left, roof, SHELL_W * S, LOFT * S, fill="#fbfbfb", stroke="#141414", sw=0.7)
    # Optional front-face opening — no cut size
    s.rect(cx - 28, roof + 14, 56, 28, fill="#ffffff", stroke="#141414", sw=0.4, dash="2.2 1.3")
    s.line(cx - 28, roof + 28, 250, 198, sw=0.28, layer="dim")
    s.text(246, 196, "OPTIONAL FRONT-FACE — NO CUT SIZE", 2.7, anchor="end")

    # Wheels at tread
    for sign in (-1, 1):
        draw_end_tire(s, cx + sign * (TREAD * S) / 2.0, ground)

    # Cab body sits above the tires. Bottom is schematic, not a cut height.
    cab_bottom = ground - 72
    s.rect(cab_left, cab_roof, cab_w, cab_bottom - cab_roof, fill="#efefef", stroke="#141414", sw=0.45)
    s.polygon(
        [
            (cab_left + 18, cab_roof + 16),
            (cab_left + cab_w - 18, cab_roof + 16),
            (cab_left + cab_w - 28, cab_bottom - 28),
            (cab_left + 28, cab_bottom - 28),
        ],
        fill="#ffffff",
        stroke="#141414",
        sw=0.3,
    )

    s.dim_h(cab_left, cab_left + cab_w, roof - 36, "CAB W ≈ 1800 mm REF", cab_roof)
    s.dim_h(left, right, roof - 16, "SHELL W = 1911 mm", roof)
    s.dim_v(roof, cab_roof, right + 16, "LOFT ≈ 700 mm", right, side="right")
    s.dim_v(roof, ground, right + 46, "H TARGET ≤ 2500 mm", right, side="right")
    s.dim_h(cx - TREAD * S / 2, cx + TREAD * S / 2, ground + 22, "TREAD F 1510 mm REF", ground)

    s.text(24, 40, "FRONT VIEW SHOWS THE OVER-CAB NOSE ONLY.", 3.2, weight="bold")
    s.text(24, 56, "The living box is aft of the cab", 2.8)
    s.text(24, 68, "and does not appear in this view.", 2.8)
    s.text(24, 88, "SHELL W 1911 = BED 1711 + 100/SIDE.", 2.8)
    s.text(24, 100, "Cab width is chassis reference,", 2.8)
    s.text(24, 112, "not a shell cut.", 2.8)
    s.text(24, 132, "SHELL EXT H ≈ 1830 — SEE S-01 / S-04.", 2.8)
    s.text(24, 152, "Wheels and cab are schematic.", 2.8)
    s.text(24, 172, "No interior. No Phase-2 gear.", 2.8)
    return finish(s)


# ---------------------------------------------------------------------------
# S-04 Rear
# ---------------------------------------------------------------------------

def sheet_s04() -> Sheet:
    s = Sheet("S-04", "REAR ELEVATION — VERTICAL FLAT BACK", "SCALE 1:10", 5)
    left = 360.0
    right = left + SHELL_W * S
    cx = (left + right) / 2.0
    ground = 430.0
    roof = ground - OAH * S
    floor = ground - FLOOR_Z * S
    bed_left = cx - (BED_W * S) / 2.0
    bed_right = cx + (BED_W * S) / 2.0

    s.line(left - 30, ground, right + 70, ground, sw=0.45)
    # Rear wall from floor to roof
    s.rect(left, roof, SHELL_W * S, EXT_H * S, fill="#fbfbfb", stroke="#141414", sw=0.7)
    # Dashed bed / rail width behind the tail skin
    s.line(bed_left, roof, bed_left, floor, sw=0.3, dash="2.2 1.4")
    s.line(bed_right, roof, bed_right, floor, sw=0.3, dash="2.2 1.4")

    s.text(cx, (roof + floor) / 2, "P5 REAR WALL", 3.6, anchor="middle", weight="bold")
    s.text(cx, (roof + floor) / 2 + 12, "VERTICAL FLAT BACK", 3.0, anchor="middle")

    # Weep ticks at the floor line, leaders to the left margin
    for i, wx in enumerate((left + 18, cx, right - 18)):
        s.polygon([(wx - 3, floor), (wx + 3, floor), (wx, floor + 5)], fill="#141414", stroke="none")
    s.line(left + 18, floor + 5, left - 16, floor + 20, sw=0.28, layer="dim")
    s.text(left - 18, floor + 18, "WEEP OUTBOARD", 2.8, anchor="end")
    s.text(left - 18, floor + 30, "SEE D-03", 2.8, anchor="end")

    # Leg ticks in the +100 side zones, outboard of the tires.
    s.rect(left + 1, floor + 2, 8, 18, fill="#ffffff", stroke="#141414", sw=0.4)
    s.rect(right - 9, floor + 2, 8, 18, fill="#ffffff", stroke="#141414", sw=0.4)
    s.line(left + 5, floor + 10, 300, 328, sw=0.28, layer="dim")
    s.text(296, 326, "LEG HARD POINT — D-02", 2.7, anchor="end")
    s.text(296, 338, "OCCUPIED ONLY ON STANDS", 2.7, anchor="end")

    for sign in (-1, 1):
        draw_end_tire(s, cx + sign * (TREAD * S) / 2.0, ground)

    s.dim_h(bed_left, bed_right, roof - 36, "BED W = 1711 mm", roof)
    s.dim_h(left, right, roof - 16, "SHELL W = 1911 mm", roof)
    s.dim_v(roof, floor, right + 18, "SHELL EXT H ≈ 1830 mm", right, side="right")
    s.dim_v(roof, ground, right + 50, "H TARGET ≤ 2500 mm", right, side="right")
    s.dim_h(cx - TREAD * S / 2, cx + TREAD * S / 2, ground + 22, "TREAD R 1510 mm REF", ground)

    s.text(24, 40, "REAR FACE IS A FLAT WALL.", 3.2, weight="bold")
    s.text(24, 56, "No rear door in Phase-1.", 2.8)
    s.text(24, 76, "Dashed lines = bed width 1711.", 2.8)
    s.text(24, 88, "Each side of the wall is", 2.8)
    s.text(24, 100, "+100 mm past the bed.", 2.8)
    s.text(24, 120, "Weep must leave the shell.", 2.8)
    s.text(24, 132, "Legs carry the occupied tail.", 2.8)
    s.text(24, 144, "See D-02 and D-03.", 2.8)
    return finish(s)


# ---------------------------------------------------------------------------
# S-05 Section
# ---------------------------------------------------------------------------

def _sheet_s05_clean() -> Sheet:
    s = Sheet("S-05", "SECTION A–A — OVER-CAB AND REAR EXTENSION", "SCALE 1:10", 6)
    hatch_defs(s)

    s.line(30, GY, X(REAR_X) + 14, GY, sw=0.45)
    cab = [
        (0, 520),
        (220, 560),
        (680, 740),
        (1000, 1080),
        (1340, CAB_ROOF_Z),
        (BED_FRONT, CAB_ROOF_Z),
        (BED_FRONT, 1020),
        (2350, 780),
        (1680, 690),
        (920, 650),
        (260, 580),
        (0, 520),
    ]
    s.polygon([(X(x), Y(z)) for x, z in cab], fill="none", stroke="#141414", sw=0.35, dash="2.4 1.5")
    s.line(X(REAR_AXLE), GY, X(REAR_AXLE), Y(FLOOR_Z), sw=0.3, dash="2 1.4", layer="dim")

    draw_section_panels(s)

    # Void labels — kept off the hatched bands (bands are ~9 mm thick on sheet).
    s.text((X(NOSE) + X(BED_FRONT)) / 2, Y(ROOF_Z) + 28, "LOFT VOID", 3.3, anchor="middle", weight="bold")
    s.text((X(NOSE) + X(BED_FRONT)) / 2, Y(ROOF_Z) + 40, "≈ 700 mm EST.", 2.9, anchor="middle")

    s.text((X(BED_FRONT) + X(REAR_X)) / 2, Y(2000), "LIVING VOID — NO INTERIOR THIS PHASE", 3.2, anchor="middle", weight="bold")
    s.text((X(BED_FRONT) + X(REAR_X)) / 2, Y(2000) + 12, "CLEAR H TARGET 1900–2000 IS NOT CLOSED BY EXT H ≈ 1830", 2.8, anchor="middle")

    # Callout bubbles in open areas
    bubble(s, X(NOSE) + 28, Y(CAB_ROOF_Z) - 16, "A")
    bubble(s, X(BED_REAR) - 16, Y(FLOOR_Z) - 22, "B")
    bubble(s, X(BED_FRONT + 900), Y(FLOOR_Z) + 22, "C")
    bubble(s, X(BED_REAR + 450), Y(FLOOR_Z) + 22, "D")

    s.dim_h(X(NOSE), X(BED_FRONT), Y(ROOF_Z) - 16, "OVER-CAB ≈ 1223 mm", Y(ROOF_Z))
    s.dim_v(Y(ROOF_Z), Y(CAB_ROOF_Z), X(NOSE) - 16, "LOFT ≈ 700 mm", X(NOSE), side="left")
    s.dim_v(Y(ROOF_Z), Y(FLOOR_Z), X(REAR_X) + 20, "SHELL EXT H ≈ 1830 mm", X(REAR_X), side="right")
    s.dim_v(Y(ROOF_Z), GY, X(REAR_X) + 50, "H TARGET ≤ 2500 mm", X(REAR_X), side="right")

    rows = [
        (X(BED_FRONT), X(BED_REAR), "BED L 2647 mm", Y(FLOOR_Z)),
        (X(BED_REAR), X(REAR_X), "TAIL EXT +1000 mm", Y(FLOOR_Z)),
        (X(REAR_AXLE), X(REAR_X), "REAR PAST AXLE ≈ 2015 mm", GY),
        (X(BED_FRONT), X(REAR_X), "SHELL FLOOR L = 3647 mm", Y(FLOOR_Z)),
    ]
    stack_dims_below(s, rows, GY + 16, 18)

    s.text(36, 456, "A  CAB–OVER-CAB JOINT — REVERSE LAP OR GASKET — SEE D-03.    B  BED–TAIL SILL — SEAL, WEEP, SPLASH BOX — SEE D-03.", 2.65)
    s.text(36, 468, "C  BOLTED OUTRIGGER TO BED RAIL — SEE D-01.    D  LANDING LEG UNDER THE +1000 TAIL — SEE D-02.  OCCUPIED ONLY ON STANDS.", 2.65)
    s.text(36, 480, "PANEL BUILD-UP IS EXAGGERATED.  GAUGE, SEALANT, AND BOLT GRADE ARE TBD.  THIS SHEET HAS ONE LENGTH DATUM SET — NO SECOND OAL.", 2.65)
    s.text(36, 492, "CAB OUTLINE IS DASHED (NOT IN SHELL SCOPE).  HATCH IS A CUT SYMBOL, NOT A MATERIAL SPEC.", 2.65)
    return finish(s)


# ---------------------------------------------------------------------------
# Detail-sheet helpers
# ---------------------------------------------------------------------------

def frame(sheet: Sheet, x, y, w, h, title: str):
    sheet.rect(x, y, w, h, fill="#ffffff", stroke="#141414", sw=0.45)
    sheet.rect(x, y, w, 8, fill="#141414", stroke="none")
    sheet.text(x + 2.5, y + 5.7, title, 3.0, fill="#ffffff", weight="bold")


def table(sheet: Sheet, x, y, col_ws, rows, row_h=13.5, size=2.55):
    width = sum(col_ws)
    height = row_h * len(rows)
    sheet.rect(x, y, width, row_h, fill="#e6e6e6", stroke="none")
    sheet.rect(x, y, width, height, fill="none", stroke="#141414", sw=0.35)
    xx = x
    for cw in col_ws[:-1]:
        xx += cw
        sheet.line(xx, y, xx, y + height, sw=0.22)
    for i in range(1, len(rows)):
        sheet.line(x, y + i * row_h, x + width, y + i * row_h, sw=0.22)
    for i, row in enumerate(rows):
        baseline = y + i * row_h + row_h / 2 + 0.34 * size
        cx = x
        for cw, cell in zip(col_ws, row):
            weight = "bold" if i == 0 else "normal"
            tw = sheet.text_width(cell, size, weight)
            if tw > cw - 3.2:
                raise SystemExit(f"{sheet.sid}: cell overflow '{cell}' {tw:.1f} > {cw - 3.2:.1f}")
            sheet.text(cx + 1.8, baseline, cell, size, weight=weight)
            cx += cw


def callout_boxes(sheet: Sheet, y, h, blocks: list[tuple[str, list[str]]]):
    gap = 6
    x = 16
    w = (809 - gap * (len(blocks) - 1)) / len(blocks)
    for title, lines in blocks:
        sheet.rect(x, y, w, h, fill="#ffffff", stroke="#141414", sw=0.4)
        sheet.text(x + 3, y + 8, title, 3.15, weight="bold")
        yy = y + 16
        for ln in lines:
            sheet.text(x + 3, yy, ln, 2.55)
            yy += 4.7
        if yy > y + h - 1:
            raise SystemExit(f"{sheet.sid}: callout overflow in {title}")
        x += w + gap


def fillet(sheet: Sheet, x, y):
    """ISO-style fillet symbol. Size is not given."""
    sheet.line(x, y, x + 22, y, sw=0.35, layer="dim")
    sheet.polygon([(x + 6, y), (x + 14, y), (x + 10, y + 5)], fill="#141414", stroke="none")
    sheet.line(x + 10, y, x + 10, y + 14, sw=0.28, layer="dim")
    sheet.arrow_v(x + 10, y + 14, 1)


# ---------------------------------------------------------------------------
# D-01 Outriggers
# ---------------------------------------------------------------------------

def sheet_d01() -> Sheet:
    s = Sheet("D-01", "BOLTED OUTRIGGERS TO BED RAILS — SHELL MODULE", "NTS — DO NOT SCALE", 9)
    frame(s, 16, 16, 500, 250, "1  PLAN — OUTRIGGERS ON BED RAILS (NTS, DO NOT SCALE)")

    # Schematic plan inside the frame
    shell = (40, 40, 420, 150)
    s.rect(*shell, fill="none", stroke="#141414", sw=0.55)
    bed_w_draw = 420 * BED_L / SHELL_L
    s.rect(40, 40 + 16, bed_w_draw, 150 - 32, fill="none", stroke="#141414", sw=0.35, dash="2.2 1.3")
    # Chassis rails
    s.rect(40, 78, bed_w_draw, 8, fill="#c5d4e4", stroke="#0b4f8a", sw=0.45)
    s.rect(40, 144, bed_w_draw, 8, fill="#c5d4e4", stroke="#0b4f8a", sw=0.45)
    # Shell-module longitudes (welded). Outboard of the rails.
    s.line(40, 52, 460, 52, sw=0.45)
    s.line(40, 178, 460, 178, sw=0.45)
    # Crossmembers — five bays, last one in the tail
    hatch_defs(s)
    s.rect(40 + bed_w_draw, 40, 420 - bed_w_draw, 150, fill="url(#hatch)", stroke="none")
    for cx in (80, 150, 220, 290, 335):
        s.line(cx, 52, cx, 178, sw=0.4)
        s.circle(cx, 82, 2.1, fill="#ffffff", stroke="#141414", sw=0.35)
        s.circle(cx, 148, 2.1, fill="#ffffff", stroke="#141414", sw=0.35)
    tail_mid = 40 + bed_w_draw + (420 - bed_w_draw) / 2
    s.text(tail_mid, 118, "TAIL +1000", 2.8, anchor="middle", weight="bold")
    s.text(tail_mid, 130, "CANTILEVER", 2.6, anchor="middle")

    fillet(s, 200, 32)
    s.text(228, 34, "FILLET — MODULE ONLY — SIZE TBD", 2.45)

    s.text(48, 196, "BLUE = BED RAILS.  BOLTS ONLY.  DO NOT WELD TO THE RAIL.", 2.6)
    s.text(48, 208, "BLACK LONGITUDES AND CROSSMEMBERS = SHELL-MODULE WELDMENT.", 2.6)
    s.text(48, 220, "OPEN CIRCLES = HOLES H1.  NO UNDIRECTED RAIL DRILL.", 2.6)
    s.text(48, 244, "SHELL FLOOR 3647 × 1911 SITS ON THESE OUTRIGGERS.  SEE S-02.", 2.7, weight="bold")

    frame(s, 528, 16, 297, 250, "2  SECTION — THROUGH-BOLT (NTS)")
    # Section sketch
    s.rect(560, 70, 180, 8, fill="#d9d9d9", stroke="#141414", sw=0.4)  # floor pan
    s.rect(600, 82, 100, 22, fill="#f4f4f4", stroke="#141414", sw=0.4)  # outrigger
    s.rect(600, 108, 100, 5, fill="#ffffff", stroke="#141414", sw=0.35)  # isolation
    s.rect(590, 116, 120, 28, fill="#c5d4e4", stroke="#0b4f8a", sw=0.45)  # rail
    s.rect(610, 148, 80, 8, fill="#d9d9d9", stroke="#141414", sw=0.4)  # backing plate
    s.line(648, 66, 648, 162, sw=0.7)  # bolt shank
    s.polygon([(640, 66), (656, 66), (656, 72), (640, 72)], fill="#141414", stroke="none")
    s.polygon([(642, 156), (654, 156), (654, 164), (642, 164)], fill="#141414", stroke="none")
    fillet(s, 700, 90)
    s.text(548, 186, "WELD SYMBOL POINTS AT THE", 2.55)
    s.text(548, 198, "SHELL-MODULE JOINT ONLY.", 2.55)
    s.text(548, 214, "GAP UNDER THE OUTRIGGER", 2.55)
    s.text(548, 226, "IS ISOLATION. NO WELD TO RAIL.", 2.55)
    s.text(548, 242, "BOLT GRADE / Ø / PLATE: TBD.", 2.55, weight="bold")

    s.text(16, 278, "NO UNDIRECTED RAIL DRILL", 4.2, weight="bold", fill="#9b1c1c")
    s.text(230, 278, "HOLE SCHEDULE — EVERY VALUE BELOW IS A PLACEHOLDER UNTIL JAY GO", 3.0, weight="bold")

    cols = [28, 175, 55, 50, 70, 80, 175, 176]
    rows = [
        ["ID", "WHERE", "Ø mm", "QTY", "GRADE", "SPACING", "RAIL DRILL", "RELEASE"],
        ["H1", "Outrigger to bed rail", "TBD", "TBD", "TBD", "TBD", "PROHIBITED UNTIL GO", "JAY GO BOX"],
        ["H2", "Backing plate", "TBD", "TBD", "TBD", "TBD", "PROHIBITED UNTIL GO", "JAY GO BOX"],
        ["H3", "Shell-module weldment jig", "TBD", "TBD", "—", "TBD", "NOT A RAIL HOLE", "SHOP JIG ONLY"],
        ["H4", "Leg pin — see D-02", "TBD", "TBD", "TBD", "TBD", "NOT A RAIL HOLE", "WITH D-02"],
    ]
    table(s, 16, 290, cols, rows, row_h=14, size=2.5)

    s.rect(16, 368, 200, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.6)
    s.checkbox(24, 376, 8, layer="draw")
    s.text(38, 382, "JAY GO — RAIL DRILL RELEASED", 2.9, weight="bold")
    s.text(230, 386, "NAME ____________________    DATE ____________    UNTIL SIGNED, DO NOT DRILL THE RAIL.", 2.8)

    callout_boxes(
        s,
        404,
        96,
        [
            (
                "ENG — LOAD PATH",
                [
                    "Bolted outriggers to bed rails.",
                    "Do not hang the shell on GI skin.",
                    "Through-bolts + backing plates.",
                    "Isolate dissimilar metals.",
                    "Floor pan lands on outriggers.",
                    "Welds stay inside the shell module.",
                    "Plate size, grade, spacing: TBD.",
                    "No undirected rail drill.",
                ],
            ),
            (
                "FIELD IoT — SPLASH / GLANDS",
                [
                    "Seal every penetration.",
                    "No gland in the splash plane",
                    "of the rail joint.",
                    "FAIL-IF wet gland at the bolts.",
                    "Any loom sits above the weep.",
                    "Do not pocket water on the plate.",
                    "Hose test of this joint: D-03.",
                    "Prototype only.",
                ],
            ),
            (
                "FSD — SHOP DECISION",
                [
                    "FSD = fabricator shop decision.",
                    "Do not drill until the Jay GO",
                    "box on this sheet is signed.",
                    "Do not invent a bolt grade.",
                    "Confirm the rail section",
                    "as-found before any pattern.",
                    "H3 jig holes are not rail holes.",
                    "Unsigned box = NO-GO cut / drill.",
                ],
            ),
        ],
    )
    return finish(s)


# ---------------------------------------------------------------------------
# D-02 Landing legs
# ---------------------------------------------------------------------------

def sheet_d02() -> Sheet:
    s = Sheet("D-02", "LANDING LEGS UNDER +1000 TAIL — BLANK kg PLACARD", "NTS — DO NOT SCALE", 10)
    frame(s, 16, 16, 460, 268, "1  TAIL +1000 — LEG STOWED AND DEPLOYED (NTS)")

    # Ground and tail sill
    s.line(40, 230, 450, 230, sw=0.45)
    s.rect(70, 150, 250, 10, fill="url(#hatch)", stroke="#141414", sw=0.35)
    hatch_defs(s)
    s.line(70, 150, 70, 230, sw=0.3, dash="2 1.3")  # bed rear / rail end
    s.text(74, 142, "BED REAR", 2.5)
    s.text(200, 142, "TAIL +1000", 2.7, weight="bold")
    # Wheel schematic at the rail end
    s.circle(120, 200, 28, fill="#1a1a1a", stroke="#141414", sw=0.4)
    s.circle(120, 200, 11, fill="#d0d0d0", stroke="#141414", sw=0.3)
    # Deployed leg
    s.line(300, 160, 300, 228, sw=0.9)
    s.rect(284, 226, 32, 6, fill="#141414", stroke="none")  # foot
    # Stowed leg (swung)
    s.line(250, 160, 340, 175, sw=0.45, dash="2.4 1.4")
    s.polyline([(250, 160), (300, 160), (340, 188), (300, 228)], sw=0.3, dash="1.5 1.2", layer="dim")
    s.text(360, 164, "STOWED", 2.6)
    s.text(360, 208, "DEPLOYED", 2.6)
    s.text(40, 250, "SWING ARC AND WHEEL CLEARANCE: TBD — AS-FOUND.  DO NOT SCALE THIS VIEW.", 2.55)
    s.text(150, 118, "OCCUPIED ONLY ON STANDS", 3.3, weight="bold", fill="#9b1c1c")

    frame(s, 488, 16, 337, 150, "2  FOOT PAD (NTS)")
    s.rect(620, 70, 70, 10, fill="#d9d9d9", stroke="#141414", sw=0.4)
    s.line(655, 40, 655, 70, sw=0.8)
    s.circle(640, 75, 1.6, fill="none", stroke="#141414", sw=0.3)
    s.circle(670, 75, 1.6, fill="none", stroke="#141414", sw=0.3)
    s.text(508, 48, "PAD L × W × t = TBD × TBD × TBD", 2.7, weight="bold")
    s.text(508, 64, "PIN / BOLT Ø AND QTY = TBD", 2.7)
    s.text(508, 110, "Holes in the pad are shell-module", 2.55)
    s.text(508, 122, "or pad holes. They are not a rail drill.", 2.55)
    s.text(508, 140, "Grade: TBD.  Jay GO still governs D-01.", 2.55)

    frame(s, 488, 174, 337, 110, "3  MAX-kg PLACARD — LEAVE BLANK")
    s.rect(508, 196, 180, 76, fill="#ffffff", stroke="#141414", sw=0.6)
    s.text(598, 210, "KE-Texh / TAMARAW", 2.6, anchor="middle", weight="bold")
    s.text(598, 226, "MAX kg", 4.0, anchor="middle", weight="bold")
    s.line(540, 240, 656, 240, sw=0.4)
    s.text(598, 254, "POST-WEIGH ONLY", 2.6, anchor="middle")
    s.text(598, 266, "DO NOT WRITE A NUMBER", 2.5, anchor="middle", fill="#9b1c1c")
    s.text(700, 210, "Affix inside", 2.5)
    s.text(700, 222, "the entry and", 2.5)
    s.text(700, 234, "on the build", 2.5)
    s.text(700, 246, "plate after", 2.5)
    s.text(700, 258, "axle-scale", 2.5)
    s.text(700, 270, "weigh.", 2.5)

    s.rect(16, 294, 300, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.6)
    s.checkbox(24, 302, 8, layer="draw")
    s.text(38, 308, "JAY GO — NO RAIL DRILL ON THIS SHEET", 2.7, weight="bold")
    s.text(330, 308, "Rail drill stays NO-GO until the D-01 Jay GO box is signed.", 2.7)

    callout_boxes(
        s,
        332,
        168,
        [
            (
                "ENG — LEGS",
                [
                    "Hard points under the +1000 tail.",
                    "Foot pad size: TBD.",
                    "Swing / ground / tire clearance: TBD.",
                    "Leg takes occupied overhang off",
                    "the rear suspension when static.",
                    "Do not size the leg from a guessed kg.",
                    "Pin holes: shell module, not the rail.",
                    "Stowed leg must clear the wheel arc.",
                    "Occupied only on stands.",
                    "Prototype only.",
                ],
            ),
            (
                "FIELD IoT — STANDS / PLACARD",
                [
                    "Habitation load is on the stands",
                    "when the shell is occupied.",
                    "Placard stays blank in this pack.",
                    "No sensor, switch, or label may",
                    "imply a kg rating before weigh.",
                    "FAIL-IF a number is written early.",
                    "Weigh on axle scales, then letter.",
                    "GVW / axle / payload remaining",
                    "are filled only after that weigh.",
                    "Do not use a stock-payload guess.",
                ],
            ),
            (
                "FSD — SHOP DECISION",
                [
                    "FSD = fabricator shop decision.",
                    "Do not cut a pad from an assumed kg.",
                    "Do not drill the chassis rail to",
                    "mount the leg. See D-01.",
                    "Confirm swing clearance on",
                    "this vehicle before the pin pattern.",
                    "Blank placard is the correct state",
                    "of this revision.",
                    "Unsigned Jay GO = NO-GO.",
                    "As-found tape still governs.",
                ],
            ),
        ],
    )
    return finish(s)


# ---------------------------------------------------------------------------
# D-03 Hose / rain
# ---------------------------------------------------------------------------

def sheet_d03() -> Sheet:
    s = Sheet("D-03", "HOSE / RAIN JOINT — FAIL-IF", "NTS — DO NOT SCALE", 11)
    hatch_defs(s)
    frame(s, 16, 16, 400, 200, "1  BED–TAIL SILL (NTS)")
    # Two floor ends, seal, weep, splash box
    s.rect(40, 70, 140, 12, fill="url(#hatch)", stroke="#141414", sw=0.35)
    s.rect(200, 70, 160, 12, fill="url(#hatch)", stroke="#141414", sw=0.35)
    s.rect(178, 74, 24, 8, fill="#ffffff", stroke="#141414", sw=0.4)  # seal
    s.text(190, 64, "SEAL TBD", 2.6, anchor="middle")
    # weep sloping outboard
    s.line(250, 82, 300, 110, sw=0.45)
    s.polygon([(300, 110), (294, 106), (296, 114)], fill="#141414", stroke="none")
    s.text(306, 114, "WEEP — DAYLIGHT", 2.6)
    # splash box
    s.polygon([(150, 110), (250, 110), (240, 150), (160, 150)], fill="none", stroke="#141414", sw=0.45)
    s.line(200, 150, 200, 168, sw=0.45)
    s.polygon([(200, 172), (196, 164), (204, 164)], fill="#141414", stroke="none")
    s.text(210, 160, "SPLASH BOX", 2.6)
    s.text(210, 172, "DRAINS OUTBOARD", 2.6)
    s.text(40, 196, "NO BLIND POCKET.  NO INWARD WEEP.", 2.7, weight="bold")

    frame(s, 428, 16, 397, 200, "2  CAB ROOF TO OVER-CAB (NTS)")
    s.rect(460, 110, 150, 10, fill="#efefef", stroke="#141414", sw=0.4)  # cab roof
    s.rect(500, 78, 180, 10, fill="url(#hatch)", stroke="#141414", sw=0.35)  # loft floor reverse lap
    s.rect(590, 90, 16, 20, fill="#ffffff", stroke="#141414", sw=0.4)  # gasket
    s.text(470, 68, "LOFT FLOOR — REVERSE LAP", 2.6)
    s.text(470, 140, "CAB ROOF — NOT SHELL SCOPE", 2.6)
    s.text(620, 128, "GASKET", 2.6)
    s.text(620, 140, "OR LAP", 2.6)
    s.text(620, 152, "TBD", 2.6)
    s.text(448, 176, "NO BLIND POCKET AT THIS JOINT.", 2.7, weight="bold")
    s.text(448, 190, "Water leaves to the outside of the cab.", 2.55)

    frame(s, 16, 224, 500, 150, "3  HOSE TEST — 10 min EACH JOINT (NTS)")
    # Tiny elevation: shell block + hose
    s.rect(40, 270, 200, 50, fill="#fbfbfb", stroke="#141414", sw=0.45)
    s.line(40, 300, 240, 300, sw=0.3, dash="2 1.2")
    s.polyline([(250, 250), (230, 268), (210, 290)], sw=0.45, layer="dim")
    s.text(252, 254, "SHOP HOSE", 2.6)
    s.text(252, 266, "10 min", 2.7, weight="bold")
    s.text(252, 278, "PRESSURE TBD", 2.6)
    s.text(40, 340, "AIM AT THE EXTENSION JOINT, THEN AT THE CAB / OVER-CAB JOINT.", 2.6)
    s.text(40, 354, "INSPECT: CABIN DRY  ·  NO POOLED WATER IN THE SILL OR SPLASH BOX  ·  GLANDS DRY.", 2.55)

    # FAIL-IF stamps
    fail_x = 530
    for i, label in enumerate(("FAIL-IF WET CABIN", "FAIL-IF TRAPPED WATER", "FAIL-IF WET GLANDS")):
        yy = 232 + i * 46
        s.rect(fail_x, yy, 280, 38, fill="#ffffff", stroke="#9b1c1c", sw=0.8)
        s.text(fail_x + 140, yy + 16, label, 3.4, anchor="middle", weight="bold", fill="#9b1c1c")
        s.text(fail_x + 140, yy + 30, "STOP · DO NOT CLOSE THE JOINT", 2.4, anchor="middle", fill="#9b1c1c")

    callout_boxes(
        s,
        384,
        116,
        [
            (
                "ENG — JOINTS",
                [
                    "Bed–tail sill: seal + outward weep",
                    "+ splash box. Sealant product TBD.",
                    "Cab–over-cab: reverse lap or gasket.",
                    "No blind pocket. Weep must daylight.",
                    "Do not drain into the loft.",
                    "Glands are not a drain path.",
                ],
            ),
            (
                "FIELD IoT — HOSE / GLANDS",
                [
                    "10 min hose at the extension joint.",
                    "10 min hose at the cab / over-cab joint.",
                    "FAIL-IF wet cabin.",
                    "FAIL-IF trapped water.",
                    "FAIL-IF wet glands.",
                    "Splash box drains; it is not a sensor pocket.",
                ],
            ),
            (
                "FSD — SHOP DECISION",
                [
                    "FSD = fabricator shop decision.",
                    "Sign the hose test before close-up.",
                    "No interior fit-out on a wet joint.",
                    "Pressure is TBD — do not invent one.",
                    "This is not an LTO rain approval.",
                    "Prototype only. Jay GO still on D-01.",
                ],
            ),
        ],
    )
    return finish(s)


# ---------------------------------------------------------------------------
# A-05 Assembly
# ---------------------------------------------------------------------------

def sheet_a05() -> Sheet:
    s = Sheet("A-05", "PANEL ASSEMBLY P1–P8 — EXPLODED, SHELL ONLY", "SCALE 1:15", 15)
    k = 1.0 / 15.0
    # Exploded side: loft, then living wall, gaps are explosion gaps.
    roof_x = 36
    roof_l = ENVELOPE_L * k
    s.polygon(
        [(roof_x, 48), (roof_x + roof_l, 48), (roof_x + roof_l + 8, 62), (roof_x + 8, 62)],
        fill="#f4f4f4",
        stroke="#141414",
        sw=0.45,
    )
    s.line(roof_x + roof_l / 2, 48, roof_x + roof_l / 2, 28, sw=0.28, layer="dim")
    s.text(roof_x + roof_l / 2, 24, "P6 ROOF — CONTINUOUS — OAH ≤ 2500", 3.0, anchor="middle", weight="bold")

    # P4 loft box
    p4x, p4y = 36, 78
    p4w, p4h = OVERCAB * k, LOFT * k
    s.polygon(
        [(p4x, p4y), (p4x + p4w, p4y), (p4x + p4w, p4y + p4h), (p4x + 6, p4y + p4h), (p4x, p4y + p4h - 8)],
        fill="#fbfbfb",
        stroke="#141414",
        sw=0.45,
    )
    s.rect(p4x + 14, p4y + 10, 36, 18, fill="#ffffff", stroke="#141414", sw=0.35)
    s.text(p4x + p4w / 2, p4y + p4h + 12, "P4 OVER-CAB ≈ 1223", 2.8, anchor="middle", weight="bold")

    # P2 side wall
    p2x = p4x + p4w + 18
    p2y = 78
    p2w = SHELL_L * k
    p2h = EXT_H * k
    s.rect(p2x, p2y, p2w, p2h, fill="#fbfbfb", stroke="#141414", sw=0.55)
    # openings to the same field-locate sizes
    s.rect(p2x + 80 * k, p2y + (ROOF_Z - (DOOR[1] + DOOR[3])) * k, DOOR[2] * k, DOOR[3] * k, fill="#ffffff", stroke="#141414", sw=0.35, dash="2 1.2")
    for win in (WIN1, WIN2):
        s.rect(
            p2x + (win[0] - BED_FRONT) * k,
            p2y + (ROOF_Z - (win[1] + win[3])) * k,
            win[2] * k,
            win[3] * k,
            fill="#ffffff",
            stroke="#141414",
            sw=0.35,
        )
    s.text(p2x + 4, p2y + p2h + 12, "P2 SIDE WALL LH — L 3647 · H ≈ 1830", 2.8, weight="bold")

    # P3 edge
    s.rect(p2x, 64, p2w, 8, fill="#ececec", stroke="#141414", sw=0.35)
    s.text(p2x + p2w + 4, 70, "P3 RH EDGE", 2.6)

    # P5 rear, exploded aft
    p5x = p2x + p2w + 24
    s.rect(p5x, p2y, 12, p2h, fill="#f4f4f4", stroke="#141414", sw=0.45)
    s.text(p5x + 16, p2y + 20, "P5", 3.0, weight="bold")
    s.text(p5x + 16, p2y + 32, "REAR", 2.6)
    s.text(p5x + 16, p2y + 44, "WALL", 2.6)

    # P1 floor
    s.rect(p2x, p2y + p2h + 28, p2w, 14, fill="#f4f4f4", stroke="#141414", sw=0.5)
    s.text(p2x, p2y + p2h + 54, "P1 FLOOR PAN  3647 × 1911  ON OUTRIGGERS — SEE D-01", 2.8, weight="bold")
    # rails under part of the floor
    s.rect(p2x, p2y + p2h + 64, BED_L * k, 6, fill="none", stroke="#0b4f8a", sw=0.7)
    s.text(p2x, p2y + p2h + 80, "BED RAILS 2647 — BOLTED — NOT A WELD TO THE CHASSIS", 2.6, fill="#0b4f8a")

    # Parts list
    frame(s, 520, 16, 305, 228, "PARTS — SHELL ONLY")
    parts = [
        "P1  Floor pan  3647 × 1911 on outriggers",
        "P2  Side wall LH  L 3647 · H ≈ 1830",
        "P3  Side wall RH  mirror of P2",
        "P4  Front / over-cab loft  ≈ 1223",
        "P5  Rear wall  vertical flat back",
        "P6  Roof  continuous  OAH ≤ 2500",
        "P7  Entry opening  700 × 1550 field locate",
        "P8  Windows  body ×2 + over-cab window",
        "Out of scope: interior, wet systems,",
        "electrics, solar, AC, awning (Phase-2).",
    ]
    yy = 36
    for ln in parts:
        s.text(530, yy, ln, 2.7)
        yy += 12
    s.text(530, 210, "Mount / weep / hatch / ladder:", 2.7, weight="bold")
    s.text(530, 222, "D-01…D-06.  Not an interior.", 2.7)

    frame(s, 520, 252, 305, 140, "OPENINGS — FIELD LOCATE")
    s.rect(540, 276, 28, 70, fill="none", stroke="#141414", sw=0.4, dash="2 1.2")
    s.text(576, 300, "P7 ENTRY", 2.7, weight="bold")
    s.text(576, 312, "700 × 1550", 2.6)
    s.text(576, 324, "behind cab", 2.6)
    s.rect(540, 356, 40, 22, fill="none", stroke="#141414", sw=0.35)
    s.rect(588, 356, 40, 22, fill="none", stroke="#141414", sw=0.35)
    s.rect(636, 360, 30, 16, fill="none", stroke="#141414", sw=0.35)
    s.text(674, 372, "P8", 2.7, weight="bold")
    s.text(530, 408, "Body windows schematic 780 × 520, plus over-cab window. Field locate.", 2.5)

    s.text(24, 470, "EXPLOSION GAPS ARE NOT VEHICLE DIMENSIONS.  CUT LENGTHS ARE THE SoR FIGURES ON S-01 / S-02 / I-00.", 2.7)
    s.text(24, 484, "OPTIONAL FRONT-FACE OPENING IS NOT MANDATORY.  PHASE-2 ROOF GEAR IS DASHED ON S-07 ONLY.", 2.7)
    s.text(24, 498, "NO INTERIOR FIT-OUT ON THIS SHEET.", 2.7, weight="bold")
    return finish(s)


def fail_box(sheet: Sheet, x, y, w, h, line1: str, line2: str):
    sheet.rect(x, y, w, h, fill="#ffffff", stroke="#9b1c1c", sw=0.7)
    sheet.text(x + w / 2, y + 12, line1, 2.9, anchor="middle", weight="bold", fill="#9b1c1c")
    sheet.text(x + w / 2, y + 24, line2, 2.35, anchor="middle", fill="#9b1c1c")


# ---------------------------------------------------------------------------
# S-06 Rear intent — not a replacement for the S-04 flat wall
# ---------------------------------------------------------------------------

def sheet_s06() -> Sheet:
    s = Sheet("S-06", "REAR ELEVATION — INTENT OPENINGS UNDER +1000", "SCALE 1:10", 7)
    left = 400.0
    right = left + SHELL_W * S
    cx = (left + right) / 2.0
    ground = 430.0
    roof = ground - OAH * S
    floor = ground - FLOOR_Z * S

    s.line(left - 20, ground, right + 80, ground, sw=0.45)
    s.rect(left, roof, SHELL_W * S, EXT_H * S, fill="#fbfbfb", stroke="#141414", sw=0.7)

    # Intent openings — no cut size. Graphic placement only.
    s.rect(cx - 36, roof + 18, 72, 40, fill="#ffffff", stroke="#141414", sw=0.4)
    s.rect(cx - 32, floor - 58, 64, 36, fill="#ffffff", stroke="#141414", sw=0.4, dash="2.4 1.4")
    # Ladder on the left of the rear face, stand-off from the skin.
    s.line(left + 16, roof + 28, left + 16, floor - 16, sw=0.7)
    s.line(left + 30, roof + 28, left + 30, floor - 16, sw=0.7)
    for my in (roof + 55, floor - 40):
        s.rect(left + 10, my, 26, 8, fill="#ffffff", stroke="#141414", sw=0.4)
    # Lamps — glands, not a cut size.
    s.rect(left + 6, floor - 18, 14, 10, fill="#1a1a1a", stroke="#141414", sw=0.3)
    s.rect(right - 20, floor - 18, 14, 10, fill="#1a1a1a", stroke="#141414", sw=0.3)
    # Bumper bar under the shell. Height is not a cut dimension.
    s.rect(left + 8, floor + 22, SHELL_W * S - 16, 12, fill="#4a4a4a", stroke="#141414", sw=0.4)

    for sign in (-1, 1):
        draw_end_tire(s, cx + sign * (TREAD * S) / 2.0, ground)

    s.dim_h(left, right, roof - 16, "SHELL W = 1911 mm", roof)
    s.dim_v(roof, floor, right + 18, "SHELL EXT H ≈ 1830 mm", right, side="right")
    s.dim_v(roof, ground, right + 48, "H TARGET ≤ 2500 mm", right, side="right")
    s.dim_h(cx - TREAD * S / 2, cx + TREAD * S / 2, ground + 20, "TREAD R 1510 mm REF", ground)

    s.text(24, 36, "RENDER INTENT — NOT CUT GEOMETRY", 3.2, weight="bold")
    s.text(24, 52, "S-04 stays the flat structural rear.", 2.7)
    s.text(24, 68, "Window and lower hatch: size TBD.", 2.7)
    s.text(24, 84, "Field locate. Not a cut freeze.", 2.7)
    s.text(24, 104, "Ladder mounts → D-05.", 2.7)
    s.text(24, 116, "Roof access. Not a shell lift.", 2.7)
    s.text(24, 136, "Lamps, bumper, weep → D-06.", 2.7)
    s.text(24, 148, "Hitch must clear the leg swing.", 2.7)
    s.text(24, 168, "This face is the +1000 tail.", 2.7)
    s.text(24, 180, "OAH ≤ 2500 = hatch closed.", 2.7, weight="bold")

    s.text(cx, roof + 72, "REAR WINDOW — INTENT", 2.5, anchor="middle")
    s.text(cx, floor - 72, "LOWER HATCH — SIZE TBD", 2.5, anchor="middle")
    s.line(left + 16, roof + 55, left - 8, roof + 55, sw=0.25, layer="dim")
    s.text(left - 12, roof + 53, "LADDER — D-05", 2.5, anchor="end")
    s.text(left - 8, floor + 30, "BUMPER — D-06", 2.4, anchor="end")
    return finish(s)


# ---------------------------------------------------------------------------
# S-07 Roof plan — intent cutout; Phase-2 gear dashed only
# ---------------------------------------------------------------------------

def sheet_s07() -> Sheet:
    s = Sheet("S-07", "ROOF PLAN — LOUNGE CUTOUT AND PHASE-2 HOOKS", "SCALE 1:10", 8)
    nose_x = 150.0
    bed_x = nose_x + OVERCAB * S
    rear_x = bed_x + SHELL_L * S
    top = 70.0
    bot = top + SHELL_W * S
    bed_rear_x = bed_x + BED_L * S

    s.rect(nose_x, top, OVERCAB * S, SHELL_W * S, fill="#f7f7f7", stroke="#141414", sw=0.55, dash="3 1.6")
    s.rect(bed_x, top, SHELL_L * S, SHELL_W * S, fill="#ffffff", stroke="#141414", sw=0.7)

    # Lounge cutout inside the over-cab. Size is not dimensioned.
    cut_x, cut_y, cut_w, cut_h = nose_x + 16, top + 28, 90, 130
    s.rect(cut_x, cut_y, cut_w, cut_h, fill="#ffffff", stroke="#141414", sw=0.55)
    s.line(cut_x, cut_y, cut_x, cut_y + cut_h, sw=1.15)
    # Dashed seats and table — intent only.
    s.rect(cut_x + 8, cut_y + 10, 22, 28, fill="none", stroke="#141414", sw=0.3, dash="1.6 1.2")
    s.rect(cut_x + 8, cut_y + cut_h - 38, 22, 28, fill="none", stroke="#141414", sw=0.3, dash="1.6 1.2")
    s.rect(cut_x + 40, cut_y + 50, 28, 22, fill="none", stroke="#141414", sw=0.3, dash="1.6 1.2")

    # Roof-rail mount ticks into the sills, not the skin.
    for rx in (bed_x + 40, bed_x + 140, bed_rear_x + 30):
        s.rect(rx, top + 6, 8, 8, fill="#ffffff", stroke="#141414", sw=0.35)
        s.rect(rx, bot - 14, 8, 8, fill="#ffffff", stroke="#141414", sw=0.35)

    # Phase-2 hooks — dashed, not a cut list.
    s.rect(bed_x + 24, top + 36, 150, 78, fill="none", stroke="#141414", sw=0.4, dash="2.4 1.4")
    s.rect(bed_x + 190, top + 40, 40, 28, fill="none", stroke="#141414", sw=0.4, dash="2.2 1.3")
    s.rect(bed_x + 24, bot - 28, 180, 10, fill="none", stroke="#141414", sw=0.35, dash="2 1.2")

    s.text(nose_x + 8, top - 16, "HINGE — OPENS FORWARD / UP", 2.7, weight="bold")
    s.text(cut_x + 6, cut_y - 16, "LOUNGE CUTOUT", 2.4, weight="bold")
    s.text(cut_x + 6, cut_y - 6, "SIZE TBD — D-04", 2.2)
    s.text(cut_x + 4, cut_y + cut_h + 14, "SEATS / TABLE — INTENT ONLY", 2.2)
    s.text(bed_x + 36, top + 58, "SOLAR — PHASE-2", 2.6)
    s.text(bed_x + 36, top + 70, "DASHED — NOT BOM", 2.4)
    s.text(bed_x + 196, top + 78, "AC P2", 2.4)
    s.text(bed_x + 36, bot - 34, "AWNING — PHASE-2 DASHED", 2.4)
    s.text(bed_rear_x + 16, top + 40, "TAIL +1000", 2.7, weight="bold")
    s.text(bed_rear_x + 16, top + 54, "SEE S-02", 2.4)
    s.text((bed_x + bed_rear_x) / 2, top + 24, "ROOF-RAIL MOUNTS → D-04", 2.5, anchor="middle")

    s.dim_h(nose_x, bed_x, bot + 28, "OVER-CAB ≈ 1223 mm", bot)
    s.dim_h(bed_x, rear_x, bot + 50, "SHELL FLOOR L = 3647 mm", bot)
    s.dim_h(bed_rear_x, rear_x, bot + 72, "TAIL EXT +1000 mm", bot)
    s.dim_v(top, bot, rear_x + 36, "SHELL W = 1911 mm", rear_x, side="right")

    s.text(24, 448, "CUTOUT, HATCH, AND RAILS ARE DESIGN INTENT. SIZES TBD. SEE D-04. NOT A CUT FREEZE.", 2.6)
    s.text(24, 462, "OAH ≤ 2500 IS HATCH CLOSED. OPEN HATCH AND OCCUPIED ROOF ARE PARKED ONLY.", 2.6, weight="bold")
    s.text(24, 476, "DASHED SOLAR / AC / AWNING ARE PHASE-2 HOOKS. NOT A CUT LIST. NOT A BOM. NOT FAB DONE.", 2.6)
    s.text(24, 490, "SEATS AND TABLE ARE INTENT ONLY. ENVELOPE DIMS MATCH DIMS.md. RENDERS ARE NOT FARM-READY.", 2.6)
    return finish(s)


# ---------------------------------------------------------------------------
# D-04 Hatch / lounge frame
# ---------------------------------------------------------------------------

def sheet_d04() -> Sheet:
    s = Sheet("D-04", "ROOF HATCH AND LOUNGE FRAME — SEALED TO STRUCTURE", "NTS — DO NOT SCALE", 12)
    hatch_defs(s)
    frame(s, 16, 16, 400, 248, "1  PLAN — FRAMED OPENING (NTS, SIZE TBD)")
    s.rect(70, 56, 250, 160, fill="none", stroke="#141414", sw=0.4)
    s.rect(100, 78, 180, 116, fill="#ffffff", stroke="#141414", sw=0.7)
    s.line(100, 78, 100, 194, sw=1.2)
    s.circle(118, 92, 3.2, fill="#ffffff", stroke="#141414", sw=0.4)
    s.circle(118, 180, 3.2, fill="#ffffff", stroke="#141414", sw=0.4)
    for px in (150, 210, 260):
        s.rect(px, 60, 10, 10, fill="#141414", stroke="none")
        s.rect(px, 202, 10, 10, fill="#141414", stroke="none")
    s.text(108, 48, "HINGE — FORWARD EDGE", 2.5, weight="bold")
    s.text(150, 130, "OPENING", 2.6, weight="bold")
    s.text(150, 142, "SIZE TBD", 2.4)
    s.text(210, 236, "RAIL POSTS INTO SILLS", 2.4)
    s.text(36, 248, "FRAME IS STRUCTURE. NOT A CUT IN THE SKIN ALONE.", 2.5, weight="bold")

    frame(s, 428, 16, 397, 248, "2  SECTION — HATCH CLOSED (NTS)")
    s.rect(470, 120, 220, 14, fill="url(#hatch)", stroke="#141414", sw=0.4)
    s.rect(560, 100, 90, 14, fill="#f4f4f4", stroke="#141414", sw=0.45)
    s.rect(548, 114, 12, 28, fill="#ffffff", stroke="#141414", sw=0.45)
    s.rect(640, 114, 12, 28, fill="#ffffff", stroke="#141414", sw=0.45)
    s.line(560, 96, 650, 70, sw=0.35, dash="2.2 1.3")
    s.text(470, 64, "DASHED LEAF = OPEN, PARKED ONLY", 2.5)
    s.text(470, 160, "CLOSED LEAF ON A FRAMED SILL", 2.55, weight="bold")
    s.text(470, 176, "CONTINUOUS SEAL — PRODUCT TBD", 2.5)
    s.text(470, 192, "HINGE AND STRUT LAND ON THE FRAME", 2.5)
    s.text(470, 208, "OAH ≤ 2500 = THIS CLOSED POSITION", 2.6, weight="bold")
    s.text(470, 228, "WELD SIZE TBD. NO SKIN-ONLY CUT.", 2.5)
    s.text(470, 244, "HOSE THE CLOSED PERIMETER BEFORE ANY LOUNGE CLAIM.", 2.45)

    fail_box(s, 16, 274, 250, 36, "ENG FAIL-IF", "OPEN CUT WITHOUT A SEALED FRAME")
    fail_box(s, 276, 274, 270, 36, "FIELD FAIL-IF", "NO SEAL · NO RAIL · WATER IN LOUNGE")
    fail_box(s, 556, 274, 268, 36, "FIELD FAIL-IF", "HATCH OPEN ON THE ROAD")

    s.rect(16, 318, 250, 26, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(24, 324, 7, layer="draw")
    s.text(38, 330, "JAY GO — STILL NO RAIL DRILL", 2.6, weight="bold")
    s.text(280, 330, "OCCUPIED ROOF = PARKED ONLY.  HATCH CLOSED AND RAILS UP BEFORE DRIVE.", 2.55)

    callout_boxes(
        s,
        354,
        146,
        [
            (
                "ENG — FRAME",
                [
                    "Opening is a framed hole in the",
                    "shell structure, not a skin cut.",
                    "Continuous seal to that frame.",
                    "Hinge and strut hardpoints land",
                    "on the frame, not on the sheet.",
                    "Rail posts go into roof rails",
                    "or sills. Weld size TBD.",
                    "FAIL-IF an open cut has no",
                    "sealed hatch frame.",
                ],
            ),
            (
                "FIELD IoT — WATER / ROAD",
                [
                    "FAIL-IF open cut, no sealed hatch.",
                    "FAIL-IF the rail is missing.",
                    "FAIL-IF water enters the lounge.",
                    "FAIL-IF the hatch is open on road.",
                    "Hose the closed perimeter before",
                    "any parked-lounge claim.",
                    "Occupied roof is parked only.",
                    "OAH ≤ 2500 means hatch closed.",
                ],
            ),
            (
                "FSD — SHOP DECISION",
                [
                    "FSD = fabricator shop decision.",
                    "Do not cut the roof from a render.",
                    "Opening size stays TBD.",
                    "Sealant and weld size stay TBD.",
                    "Do not call the lounge done",
                    "while the hatch is unsealed.",
                    "Jay GO on D-01 still governs",
                    "any chassis-rail hole.",
                    "Prototype only. Not farm-ready.",
                ],
            ),
        ],
    )
    return finish(s)


# ---------------------------------------------------------------------------
# D-05 Ladder mounts
# ---------------------------------------------------------------------------

def sheet_d05() -> Sheet:
    s = Sheet("D-05", "WALL LADDER MOUNTS — ROOF ACCESS, NOT A LIFT", "NTS — DO NOT SCALE", 13)
    frame(s, 16, 16, 420, 250, "1  REAR POST — STAND-OFF MOUNTS (NTS)")
    s.rect(80, 48, 16, 190, fill="url(#hatch)", stroke="#141414", sw=0.4)
    hatch_defs(s)
    s.line(120, 70, 120, 210, sw=0.9)
    for my, tag in ((80, "L1"), (150, "L2"), (200, "L3")):
        s.rect(96, my, 24, 8, fill="#d9d9d9", stroke="#141414", sw=0.35)
        s.line(108, my + 4, 120, my + 4, sw=0.45)
        s.text(132, my + 6, tag, 2.6, weight="bold")
    s.text(160, 70, "LADDER RAIL", 2.6, weight="bold")
    s.text(160, 88, "STAND-OFF BLOCKS", 2.5)
    s.text(160, 104, "INTO THE POST / SILL", 2.5)
    s.text(160, 120, "NOT INTO THE SKIN ALONE", 2.5, weight="bold")
    s.text(40, 248, "ROOF ACCESS · NOT SHELL LIFT", 3.3, weight="bold", fill="#9b1c1c")

    frame(s, 448, 16, 377, 160, "2  MOUNT SCHEDULE — ALL TBD")
    cols = [40, 130, 50, 45, 90]
    rows = [
        ["ID", "LANDS IN", "Ø", "QTY", "GRADE"],
        ["L1", "Rear post / sill", "TBD", "TBD", "TBD"],
        ["L2", "Rear post / sill", "TBD", "TBD", "TBD"],
        ["L3", "Rear post / sill", "TBD", "TBD", "TBD"],
    ]
    table(s, 468, 40, cols, rows, row_h=16, size=2.5)
    s.text(468, 120, "SPACING TBD. CONFIRM ON THE POST.", 2.5)
    s.text(468, 136, "NOT A CHASSIS-RAIL DRILL.", 2.5, weight="bold")
    s.text(468, 156, "See D-01 before any rail hole.", 2.5)

    fail_box(s, 448, 186, 377, 36, "FAIL-IF LADDER USED AS A JACK OR LIFT", "IT IS ROOF ACCESS ONLY")
    fail_box(s, 448, 230, 377, 36, "FAIL-IF MOUNTS LOOSEN AFTER VIBRATION", "RE-TORQUE CHECK IS TBD")

    s.rect(16, 276, 280, 26, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(24, 282, 7, layer="draw")
    s.text(38, 288, "JAY GO — NO UNDIRECTED RAIL DRILL", 2.6, weight="bold")

    callout_boxes(
        s,
        312,
        188,
        [
            (
                "ENG — MOUNTS",
                [
                    "Bolts land in rear posts or sills.",
                    "Stand-offs. Not skin-only screws.",
                    "Grade, diameter, quantity, and",
                    "spacing are TBD on this sheet.",
                    "Do not invent a grade.",
                    "The ladder is roof access.",
                    "It is not a shell lift and not",
                    "a jack. Do not size it as one.",
                ],
            ),
            (
                "FIELD IoT — VIBRATION",
                [
                    "FAIL-IF the ladder is used to",
                    "lift or jack the shell.",
                    "FAIL-IF mounts are loose after",
                    "road vibration.",
                    "Check stand-offs still clamp",
                    "the post, not the outer skin.",
                    "No gland or cable on the ladder",
                    "rail unless it is sealed.",
                    "Prototype only.",
                ],
            ),
            (
                "FSD — SHOP DECISION",
                [
                    "FSD = fabricator shop decision.",
                    "Do not copy rung spacing off",
                    "the concept render.",
                    "Do not drill the chassis rail",
                    "to hang this ladder.",
                    "Confirm post section as-found.",
                    "Unsigned Jay GO = NO-GO.",
                    "Blank grade cells stay blank.",
                    "Not an LTO access approval.",
                ],
            ),
        ],
    )
    return finish(s)


# ---------------------------------------------------------------------------
# D-06 Bumper / splash under the tail
# ---------------------------------------------------------------------------

def sheet_d06() -> Sheet:
    s = Sheet("D-06", "REAR BUMPER AND SPLASH UNDER THE +1000 TAIL", "NTS — DO NOT SCALE", 14)
    hatch_defs(s)
    frame(s, 16, 16, 460, 230, "1  BUMPER–SHELL INTERFACE (NTS)")
    s.rect(50, 70, 200, 12, fill="url(#hatch)", stroke="#141414", sw=0.4)
    s.rect(70, 110, 250, 16, fill="#4a4a4a", stroke="#141414", sw=0.4)
    s.line(200, 82, 250, 110, sw=0.45)
    s.polygon([(250, 110), (244, 104), (246, 114)], fill="#141414", stroke="none")
    s.polygon([(160, 140), (280, 140), (268, 175), (172, 175)], fill="none", stroke="#141414", sw=0.4)
    s.line(220, 175, 220, 196, sw=0.4)
    s.text(60, 58, "SHELL SILL — +1000 TAIL", 2.6, weight="bold")
    s.text(80, 100, "WEEP OUT — KEEP D-03 PATH", 2.5)
    s.text(332, 122, "BUMPER BEAM", 2.6, weight="bold")
    s.text(290, 168, "BELLY SPLASH", 2.5)
    s.text(290, 182, "MUST DRAIN", 2.5)
    s.text(40, 220, "DO NOT CLOSE THE WEEP WITH THE BUMPER.", 2.6, weight="bold")

    frame(s, 488, 16, 337, 150, "2  HITCH vs LEG SWING (NTS)")
    s.circle(620, 90, 28, fill="none", stroke="#141414", sw=0.35, dash="2 1.3")
    s.rect(600, 78, 18, 36, fill="#ffffff", stroke="#141414", sw=0.4)
    s.text(508, 48, "LEG SWING — SEE D-02", 2.6, weight="bold")
    s.text(508, 64, "HITCH MUST CLEAR THAT ARC", 2.5)
    s.text(660, 88, "HITCH", 2.5)
    s.text(508, 130, "CLEARANCE IS TBD.", 2.5)
    s.text(508, 146, "DO NOT SCALE THIS VIEW.", 2.5)

    frame(s, 488, 174, 337, 72, "3  LAMP / MUDFLAP GLANDS")
    s.circle(530, 210, 8, fill="#1a1a1a", stroke="#141414", sw=0.35)
    s.circle(530, 210, 12, fill="none", stroke="#141414", sw=0.4)
    s.text(556, 200, "LAMP", 2.5, weight="bold")
    s.text(556, 214, "GLAND SEAL TBD", 2.4)
    s.text(556, 228, "MUDFLAP MOUNT SEALED", 2.4)

    fail_box(s, 16, 256, 390, 36, "FAIL-IF TRAPPED WATER UNDER THE OCCUPIED TAIL", "SPLASH AND WEEP MUST DAYLIGHT")
    fail_box(s, 416, 256, 408, 36, "FAIL-IF WET GLANDS AT THE BUMPER", "LAMP AND MUDFLAP PENETRATIONS")

    s.rect(16, 300, 300, 26, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(24, 306, 7, layer="draw")
    s.text(38, 312, "JAY GO — NO UNDIRECTED RAIL DRILL", 2.6, weight="bold")

    callout_boxes(
        s,
        336,
        164,
        [
            (
                "ENG — INTERFACE",
                [
                    "Bumper meets the shell sill",
                    "under the +1000 tail.",
                    "Keep the belly splash and the",
                    "D-03 weep. Do not dam them.",
                    "Hitch stays clear of the",
                    "landing-leg swing. Gap TBD.",
                    "No new departure angle is",
                    "stated. Confirm as-found.",
                ],
            ),
            (
                "FIELD IoT — SPLASH / GLANDS",
                [
                    "FAIL-IF water is trapped under",
                    "the occupied tail.",
                    "FAIL-IF lamp or mudflap glands",
                    "are wet at this interface.",
                    "Weep must still daylight after",
                    "the bumper is fitted.",
                    "Hose this joint with D-03.",
                    "Prototype only.",
                ],
            ),
            (
                "FSD — SHOP DECISION",
                [
                    "FSD = fabricator shop decision.",
                    "Do not copy the render bumper.",
                    "Do not state a departure angle.",
                    "Sealant and gland parts: TBD.",
                    "Do not drill the chassis rail",
                    "to hang the bumper.",
                    "Leg swing check is on the",
                    "vehicle, with D-02.",
                    "Unsigned Jay GO = NO-GO.",
                ],
            ),
        ],
    )
    return finish(s)


# ---------------------------------------------------------------------------
# I-00 Index
# ---------------------------------------------------------------------------

def sheet_index() -> Sheet:
    s = Sheet("I-00", "DRAWING INDEX, SoR, AND RELEASE STAMP", "—", 1)
    s.text(18, 26, "KE-Texh / TAMARAW  —  PHASE-1 SHELL  —  FABRICATOR DISCUSSION PACK", 4.6, weight="bold")
    s.text(18, 40, WM, 3.3, weight="bold", fill="#9b1c1c")

    # Stamp
    s.rect(16, 50, 400, 78, fill="#ffffff", stroke="#9b1c1c", sw=0.8)
    s.text(28, 68, "STAMP: CONDITIONAL — DISCUSS", 4.0, weight="bold", fill="#9b1c1c")
    s.text(28, 84, "NO-GO CUT STEEL UNTIL THE GATES BELOW ARE SIGNED", 3.0, weight="bold")
    s.text(28, 100, "PROTOTYPE ONLY  ·  RENDERS ≠ FARM-READY  ·  NOT LTO", 2.7)
    s.text(28, 116, "OAH ≤ 2500 = HATCH CLOSED.  NO SECOND OAL.", 2.7)

    s.rect(428, 50, 397, 78, fill="#ffffff", stroke="#141414", sw=0.45)
    s.text(440, 66, "CHASSIS", 2.8, weight="bold")
    s.text(440, 80, "TMP LWB dropside  ·  WB 3085", 2.7)
    s.text(440, 92, "Stock OAL × W × H  5300 × 1800 × 1800", 2.7)
    s.text(440, 104, "Bed 2647 × 1711  ·  tread 1510 / 1510", 2.7)
    s.text(440, 116, "Verify VIN and as-found tape before any cut.", 2.6)

    # Sheet index
    sheets = [
        ["SHEET", "TITLE", "SCALE"],
        ["I-00", "Index, SoR, release stamp", "—"],
        ["S-01", "Side elevation, LH", "1:10"],
        ["S-02", "Plan, expansion envelope", "1:10"],
        ["S-03", "Front elevation, over-cab nose", "1:10"],
        ["S-04", "Rear, vertical flat back", "1:10"],
        ["S-05", "Section A–A, over-cab + tail", "1:10"],
        ["S-06", "Rear intent: window, hatch, ladder", "1:10"],
        ["S-07", "Roof plan: lounge + Phase-2 dashed", "1:10"],
        ["D-01", "Bolted outriggers / rail drill", "NTS"],
        ["D-02", "Landing legs + blank kg placard", "NTS"],
        ["D-03", "Hose / rain joints, FAIL-IF", "NTS"],
        ["D-04", "Hatch + lounge frame, sealed", "NTS"],
        ["D-05", "Wall ladder mounts, not a lift", "NTS"],
        ["D-06", "Bumper, splash, hitch vs leg", "NTS"],
        ["A-05", "Panel assembly P1–P8", "1:15"],
    ]
    table(s, 16, 136, [52, 248, 48], sheets, row_h=9.8, size=2.25)

    sor = [
        ["DATUM", "mm", "STATUS"],
        ["Shell floor L × W", "3647 × 1911", "CUT"],
        ["OAL", "≈ 6300", "CUT"],
        ["OAH", "≤ 2500", "CUT"],
        ["Over-cab", "≈ 1223", "CUT"],
        ["Tail extension", "+1000", "CUT"],
        ["Side growth", "+100 / side", "CUT"],
        ["WB", "3085", "CHASSIS"],
        ["Bed L × W", "2647 × 1711", "CHASSIS"],
        ["Shell ext H", "≈ 1830", "ESTIMATE"],
        ["Loft", "≈ 700", "ESTIMATE"],
        ["Clear standing H", "1900–2000", "TARGET"],
        ["Rear past axle", "≈ 2015", "CALLOUT"],
        ["Over-cab + floor", "4870 sum", "NOT A NEW DATUM"],
    ]
    table(s, 380, 136, [120, 100, 150], sor, row_h=9.8, size=2.2)

    s.rect(16, 302, 809, 196, fill="#ffffff", stroke="#141414", sw=0.5)
    s.text(28, 316, "GATES — UNSIGNED  ·  NO-GO CUT UNTIL AS-FOUND + JAY GO + D-01…D-06", 3.0, weight="bold")
    gates = [
        (334, "AS-FOUND TAPE", "Bed, rails, cab roof, overhangs, VIN. Freeze on a shop traveler."),
        (354, "JAY GO RAIL DRILL", "D-01 signed. No undirected drill into the bed rail or chassis rail."),
        (374, "OUTRIGGERS + LEGS + kg", "D-01 and D-02. Placard stays blank until a post-weigh."),
        (394, "HOSE / RAIN", "D-03 at the extension joint. FAIL-IF wet cabin, trapped water, wet glands."),
        (414, "HATCH FRAME", "D-04. FAIL-IF open cut with no seal, no rail, water in lounge, hatch open on road."),
        (434, "LADDER", "D-05. Roof access only. FAIL-IF used as a lift, or mounts loosen."),
        (454, "BUMPER / SPLASH", "D-06. FAIL-IF trapped water under the tail, or wet glands at the bumper."),
        (474, "PROTOTYPE ONLY", "OAH ≤ 2500 means hatch closed. Renders are not farm-ready. Not LTO."),
    ]
    for gy, title, detail in gates:
        s.checkbox(28, gy - 6, 5.5, layer="draw")
        s.text(40, gy - 1, title, 2.55, weight="bold")
        s.text(168, gy - 1, detail, 2.35)
    s.text(28, 490, "CLEAR H 1900–2000 IS A TARGET. IT IS NOT CLOSED BY SHELL EXT H ≈ 1830.", 2.4, weight="bold")
    return finish(s)


def render(sheet: Sheet, svg_path: Path, png_path: Path):
    svg_path.write_text(sheet.to_svg(), encoding="utf-8")
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(png_path),
        output_width=3364,
        output_height=2376,
    )


def main():
    SHEETS_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)

    builders = [
        ("I-00_index", sheet_index),
        ("S-01_side_elevation", _sheet_s01_clean),
        ("S-02_plan", sheet_s02),
        ("S-03_front_elevation", sheet_s03),
        ("S-04_rear_elevation", sheet_s04),
        ("S-05_section", _sheet_s05_clean),
        ("S-06_rear_intent", sheet_s06),
        ("S-07_roof_plan", sheet_s07),
        ("D-01_outriggers", sheet_d01),
        ("D-02_landing_legs", sheet_d02),
        ("D-03_hose_rain", sheet_d03),
        ("D-04_hatch_lounge", sheet_d04),
        ("D-05_ladder_mounts", sheet_d05),
        ("D-06_bumper_splash", sheet_d06),
        ("A-05_shell_assembly", sheet_a05),
    ]
    # sheet_s01 and sheet_s05 call the clean versions; the wrappers exist only as names.
    banned = ("5942", "2342", "10.9", "8.8", "1025", "1110")
    failed = False
    for name, builder in builders:
        sheet = builder()
        errors = qa_sheet(sheet)
        svg = sheet.to_svg()
        text_blob = "\n".join(re.findall(r">([^<]*)</text>", svg))
        for token in banned:
            if token in text_blob:
                errors.append(f"banned token {token}")
        if WM not in svg:
            errors.append("missing watermark")
        if "JAY GO" not in svg:
            errors.append("missing Jay GO")
        if errors:
            failed = True
            print(f"\n== {sheet.sid} {len(errors)} QA issues ==")
            for e in errors[:40]:
                print(" -", e)
        else:
            print(f"{sheet.sid} QA clean ({len(sheet.texts)} texts, {len(sheet.segs)} segs)")
        render(sheet, SHEETS_DIR / f"{name}.svg", PREVIEWS / f"{name}.png")

    for name in (
        "I-00_index",
        "S-01_side_elevation",
        "S-02_plan",
        "S-05_section",
        "S-06_rear_intent",
        "S-07_roof_plan",
        "D-01_outriggers",
        "D-02_landing_legs",
        "D-03_hose_rain",
        "D-04_hatch_lounge",
        "D-05_ladder_mounts",
        "D-06_bumper_splash",
        "A-05_shell_assembly",
    ):
        shutil.copyfile(PREVIEWS / f"{name}.png", ARTIFACTS / f"{name}.png")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
