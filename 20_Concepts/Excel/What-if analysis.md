---
type: concept
title: "What-if analysis"
aliases: ["Sensitivity analysis", "Scenario analysis", "Data tables"]
tags: ["excel-and-modeling-craft", "modeling", "data-analysis"]
difficulty: intermediate
prerequisites: ["[[Hardcoded vs formula cells]]"]
related: ["[[Goal seek]]", "[[Solver]]"]
sources: ["[[Trump Excel - Data Analysis - Scenario Manager in Excel]]", "[[BIWS - Sensitivity Analysis Excel- Tutorial, Video, and Template]]"]
status: draft
updated: 2026-04-09
---

# What-if analysis

> **TL;DR.** What-if analysis is the process of changing the values in cells to see how those changes will affect the outcome of formulas on the worksheet.

## When you'd use this

You use what-if analysis when you want to explore different potential outcomes in a financial model based on varying input assumptions. It's essential for sensitivity analysis, scenario planning, and understanding the range of possible valuations or returns under different conditions (e.g., best case, base case, worst case).

## The 30-second version

All investing and forecasting is probabilistic. Since you cannot predict the future exactly, you must assess how a company's valuation or a project's returns change when key drivers like growth rates, discount rates, or costs deviate from expectations. What-if analysis tools in Excel, primarily Data Tables and the Scenario Manager, automate this process. They allow you to systematically vary one or more inputs and observe the impact on your key outputs without manually changing the hardcoded inputs one by one.

## The full explanation

What-if analysis in Excel encompasses several built-in tools, but the two most critical for financial modeling are Data Tables (often called Sensitivity Tables) and the Scenario Manager.

### Data Tables (Sensitivity Tables)
Internally in Excel, sensitivity analyses are known as "data tables," found under the Data tab and "What-If Analysis." Data tables let you vary one or two input variables and observe the effect on one or more output variables in a structured grid.

To set up a data table properly:
1.  **Direct Relationship:** The input variables must directly affect the output variable through the model's logic.
2.  **Same Sheet:** The input variables and the output link must be on the same spreadsheet as the table itself.
3.  **Hardcoded Inputs:** The numbers in the row and column of the table that you want to sensitize must be hardcoded or driven by simple additions/percentages; they cannot be linked to the live model inputs.
4.  **Output Link:** In the top-left corner of the table (for a 2-variable table), you must enter a direct link to the output variable you want to sensitize.
5.  **Execution:** Select the entire table range, go to Data Table, and input the "Row Input Cell" and "Column Input Cell" linked to the actual model drivers.

### Scenario Manager
The Scenario Manager is used when you have more than two variables that change simultaneously, representing a cohesive "scenario" (e.g., Worst Case, Realistic, Best Case). It allows you to save sets of input values and switch between them easily. You can define which cells are the "Changing cells" and assign specific values to them for each named scenario. A powerful feature is the ability to generate a "Scenario Summary" report, which instantly creates a new tab showing a comparative overview of all scenarios and their resulting outputs.

## Formula

Example Profit calculation with 3 variables: `=B2*B3-B4-B5*B2` where B2 is Sale Quantity, B3 is Price per Unit, B4 is Fixed Cost and B5 is Variable Cost per unit.

## Worked example

Suppose you want to calculate profit with the following variables changing based on a scenario (e.g. Worst Case scenario):
Sale Quantity: 50
Price per Unit: 30
Variable Cost per Unit: 30
These variables can be put into the Scenario Manager to see the effect on the final profit result when these dependent variables change.

## Excel and modeling notes

When using Data Tables extensively, your spreadsheet can become very slow to calculate. To mitigate this, go to Excel Options or Preferences and set "Workbook Calculation" to "Automatic except for data tables". You can then manually press F9 to refresh or update the tables when needed.

Always check your data tables to ensure the logic holds. For instance, in a valuation model, if revenue growth increases, the implied value should increase. If the discount rate increases, the implied value should decrease. If the numbers don't change, or change in the wrong direction, there is a linking error.

## Interview-ready answer

What-if analysis is crucial for stress-testing financial models. I use Excel's Data Tables for sensitivity analysis to see how changes in one or two key drivers, like the discount rate or terminal growth rate, impact valuation. For broader situational analysis involving three or more variables, I use the Scenario Manager to build out discrete base, upside, and downside cases.

## Pitfalls and gotchas

- Creating a data table where the row/column inputs are linked directly to the model assumptions rather than being hardcoded values.
- Placing the data table on a different worksheet than the input driver cells, which Excel does not allow.
- Forgetting to change calculation settings to "Automatic except for data tables," resulting in a very sluggish model.
- Modifying individual cells inside a generated Data Table; you must delete and recreate the entire table if changes are needed.

## Sources

- [[BIWS - Sensitivity Analysis Excel- Tutorial, Video, and Template]]
- [[Trump Excel - Data Analysis - Scenario Manager in Excel]]