"""Millimetre drawing sheet helpers for the Tamaraw Phase-1 shell pack.

viewBox units are millimetres on an A1 landscape sheet (841 × 594).
"""

from __future__ import annotations

import html
import math

from PIL import ImageFont

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

SHEET_W = 841.0
SHEET_H = 594.0
TITLE_TOP = 506.0

# DejaVu Sans at 100 px: ascent 93, descent 24.
ASCENT = 0.93
DESCENT = 0.24


def esc(text: str) -> str:
    return html.escape(text, quote=True)


class Sheet:
    def __init__(self, sid: str, title: str, scale_label: str, sheet_no: int, sheet_count: int = 15):
        self.sid = sid
        self.title = title
        self.scale_label = scale_label
        self.sheet_no = sheet_no
        self.sheet_count = sheet_count
        self.W = SHEET_W
        self.H = SHEET_H
        self.nodes: list[str] = []
        self.texts: list[dict] = []
        self.segs: list[tuple] = []
        self.font = ImageFont.truetype(FONT_PATH, 100)
        self.font_b = ImageFont.truetype(FONTB_PATH, 100)
        self.defs: list[str] = []

    def text_width(self, text: str, size: float, weight: str = "normal") -> float:
        font = self.font_b if weight == "bold" else self.font
        return font.getlength(text) * (size / 100.0)

    def glyph_box(self, x: float, y: float, text: str, size: float, anchor: str, rotate: float, weight: str) -> tuple[float, float, float, float]:
        w = self.text_width(text, size, weight)
        asc = ASCENT * size
        desc = DESCENT * size
        if anchor == "middle":
            dx0, dx1 = -w / 2.0, w / 2.0
        elif anchor == "end":
            dx0, dx1 = -w, 0.0
        else:
            dx0, dx1 = 0.0, w
        dy0, dy1 = -asc, desc
        corners = [(dx0, dy0), (dx1, dy0), (dx0, dy1), (dx1, dy1)]
        if abs(rotate) < 0.1:
            pts = [(x + dx, y + dy) for dx, dy in corners]
        elif abs(rotate + 90) < 0.1:
            # SVG rotate(-90): (dx, dy) -> (dy, -dx) relative to anchor
            pts = [(x + dy, y - dx) for dx, dy in corners]
        else:
            raise ValueError(f"unsupported rotate {rotate}")
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        return (min(xs), min(ys), max(xs), max(ys))

    def add_text(self, x, y, text, size, anchor="start", weight="normal", fill="#141414", rotate=0.0, layer="draw") -> tuple:
        box = self.glyph_box(x, y, text, size, anchor, rotate, weight)
        self.texts.append({"text": text, "box": box, "layer": layer, "x": x, "y": y})
        rot = ""
        if abs(rotate) > 0.1:
            rot = f' transform="rotate({rotate:g} {x:.2f} {y:.2f})"'
        weight_attr = ' font-weight="bold"' if weight == "bold" else ""
        self.nodes.append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size:.2f}" text-anchor="{anchor}" '
            f'fill="{fill}"{weight_attr}{rot}>{esc(text)}</text>'
        )
        return box

    def text(self, x, y, text, size=3.2, anchor="start", weight="normal", fill="#141414", rotate=0.0, layer="draw"):
        return self.add_text(x, y, text, size, anchor, weight, fill, rotate, layer)

    def line(self, x1, y1, x2, y2, sw=0.35, stroke="#141414", dash=None, layer="geom"):
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.nodes.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{stroke}" stroke-width="{sw}" fill="none"{dash_attr}/>'
        )
        self.segs.append((x1, y1, x2, y2, layer))

    def polyline(self, pts, sw=0.35, stroke="#141414", dash=None, layer="geom"):
        if len(pts) < 2:
            return
        d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.nodes.append(
            f'<polyline points="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{dash_attr}/>'
        )
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            self.segs.append((x1, y1, x2, y2, layer))

    def polygon(self, pts, fill="none", stroke="#141414", sw=0.5, dash=None, layer="geom"):
        d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.nodes.append(
            f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="miter"{dash_attr}/>'
        )
        if stroke and stroke != "none":
            for i, (x1, y1) in enumerate(pts):
                x2, y2 = pts[(i + 1) % len(pts)]
                self.segs.append((x1, y1, x2, y2, layer))

    def rect(self, x, y, w, h, fill="none", stroke="#141414", sw=0.35, dash=None, layer="geom"):
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        stroke_attr = stroke if stroke else "none"
        self.nodes.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'fill="{fill}" stroke="{stroke_attr}" stroke-width="{sw}"{dash_attr}/>'
        )
        if stroke and stroke != "none":
            self.segs.append((x, y, x + w, y, layer))
            self.segs.append((x + w, y, x + w, y + h, layer))
            self.segs.append((x + w, y + h, x, y + h, layer))
            self.segs.append((x, y + h, x, y, layer))

    def circle(self, cx, cy, r, fill="none", stroke="#141414", sw=0.4, dash=None, layer="geom"):
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.nodes.append(
            f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{dash_attr}/>'
        )
        if stroke and stroke != "none" and r > 0:
            # QA approximation of the circumference.
            n = 24
            for i in range(n):
                a1 = 2 * math.pi * i / n
                a2 = 2 * math.pi * (i + 1) / n
                self.segs.append((cx + r * math.cos(a1), cy + r * math.sin(a1), cx + r * math.cos(a2), cy + r * math.sin(a2), layer))

    def arrow_h(self, tip_x, y, direction, layer="dim"):
        length, half = 2.6, 0.85
        tail = tip_x - direction * length
        self.polygon([(tip_x, y), (tail, y - half), (tail, y + half)], fill="#141414", stroke="none", layer=layer)

    def arrow_v(self, x, tip_y, direction, layer="dim"):
        """direction -1 points up (toward smaller y), +1 points down."""
        length, half = 2.6, 0.85
        tail = tip_y - direction * length
        self.polygon([(x, tip_y), (x - half, tail), (x + half, tail)], fill="#141414", stroke="none", layer=layer)

    def vline_gap(self, x, y0, y1, sw=0.25, layer="dim", pad=0.9):
        if y1 < y0:
            y0, y1 = y1, y0
        blocks = []
        for t in self.texts:
            if t["layer"] == "frame":
                continue
            bx0, by0, bx1, by1 = t["box"]
            if x < bx0 - pad or x > bx1 + pad:
                continue
            blocks.append((by0 - pad, by1 + pad))
        blocks.sort()
        merged = []
        for a, b in blocks:
            if not merged or a > merged[-1][1]:
                merged.append([a, b])
            else:
                merged[-1][1] = max(merged[-1][1], b)
        y = y0
        for a, b in merged:
            if b < y0 or a > y1:
                continue
            if a > y + 0.8:
                self.line(x, y, x, min(a, y1), sw=sw, layer=layer)
            y = max(y, b)
        if y1 > y + 0.8:
            self.line(x, y, x, y1, sw=sw, layer=layer)

    def hline_gap(self, y, x0, x1, sw=0.25, layer="dim", pad=0.9):
        if x1 < x0:
            x0, x1 = x1, x0
        blocks = []
        for t in self.texts:
            if t["layer"] == "frame":
                continue
            bx0, by0, bx1, by1 = t["box"]
            if y < by0 - pad or y > by1 + pad:
                continue
            blocks.append((bx0 - pad, bx1 + pad))
        blocks.sort()
        merged = []
        for a, b in blocks:
            if not merged or a > merged[-1][1]:
                merged.append([a, b])
            else:
                merged[-1][1] = max(merged[-1][1], b)
        x = x0
        for a, b in merged:
            if b < x0 or a > x1:
                continue
            if a > x + 0.8:
                self.line(x, y, min(a, x1), y, sw=sw, layer=layer)
            x = max(x, b)
        if x1 > x + 0.8:
            self.line(x, y, x1, y, sw=sw, layer=layer)

    def dim_h(self, x1, x2, y, label, ext_y, size=3.15):
        if x2 < x1:
            x1, x2 = x2, x1
        w = self.text_width(label, size)
        baseline = y - (DESCENT * size + 1.35)
        cx = self._place_h(x1, x2, baseline, label, size, w)
        self.text(cx, baseline, label, size, anchor="middle", layer="draw")
        gap_l = cx - w / 2.0 - 1.1
        gap_r = cx + w / 2.0 + 1.1
        if gap_l - x1 > 3:
            self.line(x1, y, gap_l, y, sw=0.28, layer="dim")
        if x2 - gap_r > 3:
            self.line(gap_r, y, x2, y, sw=0.28, layer="dim")
        self.arrow_h(x1, y, -1)
        self.arrow_h(x2, y, 1)
        # Extension lines stop 1.2 mm short of the feature and run 1.6 mm past the dim line.
        if ext_y < y:
            self.vline_gap(x1, ext_y + 1.2, y + 1.6, sw=0.22)
            self.vline_gap(x2, ext_y + 1.2, y + 1.6, sw=0.22)
        else:
            self.vline_gap(x1, y - 1.6, ext_y - 1.2, sw=0.22)
            self.vline_gap(x2, y - 1.6, ext_y - 1.2, sw=0.22)

    def _place_h(self, x1, x2, baseline, label, size, w) -> float:
        box_at = lambda cx: self.glyph_box(cx, baseline, label, size, "middle", 0.0, "normal")
        center = (x1 + x2) / 2.0
        candidates = [center]
        span_left = min(x1, x2) + w / 2.0 + 2.0
        span_right = max(x1, x2) - w / 2.0 - 2.0
        if span_right > span_left:
            x = span_left
            while x <= span_right:
                candidates.append(x)
                x += 4.0
        else:
            # Label wider than the dimension: scan a wider window.
            x = center - 80
            while x <= center + 80:
                candidates.append(x)
                x += 4.0
        best_cx = center
        best_score = None
        for cx in candidates:
            box = box_at(cx)
            if box[0] < 12 or box[2] > self.W - 12 or box[1] < 12 or box[3] > TITLE_TOP - 2:
                continue
            score = self._overlap_score(box)
            score += abs(cx - center) * 0.002
            if best_score is None or score < best_score:
                best_score = score
                best_cx = cx
        return best_cx

    def dim_v(self, y1, y2, x, label, ext_x, size=3.15, side="right"):
        if y2 < y1:
            y1, y2 = y2, y1
        w = self.text_width(label, size)
        cy = (y1 + y2) / 2.0
        asc = ASCENT * size
        desc = DESCENT * size
        if side == "right":
            anchor_x = x + 1.5 + asc
        else:
            anchor_x = x - 1.5 - desc
        # Nudge along the dimension if the label would collide.
        cy = self._place_v(y1, y2, anchor_x, label, size, w, cy)
        self.text(anchor_x, cy, label, size, anchor="middle", rotate=-90, layer="draw")
        # Broken dimension line around the rotated label's vertical span.
        half = w / 2.0 + 1.2
        if cy - half - y1 > 3:
            self.line(x, y1, x, cy - half, sw=0.28, layer="dim")
        if y2 - (cy + half) > 3:
            self.line(x, cy + half, x, y2, sw=0.28, layer="dim")
        self.arrow_v(x, y1, -1)
        self.arrow_v(x, y2, 1)
        if ext_x < x:
            self.hline_gap(y1, ext_x + 1.2, x + 1.6, sw=0.22)
            self.hline_gap(y2, ext_x + 1.2, x + 1.6, sw=0.22)
        else:
            self.hline_gap(y1, x - 1.6, ext_x - 1.2, sw=0.22)
            self.hline_gap(y2, x - 1.6, ext_x - 1.2, sw=0.22)

    def _place_v(self, y1, y2, anchor_x, label, size, w, cy0) -> float:
        best_cy = cy0
        best_score = None
        ys = [cy0]
        y = y1 + w / 2.0 + 2
        while y < y2 - w / 2.0 - 2:
            ys.append(y)
            y += 4
        if len(ys) == 1:
            ys = [cy0]
        for cy in ys:
            box = self.glyph_box(anchor_x, cy, label, size, "middle", -90, "normal")
            if box[0] < 8 or box[2] > self.W - 8 or box[1] < 12 or box[3] > TITLE_TOP - 2:
                continue
            score = self._overlap_score(box) + abs(cy - cy0) * 0.002
            if best_score is None or score < best_score:
                best_score = score
                best_cy = cy
        return best_cy

    def _overlap_score(self, box) -> float:
        score = 0.0
        gap = 0.8
        for t in self.texts:
            if t["layer"] == "frame":
                continue
            if _boxes_overlap(box, t["box"], gap):
                score += 20.0 + _overlap_area(box, t["box"])
        for x1, y1, x2, y2, layer in self.segs:
            if layer == "frame":
                continue
            if _seg_hits_rect(x1, y1, x2, y2, _expand(box, gap)):
                score += 8.0
        return score

    def leader(self, x1, y1, x2, y2, label, size=3.1, anchor="start", side_dx=0.0):
        """Orthogonal-looking straight leader. Label sits past (x2, y2)."""
        self.circle(x1, y1, 0.9, fill="#141414", stroke="none", layer="dim")
        self.line(x1, y1, x2, y2, sw=0.28, layer="dim")
        tx = x2 + (1.6 if anchor != "end" else -1.6) + side_dx
        # Place text so its box clears the leader endpoint.
        baseline = y2 - 0.4
        self.text(tx, baseline, label, size, anchor=anchor, layer="draw")

    def checkbox(self, x, y, side=5.5, layer="frame"):
        self.rect(x, y, side, side, fill="#ffffff", stroke="#141414", sw=0.4, layer=layer)

    def title_block(self):
        x0, y0, w, h = 10, TITLE_TOP, 821, 78
        self.rect(x0, y0, w, h, fill="#ffffff", stroke="#141414", sw=0.6, layer="frame")
        self.line(640, y0, 640, y0 + h, sw=0.4, layer="frame")
        self.line(748, y0, 748, y0 + h, sw=0.4, layer="frame")
        self.text(18, 522, "KE-Texh / TAMARAW  ·  PHASE-1 SHELL", 3.7, weight="bold", layer="frame")
        self.text(18, 535, f"{self.sid}   {self.title}", 3.15, layer="frame")
        self.text(
            18,
            550,
            "PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED",
            3.35,
            weight="bold",
            fill="#9b1c1c",
            layer="frame",
        )
        self.text(
            18,
            564,
            "GATES: AS-FOUND  ·  JAY GO RAIL DRILL  ·  OUTRIGGERS+LEGS+kg  ·  HOSE/RAIN  ·  HATCH  ·  LADDER  ·  BUMPER/SPLASH  ·  D-01…D-06  ·  PROTOTYPE ONLY",
            2.45,
            layer="frame",
        )
        self.text(
            18,
            576,
            f"REV CONDITIONAL  ·  DISCUSSION ONLY  ·  NO-GO CUT STEEL UNTIL GATES  ·  mm  ·  2026-09-23  ·  SHEET {self.sheet_no} OF {self.sheet_count}",
            2.4,
            layer="frame",
        )
        self.text(648, 524, "SHEET", 2.4, layer="frame")
        self.text(648, 540, self.sid, 5.0, weight="bold", layer="frame")
        self.text(648, 556, self.scale_label, 3.2, layer="frame")
        self.text(648, 572, "VIEWS NAMED ON SHEET", 2.3, layer="frame")
        self.checkbox(762, 522, 6.5, layer="frame")
        self.text(772, 528, "JAY GO", 2.7, weight="bold", layer="frame")
        self.text(756, 544, "RAIL DRILL", 2.5, weight="bold", layer="frame")
        self.text(756, 558, "UNSIGNED", 2.4, fill="#9b1c1c", layer="frame")
        self.text(756, 570, "= NO-GO", 2.4, fill="#9b1c1c", layer="frame")

    def border(self):
        self.rect(8, 8, self.W - 16, self.H - 16, fill="none", stroke="#141414", sw=0.7, layer="frame")

    def to_svg(self) -> str:
        defs = "".join(self.defs)
        body = "\n".join(self.nodes)
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W:.0f}mm" height="{self.H:.0f}mm" '
            f'viewBox="0 0 {self.W:.0f} {self.H:.0f}" '
            f'role="img" aria-label="{esc(self.sid + " " + self.title)}">\n'
            f"<title>{esc(self.sid + ' — ' + self.title)}</title>\n"
            "<desc>KE-Texh TAMARAW Phase-1 SHELL. REV CONDITIONAL. "
            "PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED. "
            "Prototype discussion sheet. NO-GO cut steel until gates.</desc>\n"
            f"<defs>{defs}</defs>\n"
            f'<rect width="{self.W:.0f}" height="{self.H:.0f}" fill="#ffffff"/>\n'
            '<g font-family="DejaVu Sans, sans-serif" fill="#141414" stroke-linecap="square">\n'
            f"{body}\n</g>\n</svg>\n"
        )


