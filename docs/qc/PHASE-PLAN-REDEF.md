# PHASE-PLAN-REDEF — KE-Texh Tamaraw Phase-1 SHELL

**Survive without Mavlon / fab AI.** Manual DXF/CAD path or hold paper.

| Field | Value |
|-------|-------|
| Stamp | **CONDITIONAL / NO-GO cut** until Lego L1–L6 are all GREEN |
| Watermark | **PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED** |
| SoR dims | `DIMS.md` only (this file does not add a second overall length) |
| Repo | https://github.com/centralchaos/ketexh-tamaraw-camper (public) |
| Rule | Public repo ≠ cut release. SVG/PNG present ≠ fabrication-ready. Merge to `main` / ChatGPT review does **not** clear the fabricator gate. |
| Basis | `DIMS.md`, `FAB-HANDOFF-GATE.md`, `FABRICATOR-CUT-RELEASE.md`, `PER-PART-AUDIT.md` (+ summary), `commissioning-gates.md`, `README.md`, `CUT-FORM-REGISTER.md`, `BOM-MAT-VERIFY.md` |
| Rev | A.1 · 2026-09-23 Asia/Shanghai · Fabricator Cut Release track added; Lego colors unchanged (L1 GREEN, L2–L6 RED). Prior: Rev A same day, redefine after ChatGPT Lego review. |

**Do not invent** thickness, grade, weld size, bolt grade, kW, BTU, or kg. Where the pack says TBD, this plan keeps TBD.

---

## 1. Purpose

Redefine Phase-1 delivery so the shop can **survive without Mavlon / fab AI**: either (a) finish paper + manual DXF/CAD exports to clear L2–L6, or (b) hold cut steel and keep the pack CONDITIONAL. This plan maps the 33-row audit into ordered work packages, names owners, and ties each package to a Lego gate.

**Cut-line for this document:** Phase-1 SHELL only. Phase-2 solar / awning / seats / generator unit / AC unit stay hooks.

---

## 2. Problem / outcome / MVP cut-line

### Problem

The R&D pack already has family SVGs for skins, frame, door, hatches, and plates (CUT-FORM-REGISTER: “yes for the families”). The fabricator cannot build from paper alone: L2–L6 are RED (FAB-HANDOFF-GATE). Audit: **0 PASS / 6 GAP / 18 RED / 9 HOOK** (33 rows). Missing DXFs, undeveloped P4, unsigned Eng/Jay GOs, open openings, and unsigned commissioning boxes block cut steel.

### Outcome (Phase-1 SHELL MVP)

A vehicle-mounted Phase-1 shell that:

- Matches the locked envelope on `DIMS.md` after as-found tape.
- Is cut and joined only from parts that have all six promotion fields signed (part+rev, material+qty, developed geometry, process/join, mate location, measurable AC).
- Attaches only after Jay rail-drill GO and released hole schedule.
- Declares acceptance only after commissioning gates are signed.
- Keeps gen/AC as **provisions / hooks** (mounts + FAIL-IFs only — not units).

### MVP cut-line (in vs out)

| In Phase-1 SHELL (this plan) | Out / Phase-2 hooks |
|------------------------------|---------------------|
| Floor / walls / loft flats / rear / roof skins (P1–P6) | Solar array, awning, seats |
| Entry as field-locate on P2 + DR-01/02 | Generator **unit**, AC **unit** |
| Frame FR-01…FR-22 + plates PL-01…PL-08 (when Eng/Jay release) | PL-09 / PL-10 as buy/cut Done (remain provision) |
| Hatch leaves H-01/H-02 after freeze + frame | H-03 hardware buy release before geometry/gates close |
| Gen bay + AC curb **provisions** (D-07/D-08 FAIL-IFs) | Any kW / BTU / max-kg placard fill |
| Commissioning weigh/hose/height/stability | LTO certification |

**Demonstrable end of Phase-1:** L1–L6 GREEN + traveler signed — not “SVG count looks complete.”

---

## 3. Locked SoR snapshot (from `DIMS.md` only)

Stamp on SoR: CONDITIONAL. PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED.

