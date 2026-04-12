---
type: concept
title: "Interest expense circularity"
aliases: ["Circular Reference in Financial Models"]
tags: ["modeling", "corporate-finance", "debt-schedule"]
difficulty: intermediate
prerequisites: ["[[Debt schedule]]", "[[Linking the three statements]]"]
related: []
sources: ["[[A Simple Model - Broken Models & Circular References - A Simple Model]]", "[[Project Finance - Circular References in Corporate Finance]]", "[[Project Finance - Philosophy of Circular References]]"]
status: draft
updated: "2026-04-12"
---

# Interest expense circularity

> **TL;DR.** An interest expense circularity occurs when interest expense on debt drives net income and cash flow, which in turn determines the amount of debt required, changing the interest expense again.

## When you'd use this

This concept arises when integrating the three financial statements in a corporate financial model, particularly when building debt schedules where interest is calculated based on the average debt balance rather than strictly the beginning balance.

## The 30-second version

The circularity happens because of an oddly shaped calculation loop:
1. Interest Expense reduces Net Income.
2. Net Income impacts Operating Cash Flow.
3. Cash flow levels determine the debt paydown or revolver draws needed.
4. The changing debt balance affects the average debt outstanding over the period, which then alters the interest expense.
This loop causes a `#REF!` error in Excel if not managed properly.

## The full explanation

Calculating interest on the opening balance of debt assumes the entire year's cash flows happen strictly at year-end, which is unrealistic. Using an average balance (opening + closing / 2) is far more accurate but triggers the circular reference since the closing balance depends on the interest paid during the year.

There are four primary ways to resolve or manage this circularity:

1. **Iteration Button:** Excel can calculate iterations until the loop converges. However, this causes severe model instability, disables "Goal Seek," and can permanently break the model if an error elsewhere triggers a massive `#REF!` wipeout.
2. **Algebraic substitution:** Sometimes solvable algebraically without loops, but this can become incredibly complex and unwieldy in massive models with layers of debt.
3. **Copy-and-Paste Macro:** Copying the calculated interest value and pasting it over the hardcoded input until they match. It resolves the `#REF!`, but it's clunky, ruins scenario analysis efficiency, and breaks transparency.
4. **User-Defined Functions (UDFs):** The most elegant but complex solution. It involves writing a parallel custom function using VBA to perform the looping logic behind the scenes, outputting a stable, reliable number back to the spreadsheet.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

To turn on Iterative Calculation in Excel (if absolutely necessary): Go to File > Options > Formulas > check "Enable iterative calculation".

A standard and highly recommended modeling practice is to build a "circuit breaker" or "switch" (e.g., an input cell set to "ON" or "OFF"). You use an `=IF(switch="ON", interest_calculation, 0)` formula to temporarily turn off the interest link while you are still balancing the three statements, preventing premature `#REF!` errors before the model is fully constructed.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Relying purely on the Iteration button can make the model extremely unstable and harder to audit. If the model throws an error somewhere else, the whole workbook can immediately `#REF!` out irreparably.
- Using copy/paste macros hurts model transparency and makes sensitivity testing very slow.

## Sources

- [[A Simple Model - Broken Models & Circular References - A Simple Model]]
- [[Project Finance - Circular References in Corporate Finance]]
- [[Project Finance - Philosophy of Circular References]]
