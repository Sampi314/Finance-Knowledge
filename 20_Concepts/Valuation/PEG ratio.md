---
type: concept
title: PEG ratio
aliases: [Price/Earnings-to-Growth, PEG]
tags: [valuation, relative-valuation, multiples]
difficulty: intermediate
prerequisites: ["[[P-E ratio]]"]
related: []
sources: ["[[Damodaran - PEG Ratios]]"]
status: draft
updated: 2026-04-12
---

# PEG ratio

> **TL;DR.** The PEG ratio compares a stock's Price-to-Earnings (PE) ratio to its expected growth rate, aiming to identify relative value while neutralizing the growth effect.

## When you'd use this

You'd use the PEG ratio when analyzing relative value among comparable companies to account for their different expected earnings growth rates. It helps identify companies that look "cheap" based on their PE ratio compared to their growth potential, though this must be considered alongside risk and reinvestment efficiency.

## The 30-second version

The PEG ratio is the ratio of a company's market price to its expected growth in earnings per share. In the simplest investment strategies, firms with PE ratios lower than their expected growth rates (or a PEG under 1.0) are sometimes viewed as undervalued. However, relying solely on this ratio can be misleading because PEG ratios are still heavily influenced by a company's risk profile, expected growth, and required cash flow patterns.

## The full explanation

The PEG ratio adjusts the standard PE ratio by dividing it by the expected growth rate in earnings per share. While it is often used as a rule of thumb by analysts and portfolio managers, this ratio does not fully "neutralize" the growth effect due to the complex, non-linear relationship between growth and value.

As a framework for understanding fundamentals:
1. **Risk:** High-risk companies will trade at much lower PEG ratios than low-risk companies with the same expected growth rate. Consequently, a company that appears undervalued on a PEG ratio basis might simply be the riskiest firm in its sector.
2. **Quality of Growth:** Companies that achieve growth more efficiently—by investing less capital into higher return projects—will command higher PEG ratios. Thus, "cheap" PEG companies might actually be those with high reinvestment requirements and poor project returns.
3. **Growth Rate Bias:** The relationship is not perfectly linear; companies with very high or very low growth rates tend to exhibit higher PEG ratios than average-growth firms.

Interest rates also play a significant role. When interest rates are higher, fewer stocks will appear undervalued according to simple PEG rules, whereas lower interest rates will inflate PE multiples across the board, reducing aggregate PEG ratios.

## Formula

![[PEG Ratio]]

## Worked example

(none)

## Excel and modeling notes

When calculating the PEG ratio in Excel, ensure consistency across the components. The growth rate must be based on the same base year, projected over the same time horizon (e.g., a 5-year expected growth rate), and derived from consistent sources (such as consensus estimates). If evaluating foreign companies or ADRs, match the earnings metric appropriately.

## Interview-ready answer

The PEG ratio measures relative value by dividing a company's PE ratio by its expected earnings growth rate. While it helps adjust multiples for growth, it doesn't account for differing risk profiles or capital efficiency, meaning a low PEG ratio could simply reflect higher risk or lower-quality growth rather than true undervaluation.

## Pitfalls and gotchas

- Comparing PEG ratios across companies implicitly assumes they have similar risk profiles and payout characteristics.
- Using inconsistent inputs (e.g., a forward PE paired with historical growth, or differing base years) invalidates the calculation.
- The company with the lowest PEG ratio in a sector may simply be the riskiest, rather than the most undervalued.

## Sources

- [[Damodaran - PEG Ratios]]
