---
type: question
title: "What is the difference between sensitivity analysis and scenario analysis"
tests: ["[[Sensitivity analysis]]"]
difficulty: beginner
updated: 2026-04-12
---

# What is the difference between sensitivity analysis and scenario analysis

## The question

What is the difference between sensitivity analysis and scenario analysis?

## Short answer (30 seconds)

Sensitivity analysis changes one or two input variables at a time while holding everything else constant to isolate their specific impact on the output. Scenario analysis changes multiple variables simultaneously to model coherent alternative futures, typically using base, bull, and bear cases.

## Long answer (2 minutes)

While both techniques are used to evaluate uncertainty in financial models, they serve different purposes and are constructed differently:

- **Sensitivity Analysis** is designed to isolate the impact of specific drivers. It uses data tables to show how a single output (like implied share price) changes when you alter just one or two inputs (like WACC and terminal growth rate). This helps identify which assumptions matter the most to the final valuation.
- **Scenario Analysis** models coherent alternative realities. It recognizes that if revenue growth slows significantly, margins will likely compress as well. Therefore, it changes a whole suite of variables simultaneously to create internally consistent "Base," "Bull," and "Bear" cases.

In practice, bankers use both techniques together. A pitch book will often show a sensitivity table based on the base case assumptions, alongside a scenario comparison table that presents the outputs of the three different cases.

## Common follow-ups

- **How do you present sensitivity analysis in a model?** By using one-variable or two-variable data tables in Excel, or tornado charts to rank variables by impact.
- **How do you build scenario analysis?** Using a scenario toggle (dropdown) that changes all underlying assumptions in the model simultaneously.
