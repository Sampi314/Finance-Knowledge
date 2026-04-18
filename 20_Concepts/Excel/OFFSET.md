---
type: concept
title: "OFFSET"
aliases: ["OFFSET function"]
tags: ["excel", "modeling-craft", "scenario-analysis", "depreciation"]
difficulty: intermediate
prerequisites: ["[[INDEX MATCH vs VLOOKUP]]", "[[CHOOSE]]"]
related: ["[[XLOOKUP]]"]
sources: ["[[Sumproduct - A to Z of Excel Functions- The OFFSET Function]]", "[[A Simple Model - Excel- =OFFSET() vs. =CHOOSE() - A Simple Model]]", "[[Sumproduct - Using OFFSET for Scenario Analysis]]", "[[Sumproduct - Using OFFSET for Depreciation]]"]
status: draft
updated: 2026-04-18
---

# OFFSET

> **TL;DR.** OFFSET returns a reference to a range that is a specified number of rows and columns from a given reference cell, optionally sizing it by height and width.

## When you'd use this

You would use the OFFSET function for scenario selection where the number of scenarios might change or for dynamic arrays like a depreciation schedule. Its main advantage is its ability to adjust to ranges of varying lengths and sizes dynamically, which works well when expanding model periods or adding scenario parameters, though it comes at the cost of recalculation overhead.

## The 30-second version

The OFFSET function uses a starting cell and counts a defined number of rows down and columns right to return a new reference. Its structure is `OFFSET(reference, rows, columns, [height], [width])`. Unlike other lookup functions such as CHOOSE or INDEX, OFFSET does not require hardcoding or linking directly to explicit ranges. Instead, you supply a base cell, shift positions, and optionally define a range size using the height and width arguments. This makes OFFSET extremely versatile but volatile.

## The full explanation

The syntax of the OFFSET function is:

`OFFSET(reference, rows, columns, [height], [width])`

- **reference:** The starting cell or range.
- **rows:** The number of rows to move down (positive) or up (negative) from the reference.
- **columns:** The number of columns to move right (positive) or left (negative) from the reference.
- **height:** (Optional) The height of the returned range in rows. Defaults to the height of the reference.
- **width:** (Optional) The width of the returned range in columns. Defaults to the width of the reference.

For example, if you input `OFFSET(A1,2,3)`, Excel will move 2 rows down and 3 columns to the right, landing on cell D3.

You can also use OFFSET to define a multi-cell range dynamically using the optional `[height]` and `[width]` arguments. A formula like `OFFSET(D4,-1,-2,-2,3)` evaluates to the range B2:D3, which can then be summed or averaged.

## Formula

`OFFSET(reference, rows, columns, [height], [width])`

## Worked example

Consider creating a scenario table. The assumptions for Scenario 1 are stored in column M, Scenario 2 in column N, and so on. The active scenario index is in cell H12 (e.g., 1). A formula like `OFFSET(M18,,$H$12)` will start at cell M18, move zero rows down, and move exactly H12 columns across. If H12 is 1, it shifts one column right and selects Scenario 1's values in column N. This allows you to add an unlimited number of scenarios without rewriting your formulas, whereas a CHOOSE function would require you to link each new scenario directly inside the formula.

## Excel and modeling notes

- OFFSET is a volatile function. It recalculates every time any cell in the workbook changes, which can drastically slow down large models.
- The function is also "non-auditable" by Excel's Trace Dependents auditing tool. Excel only recognizes the starting `reference` cell as a precedent, not the dynamic destination cells.
- To flag an OFFSET function's starting cell to auditors, prefix the cell's named range with `BC_` (Base Cell) and optionally color-code it so users know not to delete it.

## Interview-ready answer

The OFFSET function returns a reference shifted by a specified number of rows and columns from a starting cell. While extremely powerful for dynamic scenario selectors or depreciation waterfalls, it is a volatile function that recalculates on every workbook change, meaning it can slow down complex financial models.

## Pitfalls and gotchas

- OFFSET is volatile and slows down workbook calculation speed.
- The Trace Dependents feature does not detect cells linked via an OFFSET function, making auditing harder.
- Supplying negative dimensions for height and width may confuse newer Excel versions or array returns.

## Sources

- [[Sumproduct - A to Z of Excel Functions- The OFFSET Function]]
- [[A Simple Model - Excel- =OFFSET() vs. =CHOOSE() - A Simple Model]]
- [[Sumproduct - Using OFFSET for Scenario Analysis]]
- [[Sumproduct - Using OFFSET for Depreciation]]