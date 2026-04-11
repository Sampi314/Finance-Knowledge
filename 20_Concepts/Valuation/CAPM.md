---
type: concept
title: "CAPM"
aliases: ["Capital Asset Pricing Model"]
tags: ["valuation", "cost-of-capital", "finance"]
difficulty: intermediate
prerequisites: ["[[Cost of equity]]"]
related: ["[[Beta]]", "[[Equity risk premium]]"]
sources: ["[[Wall Street Prep - Capital Asset Pricing Model (CAPM) - Formula + Calculator]]", "[[Financial Modeling NYC - Capital Asset Pricing Model (CAPM)]]", "[[Project Finance - EMRP Issues in CAPM]]"]
status: draft
updated: 2026-04-11
---

# CAPM

> **TL;DR.** The Capital Asset Pricing Model (CAPM) is a financial model used to determine the expected return on an investment based on its systematic risk.

## When you'd use this

You would use CAPM when calculating the cost of equity (Ke), which is a core component of the weighted average cost of capital (WACC). It provides a framework to assess the risk and return tradeoff of different investments.

## The 30-second version

CAPM calculates the expected return of an asset by considering the risk-free rate, the asset's beta (a measure of its volatility relative to the market), and the expected market return. It connects the expected return on a security to its sensitivity to the broader market.

## The full explanation

The Capital Asset Pricing Model (CAPM) establishes the relationship between the risk and expected return on an equity security based on three underlying variables.

### 1. Risk-Free Rate
This is the baseline return of an investment with zero risk. It is typically treated as an input based on the current 10-year treasury rate.

### 2. Beta
Beta measures the systematic risk of a security compared to the broader market (non-diversifiable risk). For instance, a company with a beta of 1.0 would expect to see returns consistent with the overall stock market returns. But if that company were to have a beta of 2.0, it would expect a return of 20%, assuming the market had gone up by 10%. The standard procedure for estimating the beta of a company is through a regression model that compares the historical market index returns and company-specific returns, making the calculation "backward-looking".

### 3. Equity Risk Premium (ERP)
Also known as the market risk premium, the ERP measures the incremental risk (or excess return) of investing in equities over risk-free securities. It serves as additional compensation for investors to have an incentive to take on the risk of potential loss of capital. The EMRP compensates for upside and downside volatility, while a credit spread deals only with downside risk.

## Formula

![[CAPM Formula]]

## Worked example

(none)

## Excel and modeling notes

(none)

## Interview-ready answer

The CAPM formula states that the cost of equity is equal to the risk-free rate plus the product of beta and the equity risk premium. It estimates the expected rate of return for equity holders based on the perceived systematic risk.

## Pitfalls and gotchas

- The standard procedure for estimating beta relies on "backward-looking" historical regression, which may not be an accurate indicator of future share price performance.
- The equity market risk premium (EMRP) is controversial. If the EMRP is higher than the real growth rate in the economy, investors as a group will continue to get richer while the rest of the economy will become poorer, making excessively high EMRP assumptions questionable.
- Changes in the cost of capital can produce capital gains or losses measured in the market index that do not relate to the earning power of a company. Thus, declines in the cost of capital can lead to increases in market indices, distorting historical premium estimates.
- Estimates of the market risk premium can vary by a wide margin (e.g., from 4% to 12%), making the CAPM highly sensitive to this input.

## Sources

- [[Wall Street Prep - Capital Asset Pricing Model (CAPM) - Formula + Calculator]]
- [[Financial Modeling NYC - Capital Asset Pricing Model (CAPM)]]
- [[Project Finance - EMRP Issues in CAPM]]
