---
type: concept
title: "The cash flow statement"
aliases: ["Cash Flow Statement", "CFS"]
tags: ["Accounting", "Financial Statements", "Corporate Finance"]
difficulty: beginner
prerequisites: ["[[The income statement]]", "[[The balance sheet]]"]
related: ["[[Working capital]]", "[[Free cash flow]]"]
sources: ["[[Escalon Services - Cash Flow Statement- Essential Tips for Accurate Financial Analysis]]", "[[Wall Street Prep - Cash Flow Statement (CFS) - Formula + Calculator]]", "[[Financial Modeling NYC - Cash Flow Statement - Financial Modeling New York]]", "[[Kruze Consulting - Cash Flow Statement]]", "[[BIWS - The Cash Flow Statement in Financial Model and Interviews]]"]
status: draft
updated: 2026-04-10
---

# The cash flow statement

> **TL;DR.** The cash flow statement tracks how much actual cash enters and leaves a company over a specific period, categorized by operating, investing, and financing activities.

## When you'd use this

You look at a cash flow statement to understand a company's real cash position and liquidity, going beyond the paper profits shown on the income statement. It's essential for financial modeling (where cash flow from operations helps drive a DCF valuation), for assessing if a company can cover its debt obligations or issue dividends, and for estimating startup cash-zero dates or burn rates.

## The 30-second version

The income statement uses accrual accounting to show revenue and expenses when they are incurred, not necessarily when cash changes hands. The cash flow statement fixes this by reconciling net income back to actual cash movements. It tells you exactly where cash came from and where it went, broken down into three sections: Operations (core business cash flow), Investing (buying/selling assets), and Financing (raising/paying off debt or equity).

## The full explanation

A cash flow statement is one of the three core financial statements. Because most companies use accrual accounting, net income doesn't equal cash. If a company recognizes $100 in revenue but the customer hasn't paid yet (accounts receivable), net income goes up, but cash does not. The cash flow statement adjusts for these timing differences.

There are two primary methods to construct it: the direct method and the indirect method.
- **Direct method:** Tracks actual cash receipts and cash payments. While recommended for transparency, it is rarely used by major corporations because it requires separate accounting tracking.
- **Indirect method:** Starts with Net Income from the income statement and adjusts for non-cash items (like depreciation) and changes in working capital (like inventory or receivables). Almost all standard financial models use the indirect method.

The statement is divided into three key sections:

### Cash flow from operating activities
This section shows the cash generated or used by a company's core business operations. Under the indirect method, it begins with Net Income, adds back non-cash expenses (e.g., depreciation and amortization), and accounts for changes in net working capital (e.g., subtracting increases in accounts receivable or adding increases in accounts payable).

### Cash flow from investing activities
This section records the cash used to buy or sell long-term assets. The biggest item here is usually Capital Expenditures (CapEx) — the cash spent on property, plant, and equipment (PP&E). It also includes cash spent on mergers and acquisitions (M&A) or the purchase/sale of financial securities.

### Cash flow from financing activities
This section tracks cash flowing between the company and its investors or creditors. It includes cash inflows from issuing debt or equity, and cash outflows from paying down debt principal, buying back stock, or issuing dividends.

The sum of these three sections equals the **Net Change in Cash** for the period. When you add the Net Change in Cash to the beginning cash balance, you get the ending cash balance, which then flows to the balance sheet.

## Formula

The core arithmetic of the cash flow statement using the indirect method is:

$$ \text{Net Cash Flow} = \text{CFO} + \text{CFI} + \text{CFF} $$

Where:
- $\text{CFO}$ = Cash Flow from Operations (Net Income + Non-Cash Expenses - Changes in Working Capital)
- $\text{CFI}$ = Cash Flow from Investing (Asset Sales - CapEx - Acquisitions)
- $\text{CFF}$ = Cash Flow from Financing (Debt/Equity Issued - Debt Repaid - Dividends/Buybacks)

## Worked example

Imagine a company with the following financials in Year 1:
- Net Income: $18m
- Depreciation & Amortization: $10m
- Increase in Net Working Capital: $20m (This is a use of cash, so -$20m)
- Capital Expenditures (CapEx): $40m
- Mandatory Debt Repayment: $5m
- Beginning Cash Balance: $25m

Let's calculate the cash flow:
1. **Operating Cash Flow:** $18m (Net Income) + $10m (D&A) - $20m (NWC change) = $8m
2. **Investing Cash Flow:** -$40m (CapEx)
3. **Financing Cash Flow:** -$5m (Debt paydown)

**Net Change in Cash:** $8m - $40m - $5m = -$37m.

Since the starting cash was $25m, an ending cash balance of -$12m means the company ran out of cash and would need a revolver draw or external funding to survive.

## Excel and modeling notes

When modeling a cash flow statement in Excel, always link Net Income directly from the bottom of the income statement. The ending cash balance at the bottom of your cash flow statement must link to the Cash line item in the current period's balance sheet. If your balance sheet doesn't balance, the error is almost always found in a missed sign change (e.g., adding an increase in assets instead of subtracting it) within the cash flow statement.

## Interview-ready answer

"The cash flow statement shows the actual cash entering and leaving a company over a specific period. It adjusts net income for non-cash expenses and changes in working capital, then accounts for investing and financing activities to calculate the net change in cash. It's crucial because net income on the income statement doesn't represent real cash due to accrual accounting."

## Pitfalls and gotchas

- **Confusing increases in assets as cash inflows:** An increase in an operating asset (like inventory) is a *use* of cash, so it must be subtracted in the cash flow statement. An increase in a liability (like accounts payable) is a *source* of cash and is added.
- **Mixing up interest and debt principal:** Interest expense appears on the income statement and reduces net income (affecting CFO). Repaying the *principal* of the debt does not hit the income statement; it appears in Cash Flow from Financing (CFF).

## Sources

- [[Escalon Services - Cash Flow Statement- Essential Tips for Accurate Financial Analysis]]
- [[Wall Street Prep - Cash Flow Statement (CFS) - Formula + Calculator]]
- [[Financial Modeling NYC - Cash Flow Statement - Financial Modeling New York]]
- [[Kruze Consulting - Cash Flow Statement]]
- [[BIWS - The Cash Flow Statement in Financial Model and Interviews]]
