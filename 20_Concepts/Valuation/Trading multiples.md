---
type: concept
title: Trading multiples
aliases: [Valuation multiples]
tags: [valuation, relative-valuation, multiples]
difficulty: intermediate
prerequisites: ["[[Comparable company analysis]]", "[[Enterprise value]]", "[[Equity value]]"]
related: ["[[Intrinsic vs relative valuation]]"]
sources: ["[[CFI - Relative Valuation - Overview, Types, and Example]]", "[[CFI - EV-EBIT Ratio - Overview, Formula, Interpretation and Example]]", "[[IB Interview Questions - Common Valuation Multiples Explained]]"]
status: draft
updated: 2026-04-12
---

# Trading multiples

> **TL;DR.** Valuation multiples are a common language for comparing companies by normalizing their value on a per-unit basis, such as value relative to earnings or revenue.

## When you'd use this

You use trading multiples to value a company by comparing it to similar, publicly traded companies. This approach is highly relevant for equity research, investment banking pitches (like comparable companies analysis or "comps"), and M&A modeling to determine if a stock is overvalued or undervalued relative to the broader market.

## The 30-second version

Trading multiples, or relative valuation models, value businesses by comparing them to similar companies using standardized financial ratios. If comparable companies in an industry are trading at a multiple of 10x their earnings, a target company should, theoretically, also be worth 10x its earnings. The two most common forms of relative valuation are Comparable Company Analysis (Comps) and Precedent Transactions (Precedents).

## The full explanation

Valuation multiples express a company's overall value relative to a specific financial metric, such as revenue, EBITDA, or net income. By converting absolute dollar values into standardized ratios, multiples allow analysts to compare companies of drastically different sizes on an apples-to-apples basis.

Multiples are categorized fundamentally into two groups depending on the value representation they use:
1. **Enterprise Value (EV) Multiples**: These multiples compare the value of the entire business—equity plus net debt—to operating metrics available to all capital providers. Examples include EV/EBITDA, EV/EBIT, and EV/Revenue. Because these metrics sit above the interest expense (debt) line, these multiples are capital structure-neutral.
2. **Equity Value Multiples**: These multiples compare the market capitalization (only the equity portion) to post-debt metrics like Net Income or Book Value. The most well-known is the Price/Earnings (P/E) ratio. They are directly impacted by the amount of leverage a company has and its tax rate.

A company with a relatively low trading multiple might be considered undervalued compared to its peers or the market at large, though this must be viewed in the context of growth prospects, risk, and capital structure.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

When building Sum of the Parts (SOTP) models, you might assign different multiples to distinct segments of a diversified business. For instance, an e-commerce segment might be valued using a different EV/Revenue or EV/EBITDA multiple than its associated cloud computing division.

## Interview-ready answer

Trading multiples are ratios used to value a company by comparing its value to a financial metric, like EBITDA or Earnings. They are the foundation of relative valuation methods, allowing us to normalize companies of different sizes to see if a specific stock is trading at a premium or discount relative to comparable peers.

## Pitfalls and gotchas

- Mixing value types: An enterprise value metric (which includes debt) must be compared against an unlevered operating metric (like EBITDA or EBIT), while an equity value metric must be compared with a levered metric (like Net Income). Mixing EV with Net Income is mathematically flawed.
- Ignoring context: A low multiple doesn't strictly mean a company is "cheap" or a bargain; the company could possess significantly lower growth prospects, face higher risks, or have systemic operational issues compared to its peers.

## Sources

- [[CFI - Relative Valuation - Overview, Types, and Example]]
- [[CFI - EV-EBIT Ratio - Overview, Formula, Interpretation and Example]]
- [[IB Interview Questions - Common Valuation Multiples Explained]]
