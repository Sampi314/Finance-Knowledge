---
type: concept
title: "LBO overview"
aliases: ["Leveraged Buyout", "LBO"]
tags: ["lbo", "private-equity", "modeling"]
difficulty: intermediate
prerequisites: ["[[M&A overview]]", "[[Enterprise value]]"]
related: []
sources: ["[[UpLevered - How to Build an LBO Model (2026)- Step-by-Step Middle-Market Guide]]", "[[A Simple Model - Leveraged Buyout Model (LBO) - A Simple Model]]", "[[A Simple Model - Simple Leveraged Buyout Model (LBO) - A Simple Model]]"]
status: draft
updated: 2026-04-14
---

# LBO overview

> **TL;DR.** A leveraged buyout (LBO) is the acquisition of a business using a significant amount of borrowed money (debt) to meet the cost of acquisition, with the acquired company's assets often used as collateral.

## When you'd use this

You would use an LBO model to evaluate the returns of acquiring a company using a combination of debt and equity. It is primarily used by private equity firms to assess potential investments, structure deals, and determine the maximum purchase price they can offer while still achieving their target returns.

## The 30-second version

An LBO model is a three-statement model adjusted to reflect a transaction where a company is acquired using mostly debt. The process starts with determining the entry valuation and purchase price. Then, a "Sources and Uses" table is built to show where the money comes from (debt and sponsor equity) and where it goes (purchase price, fees). A debt schedule tracks debt paydown using the company's free cash flows over the holding period (typically 5-7 years). Finally, returns are calculated based on the exit valuation and the remaining equity value.

## The full explanation

Building an LBO model typically involves five core steps:

1. **Calculate Entry Valuation:** The enterprise value is calculated using the target's LTM EBITDA multiplied by an entry multiple. The equity purchase price is determined by subtracting net debt (total debt minus cash) from the enterprise value.
2. **Create Sources and Uses Table:** The "Uses" side captures the purchase price, transaction fees, and financing costs. The "Sources" side shows the funding structure, which includes senior debt, subordinated debt, and sponsor equity. The sponsor equity is typically the plug that balances the sources and uses.
3. **Build Financial Projections and Debt Schedule:** A forecast of the income statement and cash flows is created for the holding period. The debt schedule tracks mandatory amortization, cash sweeps (using excess cash to pay down debt), and interest expenses.
4. **Model Exit Scenarios and Returns:** The exit enterprise value is calculated using a projected exit EBITDA and exit multiple. The exit equity value is the exit enterprise value less the remaining debt balance. Key return metrics like Internal Rate of Return (IRR) and Multiple on Invested Capital (MOIC) are calculated.
5. **Conduct Sensitivity Analysis:** Key variables like entry/exit multiples, EBITDA growth, and leverage levels are stressed to see their impact on IRR and MOIC.

## Formula

The core equation for the equity purchase price is:
`Equity Purchase Price = Enterprise Value - Net Debt (Total Debt - Cash)`

## Worked example

(none)

## Excel and modeling notes

When building an LBO model, keep your key assumptions table at the top for easy scenario testing. Avoid circular references between cash balances and interest calculations by using beginning-of-period cash or handling iterations carefully. Ensure financing fees are properly amortized over the life of the loan.

## Interview-ready answer

A leveraged buyout is when a financial sponsor acquires a company using a mix of debt and equity. The LBO model projects the company's cash flows to pay down the debt over time, which increases the equity value. The primary goal is to determine the expected IRR and MOIC upon exiting the investment, typically in 5 to 7 years.

## Pitfalls and gotchas

- Neglecting to include financing fee amortization in the debt schedule, which understates interest expense.
- Using incorrect interest rates for different debt tranches (e.g., senior vs. subordinated debt).
- Ignoring cash sweep mechanics, leading to overly optimistic leverage profiles.
- Making aggressive revenue growth assumptions without proper justification.
- Ignoring working capital impacts on free cash flow, causing cash flow timing mismatches.

## Sources

- [[UpLevered - How to Build an LBO Model (2026)- Step-by-Step Middle-Market Guide]]
- [[A Simple Model - Leveraged Buyout Model (LBO) - A Simple Model]]
- [[A Simple Model - Simple Leveraged Buyout Model (LBO) - A Simple Model]]