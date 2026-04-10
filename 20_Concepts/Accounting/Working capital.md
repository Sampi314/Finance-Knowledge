---
type: concept
title: Working capital
aliases: ["Net Working Capital", "NWC"]
tags: ["accounting", "financial modeling", "ma"]
difficulty: intermediate
prerequisites: ["[[The balance sheet]]", "[[Current assets]]", "[[Current liabilities]]"]
related: ["[[Accounts Receivable Turnover]]", "[[Accounts Payable Turnover]]", "[[Inventory Turnover]]"]
sources: ["[[Quantus Finance - Working Capital Metrics Cheat Sheet (DSO, DPO, DIO) + 3‑Statement Forecasts]]", "[[IB Interview Questions - Net Working Capital Adjustments in M&A Deals Explained]]"]
status: draft
updated: 2026-04-10
---

# Working capital

> **TL;DR.** Working capital is a measure of a company's operational liquidity, calculated as current assets minus current liabilities.

## When you'd use this

You will use working capital when analyzing a company's short-term financial health, projecting cash flows in a 3-statement model, or determining the purchase price adjustment in an M&A transaction. Changes in working capital represent cash inflows or outflows related to the normal operating cycle of a business.

## The 30-second version

Working capital, or Net Working Capital (NWC), represents the capital required to run the day-to-day operations of a business. It measures the difference between what a company owns in the short term (current assets like inventory and accounts receivable) and what it owes in the short term (current liabilities like accounts payable). Positive working capital means the company can cover its short-term obligations, while negative working capital could signal liquidity issues.

## The full explanation

### Standard Accounting Definition
In standard accounting, working capital is simply the difference between total current assets and total current liabilities. Current assets include cash, accounts receivable, inventory, and prepaid expenses. Current liabilities include accounts payable, accrued expenses, short-term debt, and deferred revenue. The standard calculation gives an overview of a company's ability to pay off its current obligations with its most liquid assets over the short term. However, the exact items included in this definition might not fully reflect the operational realities or sustainable levels needed for future growth, leading to adjustments in specific scenarios like mergers and acquisitions.

### M&A Transaction Definition
In M&A transactions, the definition of Net Working Capital (NWC) is typically modified. Cash and debt are usually excluded because they are handled separately in the purchase price bridge. Other non-operating items or transaction-related accruals are also excluded. M&A NWC primarily includes trade accounts receivable, inventory, operating prepaid expenses, trade accounts payable, operating accrued expenses, and operating deferred revenue.

### Net Working Capital Adjustments in M&A
When a business is acquired, the buyer expects a "normal" level of working capital to operate without needing an immediate cash injection. To ensure this, purchase agreements include an NWC adjustment mechanism. A target NWC (or "peg") is established, usually based on a trailing twelve-month (TTM) average to account for seasonality. If the actual NWC delivered at closing exceeds the target, the buyer pays the seller the difference. If it falls short, the seller reimburses the buyer.

## Formula

$\text{Working Capital} = \text{Current Assets} - \text{Current Liabilities}$

$\text{M\&A Working Capital} = \text{Operating Current Assets} - \text{Operating Current Liabilities}$

## Worked example

Consider a company with the following items at closing:
- Trade Accounts Receivable: $20 million
- Inventory: $15 million
- Operating Prepaid Expenses: $5 million
- Trade Accounts Payable: $12 million
- Operating Accrued Expenses: $8 million

Actual M&A NWC = ($20M + $15M + $5M) - ($12M + $8M) = $40M - $20M = $20 million.

If the agreed NWC Target (Peg) was $18 million, the actual NWC exceeds the target by $2 million. Therefore, the buyer would pay the seller an additional $2 million as a purchase price adjustment.

## Excel and modeling notes

When modeling changes in working capital in the Cash Flow Statement (CFO):
- An increase in a current asset (e.g., Accounts Receivable or Inventory) is a use of cash (subtract it).
- An increase in a current liability (e.g., Accounts Payable) is a source of cash (add it).
In a merger model, the expected NWC adjustment directly impacts the sources and uses of funds and the final equity purchase price.

## Interview-ready answer

"Net working capital is current assets minus current liabilities, but in an M&A context, it typically excludes cash and debt. It represents the operating liquidity of a business. In M&A deals, a working capital adjustment ensures the buyer receives the business with a normal, target level of working capital to sustain operations; if actual NWC exceeds the target, the buyer pays more, and if it's below the target, the purchase price is reduced."

## Pitfalls and gotchas

- Failing to recognize the difference between the standard accounting definition of working capital and the typical M&A definition (which usually excludes cash and debt).
- Forgetting that an increase in current assets is a *use* of cash, while an increase in current liabilities is a *source* of cash on the cash flow statement.
- Overlooking seasonality when setting an NWC target in M&A deals; a point-in-time target might lead to a distorted value transfer if the business is highly seasonal.

## Sources

- [[Quantus Finance - Working Capital Metrics Cheat Sheet (DSO, DPO, DIO) + 3‑Statement Forecasts]]
- [[IB Interview Questions - Net Working Capital Adjustments in M&A Deals Explained]]
