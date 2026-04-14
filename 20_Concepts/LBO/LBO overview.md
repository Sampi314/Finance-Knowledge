---
type: concept
title: "LBO overview"
aliases: ["Leveraged Buyout"]
tags: ["lbo", "private-equity", "m&a"]
difficulty: intermediate
prerequisites: ["[[Enterprise value]]", "[[Three-statement model]]"]
related: ["[[M&A overview]]"]
sources: ["[[UpLevered - How to Build an LBO Model (2026)- Step-by-Step Middle-Market Guide]]", "[[A Simple Model - How Private Equity Works - A Simple Model]]", "[[A Simple Model - What is Private Equity - A Simple Model]]", "[[A Simple Model - Leveraged Buyout Model - A Simple Model]]"]
status: draft
updated: 2026-04-14
---

# LBO overview

> **TL;DR.** A Leveraged Buyout (LBO) is the acquisition of an operating business using a combination of debt and equity, where the cash flows of the business are used to pay down the debt over time to increase equity returns.

## When you'd use this

You would build an LBO model or structure an LBO transaction when acquiring a company, particularly in private equity. It is used to evaluate the potential returns (IRR and Cash-on-Cash) of an acquisition, determine the maximum purchase price, or assess different capital structures.

## The 30-second version

An LBO is often compared to taking out a mortgage to buy a home. A private equity firm buys a company using some of its own money (equity) and borrowing the rest (debt). The target company's cash flow is then used to pay down the debt over the holding period (usually 3 to 7 years). When the private equity firm eventually sells the company, the combination of growing the company's value and paying down the debt results in a larger share of the proceeds going to the equity investors, magnifying their returns.

## The full explanation

### Core Mechanics

An LBO model is fundamentally a three-statement model adjusted to reflect a transaction. To reflect the transaction, three primary components are added: Sources and Uses, Balance Sheet Adjustments (purchase accounting), and Exit Analysis.

**Debt and Equity Benefits:**
Debt is borrowed money that earns interest and requires principal repayments over an amortization schedule. Equity represents the ownership value remaining after debts are paid. If the asset grows in value, the use of leverage (debt) amplifies the percentage return on the equity invested compared to an unlevered investment.

**Key Steps in LBO Modeling:**
1.  **Entry Valuation:** Determine the purchase price, often based on a multiple of EBITDA.
2.  **Sources & Uses:** Calculate how much capital is needed to buy the business and where it comes from (various debt tranches and sponsor equity).
3.  **Debt Schedule:** Model the different tranches of debt, interest rates, mandatory amortization, and optional prepayments (cash sweeps) funded by the company's operating cash flows.
4.  **Returns (Exit):** Project the exit value, usually using an exit multiple, subtract remaining debt, and calculate the Internal Rate of Return (IRR) and Multiple on Invested Capital (MOIC or Cash-on-Cash) for the equity investors.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

An LBO model does not have to be overly complicated. Middle-market deals typically range from $25M to $500M in enterprise value. When modeling working capital, translate AR/Inv/AP days into dollar balances and model revolvers dynamically with a facility cap. It is essential to calculate interest on average or beginning-of-period balances to avoid circularity issues. For exit multiples, test ±1.0× to bracket valuation risk.

## Interview-ready answer

A Leveraged Buyout (LBO) is the acquisition of a company using a significant amount of borrowed money (bonds or loans) to meet the cost of acquisition. The assets of the company being acquired are often used as collateral for the loans, and the company's cash flows are used to service and pay down the debt over time. The purpose of using leverage is to enhance the return on equity for the private equity sponsor.

## Pitfalls and gotchas

- **Over-leveraging:** Taking on too much debt can lead to covenant breaches, liquidity crunches, or a complete loss of sponsor equity if cash flows drop.
- **Circularity:** Calculating interest based on end-of-period debt balances can create circular references in Excel; use beginning or average balances.
- **Unrealistic Exit Assumptions:** Assuming multiple expansion without a clear value-creation thesis.

## Sources

- [[UpLevered - How to Build an LBO Model (2026)- Step-by-Step Middle-Market Guide]]
- [[A Simple Model - How Private Equity Works - A Simple Model]]
- [[A Simple Model - What is Private Equity - A Simple Model]]
- [[A Simple Model - Leveraged Buyout Model - A Simple Model]]