### Chassis (TMP LWB dropside — verify on the VIN)

| Datum | Value | Notes |
|-------|-------|-------|
| Wheelbase | **3085 mm** | Public LWB |
| Stock overall L × W × H | **5300 × 1800 × 1800 mm** | TMP dropside |
| Cargo bed L × W | **2647 × 1711 mm** | TMP |
| Tread front / rear | 1510 / 1510 mm | Chassis reference on S-03 / S-04 |

Payload in the source brief is a plate check, not a shell design weight. Max-kg placard on D-02 stays blank until as-built weigh.

### Phase-1 shell envelope

| Datum | Value | Notes |
|-------|-------|-------|
| Overall length | **≈ 6300 mm** | OEM 5300 + tail 1000. One overall length. |
| Shell floor L × W | **3647 × 1911 mm** | Bed 2647 + tail 1000; width 1711 + 2×100 |
| Overall height | **≤ 2500 mm** | Hatch closed. If AC curb provision is built, curb is included in closed height. |
| Over-cab length | **≈ 1223 mm** | Estimate |
| Tail extension | **+1000 mm** | Beyond stock dropside |
| Side growth | **+100 mm / side** | Shell width 1911 |
| Shell exterior height | **≈ 1830 mm** | Construction **estimate**. As-found tape governs. |
| Loft | **≈ 700 mm** | Construction **estimate** |
| Clear standing height | **1900–2000 mm** | Target. Not closed by the 1830 mm exterior. |
| Rear past axle | **≈ 2015 mm** | Side/section callout |
| Over-cab + floor | **4870 mm** | Sum 1223 + 3647 only. Not a new measured datum. |

### Openings (release posture)

| Opening | Figure | Release |
|---------|--------|---------|
| Entry | **700 × 1550 mm** target, behind cab, on P2 | Field locate. Not a cut freeze. |
| Body windows | Schematic on elevations | Size TBD. Field locate. |
| Over-cab window | On loft side | Size TBD. Field locate. |
| Front face | Optional | No cut size |
| Rear window, lower hatch, lounge cutout | Intent on S-06 / S-07 / D-04 / H-01 / H-02 | **No cut size.** |
| AC curb, generator bay | Provisions on S-08 / D-07 / D-08 | Not the units. Not cut Done. |

### Rejected substitutions (do not cut)

| Do not cut | Use |
|------------|-----|
| Floor width 1912 | **1911** |
| Over-cab 1215 | **≈ 1223** |
| Entry 780 × 1550 | **700 × 1550** field locate |
| Photo-scale overall length 5942 (and photo-scale height) | Reference only in `fab-pack/reference/`. **Not a cut figure.** |

Vertical estimates close only if this vehicle’s rail and cab-roof heights match the schematic. **As-found tape governs.**

---

## 4. Workstreams ↔ Lego L1–L6

From `FAB-HANDOFF-GATE.md`. Cut steel / fabricator send blocked while any of L2–L6 is RED.

| # | Question | Today | Clears when (exact) |
|---|----------|-------|---------------------|
| **L1** | Can the shop identify the overall envelope? | **GREEN** | Locked floor, entry target, over-cab, OAL, tail on SoR + elevations agree (no dual OAL). *Context PASS on audit; still CONDITIONAL until as-found tape matches.* |
| **L2** | Can it cut every Phase-1 part from controlled patterns? | **RED** | DXF (or shop-accepted equivalent) for C-FR, C-PL, DR-*, H-*, loft B/D/E; P4 flats **developed** after bend allowance locked; kerf on C-00. |
| **L3** | Can it select stock and make structural joints without asking Eng? | **RED** | Tube section, plate thickness/grade, weld size, skin splice signed on MAT-01 / C-FR / C-PL (no invented defaults). |
| **L4** | Can it drill and attach the body to the vehicle? | **RED** | As-found chassis tape filed; Jay **rail-drill GO** signed; hole schedule on D-01/C-PL released. |
| **L5** | Can it build and verify hatch + Phase-1 provisions? | **RED** | Hatch frame sizes frozen; H-* DXF; gen/AC remain **provisions/hooks only** with named conditions resolved (still NOT THE UNIT). |
| **L6** | Can it declare the completed vehicle acceptable? | **RED** | Commissioning gates signed (weigh, stability, hose, height, FAIL-IFs). |

