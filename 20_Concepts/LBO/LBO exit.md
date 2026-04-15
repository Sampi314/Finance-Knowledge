---
type: concept
title: "LBO exit"
aliases: ["LBO exit strategies"]
tags: ["lbo", "exit-strategies", "private-equity"]
difficulty: intermediate
prerequisites: ["[[LBO overview]]"]
related: ["[[IRR]]", "[[Multiple of money]]", "[[Cash-on-cash return]]"]
sources: ["[[BIWS - LBO Exit Strategies- M&A, IPOs, and Dividends, Recapitalizations]]", "[[A Simple Model - Exit Analysis - LBO Case Study - A Simple Model]]"]
status: stub
updated: 2026-04-15
---

# LBO exit

> **TL;DR.** LBO exits encompass the strategies a private equity firm uses to realize returns on a leveraged buyout, primarily through M&A sales, IPOs, or dividend recapitalizations.

## When you'd use this

You would use this when modeling the end of an investment holding period in a leveraged buyout analysis. It determines how and when the sponsor realizes their investment, which is essential for calculating expected returns like IRR and MOIC.

## The 30-second version

In most leveraged buyouts, the exit is modeled as an M&A sale where the company is sold to another business or private equity firm, assuming a simple exit multiple based on EBITDA. However, other paths exist depending on market conditions and company size. An Initial Public Offering (IPO) is used when the company is too large to be bought or M&A markets are weak, though it takes time to fully divest shares. A dividend recapitalization is sometimes used to extract cash while retaining ownership indefinitely, especially when other exits aren't feasible.

## The full explanation

LBO exit strategies primarily determine how the private equity sponsor will recoup their investment and realize returns. The primary metric focused on through these strategies is the expected return on investment, measured through Internal Rate of Return (IRR) and Multiple on Invested Capital (MOIC).

**M&A Sale**
The preferred strategy in the vast majority of scenarios because it allows the private equity firm to sell 100% of its stake cleanly. In an LBO model, you assume an exit multiple (usually based on EBITDA) to calculate the Enterprise Value, then subtract Net Debt to back into the Equity Value. It generally yields the highest returns with the least uncertainty.

**Initial Public Offering (IPO)**
Used when companies are too large to be bought or operating in unfavorable M&A environments. In an IPO, the sponsor cannot sell its entire stake at once to avoid sending negative market signals. Instead, they sell off holdings over several years. This extended timeframe often results in a lower IRR compared to a clean M&A sale, though the Multiple of Money (MoM) might remain similar depending on share price fluctuations.

**Dividend Recapitalization**
Considered a "non-exit," the firm holds the company indefinitely and issues dividends from excess cash flow, sometimes taking on additional debt to do so. This approach relies heavily on the company generating robust free cash flow and is often used in emerging markets where capital markets are less liquid. Because it takes a long time to recoup the initial investment via dividends, the IRR usually suffers significantly, even if the MoM eventually looks reasonable.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

(none)

## Interview-ready answer

The three primary LBO exit strategies are an M&A sale, an IPO, and a dividend recapitalization. An M&A sale is preferred because it's a clean exit that typically yields the highest IRR. An IPO involves selling shares over time, which usually lowers IRR due to the extended timeline, and a dividend recapitalization is a "non-exit" where the firm continuously extracts cash while retaining ownership.

## Pitfalls and gotchas

- Relying solely on M&A exits in models might not be realistic for very large companies or during weak M&A markets.
- IPOs often result in lower IRRs due to the time required to fully divest shares without spooking the market.
- Dividend recapitalizations require strong, consistent free cash flow and generally yield lower IRRs because of the extended time to recoup the investment.

## Gaps

- Missing exact formula
- Missing worked example
- Missing Excel and modeling notes

## Sources

- [[BIWS - LBO Exit Strategies- M&A, IPOs, and Dividends, Recapitalizations]]
- [[A Simple Model - Exit Analysis - LBO Case Study - A Simple Model]]
