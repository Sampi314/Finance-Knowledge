---
type: concept
title: "Named ranges"
aliases: ["Named range"]
tags: ["excel-and-modeling-craft", "excel"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Trump Excel - How to Create Named Ranges in Excel (A Step-by-step Guide)]]", "[[Trump Excel - How to Delete Named Range in Excel- 2 Easy Ways!]]"]
status: draft
updated: 2026-04-13
---

# Named ranges

> **TL;DR.** Named ranges allow you to assign a memorable name to a cell or range of cells in Excel, making formulas easier to read and managing data more efficient.

## When you'd use this

You would use named ranges when dealing with complex datasets or formulas where cell references like `A2:A100` become hard to track. They are especially useful for inputs, assumptions, and specific data categories in financial models to improve clarity and reduce errors.

## The 30-second version

In Excel, instead of referring to a group of cells by their grid coordinates (e.g., `C2:C11`), you can define a custom name for them, like `Sales`. Once defined, you can use `Sales` directly in formulas, such as `=SUM(Sales)`. This makes your formulas more intuitive, saves time when selecting cells, and allows Excel's autocomplete feature to quickly suggest the range name as you type.

## The full explanation

Named ranges are a core feature in Excel that replace standard cell references with user-defined names.

### Creating Named Ranges
You can create a named range by selecting the cells and typing the desired name into the **Name Box** (located to the left of the formula bar). They can also be created dynamically using functions like `INDEX` and `COUNTIF` so that the range automatically expands when new data is added.

### Benefits
1. **Readability:** Formulas like `=SUMIF(SalesRep, "Tom", Sales)` are much easier to understand than `=SUMIF(B2:B11, "Tom", C2:C11)`.
2. **Efficiency:** You don't need to navigate back to the source dataset to select cells; you can simply type the name.
3. **Management:** All named ranges can be viewed, edited, filtered, and deleted centrally using the **Name Manager** in the Formula tab.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When managing many named ranges, the Name Manager is the go-to tool. It allows filtering to find names with errors or those scoped to specific worksheets. To delete them, you can select one or multiple ranges in the Name Manager and hit Delete. Alternatively, VBA can be used to bulk delete named ranges, for example, by looping through all ranges and deleting those containing a specific text string.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- While dynamic named ranges can be created using the `OFFSET` function, `OFFSET` is volatile and can slow down the workbook. Using `INDEX` with `COUNTIF` is a better, semi-volatile alternative.
- Dynamic named ranges relying on `COUNTIF` to determine the last row will fail or produce incorrect ranges if there are blank cells within the data.

## Sources

- [[Trump Excel - How to Create Named Ranges in Excel (A Step-by-step Guide)]]
- [[Trump Excel - How to Delete Named Range in Excel- 2 Easy Ways!]]