---
type: concept
title: "Goal seek"
aliases: ["Goal Seek in Excel"]
tags: ["excel", "data-analysis", "what-if-analysis"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Chandoo - Excel Goal Seek Tutorial - Learn how to use goal seek feature by building a retirement calculator in Excel]]", "[[Trump Excel - Data Analysis - Goal Seek in Excel]]"]
status: stub
updated: 2026-04-09
---

# Goal seek

> **TL;DR.** Goal Seek is an Excel feature that allows you to determine the required input value to achieve a specific target output from a formula.

## When you'd use this

You would use Goal Seek when you know the desired result of a formula but are unsure of the exact input value required to reach that result. It is particularly useful for solving simple linear equations, finding a break-even point, or determining loan amounts and interest rates.

## The 30-second version

Think of Goal Seek as the opposite of standard formula calculation. Normally, formulas take inputs and calculate an output. Goal Seek works backward: you define the target output (the goal), select the formula cell, and specify which input cell Excel should adjust. Excel will then automatically perform trial-and-error calculations to find the exact input value needed to meet your target.

## The full explanation

Goal Seek is a built-in "What-If Analysis" tool in Excel. It is designed to solve for a single variable by altering its value until a dependent formula reaches a specified target.

### How it works
The Goal Seek dialogue box requires three specific inputs:
1.  **Set cell:** The cell containing the formula that you want to reach a specific target value.
2.  **To value:** The numerical target or goal you want the formula to achieve.
3.  **By changing cell:** The cell containing the input value that Excel will adjust to reach the target. This cell must be referenced by the formula in the "Set cell".

Once executed, Excel rapidly tests different values in the changing cell. If it finds a solution, it displays a status dialogue box. You can choose to accept the solution (which permanently changes the cell value) or cancel to revert to the original value.

## Formula

(none)

## Worked example

Imagine you are calculating a monthly loan payment using the PMT function: `PMT(Interest_Rate/12, Number_of_Payments, Loan_Amount)`.
Suppose the calculated monthly payment for a certain loan amount is $1,500, but your budget only allows for a $1,000 monthly payment. You want to know what loan amount you can afford.

Using Goal Seek:
1.  **Set cell:** The cell with the PMT formula.
2.  **To value:** -1000 (negative because it's a cash outflow).
3.  **By changing cell:** The cell containing the Loan Amount.

Goal Seek will calculate and update the Loan Amount cell to the exact figure that results in a $1,000 monthly payment.

## Excel and modeling notes

(none)

## Interview-ready answer

Goal Seek is an Excel What-If Analysis tool used to find the required input value for a formula to reach a specific target output. It's essentially reverse-engineering a formula by letting Excel run trial-and-error calculations on a single variable until the goal is met.

## Pitfalls and gotchas

(none)

## Gaps
- Missing exact formula
- Missing Excel and modeling notes
- Missing pitfalls and gotchas

## Sources

- [[Chandoo - Excel Goal Seek Tutorial - Learn how to use goal seek feature by building a retirement calculator in Excel]]
- [[Trump Excel - Data Analysis - Goal Seek in Excel]]
