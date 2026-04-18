---
type: concept
title: "INDIRECT"
aliases: []
tags: [excel, financial-modeling, functions]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[Trump Excel - Excel INDIRECT Function (Explained with Examples + Video)]]", "[[Sumproduct - A to Z of Excel Functions- The INDIRECT Function]]"]
status: draft
updated: 2026-04-18
---

# INDIRECT

> **TL;DR.** The INDIRECT function in Excel converts a text string into a valid cell reference, allowing formulas to dynamically link to cells, ranges, named ranges, or other worksheets.

## When you'd use this

You would use INDIRECT when you need to dynamically build cell references from text strings rather than hardcoding them. It is particularly useful for creating dependent drop-down lists, pulling data from multiple summary sheets where worksheet names change dynamically, or locking ranges (such as in a `SUM` formula) so that they don't shift when rows or columns are inserted or deleted.

## The 30-second version

The INDIRECT function takes text as input and evaluates it as an actual cell reference. For example, if cell C1 contains the text "A1", then `=INDIRECT(C1)` will return the value stored in cell A1. You can use it to build references dynamically by concatenating text with cell values, such as referencing different worksheets based on a drop-down selection. Because INDIRECT is a volatile function, it recalculates every time Excel calculates, which can slow down large models if overused.

## The full explanation

The INDIRECT function allows the creation of a formula by referring to the contents of a cell, rather than the cell reference itself. The syntax is `=INDIRECT(ref_text, [a1])`.

- **ref_text:** A required reference to a cell that contains an A1-style reference, an R1C1-style reference, a named range, or a text string. If it is not a valid cell reference, INDIRECT returns a `#REF!` error. If it refers to an external workbook, that workbook must be open, otherwise it also returns a `#REF!` error.
- **[a1]:** An optional logical value specifying the reference type. If TRUE or omitted, `ref_text` is interpreted as an A1-style reference. If FALSE, it is interpreted as an R1C1-style reference.

### Locking Cell References

Normally, if you use `=SUM(F11:F20)`, inserting or deleting a row within that range will cause Excel to automatically adjust the formula to `=SUM(F11:F21)`. If you strictly want to sum exactly that range regardless of structural changes, `=SUM(INDIRECT("F11:F20"))` will maintain the integrity of the referenced range.

### Referencing Other Worksheets

You can use INDIRECT to pull data from other sheets by combining the sheet name with the cell reference. If cell A1 contains the name of a sheet (e.g., "Data Set"), you can dynamically pull from cell A1 of that sheet using `=INDIRECT("'"&A1&"'!A1")`. The single quotes ensure the formula still works if the worksheet name contains spaces. Similarly, using the R1C1 notation, you could use `=INDIRECT("'"&Selection&"_BA'!RC",FALSE)` to pull from multiple similarly constructed datasheets using the current formula location's row and column coordinates.

## Formula

`=INDIRECT(ref_text, [a1])`

## Worked example

Suppose cell C1 contains the number 2. Using the formula `=INDIRECT("A"&C1)` will evaluate to cell A2. To find the average of a named range called "Math", use the formula `=AVERAGE(INDIRECT("Math"))`.

## Excel and modeling notes

- **Volatility:** INDIRECT is a volatile function. This means it recalculates whenever the Excel workbook is open or whenever any calculation is triggered in the worksheet. Overusing INDIRECT in large datasets can significantly slow down processing time.
- **Dependent Drop-Down Lists:** A common advanced use case is creating dependent drop-down lists. By combining Data Validation with `INDIRECT`, the choices in a second drop-down can depend on the selection in the first drop-down by referencing a named range matching the first selection (e.g., source `=INDIRECT($D$2)`).
- **R1C1 and ADDRESS Integration:** Advanced modellers frequently combine INDIRECT with `ADDRESS` or R1C1 notation to create highly flexible, location-independent references, although this can make formulas difficult to review or audit because the cell referred to is not the ultimate location of the value used.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- It is a volatile function, which adds to processing time and can significantly slow down performance in large financial models.
- If referencing another workbook, the external workbook must be open, otherwise the function will return a `#REF!` error.
- If the evaluated text string is not a valid cell reference (or exceeds row/column limits), INDIRECT will return a `#REF!` error.
- INDIRECT encourages the use of hardcoded strings in formulas, leading to a potential lack of transparency, flexibility, and auditability in a model.

## Sources

- [[Trump Excel - Excel INDIRECT Function (Explained with Examples + Video)]]
- [[Sumproduct - A to Z of Excel Functions- The INDIRECT Function]]
