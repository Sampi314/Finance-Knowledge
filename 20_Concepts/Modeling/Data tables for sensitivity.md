---
type: concept
title: "Data tables for sensitivity"
aliases: ["Sensitivity Analysis Excel", "What-If Analysis", "Data Table"]
tags: ["financial-modeling", "excel", "sensitivity-analysis"]
difficulty: intermediate
prerequisites: ["[[Three-statement model]]", "[[Scenario manager]]"]
related: []
sources: ["[[BIWS - Sensitivity Analysis Excel- Tutorial, Video, and Template]]", "[[CFI - What is Sensitivity Analysis]]", "[[CFI - Sensitivity Analysis Table Template - Download]]"]
status: draft
updated: 2026-04-13
---

# Data tables for sensitivity

> **TL;DR.** Data tables in Excel are tools used in financial modeling to vary assumptions and analyze how different values of independent variables affect a specific dependent variable (like valuation).

## When you'd use this

Data tables are primarily used when building financial models to perform sensitivity analysis. They allow analysts to run "What-If" scenarios to predict the outcome of a specific action, such as assessing how a company's implied value changes when varying the discount rate and terminal growth rate.

## The 30-second version

Sensitivity analysis lets you vary the assumptions in a model and observe the output under a range of different scenarios, since investing is probabilistic and the future cannot be predicted perfectly. Internally in Excel, sensitivity analyses are known as "data tables." They calculate multiple outcomes by replacing one or two variables in a formula with different values. This is essential for determining boundaries and helping decision-makers understand how responsive the output is to changes in certain variables.

## The full explanation

A Financial Sensitivity Analysis, also known as a What-If analysis, is commonly used to predict the outcome of an action under defined boundaries determined by independent variables. In Excel, this analysis is performed using the "What-If Analysis" feature, which contains Goal Seek and Data Table.

The direct method involves substituting different numbers into an assumption, while the indirect method inserts a percent change into formulas instead of directly changing the value of an assumption. The results can be displayed in one-way or two-way data tables or visualized via Tornado Charts.

To set up a data table, several key requirements must be met:
- The input variables and output must be on the same spreadsheet as the table.
- The numbers in the input row and column cannot be linked to or from anything that's in the model.
- The row and column inputs and the output must be related in some way.
- A direct link to the output variable must be entered in the top-left corner of the table.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When building data tables in Excel:
- The input variables and output must reside on the same spreadsheet.
- Do not link the numbers in the input row and column to anything in the model; they must be hard-coded.
- Set "Workbook Calculation" in Excel Options to "Automatic except for data tables" to prevent the spreadsheet from slowing down, and press F9 to refresh or update the tables.
- You cannot modify individual cells in the table once it has been created; to change inputs or outputs, you must delete and re-enter the entire table.

## Interview-ready answer

Sensitivity analysis focuses on understanding the effect of a set of independent variables on a dependent variable under specific conditions, holding other factors constant. In contrast, scenario analysis involves examining a specific, comprehensive picture of the future by detailing multiple variables that align with a major economic shock or market shift.

## Pitfalls and gotchas

- Modifying individual cells in an existing data table: If you need to change something, you must delete and recreate the entire table.
- Linking input row or column values directly to the model: This prevents the data table from functioning properly. Always hard-code these values.
- Not linking the top-left corner of the table directly to the output variable.
- Forgetting to set calculation options to "Automatic except for data tables," which can severely slow down large models.

## Sources

- [[BIWS - Sensitivity Analysis Excel- Tutorial, Video, and Template]]
- [[CFI - What is Sensitivity Analysis]]
- [[CFI - Sensitivity Analysis Table Template - Download]]
