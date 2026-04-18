---
type: concept
title: "Conditional formatting for models"
aliases: ["Conditional Formatting"]
tags: ["excel", "formatting", "modeling"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Sumproduct - Conditional Formatting]]", "[[Sumproduct - Keeping Up Appearances – Conditional Formatting]]"]
status: stub
updated: 2026-04-09
---

# Conditional formatting for models

> **TL;DR.** Conditional Formatting allows you to apply formats to a cell or range of cells and have that formatting change depending on the value of the cell or the value of a corresponding formula.

## When you'd use this

You would use conditional formatting to highlight specific cells based on their content, such as highlighting numbers greater than or less than a value, highlighting duplicates, or applying traffic light formatting with icon sets for quick visual insights.

## The 30-second version

With Excel’s IF function, the contents of a cell can be modified if a condition is met, but the formatting cannot be changed this way. Conditional formatting solves this. In older versions of Excel, it stopped once the first condition was met (up to three formats). In Excel 2007 and newer, there is no limit to the number of rules, and multiple formats can be applied at the same time. The features include options like Highlight Cells Rules, Date Occurring, Duplicate Values, Data Bars, Color Scales, and Icon Sets.

## The full explanation

Conditional formatting is accessed from the 'Styles' group of the 'Home' tab (or `ALT + O + D`). It formats cells depending on whether a condition is true.

### Rule Evaluation
In Excel 2003 and earlier, as soon as Excel finds a condition that is met, it formats the cell accordingly and stops testing further conditions. You can define up to three conditions.
In Excel 2007 and newer, testing does not have to stop once a condition is met. More than one conditional format can be applied to a cell simultaneously. The Conditional Formatting Rules Manager allows you to manage the sequence and choose whether to "stop if true" for certain conditions.

### Available Formatting Options
- **Highlight Cells Rules:** Similar to "Cell Value Is" functionalities (e.g., Greater Than, Less Than, Between, Equal To).
- **Duplicate Values:** Easily highlights duplicates without concocting complex formulas.
- **Top / Bottom Rules:** Highlights top or bottom items or percentages. The amount doesn't have to be '10' and can be customized.
- **Visual Styles:** Features like Color Scales (useful for traffic light reporting), Icon Sets (stratifying data into sections using icons), and Data Bars allow for graded shading and visualization.

## Formula

If you want to find duplicates using a formula instead of built-in conditional formatting, the formula looks like this:
`=IF(COUNTIF($A:$A,$A1)>1,COUNTIF($A$1:$A1,$A1)>1)`

Or, to find a percentile to manually recreate a bottom 37% rule:
`=Cell_Ref<=PERCENTILE(Range,0.37)`

## Worked example

To apply graded shading based on numbers:
If cells A1:A10 have the values 10, 20, 30, ..., 100 respectively, you can apply a Color Scale to those cells. Conditional formatting will automatically fill them in with graded colors representing their relative value within the range.

For applying complex number formatting with multiple conditions:
1. Construct the underlying custom number format first (e.g., setting positive and negative numbers to percentages and zeros to a hyphen).
2. Apply conditional formatting so that if the cell value is greater than 1, numbers greater than a million are displayed to the nearest 0.1m, numbers between 1,000 and a million to the nearest 0.00k, etc.
3. Apply a second conditional format for when the cell value is less than -1.

## Excel and modeling notes

Always try to add conditional formatting after completing all of the calculations in your model. This is because conditional formatting sometimes misbehaves when rows or columns are deleted and / or inserted.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Conditional formatting sometimes misbehaves when rows or columns are deleted and / or inserted.
- In Excel 2003 and earlier, the order of conditions matters because Excel stops checking once the first condition is met.

## Gaps

- Missing interview-ready answer

## Sources

- [[Sumproduct - Conditional Formatting]]
- [[Sumproduct - Keeping Up Appearances – Conditional Formatting]]