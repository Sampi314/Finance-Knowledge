---
type: concept
title: "Cost of equity"
aliases: ["Cost of Equity", "ke", "Ke"]
tags: [valuation, wacc, discount-rate]
difficulty: beginner
prerequisites: []
related: ["[[Free cash flow]]", "[[Present value]]"]
sources: ["[[Wall Street Prep - Cost of Equity (ke) - Formula + Calculator]]", "[[CFI - Cost of Equity - Formula, Guide, How to Calculate Cost of Equity]]", "[[BIWS - Cost of Equity- Real-Life Examples and Excel Calculations]]"]
status: draft
updated: 2026-04-11
---

# Cost of equity

> **TL;DR.** The cost of equity is the annualized rate of return that investors demand to compensate them for the risk of buying a company's common stock.

## When you'd use this

You use the cost of equity primarily in valuation and Discounted Cash Flow (DCF) analysis. It serves as the discount rate for discounting levered free cash flows (FCFE), or as a core component when calculating the Weighted Average Cost of Capital (WACC) to discount unlevered free cash flows (FCFF). It is essential for determining whether an investment or project will generate enough return to satisfy equity investors.

## The 30-second version

The Cost of Equity ($K_e$) represents two sides of the same coin. To equity investors, it is the target annualized rate of return they expect to earn from buying common stock, considering the risk of that stock relative to the broader market. To the company, it represents the "cost" of raising capital through issuing additional common stock to fund its operations, which includes the cash cost of paying dividends and the implicit cost of equity dilution.

Unlike debt, which has a contracted interest rate, the cost of equity is theoretical and unobservable. It is typically estimated using the Capital Asset Pricing Model (CAPM) or the Dividend Capitalization Model.

## The full explanation

Because equity investors take on more risk than debt holders (since equity sits at the bottom of the capital structure and gets paid last in a liquidation), they demand a higher expected rate of return. The cost of equity is the way we quantify that expected return.

There are two primary methods to calculate the Cost of Equity:

### 1. Capital Asset Pricing Model (CAPM)

The most widely used method to estimate the cost of equity is the CAPM. This approach ties the expected return of an asset to its systematic risk relative to the overall market.

The formula adds a risk premium to a baseline risk-free rate, scaled by a factor called Beta ($\beta$):
- **Risk-Free Rate ($R_f$):** The yield on a default-free government bond (typically the 10-year US Treasury note). It represents the return an investor could get with zero risk.
- **Beta ($\beta$):** A measure of the stock's volatility relative to the broader market. A Beta of 1 means the stock moves with the market; >1 means it is more volatile; <1 means it is less volatile.
- **Equity Risk Premium (ERP):** The excess return that investors demand for investing in the overall stock market rather than in risk-free bonds (Expected Market Return - Risk-Free Rate).

### 2. Dividend Capitalization Model (Dividend Discount Model)

For mature companies that pay a stable, predictable dividend, the cost of equity can be estimated using the Dividend Capitalization Model. This approach assumes that the cost of equity is equal to the dividend yield plus the expected growth rate of those dividends.

The inputs are the expected dividend next year ($D_1$), the current stock price ($P_0$), and the expected constant growth rate of the dividend ($g$). This model is much less common because it only works for dividend-paying companies and ignores market risk completely.

## Formula

The Cost of Equity using CAPM:

![[Capital Asset Pricing Model (CAPM)]]

The Cost of Equity using the Dividend Capitalization Model:

$$ K_e = \frac{D_1}{P_0} + g $$

*Where:*
*   $K_e$ = Cost of Equity
*   $D_1$ = Dividends per share next year
*   $P_0$ = Current share price
*   $g$ = Expected dividend growth rate

## Worked example

Imagine we want to calculate the cost of equity for a company using CAPM.

1. **Risk-Free Rate:** We look up the yield on the 10-year US Treasury note and find it is 3.0%.
2. **Beta:** Based on historical regression or industry comparables, the company has a Beta of 1.2, meaning it's 20% more volatile than the market.
3. **Expected Market Return:** We estimate the broader stock market will return 8.0% annually.
4. **Equity Risk Premium (ERP):** 8.0% - 3.0% = 5.0%.

$$ K_e = 3.0\% + (1.2 \times 5.0\%) $$
$$ K_e = 3.0\% + 6.0\% $$
$$ K_e = 9.0\% $$

In this scenario, equity investors require a 9.0% annualized return to invest in this company.

Using the Dividend Capitalization Model for a company trading at \$50 per share ($P_0$), paying a \$2.00 dividend next year ($D_1$), and growing dividends at 3% ($g$):

$$ K_e = \frac{2.00}{50} + 3.0\% = 4.0\% + 3.0\% = 7.0\% $$

## Excel and modeling notes

- When calculating WACC in a DCF, you almost exclusively use CAPM for the cost of equity.
- When sourcing inputs, the risk-free rate should match the duration and currency of the cash flows (e.g., US 10-year Treasury yield for a 5-10 year US-based DCF).
- Beta can be tricky to source for private companies. You typically have to find publicly traded comparable companies, "unlever" their Betas to strip out the effects of debt, take the median, and then "relever" it based on your target company's capital structure.

## Interview-ready answer

If asked "How do you calculate the Cost of Equity?" your answer should immediately reference CAPM:

"The most common way to calculate the cost of equity is the Capital Asset Pricing Model, or CAPM. The formula is Risk-Free Rate plus Beta multiplied by the Equity Risk Premium.

The Risk-Free Rate is typically the yield on a 10-year Treasury note. Beta measures the stock's volatility relative to the broader market. And the Equity Risk Premium is the expected return of the market minus the risk-free rate, representing the extra compensation investors demand for holding stocks instead of bonds.

Alternatively, for mature, dividend-paying companies, you could use the Dividend Discount Model, which is the dividend yield plus the dividend growth rate."

## Pitfalls and gotchas

- **Cost of Equity vs Cost of Debt:** Cost of equity is almost always higher than the cost of debt. This is because debt is secured, guarantees payment, and sits higher in the capital structure, meaning debtholders get paid before equity holders if the company goes bankrupt.
- **WACC Confusion:** Don't use Cost of Equity as the discount rate for Unlevered Free Cash Flow (FCFF). Cost of equity only represents equity holders, so it should only be used to discount Levered Free Cash Flow (FCFE). FCFF must be discounted using the Weighted Average Cost of Capital (WACC), which blends both the cost of equity and the cost of debt.
- **Negative Beta:** While mathematically possible, plugging a negative Beta into CAPM implies an expected return lower than the risk-free rate, which breaks economic logic (nobody pays to take on equity risk).

## Sources

- [[Wall Street Prep - Cost of Equity (ke) - Formula + Calculator]]
- [[CFI - Cost of Equity - Formula, Guide, How to Calculate Cost of Equity]]
- [[BIWS - Cost of Equity- Real-Life Examples and Excel Calculations]]
