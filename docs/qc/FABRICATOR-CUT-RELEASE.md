# FABRICATOR-CUT-RELEASE — KE-Texh Tamaraw Phase-1 SHELL

**Stamp:** **CONDITIONAL / NO-GO cut**
**Hold:** Fabricator cut send is **HOLD**. This file is the track to reach GO. It is not a GO stamp.
**Watermark:** **PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED**
**Today:** L1 **GREEN** · L2–L6 **RED** (colors live in `FAB-HANDOFF-GATE.md`). Audit **0 PASS / 6 GAP / 18 RED / 9 HOOK**. No part is CUT-READY.
**Rev:** A · 2026-09-23 Asia/Shanghai

**Do not invent** thickness, grade, weld size, bolt grade, kerf, kW, BTU, or kg. Where the pack says TBD, this track keeps TBD. Empty signature lines stay empty.

---

## 1. Purpose

**Fabricator Cut Release** is the authorized send of cut patterns + traveler for Phase-1 SHELL steel/composite blanks.

It is a separate act from:

- R&D / plan review of this public pack (`PHASE-PLAN-REDEF.md`, family SVGs, QC notes).
- LTO certification. This pack is not an LTO submission.

Public merge, ChatGPT review, and SVG/PNG presence do not perform that send. The shop folder goes out only after the exit criteria below are met and the authorization block is signed **on the traveler**, not by editing this file.

**Cut-line:** Phase-1 SHELL blanks only. Phase-2 solar / awning / seats, and generator / AC **units**, stay out of the cut zip.

---

## 2. Hard rule

**Today’s status is still NO-GO.**

Lego colors are not changed by this document. `FAB-HANDOFF-GATE.md` stays authoritative: L1 GREEN, L2–L6 RED. Cut steel and fabricator send stay blocked while any of L2–L6 is RED.

Read this file as the checklist that must go green later. Do not read it as permission to cut, drill, or email a shop.

---

## 3. Exit criteria

GO cut send requires **both**: every Lego row L1–L6 **GREEN** on `FAB-HANDOFF-GATE.md`, and residual items 1–8 filed as named there. This table does not add gate numbers. Residual rows are **Open**. They are not a second color scale. Their parent Lego rows are already RED.

