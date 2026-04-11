---
type: concept
title: "Beta"
aliases: ["beta (β)"]
tags: ["valuation", "wacc", "risk"]
difficulty: beginner
prerequisites: []
related: ["[[CAPM]]", "[[Cost of equity]]", "[[Levered vs unlevered beta]]"]
sources: ["[[IB Interview Questions - Levered vs Unlevered Beta- When and Why to Unlever]]", "[[Wall Street Prep - Levered and Unlevered Beta (β) - Formula + Calculator]]"]
status: draft
updated: 2026-04-11
---

# Beta

> **TL;DR.** Beta measures the sensitivity of a stock's returns relative to the overall market's returns.

## When you'd use this

You use beta when determining the cost of equity for a company, most commonly through the Capital Asset Pricing Model (CAPM). It forms a crucial input in calculating a company's Weighted Average Cost of Capital (WACC) for intrinsic valuation methodologies like a Discounted Cash Flow (DCF) model.

## The 30-second version

Beta (β) quantifies systematic risk—the risk that affects the entire market and cannot be mitigated through portfolio diversification (e.g., recessions, global events). The overall stock market is defined as having a beta of 1.0. If a company's stock has a beta greater than 1.0, it is more volatile than the market, demanding a higher expected return from investors to compensate for the additional risk. A beta of less than 1.0 indicates the stock is less volatile than the broader market.

## The full explanation

Beta is an integral component of CAPM. It defines the relationship between the systematic risk of an asset and its expected return. Investors demand compensation for assuming non-diversifiable risk, making beta the defining variable in how much equity investors expect to earn.

### Levered vs Unlevered Beta

There are two primary types of beta used in corporate finance valuation:

1. **Levered Beta (Equity Beta):** This is the beta you observe on financial platforms like Bloomberg or Yahoo Finance. It reflects both the inherent business risk of a company's operations and the financial risk created by the debt in its capital structure. As debt increases, levered beta increases because fixed debt obligations amplify the volatility of returns for equity holders.
2. **Unlevered Beta (Asset Beta):** This isolates pure business risk by removing the effects of financial leverage. It represents the beta a company would theoretically have if it were financed entirely by equity. Unlevered beta is primarily used to compare the operational risk profiles of companies with different capital structures.

When valuing a private company or a company whose capital structure is expected to change (e.g., an LBO), you typically find the unlevered beta of comparable public companies, calculate the median, and then "relever" that beta to your target company's capital structure.

### Interpreting Beta

- **β = 1:** The security's price moves with the market.
- **β > 1:** The security is more volatile than the market.
- **β < 1:** The security is less volatile than the market.
- **β = 0:** The security has no correlation with the market.

## Formula

The mathematical calculation of beta involves dividing the covariance of the security's returns and the market's returns by the variance of the market's returns:

$$ \beta = \frac{Covariance(R_e, R_m)}{Variance(R_m)} $$

## Worked example

(none)

## Excel and modeling notes

When building valuation models, never use a comparable company's levered beta directly if its capital structure differs from your target company. Always unlever the comparable company's beta using its debt-to-equity ratio and tax rate, then relever it using your target company's intended capital structure.

## Interview-ready answer

Beta measures a stock's systematic risk relative to the broader market, dictating the expected return for equity investors in the CAPM formula. It can be observed as levered beta, which includes both operational and financial risk, or calculated as unlevered beta, which isolates pure business risk for comparability. [[What happens to beta as a company increases leverage?]]

## Pitfalls and gotchas

- Using a company's historical beta assumes its past risk profile perfectly predicts its future, which may not be accurate if its business model has shifted.
- Failing to unlever and relever beta when using comparable companies with different leverage levels.
- Using book values instead of market values for debt and equity when calculating the debt-to-equity ratio to adjust beta.

## Sources

- [[IB Interview Questions - Levered vs Unlevered Beta- When and Why to Unlever]]
- [[Wall Street Prep - Levered and Unlevered Beta (β) - Formula + Calculator]]
