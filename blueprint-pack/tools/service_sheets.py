"""S-08, D-07, and D-08 — provisions only.

Generator and roof-AC units are not a buy list and not cut Done.
Bolt grade, kW, BTU, and max kg stay TBD.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sheetlib import Sheet  # noqa: E402

OVERCAB = 1223
SHELL_L = 3647
SHELL_W = 1911


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


def fail_box(sheet: Sheet, x, y, w, h, line1: str, line2: str):
    sheet.rect(x, y, w, h, fill="#ffffff", stroke="#9b1c1c", sw=0.7)
    sheet.text(x + w / 2, y + 12, line1, 2.7, anchor="middle", weight="bold", fill="#9b1c1c")
    sheet.text(x + w / 2, y + 24, line2, 2.3, anchor="middle", fill="#9b1c1c")


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


def hatch_defs(sheet: Sheet):
    sheet.defs.append(
        """
<pattern id="hatch" patternUnits="userSpaceOnUse" width="3.2" height="3.2" patternTransform="rotate(45)">
  <line x1="0" y1="0" x2="0" y2="3.2" stroke="#6a6a6a" stroke-width="0.25"/>
</pattern>
"""
    )


def finish(sheet: Sheet) -> Sheet:
    sheet.border()
    sheet.title_block()
    return sheet


def sheet_s08() -> Sheet:
    s = Sheet("S-08", "SERVICE PLAN — AC CURB AND GENERATOR BAY", "ROOF 1:10 · BAY NTS", 9)
    sc = 0.072
    nose_x = 28.0
    bed_x = nose_x + OVERCAB * sc
    rear_x = bed_x + SHELL_L * sc
    top = 48.0
    bot = top + SHELL_W * sc

    s.rect(nose_x, top, OVERCAB * sc, SHELL_W * sc, fill="#f7f7f7", stroke="#141414", sw=0.5, dash="3 1.6")
    s.rect(bed_x, top, SHELL_L * sc, SHELL_W * sc, fill="#ffffff", stroke="#141414", sw=0.65)

    # Lounge symbol on the over-cab. No size.
    s.rect(nose_x + 14, top + 28, 52, 78, fill="none", stroke="#141414", sw=0.4, dash="2 1.2")
    s.text(nose_x + 18, top + 18, "LOUNGE TBD", 2.2, weight="bold")

    # AC curb and knockout — dashed provision, no size.
    s.rect(bed_x + 18, top + 22, 62, 40, fill="none", stroke="#141414", sw=0.45, dash="2.4 1.4")
    s.rect(bed_x + 28, top + 70, 16, 12, fill="none", stroke="#141414", sw=0.4, dash="1.8 1.2")
    s.text(bed_x + 86, top + 36, "AC CURB PAD", 2.4, weight="bold")
    s.text(bed_x + 86, top + 48, "SIZE TBD — D-08", 2.2)
    s.text(bed_x + 86, top + 60, "NOT THE UNIT", 2.2)
    s.text(bed_x + 50, top + 84, "DUCT / KNOCKOUT TBD", 2.15)

    # Solar and awning remain hooks.
    s.rect(bed_x + 150, top + 24, 78, 46, fill="none", stroke="#141414", sw=0.35, dash="2 1.2")
    s.text(bed_x + 156, top + 42, "SOLAR HOOK", 2.2)
    s.text(bed_x + 156, top + 54, "NOT BOM", 2.15)
    s.rect(bed_x + 16, bot - 16, 120, 8, fill="none", stroke="#141414", sw=0.35, dash="2 1.2")
    s.text(bed_x + 142, bot - 10, "AWNING HOOK — NOT BOM", 2.15)

    s.dim_h(nose_x, bed_x, bot + 16, "OVER-CAB ≈ 1223", top)
    s.dim_h(bed_x, rear_x, bot + 32, "FLOOR L 3647", top)
    s.dim_v(top, bot, rear_x + 16, "W 1911", rear_x, side="right")

    frame(s, 460, 40, 360, 150, "STATUS — PROVISION, NOT A UNIT")
    table(
        s,
        472,
        56,
        [150, 180],
        [
            ["ITEM", "STATUS"],
            ["AC curb pad", "PROVISION — D-08"],
            ["Duct / knockout", "TBD — NOT A CUT"],
            ["Generator bay", "PROVISION — D-07"],
            ["Solar / awning", "PHASE-2 HOOK"],
            ["AC unit", "NOT CUT DONE"],
            ["Generator unit", "NOT CUT DONE"],
        ],
        row_h=16,
        size=2.35,
    )

    frame(s, 28, 250, 792, 200, "GENERATOR BAY — UNDER THE ENVELOPE — SIDE OR REAR SKIRT")
    s.rect(52, 290, 340, 100, fill="#f7f7f7", stroke="#141414", sw=0.5)
    s.rect(70, 318, 90, 48, fill="none", stroke="#141414", sw=0.5, dash="2.4 1.4")
    s.line(52, 290, 392, 290, sw=0.9)
    s.text(60, 282, "ENVELOPE SKIRT — NTS", 2.3, weight="bold")
    s.text(78, 338, "GEN BAY", 2.3, weight="bold")
    s.text(170, 330, "FRAME TO SILL / OUTRIGGER", 2.4, weight="bold")
    s.text(170, 344, "NOT TO SKIN ALONE", 2.4)
    s.text(170, 360, "EXHAUST AWAY FROM HATCH", 2.3)
    s.text(170, 374, "AND FROM INTAKES — D-07", 2.3)
    s.text(420, 300, "NO BAY SIZE ON THIS SHEET.", 2.5, weight="bold")
    s.text(420, 316, "LOCATION IS A PROVISION.", 2.4)
    s.text(420, 332, "ENG CONFIRMS SIDE OR REAR.", 2.4)
    s.text(420, 356, "PARKED-ONLY GENERATOR RUN.", 2.5, weight="bold", fill="#9b1c1c")
    s.text(420, 372, "NO kW. NO BTU. NO BOLT GRADE.", 2.4, weight="bold")
    s.text(420, 396, "OAH ≤ 2500 = HATCH CLOSED", 2.4, weight="bold")
    s.text(420, 410, "+ CURB INSTALLED. ROAD =", 2.4)
    s.text(420, 424, "SEALED UNIT OR BLANKED COVER.", 2.4)

    s.text(28, 468, "DO NOT SCALE THE BAY. ROOF ENVELOPE DIMS ARE THE SoR FIGURES ONLY.", 2.55)
    s.text(28, 484, "UNITS ARE NOT A BUY LIST AND NOT CUT DONE. JAY GO STILL GATES ANY RAIL DRILL.", 2.55, weight="bold")
    return finish(s)


def sheet_d07() -> Sheet:
    s = Sheet("D-07", "GENERATOR PROVISION — BAY AND MOUNTS, NOT THE UNIT", "NTS — DO NOT SCALE", 16)
    hatch_defs(s)
    frame(s, 16, 16, 500, 228, "1  BAY TO SILL AND OUTRIGGER — NOT SKIN")
    s.rect(48, 78, 250, 12, fill="url(#hatch)", stroke="#141414", sw=0.4)
    s.rect(78, 90, 10, 58, fill="#ffffff", stroke="#141414", sw=0.4)
    s.rect(230, 90, 10, 58, fill="#ffffff", stroke="#141414", sw=0.4)
    s.rect(100, 128, 110, 10, fill="#ffffff", stroke="#141414", sw=0.45, dash="2 1.2")
    s.rect(64, 156, 190, 12, fill="#d0d0d0", stroke="#141414", sw=0.45)
    s.rect(300, 70, 78, 96, fill="none", stroke="#141414", sw=0.45, dash="2.2 1.3")
    s.circle(308, 100, 2.0, fill="#141414", stroke="none")
    s.circle(308, 132, 2.0, fill="#141414", stroke="none")
    s.text(48, 68, "SILL — STRUCTURE", 2.45, weight="bold")
    s.text(104, 122, "ISOLATOR PAD TBD", 2.3)
    s.text(70, 182, "OUTRIGGER — D-01", 2.4, weight="bold")
    s.text(300, 60, "SERVICE DOOR", 2.4, weight="bold")
    s.text(300, 180, "HINGE ON THE POST", 2.35, weight="bold")
    s.text(40, 206, "FAIL-IF THE MASS IS ON THE +1000 SKIN ONLY.", 2.45, weight="bold", fill="#9b1c1c")
    s.text(40, 222, "BOLT GRADE AND QTY ARE TBD. ENG GO IS EMPTY.", 2.4)

    frame(s, 528, 16, 297, 228, "2  EXHAUST, FILL, WEEP")
    s.text(544, 44, "EXHAUST HARDPOINT", 2.6, weight="bold")
    s.text(544, 60, "Away from the lounge hatch,", 2.4)
    s.text(544, 74, "the lounge intake, and the", 2.4)
    s.text(544, 88, "over-cab intake.", 2.4)
    s.text(544, 110, "FUEL FILL AND VENT", 2.6, weight="bold")
    s.text(544, 126, "Clear of cabin weep and", 2.4)
    s.text(544, 140, "electrical glands.", 2.4)
    s.text(544, 162, "SPLASH / WEEP", 2.6, weight="bold")
    s.text(544, 178, "Continuous with D-06.", 2.4)
    s.text(544, 200, "PARKED-ONLY RUN.", 2.6, weight="bold", fill="#9b1c1c")
    s.text(544, 216, "NO kW ON THIS SHEET.", 2.45, weight="bold")

    fail_box(s, 16, 254, 260, 36, "FAIL-IF EXHAUST OR CO IN CABIN", "LOUNGE AND CABIN BOTH")
    fail_box(s, 286, 254, 260, 36, "FAIL-IF MASS ON SKIN ONLY", "NEEDS OUTRIGGERS AND LEGS")
    fail_box(s, 556, 254, 268, 36, "FAIL-IF WET GLANDS", "OR A RAIL DRILL WITHOUT JAY GO")

    s.rect(16, 298, 250, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(24, 306, 7, layer="draw")
    s.text(38, 312, "JAY GO — RAIL DRILL UNSIGNED", 2.5, weight="bold")
    s.rect(276, 298, 250, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(284, 306, 7, layer="draw")
    s.text(298, 312, "ENG GO — PAD BOLTS UNSIGNED", 2.5, weight="bold")
    s.rect(536, 298, 288, 28, fill="#ffffff", stroke="#141414", sw=0.45)
    s.text(548, 312, "MAX kg BLANK UNTIL WEIGH", 2.5, weight="bold")

    callout_boxes(
        s,
        336,
        164,
        [
            (
                "ENG — BAY",
                [
                    "Frame the bay to the sill and",
                    "to the outriggers. Not to skin.",
                    "Isolator pad plate. Grade TBD.",
                    "Quantity TBD. Eng GO is empty.",
                    "Service-door hinge lands on",
                    "the post, not on the sheet.",
                    "Exhaust stays clear of the",
                    "hatch and of both intakes.",
                    "No generator kW is stated.",
                ],
            ),
            (
                "FIELD — RUN / WATER",
                [
                    "FAIL-IF exhaust or CO enters",
                    "the lounge or the cabin.",
                    "FAIL-IF the mass sits on the",
                    "+1000 skin, or has no legs",
                    "when the bay is occupied.",
                    "FAIL-IF glands are wet.",
                    "Run is parked only.",
                    "Keep the D-06 weep open.",
                    "Placard stays blank.",
                ],
            ),
            (
                "FSD — NOT A BUY LIST",
                [
                    "FSD = fabricator shop decision.",
                    "Do not buy a generator from",
                    "this sheet. Unit is not Done.",
                    "Do not invent a bolt grade.",
                    "Fill and vent stay clear of",
                    "weep and electrical glands.",
                    "Unsigned Jay GO = no rail hole.",
                    "Unsigned Eng GO = no pad bolts.",
                    "Not an LTO release.",
                ],
            ),
        ],
    )
    return finish(s)


def sheet_d08() -> Sheet:
    s = Sheet("D-08", "AC PROVISION — ROOF CURB INTO STRUCTURE, NOT THE UNIT", "NTS — DO NOT SCALE", 17)
    hatch_defs(s)
    frame(s, 16, 16, 500, 228, "1  CURB INTO ROOF RAILS — NOT SKIN")
    s.rect(60, 90, 280, 14, fill="url(#hatch)", stroke="#141414", sw=0.4)
    s.rect(100, 70, 12, 20, fill="#ffffff", stroke="#141414", sw=0.4)
    s.rect(280, 70, 12, 20, fill="#ffffff", stroke="#141414", sw=0.4)
    s.rect(112, 58, 168, 14, fill="#ffffff", stroke="#141414", sw=0.5, dash="2.2 1.3")
    s.line(150, 104, 150, 150, sw=0.4)
    s.polygon([(150, 150), (146, 142), (154, 142)], fill="#141414", stroke="none")
    s.text(70, 48, "CURB FRAME — SIZE TBD", 2.45, weight="bold")
    s.text(70, 168, "ROOF RAIL", 2.4, weight="bold")
    s.text(170, 168, "CONDENSATE TO WEEP", 2.4, weight="bold")
    s.text(170, 182, "NOT INTO THE CABIN CAVITY", 2.35)
    s.text(40, 206, "FAIL-IF THE CURB IS SCREWED TO SKIN ONLY.", 2.45, weight="bold", fill="#9b1c1c")
    s.text(40, 222, "NO BTU. NO UNIT MODEL. OPENING SIZE TBD.", 2.4)

    frame(s, 528, 16, 297, 228, "2  ROAD AND HOSE")
    s.text(544, 44, "OAH ≤ 2500 MEANS", 2.55, weight="bold")
    s.text(544, 60, "hatch closed AND the", 2.4)
    s.text(544, 74, "curb is installed.", 2.4)
    s.text(544, 96, "ON THE ROAD", 2.55, weight="bold")
    s.text(544, 112, "Sealed unit, or a blanked", 2.4)
    s.text(544, 126, "cover. Not an open curb.", 2.4)
    s.text(544, 148, "HOSE THE CLOSED CURB", 2.5, weight="bold")
    s.text(544, 164, "perimeter with D-03", 2.4)
    s.text(544, 178, "before any claim.", 2.4)
    s.text(544, 202, "UNIT IS NOT CUT DONE.", 2.5, weight="bold", fill="#9b1c1c")
    s.text(544, 218, "NOT A BUY LIST.", 2.45, weight="bold")

    fail_box(s, 16, 254, 260, 36, "FAIL-IF CURB IS SKIN-ONLY", "TIE IT TO THE ROOF RAILS")
    fail_box(s, 286, 254, 260, 36, "FAIL-IF CONDENSATE IN CABIN", "OR INTO THE LOUNGE")
    fail_box(s, 556, 254, 268, 36, "FAIL-IF THE CURB IS OPEN", "ON THE ROAD")

    s.rect(16, 298, 250, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(24, 306, 7, layer="draw")
    s.text(38, 312, "ENG GO — CURB JOINT UNSIGNED", 2.45, weight="bold")
    s.rect(276, 298, 250, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(284, 306, 7, layer="draw")
    s.text(298, 312, "JAY GO — RAIL DRILL UNSIGNED", 2.45, weight="bold")
    s.rect(536, 298, 288, 28, fill="#ffffff", stroke="#141414", sw=0.45)
    s.text(548, 312, "SEALANT AND COVER: TBD", 2.5, weight="bold")

    callout_boxes(
        s,
        336,
        164,
        [
            (
                "ENG — CURB",
                [
                    "Curb frame ties into roof rails.",
                    "It is not a skin-only angle.",
                    "Condensate goes to the weep.",
                    "It does not enter the cavity.",
                    "Hose the closed perimeter.",
                    "OAH ≤ 2500 is hatch closed",
                    "with the curb in place.",
                    "Opening size stays TBD.",
                    "No BTU is stated.",
                ],
            ),
            (
                "FIELD — WATER / ROAD",
                [
                    "FAIL-IF the curb is skin-only.",
                    "FAIL-IF condensate enters the",
                    "cabin or the lounge.",
                    "FAIL-IF the curb is open",
                    "while the vehicle is on road.",
                    "Road state is a sealed unit",
                    "or a blanked cover.",
                    "Hose this joint with D-03.",
                    "The unit is not cut Done.",
                ],
            ),
            (
                "FSD — NOT A BUY LIST",
                [
                    "FSD = fabricator shop decision.",
                    "Do not order an AC unit from",
                    "this sheet.",
                    "Do not cut the roof skin for",
                    "a curb until D-04 and D-08",
                    "both still say the opening",
                    "is unreleased.",
                    "Sealant stays TBD.",
                    "Jay GO still gates rail holes.",
                    "Not an LTO release.",
                ],
            ),
        ],
    )
    return finish(s)