**Residual named gates (do not improvise beside fabricator):**  
(1) as-found tape · (2) Jay rail-drill GO · (3) Eng tube/plate/weld · (4) bend allowance → develop P4 A–E · (5) DXF: C-FR, C-PL, DR, H, loft B/D/E · (6) hatch frame freeze · (7) kerf + skin splice on C-00/BOM · (8) commissioning weigh/hose/OAH/stability.

---

## 5. Phased delivery plan (demonstrable ends)

Each phase ends with a **shop-visible artifact**, not a meeting.

### P0 — Capture (as-found tape)

**End:** Traveler rows filled: bed L×W, rail spacing, cab roof H, VIN recorded (+ photos). Front/rear overhangs taped per commissioning list.

**Field checklist (from `commissioning-gates.md` §1 + register fill-order):**

- [ ] Photograph and tape cargo bed L × W (compare to **2647 × 1711** TMP).
- [ ] Tape rail spacing (outrigger pitch input — do not invent FR-06 qty).
- [ ] Tape cab roof height and rail heights (closes ≈1830 / ≈1223 / ≈700 **estimates**).
- [ ] Tape front and rear overhangs; note rear past-axle vs ≈2015 callout (informational).
- [ ] Record VIN plate; confirm LWB dropside against stock **5300 × 1800 × 1800**.
- [ ] Photograph D-01 rail zones before any drill.
- [ ] Freeze numbers on traveler; mark Architect CONDITIONAL floor **3647 × 1911** / OAL **≈6300** as verified or delta-listed (delta → Eng, not silent edit of DIMS).

**Owner:** Field · **Gate:** feeds L4 (and L1 confirmation) · **No cut.**

### P1 — Paper complete (R&D pack already largely here)

**End:** Paper hygiene closed enough that promotion work is geometry/GO, not missing sheets.

**Already present (do not re-author):** family SVGs for P1–P6, C-FR, C-PL, DR-01/02, H-01…H-03, F-00…F-03, shop binder (CVR-00, C-00, MAT-01, FS-01, BOM-01, AS-01, J-01, QA-01), elevations S-01…S-08, details D-01…D-08, A-05, I-00. QC establishes family presence and dim consistency vs DIMS — **not** manufacturing completeness.

**Still missing on paper (from BOM-MAT-VERIFY + audit):**

| Gap | Action (no invent) |
|-----|--------------------|
| PL-09 / PL-10 BOM naming | Jay decides: explicit BOM lines as provision plates **or** formal note “counted only under D-07/D-08.” PR #4 tip `863c427` (BOM+audit; earlier BOM-only tip was 6d5562d) claims plate BOM patch — **verify on tip before treating closed.** |
| Qtys TBD | Leave TBD until Eng/Jay: FR-06, FR-08, PL-01…10 (except PL-08 qty **2** on C-PL), H-03, all FS-01 symbols. |
| Kerf / nest brand / skin splices | Decision recorded on C-00 / C-01 / C-06 — empty until Eng. |
| Opening cut sizes | Stay TBD / field-locate until P5 hatch freeze. |
| Dual-path note | Survive-without-Mavlon: **manual CAD DXF export** from existing SVG masters, or **hold paper** (no fabricator send). |

**Owner:** Cursor / Lilu (docs) · Jay (BOM hygiene decision) · **Gate:** supports L2/L3 hygiene · **No cut.**

### P2 — Geometry release (DXF + developed P4 + kerf)

**End:** Shop-accepted DXF (or equivalent) for every Phase-1 cut family still RED on patterns; P4 A–E developed after bend allowance locked; kerf stated on C-00.

**Part families (ordered):**

