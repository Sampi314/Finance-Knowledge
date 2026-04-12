---
type: concept
title: "Depreciation schedule"
aliases: []
tags: ["modeling", "accounting", "assets"]
difficulty: intermediate
prerequisites: ["[[Capex schedule]]", "[[Cost build]]"]
related: ["[[Three-statement model]]"]
sources: ["[[Financial Modeling NYC - How to Build a Depreciation Schedule to Calculate Depreciation Expense]]", "[[CFI - Half-Year Convention for Depreciation - Definition]]"]
status: draft
updated: 2026-04-12
---

# Depreciation schedule

> **TL;DR.** A depreciation schedule tracks the historical cost, accumulated depreciation, and annual depreciation expense of fixed assets over their useful lives.

## When you'd use this

You build a depreciation schedule when modeling a company's fixed assets (PP&E). It is necessary to accurately project the depreciation expense on the income statement, track the carrying value of assets on the balance sheet, and understand the tax implications of different depreciation methods.

## The 30-second version

A depreciation schedule details the loss in value of an individual asset or a company's total fixed assets over their useful life. It tracks the original cost, salvage value, annual depreciation expense, and accumulated depreciation. By forecasting these metrics, analysts can link the expense back to the income statement (reducing taxable income) and add it back to the cash flow statement (since it's a non-cash expense), ultimately updating the ending PP&E balance on the balance sheet.

## The full explanation

Depreciation allocates the cost of a tangible asset over its useful life, reflecting wear and tear or obsolescence. In financial modeling, a depreciation schedule is vital for connecting the three statements.

**Methods of Depreciation**
There are several ways to calculate depreciation, the most common being the straight-line method, which spreads the cost evenly over the asset's useful life. Accelerated methods, such as Double-Declining Balance (DDB) or Modified Accelerated Cost Recovery System (MACRS), front-load the expense, reducing taxable income in the early years. The choice of method affects net income, taxes, and cash flow.

**Half-Year Convention**
The half-year convention is a tax rule assuming an asset is placed in service (or disposed of) exactly halfway through the year, regardless of the actual date. This means only half of the annual depreciation is recognized in the first year, and the remaining half is tacked onto an additional year at the end of the schedule.

**Connecting to the Statements**
The schedule links to the income statement via depreciation expense (often part of COGS or SG&A). Because it's a non-cash expense, it is added back to net income on the cash flow statement. Finally, the accumulated depreciation reduces the gross PP&E on the balance sheet to arrive at the net book value.

## Formula

Straight-line depreciation formula:
$\text{Annual Depreciation Expense} = \frac{\text{Cost} - \text{Salvage Value}}{\text{Useful Life}}$

## Worked example

Suppose a company purchases a machine for $25,000 with a 5-year useful life and $0 salvage value, using straight-line depreciation and the half-year convention.

1. **Annual Straight-Line Depreciation:** $25,000 / 5 = $5,000 per year.
2. **Year 1 (Half-Year):** $5,000 / 2 = $2,500.
3. **Years 2-5:** $5,000 each year.
4. **Year 6 (Remaining Half-Year):** $2,500.

The schedule extends to a 6th year to fully depreciate the asset due to the half-year convention in Year 1.

## Excel and modeling notes

When building the schedule in Excel, create a "waterfall" structure if tracking multiple asset classes or vintages. Ensure the first line item clearly states the assumption used (e.g., straight-line). Use the `OFFSET` or `INDEX/MATCH` functions to dynamically track depreciation based on the useful life of new CapEx additions.

## Interview-ready answer

A depreciation schedule tracks the depreciation expense and accumulated depreciation of fixed assets over time. You start with the beginning PP&E balance, add new CapEx, and subtract the period's depreciation expense to find the ending PP&E balance. This expense reduces net income on the income statement, is added back on the cash flow statement as a non-cash charge, and decreases the asset's carrying value on the balance sheet.

## Pitfalls and gotchas

- Forgetting to add back depreciation on the cash flow statement, causing the balance sheet to go out of balance.
- Confusing tax depreciation (often accelerated like MACRS) with book depreciation (often straight-line), which creates deferred tax liabilities (DTLs).
- Ignoring the half-year convention when tax regulations mandate it, leading to overstated first-year depreciation.

## Sources

- [[Financial Modeling NYC - How to Build a Depreciation Schedule to Calculate Depreciation Expense]]
- [[CFI - Half-Year Convention for Depreciation - Definition]]
