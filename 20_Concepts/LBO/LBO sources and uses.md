---
type: concept
title: "LBO sources and uses"
aliases: ["LBO Sources and Uses of Funds"]
tags: ["lbo", "financial-modeling"]
difficulty: intermediate
prerequisites: ["[[LBO overview]]", "[[Sources and uses table]]"]
related: ["[[Sponsor returns]]", "[[Multiple of money]]"]
sources: ["[[IB Interview Questions - Sources and Uses of Funds in M&A Transactions Explained]]", "[[UpLevered - How to Build an LBO Model (2026)- Step-by-Step Middle-Market Guide]]", "[[Wall Street Prep - Advanced LBO Modeling Test - Training Guide]]", "[[A Simple Model - Simple Leveraged Buyout Model (LBO) - A Simple Model]]"]
status: draft
updated: 2026-04-15
---

# LBO sources and uses

> **TL;DR.** In a leveraged buyout, the sources and uses table is specialized to highlight high debt utilization, transaction/financing fees, and the critical calculation of the sponsor equity "plug" required to balance the deal.

## When you'd use this

You build an LBO-specific Sources and Uses table at the very beginning of an LBO model to determine the exact equity check required from the private equity sponsor. Because sponsor equity is the denominator for return metrics like IRR and Multiple of Money (MoM), this schedule is the foundational driver of all subsequent LBO return analysis.

## The 30-second version

An LBO sources and uses table is an accounting identity where total cash needed (Uses) must equal total capital raised (Sources). In an LBO, Uses typically include purchasing the target's equity, refinancing existing debt, and paying transaction and financing fees. Sources rely heavily on various debt tranches (e.g., senior debt, subordinated debt) and rollover equity. To make the table balance, the sponsor's equity contribution acts as the "plug," filling the gap between total uses and available debt.

## The full explanation

While the fundamental rule that `Sources = Uses` applies to all M&A transactions, an LBO-specific schedule has distinct structural characteristics and focus areas.

### Defining the Uses (Cash Outflows)
- **Purchase Equity Value:** The cash required to buy the target's equity. If the deal is structured "cash-free, debt-free", this is derived by taking the Enterprise Value and subtracting the target's Net Debt.
- **Refinancing Existing Net Debt:** Existing debt on the target's balance sheet usually contains change-of-control provisions and must be paid off at closing.
- **Transaction Fees:** M&A advisory, legal, and accounting diligence fees (typically 2% to 4% of transaction value for middle-market deals). These are expensed immediately.
- **Financing Fees:** Fees paid to lenders for raising new debt (typically 2% to 3% of the debt amount), which cover original issue discount (OID) and arrangement fees. These are capitalized and amortized.
- **Minimum Cash to Balance Sheet:** Cash required to run the day-to-day operations immediately post-close.

### Defining the Sources (Capital Inflows)
- **Senior and Subordinated Debt:** The primary engine of an LBO. Debt is maximized based on cash flow lending parameters (e.g., 4.0x EBITDA for senior, 1.5x for subordinated) to minimize the equity required.
- **Rollover Equity:** Target management or founders often reinvest a portion of their proceeds into the new capital structure.
- **Sponsor Equity (The Plug):** Private equity firms solve for this last. After maximizing debt and accounting for rollover, the remaining capital required to fund Total Uses is the sponsor equity.

### Why It Matters for LBOs
The sponsor equity plug is the literal denominator in the LBO return calculation. Since PE firms aim for high IRRs (e.g., 20%+), they actively structure the Sources and Uses to maximize debt and minimize this equity plug without placing the target company in financial distress.

## Formula

(none)

## Worked example

Consider a middle-market LBO on a cash-free, debt-free basis:
- Target LTM EBITDA: $10M
- Entry Multiple: 10.0x
- Enterprise Value: $100M
- Existing Net Debt: $10M
- Equity Purchase Price: $90M ($100M - $10M)

**Uses:**
- Equity Purchase Price: $90M
- Transaction Fees: $3M
- Financing Fees: $1M
- **Total Uses: $94M**

**Sources:**
- Senior Debt: $55M
- Subordinated Debt: $15M
- **Sponsor Equity (Plug): $24M** (calculated as $94M Uses - $70M Debt)
- **Total Sources: $94M**

## Excel and modeling notes

- Standard modeling practice treats Sponsor Equity as a plug formula: `Total Uses - SUM(Debt Sources) - Rollover Equity`.
- Ensure circular references are managed if financing fees are calculated as a percentage of a debt tranche that itself is dynamically sized.
- Transaction fees decrease Retained Earnings, while Financing fees create a Capitalized Financing Fee asset on the pro forma balance sheet.

## Interview-ready answer

"In an LBO, the sources and uses table outlines the capital raised and the cash required to close the deal. The primary uses are the equity purchase price, refinancing existing debt, and paying transaction and financing fees. The sources maximize debt tranches—like senior and subordinated debt—alongside rollover equity. The sponsor's equity contribution acts as the mathematical plug to balance the two sides, which directly determines the initial investment size used to calculate IRR."

## Pitfalls and gotchas

- **Excluding Financing Fees from Uses:** Missing the 2-3% fees required to raise debt will understate the cash needed at close, thereby artificially lowering the equity plug and falsely inflating the IRR.
- **Mishandling Debt Refinancing:** In a cash-free, debt-free transaction, existing debt reduces the Equity Purchase Price but must still be funded as a distinct Use (Refinancing Existing Debt) if the cash isn't extracted pre-close.
- **Improper Treatment of Rollover Equity:** If management rolls over equity, it must simultaneously reduce the cash Equity Purchase Price (Uses) and appear as a Source, or simply be included as a Source while the Uses reflect the total equity value.

## Sources

- [[IB Interview Questions - Sources and Uses of Funds in M&A Transactions Explained]]
- [[UpLevered - How to Build an LBO Model (2026)- Step-by-Step Middle-Market Guide]]
- [[Wall Street Prep - Advanced LBO Modeling Test - Training Guide]]
- [[A Simple Model - Simple Leveraged Buyout Model (LBO) - A Simple Model]]