| Gate | Source name | Today | Checkable artifact | Pointer |
|------|-------------|-------|--------------------|---------|
| **L1** | Shop can identify the overall envelope | **GREEN** | `DIMS.md` and elevations S-01…S-08 / I-00 agree on the locked envelope (no second overall length). Still CONDITIONAL until as-found tape matches. | `FAB-HANDOFF-GATE.md` L1 · `DIMS.md` · `PHASE-PLAN-REDEF.md` §3 |
| **L2** | Shop can cut every Phase-1 part from controlled patterns | **RED** | DXF, or a shop-accepted equivalent, for C-FR, C-PL, DR-*, H-*, and loft B/D/E; P4 flats A–E **developed** after bend allowance is locked; kerf recorded on C-00. | `FAB-HANDOFF-GATE.md` L2 · `inventory/PER-PART-AUDIT.md` geometry column · WP-C, WP-D, WP-E, WP-F, WP-G |
| **L3** | Shop can select stock and make structural joints without asking Eng | **RED** | Tube section, plate thickness/grade, weld size, and skin splice signed on MAT-01 / C-FR / C-PL / J-01. No defaults written here. | `FAB-HANDOFF-GATE.md` L3 · `notes/commissioning-gates.md` §3 · WP-J |
| **L4** | Shop can drill and attach the body to the vehicle | **RED** | As-found chassis tape filed; Jay **rail-drill GO** signed; hole schedule on D-01 / C-PL released. | `FAB-HANDOFF-GATE.md` L4 · `notes/commissioning-gates.md` §1–§2 · WP-I |
| **L5** | Shop can build and verify hatch + Phase-1 provisions | **RED** | Hatch frame sizes frozen; H-* DXF (or shop-accepted equivalent); gen/AC remain **provisions/hooks only** with named conditions signed (still not the unit). | `FAB-HANDOFF-GATE.md` L5 · `notes/commissioning-gates.md` §6, §9–§10 · WP-H, WP-K · `PER-PART-AUDIT.md` |
| **L6** | Shop can declare the completed vehicle acceptable | **RED** | Commissioning gates signed (weigh, stability, hose, height, FAIL-IFs). | `FAB-HANDOFF-GATE.md` L6 · `notes/commissioning-gates.md` · WP-L |
| **1** | As-found tape on chassis / rails | **Open** | Traveler tape table filled: bed L×W, rail spacing, cab roof H, front and rear overhangs, VIN. | `notes/commissioning-gates.md` §1 · `PHASE-PLAN-REDEF.md` P0 / WP-A |
| **2** | Jay rail-drill GO | **Open** | Jay GO line signed on the traveler. FS-01 H-R and H-B stay TBD until that line is signed. | `notes/commissioning-gates.md` §2 · WP-I |
| **3** | Eng: tube section, plate t/grade, weld size | **Open** | Eng GO line signed. MAT-01, J-01, and C-FR boxes filled by Eng, or an explicit refuse. | `notes/commissioning-gates.md` §3 · WP-J |
| **4** | Bend allowance → develop P4 A–E | **Open** | Developed blanks A–E, or a controlled shop-develop instruction, after bend allowance is locked. Allowance value is not stated in this file. | `inventory/PER-PART-AUDIT.md` P4-A…P4-E · WP-D |
| **5** | DXF release: C-FR, C-PL, DR, H, loft B/D/E | **Open** | Those pattern files accepted by the shop and listed on the traveler. | `inventory/PER-PART-AUDIT.md` · `FAB-HANDOFF-GATE.md` L2 |
| **6** | Hatch frame freeze | **Open** | Frame sizes frozen (FR-17 / FR-18 / FR-22, D-04, F-03) and H-01 / H-02 leaves released with them. | `notes/commissioning-gates.md` §6 · WP-H |
| **7** | Kerf + skin splice on C-00 / BOM | **Open** | Decision recorded on C-00 / BOM-01. Kerf number is not stated in this file. | `inventory/CUT-FORM-REGISTER.md` (C-00) · WP-B / WP-C |
| **8** | Commissioning: weigh placard, hose FAIL-IF, OAH closed, stability support | **Open** | Weigh date and placard-blank check, hose result, OAH ≤ 2500 with hatch closed, stability / outrigger and leg boxes signed. | `notes/commissioning-gates.md` §4–§5 · WP-L |

**Leave NO-GO only when** the L1–L6 column on `FAB-HANDOFF-GATE.md` is all GREEN **and** residual artifacts 1–8 are filed on the traveler. Until that day the stamp on this file stays **CONDITIONAL / NO-GO cut**.

---

## 4. Release binder contents

The zip or folder the shop gets, **after** the exit criteria are met. Do not assemble or send this folder while the stamp is NO-GO. Checkboxes below are the future contents list. They are not ticked.

### Include

- [ ] **SoR dims** — `DIMS.md` only. No second overall length. No photo-scale figure substituted for it.
- [ ] **Elevations** — S-01…S-08 in `blueprint-pack/sheets/` (index I-00 with them).
- [ ] **C-series DXF** (or a shop-accepted equivalent) for the Phase-1 skin families the gate names (C-01…C-06, including developed loft flats).
- [ ] **C-FR / C-PL / DR / H** — frame cut list, plates PL-01…PL-08, DR-01/DR-02, H-01/H-02, as DXF or shop-accepted equivalent.
- [ ] **Developed P4** — flats A–E after bend allowance is locked (WP-D). Undeveloped estimate sheets stay out.
- [ ] **MAT-01 / J-01** — Eng boxes **signed** (stock, tube, plate, weld, skin splice). Unsigned TBD sheets do not satisfy this line.
- [ ] **D-01 hole schedule** — included only **after** Jay rail-drill GO. Centers and edge distance come from that release, not from this file.
- [ ] **Hatch freeze** — frozen frame (D-04 / F-03) plus H-01 / H-02 leaves.
- [ ] **C-00 kerf / splice** — the recorded decision on `cut/C-00_nest_index.svg` (and the matching BOM note). This file does not state a kerf value.
- [ ] **Traveler** — `notes/commissioning-gates.md` boxes copied onto the shop traveler and signed.
- [ ] **FAIL-IFs for provisions** — D-07 generator bay and D-08 AC curb, as provisions. The wording already in commissioning §9–§10. Units are not attached to these sheets.

### Exclude (do not put these in the cut zip as cut-Done)