| Family | DVX today | Release work |
|--------|-----------|--------------|
| P1 floor | C-01 SVG+DXF present; **3647 × 1911** | Freeze splice/kerf before cut; otherwise keep GAP |
| P2 / P3 walls | C-02/C-03 SVG+DXF; H ≈1830 est. | Tape height; entry **700 × 1550** remains field-locate (not freeze); window size TBD |
| P4 loft A–E | A/C DXF reported; **B/D/E DXF missing**; none developed | Lock bend allowance → develop flats → DXF B/D/E **or** stamp controlled shop-develop instruction |
| P5 rear | C-05 SVG; openings no cut size | Freeze openings with hatch work or keep intent-only |
| P6 roof | C-06 SVG+DXF; **4870 × 1911** | Freeze splice + lounge opening with hatch |
| C-FR | SVG; **no DXF** | Export DXF; miters/holes still need Eng |
| C-PL | SVG; **no DXF** | Export DXF after hole schedule (ties to L4) |
| DR-01/02 | SVG; **no DXF** | Freeze overlap/seal → DXF |
| H-01/02 | SVG; **no DXF**; size TBD | Freeze with D-04 / F-03 → DXF |

**Owner:** Cursor (manual DXF/CAD) · Eng (bend allowance sign) · **Gate:** L2 · **No cut until L3–L5 also clear for that part.**

### P3 — Stock & joinery (Eng GO boxes only)

**End:** Eng GO signed on traveler for tube section, plate thickness/grade, weld size, skin splice — **or** explicit refuse. Empty boxes stay empty. No invented defaults.

**Boxes (from commissioning §3 + MAT-01 / J-01 / C-FR):**

- Outer / inner / core thickness & grade (MAT-01) — Eng
- Frame tube section (F-02 / C-FR) — Eng
- Plate thickness/grade (C-PL) — Eng
- Weld / filler (J-01) — Eng
- Sealant & weatherstrip product class — Eng
- Skin splice decision (C-01 / C-06) — Eng

**Owner:** Eng · **Gate:** L3 · FS-01 H-R/H-B still gated by Jay (L4), not Eng.

### P4 — Vehicle attach (rail-drill GO + hole schedule)

**End:** As-found tape filed + Jay GO signed on D-01 + hole schedule released on D-01 / C-PL (centers, edge distance). No undirected drill into bed or chassis rail. FS-01 H-R / H-B leave TBD until this box.

**Owner:** Field (tape) · Jay (GO) · Eng/Cursor (schedule draught after GO inputs) · **Gate:** L4.

### P5 — Hatch freeze + provision FAIL-IFs

**End:**

1. Hatch frame sizes frozen (FR-17/18/22 + F-03 / D-04); H-01 / H-02 leaves + DXF; FAIL-IFs per commissioning §6.
2. Gen bay (D-07) and AC curb (D-08) conditions named and signed as **provisions** — units remain HOOK. FAIL-IFs per commissioning §9–§10. No kW / BTU / kg.

**Owner:** Eng (geometry) · Jay (accept FAIL-IF language) · Cursor (DXF after freeze) · **Gate:** L5.

### P6 — Commissioning / acceptance

**End:** All boxes in `commissioning-gates.md` signed on traveler. Placard still blank until axle scales. OAH ≤ 2500 with hatch closed (and curb if built). Hose 10 min FAIL-IF wet cabin / trapped water / wet glands. Ladder roof-access only. Bumper weep + hitch clear of landing-leg swing.

**Owner:** Field / Jay · **Gate:** L6 · **Then** fabricator language may leave NO-GO — still not LTO.

### Cut-send track (not a phase end)

P0–P6 do not authorize steel. The authorized send of cut patterns + traveler — separate from R&D review and from LTO — is `docs/qc/FABRICATOR-CUT-RELEASE.md` (exit checklist, binder contents, cut-batch order, blank authorization lines).

**Default: HOLD** until L2–L6 are GREEN. L1 stays GREEN. This pointer does not flip a Lego color and does not mark any part CUT-READY.

---

## 6. Per-part promotion backlog (33 rows → work packages)

**Promotion rule:** R&D → CUT-READY only when all six fields filled and signed: (1) part ID + rev · (2) material + qty · (3) developed geometry · (4) process/join · (5) mate location · (6) measurable AC.

