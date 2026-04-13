---
type: concept
title: "Working capital schedule"
aliases: ["NWC schedule", "Net working capital schedule"]
tags: ["modeling", "working-capital", "liquidity", "forecasting"]
difficulty: intermediate
prerequisites: ["[[The balance sheet]]", "[[The income statement]]", "[[Cash from operations]]"]
related: ["[[Three-statement model]]", "[[Linking the three statements]]"]
sources: ["[[Financial Modeling NYC - How to Project Working Capital- Learn to Calculate Working Capital]]", "[[Macabacus - Working Capital Forecasting & Ratio Analysis]]", "[[IB Interview Questions - 3-Statement Financial Model- How to Build One]]"]
status: draft
updated: 2026-04-13
---

# Working capital schedule

> **TL;DR.** A working capital schedule forecasts a company's short-term non-cash assets and non-debt liabilities to track liquidity and link the income statement to the balance sheet and cash flow statement.

## When you'd use this

You build a working capital schedule whenever constructing a three-statement model, performing a Discounted Cash Flow (DCF) valuation, or evaluating an LBO. It is critical for determining how much cash a company generates or consumes through its day-to-day operations and changes in net working capital (NWC).

## The 30-second version

The working capital schedule is a supporting schedule that projects the components of net working capital: current assets (like accounts receivable and inventory, excluding cash) and current liabilities (like accounts payable and accrued expenses, excluding short-term debt). These line items are typically forecasted as a percentage of sales or COGS, or driven by days outstanding metrics (DSO, DIO, DPO). The schedule aggregates these projections to determine the net change in working capital, which directly impacts the cash flow statement.

## The full explanation

A well-built working capital schedule acts as the bridge connecting operating assumptions to the balance sheet and cash flow statement.

First, it separates operating current assets from operating current liabilities. Operating assets usually include Accounts Receivable (A/R), Inventory, and Prepaid Expenses. Operating liabilities generally include Accounts Payable (A/P) and Accrued Expenses. Non-operating items like cash, cash equivalents, and short-term borrowings are deliberately excluded because working capital is intended to measure the efficiency of daily operational performance rather than financing.

After forecasting the individual line items based on historical trends and operating drivers, the schedule calculates the change in each item period-over-period. This change is then linked to the Cash Flow from Operations. An increase in a current asset (like growing inventory) represents a use of cash, while an increase in a current liability (like stretching accounts payable) represents a source of cash.

## Formula

![[Cash Conversion Cycle]]

## Worked example

(none)

## Excel and modeling notes

It is standard practice to express accounts receivable as a percentage of sales, inventory as a percentage of COGS, and accounts payable as a percentage of COGS. Alternatively, you can forecast these items using days outstanding ratios. When modeling, you may hold these ratios flat over the projection period for simplicity, or adjust them to reflect anticipated changes like supply chain improvements, seasonality, or operational synergies in M&A deals.

## Interview-ready answer

A working capital schedule forecasts non-cash current assets and non-debt current liabilities to determine a company's net working capital. The period-over-period changes in these working capital items are crucial because they represent cash inflows or outflows that must be accounted for in the cash flow from operations, ultimately impacting the company's free cash flow.

## Pitfalls and gotchas

- Including cash or short-term debt in the working capital calculation, which improperly mixes financing and operating activities.
- Misaligning the drivers; for example, forecasting inventory based on sales rather than Cost of Goods Sold (COGS).
- Forgetting to invert the signs when linking changes in working capital to the cash flow statement (assets increasing means cash decreasing).

## Sources

- [[Financial Modeling NYC - How to Project Working Capital- Learn to Calculate Working Capital]]
- [[Macabacus - Working Capital Forecasting & Ratio Analysis]]
- [[IB Interview Questions - 3-Statement Financial Model- How to Build One]]
