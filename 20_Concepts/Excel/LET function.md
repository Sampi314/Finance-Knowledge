---
type: concept
title: "LET function"
aliases: ["LET"]
tags: ["excel", "functions", "formulas", "performance"]
difficulty: intermediate
prerequisites: []
related: ["LAMBDA function"]
sources: ["[[ExcelJet - Excel LET function - Exceljet]]", "[[Trump Excel - LET Function in Excel (Basic & Advanced Examples)]]"]
status: stub
updated: 2026-04-09
---

# LET function

> **TL;DR.** The LET function allows you to define named variables in an Excel formula to eliminate redundant calculations and make complex formulas easier to read.

## When you'd use this

You'd use the LET function when writing long or complex formulas where the same calculation is repeated multiple times. It's particularly useful when dealing with Nested IFS or large array formulas where performance or readability is a concern.

## The 30-second version

The LET function assigns names to calculation results or values, allowing you to use those names within a formula instead of repeating the calculation. This improves calculation performance by computing the value once, and improves readability by giving descriptive names to complex formula components.

## The full explanation

The LET function defines named variables inside a formula. It can handle up to 126 name/value pairs, but only the first pair is required. The variables are evaluated in order and their scope is limited to the current LET function and its nested functions.

### Key Benefits

1. **Clarity** - Naming variables makes complex formulas much easier to read and understand.
2. **Simplification** - Defining variables in one place eliminates redundancy and helps prevent errors from duplicated code.
3. **Performance** - Eliminating redundant calculations means faster processing, as expensive calculations are only executed once.

### Syntax

`=LET(name1, value1, [name2/value2], ..., result)`
- *name1*: The name you assign to the first value. Must begin with a letter, cannot contain spaces, and cannot look like a cell reference (e.g., A1, ct1).
- *value1*: The value or calculation assigned to name1.
- *result*: The final calculation returned by the function. Must always be the last argument.

## Formula

`=LET(name1, value1, [name2/value2], ..., result)`

## Worked example

Here is a simple example to calculate the final price with tax added, using variables for price and tax rate.

`=LET(price,B2:B4, taxrate,C2:C4, price*(1+taxrate))`

- `price` stores the values in B2:B4.
- `taxrate` stores the values in C2:C4.
- `price*(1+taxrate)` is the final calculation that returns the result.

## Excel and modeling notes

- Variable names in LET are not case-sensitive.
- You can use an underscore (_) in the name, but not spaces or punctuation symbols.
- A variable name cannot be the output of a formula and must not conflict with range syntax (like B10).

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Variable names that look like cell references (e.g., `ct1`) will cause an error.
- The last argument of the LET function must always be a calculation that returns the final result.

## Gaps

- Missing interview-ready answer

## Sources

- [[ExcelJet - Excel LET function - Exceljet]]
- [[Trump Excel - LET Function in Excel (Basic & Advanced Examples)]]
