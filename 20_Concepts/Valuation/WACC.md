---
type: concept
title: "WACC"
aliases: ["Weighted Average Cost of Capital"]
tags: ["valuation", "cost-of-capital", "dcf"]
difficulty: intermediate
prerequisites: ["[[Cost of equity]]", "[[Cost of debt]]", "[[Capital structure]]"]
related: ["[[Intrinsic vs relative valuation]]"]
sources: ["[[IB Interview Questions - How to Calculate WACC Step-by-Step]]"]
status: draft
updated: 2026-04-11
---

# WACC

> **TL;DR.** The Weighted Average Cost of Capital (WACC) represents a company's blended cost of financing across all capital sources and serves as the discount rate for unlevered free cash flows in DCF models.

## When you'd use this

WACC is primarily used as the discount rate in Discounted Cash Flow (DCF) valuations to determine the enterprise value of a business. It is also used in capital budgeting to evaluate whether potential projects or investments will generate returns that exceed the company's cost of capital.

## The 30-second version

WACC combines the cost of equity (what shareholders require as returns) and the cost of debt (what lenders charge for borrowing) into a single rate that reflects a company's overall cost of capital. It weights each capital source according to its proportion of total financing (ideally using market values rather than book values). Because interest expense is tax-deductible, the cost of debt component uses an after-tax rate, making debt generally "cheaper" than equity, up to a point where financial distress risks outweigh the tax benefits.

## The full explanation

The Weighted Average Cost of Capital (WACC) represents the blended rate of return a company must earn to satisfy all of its capital providers, both debt holders and equity investors.

When you discount future cash flows to present value in a DCF model, you are asking: what return must this investment generate to satisfy all capital providers? WACC answers that question. Since unlevered free cash flow represents cash available to all capital providers, we discount at this blended rate representing all providers' required returns.

### Market Values vs. Book Values

WACC should reflect the current cost of raising capital, which is best captured by market values rather than historical book values.
- **Equity market value:** Calculated using market capitalization (current stock price multiplied by fully diluted shares outstanding).
- **Debt market value:** The trading price of bonds. If debt isn't publicly traded, book value is often used as an approximation.

Some analysts use a **target capital structure** instead of the current capital structure, particularly when the company is undergoing significant financing changes or if its current structure is abnormal compared to industry norms.

### The Components of WACC

The two primary components of WACC are the Cost of Equity and the Cost of Debt.

**Cost of Equity** is usually calculated using the Capital Asset Pricing Model (CAPM): $R_e = R_f + \beta \times (R_m - R_f)$. It represents the return shareholders expect to compensate for the time value of money and the company's systematic risk.

**Cost of Debt** represents the effective interest rate a company pays on its borrowings, often found via Yield to Maturity on existing bonds or a credit spread approach. Importantly, because interest expense is tax-deductible, the effective cost of debt is lower than the stated interest rate. This reduction is called the interest tax shield, requiring the use of the after-tax cost of debt in the WACC calculation: $R_d \times (1 - T)$.

### Capital Structure Dynamics
Initially, as a company takes on more debt, its WACC typically decreases because debt is cheaper than equity after the tax shield. However, as leverage increases, both debt and equity become riskier (beta increases). Eventually, WACC reaches a minimum and then increases with additional leverage.

## Formula

![[WACC Formula]]

## Worked example

[[WACC Calculation Example]]

## Excel and modeling notes

When building a DCF model, WACC assumptions significantly impact terminal value calculations, which often represent 60-80% of total DCF value. A seemingly small 0.5% change in WACC might shift terminal value by 10-15%, making sensitivity analysis around WACC assumptions critically important.

Ensure consistency across your inputs. The risk-free rate should match the projection duration, beta should use an appropriate historical period, and the capital structure used should be applied consistently.

## Interview-ready answer

[[Walk me through how you calculate WACC]]

## Pitfalls and gotchas

- **Using Book Values Instead of Market Values:** Using book equity when market capitalization is much higher underweights equity and produces an artificially low WACC.
- **Forgetting the Tax Shield:** A common error is using the pre-tax cost of debt instead of the after-tax cost.
- **Mismatching Time Periods:** Using inconsistent timeframes for the risk-free rate, beta estimation, or capital structure assumptions.
- **Using Inappropriate Beta:** Published betas can be noisy or reflect outdated capital structures.
- **Ignoring Country Risk:** For companies operating in emerging markets, standard CAPM may underestimate required returns without adding a country risk premium.

## Sources

- [[IB Interview Questions - How to Calculate WACC Step-by-Step]]
