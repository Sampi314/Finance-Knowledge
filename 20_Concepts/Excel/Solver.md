---
type: concept
title: Solver
aliases: []
tags: [excel, financial-modeling, optimization]
difficulty: intermediate
prerequisites: []
related: ["[[Goal seek]]"]
sources: ["[[Chandoo - Are you a Solver Virgin- Watch this tutorial video ..., » Chandoo.org - Learn Excel, Power BI & Charting Online]]", "[[Chandoo - CP035- on Solver, its story and future - Interview with Dan Fylstra » Chandoo.org - Learn Excel, Power BI & Charting Online]]", "[[Damodaran - Document]]"]
status: stub
updated: 2026-04-09
---

# Solver

> **TL;DR.** Excel Solver can run various permutations and combinations and find out the best possible solution for a given problem.

## When you'd use this

You would use Solver when you need to answer questions like finding the maximum profits you can make, the best way to schedule employees in shifts, or the best combination of tasks you can finish in a given time. It is like Goal Seek, but better and more capable of handling complex optimization algorithms. It can also be used to estimate the probability of distress for a bond by setting a model's value equal to the market price of the bond.

## The 30-second version

For a given problem, Excel Solver can run various permutations and combinations to find the best possible solution for you. It's an optimization tool created by Dan Fylstra. In order to make the best use of solver, you need to define your problem very clearly and model it using Excel.

## The full explanation

Solver is a powerful optimization add-in in Excel. It can solve problems for you by testing many scenarios.

### Modeling Your Problem First
To use Solver effectively, you first need to model your problem clearly in Excel. This involves setting up your inputs, a calculation engine, and a target output cell. Once you have a working model, you can use Solver to find the optimal inputs to achieve a desired outcome in your target cell, subject to constraints you define.

### Tweak Solver Settings
You can modify how Solver operates by messing with its settings. This is done by clicking on the “options” button within the Solver dialog box.

## Formula

(none)

## Worked example

To estimate the probability of distress using a bond's market price:
1. Set up your model with inputs like Coupon Rate (e.g., 0.12), Maturity of bond (e.g., 8), Riskfree rate (e.g., 0.05), and Market price of bond (e.g., 653).
2. Calculate the Present Value of Cash Flows factoring in the probability of distress (p).
3. Open Solver (from tools).
4. Set the calculated present value equal to the market price of bond.
5. Solve for the probability of distress (p).

## Excel and modeling notes

Start by modeling sample problems you find in work or life to practice and master the art of using Solver. Be sure to define your problem first before trying to run the tool.

## Interview-ready answer

(none)

## Pitfalls and gotchas

- Not defining your problem clearly and modeling it correctly in Excel before using the tool.

## Gaps

- Missing exact formula
- Missing interview-ready answer

## Sources

- [[Chandoo - Are you a Solver Virgin- Watch this tutorial video ..., » Chandoo.org - Learn Excel, Power BI & Charting Online]]
- [[Chandoo - CP035- on Solver, its story and future - Interview with Dan Fylstra » Chandoo.org - Learn Excel, Power BI & Charting Online]]
- [[Damodaran - Document]]
