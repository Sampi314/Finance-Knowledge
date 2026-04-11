---
type: concept
title: "Cost of debt"
aliases: ["Cost of debt financing"]
tags: ["valuation", "wacc"]
difficulty: intermediate
prerequisites: ["[[Cost of equity]]"]
related: ["[[Cost of equity]]"]
sources: ["[[IB Interview Questions - Capital Structure Decisions- Debt vs Equity Explained]]", "[[IB Interview Questions - How to Calculate WACC Step-by-Step]]"]
status: draft
updated: 2026-04-11
---

# Cost of debt

> **TL;DR.** The cost of debt represents the effective interest rate a company pays on its borrowings, adjusted for tax benefits.

## When you'd use this

The cost of debt is used as a primary input when calculating a company's Weighted Average Cost of Capital (WACC), which serves as the discount rate in a DCF valuation. It's also evaluated when a company is deciding how to finance a new project or acquisition, as it helps determine the cheapest source of capital.

## The 30-second version

The cost of debt is the return that lenders require to provide debt financing to a company. Unlike the cost of equity, it is generally observable from market interest rates or the company's current bond yields. Because interest payments are tax-deductible, the true cost to the company is the "after-tax" cost of debt, which is lower than the stated interest rate. Debt is typically cheaper than equity because it is less risky for investors (they get paid first in bankruptcy) and it provides a tax shield.

## The full explanation

### Why Debt is Cheaper than Equity
The cost of debt is almost always lower than the cost of equity for two interrelated reasons: **tax deductibility** and **seniority in the capital structure**.
1.  **Tax Shield:** Interest payments on debt are tax-deductible, meaning they reduce the company's taxable income.
2.  **Seniority:** In a bankruptcy or liquidation, debt holders are paid before equity holders. Because lenders face less risk, they accept a lower return.

### Methods for Calculating Cost of Debt
There are several ways to determine a company's pre-tax cost of debt:
- **Yield to Maturity (YTM):** For companies with publicly traded bonds, the current YTM reflects the market's required return.
- **Credit Spread Approach:** Add the company's credit spread (based on its credit rating) to the risk-free rate.
- **Average Interest Rate:** For private companies, divide historical Interest Expense by Average Total Debt.

### The Tax Shield
Because the government effectively subsidizes a portion of interest costs through tax savings, the effective cost is calculated on an after-tax basis by multiplying the pre-tax rate by $(1 - T)$, where $T$ is the corporate tax rate.

## Formula

![[After-tax Cost of Debt]]

## Worked example

(none)

## Excel and modeling notes

When building a WACC calculation in Excel, ensure that the tax rate used to calculate the after-tax cost of debt aligns with the long-term marginal tax rate of the company, rather than the historical effective tax rate, which can be distorted by one-time items.

## Interview-ready answer

"The cost of debt is the effective interest rate a company pays on its borrowed money. We calculate it by taking the pre-tax cost of debt—found by looking at the yield to maturity on existing bonds or adding a credit spread to the risk-free rate—and multiplying it by $(1 - \text{tax rate})$ to account for the interest tax shield."

## Pitfalls and gotchas

- Using the historical interest rate or book value of debt instead of current market rates (Yield to Maturity).
- Forgetting to multiply the pre-tax cost of debt by $(1 - \text{tax rate})$ when using it in WACC.
- Using an effective tax rate instead of a marginal tax rate for the tax shield calculation.

## Sources

- [[IB Interview Questions - Capital Structure Decisions- Debt vs Equity Explained]]
- [[IB Interview Questions - How to Calculate WACC Step-by-Step]]
