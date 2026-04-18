---
type: concept
title: "LAMBDA function"
aliases: ["LAMBDA"]
tags: ["excel-and-modeling-craft", "functions", "formulas", "dynamic-arrays"]
difficulty: intermediate
prerequisites: ["[[LET function]]"]
related: ["[[Dynamic arrays]]"]
sources: ["[[BIWS - Excel Lambda Functions- Full Tutorial and XL Examples]]", "[[ExcelJet - Excel LAMBDA function - Exceljet]]", "[[Trump Excel - Excel LAMBDA Function - Easy Explanation with Examples]]", "[[Sumproduct - A to Z of Excel Functions- The LAMBDA Function]]", "[[Gridlines - What does Lambda mean- - Gridlines]]"]
status: draft
updated: 2024-05-24
---

# LAMBDA function

> **TL;DR.** The LAMBDA function allows you to create your own reusable custom functions in Excel without using VBA or macros.

## When you'd use this

You would use the LAMBDA function to simplify complex calculations that you use repeatedly in a workbook. It is ideal for moderately complex logic where you want a single source of truth for a formula, making it easier to read and maintain across an entire file.

## The 30-second version

In Excel, the LAMBDA function lets you define a custom function using standard Excel formula syntax. Once you create and test a generic LAMBDA formula, you add it to the Name Manager to give it a memorable name. You can then use this named function anywhere in your workbook, just like native Excel functions. This eliminates the need for copy-pasting complex logic or writing VBA code, allowing for cleaner, more portable, and easier-to-update models.

## The full explanation

The LAMBDA function works by taking input parameters and a final calculation. The general syntax is `=LAMBDA(parameter1, parameter2, ..., calculation)`.

Creating a custom function with LAMBDA involves a few steps:
1. Build and test the logic using standard cell references.
2. Convert the formula into an unnamed LAMBDA function, testing it by appending values in a separate set of parentheses at the end, such as `=LAMBDA(x, y, x*y)(5, 10)`.
3. Open the Name Manager (Ctrl + F3), create a new name, and paste the LAMBDA formula (without the testing parameters) into the "Refers to" field.
4. Call the newly named function anywhere in the workbook.

LAMBDAs also support recursion, meaning a LAMBDA function can call itself to perform looping calculations, making Excel formulas Turing complete.

## Formula

![[LAMBDA]]

## Worked example

[[Multiple of Invested Capital (MOIC) Lambda]]

## Excel and modeling notes

- Use the `LET` function inside a LAMBDA to declare variables and simplify complex logic, reducing redundant calculations.
- It is best used for calculations that require moderate error-checking but aren't overly complex. Very nuanced error-checking or looping through entire sheets might still be better suited for VBA.
- Use `Alt + Enter` to add line breaks in the Formula Bar to make editing complex LAMBDA functions easier.

## Interview-ready answer

The LAMBDA function is a recent Excel addition that allows users to create custom, reusable functions without writing VBA code. You define the input parameters and the calculation, then save it in the Name Manager. This reduces formula errors, simplifies auditing, and ensures formula logic exists in just one place.

## Pitfalls and gotchas

- If you attempt to enter a LAMBDA without its test parameters (e.g., `=LAMBDA(x, x+1)`) directly in a cell, Excel will return a `#CALC!` error.
- You cannot name a custom LAMBDA the same as an existing Excel function (e.g., `SUM`), as Excel will default to its native function, ignoring your custom one.
- LAMBDA functions are tied to the workbook's Name Manager, meaning they are not automatically portable to other files unless explicitly defined in them.
- Recursive LAMBDAs need careful handling; if they refer to their own name before it's properly defined in the Name Manager, they will produce errors.

## Sources

- [[BIWS - Excel Lambda Functions- Full Tutorial and XL Examples]]
- [[ExcelJet - Excel LAMBDA function - Exceljet]]
- [[Trump Excel - Excel LAMBDA Function - Easy Explanation with Examples]]
- [[Sumproduct - A to Z of Excel Functions- The LAMBDA Function]]
- [[Gridlines - What does Lambda mean- - Gridlines]]
