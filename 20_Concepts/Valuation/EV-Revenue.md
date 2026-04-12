---
type: concept
title: EV/Revenue
aliases: ["EV/Sales", "Enterprise Value to Revenue", "Enterprise Value-to-Sales"]
tags: ["valuation", "multiples", "relative-valuation"]
difficulty: intermediate
prerequisites: ["[[Enterprise value and equity value]]", "[[Comparable company analysis]]"]
related: ["[[EV/EBITDA]]", "[[Trading multiples]]"]
sources: ["[[IB Interview Questions - Common Valuation Multiples Explained]]", "[[CFI - Enterprise Value-to-Sales (EV-Sales) - Formula, Examples]]"]
status: draft
updated: 2026-04-12
---

# EV/Revenue

> **TL;DR.** EV/Revenue is a financial ratio that compares a company's total value to its total sales revenue, frequently used to value businesses that are not yet profitable.

## When you'd use this

You would typically use the EV/Revenue (or EV/Sales) multiple when valuing early-stage or high-growth companies—such as software, biotech, or internet startups—that have negative or minimal earnings (EBITDA). It is also commonly used in M&A analysis when acquirers are buying a target for strategic reasons (like market share or customer base) rather than just current profitability, where synergies might justify paying a premium.

## The 30-second version

Enterprise Value-to-Sales (EV/Sales) measures how many dollars of enterprise value an investor is paying for every dollar of the company's revenue. A high EV/Revenue multiple usually suggests that a company is considered "expensive" or overvalued, though growth-oriented investors might accept a high ratio if they believe future sales will scale rapidly. Conversely, a lower EV/Revenue multiple relative to peers can indicate that the business is undervalued. Because it sits "above the debt line," it strips out differences in capital structure, making it ideal for apples-to-apples comparisons.

## The full explanation

EV/Revenue is a foundational relative valuation metric that divides Enterprise Value (the total value of a company’s operations to all capital providers) by its total sales.

### Why Use Revenue?

While EV/EBITDA is the most common multiple in investment banking, EBITDA can be negative or meaningless for fast-growing companies investing heavily in marketing and R&D. Revenue, on the other hand, is almost always positive and less prone to accounting manipulations (like differences in depreciation policies). By using revenue as the denominator, analysts can compare the core top-line generation ability of businesses of differing sizes.

### Interpreting the Multiple

When analyzing EV/Revenue:
- **High Ratio:** Means the company is relatively more expensive per unit of sales. This often characterizes high-growth technology companies with strong gross margins and recurring revenue (e.g., SaaS). Investors are paying a premium today for massive expected future scale.
- **Low Ratio:** Suggests the company is cheaper per unit of sales. Mature, slow-growing, or lower-margin businesses (like traditional retail or heavy industrials) typically trade at lower EV/Revenue multiples.

Generally, ratios might sit between 1x and 3x for average businesses, but high-growth tech firms can command multiples of 10x, 15x, or even higher. It is essential to compare a company's multiple only to peers within its niche industry.

## Formula

![[EV-Revenue]]

## Worked example

(none)

## Excel and modeling notes

When building a comparable company analysis (comps) in Excel, make sure that both the numerator (Enterprise Value) and denominator (Revenue) correspond to the same time period. Typically, you will align them by using Next Twelve Months (NTM) or Last Twelve Months (LTM) revenue. Remember that Enterprise Value is a point-in-time metric (current share price × shares outstanding, plus net debt), while revenue is a flow metric over a period.

## Interview-ready answer

EV/Revenue is a valuation multiple that compares a company's total enterprise value to its top-line sales. We use it primarily for companies that have negative earnings or EBITDA, such as early-stage tech startups, or when valuing a company purely on its ability to generate market share and top-line growth. It normalizes value on a per-unit basis while remaining capital structure-neutral.

## Pitfalls and gotchas

- **Ignores Profitability:** The biggest weakness of EV/Revenue is that it completely ignores profitability and cost structure. A company with $100M in revenue and 90% gross margins is vastly more valuable than a company with $100M in revenue and 10% gross margins, yet they could theoretically have the same EV/Revenue multiple.
- **Not a Cash Flow Proxy:** Unlike EBITDA, revenue is not a proxy for operating cash flow. Relying purely on EV/Revenue can blind an analyst to cash burn and capital expenditure requirements.
- **Mismatch of Time Periods:** Ensure the revenue used matches the capital structure snapshot (e.g., using forward 1-year revenue estimates against current EV).

## Sources

- [[IB Interview Questions - Common Valuation Multiples Explained]]
- [[CFI - Enterprise Value-to-Sales (EV-Sales) - Formula, Examples]]
