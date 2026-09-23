"""Phase-1 shell cut, frame, door, hatch, and shop sheets.

Figures come from the SoR only. Dashed openings are field-locate or intent.
Generator and AC units are not cut lines. Kerf, bend, grade, weld, and kg stay TBD.
"""

from __future__ import annotations

import sys
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(REPO / "blueprint-pack" / "tools"))

from sheetlib import Sheet  # noqa: E402

COUNT = 25
OUT = ROOT


def frame(s: Sheet, x, y, w, h, title: str):
    s.rect(x, y, w, h, fill="#ffffff", stroke="#141414", sw=0.45)
    s.rect(x, y, w, 8, fill="#141414", stroke="none")
    s.text(x + 2.5, y + 5.7, title, 2.7, fill="#ffffff", weight="bold")


def table(s: Sheet, x, y, col_ws, rows, row_h=12.0, size=2.15):
    width = sum(col_ws)
    height = row_h * len(rows)
    s.rect(x, y, width, row_h, fill="#e6e6e6", stroke="none")
    s.rect(x, y, width, height, fill="none", stroke="#141414", sw=0.35)
    xx = x
    for cw in col_ws[:-1]:
        xx += cw
        s.line(xx, y, xx, y + height, sw=0.22)
    for i in range(1, len(rows)):
        s.line(x, y + i * row_h, x + width, y + i * row_h, sw=0.22)
    for i, row in enumerate(rows):
        baseline = y + i * row_h + row_h / 2 + 0.34 * size
        cx = x
        for cw, cell in zip(col_ws, row):
            weight = "bold" if i == 0 else "normal"
            tw = s.text_width(cell, size, weight)
            if tw > cw - 2.4:
                raise SystemExit(f"{s.sid}: overflow '{cell}' {tw:.1f}>{cw - 2.4:.1f}")
            s.text(cx + 1.4, baseline, cell, size, weight=weight)
            cx += cw


def finish(s: Sheet) -> Sheet:
    s.border()
    s.title_block()
    return s


def new(sid, title, scale, no) -> Sheet:
    return Sheet(sid, title, scale, no, COUNT)


def grain(s: Sheet, x, y):
    s.text(x, y - 3.4, "GRAIN / FACE", 2.15, weight="bold")
    s.line(x, y, x + 22, y, sw=0.32)
    s.arrow_h(x + 22, y, 1)


