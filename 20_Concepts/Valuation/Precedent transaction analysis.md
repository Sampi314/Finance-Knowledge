---
type: concept
title: Precedent transaction analysis
aliases: ["Precedent transactions", "M&A comps", "Deal comps"]
tags: ["valuation", "m-and-a", "relative-valuation"]
difficulty: intermediate
prerequisites: ["[[Enterprise value]]", "[[EV/EBITDA]]"]
related: ["[[Comparable company analysis]]"]
sources: ["[[IB Interview Questions - Precedent Transactions Analysis: Step-by-Step Guide]]", "[[Financial Modeling NYC - How to Perform Precedent Transactions Analysis]]"]
status: draft
updated: 2026-04-12
---

# Precedent transaction analysis

> **TL;DR.** Precedent transaction analysis is a relative valuation methodology that determines a company's worth by analyzing the purchase multiples paid in prior M&A transactions involving comparable companies.

## When you'd use this

Precedent transaction analysis is used primarily in sell-side M&A advisory and fairness opinions to understand what buyers might be willing to pay for a company. It is also used when comparing market valuation methodologies, particularly to assess the control premium and potential synergies that acquirers might price into an entire buyout as opposed to a minority stake.

## The 30-second version

Precedent transactions look at past M&A deals to see how much was paid for similar companies. Unlike comparable company analysis (trading comps) which looks at public share prices, precedent transactions factor in the "control premium" — the extra amount a buyer pays to gain a controlling stake in a company — as well as expected synergies. The typical process involves identifying 8-15 recent and highly comparable M&A deals, calculating multiples (like EV/EBITDA or EV/Revenue) for those deals, and then applying a median multiple range to the target company's metrics to find its implied enterprise value.

## The full explanation

Precedent transactions are one of the core valuation methodologies in investment banking, alongside Comparable Company Analysis and Discounted Cash Flow (DCF). The premise is that you can value a business by evaluating what acquirers have recently paid to purchase similar businesses.

While trading comps tell you what a minority (liquid) stake in a business is currently worth, precedent transactions reflect the price required to acquire the entire business outright.

### Key Characteristics

- **Control Premium:** Buyers typically pay a 25-40% premium over the target's standalone public market price to gain majority control and the right to dictate strategy.
- **Synergies Reflective:** Strategic acquirers often expect cost savings or revenue boosts (synergies) post-acquisition. They are willing to pay a higher multiple because they bake these synergies into their valuation.
- **Deal-specific factors:** Multiples can vary greatly due to the competitive dynamics of an auction, the strategic importance of the target, and whether the buyer is a financial sponsor or a strategic player.
- **Time Sensitivity:** Historical transactions can become stale if macroeconomic conditions or the industry landscape shifts. Generally, deals from the past 2-3 years are the most relevant.

### The Steps in Precedent Transaction Analysis

1. **Identify Comparable Transactions:** Selecting the right precedent deals is critical. Analysts filter by industry, size (usually 0.5x to 3x the target's size), transaction type (strategic vs. sponsor), and timing (past 3-5 years). 8-15 strong comparables is the ideal target range.
2. **Gather Transaction Data:** You calculate the fully diluted Enterprise Value representing the purchase price and dig into the target company's LTM (Last Twelve Months) financials at the time the deal was announced.
3. **Calculate Transaction Multiples:** Determine the multiples paid. The most common is EV/EBITDA. For high-growth or pre-profit companies, EV/Revenue might be used instead.
4. **Analyze and Apply Results:** Find the mean, median, and range of these multiples. The median is usually the focal point as it is robust to outliers. The selected multiple range is then multiplied by the subject company's metrics to derive an implied Enterprise Value.

## Formula

The main multiples calculated for each transaction are:

- $\text{EV/EBITDA} = \frac{\text{Enterprise Value}}{\text{LTM EBITDA}}$
- $\text{EV/Revenue} = \frac{\text{Enterprise Value}}{\text{LTM Revenue}}$

To calculate the control premium for a publicly traded company that was acquired:

![[Control premium formula]]

## Worked example

(none)

## Excel and modeling notes

When building out a precedent transaction comp sheet in Excel, standardizing the data is crucial. Data is typically sourced from tools like Capital IQ, FactSet, or directly from SEC filings (such as proxy statements or 8-Ks). Ensure that the Enterprise Value calculation accurately includes the fully diluted equity purchase price (using the treasury stock method for options), plus assumed debt, minus acquired cash. Exclude or specifically note any contingent consideration like earnouts if their realization is highly uncertain.

## Interview-ready answer

**Interviewer:** "Walk me through how to perform a Precedent Transactions analysis."

**You:** "Sure. First, you identify comparable M&A transactions based on criteria like industry, financial size, geography, and date—typically looking for deals within the last 2-3 years. Second, you gather the financial data for the acquired companies, particularly their LTM EBITDA and Revenue at the time of the deal announcement, as well as the purchase price. Third, you calculate the Enterprise Value for each transaction and the corresponding valuation multiples, usually EV/EBITDA. Finally, you calculate the median and range of these multiples across the precedent deals and apply them to your target company's metrics to find an implied Enterprise Value range."

## Pitfalls and gotchas

- **Including non-comparable deals:** A larger data set isn't better if half the deals are bad fits. Only use highly relevant deals.
- **Ignoring market conditions:** Multiples paid during a market peak or a zero-interest-rate environment aren't directly applicable during a market trough or high-interest-rate environment.
- **Confusing Enterprise and Equity Value:** Ensure apples-to-apples comparisons. EV goes with EBITDA/Revenue. Equity Value goes with Net Income.
- **Relying on a single transaction:** Never anchor to just one deal. Always use a blended range (like a median) since each deal has its own unique synergies and competitive bidding dynamics.

## Sources

- [[IB Interview Questions - Precedent Transactions Analysis: Step-by-Step Guide]]
- [[Financial Modeling NYC - How to Perform Precedent Transactions Analysis]]
