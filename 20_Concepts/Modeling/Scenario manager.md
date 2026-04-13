---
type: concept
title: "Scenario manager"
aliases: ["Scenario analysis"]
tags: ["modeling"]
difficulty: intermediate
prerequisites: []
related: []
sources: ["[[Trump Excel - Data Analysis - Scenario Manager in Excel]]", "[[Pivotal180 - Creating Scenarios in an Excel Financial Model]]", "[[Chandoo - Scenario Analysis for the Project Valuation Financial Modeling]]", "[[Sumproduct - Managing Scenario Manager]]", "[[Chandoo - Switch Scenarios Dynamically using Slicers]]"]
status: draft
updated: 2026-04-13
---

# Scenario manager

> **TL;DR.** Scenario manager refers to techniques used to test how changing multiple variables simultaneously affects the final outputs of a financial model.

## When you'd use this

You would use scenario analysis when a single-point estimate is insufficient for decision making. It is critical when evaluating a project or investment where inputs (like revenues, growth rates, or costs) are uncertain, allowing stakeholders to see potential outcomes across different states of the world, such as base, worst, and best cases.

## The 30-second version

A model's final outputs (like NPV or IRR) depend on its inputs. While a data table can show how one or two variables affect a result, a scenario manager can handle changes to three or more variables simultaneously. By defining sets of inputs for different "scenarios" (e.g., Optimistic, Realistic, Pessimistic), you can instantly switch the entire model to reflect those assumptions and evaluate the impact on profitability or valuation.

## The full explanation

In financial modeling, evaluating risk and potential returns requires understanding how changes to fundamental assumptions impact key metrics. When multiple assumptions must change together—to reflect a coherent view of a future state—scenario analysis is required.

There are several ways to implement scenario management in Excel:

1. **Excel's Built-in Scenario Manager:** Found under Data > What-If Analysis, this tool allows you to define up to 32 changing variables for different scenarios. You explicitly enter the values for each variable per scenario. While easy to set up and capable of generating a summary report, it has significant drawbacks: it overwrites cell formulas with hardcoded values when switching scenarios, and its outputs are not dynamic (the summary report must be regenerated if inputs change).
2. **Data Tables:** While primarily used for sensitivity analysis of one or two variables, data tables can be cleverly combined with lookup functions to evaluate different scenarios.
3. **Formula-based Scenario Selectors:** The most robust and common method in professional financial modeling is using an index or offset function. By creating a dedicated assumption sheet with a block of data where columns represent scenarios (e.g., Base, Upside, Downside) and rows represent variables, you can use a single "case selector" cell (e.g., 1, 2, or 3). Functions like `INDEX`, `OFFSET`, or `CHOOSE` look at this selector to pull the active scenario's assumptions into the model's calculation engine.
4. **Slicers and Pivot Tables:** A modern approach involves setting up scenarios in a table, creating a pivot table, and adding a Slicer. The slicer acts as an interactive button to switch the active scenario, with the model dynamically linking to the pivot table's output.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When building formula-based scenarios, the `INDEX` function is generally preferred over `OFFSET` because `OFFSET` is a volatile function that can slow down large models. Always ensure your scenario inputs are hardcoded constants and clearly separated from the model's calculation logic.

## Interview-ready answer

Scenario management is the process of testing a financial model under different sets of assumptions, such as a base, upside, and downside case. While Excel has a built-in Scenario Manager, best practice is to build a dynamic scenario selector using the `CHOOSE` or `INDEX` functions to pull active assumptions from a dedicated scenario table without breaking model formulas.

## Pitfalls and gotchas

- Using Excel's built-in Scenario Manager on a cell containing a formula will permanently replace that formula with a hardcoded value.
- Failing to fully link the model properly before running scenario analysis will result in inaccurate or static outputs.
- Using the volatile `OFFSET` function for scenario selection can drastically reduce the performance of large, complex models.

## Sources

- [[Trump Excel - Data Analysis - Scenario Manager in Excel]]
- [[Pivotal180 - Creating Scenarios in an Excel Financial Model]]
- [[Chandoo - Scenario Analysis for the Project Valuation Financial Modeling]]
- [[Sumproduct - Managing Scenario Manager]]
- [[Chandoo - Switch Scenarios Dynamically using Slicers]]
