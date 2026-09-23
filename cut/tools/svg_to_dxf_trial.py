#!/usr/bin/env python3
"""Export as-drawn SVG sheet geometry to a minimal mm DXF.

Matches the hand-written DXF header used by write_dxf() in this folder
($INSUNITS = 4). Reads viewBox units as millimetres when the SVG width/height
are the same numbers with a mm suffix. Does not rescale symbols to SoR text.

Text stays DXF TEXT. It is not exploded to paths.
Stroke-only geometry stays on AS-DRAWN or DASHED. Fill-only symbols stay on
FILL. A stamp on STAMP marks the file CONDITIONAL inventory, not CUT-READY.

This is a trial exporter. It does not release a cut profile.
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DXF_DIR = ROOT / "dxf"

SOURCES = [
    ROOT / "C-FR_frame_cut_list.svg",
    ROOT / "C-PL_mount_plates.svg",
    ROOT / "door" / "DR-01_leaf.svg",
    ROOT / "door" / "DR-02_jamb.svg",
    ROOT / "hatch" / "H-01_lounge.svg",
    ROOT / "hatch" / "H-02_rear.svg",
    ROOT / "C-04_p4_overcab.svg",
]

# Part-scale figures that must not appear as invented line lengths.
FORBIDDEN_LENGTHS = (
    Decimal("3647"),
    Decimal("1911"),
    Decimal("4870"),
    Decimal("1550"),
    Decimal("1223"),
    Decimal("1830"),
    Decimal("2647"),
    Decimal("700"),
)

STAMP = (
    "CONDITIONAL INVENTORY - NOT CUT-READY",
    "AS-DRAWN A1 SHEET mm. NOT PART SCALE. UNDEVELOPED / NTS WHERE THE SVG SAYS SO.",
    "DO NOT PLASMA. PRELIMINARY - VERIFY ON VEHICLE - NOT LTO-CERTIFIED.",
)

ASCII_FOLD = str.maketrans(
    {
        "×": "x",
        "—": "-",
        "–": "-",
        "≈": "~",
        "·": ".",
        "≤": "<=",
        "…": "...",
    }
)


def local(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def dec(value: str | None, default: str = "0") -> Decimal:
    if value is None or value == "":
        return Decimal(default)
    return Decimal(value)


def fmt(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.01")), "f")


def fold_text(value: str) -> str:
    folded = " ".join(value.translate(ASCII_FOLD).split())
    if len(folded) > 250:
        raise ValueError(f"TEXT longer than 250 chars: {folded[:40]}...")
    return folded


def parse_mm_size(raw: str | None) -> Decimal | None:
    if raw is None:
        return None
    text = raw.strip()
    if not text.endswith("mm"):
        return None
    return Decimal(text[:-2])


def parse_viewbox(raw: str) -> tuple[Decimal, Decimal, Decimal, Decimal]:
    parts = raw.replace(",", " ").split()
    if len(parts) != 4:
        raise ValueError(f"viewBox is not 4 numbers: {raw}")
    min_x, min_y, width, height = (Decimal(part) for part in parts)
    return min_x, min_y, width, height


def stroke_layer(el: ET.Element) -> str | None:
    stroke = el.get("stroke")
    if stroke is None or stroke == "none":
        return None
    if el.get("stroke-dasharray"):
        return "DASHED"
    return "AS-DRAWN"


def is_page_fill(el: ET.Element, vb_w: Decimal, vb_h: Decimal) -> bool:
    if stroke_layer(el) is not None:
        return False
    width = dec(el.get("width"))
    height = dec(el.get("height"))
    return width >= vb_w - 1 and height >= vb_h - 1


class Entities:
    def __init__(self) -> None:
        self.lines: list[tuple[str, Decimal, Decimal, Decimal, Decimal]] = []
        self.circles: list[tuple[str, Decimal, Decimal, Decimal]] = []
        self.texts: list[tuple[str, Decimal, Decimal, Decimal, str, str]] = []

    def line(self, layer: str, x1: Decimal, y1: Decimal, x2: Decimal, y2: Decimal) -> None:
        self.lines.append((layer, x1, y1, x2, y2))

    def rect(self, layer: str, x: Decimal, y: Decimal, w: Decimal, h: Decimal) -> None:
        self.line(layer, x, y, x + w, y)
        self.line(layer, x + w, y, x + w, y + h)
        self.line(layer, x + w, y + h, x, y + h)
        self.line(layer, x, y + h, x, y)

    def circle(self, layer: str, cx: Decimal, cy: Decimal, r: Decimal) -> None:
        self.circles.append((layer, cx, cy, r))

    def text(self, layer: str, x: Decimal, y: Decimal, height: Decimal, value: str, anchor: str) -> None:
        self.texts.append((layer, x, y, height, value, anchor))


def add_polygon(ents: Entities, layer: str, el: ET.Element) -> None:
    raw = el.get("points") or ""
    nums = raw.replace(",", " ").split()
    if len(nums) < 4 or len(nums) % 2:
        raise ValueError(f"polygon points are not pairs: {raw}")
    pts = [(Decimal(nums[i]), Decimal(nums[i + 1])) for i in range(0, len(nums), 2)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        ents.line(layer, x1, y1, x2, y2)


def collect(svg: ET.Element, vb_w: Decimal, vb_h: Decimal) -> Entities:
    ents = Entities()
    for el in svg.iter():
        if el.get("transform"):
            raise ValueError(f"transform present on <{local(el.tag)}>; not exported")
        name = local(el.tag)
        if name == "path":
            raise ValueError("path present; text-as-paths / path geometry is not exported")
        if name == "rect":
            if is_page_fill(el, vb_w, vb_h):
                continue
            layer = stroke_layer(el) or "FILL"
            ents.rect(layer, dec(el.get("x")), dec(el.get("y")), dec(el.get("width")), dec(el.get("height")))
        elif name == "line":
            layer = stroke_layer(el) or "FILL"
            ents.line(layer, dec(el.get("x1")), dec(el.get("y1")), dec(el.get("x2")), dec(el.get("y2")))
        elif name == "circle":
            layer = stroke_layer(el) or "FILL"
            ents.circle(layer, dec(el.get("cx")), dec(el.get("cy")), dec(el.get("r")))
        elif name == "polygon":
            layer = stroke_layer(el) or "FILL"
            add_polygon(ents, layer, el)
        elif name == "polyline":
            raise ValueError("polyline present; not exported")
        elif name == "text":
            value = fold_text("".join(el.itertext()))
            if not value:
                continue
            anchor = el.get("text-anchor") or "start"
            if anchor not in ("start", "middle", "end"):
                raise ValueError(f"unsupported text-anchor {anchor}")
            ents.text("ANNOTATION", dec(el.get("x")), dec(el.get("y")), dec(el.get("font-size"), "2.5"), value, anchor)
    return ents


def flip_y(ents: Entities, height: Decimal) -> Entities:
    flipped = Entities()
    for layer, x1, y1, x2, y2 in ents.lines:
        flipped.line(layer, x1, height - y1, x2, height - y2)
    for layer, cx, cy, r in ents.circles:
        flipped.circle(layer, cx, height - cy, r)
    for layer, x, y, size, value, anchor in ents.texts:
        flipped.text(layer, x, height - y, size, value, anchor)
    return flipped


def dxf_text(layer: str, x: Decimal, y: Decimal, height: Decimal, value: str, anchor: str) -> list[str]:
    halign = {"start": "0", "middle": "1", "end": "2"}[anchor]
    body = [
        "0", "TEXT",
        "8", layer,
        "10", fmt(x),
        "20", fmt(y),
        "30", "0",
        "40", fmt(height),
        "1", value,
        "72", halign,
    ]
    if halign != "0":
        body += ["11", fmt(x), "21", fmt(y), "31", "0"]
    return body


def write_dxf(path: Path, height: Decimal, ents: Entities) -> None:
    body = [
        "999",
        "CONDITIONAL INVENTORY - NOT CUT-READY - AS-DRAWN SHEET mm - NOT PART SCALE",
        "0", "SECTION",
        "2", "HEADER",
        "9", "$INSUNITS",
        "70", "4",
        "0", "ENDSEC",
        "0", "SECTION",
        "2", "ENTITIES",
    ]
    for index, line in enumerate(STAMP):
        y = height + Decimal(8) + Decimal(index) * Decimal(6)
        body += dxf_text("STAMP", Decimal("12"), y, Decimal("3.50"), line, "start")
    for layer, x1, y1, x2, y2 in ents.lines:
        body += [
            "0", "LINE",
            "8", layer,
            "10", fmt(x1),
            "20", fmt(y1),
            "30", "0",
            "11", fmt(x2),
            "21", fmt(y2),
            "31", "0",
        ]
    for layer, cx, cy, r in ents.circles:
        body += [
            "0", "CIRCLE",
            "8", layer,
            "10", fmt(cx),
            "20", fmt(cy),
            "30", "0",
            "40", fmt(r),
        ]
    for layer, x, y, size, value, anchor in ents.texts:
        body += dxf_text(layer, x, y, size, value, anchor)
    body += ["0", "ENDSEC", "0", "EOF"]
    path.write_text("\n".join(body) + "\n", encoding="ascii")


def line_length(x1: Decimal, y1: Decimal, x2: Decimal, y2: Decimal) -> Decimal:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2).sqrt()


def content_rects(ents: Entities) -> list[tuple[Decimal, Decimal]]:
    """Unique stroked width x height pairs, excluding the A1 border."""
    found: list[tuple[Decimal, Decimal]] = []
    horizontals = [
        (layer, x1, y1, x2, y2)
        for layer, x1, y1, x2, y2 in ents.lines
        if y1 == y2 and layer in ("AS-DRAWN", "DASHED")
    ]
    verticals = [
        (layer, x1, y1, x2, y2)
        for layer, x1, y1, x2, y2 in ents.lines
        if x1 == x2 and layer in ("AS-DRAWN", "DASHED")
    ]
    for layer, x1, y, x2, _y in horizontals:
        width = abs(x2 - x1)
        left, right = min(x1, x2), max(x1, x2)
        heights: list[Decimal] = []
        for vlayer, vx, vy1, _vx, vy2 in verticals:
            if vlayer != layer or vx not in (left, right):
                continue
            if min(vy1, vy2) == y or max(vy1, vy2) == y:
                heights.append(abs(vy2 - vy1))
        for height in heights:
            if height == 0 or width == 0 or width >= 800 or height >= 500:
                continue
            pair = (width, height)
            if pair not in found:
                found.append(pair)
    return found


def forbidden_hits(ents: Entities) -> list[str]:
    hits: list[str] = []
    for layer, x1, y1, x2, y2 in ents.lines:
        length = line_length(x1, y1, x2, y2)
        for banned in FORBIDDEN_LENGTHS:
            if abs(length - banned) <= Decimal("0.5"):
                hits.append(f"{layer} line {fmt(length)} mm ~= {banned}")
    return hits


def export_one(src: Path) -> str:
    tree = ET.parse(src)
    svg = tree.getroot()
    if local(svg.tag) != "svg":
        raise ValueError("root is not svg")
    min_x, min_y, vb_w, vb_h = parse_viewbox(svg.get("viewBox") or "")
    width_mm = parse_mm_size(svg.get("width"))
    height_mm = parse_mm_size(svg.get("height"))
    if min_x != 0 or min_y != 0:
        raise ValueError("viewBox origin is not 0 0")
    if width_mm != vb_w or height_mm != vb_h:
        raise ValueError(
            f"mm size {width_mm}x{height_mm} does not match viewBox {vb_w}x{vb_h}"
        )
    raw = collect(svg, vb_w, vb_h)
    flipped = flip_y(raw, vb_h)
    hits = forbidden_hits(flipped)
    if hits:
        raise ValueError("part-scale length appeared in geometry: " + "; ".join(hits))
    dest = DXF_DIR / f"{src.stem}.dxf"
    write_dxf(dest, vb_h, flipped)
    stamp_ok = "CONDITIONAL INVENTORY - NOT CUT-READY" in dest.read_text(encoding="ascii")
    insunits_ok = "\n9\n$INSUNITS\n70\n4\n" in dest.read_text(encoding="ascii")
    if not stamp_ok or not insunits_ok:
        raise ValueError("written DXF failed stamp or $INSUNITS check")
    rects = content_rects(flipped)
    rect_note = ", ".join(f"{fmt(w)}x{fmt(h)}" for w, h in rects[:8]) or "(none)"
    return (
        f"{src.relative_to(ROOT)} -> dxf/{dest.name} | "
        f"units mm viewBox {fmt(vb_w)}x{fmt(vb_h)} | "
        f"LINE {len(flipped.lines)} CIRCLE {len(flipped.circles)} TEXT {len(flipped.texts)} | "
        f"content spans {rect_note} | "
        f"part-scale lengths absent"
    )


def main() -> int:
    DXF_DIR.mkdir(parents=True, exist_ok=True)
    failed = False
    for src in SOURCES:
        try:
            print(export_one(src))
        except (ET.ParseError, OSError, UnicodeEncodeError, ValueError) as exc:
            failed = True
            print(f"BLOCKED {src.name}: {exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
