---
type: concept
title: SUMIFS and COUNTIFS
aliases: []
tags: [Excel, functions, logic]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Trump Excel - How to Use Excel SUMIFS Function (Examples + Video)]]", "[[Trump Excel - How to Use Multiple Criteria in Excel COUNTIF and COUNTIFS]]", "[[Macabacus - Steps to Summarize Data with SUMIF-SUMIFS (Downloadable Template)]]", "[[Wall Street Prep - COUNTIFS Function in Excel - Formula + Calculator]]"]
status: draft
updated: 2026-04-18
---

# SUMIFS and COUNTIFS

> **TL;DR.** SUMIFS and COUNTIFS are Excel functions used to conditionally sum or count cells that meet multiple specified criteria.

## When you'd use this

You would use these functions when performing financial or data analysis where you need to aggregate data based on more than one condition. For instance, calculating the total revenue generated from a specific product line in a particular region, or counting the number of employees in a given department who have been with the company for over five years.

## The 30-second version

The `SUMIFS` function adds values in a range that meet multiple criteria. It requires the range to sum, followed by pairs of criteria ranges and criteria. The `COUNTIFS` function counts the number of cells that meet multiple criteria, requiring pairs of criteria ranges and criteria. Both functions use `AND` logic, meaning all conditions must be true for a cell to be summed or counted.

## The full explanation

### SUMIFS

The `SUMIFS` function adds the values in a specified sum range if all the corresponding criteria are met.

**Syntax:**
`=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], …)`

- **sum_range**: The range of cells to add. Blank and text values are ignored.
- **criteria_range1**: The range of cells evaluated against `criteria1`.
- **criteria1**: The condition that defines which cells in `criteria_range1` to add.
- **[criteria_range2, criteria2]**: Optional additional ranges and criteria.

### COUNTIFS

The `COUNTIFS` function counts the number of cells that meet all specified criteria.

**Syntax:**
`=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2]…)`

- **criteria_range1**: The range of cells evaluated against `criteria1`.
- **criteria1**: The condition that defines which cells to count.
- **[criteria_range2, criteria2]**: Optional additional ranges and criteria.

### Criteria Formatting

- Criteria can be numbers, text, cell references, or logical expressions.
- Logical operators (like `>`, `<`, `>=`, `<=`, `<>`) and text must be enclosed in double quotes (e.g., `">10"`, `"Technology"`).
- If combining an operator with a cell reference, enclose the operator in double quotes and use an ampersand (`&`) to join it to the reference (e.g., `">"&D3`).
- Wildcards can be used for partial matches: `*` for any number of characters and `?` for a single character. Use `~` to escape wildcards.

## Formula

The syntax formulas are:
`=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], …)`
`=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2]…)`

## Worked example

Here is an example of `SUMIFS` calculating the total investments made in the Healthcare sector in North America and Europe:
`=SUMIFS(InvestmentData[Investment Amount], InvestmentData[Sector], "Healthcare", InvestmentData[Region], "North America") + SUMIFS(InvestmentData[Investment Amount], InvestmentData[Sector], "Healthcare", InvestmentData[Region], "Europe")`

Here is an example of using `COUNTIFS` to count final exam grades that are greater than or equal to 90 for students who attended the review session:
`=COUNTIFS(C6:C13,">=90",D6:D13,"=Yes")`

## Excel and modeling notes

- Cells in `sum_range` are added only when all the corresponding criteria are met.
- The size of the `sum_range` and all `criteria_range` arguments must be identical. If they differ, the formula will return an error or unexpected results.
- `SUMIFS` is often used instead of `SUMIF` even with a single condition, as it's easier to append conditions later without rearranging the formula structure.
- Consider using named ranges or Excel Tables to make formulas more readable and easier to maintain.
- Do not use `COUNTA` to count non-blank cells because it will also count a cell that contains an empty string (often returned by formulas as `=""` or when people enter only an apostrophe). Instead, use `COUNTIF` with `"?*"` to count text, along with counting numbers and logical values.

## Interview-ready answer

`SUMIFS` and `COUNTIFS` are powerful aggregation functions in Excel that allow you to sum or count values based on multiple conditions. They are essential for segmenting financial data, such as summing sales by region and product, or counting transactions within a specific date range.

## Pitfalls and gotchas

- **Unequal Range Sizes:** The `sum_range` and all `criteria_range` arguments must be the exact same size.
- **Syntax Errors with Operators:** When using operators with cell references, forgetting to put operators in quotes and using the `&` symbol (e.g., `">"&A1`) is a common mistake.
- **Trailing Spaces:** Leading or trailing spaces in the data or criteria can cause matches to fail. Use the `TRIM` function to clean data first.

## Sources

- [[Trump Excel - How to Use Excel SUMIFS Function (Examples + Video)]]
- [[Trump Excel - How to Use Multiple Criteria in Excel COUNTIF and COUNTIFS]]
- [[Macabacus - Steps to Summarize Data with SUMIF-SUMIFS (Downloadable Template)]]
- [[Wall Street Prep - COUNTIFS Function in Excel - Formula + Calculator]]