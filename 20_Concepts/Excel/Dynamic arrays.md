---
type: concept
title: Dynamic arrays
aliases: ["spill arrays", "dynamic array formulas"]
tags: ["Excel", "formula-engine", "spilling"]
difficulty: intermediate
prerequisites: ["[[Array formulas]]"]
related: ["FILTER function", "SORT function", "UNIQUE function"]
sources: ["[[ExcelJet - Dynamic array formulas in Excel - Exceljet]]"]
status: draft
updated: 2024-05-01
---

# Dynamic arrays

> **TL;DR.** Dynamic arrays are a modern Excel feature that allows a single formula to evaluate multiple values and automatically return ("spill") the results into a range of adjacent cells.

## When you'd use this

You use dynamic arrays when you need to perform calculations on a range of data that results in multiple outputs, such as extracting unique values, sorting a list, or filtering data based on criteria. They eliminate the need for complex, manual, multi-cell array formulas or rigid lookup structures.

## The 30-second version

Introduced in Excel 365, dynamic arrays fundamentally change the formula engine. Instead of a formula returning a single value or requiring the legacy `Ctrl+Shift+Enter` (CSE) syntax to evaluate multiple items, formulas natively return arrays. When a formula's result contains multiple values, Excel automatically "spills" those values onto the worksheet into an appropriately sized range, known as the spill range.

## The full explanation

### Spilling and the Spill Range

In Dynamic Excel (Excel 365 and 2021+), if a formula returns an array of values, it dynamically allocates the required cells to display the output. The rectangle that encloses these values is called the "spill range". If the source data changes, the spill range expands or contracts accordingly. If existing data blocks the spill range, Excel returns a `#SPILL!` error until the space is cleared.

### The Spill Operator (`#`)

You can reference an entire dynamic array by appending a hash symbol (`#`) to the address of the top-left cell of the spill range. For example, if a `UNIQUE` function in cell `E5` spills down to `E10`, referencing `E5#` in another formula will automatically reference the entire `E5:E10` range. If the spill range resizes, `E5#` continues to capture the correct, updated range.

### Implicit Intersection (`@`)

Implicit intersection is the process of reducing an array of values to a single value. In Legacy Excel, this often happened silently. In modern Excel with dynamic arrays, the `@` operator is explicitly used to force implicit intersection, preventing a formula from spilling when only a single value is intended.

### "Lifting"

Lifting is an automatic behavior where a function not originally programmed to accept arrays natively (like `EOMONTH`) is called multiple times by Excel—once for each value in the provided array. Sometimes older functions resist spilling and return `#VALUE!`. This can often be bypassed by prepending a `+` operator to the range reference (e.g., `EOMONTH(+A1:A5, 1)`), forcing Excel to evaluate the array first.

## Formula

`=UNIQUE(B5:B15)`

## Worked example

If you want to extract unique cities from a list in `B5:B15`, you can use the `UNIQUE` function in a single cell, such as `E5`:

1. Enter `=UNIQUE(B5:B15)` into cell `E5`.
2. The formula will extract the unique values and dynamically "spill" them down into `E5:E9` (if there are 5 unique cities).
3. If the underlying data in `B5:B15` changes, the spilled range will automatically update.

## Excel and modeling notes

- Dynamic arrays significantly reduce the need for absolute (`$A$1`) or mixed references since one formula can calculate the whole range.
- Array operations are intuitive; you can run logical tests against whole ranges (e.g., `B5:B9="ca"`) which returns an array of `TRUE`/`FALSE` values natively.

## Interview-ready answer

Dynamic arrays are an update to Excel's calculation engine that allows a single formula to return multiple results that "spill" into adjacent cells dynamically. This removes the need for legacy Control-Shift-Enter array formulas and introduces a `#` operator to dynamically reference expanding or contracting data ranges.

## Pitfalls and gotchas

- Blocked spill ranges will result in a `#SPILL!` error, requiring you to clear the obstructing cells.
- Older functions might not spill naturally when provided a range, requiring the `+` operator workaround to force array evaluation.
- Sharing files with Legacy Excel users (2019 or older) can break dynamic arrays, as those versions do not support spilling and rely on implicit intersection (indicated by injected `@` symbols).

## Sources

- [[ExcelJet - Dynamic array formulas in Excel - Exceljet]]
