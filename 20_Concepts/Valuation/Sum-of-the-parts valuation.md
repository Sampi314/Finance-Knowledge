---
type: concept
title: "Sum-of-the-parts valuation"
aliases: ["SOTP valuation", "Break-up analysis", "SOTP"]
tags: ["valuation", "conglomerate-discount", "spin-off"]
difficulty: intermediate
prerequisites: ["[[Enterprise value]]", "[[Equity value]]", "[[Comparable company analysis]]", "[[DCF valuation]]"]
related: ["[[The bridge from EV to equity value]]", "[[Football field chart]]"]
sources: ["[[IB Interview Questions - Sum of the Parts (SOTP) Valuation- When and How to Use It]]", "[[Financial Modeling NYC - Building Sensitivity Tables the Right Way – Tutorial]]", "[[BIWS - Sum of the Parts Valuation- Tutorial and Excel Example]]", "[[Macabacus - Sum-of-the-Parts Financial Analysis Guide | EV]]"]
status: draft
updated: 2024-05-18
---

# Sum-of-the-parts valuation

> **TL;DR.** A sum-of-the-parts (SOTP) valuation determines a company's total value by separately valuing its individual business segments and adding those values together.

## When you'd use this

You would use SOTP valuation when a company operates in multiple, distinct industries with different growth, profitability, and risk profiles. A single valuation multiple often fails to capture the true value of diversified conglomerates. This method is frequently used when defending against hostile takeovers, assessing potential spin-offs, split-offs, or divestitures, and identifying if a conglomerate is trading at a "conglomerate discount" relative to the standalone value of its pieces.

## The 30-second version

A sum-of-the-parts (SOTP) analysis, also known as a break-up analysis, involves segregating a diversified company into its distinct business segments. Instead of applying one blended valuation metric to the entire company, you apply segment-specific valuation methods (like DCF or trading multiples) based on each segment's unique characteristics. Once you calculate the implied enterprise value of each division, you add them all together to get the total enterprise value. From there, you deduct net debt and make other non-operating adjustments to arrive at the company's total equity value.

## The full explanation

### Segmenting the Business

The first step in a SOTP valuation is to define the perimeter of each business unit. Companies are typically segmented by business line, geography, asset class, or regulatory perimeter. It is important to align this segmentation with how the business is managed and reported to ensure credibility and auditability.

### Normalizing Financials

Once the segments are defined, you need separate financial statements or projections for each. This involves gathering segment-level data from 10-Ks, 10-Qs, investor presentations, or research reports. You must normalize the financials to reflect sustainable performance, which includes adjusting for non-recurring items, allocating shared corporate overhead appropriately, and aligning accounting policies across units.

### Valuing Each Segment

A robust SOTP valuation matches the valuation methodology to the economic reality of each segment. A fast-growing software division might be valued using an EV/Revenue multiple, while a mature manufacturing division might be valued using a DCF model or EV/EBITDA multiple. Relevant comparable companies and precedent transactions should be selected specifically for each division.

### Bridging to Equity Value

After valuing each segment independently, you add the implied enterprise values together to determine the consolidated enterprise value. The final step is to build the bridge to equity value. You must account for corporate center costs (distinguishing between eliminable and strategic holding costs), net debt, pension liabilities, minority interests, and non-operating assets to arrive at the final equity value.

## Formula

(none)

## Worked example

(none)

## Excel and modeling notes

- Allocate corporate overhead carefully. If depreciation or amortization are not provided by segment, allocate them based on the percentage of assets, revenues, or industry norms.
- Ensure that the sum of the financial metrics (like EBITDA or revenue) across all segments equals the consolidated financial metrics for the entire company.
- Clearly distinguish between truly eliminable corporate costs, strategic holding costs, and temporary transition costs, as this distinction directly impacts equity value in a transaction context.
- Create transparent valuation bridges for each segment that show the forecast drivers, margin evolution, and capital expenditure assumptions leading to the enterprise value.

## Interview-ready answer

In a sum-of-the-parts valuation, you value a diversified company by analyzing each of its business segments separately using the most appropriate valuation methodology for that specific segment. You calculate the implied enterprise value for each division, add them together to find the company's total enterprise value, and then bridge to equity value by subtracting net debt and adjusting for corporate overhead and non-operating items.

## Pitfalls and gotchas

- Applying inappropriate valuation methodologies: Using the same multiple for segments with vastly different growth or risk profiles undermines the SOTP analysis.
- Mishandling corporate costs: Inconsistent treatment or improper allocation of shared corporate overhead is a common point of failure.
- Incomplete financial data: Companies do not always break out detailed financials for every segment, requiring estimation and allocation that can introduce errors.
- Ignoring synergy losses: When evaluating a spin-off, failing to account for the loss of shared synergies or economies of scale can overstate the standalone value of the segments.

## Sources

- [[IB Interview Questions - Sum of the Parts (SOTP) Valuation- When and How to Use It]]
- [[Financial Modeling NYC - Building Sensitivity Tables the Right Way – Tutorial]]
- [[BIWS - Sum of the Parts Valuation- Tutorial and Excel Example]]
- [[Macabacus - Sum-of-the-Parts Financial Analysis Guide | EV]]