Ordered for survive-without-Mavlon (capture → paper → geometry → Eng/Jay GOs → attach → hatch → accept). HOOK rows are tracked, not promoted to cut.

### WP-A — As-found capture

| | |
|--|--|
| **Part IDs** | *(traveler / all height-sensitive: P2, P3, P5, FR-07/08/15, P4 envelope)* |
| **Verdict** | N/A process — unblocks GAP/RED heights |
| **Deliverables** | Signed tape table (bed, rails, cab roof H, VIN, overhangs); photo set; delta list vs DIMS if any |
| **Owner** | Field |
| **Gate** | L4 (feeds L1 confirm) |

### WP-B — Paper / BOM hygiene

| | |
|--|--|
| **Part IDs** | PL-09, PL-10 (naming); process sheets C-00 / BOM-01 / MAT-01 / FS-01 (no new invented lines) |
| **Verdict** | HOOK (PL-09/10); process N/A |
| **Deliverables** | Jay decision on PL-09/10 BOM treatment; re-run BOM-MAT-VERIFY on PR #4 tip if merged; kerf/splice decision **placeholders** only |
| **Owner** | Jay · Lilu / Cursor |
| **Gate** | L2/L3 hygiene |

### WP-C — Skin GAP close (DXF present families)

| | |
|--|--|
| **Part IDs** | P1, P2, P3, P5, P6, P7 |
| **Verdict** | GAP ×6 |
| **Deliverables** | Splice/kerf freeze (P1/P6); as-found height confirm (P2/P3/P5); entry remains field-locate on P2 (P7); window/hatch openings stay TBD until WP-G or explicit non-cut |
| **Owner** | Eng (splice/kerf) · Field (tape) · Cursor (sheet rev) |
| **Gate** | L2 partial (skins) |

### WP-D — P4 loft develop + missing DXF

| | |
|--|--|
| **Part IDs** | P4-A, P4-B, P4-C, P4-D, P4-E |
| **Verdict** | RED ×5 |
| **Deliverables** | Bend allowance signed; developed blanks A–E; DXF for B/D/E (A/C already reported) **or** controlled shop-develop forever note |
| **Owner** | Eng · Cursor |
| **Gate** | L2 |

### WP-E — Frame C-FR release

| | |
|--|--|
| **Part IDs** | FR-01…FR-22 (rollup) |
| **Verdict** | RED |
| **Deliverables** | C-FR DXF; tube section; miters/holes; weld callouts via J-01; as-found heights applied to ≈ rows; qty decisions for FR-06 / FR-08 (Eng — no invent before GO) |
| **Owner** | Eng · Cursor (DXF) |
| **Gate** | L2 + L3 |

### WP-F — Structural plates PL-01…PL-08

| | |
|--|--|
| **Part IDs** | PL-01, PL-02, PL-03, PL-04, PL-05, PL-06, PL-07, PL-08 |
| **Verdict** | RED ×8 |
| **Deliverables** | C-PL DXF; plate patterns; hole centers/edge (after Jay inputs for PL-01); Eng material/join; PL-08 weld with J-01; PL-03 roof-access-only confirm; PL-06 no kg placard |
| **Owner** | Eng · Jay (PL-01 GO path) · Cursor |
| **Gate** | L2 + L3 + L4 (PL-01) |

### WP-G — Door family

| | |
|--|--|
| **Part IDs** | DR-01, DR-02 *(+ P7 interface)* |
| **Verdict** | RED ×2 (P7 GAP) |
| **Deliverables** | Opening/overlap/seal freeze with field-locate entry; jamb interface with FR-19…21; DXF export |
| **Owner** | Eng · Field · Cursor |
| **Gate** | L2 |

### WP-H — Hatch freeze + leaves

| | |
|--|--|
| **Part IDs** | H-01, H-02 *(frame: FR-17/18/22)* |
| **Verdict** | RED ×2 |
| **Deliverables** | Opening + hatch frame freeze (D-04 / F-03); leaf DXF; FAIL-IF language on traveler |
| **Owner** | Eng · Cursor |
| **Gate** | L5 (+ L2) |