def go_pair(s: Sheet, x, y):
    s.rect(x, y, 168, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(x + 4, y + 8, 6, layer="draw")
    s.text(x + 14, y + 13, "JAY GO UNSIGNED", 2.3, weight="bold")
    s.text(x + 14, y + 23, "RAIL DRILL = NO-GO", 2.15, fill="#9b1c1c")
    s.rect(x + 176, y, 168, 28, fill="#ffffff", stroke="#9b1c1c", sw=0.55)
    s.checkbox(x + 180, y + 8, 6, layer="draw")
    s.text(x + 190, y + 13, "ENG GO UNSIGNED", 2.3, weight="bold")
    s.text(x + 190, y + 23, "TUBE / WELD = TBD", 2.15, fill="#9b1c1c")


def sheet_cvr():
    s = new("CVR-00", "COVER — R&D FABRICATOR PACK", "—", 1)
    s.text(18, 24, "FABRICATOR BUILDS FROM THIS PACK ONLY. A VERBAL BRIEF IS NOT THE SoR.", 3.3, weight="bold")
    s.text(18, 38, "PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED", 3.1, weight="bold", fill="#9b1c1c")
    s.rect(16, 46, 809, 36, fill="#ffffff", stroke="#9b1c1c", sw=0.7)
    s.text(28, 60, "STAMP: CONDITIONAL — GATES UNSIGNED = DO NOT CUT", 3.4, weight="bold", fill="#9b1c1c")
    s.text(28, 74, "REV CONDITIONAL  ·  2026-09-23  ·  R&D BUILD  ·  NOT AN LTO RELEASE", 2.6)
    rows = [
        ["READ", "WHERE", "WHAT YOU MAY CUT"],
        ["1", "DIMS.md", "SoR figures only"],
        ["2", "I-00 then S-01…S-08", "Envelope. Dashed is not a cut."],
        ["3", "D-01…D-08", "Mounts. Units are not Done."],
        ["4", "cut/C-00…C-06", "Sheet blanks. Splices TBD."],
        ["5", "cut/C-FR and C-PL", "Members and plates. Holes TBD."],
        ["6", "cut/frame F-00…F-03", "Load path into rails, not skin."],
        ["7", "cut/door and cut/hatch", "Field locate and intent."],
        ["8", "cut/shop AS J FS MAT", "Sequence, joints, holes, stock."],
        ["9", "cut/shop BOM-01 QA-01", "Phase-1 lines. Then hose test."],
    ]
    table(s, 16, 92, [28, 220, 280], rows, row_h=14, size=2.4)
    s.text(18, 268, "REJECTED SUBSTITUTIONS — DO NOT CUT TO THESE", 2.8, weight="bold")
    table(
        s,
        16,
        276,
        [200, 280],
        [
            ["REJECTED", "USE INSTEAD"],
            ["Any floor width but 1911", "1911"],
            ["Any over-cab but ≈ 1223", "≈ 1223"],
            ["Any entry but 700 × 1550", "700 × 1550 field locate"],
            ["Photo-scale overall length", "OAL ≈ 6300 only"],
        ],
        row_h=13,
        size=2.3,
    )
    s.text(520, 300, "GATES STILL OPEN", 2.8, weight="bold")
    s.text(520, 316, "As-found tape", 2.4)
    s.text(520, 330, "Jay GO rail drill", 2.4)
    s.text(520, 344, "Eng tube and weld", 2.4)
    s.text(520, 358, "Weigh before any kg", 2.4)
    s.text(520, 372, "Hose test D-03", 2.4)
    s.text(520, 386, "D-07 / D-08 provisions", 2.4)
    s.text(18, 470, "PHASE-2 SOLAR, AWNING, SEATS, AC UNIT, AND GENERATOR UNIT ARE HOOKS. THEY ARE NOT CUT DONE.", 2.6, weight="bold")
    s.text(18, 488, "DISTRIBUTION: SHOP TRAVELER + THIS PACK. DO NOT SCALE A PNG.", 2.6)
    return finish(s)


def sheet_c00():
    s = new("C-00", "NEST INDEX — STOCK, QTY, LEFTOVER", "NTS", 2)
    s.text(18, 24, "STOCK CANDIDATES: 1220×2440 AND 1525×3050. NO BRAND. KERF TBD. EDGE ALLOWANCE TBD.", 2.7, weight="bold")
    s.text(18, 36, "1220×2440 HOLDS NONE OF THE SHELL EDGES BELOW. 1525×3050 STILL NEEDS SPLICES. JOINTS ARE SHOP TBD.", 2.45)
    rows = [
        ["MK", "BLANK", "L", "W", "QTY", "STOCK", "SPLICE", "LEFTOVER"],
        ["P1", "Floor pan", "3647", "1911", "1", "B + splice", "L and W", "Yield TBD"],
        ["P2", "Side LH", "3647", "≈1830", "1", "B + splice", "L and W", "Yield TBD"],
        ["P3", "Side RH", "3647", "≈1830", "1", "B + splice", "L and W", "Yield TBD"],
        ["P4-A", "Loft floor est.", "≈1223", "1911", "1", "One B", "None if est.", "L-offcut"],
        ["P4-B", "Loft ceiling est.", "≈1223", "1911", "1", "One B", "None if est.", "L-offcut"],
        ["P4-C", "Front face est.", "1911", "≈1830", "1", "B + splice", "Both >1525", "Yield TBD"],
        ["P4-D", "Loft side LH", "≈1223", "≈1830", "1", "B + splice", "H >1525", "Yield TBD"],
        ["P4-E", "Loft side RH", "≈1223", "≈1830", "1", "B + splice", "H >1525", "Yield TBD"],
        ["P5", "Rear wall", "1911", "≈1830", "1", "B + splice", "Both >1525", "Yield TBD"],
        ["P6", "Roof", "4870", "1911", "1", "B + splice", "L and W", "Yield TBD"],
        ["P7", "Entry", "—", "—", "0", "Not a blank", "On P2 only", "Field locate"],
        ["P8", "Windows", "—", "—", "0", "Not a blank", "Dashed only", "Size TBD"],
    ]
    table(s, 16, 46, [42, 110, 52, 58, 32, 78, 78, 80], rows, row_h=16.2, size=2.2)
    s.text(18, 290, "B = 1525×3050. L-OFFCUT IS THE REMAINDER ON THAT SHEET. DO NOT RELEASE THE OFFCUT AS A PART.", 2.45)
    s.text(18, 306, "P4 LENGTHS ARE ESTIMATES. H ≈ 1830 IS AN ESTIMATE. AS-FOUND TAPE GOVERNS THOSE EDGES.", 2.45)
    s.text(18, 322, "BEND ALLOWANCE IS TBD. THESE ARE ENVELOPE FLATS, NOT DEVELOPED BLANKS. NO THICKNESS.", 2.45, weight="bold")
    s.text(18, 338, "P7 TARGET 700×1550 IS FIELD LOCATE, NOT A CUT FREEZE. P8 HAS NO CUT SIZE.", 2.45)
    s.text(18, 354, "AC CURB AND GENERATOR BAY ARE NOT NEST BLANKS. SEE D-07 AND D-08. UNITS ARE NOT CUT DONE.", 2.45, weight="bold")
    s.text(18, 378, "GRAIN / FACE ARROW IS ON EACH BLANK SHEET. FACE MEANS THE EXTERIOR SKIN.", 2.45)
    s.text(18, 402, "QTY IS THE SHELL COUNT. DO NOT MULTIPLY FOR PHASE-2 GEAR.", 2.45)
    go_pair(s, 18, 450)
    return finish(s)


def _panel(s, x, y, rw, rh, sc, h_label, v_label):
    w, h = rw * sc, rh * sc
    s.rect(x, y, w, h, fill="#f4f4f4", stroke="#141414", sw=0.6)
    s.dim_h(x, x + w, y + h + 14, h_label, y + h, size=2.8)
    s.dim_v(y, y + h, x + w + 14, v_label, x + w, side="right", size=2.8)
    grain(s, x + 8, y + h - 10)
    return w, h


def sheet_c01():
    s = new("C-01", "P1 FLOOR PAN FLAT — 3647 × 1911", "DO NOT SCALE", 3)
    s.text(18, 24, "CUT FIGURES: 3647 × 1911. EDGE ALLOWANCE TBD. KERF TBD. DO NOT ADD A MILLIMETRE.", 2.7, weight="bold")
    sc = 0.12
    x, y = 36, 58
    w, h = _panel(s, x, y, 3647, 1911, sc, "3647 mm", "1911 mm")
    split = x + 2647 * sc
    s.line(split, y, split, y + h, sw=0.35, dash="3 1.5")
    s.text(x + 8, y + 12, "P1  BED ZONE 2647", 2.5, weight="bold")
    s.text(split + 6, y + 12, "TAIL +1000", 2.5, weight="bold")
    s.text(18, 400, "EXCEEDS 1220×2440 AND 1525×3050. SPLICE JOINT IS SHOP TBD. SEE C-00.", 2.6)
    s.text(18, 416, "PAN LANDS ON OUTRIGGERS. IT IS NOT THE CHASSIS JOINT. SEE F-01 AND D-01.", 2.6, weight="bold")
    s.text(18, 432, "WEEP PATH IS REQUIRED. HOLE DIAMETER AND PITCH ARE TBD. SEE A06.", 2.6)
    s.text(18, 448, "DASHED LINE IS THE BED / TAIL BREAK. IT IS NOT A CUT LINE.", 2.6)
    return finish(s)


def sheet_c02():
    s = new("C-02", "P2 LH SIDE WALL — ENTRY FIELD LOCATE", "DO NOT SCALE", 4)
    s.text(18, 22, "ENVELOPE L 3647. H ≈ 1830 IS AN ESTIMATE. AS-FOUND GOVERNS. DO NOT SCALE OPENINGS.", 2.6, weight="bold")
    sc = 0.105
    x, y = 40, 56
    w, h = _panel(s, x, y, 3647, 1830, sc, "3647 mm", "H ≈ 1830 EST.")
    s.rect(x + 28, y + 16, 700 * sc, 1550 * sc, fill="none", stroke="#141414", sw=0.45, dash="2.4 1.4")
    s.rect(x + 150, y + 28, 46, 28, fill="none", stroke="#141414", sw=0.4, dash="2 1.2")
    s.text(x + 8, y + 12, "P2 LH", 2.4, weight="bold")
    s.text(460, 80, "P7 ENTRY", 2.8, weight="bold")
    s.text(460, 96, "700 × 1550 TARGET", 2.5)
    s.text(460, 112, "FIELD LOCATE", 2.5, weight="bold")
    s.text(460, 128, "NOT A CUT FREEZE", 2.5, fill="#9b1c1c")
    s.text(460, 144, "NO EDGE DIMENSION", 2.5)
    s.text(460, 168, "HEAD + SILL SHARE", 2.5)
    s.text(460, 184, "1830 EST. − 1550 = 280", 2.4)
    s.text(460, 200, "SPLIT IS NOT GIVEN", 2.4, weight="bold")
    s.text(460, 224, "P8 WINDOW SYMBOL", 2.6, weight="bold")
    s.text(460, 240, "SIZE TBD", 2.5)
    s.text(460, 256, "DO NOT SCALE IT", 2.5)
    s.text(18, 400, "THE DASHED RECTANGLES ARE NOT LOCATED. DO NOT MEASURE THEM OFF THE PLOT.", 2.6, weight="bold")
    s.text(18, 418, "DEFAULT DOOR IS THIS LH WALL ONLY. RH IS C-03.", 2.6)
    s.text(18, 436, "WALL HEIGHT IS AN ESTIMATE UNTIL THE TAPE IS FROZEN.", 2.6)
    return finish(s)


def sheet_c03():
    s = new("C-03", "P3 RH SIDE WALL — MIRROR, NO ENTRY", "DO NOT SCALE", 5)
    s.text(18, 22, "MIRROR OF P2. DEFAULT: NO ENTRY CUT ON RH UNLESS A DUAL-DOOR SHEET IS ISSUED.", 2.6, weight="bold")
    sc = 0.105
    x, y = 40, 56
    _panel(s, x, y, 3647, 1830, sc, "3647 mm", "H ≈ 1830 EST.")
    s.rect(x + 160, y + 30, 50, 30, fill="none", stroke="#141414", sw=0.4, dash="2 1.2")
    s.text(x + 8, y + 12, "P3 RH", 2.4, weight="bold")
    s.text(460, 90, "NO ENTRY ON RH", 2.8, weight="bold")
    s.text(460, 110, "DO NOT COPY P7 HERE", 2.5)
    s.text(460, 134, "P8 WINDOW SYMBOL", 2.6, weight="bold")
    s.text(460, 150, "SIZE TBD", 2.5)
    s.text(460, 166, "FIELD LOCATE", 2.5)
    s.text(460, 182, "DO NOT SCALE IT", 2.5)
    s.text(18, 400, "H ≈ 1830 IS AN ESTIMATE. AS-FOUND GOVERNS. SPLICE PER C-00.", 2.6)
    s.text(18, 418, "ONE WINDOW SYMBOL. BODY WINDOWS ARE TWO ON THE SHELL, NOT TWO ON THIS WALL.", 2.6)
    return finish(s)


def sheet_c04():
    s = new("C-04", "P4 OVER-CAB LOFT — ENVELOPE FLATS", "DO NOT SCALE", 6)
    s.text(18, 22, "ENVELOPE ≈ 1223 × 1911. FLATS ARE NOT DEVELOPED. BEND ALLOWANCE TBD. NO THICKNESS.", 2.55, weight="bold")
    specs = [
        (24, 40, 150, 96, "P4-A LOFT FLOOR", "≈1223 × 1911 EST."),
        (230, 40, 150, 96, "P4-B LOFT CEILING", "≈1223 × 1911 EST."),
        (436, 40, 150, 96, "P4-C FRONT FACE", "1911 × ≈1830 EST."),
        (24, 168, 150, 96, "P4-D LOFT SIDE LH", "≈1223 × ≈1830 EST."),
        (230, 168, 150, 96, "P4-E LOFT SIDE RH", "≈1223 × ≈1830 EST."),
    ]
    for x, y, w, h, a, b in specs:
        s.rect(x, y, w, h, fill="#f4f4f4", stroke="#141414", sw=0.5)
        s.text(x + 6, y + 14, a, 2.4, weight="bold")
        s.text(x + 6, y + 28, b, 2.2)
        s.text(x + 6, y + 42, "ESTIMATE", 2.2, fill="#9b1c1c")
        grain(s, x + 6, y + h - 8)
    s.text(420, 190, "PLOT IS NOT TO SCALE.", 2.5, weight="bold")
    s.text(420, 208, "CUT THE TEXT FIGURES.", 2.4)
    s.text(420, 226, "AS-FOUND GOVERNS H", 2.4)
    s.text(420, 244, "AND THE 1223 LENGTH.", 2.4)
    s.text(18, 300, "FRONT-FACE OPENING IS OPTIONAL AND HAS NO CUT SIZE. DO NOT ADD ONE.", 2.55)
    s.text(18, 318, "OVER-CAB WINDOW IS P8. SIZE TBD. FIELD LOCATE. NOT DRAWN AS A CUT.", 2.55)
    s.text(18, 336, "CAB ROOF IS NOT A BEAM. THE RING CARRIES THE LOFT. SEE F-02 AND J-01.", 2.55, weight="bold")
    s.text(18, 362, "P4-A AND P4-B EACH FIT ONE 1525×3050 IF THE ESTIMATE HOLDS. OFFCUT IS NOT A PART.", 2.55)
    s.text(18, 380, "P4-C AND THE SIDES EXCEED 1525 ON THE TALL EDGE. SPLICE TBD.", 2.55)
    go_pair(s, 18, 430)
    return finish(s)


def sheet_c05():
    s = new("C-05", "P5 REAR WALL — INTENT OPENINGS NOT FROZEN", "DO NOT SCALE", 7)
    s.text(18, 22, "ENVELOPE 1911 × H ≈ 1830 ESTIMATE. REAR WINDOW AND LOWER HATCH HAVE NO CUT SIZE.", 2.55, weight="bold")
    x, y, w, h = 80, 48, 220, 210
    s.rect(x, y, w, h, fill="#f4f4f4", stroke="#141414", sw=0.6)
    s.rect(x + 50, y + 24, 70, 40, fill="none", stroke="#141414", sw=0.4, dash="2.2 1.3")
    s.rect(x + 40, y + 130, 90, 50, fill="none", stroke="#141414", sw=0.4, dash="2.2 1.3")
    s.dim_h(x, x + w, y + h + 14, "1911 mm", y + h, size=2.8)
    s.dim_v(y, y + h, x + w + 14, "H ≈ 1830 EST.", x + w, side="right", size=2.7)
    grain(s, x + 8, y + h - 12)
    s.text(360, 70, "UPPER DASHED", 2.6, weight="bold")
    s.text(360, 86, "REAR WINDOW", 2.5)
    s.text(360, 102, "INTENT TBD", 2.5)
    s.text(360, 118, "NOT A CUT FREEZE", 2.5, fill="#9b1c1c")
    s.text(360, 146, "LOWER DASHED", 2.6, weight="bold")
    s.text(360, 162, "LOWER HATCH", 2.5)
    s.text(360, 178, "INTENT TBD — H-02", 2.5)
    s.text(360, 194, "NOT A CUT FREEZE", 2.5, fill="#9b1c1c")
    s.text(360, 222, "DO NOT SCALE EITHER", 2.5, weight="bold")
    s.text(360, 238, "OPENING.", 2.5)
    s.text(18, 400, "SYMBOLS ARE NOT LOCATED AND NOT SIZED. S-06 IS INTENT, NOT A PATTERN.", 2.6)
    s.text(18, 418, "BOTH EDGES EXCEED 1525. SPLICE TBD. SEE C-00.", 2.6)
    return finish(s)


def sheet_c06():
    s = new("C-06", "P6 ROOF — 4870 × 1911 — LOUNGE NOT FROZEN", "DO NOT SCALE", 8)
    s.text(18, 22, "4870 = 1223 + 3647. NOT A NEW MEASURED DATUM. LOUNGE HATCH SIZE IS INTENT TBD.", 2.55, weight="bold")
    sc = 0.09
    x, y = 36, 48
    w, h = _panel(s, x, y, 4870, 1911, sc, "4870 mm  (1223+3647)", "1911 mm")
    oc = x + 1223 * sc
    s.line(oc, y, oc, y + h, sw=0.35, dash="3 1.4")
    s.rect(oc + 40, y + 28, 70, 46, fill="none", stroke="#141414", sw=0.45, dash="2.2 1.3")
    s.text(x + 6, y + 12, "OVER-CAB", 2.2, weight="bold")
    s.text(oc + 6, y + 12, "FLOOR ROOF", 2.2, weight="bold")
    s.text(520, 70, "DASHED HATCH", 2.6, weight="bold")
    s.text(520, 86, "INTENT / NOT A CUT", 2.4, fill="#9b1c1c")
    s.text(520, 102, "SIZE TBD — F-03 H-01", 2.4)
    s.text(520, 118, "DO NOT SCALE IT", 2.4, weight="bold")
    s.text(520, 142, "SHOP SPLICE TBD", 2.5, weight="bold")
    s.text(520, 158, "IF STOCK REQUIRES.", 2.4)
    s.text(520, 174, "BREAK IS NOT THIS PLOT.", 2.4)
    s.text(520, 198, "PHASE-2 SOLAR,", 2.4, weight="bold")
    s.text(520, 214, "AC, AND AWNING", 2.4, weight="bold")
    s.text(520, 230, "ARE NOT CUT HERE.", 2.4, weight="bold")
    s.text(520, 254, "AC CURB IS D-08.", 2.4)
    s.text(520, 270, "NOT A ROOF CUT", 2.4)
    s.text(520, 286, "ON THIS SHEET.", 2.4)
    s.text(18, 400, "OAH ≤ 2500 IS THE HATCH CLOSED. OPENING THE HATCH IS PARKED ONLY.", 2.6, weight="bold")
    s.text(18, 418, "WIDTH AND LENGTH BOTH EXCEED 1525×3050. SEE C-00. JOINT DESIGN IS UNRELEASED.", 2.6)
    return finish(s)


def sheet_cfr():
    s = new("C-FR", "FRAME CUT LIST — LENGTHS FROM THE SoR", "NTS", 9)
    s.text(18, 22, "TUBE SECTION TBD. MITER TBD. HOLES TBD. CUT LENGTH FOLLOWS THE NOTE, NOT A GUESS.", 2.5, weight="bold")
    rows = [
        ["MK", "MEMBER", "LENGTH", "QTY", "END", "HOLES", "NOTE"],
        ["FR-01", "Floor long LH", "3647", "1", "TBD", "TBD", "Rail + tail. Not skin."],
        ["FR-02", "Floor long RH", "3647", "1", "TBD", "TBD", "Mirror of FR-01."],
        ["FR-03", "Floor cross front", "1911 env.", "1", "TBD", "TBD", "Minus joint TBD."],
        ["FR-04", "Floor cross rear", "1911 env.", "1", "TBD", "TBD", "Tail end. Joint TBD."],
        ["FR-05", "Bed-tail fishplate", "TBD", "2", "—", "TBD", "J-01. Size unreleased."],
        ["FR-06", "Outrigger", "TBD", "TBD", "TBD", "Jay GO", "Pitch = as-found."],
        ["FR-07", "Corner post", "≈1830 est.", "4", "TBD", "TBD", "Cut = as-found H."],
        ["FR-08", "Mid post", "≈1830 est.", "TBD", "TBD", "TBD", "Count = Eng."],
        ["FR-09", "Sill LH", "3647", "1", "TBD", "TBD", "Entry is field locate."],
        ["FR-10", "Sill RH", "3647", "1", "TBD", "TBD", "No entry by default."],
        ["FR-11", "Roof long LH", "4870", "1", "TBD", "TBD", "1223+3647. Splice TBD."],
        ["FR-12", "Roof long RH", "4870", "1", "TBD", "TBD", "Mirror. Splice TBD."],
        ["FR-13", "Roof cross nose", "1911 env.", "1", "TBD", "TBD", "Minus joint TBD."],
        ["FR-14", "Roof cross rear", "1911 env.", "1", "TBD", "TBD", "Minus joint TBD."],
        ["FR-15", "Over-cab long", "≈1223 est.", "2", "TBD", "TBD", "Estimate. Confirm."],
        ["FR-16", "Over-cab cross", "1911 env.", "1", "TBD", "TBD", "At the cab face."],
        ["FR-17", "Hatch frame long", "TBD", "2", "TBD", "TBD", "Opening intent only."],
        ["FR-18", "Hatch frame cross", "TBD", "2", "TBD", "TBD", "Closed ring. D-04."],
        ["FR-19", "Door stile", "1550+TBD", "2", "TBD", "TBD", "Plus buildup. DR-02."],
        ["FR-20", "Door head", "700+TBD", "1", "TBD", "TBD", "Field locate on P2."],
        ["FR-21", "Door threshold", "700+TBD", "1", "TBD", "TBD", "Weep outward."],
        ["FR-22", "Rear hatch frame", "TBD", "4", "TBD", "TBD", "H-02 size unreleased."],
    ]
    table(s, 16, 32, [48, 118, 72, 36, 40, 52, 150], rows, row_h=14.6, size=2.15)
    s.text(18, 400, "NO GENERATOR AND NO AC UNIT ON THIS LIST. PROVISIONS ARE D-07 AND D-08.", 2.5, weight="bold")
    s.text(18, 418, "1911 ENV. MEANS THE SHELL WIDTH. DEDUCT THE JOINT. DO NOT CUT 1911 BLIND.", 2.5)
    s.text(18, 436, "≈1830 AND ≈1223 ARE ESTIMATES. AS-FOUND TAPE GOVERNS BEFORE THE SAW.", 2.5)
    go_pair(s, 400, 448)
    return finish(s)


def sheet_cpl():
    s = new("C-PL", "MOUNT PLATES AND GUSSETS — HOLES TBD", "NTS", 10)
    s.text(18, 22, "NO PLATE SIZE, HOLE DIAMETER, OR BOLT GRADE IS RELEASED. JAY GO GATES RAIL HOLES.", 2.55, weight="bold")
    rows = [
        ["MK", "PLATE", "QTY", "HOLES", "LANDS ON", "STATUS"],
        ["PL-01", "Outrigger backing", "TBD", "TBD", "Bed / chassis rail", "Jay GO"],
        ["PL-02", "Outrigger top", "TBD", "TBD", "Outrigger + floor", "Eng GO"],
        ["PL-03", "Ladder stand-off", "TBD", "TBD", "Post or sill D-05", "Not a jack"],
        ["PL-04", "Hatch hinge", "TBD", "TBD", "Hatch frame F-03", "Not skin"],
        ["PL-05", "Hatch strut", "TBD", "TBD", "Hatch frame", "Not skin"],
        ["PL-06", "Landing-leg pad", "TBD", "TBD", "Tail frame D-02", "kg blank"],
        ["PL-07", "Door hinge reinforcer", "TBD", "TBD", "Jamb post", "Not skin"],
        ["PL-08", "Bed-tail fishplate", "2", "TBD", "Floor longs J-01", "Eng weld"],
        ["PL-09", "Gen isolator pad", "TBD", "TBD", "Sill / outrigger", "Provision"],
        ["PL-10", "AC curb cleat", "TBD", "TBD", "Roof rail D-08", "Provision"],
    ]
    table(s, 16, 36, [52, 150, 40, 48, 150, 80], rows, row_h=18, size=2.3)
    s.rect(560, 50, 240, 140, fill="#f7f7f7", stroke="#141414", sw=0.5)
    s.circle(620, 100, 4, fill="none", stroke="#141414", sw=0.4)
    s.circle(700, 100, 4, fill="none", stroke="#141414", sw=0.4)
    s.circle(620, 150, 4, fill="none", stroke="#141414", sw=0.4)
    s.circle(700, 150, 4, fill="none", stroke="#141414", sw=0.4)
    s.text(580, 70, "GENERIC PLATE", 2.4, weight="bold")
    s.text(575, 210, "CENTERS TBD. NOT A PATTERN.", 2.3, weight="bold")
    s.text(18, 400, "PL-09 AND PL-10 ARE PROVISIONS. THEY DO NOT RELEASE A GENERATOR OR AN AC UNIT.", 2.55, weight="bold")
    s.text(18, 418, "EDGE DISTANCE TBD. DO NOT DRILL THE CHASSIS RAIL UNTIL JAY GO ON D-01.", 2.55)
    go_pair(s, 18, 450)
    return finish(s)


def sheet_f00():
    s = new("F-00", "FRAME INDEX — MEMBERS AND GATES", "—", 11)
    s.text(18, 24, "LOAD PATH: SKIN TO STIFFENERS TO POSTS AND SILLS TO OUTRIGGERS TO RAILS. NOT THE GI SKIN.", 2.6, weight="bold")
    rows = [
        ["SHEET", "COVERS", "RELEASE"],
        ["F-01", "Floor plan, tail +1000, outriggers", "Holes TBD + Jay GO"],
        ["F-02", "Posts, sills, roof rails, over-cab ring", "Tube section TBD"],
        ["F-03", "Roof ring and lounge hatch frame", "Opening size TBD"],
        ["C-FR", "Cut list matching F-01…F-03", "Miters TBD"],
        ["J-01", "Splices and corners", "Weld size TBD"],
        ["D-01", "Rail drill", "Jay GO unsigned"],
        ["D-07", "Generator bay provision", "Unit not cut Done"],
        ["D-08", "AC curb provision", "Unit not cut Done"],
    ]
    table(s, 16, 40, [70, 320, 200], rows, row_h=18, size=2.45)
    s.text(18, 230, "KNOWN LENGTHS", 2.8, weight="bold")
    s.text(18, 248, "Floor longs and sills 3647. Width envelope 1911. Roof longs 4870 = 1223+3647.", 2.5)
    s.text(18, 264, "Posts ≈1830 estimate. Over-cab longs ≈1223 estimate. As-found governs both.", 2.5)
    s.text(18, 280, "Outrigger length is as-found rail pitch plus the edge reach. Do not invent the pitch.", 2.5)
    s.text(18, 304, "FAIL-IF A JOINT LANDS IN THE OUTER SKIN ONLY.", 2.7, weight="bold", fill="#9b1c1c")
    go_pair(s, 18, 430)
    return finish(s)


def sheet_f01():
    s = new("F-01", "FLOOR AND OUTRIGGER FRAME PLAN", "DO NOT SCALE", 12)
    s.text(18, 22, "FRAME LANDS ON BED RAILS. TAIL +1000 IS IN THE FRAME. SKIN DOES NOT CARRY THE SHELL.", 2.55, weight="bold")
    sc = 0.1
    x, y = 40, 70
    w, h = 3647 * sc, 1911 * sc
    s.rect(x, y, w, h, fill="#f7f7f7", stroke="#141414", sw=0.6)
    s.line(x + 16, y + 14, x + w - 16, y + 14, sw=0.7)
    s.line(x + 16, y + h - 14, x + w - 16, y + h - 14, sw=0.7)
    split = x + 2647 * sc
    s.line(split, y, split, y + h, sw=0.35, dash="3 1.4")
    for i in range(4):
        yy = y + 36 + i * 28
        s.line(x + 10, yy, x + w - 10, yy, sw=0.3, dash="2 1.4")
    s.dim_h(x, x + w, y + h + 16, "3647 mm", y + h, size=2.7)
    s.dim_v(y, y + h, x + w + 14, "1911 mm", x + w, side="right", size=2.6)
    s.text(x + 8, y + 12, "LH LONG", 2.2, weight="bold")
    s.text(x + 8, y + h - 8, "RH LONG", 2.2, weight="bold")
    s.text(split + 4, y + 28, "TAIL +1000", 2.2, weight="bold")
    s.text(500, 80, "DASHED CROSSES", 2.5, weight="bold")
    s.text(500, 96, "OUTRIGGERS", 2.4)
    s.text(500, 112, "PITCH = AS-FOUND", 2.4, weight="bold")
    s.text(500, 128, "QTY TBD", 2.4)
    s.text(500, 152, "INSET OF LONGS", 2.5, weight="bold")
    s.text(500, 168, "IS NOT A CUT DIM", 2.4)
    s.text(500, 192, "LOAD PATH DOWN", 2.5, weight="bold")
    s.text(500, 208, "INTO THE RAILS", 2.4)
    s.text(500, 224, "NOT INTO SKIN", 2.4, fill="#9b1c1c")
    s.text(18, 400, "HOLE SCHEDULE: DIAMETER TBD, EDGE TBD, TORQUE TBD. SEE FS-01 AND D-01.", 2.55)
    s.text(18, 418, "BED / TAIL SPLICE IS J-01. DO NOT WELD UNTIL ENG GO.", 2.55)
    go_pair(s, 18, 448)
    return finish(s)


def sheet_f02():
    s = new("F-02", "WALL POSTS, SILLS, ROOF RAILS, OVER-CAB RING", "DO NOT SCALE", 13)
    s.text(18, 22, "TUBE SECTION IS TBD. DO NOT PICK A SIZE FROM THIS PLOT.", 2.6, weight="bold")
    sc = 0.07
    ox, roof_y = 50, 80
    floor_y = roof_y + 1830 * sc
    roof_x0 = ox
    floor_x0 = ox + 1223 * sc
    x1 = floor_x0 + 3647 * sc
    s.line(roof_x0, roof_y, x1, roof_y, sw=0.9)
    s.line(floor_x0, floor_y, x1, floor_y, sw=0.9)
    s.line(roof_x0, roof_y, roof_x0, floor_y, sw=0.7)
    s.line(floor_x0, roof_y, floor_x0, floor_y, sw=0.7)
    s.line(x1, roof_y, x1, floor_y, sw=0.7)
    mid = floor_x0 + 140
    s.line(mid, roof_y, mid, floor_y, sw=0.4, dash="2 1.3")
    s.dim_h(roof_x0, floor_x0, roof_y - 16, "≈1223 EST.", roof_y, size=2.6)
    s.dim_h(floor_x0, x1, floor_y + 18, "3647 mm", floor_y, size=2.6)
    s.dim_v(roof_y, floor_y, x1 + 16, "H ≈1830 EST.", x1, side="right", size=2.5)
    s.text(roof_x0 + 4, roof_y + 14, "ROOF RAIL 4870", 2.3, weight="bold")
    s.text(floor_x0 + 4, floor_y - 8, "SILL 3647", 2.3, weight="bold")
    s.text(mid + 4, roof_y + 40, "MID X TBD", 2.2)
    s.text(500, 90, "SECTION TBD", 2.8, weight="bold")
    s.text(500, 110, "ENG GO IS EMPTY.", 2.5)
    s.text(500, 134, "POST CUT LENGTH", 2.5, weight="bold")
    s.text(500, 150, "= AS-FOUND H.", 2.5)
    s.text(500, 166, "1830 IS ESTIMATE.", 2.5)
    s.text(500, 190, "CAB ROOF IS NOT", 2.5, weight="bold")
    s.text(500, 206, "A BEAM. SEE J-01.", 2.5)
    s.text(18, 400, "CORNER POSTS: QTY 4. MID POSTS: QTY TBD. NO ENTRY ON THE RH SILL.", 2.55)
    s.text(18, 418, "OVER-CAB RING LONGS ≈1223 ESTIMATE. WIDTH ENVELOPE 1911.", 2.55)
    go_pair(s, 18, 448)
    return finish(s)


def sheet_f03():
    s = new("F-03", "ROOF RING AND LOUNGE HATCH FRAME", "DO NOT SCALE", 14)
    s.text(18, 22, "FAIL-IF THE ROOF IS CUT OPEN BEFORE THIS RING IS CLOSED AND SEALED. SEE D-04.", 2.55, weight="bold", fill="#9b1c1c")
    sc = 0.085
    x, y = 36, 56
    w, h = 4870 * sc, 1911 * sc
    s.rect(x, y, w, h, fill="#f7f7f7", stroke="#141414", sw=0.6)
    s.rect(x + 10, y + 10, w - 20, h - 20, fill="none", stroke="#141414", sw=0.45)
    oc = x + 1223 * sc
    s.line(oc, y, oc, y + h, sw=0.3, dash="2 1.2")
    s.rect(oc + 36, y + 36, 80, 50, fill="none", stroke="#141414", sw=0.5, dash="2.4 1.3")
    s.rect(oc + 48, y + 28, 12, 8, fill="#141414", stroke="none")
    s.rect(oc + 80, y + 28, 12, 8, fill="#141414", stroke="none")
    s.dim_h(x, x + w, y + h + 14, "4870 mm", y + h, size=2.6)
    s.dim_v(y, y + h, x + w + 12, "1911", x + w, side="right", size=2.5)
    s.text(560, 70, "DASHED OPENING", 2.6, weight="bold")
    s.text(560, 86, "SIZE TBD", 2.4)
    s.text(560, 102, "DO NOT SCALE", 2.4, weight="bold")
    s.text(560, 126, "BLACK PADS", 2.5, weight="bold")
    s.text(560, 142, "HINGE / STRUT", 2.4)
    s.text(560, 158, "ON THE FRAME", 2.4)
    s.text(560, 174, "NOT ON THE SKIN", 2.4, fill="#9b1c1c")
    s.text(560, 198, "INNER LINE INSET", 2.4)
    s.text(560, 214, "IS NOT A CUT DIM", 2.4)
    s.text(18, 400, "OAH ≤ 2500 IS HATCH CLOSED. OPEN LEAF IS PARKED ONLY. SEE H-01.", 2.55, weight="bold")
    s.text(18, 418, "AC CURB IS NOT THIS OPENING. CURB PROVISION IS D-08 AND IS NOT CUT DONE.", 2.55)
    go_pair(s, 18, 448)
    return finish(s)


def sheet_dr01():
    s = new("DR-01", "ENTRY DOOR LEAF — 700 × 1550 FIELD LOCATE", "NTS", 15)
    s.text(18, 22, "CLEAR TARGET 700 × 1550. LEAF OVERALL = THAT OPENING PLUS EDGE OVERLAP TBD. NO OVERLAP mm.", 2.5, weight="bold")
    s.rect(70, 48, 150, 300, fill="#f4f4f4", stroke="#141414", sw=0.6)
    s.rect(86, 64, 118, 268, fill="none", stroke="#141414", sw=0.45, dash="2.4 1.4")
    s.rect(74, 100, 10, 16, fill="#141414", stroke="none")
    s.rect(74, 160, 10, 16, fill="#141414", stroke="none")
    s.rect(74, 230, 10, 16, fill="#141414", stroke="none")
    s.text(96, 180, "CLEAR", 2.4, weight="bold")
    s.text(96, 194, "700 × 1550", 2.3)
    s.text(250, 70, "OUTER RECT = LEAF", 2.5, weight="bold")
    s.text(250, 88, "OVERLAP BAND = TBD", 2.5)
    s.text(250, 106, "NO MILLIMETRE GIVEN", 2.5, fill="#9b1c1c")
    s.text(250, 132, "DASHED = CLEAR OPENING", 2.5, weight="bold")
    s.text(250, 150, "FIELD LOCATE ON P2", 2.5)
    s.text(250, 176, "BLACK PADS = HINGES", 2.5, weight="bold")
    s.text(250, 194, "CENTERS TBD", 2.5)
    s.text(250, 212, "BOLT TO THE JAMB POST", 2.5)
    s.text(250, 230, "FAIL-IF SKIN-ONLY", 2.5, weight="bold", fill="#9b1c1c")
    s.text(250, 256, "LATCH SIDE TBD", 2.5)
    s.text(250, 274, "SEAL PATH IN THE BAND", 2.5)
    s.text(250, 292, "SEAL SECTION TBD", 2.5)
    s.text(18, 420, "DO NOT SCALE THIS LEAF. CUT ONLY AFTER THE OPENING IS FIELD-LOCATED AND THE OVERLAP IS RELEASED.", 2.55)
    go_pair(s, 18, 448)
    return finish(s)


def sheet_dr02():
    s = new("DR-02", "DOOR JAMB IN THE WALL — THRESHOLD WEEP", "NTS", 16)
    s.text(18, 22, "JAMB LANDS ON POSTS AND SILLS. THIS SHEET DOES NOT SET X FROM THE CAB OR Z FROM THE FLOOR.", 2.5, weight="bold")
    s.rect(80, 56, 200, 280, fill="#f7f7f7", stroke="#141414", sw=0.55)
    s.rect(100, 80, 160, 220, fill="none", stroke="#141414", sw=0.45, dash="2.2 1.3")
    s.line(90, 316, 270, 316, sw=0.8)
    s.line(180, 324, 180, 348, sw=0.4)
    s.polygon([(180, 348), (176, 340), (184, 340)], fill="#141414", stroke="none")
    s.text(110, 74, "HEAD — 700+TBD", 2.3, weight="bold")
    s.text(108, 200, "FIELD LOCATE", 2.4, weight="bold")
    s.text(320, 80, "STILES", 2.6, weight="bold")
    s.text(320, 98, "1550 + BUILDUP TBD", 2.4)
    s.text(320, 122, "HEAD AND THRESHOLD", 2.6, weight="bold")
    s.text(320, 140, "700 + BUILDUP TBD", 2.4)
    s.text(320, 164, "DO NOT CUT 1550", 2.4, weight="bold")
    s.text(320, 182, "AS THE STILE.", 2.4)
    s.text(320, 206, "WEEP ARROW", 2.6, weight="bold")
    s.text(320, 224, "DRAINS OUTWARD", 2.4)
    s.text(320, 248, "NOT INTO THE LOFT", 2.4)
    s.text(320, 272, "SEE C-02 FOR THE", 2.4)
    s.text(320, 290, "WALL SYMBOL", 2.4)
    s.text(18, 420, "HINGE REINFORCER IS PL-07 ON THE POST. FAIL-IF THE HINGE IS IN THE SKIN ONLY.", 2.55, weight="bold")
    go_pair(s, 18, 448)
    return finish(s)


def sheet_h01():
    s = new("H-01", "ROOF LOUNGE HATCH LEAF — SIZE INTENT TBD", "NTS", 17)
    s.text(18, 22, "OPENS FORWARD / UP. OAH ≤ 2500 IS THE CLOSED POSITION. OPEN IS PARKED ONLY.", 2.55, weight="bold")
    s.rect(60, 160, 280, 120, fill="#f4f4f4", stroke="#141414", sw=0.55)
    s.rect(90, 184, 160, 70, fill="none", stroke="#141414", sw=0.45, dash="2.2 1.3")
    s.line(90, 184, 200, 70, sw=0.45, dash="2 1.2")
    s.line(250, 184, 300, 90, sw=0.45, dash="2 1.2")
    s.text(70, 310, "CLOSED LEAF ON THE ROOF", 2.4, weight="bold")
    s.text(320, 64, "OPEN LEAF — PARKED ONLY", 2.4, weight="bold")
    s.text(400, 80, "NO LEAF SIZE", 2.7, weight="bold")
    s.text(400, 100, "INTENT TBD", 2.5, fill="#9b1c1c")
    s.text(400, 124, "CONTINUOUS SEAL", 2.5, weight="bold")
    s.text(400, 142, "SECTION TBD", 2.5)
    s.text(400, 166, "HINGE AND STRUT", 2.5, weight="bold")
    s.text(400, 184, "ON THE FRAME F-03", 2.5)
    s.text(400, 202, "NOT ON THE SKIN", 2.5, fill="#9b1c1c")
    s.text(400, 226, "FAIL-IF OPEN CUT", 2.5, weight="bold", fill="#9b1c1c")
    s.text(400, 244, "WITHOUT THE FRAME", 2.5)
    s.text(400, 268, "ROAD = CLOSED", 2.5, weight="bold")
    s.text(18, 420, "DO NOT SCALE THE DASHED OPENING. D-04 GOVERNS THE SEALED FRAME.", 2.55)
    go_pair(s, 18, 448)
    return finish(s)


def sheet_h02():
    s = new("H-02", "REAR LOWER HATCH — SIZE TBD", "NTS", 18)
    s.text(18, 22, "S-06 INTENT. NO CUT SIZE. SEAL REQUIRED. HINGE EDGE IS TBD.", 2.6, weight="bold")
    s.rect(80, 56, 220, 250, fill="#f4f4f4", stroke="#141414", sw=0.55)
    s.rect(110, 180, 150, 80, fill="none", stroke="#141414", sw=0.5, dash="2.4 1.4")
    s.text(120, 210, "INTENT", 2.5, weight="bold")
    s.text(120, 226, "NOT A CUT", 2.4, fill="#9b1c1c")
    s.text(360, 80, "HINGE EDGE TBD", 2.6, weight="bold")
    s.text(360, 100, "DO NOT ASSUME BOTTOM,", 2.4)
    s.text(360, 116, "SIDE, OR TOP.", 2.4)
    s.text(360, 140, "SEAL PATH TBD", 2.6, weight="bold")
    s.text(360, 160, "CONTINUOUS WHEN CLOSED", 2.4)
    s.text(360, 184, "FRAME IS FR-22", 2.5, weight="bold")
    s.text(360, 202, "LENGTHS TBD", 2.4)
    s.text(360, 226, "NOT A ROAD OPENING", 2.5, weight="bold")
    s.text(360, 244, "UNTIL THE SEAL IS IN", 2.4)
    s.text(18, 420, "DO NOT SCALE THE DASHED RECTANGLE. C-05 SHOWS THE SAME RULE ON THE WALL BLANK.", 2.55)
    go_pair(s, 18, 448)
    return finish(s)


def sheet_h03():
    s = new("H-03", "HATCH AND DOOR HARDWARE — ALL TBD", "—", 19)
    s.text(18, 22, "EVERY GRADE, LENGTH, AND COUNT IS UNRELEASED. EMPTY GO = DO NOT BUY AS CUT DONE.", 2.55, weight="bold")
    rows = [
        ["ITEM", "LANDS ON", "QTY", "GRADE", "GO"],
        ["Door hinge", "Jamb post DR-01", "TBD", "TBD", "Eng"],
        ["Door latch", "Stile + jamb", "TBD", "TBD", "Eng"],
        ["Door seal", "Overlap band", "TBD", "TBD", "Eng"],
        ["Lounge hinge", "Hatch frame F-03", "TBD", "TBD", "Eng"],
        ["Lounge strut", "Hatch frame", "TBD", "TBD", "Eng"],
        ["Lounge seal", "Closed perimeter", "TBD", "TBD", "Eng"],
        ["Rear hatch hinge", "FR-22 TBD edge", "TBD", "TBD", "Eng"],
        ["Rear hatch latch", "Frame", "TBD", "TBD", "Eng"],
        ["Gen door hinge", "Bay post D-07", "TBD", "TBD", "Eng"],
        ["AC curb cover", "Curb D-08", "TBD", "TBD", "Eng"],
    ]
    table(s, 16, 40, [150, 180, 50, 60, 50], rows, row_h=22, size=2.45)
    s.text(18, 420, "GEN DOOR AND AC COVER ARE PROVISIONS. THEY DO NOT RELEASE THE UNITS.", 2.55, weight="bold")
    go_pair(s, 18, 448)
    return finish(s)


def sheet_as():
    s = new("AS-01", "ASSEMBLY SEQUENCE — PHASE-1 SHELL", "—", 20)
    s.text(18, 22, "STOP AT EVERY HOLD. A LATER STEP DOES NOT WAIVE AN EARLIER GATE.", 2.6, weight="bold")
    rows = [
        ["STEP", "ACTION", "SHEET", "HOLD"],
        ["01", "Tape bed, rails, cab roof, VIN. Freeze traveler.", "DIMS", "AS-FOUND"],
        ["02", "Cut floor longs 3647. Do not drill.", "C-FR F-01", "ENG section"],
        ["03", "Dry-fit bed-tail splice. Weld after Eng GO.", "J-01", "ENG weld"],
        ["04", "Outriggers from as-found pitch.", "F-01 D-01", "AS-FOUND"],
        ["05", "Drill rails only after Jay GO.", "FS-01", "JAY GO"],
        ["06", "Bolt frame to rails with backing plates.", "C-PL", "JAY GO"],
        ["07", "Stand posts. Cut length = as-found H.", "F-02", "AS-FOUND H"],
        ["08", "Sills and mid posts. Mid count = Eng.", "F-02", "ENG"],
        ["09", "Over-cab ring. Cab roof is not the beam.", "J-01", "ENG"],
        ["10", "Close hatch frame before any roof opening.", "F-03", "D-04"],
        ["11", "Hang skins. Leave dashed openings uncut.", "C-01…C-06", "FIELD"],
        ["12", "Field-locate entry 700×1550 on P2.", "DR-02", "FIELD"],
        ["13", "Door leaf. Hinges to the jamb post.", "DR-01", "ENG"],
        ["14", "Hatch leaves. Sizes still TBD.", "H-01 H-02", "D-04"],
        ["15", "Seal. Hose test.", "QA-01", "HOSE"],
        ["16", "Legs and bumper after D-02 and D-06.", "D-02 D-06", "GATES"],
        ["17", "Gen bay and AC curb provisions only.", "D-07 D-08", "NOT UNITS"],
        ["18", "Weigh. Placard stays blank until then.", "D-02", "WEIGH"],
    ]
    table(s, 16, 34, [40, 340, 110, 100], rows, row_h=18.5, size=2.25)
    s.text(18, 430, "STEP 17 DOES NOT BUY A GENERATOR OR AN AC UNIT. PARKED-ONLY GEN RUN. OPEN HATCH IS PARKED ONLY.", 2.45, weight="bold")
    s.text(18, 448, "OAH ≤ 2500 IS HATCH CLOSED, AND WITH THE CURB INSTALLED IF THAT PROVISION IS BUILT.", 2.45)
    return finish(s)


def sheet_j():
    s = new("J-01", "JOINERY — LOAD IN RAILS AND POSTS, NOT SKIN", "NTS", 21)
    s.text(18, 22, "WELD SIZE TBD. TUBE SECTION TBD. EMPTY ENG GO = DO NOT WELD.", 2.6, weight="bold")
    blocks = [
        (16, 40, "1  BED — TAIL SPLICE", "Two longs in line. Fishplate PL-08 both sides.", "Plate size TBD. Weld size TBD.", "Load stays in the rail line."),
        (420, 40, "2  CAB — OVER-CAB", "Gap and gasket TBD.", "Loft load goes to the posts.", "Cab skin is not the beam."),
        (16, 230, "3  POST TO SILL", "Post lands on the sill.", "Bolt or weld TBD.", "Outer sheet is cladding."),
        (420, 230, "4  ROOF TO WALL", "Roof rail bears on the post head.", "Lap or gasket TBD. No pocket.", "See D-03 before hose test."),
    ]
    for x, y, title, a, b, c in blocks:
        frame(s, x, y, 390, 170, title)
        s.line(x + 24, y + 70, x + 170, y + 70, sw=0.9)
        s.line(x + 90, y + 58, x + 90, y + 82, sw=0.4)
        s.text(x + 190, y + 40, a, 2.35)
        s.text(x + 190, y + 58, b, 2.35)
        s.text(x + 190, y + 76, c, 2.35, weight="bold")
        s.checkbox(x + 190, y + 100, 7, layer="draw")
        s.text(x + 204, y + 106, "ENG GO UNSIGNED", 2.3, weight="bold", fill="#9b1c1c")
    s.text(18, 430, "FAIL-IF ANY OF THESE JOINTS IS MADE IN THE OUTER SKIN ONLY.", 2.6, weight="bold", fill="#9b1c1c")
    s.text(18, 450, "GENERATOR BAY AND AC CURB USE THE SAME RULE: STRUCTURE, NOT SKIN. SEE D-07 AND D-08.", 2.5)
    return finish(s)


def sheet_fs():
    s = new("FS-01", "FASTENER AND HOLE SCHEDULE — ALL TBD", "—", 22)
    s.text(18, 22, "NO DIAMETER, EDGE DISTANCE, TORQUE, OR GRADE IS A RELEASED NUMBER.", 2.6, weight="bold")
    rows = [
        ["SYM", "WHERE", "QTY", "DIA", "EDGE", "TORQUE", "GO"],
        ["H-R", "Rail through outrigger", "TBD", "TBD", "TBD", "TBD", "Jay"],
        ["H-B", "Backing plate PL-01", "TBD", "TBD", "TBD", "TBD", "Jay"],
        ["H-P", "Post to sill", "TBD", "TBD", "TBD", "TBD", "Eng"],
        ["H-H", "Hinge to jamb post", "TBD", "TBD", "TBD", "TBD", "Eng"],
        ["H-S", "Strut to hatch frame", "TBD", "TBD", "TBD", "TBD", "Eng"],
        ["H-L", "Ladder stand-off", "TBD", "TBD", "TBD", "TBD", "Eng"],
        ["H-G", "Leg pad", "TBD", "TBD", "TBD", "TBD", "Eng"],
        ["H-N", "Gen isolator pad", "TBD", "TBD", "TBD", "TBD", "Eng"],
        ["H-C", "AC curb to roof rail", "TBD", "TBD", "TBD", "TBD", "Eng"],
    ]
    table(s, 16, 40, [48, 180, 48, 48, 52, 60, 48], rows, row_h=22, size=2.4)
    s.text(18, 400, "H-H FAIL-IF THE HOLE IS IN THE SKIN ONLY. H-N AND H-C DO NOT RELEASE THE UNITS.", 2.55, weight="bold")
    s.text(18, 420, "H-R AND H-B: UNSIGNED JAY GO = DO NOT DRILL THE RAIL.", 2.55, fill="#9b1c1c")
    go_pair(s, 18, 448)
    return finish(s)


def sheet_mat():
    s = new("MAT-01", "MATERIAL SCHEDULE — THICKNESS AND GRADE TBD", "—", 23)
    s.text(18, 22, "EMPTY ENG GO = THE LINE IS NOT RELEASED. DO NOT SUBSTITUTE A BRAND.", 2.6, weight="bold")
    rows = [
        ["LINE", "ROLE", "THICKNESS", "GRADE", "GO"],
        ["Outer skin", "Weather face", "TBD", "TBD", "Eng"],
        ["Core", "If a sandwich is used", "TBD", "TBD", "Eng"],
        ["Inner skin", "Liner", "TBD", "TBD", "Eng"],
        ["Frame tube", "F-00 members", "TBD", "TBD", "Eng"],
        ["Angle / sill", "Open shapes", "TBD", "TBD", "Eng"],
        ["Plate", "C-PL", "TBD", "TBD", "Eng"],
        ["Sealant", "Joints D-03", "TBD", "TBD", "Eng"],
        ["Weatherstrip", "Door and hatches", "TBD", "TBD", "Eng"],
        ["Isolation", "Dissimilar metals", "TBD", "TBD", "Eng"],
        ["Fastener", "FS-01", "TBD", "TBD", "Eng"],
    ]
    table(s, 16, 40, [110, 180, 90, 70, 50], rows, row_h=22, size=2.4)
    s.text(18, 420, "NO SANDWICH BRAND. NO BOLT GRADE. NO WELD FILLER SPEC. PHASE-2 UNITS ARE NOT MATERIALS ON THIS SHEET.", 2.45, weight="bold")
    return finish(s)


def sheet_bom():
    s = new("BOM-01", "PHASE-1 BOM — UNITS ARE HOOKS ONLY", "—", 24)
    s.text(18, 22, "A ROW MARKED HOOK IS NOT FAB DONE AND NOT A PURCHASE RELEASE.", 2.6, weight="bold")
    rows = [
        ["ITEM", "QTY", "SHEET", "STATUS"],
        ["P1 floor blank", "1", "C-01", "Splice TBD"],
        ["P2 / P3 walls", "1 + 1", "C-02 C-03", "H estimate"],
        ["P4 flats A–E", "5", "C-04", "Estimates"],
        ["P5 rear", "1", "C-05", "Openings TBD"],
        ["P6 roof", "1", "C-06", "Splice TBD"],
        ["Frame FR-01…FR-22", "See C-FR", "C-FR", "Section TBD"],
        ["Plates PL-01…PL-08", "TBD", "C-PL", "Holes TBD"],
        ["Door leaf + jamb", "1", "DR-01 DR-02", "Overlap TBD"],
        ["Lounge hatch leaf", "1", "H-01", "Size TBD"],
        ["Rear hatch leaf", "1", "H-02", "Size TBD"],
        ["Hardware", "TBD", "H-03 FS-01", "Not released"],
        ["Gen bay provision", "1", "D-07", "NOT THE UNIT"],
        ["AC curb provision", "1", "D-08", "NOT THE UNIT"],
        ["Generator unit", "—", "D-07", "HOOK ONLY"],
        ["AC unit", "—", "D-08", "HOOK ONLY"],
        ["Solar / awning / seats", "—", "S-07 S-08", "HOOK ONLY"],
    ]
    table(s, 16, 34, [180, 80, 120, 140], rows, row_h=20.5, size=2.35)
    return finish(s)


def sheet_qa():
    s = new("QA-01", "SHOP QA AND HOSE TEST — FAIL-IF", "—", 25)
    s.text(18, 22, "ANY FAIL STOPS THE CLAIM. DO NOT SIGN PAST AN OPEN GATE.", 2.6, weight="bold")
    rows = [
        ["CHECK", "FAIL-IF", "SHEET"],
        ["Cabin dry", "Wet cabin after the hose", "D-03"],
        ["Roof opening", "Open cut without a sealed frame", "F-03 D-04"],
        ["Mounts", "Skin-only hinge, curb, or bay", "DR-01 D-07 D-08"],
        ["Length", "A second overall length on a cut sheet", "DIMS"],
        ["Photo scale", "Anyone cuts to the photo study", "reference/"],
        ["Ladder", "Ladder used as a jack or a lift", "D-05"],
        ["Hatch road", "Hatch open on the road", "H-01"],
        ["Gen exhaust", "Exhaust or CO in lounge or cabin", "D-07"],
        ["Gen mass", "Mass on +1000 skin, or no legs", "D-07"],
        ["Glands", "Wet glands at fill, bumper, or bay", "D-06 D-07"],
        ["Rail drill", "Hole in the rail without Jay GO", "D-01"],
        ["AC water", "Condensate into cabin or lounge", "D-08"],
        ["AC road", "Open curb on the road", "D-08"],
        ["kg", "A number written before the weigh", "D-02"],
    ]
    table(s, 16, 36, [90, 320, 120], rows, row_h=22, size=2.35)
    s.text(18, 430, "HOSE THE CLOSED HATCH, THE CLOSED CURB, AND THE BED-TAIL JOINT BEFORE ANY OCCUPANCY CLAIM.", 2.5, weight="bold")
    return finish(s)


BUILDERS = [
    ("CVR-00_cover", sheet_cvr, ROOT),
    ("C-00_nest_index", sheet_c00, ROOT),
    ("C-01_p1_floor", sheet_c01, ROOT),
    ("C-02_p2_lh", sheet_c02, ROOT),
    ("C-03_p3_rh", sheet_c03, ROOT),
    ("C-04_p4_overcab", sheet_c04, ROOT),
    ("C-05_p5_rear", sheet_c05, ROOT),
    ("C-06_p6_roof", sheet_c06, ROOT),
    ("C-FR_frame_cut_list", sheet_cfr, ROOT),
    ("C-PL_mount_plates", sheet_cpl, ROOT),
    ("frame/F-00_index", sheet_f00, ROOT),
    ("frame/F-01_floor", sheet_f01, ROOT),
    ("frame/F-02_posts", sheet_f02, ROOT),
    ("frame/F-03_roof_ring", sheet_f03, ROOT),
    ("door/DR-01_leaf", sheet_dr01, ROOT),
    ("door/DR-02_jamb", sheet_dr02, ROOT),
    ("hatch/H-01_lounge", sheet_h01, ROOT),
    ("hatch/H-02_rear", sheet_h02, ROOT),
    ("hatch/H-03_hardware", sheet_h03, ROOT),
    ("shop/AS-01_sequence", sheet_as, ROOT),
    ("shop/J-01_joinery", sheet_j, ROOT),
    ("shop/FS-01_fasteners", sheet_fs, ROOT),
    ("shop/MAT-01_materials", sheet_mat, ROOT),
    ("shop/BOM-01_phase1", sheet_bom, ROOT),
    ("shop/QA-01_hose", sheet_qa, ROOT),
]


def write_dxf():
    dxf_dir = ROOT / "dxf"
    dxf_dir.mkdir(parents=True, exist_ok=True)
    profiles = {
        "C-01_p1_floor": (3647, 1911, "CUT envelope. Edge allowance TBD. No openings."),
        "C-02_p2_lh": (3647, 1830, "ESTIMATE height. Openings are NOT in this DXF."),
        "C-03_p3_rh": (3647, 1830, "ESTIMATE height. No entry. Openings NOT in this DXF."),
        "C-05_p5_rear": (1911, 1830, "ESTIMATE height. Hatches NOT in this DXF."),
        "C-06_p6_roof": (4870, 1911, "Envelope only. Lounge hatch NOT in this DXF."),
        "C-04_p4a_loft_floor": (1911, 1223, "ESTIMATE. Not a developed blank."),
        "C-04_p4c_front": (1911, 1830, "ESTIMATE height."),
    }
    for name, (length, width, note) in profiles.items():
        ents = ["0", "SECTION", "2", "ENTITIES"]
        pts = [(0, 0), (length, 0), (length, width), (0, width)]
        for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
            ents += [
                "0", "LINE", "8", "ENVELOPE",
                "10", str(x1), "20", str(y1), "30", "0",
                "11", str(x2), "21", str(y2), "31", "0",
            ]
        ents += [
            "0", "TEXT", "8", "NOTE", "10", "0", "20", str(width + 40), "30", "0",
            "40", "40", "1", note,
        ]
        body = ["0", "SECTION", "2", "HEADER", "9", "$INSUNITS", "70", "4", "0", "ENDSEC"]
        body += ents + ["0", "ENDSEC", "0", "EOF"]
        (dxf_dir / f"{name}.dxf").write_text("\n".join(body) + "\n", encoding="utf-8")


def main():
    banned = ("5942", "1912", "1215", "2342", "10.9", "8.8", "1025", "1110", "780×1550", "780 x 1550")
    failed = False
    for name, builder, _base in BUILDERS:
        sheet = builder()
        errors = []
        # QA from sheetlib checks collisions. Import lazily to keep the name.
        from sheetlib import qa_sheet

        errors.extend(qa_sheet(sheet))
        svg = sheet.to_svg()
        blob = "\n".join(__import__("re").findall(r">([^<]*)</text>", svg))
        for token in banned:
            if token in blob:
                errors.append(f"banned {token}")
        if "PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED" not in svg:
            errors.append("missing watermark")
        if "JAY GO" not in svg:
            errors.append("missing Jay GO")
        if errors:
            failed = True
            print(f"\n== {sheet.sid} {len(errors)} ==")
            for e in errors[:25]:
                print(" -", e)
        else:
            print(f"{sheet.sid} QA clean")
        dest = ROOT / f"{name}.svg"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(svg, encoding="utf-8")
        png = dest.with_suffix(".png")
        cairosvg.svg2png(url=str(dest), write_to=str(png), output_width=3364, output_height=2376)
    write_dxf()
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
