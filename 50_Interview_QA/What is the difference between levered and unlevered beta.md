---
type: question
title: What is the difference between levered and unlevered beta
tests: ["[[Levered vs unlevered beta]]"]
difficulty: beginner
updated: 2026-04-11
---

# What is the difference between levered and unlevered beta

## The question

What is the difference between levered and unlevered beta?

## Short answer (30 seconds)

Levered beta is the observed equity beta that reflects both business risk and the financial risk created by debt in a company's capital structure. Unlevered beta strips out this financial leverage to isolate pure business risk. We unlever when using comparable company betas to value a target with a different capital structure.

## Long answer (2 minutes)

- **Levered Beta (Equity Beta)**: This is what you observe directly on platforms like Bloomberg or Yahoo Finance. It represents the total systematic risk of a company's equity, incorporating both the inherent operating risk of the business (business risk) and the amplified volatility that comes from fixed debt obligations (financial risk).
- **Unlevered Beta (Asset Beta)**: This is a hypothetical measure of risk. It represents the beta a company would have if it were financed entirely with equity and carried no debt. It captures pure business risk.
- **Why it matters**: Capital structure is a choice, and companies in the same industry can have widely different leverage profiles. Because you can't compare the levered betas of companies with different debt levels apples-to-apples, you must "unlever" the comparables' betas to find their true business risk. Then, you find the median unlevered beta across the industry and "relever" it to your target company's specific capital structure. This ensures you apply an accurate cost of equity that reflects the target's actual financial risk.

## Common follow-ups

- What happens to beta as a company increases leverage? It increases. Levered beta increases because equity holders bear more risk when debt increases; the fixed debt obligations amplify equity returns in both directions. Unlevered beta remains unchanged as it isolated pure business risk.
- Why do we multiply by (1-T) in the beta formulas? The tax shield from interest expense reduces the effective cost of debt and partially offsets the leverage risk. The (1-T) term accounts for this tax benefit. Higher tax rates mean a larger tax shield, reducing the magnitude of the leverage adjustment.
