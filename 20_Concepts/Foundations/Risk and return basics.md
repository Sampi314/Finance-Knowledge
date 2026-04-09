---
type: concept
title: "Risk and return basics"
aliases: []
tags: ["foundations", "risk", "return", "capm"]
difficulty: beginner
prerequisites: []
related: []
sources: ["[[Damodaran - adamodar_New_Home_Page_littlebook_discountrates_htm]]", "[[Financial Modeling NYC - Capital Asset Pricing Model (CAPM)]]"]
status: draft
updated: 2026-04-09
---

# Risk and return basics

> **TL;DR.** Risk and return basics form the foundation of investment assessment, where the expected return of an investment must compensate for the systematic risk taken, often evaluated using frameworks like the Capital Asset Pricing Model (CAPM).

## When you'd use this

You use this when estimating the cost of capital for a company or when evaluating any potential investment. It helps you understand how investors balance the demand for higher expected returns with higher levels of risk.

## The 30-second version

At its core, investing involves trading current certainty for future uncertainty. Cash flows that are riskier are assigned a lower present value, which is reflected mathematically by applying a higher discount rate. A central idea in finance is that investors should be compensated only for non-diversifiable risk (systematic risk)—the risk attributable to the broader market. Models like the Capital Asset Pricing Model (CAPM) use a stock's beta, a risk-free rate, and an expected market return to estimate a fair expected return that adequately compensates an investor for the risk they take.

## The full explanation

### Business Risk vs. Equity Risk
There are two ways of looking at risk in relation to a firm's balance sheet: the risk of the firm's operations and assets (business risk), and the risk borne by equity investors (equity risk). Equity risk depends not only on the underlying business risk but also on the firm's choice of capital structure. When a firm uses more debt, the business risk doesn't necessarily change, but the equity risk increases because debt payments represent fixed obligations that take precedence over equity returns.

### Measuring Risk and Cost of Equity
The risk in an equity investment is challenging to measure because, unlike debt which has explicit interest rates, the cost of equity is implicit and depends on the varying perceptions of different investors. To standardize this, financial theory focuses on the *marginal investor*—the one most likely to influence the market price. The marginal investor is assumed to be fully diversified. Thus, only the non-diversifiable, or market, risk is priced.

### The Capital Asset Pricing Model (CAPM)
CAPM is the most widely used model to determine the expected return on an investment based on its systematic risk. It uses three key inputs:
1.  **Risk-free rate:** The expected return on an investment with guaranteed returns (often derived from long-term government bonds).
2.  **Beta:** A measure of the asset's volatility relative to the broader market.
3.  **Equity risk premium:** The additional return that investors demand for taking on the risk of equities as a class compared to a risk-free asset.

Despite some simplifying assumptions and valid criticisms, CAPM remains the core framework for assessing the trade-off between risk and expected return.

## Formula

![[Capital Asset Pricing Model (CAPM)]]

## Worked example

If a stock has a beta of 1.2, the risk-free rate is 3%, and the expected market return is 8%, the CAPM would estimate the expected return on the stock to be 9% (3% + 1.2 * (8% – 3%)).

## Excel and modeling notes

When building a financial model, the expected return from CAPM represents the firm's Cost of Equity. This is a critical input in calculating the Weighted Average Cost of Capital (WACC), which is used as the discount rate for discounting future cash flows. Ensure that the time horizon for the risk-free rate matches the time horizon of the cash flows being modeled (e.g., matching a 10-year treasury yield with long-term cash flow projections).

## Interview-ready answer

[[How do we measure the risk of equity investments?]]

## Pitfalls and gotchas

- Using a short-term risk-free rate (like a 6-month treasury bill) to discount long-term cash flows exposes the model to reinvestment risk; a long-term bond yield is typically more appropriate.
- Failing to account for changes in the firm's capital structure over time. As a company's debt-to-equity ratio changes, its equity risk and cost of equity will change as well.
- Assuming historical beta is a perfect predictor of future risk, especially for young companies or companies undergoing significant structural changes.

## Sources

- [[Damodaran - adamodar_New_Home_Page_littlebook_discountrates_htm]]
- [[Financial Modeling NYC - Capital Asset Pricing Model (CAPM)]]