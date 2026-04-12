---
type: concept
title: EV/EBITDA
aliases: ["EV to EBITDA"]
tags: ["valuation", "multiples", "comps"]
difficulty: beginner
prerequisites: ["[[Enterprise value]]", "[[EBITDA formula]]"]
related: ["[[Trading multiples]]", "[[Comparable company analysis]]"]
sources: ["[[IB Interview Questions - Enterprise Value vs Equity Value- Complete Guide]]", "[[IB Interview Questions - How to Build a Comparable Company Analysis (Comps)]]", "[[IB Interview Questions - Precedent Transactions Analysis - Step-by-Step Guide]]"]
status: draft
updated: 2026-04-12
---

# EV/EBITDA

> **TL;DR.** EV/EBITDA is a capital structure-neutral valuation multiple that measures a company's total value relative to its operating cash flow before interest, taxes, depreciation, and amortization.

## When you'd use this

You would use EV/EBITDA when comparing companies in the same industry that have different capital structures (i.e., different levels of debt and equity). It is the most commonly used multiple in comparable company analysis and precedent transaction analysis because it allows you to evaluate the core operating value of businesses irrespective of how they are financed.

## The 30-second version

EV/EBITDA is a ratio where the numerator is Enterprise Value (the total cost to acquire the entire operating business, including debt) and the denominator is EBITDA (a proxy for operating cash flow). By matching a capital structure-neutral valuation metric (Enterprise Value) with a capital structure-neutral profitability metric (EBITDA), this multiple provides a clean comparison of how the market values the core operations of different businesses. A higher multiple typically indicates that the market expects higher growth or lower risk.

## The full explanation

EV/EBITDA stands for Enterprise Value to Earnings Before Interest, Taxes, Depreciation, and Amortization. It is a cornerstone of relative valuation methodology, particularly in investment banking and M&A.

**Capital Structure Neutrality**
The fundamental advantage of EV/EBITDA is its neutrality to capital structure. Because Enterprise Value captures the value available to all investors (both debt and equity holders) and EBITDA measures profitability before the impact of interest expense (which depends on debt), the ratio accurately reflects the operating performance of a business regardless of its financing decisions.

**M&A Relevance**
In M&A, EV/EBITDA is the preferred metric because an acquirer buys the entire enterprise, assuming the target's debt and receiving its cash. It provides a more accurate picture of the true acquisition cost relative to the operating cash flow the business generates.

**Numerator and Denominator Consistency**
A key principle in valuation is that the numerator and denominator of a multiple must align in terms of the stakeholders they represent. Enterprise Value represents the value to all capital providers, so it must be paired with a metric like EBITDA, which represents cash flow available to all capital providers (before debt service).

## Formula

$$ \text{EV/EBITDA} = \frac{\text{Enterprise Value}}{\text{LTM EBITDA}} $$

## Worked example

[[Company A vs Company B EV-EBITDA comparison]]

## Excel and modeling notes

When building comps in Excel, calculate both trailing (LTM) and forward (NTM) EV/EBITDA multiples. NTM multiples are often preferred as they reflect market expectations of future performance. Ensure you apply the same definitions and adjustments for EBITDA across all comparable companies.

## Interview-ready answer

EV/EBITDA is an enterprise value multiple that measures a company's total operating value relative to its operating cash flow. Because both Enterprise Value and EBITDA are calculated before the impact of interest and debt, EV/EBITDA is a capital structure-neutral metric. This makes it superior to P/E when comparing companies with different leverage levels, as it allows us to evaluate the core operating businesses purely on their own merits without the distortion of financing choices.

## Pitfalls and gotchas

- Confusing EV multiples with equity multiples: Never pair Enterprise Value with Net Income, or Equity Value with EBITDA.
- Ignoring capital intensity: EV/EBITDA ignores depreciation and amortization, which can be misleading for capital-intensive businesses. In such cases, EV/EBIT might be more appropriate.
- Failing to adjust for non-recurring items: Ensure EBITDA is properly normalized for one-time charges or unusual expenses to get a true picture of recurring operating cash flow.

## Sources

- [[IB Interview Questions - Enterprise Value vs Equity Value- Complete Guide]]
- [[IB Interview Questions - How to Build a Comparable Company Analysis (Comps)]]
- [[IB Interview Questions - Precedent Transactions Analysis - Step-by-Step Guide]]
