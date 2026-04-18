---
type: concept
title: "CHOOSE"
aliases: []
tags: ["excel", "modeling", "functions", "scenario-analysis"]
difficulty: beginner
prerequisites: []
related: ["[[IF and nested IF]]", "[[IFS function]]", "[[INDEX MATCH vs VLOOKUP]]"]
sources: ["[[Wall Street Prep - CHOOSE Function in Excel - Formula + Calculator]]", "[[ExcelJet - Excel CHOOSE function - Exceljet]]", "[[A Simple Model - Excel- =OFFSET() vs. =CHOOSE() - A Simple Model]]"]
status: stub
updated: 2026-04-18
---

# CHOOSE

> **TL;DR.** The CHOOSE function in Excel returns a value from a specified list based on an index number.

## When you'd use this

You would use the CHOOSE function primarily for scenario analysis in financial modeling. It allows you to create a "toggle" cell that switches a model between different cases (e.g., Base Case, Upside Case, Downside Case) by selecting the corresponding set of assumptions from a list.

## The 30-second version

The Excel CHOOSE function takes an index number (from 1 to 254) as its first argument and uses it to select a value from the subsequent arguments provided. For example, if the index number is 2, it returns the second value listed after the index. The values you provide can be hard-coded numbers, text, formulas, or cell references. In financial models, this index number often links to a scenario selector (like a dropdown menu), allowing the model's outputs to dynamically update based on the chosen scenario.

## The full explanation

The `CHOOSE` function is a straightforward lookup function that returns a value from a list based on its position.

### Syntax
The basic syntax is `=CHOOSE(index_num, value1, [value2], ...)`.
- **index_num**: A number between 1 and 254 that specifies which value argument to return.
- **value1, value2, ...**: The list of values to choose from. These can be numbers, text, cell references, or formulas.

### Scenario Analysis
In financial modeling, `CHOOSE` is heavily utilized to build scenario toggles. Models typically contain at least three scenarios:
1. **Base Case**: The most likely outcome with conservative assumptions.
2. **Upside Case**: An optimistic, "best case" scenario.
3. **Downside Case**: A pessimistic, "worst case" scenario.

By assigning each case an index number (e.g., 1 for Base, 2 for Upside, 3 for Downside), you can use `CHOOSE` to pull the appropriate growth rates, margins, or other assumptions into the model's active forecast column. When the user changes the index number in the toggle cell, all formulas using `CHOOSE` instantly update to reflect the new scenario.

## Formula

`=CHOOSE(index_num, value1, [value2],...)`

- `index_num`: Specifies which of the following value arguments to return, an integer from 1 to 254.
- `value1`: Required argument that can be a number, range, cell reference, formula, or text.
- `value2`: Optional argument that could be a number, range, cell reference, formula, or text.

## Worked example

Suppose a company's revenue growth depends on the active operating case:
- Upside Case (Case = 2): 5.0% YoY
- Downside Case (Case = 3): (2.0%) YoY

If the case switch is in cell `Case` and the assumptions are in cells `F12`, `F13`, and `F14`, the formula to select the growth rate is:
`=CHOOSE(Case, F12, F13, F14)`

To calculate the new revenue based on the prior year's revenue and the chosen growth rate:
`Forecasted Revenue = Prior Revenue * (1 + CHOOSE(Case, F12, F13, F14))`

If `Case` is 2, it grows by 5.0% YoY, or decline by 2.0% if set to 3.

## Excel and modeling notes

- If `index_num` is out of range (e.g., you provide an index of 4 but only list 3 values), `CHOOSE` will return a `#VALUE!` error.
- `CHOOSE` cannot directly retrieve an item from inside a contiguous range or array constant (e.g., `=CHOOSE(2, A1:A3)` returns an error). You must list the cells individually: `=CHOOSE(2, A1, A2, A3)`.
- While simple and intuitive, `CHOOSE` can become cumbersome if you frequently add or delete scenarios, as you must manually update the formula to include or remove direct links to each new scenario cell. In such dynamic situations, using the `OFFSET` function might be a more flexible alternative.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- **Direct linking limitations**: If you add a new scenario row to your assumptions table, formulas using `CHOOSE` will not automatically expand to include it; you must edit the formula to add the new cell reference.
- **Out-of-bounds index**: Entering an index number that exceeds the number of provided values results in a `#VALUE!` error.
- **Range references**: Attempting to pass a single range (like `A1:A5`) as the value arguments instead of individual references will not work for selecting the nth item within that range.

## Gaps
- Missing interview-ready answer

## Sources

- [[Wall Street Prep - CHOOSE Function in Excel - Formula + Calculator]]
- [[ExcelJet - Excel CHOOSE function - Exceljet]]
- [[A Simple Model - Excel- =OFFSET() vs. =CHOOSE() - A Simple Model]]
