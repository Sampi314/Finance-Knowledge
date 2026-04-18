---
type: concept
title: "Array formulas"
aliases: []
tags: ["excel", "modeling", "formulas"]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[Sumproduct - Array of Light]]", "[[A Simple Model - Arrays in Excel Without Ctrl+Shift+Enter - A Simple Model]]"]
status: stub
updated: 2026-04-18
---

# Array formulas

> **TL;DR.** Array formulas perform multiple calculations on one or more items in an array, returning either a single aggregated result or multiple results.

## When you'd use this

You would use array formulas when you need to perform multiple calculations across a set of data in a single step. They are particularly useful for complex criteria-based calculations, such as finding the most recent date that meets a specific condition without sorting the data.

## The 30-second version

An array in Excel is a contiguous set of items in a single row or column. Array formulas evaluate multiple values within these arrays simultaneously. They can return a single aggregated value using functions like SUM, MAX, or AVERAGE, or return multiple values across several cells using functions like TRANSPOSE. Historically, many array formulas required pressing CTRL+SHIFT+ENTER to execute, enclosing the formula in braces `{}`.

## The full explanation

In Excel, arrays can be a one-dimensional horizontal array (a row), a one-dimensional vertical array (a column), or a two-dimensional array (a table). Array formulas perform calculations on these arrays to return either single or multiple outputs.

### Single-cell Array Formulas
These formulas work with an array of data and aggregate it using functions like SUM, AVERAGE, MIN, MAX, or COUNT to return a single value.

### Multi-cell Array Formulas
These formulas return a result into two or more cells. Functions like MINVERSE, LINEST, and TRANSPOSE inherently return arrays of values as their result.

### Ctrl+Shift+Enter (CSE)
While some functions natively handle arrays (like SUMPRODUCT or INDEX), Excel often needs to be told it's evaluating an array formula. This is done by entering the formula using CTRL+SHIFT+ENTER, which adds braces `{}` around the formula. Alternatively, advanced users often nest standard functions that create arrays within other functions to accomplish the same goals without needing a CSE formula, which makes models more flexible.

## Formula

`={MAX(IF($G$18:$G$40<=$G$14,$F$18:$F$40))}`

The central formula checks which data is less than or equal to the target value and returns the corresponding dates. MAX() takes the largest value (the most recent date).

## Worked example

**Dates Challenge**
Given a two-column data file (dates and data), you need to return the most recent date at which the corresponding data was less than or equal to a target value. The dates are not necessarily in ascending order. Using an array formula allows you to find the most recent (biggest) date out of a list of dates that meet the condition without adding a helper column.

## Excel and modeling notes

- Array formulas can accomplish tasks that would otherwise require multiple helper columns, making models more concise.
- However, complex array formulas can be difficult for end-users to understand and audit.
- Large array formulas can significantly slow down calculation times or cause Excel to stop calculating without providing an error message.
- Some advanced users prefer nested standard functions over explicit array formulas to maintain flexibility and avoid CSE requirements.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Multi-cell array formulas require selecting the exact range of output cells before entering the formula.
- Individual cells within a multi-cell array formula cannot be edited or deleted independently.
- Array formulas are often less intuitive for junior analysts to review.
- They can cause severe performance issues in large financial models.

## Gaps

- Missing interview-ready answer

## Sources

- [[Sumproduct - Array of Light]]
- [[A Simple Model - Arrays in Excel Without Ctrl+Shift+Enter - A Simple Model]]
