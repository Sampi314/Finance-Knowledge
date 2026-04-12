---
type: concept
title: "Sensitivity analysis"
aliases: []
tags: ["Valuation", "financial-modeling"]
difficulty: intermediate
prerequisites: ["[[DCF valuation]]", "[[WACC]]", "[[Terminal value]]"]
related: ["[[Gordon growth method]]", "[[Exit multiple method]]"]
sources: ["[[IB Interview Questions - Sensitivity and Scenario Analysis in Financial Modeling]]"]
status: draft
updated: 2026-04-12
---

# Sensitivity analysis

> **TL;DR.** Sensitivity analysis examines how the output of a financial model changes when a single input variable is adjusted while holding all other assumptions constant.

## When you'd use this

Sensitivity analysis is used in virtually every DCF valuation, LBO model, and merger analysis to understand the risks embedded in any valuation or investment thesis. You would use it to show the range of potential outcomes, rather than relying on a single-point estimate. It is heavily featured in pitch books, investment committee memos, and board presentations to quickly communicate upside and downside risks.

## The 30-second version

Every financial model is built on assumptions that will inevitably be somewhat wrong. Sensitivity analysis answers the question of how much the final answer (e.g., enterprise value, implied share price, IRR, or EPS accretion/dilution) changes when those assumptions are wrong. It isolates the impact of individual variables, often using one-variable or two-variable data tables in Excel, to show decision-makers which inputs have the greatest influence on the outcome.

## The full explanation

Sensitivity analysis transforms a financial model from a fragile single-point estimate into a robust analytical framework. It tests the boundaries of your valuation by systematically altering key drivers.

In practice, a two-variable data table is the workhorse of sensitivity analysis. It calculates an output for every combination of two input ranges. For example, by varying the Weighted Average Cost of Capital (WACC) across the top row and the Terminal Growth Rate down the side column, you generate a grid of implied share prices. This proves that a company's valuation is a range, not an absolute number.

Different models require sensitizing different variables:
- **DCF Valuation:** WACC vs. Terminal Growth Rate, or EBITDA Exit Multiple vs. WACC.
- **LBO Model:** Entry Multiple vs. Exit Multiple, Leverage vs. Exit Multiple, or Revenue Growth vs. EBITDA Margin.
- **Merger Model:** Purchase Price Premium vs. Synergies Realized, or Purchase Price vs. Financing Mix (Debt vs. Equity).

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

Building a two-variable data table in Excel uses the Data Table function (Data > What-If Analysis > Data Table).
- The top-left cell links to your output formula (e.g., implied share price).
- The top row contains the range for Variable 1.
- The left column contains the range for Variable 2.

A well-formatted table highlights the base case cell, centers the base case in the middle of the table, uses consistent intervals for the variables, applies green-to-red conditional formatting for visual impact, and clearly labels the axes. For a more visual presentation, tornado charts can be used to rank variables by their overall impact on the model's output.

## Interview-ready answer

If asked what you would sensitize in a DCF, explain that you would sensitize WACC against the Terminal Growth Rate, or WACC against the Exit Multiple. This is because the terminal value typically drives 60-80% of the total enterprise value, making the model highly sensitive to small changes in these particular assumptions. Mentioning that valuation is highly assumption-dependent shows analytical maturity.

## Pitfalls and gotchas

- **Burying the results:** Sensitivity tables should be placed on the same page as the valuation summary in a pitch book, not hidden in an appendix.
- **Inconsistent intervals:** Ensure the variable ranges use sensible, consistent increments (e.g., 0.5% jumps for WACC, not random variations).
- **Confusing it with scenario analysis:** Sensitivity analysis isolates one or two variables at a time, whereas scenario analysis models coherent alternative futures by changing multiple variables simultaneously (base, bull, bear).

## Sources

- [[IB Interview Questions - Sensitivity and Scenario Analysis in Financial Modeling]]
