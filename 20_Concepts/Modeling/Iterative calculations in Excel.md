---
type: concept
title: "Iterative calculations in Excel"
aliases: ["Iterative calculations"]
tags: ["modeling", "excel", "circular-references"]
difficulty: intermediate
prerequisites: ["[[Interest expense circularity]]"]
related: []
sources: ["[[BIWS - Circular Reference Excel - How to Find and Fix Them]]", "[[Macabacus - Circular Reference in Excel - How to Find and Fix Errors]]", "[[Financial Modelling Handbook - How to manage circularity in a financial model]]", "[[Pivotal180 - DSRA Circular Reference in Excel - 3 Ways to Fix It]]", "[[A Simple Model - Broken Models & Circular References - A Simple Model]]"]
status: draft
updated: "2026-04-13"
---

# Iterative calculations in Excel

> **TL;DR.** Iterative calculations are a setting in Excel that forces the program to repeatedly recalculate circular formulas until the values converge on a solution.

## When you'd use this
You would use iterative calculations in a financial model when a circular reference naturally arises from the mechanics of the deal or accounting, such as when interest expense depends on the debt balance, but the debt balance depends on the cash flow after interest expense. This allows the model to calculate despite the circularity without using a macro.

## The 30-second version
By default, Excel will not calculate a spreadsheet if it contains a circular reference (where a cell's input depends directly or indirectly on its own output). By enabling "Iterative calculations" in Excel's Formula Options, you instruct Excel to cycle through the calculation a set number of times (e.g., 100) until the difference between iterations is extremely small (e.g., 0.0001). While it resolves the immediate calculation error, most professionals avoid it in client-facing models because it can hide unintentional circular errors, slow down the workbook, and may fail to converge on a stable output.

## The full explanation
A circular reference occurs when a formula refers directly or indirectly back to its own cell value, creating an endless loop. This happens commonly in financial modeling when calculating interest based on an average debt balance, or when sizing a Debt Service Reserve Account (DSRA) based on future debt service.

When iterative calculations are enabled, Excel will repeatedly recalculate the circular chain until the values stop changing significantly (converge) or until it hits the maximum number of iterations.

There are three common ways to manage circularity:
1. **Iterative calculations**: Quick but generally discouraged in professional modeling because they can mask unintended errors, decrease performance, and lead to unstable models.
2. **Algebraic solutions**: Using mathematical substitutions to avoid the circularity entirely, or using lagged balances (e.g., prior period debt) as an approximation.
3. **Copy-paste macros**: The industry standard for transaction models. A VBA macro copies the calculated circular value and pastes it as a hardcoded number into a static row, breaking the live formula loop. A "circularity switch" (toggle between 1 and 0) is also commonly used to manually break the loop when the model breaks.

## Formula
(none)

## Worked example
(none)

## Excel and modeling notes
To enable iterative calculations in Excel, go to `File > Options > Formulas` and check the box for "Enable iterative calculation." You can adjust the "Maximum Iterations" (typically 100) and "Maximum Change" (typically 0.0001). If using a circularity switch (e.g., cell B21 = 1 or 0), wrap the circular formula in an IF statement that multiplies or sets the value to 0 when the switch is off.

## Interview-ready answer
(none)

## Pitfalls and gotchas
- Leaving iterative calculations enabled can hide new, accidental circular references you introduce while modeling.
- If the model's logic does not naturally converge, turning on iterative calculations will cause the model to jump to different results every time you press F9 (recalculate).
- Activating iterative calculations happens at the Excel application level, meaning all open workbooks will run in iterative mode, which may unintentionally affect other files.

## Sources
- [[BIWS - Circular Reference Excel - How to Find and Fix Them]]
- [[Macabacus - Circular Reference in Excel - How to Find and Fix Errors]]
- [[Financial Modelling Handbook - How to manage circularity in a financial model]]
- [[Pivotal180 - DSRA Circular Reference in Excel - 3 Ways to Fix It]]
- [[A Simple Model - Broken Models & Circular References - A Simple Model]]