def _expand(box, pad):
    return (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)


def _boxes_overlap(a, b, gap) -> bool:
    return not (a[2] + gap < b[0] or b[2] + gap < a[0] or a[3] + gap < b[1] or b[3] + gap < a[1])


def _overlap_area(a, b) -> float:
    x0 = max(a[0], b[0])
    y0 = max(a[1], b[1])
    x1 = min(a[2], b[2])
    y1 = min(a[3], b[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0
    return (x1 - x0) * (y1 - y0)


def _seg_hits_rect(x1, y1, x2, y2, r) -> bool:
    c1 = _code(x1, y1, r)
    c2 = _code(x2, y2, r)
    for _ in range(12):
        if c1 == 0 or c2 == 0:
            return True
        if c1 & c2:
            return False
        c = c1 or c2
        if c & 8:  # top (y < r1)
            if y2 == y1:
                return False
            x = x1 + (x2 - x1) * (r[1] - y1) / (y2 - y1)
            y = r[1]
        elif c & 4:  # bottom
            if y2 == y1:
                return False
            x = x1 + (x2 - x1) * (r[3] - y1) / (y2 - y1)
            y = r[3]
        elif c & 2:  # right
            if x2 == x1:
                return False
            y = y1 + (y2 - y1) * (r[2] - x1) / (x2 - x1)
            x = r[2]
        else:
            if x2 == x1:
                return False
            y = y1 + (y2 - y1) * (r[0] - x1) / (x2 - x1)
            x = r[0]
        if c == c1:
            x1, y1 = x, y
            c1 = _code(x1, y1, r)
        else:
            x2, y2 = x, y
            c2 = _code(x2, y2, r)
    return False


def _code(x, y, r) -> int:
    c = 0
    if x < r[0]:
        c |= 1
    elif x > r[2]:
        c |= 2
    if y < r[1]:
        c |= 8
    elif y > r[3]:
        c |= 4
    return c


def qa_sheet(sheet: Sheet) -> list[str]:
    errors = []
    texts = sheet.texts
    for i, a in enumerate(texts):
        ax0, ay0, ax1, ay1 = a["box"]
        if ax0 < 6 or ay0 < 6 or ax1 > sheet.W - 6 or ay1 > sheet.H - 6:
            errors.append(f"off-sheet text '{a['text']}' box={tuple(round(v, 1) for v in a['box'])}")
        for b in texts[i + 1 :]:
            if _boxes_overlap(a["box"], b["box"], 0.7):
                errors.append(f"text/text '{a['text']}' × '{b['text']}'")
        for x1, y1, x2, y2, layer in sheet.segs:
            if a["layer"] == "frame" and layer == "frame":
                pad = 0.35
            elif a["layer"] == "frame":
                continue
            else:
                pad = 0.65
                if layer == "frame":
                    pad = 0.5
            if _seg_hits_rect(x1, y1, x2, y2, _expand(a["box"], pad)):
                errors.append(f"text/line '{a['text']}' layer={layer} seg=({x1:.0f},{y1:.0f})-({x2:.0f},{y2:.0f})")
                break
    return errors
