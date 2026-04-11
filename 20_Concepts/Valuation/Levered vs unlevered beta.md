---
type: concept
title: Levered vs unlevered beta
aliases: ["Equity beta", "Asset beta", "Observed beta"]
tags: ["valuation", "cost-of-capital", "capm"]
difficulty: intermediate
prerequisites: ["[[Beta]]", "[[CAPM]]", "[[Cost of equity]]"]
related: ["[[WACC]]", "[[Capital structure]]"]
sources: ["[[IB Interview Questions - Levered vs Unlevered Beta- When and Why to Unlever]]"]
status: draft
updated: 2026-04-11
---

# Levered vs unlevered beta

> **TL;DR.** Levered beta measures the risk of a company's equity including both business and financial risk, while unlevered beta isolates pure business risk by removing the effect of debt.

## When you'd use this

You use levered vs unlevered beta when applying comparable company analysis to value a target company, especially one with a different capital structure than its peers. It is necessary when building up the cost of equity using the Capital Asset Pricing Model (CAPM) for a private company or a public company undergoing a change in leverage (such as in an LBO).

## The 30-second version

Beta measures a stock's sensitivity to market movements. However, the beta observed for a public company (levered beta) reflects two things: the inherent risk of its operations (business risk) and the added risk from its debt (financial risk). Because companies choose different capital structures, you cannot directly compare their observed betas. Instead, you "unlever" their betas to strip out the financial risk, finding their pure "asset beta". You can then average these unlevered betas across comparable companies and "relever" the result to match your target company's specific debt-to-equity ratio.

## The full explanation

### Understanding Beta Risks

Beta is a key input in the Capital Asset Pricing Model (CAPM) for calculating the cost of equity. A beta of 1.0 means the stock moves in line with the market. The beta you look up on financial data platforms is **levered beta** (also called equity beta).

**Levered beta captures total equity risk**, which consists of:
- **Business risk**: The volatility inherent in the company's operations, industry, and competitive position.
- **Financial risk**: The additional volatility created by using debt in the capital structure. Fixed debt obligations amplify equity returns in both directions, making equity more volatile.

**Unlevered beta** (also called asset beta) measures only the systematic business risk of a company's operations, representing the beta a company would have if it carried no debt.

### Why Unlevering is Necessary

Capital structure is a choice, not an inherent characteristic of the business. Two companies in the same industry with similar operations should have similar unlevered betas regardless of how they choose to finance themselves.

When using comparable companies to determine beta for a target company, the comparables will likely have different leverage levels. Using their levered betas directly would inappropriately apply their financial risk profiles to your target. To compare pure operating risk, you must first unleash the comparables' betas.

### The Unlever and Relever Process

1. **Unlever comparables**: Apply the Hamada equation to strip out each comparable company's financial leverage and isolate its pure business risk.
2. **Calculate central tendency**: Take the median (preferred to avoid outliers) of the unlevered betas to find the industry asset beta.
3. **Determine target capital structure**: Decide on the appropriate D/E ratio for your target (current, management target, or industry average).
4. **Relever**: Apply the relevering formula using the target's D/E ratio and tax rate to get the appropriate equity beta for the target.
5. **Use in CAPM**: Plug the newly relevered beta into the CAPM formula to calculate the cost of equity.

## Formula

![[Hamada equation]]

## Worked example

(none)

## Excel and modeling notes

When performing these calculations in Excel, ensure you are using **market values** for both debt and equity in your D/E ratio calculations, rather than book values. Use the median, not the mean, when aggregating unlevered betas to prevent a single outlier (perhaps a highly levered or distressed comparable) from skewing your analysis. Additionally, be aware of circular references in DCF models where capital structure depends on equity value, which depends on WACC, which depends on capital structure; this is often resolved by using target weights.

## Interview-ready answer

[[What is the difference between levered and unlevered beta]]

## Pitfalls and gotchas

- **Using book values**: The D/E ratio should use market value of debt and market value of equity. Book values can differ significantly from market values and lead to incorrect adjustments.
- **Forgetting to relever**: Analysts sometimes calculate the median unlevered beta and mistakenly use it directly in CAPM. Unlevered beta is just an intermediate step; you must relever it to the target's capital structure.
- **Using inconsistent tax rates**: When unlevering each comparable's beta, use that specific company's tax rate. But when relevering the median beta for your target, use the **target company's tax rate**. Mixing these up is a common error.

## Sources

- [[IB Interview Questions - Levered vs Unlevered Beta- When and Why to Unlever]]
