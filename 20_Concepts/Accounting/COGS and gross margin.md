---
type: concept
title: "COGS and gross margin"
aliases: ["Cost of Goods Sold", "Gross Profit Margin", "Gross Profit"]
tags: ["accounting", "income-statement", "profitability"]
difficulty: beginner
prerequisites: ["[[The income statement]]", "[[Revenue recognition]]"]
related: ["[[Operating expenses]]", "[[EBITDA]]", "[[Net income]]"]
sources: ["[[IB Interview Questions - 3-Statement Financial Model- How to Build One]]", "[[Pivotal180 - The three key financial statements, an introduction]]", "[[Financial Modeling NYC - How to Forecast an Income Statement- Analyze and Project Revenue, Expenses, and Other Income Statement Line Items]]"]
status: draft
updated: 2026-04-10
---

# COGS and gross margin

> **TL;DR.** Cost of Goods Sold (COGS) represents the direct costs of producing goods or services, and Gross Margin is the percentage of revenue left after subtracting COGS.

## When you'd use this

You would use COGS and gross margin when evaluating a company's core profitability, projecting future financial performance in a three-statement model, and comparing operational efficiency across companies in the same industry. It's a foundational metric in building an income statement.

## The 30-second version

Cost of Goods Sold (COGS), also known as cost of sales or cost of services, is how much it directly costs a business to produce its products or services. It does not include indirect expenses like sales, general, and administrative (SG&A) costs. Gross profit is calculated by subtracting COGS from total revenue. Gross margin expresses that gross profit as a percentage of revenue. A higher gross margin indicates a company can produce its goods efficiently and has more money left over to cover its operating expenses, pay down debt, and generate net income.

## The full explanation

### Cost of Goods Sold (COGS)

Cost of Goods Sold (COGS) is a line item on the income statement that captures all direct costs attributable to the production of the goods sold or services provided by a company. This typically includes the cost of raw materials and direct labor. It excludes indirect expenses such as marketing, rent, and administrative costs.

Because COGS is directly tied to production, it generally varies with the level of output or sales. Accurately tracking COGS is essential because it is the first major expense deducted from revenue on the income statement, ultimately determining gross profit.

### Gross Profit and Gross Margin

Gross profit is the absolute dollar amount remaining after deducting COGS from revenue.

The **Gross Margin** (often referred to interchangeably with Gross Profit Margin) is the gross profit expressed as a percentage of revenue. This metric is crucial for financial analysts because it indicates how efficiently a company manages its production costs and pricing strategy. If a company has a 40% gross margin, it means that for every dollar of revenue generated, it retains $0.40 to cover operating expenses, interest, taxes, and net profit.

### Forecasting COGS and Gross Margin in Financial Models

In a three-statement financial model, projecting COGS is one of the most critical steps after forecasting revenue. Analysts typically forecast COGS as a percentage of revenue based on historical margins.

For instance, if a company has maintained stable gross margins historically, an analyst might hold that percentage flat in future projections. However, if the company has been steadily improving its gross margins by 50 basis points per year due to economies of scale or operational improvements, the analyst might project continued modest margin expansion.

## Formula

The absolute dollar value of Gross Profit is calculated as:

![[Gross Profit]]

Gross Margin is calculated as:

$$ \text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} $$

## Worked example

(none)

## Excel and modeling notes

When building a three-statement model, COGS is typically projected directly below revenue on the income statement.

1. Calculate historical COGS as a percentage of revenue for the past 3-5 years.
2. Formulate a thesis on whether this margin will improve, decline, or remain flat.
3. Multiply the projected revenue by the assumed COGS percentage to calculate the forecasted COGS line item.

Color-code your model appropriately: use blue font for hard-coded assumptions (like your forecasted COGS percentage) and black font for formulas (like the resulting COGS dollar amount and Gross Profit).

Additionally, working capital schedules heavily rely on COGS. Metrics like Days Inventory Outstanding (DIO) and Days Payable Outstanding (DPO) use COGS in their calculations (e.g., `Inventory = (DIO * COGS) / 365`).

## Interview-ready answer

Cost of Goods Sold (COGS) represents the direct costs to produce a company's goods or services, such as raw materials and direct labor. Gross profit is revenue minus COGS, and gross margin is gross profit expressed as a percentage of revenue. In financial modeling, we typically forecast COGS as a percentage of revenue based on historical trends, and it's a critical driver not only for the income statement but also for working capital metrics like Days Inventory Outstanding.

## Pitfalls and gotchas

- **Confusing COGS with SG&A:** COGS only includes direct costs of production. Indirect operating expenses like marketing, corporate rent, and management salaries belong in SG&A, below the gross profit line.
- **Embedded Depreciation:** Depending on the company and industry, depreciation and amortization (D&A) may be partially embedded in COGS (e.g., depreciation of manufacturing equipment). Analysts must be careful when adjusting EBITDA to understand if D&A needs to be stripped out of COGS.
- **Working capital mismatches:** When projecting inventory and accounts payable, you must use COGS, not revenue, in your days-based metrics (DIO and DPO). Using revenue for these metrics is a common modeling error.

## Sources

- [[IB Interview Questions - 3-Statement Financial Model- How to Build One]]
- [[Pivotal180 - The three key financial statements, an introduction]]
- [[Financial Modeling NYC - How to Forecast an Income Statement- Analyze and Project Revenue, Expenses, and Other Income Statement Line Items]]