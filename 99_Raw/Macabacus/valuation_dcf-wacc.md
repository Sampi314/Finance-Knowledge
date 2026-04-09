# Weighted-Average Cost of Capital (WACC)

**Source:** https://macabacus.com/valuation/dcf-wacc

---

Weighted-Average Cost of Capital (WACC)
=======================================

The rate used to discount future unlevered free cash flows (UFCFs) and the [terminal value (TV)](https://macabacus.com/valuation/dcf-terminal-value)
 to their present values should reflect the blended after-tax returns expected by the various providers of capital. The discount rate is a weighted-average of the returns expected by the different classes of capital providers (holders of different types of equity and debt), and must reflect the _long-term targeted_ capital structure as opposed to the current capital structure. While a separate discount rate can be developed for each projection interval to reflect the changing capital structure, the discount rate is usually assumed to remain constant throughout the projection period.

![](https://macabacus.com/assets/2025/10/lseg-promotion.png)

Webinar: The AI Edge in Investment Banking
------------------------------------------

**Presented By LSEG & Macabacus:** Learn practical insights about AI’s influence on the future of banking.

Thursday, Oct 30th at 10AM EDT / 2PM GMT.

[View Resource](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

In situations where projections are judged to be aggressive, it may be appropriate to use a higher discount rate than if the projections are deemed to be more reasonable. While choosing the discount rate is a matter of judgment, it is common practice to use the weighted-average cost of capital (WACC) as a starting point.

Considerations in Calculating WACC
----------------------------------

The following are important considerations when calculating WACC:

*   WACC must comprise a weighted-average of the marginal costs of all sources of capital (debt, equity, etc.) since UFCF represents cash available to all providers of capital.
*   WACC must be computed after corporate taxes, since UFCFs are computed after-tax.
*   WACC must use nominal rates of return built up from real rates and expected inflation, because the expected UFCFs are expressed in nominal terms.
*   WACC must be adjusted for the systematic risk borne by each provider of capital, since each expects a return that compensates for the risk assumed.
*   While calculating the weighted-average of the returns expected by various providers of capital, market value weights for each financing element (equity, debt, etc.) must be used, because market values reflect the true economic claim of each type of financing outstanding whereas book values may not.
*   Long-term WACCs should incorporate assumptions regarding long-term debt rates, not just current debt rates.

Calculation of WACC
-------------------

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WACC | \=  | E   | ×   | re  | +   | D   | ×   | (1 − t) | ×   | rd  | +   | P   | ×   | rp  |
| (E+D+P) | (E+D+P) | (E+D+P) |

Where:

|     |     |     |
| --- | --- | --- |
| E   | \=  | Market value of equity |
| D   | \=  | Market value of debt |
| P   | \=  | Market value of preferred stock |
| re  | \=  | Cost of equity |
| rd  | \=  | Cost of debt |
| rp  | \=  | Cost of preferred stock |
| t   | \=  | Marginal tax rate |

The market values of equity, debt, and preferred should reflect the _targeted_ capital structure, which may be different from the current capital structure. Even though the WACC calculation calls for the market value of debt, the book value of debt may be used as a proxy so long as the company is not in financial distress, in which case the market and book values of debt could differ substantially. Multiplying the debt term in the WACC equation by (1−t) captures the benefit of the tax shield arising from interest expense.

Calculating the Cost of Equity
------------------------------

The cost of equity is usually calculated using the capital asset pricing model (CAPM), which defines the cost of equity as follows:

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| re  | \=  | rf  | +   | β   | ×   | (rm − rf) |

Where:

|     |     |     |
| --- | --- | --- |
| rf  | \=  | Risk-free rate (represented by 10-yr U.S. Treasury bond rate) |
| β   | \=  | Predicted equity beta (levered) |
| (rm − rf) | \=  | Market risk premium |

![Beta Regression](https://macabacus.com/wp-content/uploads/2023/01/beta.png)The market risk premium has historically averaged around 7% and the risk-free rate around 4%.

Beta is a measure of the volatility of a stock’s returns relative to the equity returns of the overall market. It is determined by plotting the stock’s and market’s returns at discrete intervals over a period of time and fitting (regressing) a line through the resulting data points. The slope of that line is the levered equity beta. When the slope of the line is 1.00, the returns of the stock are no more or less volatile than returns on the market. When the slope exceeds 1.00, the stock’s returns are more volatile than the market’s returns.

Predicted Beta
--------------

Equity betas can be obtained from the Barra Book. These betas will be _levered_ and either historical or predicted. The historical beta is based on actual trading data for the period examined (often 2 years), while the predicted beta statistically adjusts the historical beta to reflect an expectation that an individual company’s beta will revert toward the mean over time. For example, if a company’s historical beta is less than 1.00, then the predicted beta will be greater than the historical beta but less than 1.00. Similarly, if the historical beta is greater than 1.00, the predicted beta will be less than the historical beta but greater than 1.00. It is generally advisable to use predicted beta.

Betas of comparable companies are used to estimate re of private companies, or where the shares of the company being valued do not have a long enough trading history to provide a good estimate of the beta.

Predicted beta may be calculated using one of two methods:

(A) Using the company’s beta:

1.  De-lever the beta using the following formula:  
    
    |     |     |     |
    | --- | --- | --- |
    | Unlevered β | \=  | Levered β |
    | 1 + \[(D/E) × (1−t) + P/E\] |
    
    Where:
    
    |     |     |     |
    | --- | --- | --- |
    | E   | \=  | Market value of _existing_ equity |
    | D   | \=  | Market value of _existing_ debt |
    | P   | \=  | Market value of _existing_ preferred stock |
    
2.  Re-lever the unlevered β with the targeted capital structure (typically reflecting an average capital structure for the industry, not the capital structure for the individual company) using the formula:  
    
    |     |     |     |     |     |
    | --- | --- | --- | --- | --- |
    | Levered β | \=  | Unlevered β | ×   | \[1 + \[(D/E) × (1−t) + P/E\]\] |
    
    Where:
    
    |     |     |     |
    | --- | --- | --- |
    | Levered β | \=  | β used in CAPM formula for re |
    | E   | \=  | Market value of _targeted_ equity |
    | D   | \=  | Market value of _targeted_ debt |
    | P   | \=  | Market value of _targeted_ preferred stock |
    

(B) Using betas of comparable companies:

1.  De-lever the comparable companies’ betas using the formula stated above. Use each comparable company’s _existing_ capital structure to de-lever its beta.
2.  Calculate the average unlevered beta of the comparable companies.
3.  Re-lever the average unlevered beta using the formula above. Use the company’s _targeted_ capital structure to re-lever the average unlevered beta.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

Discover more topics
--------------------

[Webinar: The AI Edge in Investment Banking](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Join experts from Macabacus & LSEG to learn practical insights about AI’s influence on the future of banking.

[Read more](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

[DCF Excel Template](https://macabacus.com/excel/templates/discounted-cash-flow)

Elevate your investment analysis with our free DCF model template. Understand discounted cash flow principles and perform accurate valuations in Excel.

[Read more](https://macabacus.com/excel/templates/discounted-cash-flow)

[Operating Model Excel Template](https://macabacus.com/excel/templates/operating-model)

Download our free operating model Excel template. Forecast revenue, expenses, and key financial metrics for better decision-making.

[Read more](https://macabacus.com/excel/templates/operating-model)

[LBO Excel Model](https://macabacus.com/excel/templates/lbo-model-short)

Try LBO modeling with our comprehensive Excel template. Understand key concepts, calculate returns, and gain actionable insights.

[Read more](https://macabacus.com/excel/templates/lbo-model-short)