- Generator **unit** and AC **unit**.
- Solar, awning, seats.
- Photo-scale reference under `fab-pack/reference/` (including any photo-scale overall length).
- Unsigned TBDs: empty Eng/Jay boxes, unfrozen opening sizes, undeveloped P4, missing DXF families, kerf/splice still blank.
- PL-09 and PL-10 as cut-Done parts (provision plates only; WP-K).
- H-03 / FS-01 as a buy release before hatch geometry and gates close.
- A claim of LTO certification, kW, BTU, or a filled max-kg placard.

---

## 5. Cut-batch order

Suggested sequence **once the exit criteria for that batch are clear**. Until then every line stays **CONDITIONAL / NO-GO cut**. Nothing in the table is CUT-READY. Work-package IDs are from `PHASE-PLAN-REDEF.md` §6.

| Order | Batch | Work package | Clears before this batch may be cut |
|------:|-------|--------------|-------------------------------------|
| 1 | Skins, with kerf already recorded on C-00 | **WP-C** (P1, P2, P3, P5, P6) and developed loft **WP-D** (P4 A–E) | L2 for that family. Kerf and skin splice recorded (residual 7). P4 bend allowance locked before loft blanks (residual 4). Entry on P2 stays field-locate until frozen; P7 is not its own blank. |
| 2 | Frame | **WP-E** (C-FR, FR-01…FR-22) | C-FR DXF or shop-accepted equivalent (residual 5) and Eng tube/join boxes signed (L3, residual 3). Qty-TBD members stay off the saw. |
| 3 | Plates, after the hole schedule | **WP-F** (PL-01…PL-08) | Hole schedule released and Jay rail-drill GO signed (L4, residual 2, WP-I). Not before that schedule. |
| 4 | Door | **WP-G** (DR-01, DR-02) | Opening, overlap, and seal frozen; DXF or shop-accepted equivalent. |
| 5 | Hatch leaves | **WP-H** (H-01, H-02) | Hatch frame freeze (L5, residual 6) and leaf patterns released. |

**Never cut-Done in any batch:** PL-09, PL-10, generator unit, AC unit, solar, awning, seats (**WP-K**). Provision sheets may travel as FAIL-IFs only.

A later batch does not start because an earlier SVG exists. Each batch waits on its own row above, and the pack stamp stays NO-GO until §3 is fully clear.

---

## 6. Authorization block

Blank on purpose. Sign on the traveler copy that ships with the binder. Do not type a name into this file and treat it as signed.

| Check | Signature | Date | Rev |
|-------|-----------|------|-----|
| Jay GO cut send | | | |
| Eng GO stock/join | | | |
| Field tape filed | | | |
| Lilu visual QA clean (no overlapping dims) | | | |

Cut-send date: ______________

Binder rev sent: ______________

All four rows empty = **HOLD**. Visual QA is not claimed clean. Overlapping dimensions are not waived.

---

## 7. Watermark and stamp language

Put both lines on the binder cover and on the traveler:

- `PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED`
- `CONDITIONAL / NO-GO cut`

`CONDITIONAL / NO-GO cut` stays until §3 exit criteria are met (L1–L6 all GREEN and residual 1–8 filed).

`PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED` stays after a future cut GO. A cut send is not an LTO certificate. As-found tape still governs estimates on the vehicle.

---

## 8. Cross-refs

| Doc | Role |
|-----|------|
| `DIMS.md` | Only envelope register |
| `docs/qc/FAB-HANDOFF-GATE.md` | Authoritative L1–L6 colors and residual gate names |
| `docs/qc/PHASE-PLAN-REDEF.md` | P0–P6 and WP-A…WP-L; cut-send stays HOLD |
| `inventory/PER-PART-AUDIT.md` | 33-row six-field matrix (0 PASS) |
| `docs/qc/PER-PART-AUDIT-SUMMARY.md` | 0 / 6 / 18 / 9 counts |
| `notes/commissioning-gates.md` | Traveler boxes and provision FAIL-IFs |
| `inventory/CUT-FORM-REGISTER.md` | What is drawn vs what is still thin |
| `docs/qc/BOM-MAT-VERIFY.md` | BOM/MAT gaps; no invented stock |
| `README.md` | Pack reading order |

---

*End FABRICATOR-CUT-RELEASE Rev A. CONDITIONAL / NO-GO cut. HOLD. PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED.*
