---
type: concept
title: Cash from operations
aliases: ["Cash Flow from Operations", "CFO", "Operating Cash Flow", "OCF"]
tags: ["accounting", "cash-flow", "working-capital", "operations"]
difficulty: beginner
prerequisites: ["[[Net income]]", "[[Working capital]]", "[[Depreciation and amortization]]", "[[The cash flow statement]]"]
related: ["[[Cash from investing]]", "[[Cash from financing]]", "[[Free cash flow]]", "[[EBITDA]]"]
sources: ["[[Wall Street Prep - Cash Flow from Operations (CFO) - Format + Examples]]", "[[Kruze Consulting - Cash Flow Statement]]", "[[Financial Modeling NYC - How to Forecast a Cash Flow Statement- Guide for Financial Planning]]", "[[CFI - Cash Flow from Operations - Definition, Formula and Example]]"]
status: draft
updated: 2026-04-10
---

# Cash from operations

> **TL;DR.** Cash from operations represents the total amount of cash a company generates from its core, day-to-day business activities.

## When you'd use this

You'd look at cash from operations to understand how well a company's core business is generating cash. Since net income includes non-cash items (like depreciation) and doesn't account for cash tied up in things like inventory or delayed customer payments (working capital), cash from operations strips away these accounting nuances to show the actual cash entering and leaving the business. It is a critical measure for determining if a company can sustain its operations, pay its bills, and invest in growth without needing external financing.

## The 30-second version

Cash from operations (or operating cash flow) is the first section of the cash flow statement. It starts with net income from the income statement, which is based on accrual accounting. Because net income includes non-cash expenses and doesn't capture changes in working capital, cash from operations adjusts for these items. It adds back non-cash expenses like depreciation and amortization, and then accounts for the cash impact of changes in working capital assets (like accounts receivable and inventory) and liabilities (like accounts payable). The resulting number tells you exactly how much cash the core business produced or consumed during the period.

## The full explanation

Cash from operations bridges the gap between accrual-based net income and actual cash movements. Under accrual accounting, revenue is recognized when it is earned (even if cash hasn't been received yet) and expenses are matched with their corresponding benefits (even if cash hasn't been paid yet). This makes net income a good measure of profitability but a poor measure of cash generation.

To calculate cash from operations using the indirect method—which is the most common approach—you start with net income and make two main types of adjustments:

### 1. Adding Back Non-Cash Expenses
Certain expenses reduce net income on the income statement but don't actually involve a cash outflow in the current period. The most common example is Depreciation and Amortization (D&A). When a company buys a piece of equipment, the cash goes out the door immediately (which is recorded in Cash from Investing as Capital Expenditures). However, the expense is spread out over the equipment's useful life via depreciation. Since depreciation reduces net income but isn't a cash payment, it must be added back.

### 2. Adjusting for Changes in Working Capital
Working capital accounts for short-term assets and liabilities. Changes in these accounts represent cash being tied up or released:

*   **Accounts Receivable (A/R):** If A/R increases, it means the company sold products on credit and hasn't collected the cash yet. This is an increase in an asset, which is a *use* of cash (decrease in cash flow). When A/R decreases, customers are paying their bills, which is a *source* of cash.
*   **Inventory:** An increase in inventory means the company spent cash to buy more goods. This is a *use* of cash. A decrease means they sold off existing inventory.
*   **Accounts Payable (A/P):** If A/P increases, the company is delaying payment to suppliers. This means the cash is still in the company's bank account, so it's a *source* of cash (increase in cash flow). When A/P decreases, the company is paying its bills, which is an outflow.

In general, an increase in a current asset is a use of cash, while an increase in a current liability is a source of cash.

## Formula

The indirect method for calculating cash from operations is:

$\text{Cash Flow from Operations} = \text{Net Income} + \text{Non-Cash Expenses (e.g., D\&A)} \pm \text{Changes in Working Capital}$

## Worked example

(none)

## Excel and modeling notes

When forecasting a cash flow statement in Excel, cash from operations is almost always built using the indirect method. You will typically link the starting "Net Income" line directly from the bottom of the forecasted income statement. D&A is linked from your supporting depreciation schedules.

The changes in working capital items (Accounts Receivable, Inventory, Accounts Payable, etc.) are usually forecasted in a separate Working Capital Schedule. A common error in modeling is getting the signs wrong for working capital changes: remember that an *increase* in an asset (like A/R) is a cash *outflow* (negative sign on the cash flow statement), while an *increase* in a liability (like A/P) is a cash *inflow* (positive sign).

## Interview-ready answer

Cash from operations is the cash a company generates from its core business activities. It starts with net income and adjusts for non-cash items like depreciation and amortization, as well as changes in working capital, to show the actual cash impact of operations. It's a cleaner measure of a company's ability to generate cash than net income, which is subject to accrual accounting rules.

## Pitfalls and gotchas

- **Confusing CFO with Free Cash Flow (FCF):** Cash from operations does not account for Capital Expenditures (CapEx), which are necessary investments to maintain or grow the business. FCF is a more comprehensive measure of cash available to investors because it subtracts CapEx from CFO.
- **Sign errors in modeling:** It's easy to accidentally flip the signs when projecting changes in working capital. Always double-check that asset increases represent cash outflows and liability increases represent cash inflows.
- **Assuming positive CFO means the company is healthy:** A company can have positive operating cash flow by delaying payments to suppliers (increasing A/P) or aggressively collecting receivables, which might not be sustainable long-term.

## Sources

- [[Wall Street Prep - Cash Flow from Operations (CFO) - Format + Examples]]
- [[Kruze Consulting - Cash Flow Statement]]
- [[Financial Modeling NYC - How to Forecast a Cash Flow Statement- Guide for Financial Planning]]
- [[CFI - Cash Flow from Operations - Definition, Formula and Example]]
