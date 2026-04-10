---
type: concept
title: "The balance sheet"
aliases: ["Balance Sheet", "BS"]
tags: [accounting, financial-statements]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[BIWS - The Balance Sheet in Financial Model and Interviews]]", "[[IB Interview Questions - 3-Statement Financial Model- How to Build One]]", "[[IB Interview Questions - How to Link the Three Financial Statements (Explained)]]"]
status: draft
updated: 2026-04-10
---

# The balance sheet

> **TL;DR.** The balance sheet is a financial statement that provides a snapshot of a company's assets, liabilities, and equity at a specific point in time, always adhering to the fundamental equation: Assets = Liabilities + Equity.

## When you'd use this

You use the balance sheet to assess a company's financial position, liquidity, and leverage at a specific moment. It is critical for analyzing whether a company has enough short-term assets to cover its short-term obligations, understanding how the business is funded (debt vs. equity), and serving as a foundational piece in three-statement modeling to forecast future cash flows.

## The 30-second version

The balance sheet is like a financial photograph. It lists what a company owns (assets) and how it paid for those things—either by owing others (liabilities) or through owner capital and retained profits (equity). "Current" items are expected to be used or paid within a year, reflecting day-to-day operations and liquidity. "Long-term" items relate to multi-year investments and financing. Because every resource must have a funding source, total assets must perfectly equal total liabilities plus equity.

## The full explanation

The balance sheet is organized into three main sections: Assets, Liabilities, and Equity.

### Assets
Assets are resources the company owns that provide future economic benefit. They are generally ordered by liquidity (how easily they can be converted to cash).
- **Current Assets:** Items expected to be converted to cash or consumed within one year. Examples include Cash, Accounts Receivable (money owed by customers), and Inventory.
- **Long-Term Assets:** Assets that will provide value for more than a year. The most common is Property, Plant & Equipment (PP&E). Other examples include Intangible Assets and Goodwill.

### Liabilities
Liabilities represent future obligations or cash outflows. Like assets, they are split by their timeline.
- **Current Liabilities:** Obligations due within a year. Examples include Accounts Payable (money owed to suppliers) and Accrued Expenses.
- **Long-Term Liabilities:** Obligations due in more than one year, primarily Long-Term Debt used to finance major assets or operations.

### Equity
Equity (or Shareholders' Equity) represents the owners' claim on the business. It consists of capital directly invested by shareholders (Common Stock, Additional Paid-In Capital) and the accumulated profits the company has kept over time rather than paying out as dividends (Retained Earnings).

### How it links to other statements
In financial modeling, the balance sheet is closely tied to the other statements:
- **Net Income** from the Income Statement flows into Retained Earnings.
- The **Net Change in Cash** from the Cash Flow Statement updates the top-line Cash balance.
- **Capital Expenditures (CapEx)** increase PP&E, while **Depreciation** reduces it.
- **Debt issuance/repayment** updates the Debt balances.

## Formula

The fundamental accounting equation is:
Assets = Liabilities + Equity

## Worked example

(none)

## Excel and modeling notes

When forecasting the balance sheet in a 3-statement model:
- **Current Assets/Liabilities** (excluding cash and debt) are typically projected as a percentage of relevant Income Statement metrics (e.g., Accounts Receivable tied to Revenue via DSO).
- **Long-Term Assets** like PP&E follow a "roll-forward" schedule: Ending PP&E = Beginning PP&E + CapEx - Depreciation.
- **Long-Term Debt** is linked to a separate debt schedule based on issuances and repayments.
- **Equity** is rolled forward: Ending Retained Earnings = Beginning Retained Earnings + Net Income - Dividends.
- A common check is to calculate `Total Assets - (Total Liabilities + Equity)` which must exactly equal zero in every projected period.

## Interview-ready answer

The balance sheet provides a snapshot of a company's financial position at a specific point in time, showing its assets, liabilities, and equity. It relies on the fundamental equation that Assets equal Liabilities plus Equity, meaning every resource a company owns was funded either by borrowing or by owner capital. In a 3-statement model, it serves as the final check—if your model is built correctly with net income flowing to retained earnings and cash flows updating asset and liability balances, the balance sheet must balance perfectly.

## Pitfalls and gotchas

- **Failing to balance:** The most obvious pitfall in modeling or interviews. If a change affects one side of the equation (like an asset increasing), there must be a corresponding change (another asset decreasing, or a liability/equity increasing) to keep it balanced.
- **Confusing cash vs. accrual:** Assuming an increase in Accounts Receivable means more cash. It is actually a use of cash (revenue recognized, but cash not yet collected).
- **Circular references:** In models, interest expense depends on average debt, which depends on cash flow, which depends on interest expense. This creates a circular loop that must be handled carefully.

## Sources

- [[BIWS - The Balance Sheet in Financial Model and Interviews]]
- [[IB Interview Questions - 3-Statement Financial Model- How to Build One]]
- [[IB Interview Questions - How to Link the Three Financial Statements (Explained)]]
