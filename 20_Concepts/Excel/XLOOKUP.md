---
type: concept
title: "XLOOKUP"
aliases: []
tags: ["excel-modeling", "lookup", "functions"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[BIWS - XLOOKUP in Excel- How to Use It, and Whether Or Not It’s a Game-Changer (14-38)]]", "[[Trump Excel - Excel XLOOKUP Function- All You Need to Know (10 Examples)]]"]
status: stub
updated: 2026-04-18
---

# XLOOKUP

> **TL;DR.** XLOOKUP is an improved Excel 365 function that searches a range or array and returns an item corresponding to the first match it finds, without the limitations of VLOOKUP.

## When you'd use this

You would use XLOOKUP when you need to search for a value in a table and return a corresponding value from another column or row. It is especially useful when the return column is to the left of the search column, when you need a default value for missing matches, when you need to search from bottom to top, or when you are performing two-way lookups.

## The 30-second version

XLOOKUP is designed to replace VLOOKUP, HLOOKUP, and INDEX/MATCH. It requires a lookup value, a lookup array, and a return array. Unlike VLOOKUP, it doesn't require a column index number, making it robust against column insertions and allowing you to fetch values to the left of the lookup value. It also natively handles missing values and can search in any direction.

## The full explanation

XLOOKUP is an Office 365 exclusive function intended to be an improved version of older lookup functions like VLOOKUP, HLOOKUP, and INDEX/MATCH.

It fixes several major limitations of older functions:
- It can search in any direction, not just left to right, meaning you can look up values to the left of your search column.
- It returns a reference to an array, not a value based on a hardcoded column number, making it immune to column insertions.
- It has built-in support for handling errors (when data is not found) via its optional `[if_not_found]` argument.
- It can search from first-to-last or last-to-first using the `[search_mode]` argument.
- It supports exact matches, exact or next smaller item, exact or next larger item, and partial matching using wildcards.
- It can do horizontal or vertical lookups.

Nested XLOOKUP functions can also replace the INDEX/MATCH combo for two-way lookups, resulting in slightly shorter formulas. Because of the `[if_not_found]` argument, XLOOKUP functions can also be nested to lookup in multiple ranges or tables.

## Formula

The syntax is `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`

For example, calculating a discounted price:
`=H3 * (1 - XLOOKUP(E3, Schools!$C$3:$C$17, Schools!$E$3:$E$17, 0, 0))`

A nested XLOOKUP for a 2-way lookup:
`=XLOOKUP(B21, $B$2:$E$2, XLOOKUP(C20,$C$2:$C$17, $B$2:$E$17, “N/A”))`

Finding the last matching value:
`=XLOOKUP(F1, $B$2:$B$15, $C$2:$C$15, , , -1)`

## Worked example

To find the discounted price after a group discount a school receives:
1. Normal price is in cell H3.
2. The promo code is in cell E3.
3. The promo codes are in `Schools!$C$3:$C$17` and the discounts are in `Schools!$E$3:$E$17`.
4. If a promo code isn't found, the discount should be `0` (no discount).
5. Exact match mode is `0`.

The formula is:
`=H3 * (1 - XLOOKUP(E3, Schools!$C$3:$C$17, Schools!$E$3:$E$17, 0, 0))`

This correctly outputs the final discounted price and avoids #N/A errors if no promo code is provided.

## Excel and modeling notes

- You can natively handle errors by providing the `[if_not_found]` argument directly inside XLOOKUP, bypassing the need for an `IFERROR` wrapper.
- Unlike VLOOKUP, inserting or deleting columns in the middle of your lookup array will not break XLOOKUP because it uses explicit cell references for the return array instead of a static column number.
- You can specify wildcard matches by setting the `[match_mode]` argument to `2`.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- The biggest drawback is backwards compatibility: it is not backward compatible and doesn't work in older standalone versions of Excel (2019, 2016, etc.), so it will return errors if your model is opened in an older version of Excel.

## Gaps

- Missing interview-ready answer

## Sources

- [[BIWS - XLOOKUP in Excel- How to Use It, and Whether Or Not It’s a Game-Changer (14-38)]]
- [[Trump Excel - Excel XLOOKUP Function- All You Need to Know (10 Examples)]]
