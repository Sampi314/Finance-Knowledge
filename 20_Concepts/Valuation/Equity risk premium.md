---
type: concept
title: Equity risk premium
aliases: ["ERP", "Market risk premium"]
tags: [valuation, erp, risk, capm]
difficulty: intermediate
prerequisites: ["[[Cost of equity]]", "[[The risk-free rate]]"]
related: ["[[CAPM]]"]
sources: ["[[Wall Street Prep - Equity Risk Premium (ERP) | Formula + Calculator]]", "[[CFI - Equity Risk Premium - Definition, Calculate, Formula]]"]
status: draft
updated: 2026-04-11
---

# Equity risk premium

> **TL;DR.** The equity risk premium is the extra return investors demand for choosing risky stocks over risk-free bonds.

## When you'd use this

You use the equity risk premium (ERP) whenever you are trying to calculate a company's cost of equity, typically using the Capital Asset Pricing Model (CAPM). It is a core assumption in any discounted cash flow (DCF) model and significantly impacts the discount rate, and therefore, the valuation of the business. You might also look at changes in the equity risk premium over time to gauge overall market sentiment and the level of perceived risk in the economy.

## The 30-second version

The equity risk premium (ERP)—sometimes referred to as the market risk premium—is the difference between the expected return on a broad equity market index (like the S&P 500) and the return on a risk-free asset (like a 10-year U.S. Treasury note).

Because investing in the stock market involves uncertainty and the potential loss of capital, rational investors will not buy stocks unless they expect to earn a higher return than they would by holding safe government bonds. The ERP is this required extra compensation. If the extra return is perceived to be too low, investors will move their money to safer assets.

## The full explanation

### The foundation of risk and reward
The fundamental principle of finance is that risk and return are directly correlated. A risk-free asset, like a government security, provides a known return with virtually zero risk of default. Equities, on the other hand, are inherently riskier because their cash flows are uncertain and they sit at the bottom of the capital structure.

The equity risk premium quantifies this relationship. It is the compensation investors demand for bearing the volatility and uncertainty of the stock market. In the long run, historical data consistently demonstrates that investors are indeed rewarded with a premium for taking on equity risk.

### Forward-looking vs. historical ERP
There are two main ways to think about and estimate the equity risk premium:

1.  **Historical approach**: This method looks at past performance. For instance, if the U.S. stock market has historically returned an average of about 9-10% annually over several decades, and risk-free bonds have averaged around 3-4%, the historical equity risk premium would be 5-6%.
2.  **Implied (forward-looking) approach**: This method calculates the ERP based on current market valuations and expected future cash flows. If market valuations are high relative to expected earnings, the implied risk premium is typically lower, and vice versa.

### Impact on cost of equity and CAPM
The equity risk premium is a critical input in the Capital Asset Pricing Model (CAPM). While the ERP represents the extra return required for investing in the *overall market*, CAPM adjusts this premium for the specific risk (Beta) of an *individual stock*.

A higher market-wide ERP directly increases the cost of equity for every company in that market, which in turn raises the Weighted Average Cost of Capital (WACC) and lowers DCF valuations.

### Country Risk Premium (CRP)
When investing in emerging or less developed markets, investors face additional risks such as political instability, high inflation, currency fluctuations, and liquidity constraints. To account for this, analysts often add a Country Risk Premium (CRP) to the baseline equity risk premium when calculating the cost of equity for companies operating in those regions.

## Formula

![[Equity risk premium formula]]

## Worked example

Let's assume an analyst is calculating the equity risk premium to use in a valuation model.

- They observe that the current yield on a 10-year U.S. Treasury note (the risk-free rate) is **2.0%**.
- Based on their research and market forecasts, they expect the S&P 500 to generate an annual return of **8.0%**.

The equity risk premium is simply the difference:
**ERP** = 8.0% - 2.0% = **6.0%**

This 6.0% is the premium an investor expects to earn for taking on the general risk of the stock market instead of holding a safe government bond. If the analyst were valuing a specific stock with a Beta of 1.5, the risk premium for that *specific* stock would be 1.5 × 6.0% = 9.0%.

## Excel and modeling notes

-   **Standard assumptions**: In practice, investment banks and valuation firms often use a standard, firm-wide equity risk premium assumption (typically ranging from 4.5% to 6.0% in mature markets like the U.S.) rather than having each analyst calculate it from scratch for every model.
-   **Consistency is key**: Ensure that the time horizon for the expected market return matches the time horizon for the risk-free rate. If you use a 10-year Treasury yield as the risk-free rate, your expected market return should ideally reflect a 10-year outlook.
-   **Sensitivity analysis**: Because the ERP is an estimate and has a massive impact on valuation, it is highly recommended to include it as a variable in a sensitivity table to see how changes in the market premium affect the implied share price.

## Interview-ready answer

**"What is the equity risk premium and how is it used?"**

"The equity risk premium is the excess return that investors demand for investing in the broader stock market rather than in a risk-free asset, like a 10-year U.S. Treasury note. It compensates investors for the inherent uncertainty and volatility of holding equities.

In corporate finance, it's a primary input in the Capital Asset Pricing Model (CAPM) to calculate a company's cost of equity. You take the risk-free rate and add the equity risk premium multiplied by the company's Beta. Historically in the U.S., the equity risk premium has typically ranged between 4% and 6%."

## Pitfalls and gotchas

-   **Confusing market return with market risk premium**: The expected market return ($E(R_m)$) is the *total* return expected from the market. The equity risk premium is the expected market return *minus* the risk-free rate. Do not use the total market return when the CAPM formula calls for the ERP.
-   **Using a short-term risk-free rate**: It is a mistake to use a 3-month Treasury bill rate when valuing a company's long-term cash flows. Always use a long-term risk-free rate (like the 10-year yield) to calculate the ERP for a DCF.
-   **Ignoring changing market conditions**: The equity risk premium is not a static number. It fluctuates based on macroeconomic volatility, geopolitical risks, and overall investor sentiment. Using an outdated historical average during a period of extreme market distress will result in an inaccurate cost of equity.

## Sources

- [[Wall Street Prep - Equity Risk Premium (ERP) | Formula + Calculator]]
- [[CFI - Equity Risk Premium - Definition, Calculate, Formula]]