### WP-I — Vehicle attach schedule

| | |
|--|--|
| **Part IDs** | PL-01 path · D-01 · FS-01 H-R/H-B · FR-06 |
| **Verdict** | RED (attach blockers) |
| **Deliverables** | Jay rail-drill GO signed; hole schedule released; no undirected rail drill |
| **Owner** | Jay · Field |
| **Gate** | L4 |

### WP-J — Eng stock & joinery GO

| | |
|--|--|
| **Part IDs** | MAT-01 classes covering P1–P6, FR, PL, DR/H weatherstrip; J-01 |
| **Verdict** | Cross-cutting RED on L3 |
| **Deliverables** | Signed Eng GO or refuse; still no invented thickness/grade/weld |
| **Owner** | Eng |
| **Gate** | L3 |

### WP-K — Provisions & Phase-2 hooks (do not promote)

| | |
|--|--|
| **Part IDs** | P8, PL-09, PL-10, H-03, Gen bay provision, AC curb provision, Generator unit, AC unit, Solar / awning / seats |
| **Verdict** | HOOK ×9 |
| **Deliverables** | Signed FAIL-IF / condition checklists for D-07/D-08; H-03 remains schedule-not-buy until hatch gates close; P8 stays non-cut unless separately sized; units stay HOOK ONLY on BOM |
| **Owner** | Eng · Jay · Lilu |
| **Gate** | L5 (provisions only) — **never** L2 cut-Done for units |

### WP-L — Commissioning closeout

| | |
|--|--|
| **Part IDs** | Whole vehicle / traveler (outriggers, legs, hose, hatch, ladder, bumper, provisions) |
| **Verdict** | L6 RED until signed |
| **Deliverables** | All commissioning boxes signed; weigh date; placard blank confirmation; hose result; OAH check |
| **Owner** | Field · Jay |
| **Gate** | L6 |

**Row coverage check:** GAP(6)+RED(18)+HOOK(9)=33. Skins in WP-C; P4 in WP-D; FR in WP-E; PL-01…08 in WP-F; DR in WP-G; H-01/02 in WP-H; nine HOOKs in WP-K; process/GO in WP-A/B/I/J/L.

---

## 7. Explicit OUT of scope / never invent

**Out of Phase-1 cut / buy release**

- Generator unit, AC unit (HOOK ONLY).
- Solar, awning, seats (Phase-2).
- P8 body windows as cut blanks (size TBD).
- H-03 / FS-01 as purchase release before hatch geometry and gates close.
- PL-09 / PL-10 as FAB DONE cut parts (provision plates only).
- LTO certification / public-repo merge as a cut gate.
- Photo-scale figures in `fab-pack/reference/` (e.g. OAL 5942).

**Never invent (empty = empty)**

- Thickness, material grade, sandwich brand.
- Tube section, weld size, filler spec.
- Bolt grade, dia, edge, torque, qty (except where register already states a qty, e.g. PL-08 **qty 2**).
- Kerf value, nest brand, skin splice geometry.
- Bend allowance (until Eng locks it).
- Hatch / window / lounge / rear opening cut sizes (until freeze).
- kW, BTU, max kg / placard fill.
- Dual overall length or rejected substitutions (1912 / 1215 / 780×1550).

**QC-REPORT establishes ≠ release:** dim consistency, family SVG presence, stamps, provision-only wording. It does **not** establish developed flats, stock, kerf, weld, or bolt grade.

---

## 8. Decision log placeholders (Jay)

