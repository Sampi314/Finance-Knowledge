---
type: concept
title: "Sources and uses table"
aliases: ["Sources and Uses", "Sources and Uses of Funds"]
tags: ["m&a", "lbo", "financial-modeling"]
difficulty: beginner
prerequisites: ["[[M&A overview]]", "[[Purchase price]]"]
related: ["[[Accretion dilution analysis]]"]
sources: ["[[IB Interview Questions - Sources and Uses of Funds in M&A Transactions Explained]]"]
status: draft
updated: 2026-04-14
---

# Sources and uses table

> **TL;DR.** The Sources and Uses of Funds table is a foundational schedule in M&A and LBO transactions that shows exactly where the money to complete a deal comes from and where it goes, ensuring total sources exactly equal total uses.

## When you'd use this

You build a Sources and Uses table at the very beginning of structuring an M&A or Leveraged Buyout (LBO) transaction. It translates the negotiated deal terms into the actual financial structure required to close. This schedule is a prerequisite for more complex modeling, such as calculating sponsor returns in an LBO or analyzing accretion/dilution in a merger model.

## The 30-second version

A Sources and Uses table is a simple but essential accounting schedule that balances two sides of a transaction. The "Uses" side lists every cash outflow required at closing, primarily the purchase price of the target's equity, refinanced debt, and fees. The "Sources" side lists where that capital comes from, such as new debt, rollover equity, and buyer cash. Because every dollar spent must come from somewhere, Total Sources must exactly equal Total Uses. In practice, bankers use one item—typically the sponsor's equity in an LBO—as a "plug" to balance the two sides.

## The full explanation

The Sources and Uses table is a fundamental component of investment banking models, pitch books, and transaction documentation. Its core principle is an accounting identity: `Total Sources = Total Uses`. Any imbalance indicates a modeling error.

### Uses of Funds: Where the Money Goes
The Uses side captures everything that requires funding to complete the transaction:
- **Purchase of Equity:** The largest use is paying the existing shareholders. For a public company, this is the offer price multiplied by fully diluted shares. Note that this is the equity value, not the enterprise value.
- **Refinancing Existing Debt:** Target companies usually have existing debt with "change-of-control" provisions that require the debt to be paid off at closing.
- **Transaction Fees:** M&A deal fees, including investment banking advisory (0.5% to 1.5% of transaction value), legal, and accounting fees. These are typically expensed immediately.
- **Financing Fees:** Fees related to raising new debt, such as arrangement and commitment fees. These are capitalized and amortized over the life of the debt.
- **Other Uses:** Minimum cash required for operations, working capital true-ups, or escrow funding.

### Sources of Funds: Where the Money Comes From
The Sources side captures all committed funding enabling the deal:
- **Senior Secured Debt:** The largest debt component, such as Term Loan B or a Revolving Credit Facility, sized based on leverage multiples (e.g., 4.0x EBITDA).
- **Subordinated Debt:** Second lien term loans, mezzanine debt, or high yield bonds that provide additional leverage.
- **Sponsor Equity:** In an LBO, the private equity firm's investment. This acts as the "plug"; the sponsor maximizes debt capacity and funds the remainder with equity to complete the transaction.
- **Rollover Equity:** Existing shareholders (like management or founders) retaining a portion of their ownership. It appears on both sides (Uses as purchase price owed, Sources as their reinvestment).
- **Cash on Balance Sheet / Stock:** In strategic M&A, the acquirer may use their existing corporate treasury cash or issue stock as consideration.

### Building the Table
1. Determine the equity purchase price and add any debt that needs to be refinanced.
2. Estimate all transaction and financing fees to find **Total Uses**.
3. Determine total available debt based on lender commitments and add other sources like rollover equity.
4. Calculate the **Plug** (typically Sponsor Equity) by subtracting all available sources from Total Uses.
5. Verify that Total Sources perfectly balance against Total Uses.

## Formula

(none)

## Worked example

Consider a private equity firm acquiring a company with **$100 million** EBITDA at an **8.0x EBITDA** enterprise value.

**Transaction Terms:**
- Enterprise Value: **$800 million**
- Existing Net Debt: **$150 million** (to be refinanced)
- Transaction Fees: **$20 million**
- Financing Fees: **$15 million**
- Senior Debt: 4.0x EBITDA = **$400 million**
- Subordinated Debt: 1.5x EBITDA = **$150 million**
- Management Rollover: **$25 million**

**Uses of Funds:**
- Equity Purchase Price: **$650 million** ($800M EV - $150M Net Debt)
- Refinance Existing Debt: **$150 million**
- Transaction Fees: **$20 million**
- Financing Fees: **$15 million**
- **Total Uses: $835 million**

**Sources of Funds:**
- Senior Secured Debt: **$400 million**
- Subordinated Debt: **$150 million**
- Management Rollover: **$25 million**
- Sponsor Equity (Plug): **$260 million** ($835M Uses - $575M other sources)
- **Total Sources: $835 million**

## Excel and modeling notes

- Always create a dedicated "Check" cell that subtracts Total Sources from Total Uses. It should perfectly equal zero. Conditionally format this cell to turn red if the difference is non-zero.
- The Sponsor Equity line item is usually calculated directly as `Total Uses - SUM(Debt Sources) - Rollover`.
- Ensure you differentiate between transaction fees (which flow through retained earnings on the pro forma balance sheet as an expense) and financing fees (which create a deferred financing cost asset).

## Interview-ready answer

"A Sources and Uses table shows where funding for a transaction comes from and where it goes. Uses include the purchase price for equity, refinancing existing debt if required, transaction fees paid to advisors, and financing fees paid to lenders. Sources include the various debt tranches funding the deal, any rollover equity from existing owners, and the equity contribution from the buyer, which is typically the plug that balances the table. Total sources must exactly equal total uses."

## Pitfalls and gotchas

- **Forgetting financing fees:** New debt requires fees that must be funded at closing. Omitting these understates total uses and overstates equity returns.
- **Confusing enterprise value and equity value:** Uses should reflect the equity purchase price, not the enterprise value. Assumed or refinanced net debt is handled separately.
- **Mishandling rollover equity:** Rollover equity must appear in both sources and uses to maintain the balance. Omitting it from one side breaks the table.

## Sources

- [[IB Interview Questions - Sources and Uses of Funds in M&A Transactions Explained]]