| # | Decision | Options | Needed before | Status |
|---|----------|---------|---------------|--------|
| D1 | Merge PR #4 (BOM PL plate patch tip `863c427` (BOM+audit; earlier BOM-only tip was 6d5562d))? | Merge / hold / re-verify on tip then merge | WP-B hygiene; BOM-MAT-VERIFY re-run | ☐ |
| D2 | Fabricator send hold? | **Hold** (default while L2–L6 RED) / send only after all Lego GREEN. Fabricator Cut Release track added — default HOLD until L2–L6 GREEN (`FABRICATOR-CUT-RELEASE.md`). | Any steel cut | ☐ Hold |
| D3 | Which WP first after P0 tape? | Recommended: WP-B → WP-D (P4) → WP-E (C-FR) in parallel with WP-J Eng GO start; **or** hold all geometry and stay paper-only | Survive-without-Mavlon path | ☐ |
| D4 | PL-09/PL-10 BOM treatment | Explicit provision lines **or** “counted only under D-07/D-08” | Shop explosion clarity | ☐ |
| D5 | P4 path | Develop + DXF B/D/E **or** stamp shop-develop forever | L2 | ☐ |
| D6 | Manual DXF owner | Cursor local CAD export vs outside draughtsman vs hold paper | L2 | ☐ |
| D7 | Rail-drill GO | Sign / refuse / defer until tape | L4 — no undirected drill | ☐ |
| D8 | Eng GO chase | Who pings Eng; refuse-by-date? | L3 | ☐ |

*Jay signs on the traveler; this table is a planning mirror only.*

---

## 9. Next 7-day recommended sequence

**Assumption:** Survive without Mavlon — **manual DXF/CAD path** where SVG masters exist, otherwise **hold paper** (no fabricator send). Estimates are schedule estimates only.

| Day | Focus | Output | Owner |
|-----|-------|--------|-------|
| **1** | P0 field tape + photo set; open D1–D3 placeholders | Signed traveler §1 or scheduled truck day | Field · Jay |
| **2** | WP-B: PR #4 decision; BOM PL-09/10 rule; confirm no invented MAT/FS fills | Hygiene note + verify tip SHA | Jay · Lilu |
| **3** | WP-J kickoff: Eng receives TBD list (tube, plate t/grade, weld, splice, bend allowance) — **empty GO boxes, not draft numbers** | Eng GO request packet | Eng · Cursor |
| **4** | WP-D start: loft develop method; DXF export trial on one C-FR or C-PL sample | Process note: SVG→DXF path works / blocked | Cursor |
| **5** | WP-C: apply as-found heights to P2/P3/P5 notes; list splice/kerf decisions still open | Rev marks on sheets (still CONDITIONAL) | Cursor · Eng |
| **6** | WP-E/F draught prep: hole/miter TBD list for Eng/Jay; no rail drill | Attach & frame open-items list | Eng · Jay |
| **7** | Gate review: L1 still GREEN? L2–L6 still RED? Update this plan’s decision log; **fabricator send remains HOLD** | 15-min Jay sync; traveler still NO-GO | Jay · Lilu |

**If tape day slips:** stay on WP-B + Eng GO request + DXF path proving; do not freeze heights or hatch sizes from estimates.

**If Eng GO refuses or delays:** keep MAT-01/J-01 TBD; do not substitute brands; geometry DXF may still proceed as CONDITIONAL inventory only — **not** CUT-READY.

**Cut send:** binder contents, exit checklist, and batch order are in `docs/qc/FABRICATOR-CUT-RELEASE.md`. Day 7 does not clear them. Default remains HOLD until L2–L6 GREEN.

---

## Cross-refs

| Doc | Role |
|-----|------|
| `DIMS.md` | Only envelope register |
| `FAB-HANDOFF-GATE.md` | Lego L1–L6 + residual gates |
| `FABRICATOR-CUT-RELEASE.md` | Cut-send track: exit checklist, binder, batch order. Default HOLD |
| `PER-PART-AUDIT.md` | 33-row six-field matrix |
| `PER-PART-AUDIT-SUMMARY.md` | 0/6/18/9 counts + top blockers |
| `commissioning-gates.md` | Signed traveler boxes |
| `CUT-FORM-REGISTER.md` | Human cut/form walk |
| `BOM-MAT-VERIFY.md` | BOM/MAT gaps (tip `9eb43ea`; PR #4 note) |
| `README.md` | Pack reading order |

---

*End PHASE-PLAN-REDEF Rev A.1. CONDITIONAL / NO-GO cut. PRELIMINARY — VERIFY ON VEHICLE — NOT LTO-CERTIFIED. Fabricator send HOLD.*
