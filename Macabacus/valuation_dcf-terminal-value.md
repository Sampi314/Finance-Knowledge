# Terminal Value: DCF & Valuation Methods

**Source:** https://macabacus.com/valuation/dcf-terminal-value

---

Mastering Terminal Value Calculation in Discounted Cash Flow (DCF) Analysis
===========================================================================

The terminal value (TV) captures the value of a business beyond the projection period in a [DCF analysis](https://macabacus.com/valuation/dcf-overview)
, and is the present value of all subsequent cash flows. Depending on the circumstance, the terminal value can constitute approximately 75% of the value in a 5-year DCF and 50% of the value in a 10-year DCF. As a result, great attention must be paid to terminal value assumptions. The terminal value may be calculated using two different methods.

![](https://macabacus.com/assets/2025/10/lseg-promotion.png)

Webinar: The AI Edge in Investment Banking
------------------------------------------

**Presented By LSEG & Macabacus:** Learn practical insights about AI’s influence on the future of banking.

Thursday, Oct 30th at 10AM EDT / 2PM GMT.

[View Resource](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Terminal Value Multiple Method
------------------------------

The [terminal multiple method](https://macabacus.com/merger-model/terminal-multiple-method)
 inherently assumes that the business will be valued at the end of the projection period, based on public markets valuations. The terminal value is typically calculated by applying an appropriate multiple ([EV/EBITDA](https://macabacus.com/blog/assess-company-value-ev-ebitda-ratio)
, EV/EBIT, etc.) to the relevant statistic projected for the last projected year.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| TV  | \=  | LTM Terminal Multiple | ×   | Statistic projected for the last 12 months of the projection period |

Since the DCF values cash flow available to all providers of capital, EV multiples are generally used rather than equity value multiples. The exit multiple assumption is usually developed based on selected companies’ trading multiples. In certain cases, precedent transaction multiples may be used, depending on the exit contemplated and specific circumstances. Assuming the terminal multiple is being applied to the statistic projected for the last projection year, be sure to use a _trailing_ multiple rather than a _forward_ multiple.

**Terminal Value in DCF: A Key Component**
------------------------------------------

In DCF analysis, the **terminal value in DCF** reflects a company’s future value beyond the explicit projection period. By validating results between the terminal multiple and perpetuity growth methods, analysts can confirm assumptions and enhance the reliability of their financial model.

### **What is a Terminal Value?**

Terminal value represents the estimated worth of a business beyond the explicit forecast period in a **discounted cash flow (DCF)** analysis. Since projecting financials indefinitely is impractical, terminal value provides a way to capture a company’s long-term value using either the **terminal multiple method** or the **perpetuity growth method**. It typically accounts for a significant portion of a company’s total valuation, making it crucial to validate assumptions carefully. By ensuring that the selected approach aligns with realistic market conditions, terminal value enhances the accuracy of financial models and supports sound investment decisions.

Perpetuity Growth Method
------------------------

The [perpetuity growth method](https://macabacus.com/merger-model/perpetuity-growth-method)
 assumes that the company will continue its historic business and generate FCFs at a steady state forever. The TV under this method can be calculated as follows:

|     |     |     |
| --- | --- | --- |
| TV  | \=  | FCFn × (1+g) |
| WACC − g |

Where:

|     |     |     |
| --- | --- | --- |
| FCFn | \=  | FCF for the last 12 months of the projection period |
| g   | \=  | Perpetuity growth rate (at which FCFs are expected to grow forever) |
| WACC | \=  | Weighted-average cost of capital |

The perpetuity growth rate is typically between the historical inflation rate of 2-3% and the historical GDP growth rate of 4-5%. If you assume a perpetuity growth rate in excess of 5%, you are basically saying that you expect the company’s growth to outpace the economy’s growth forever.

The perpetuity growth method is not used as frequently in practice due to the difficulty in estimating the perpetuity growth rate and determining when the company achieves steady-state. However, the perpetuity growth rate _implied_ using the terminal multiple method should always be calculated to check the validity of the terminal multiple assumption.

**Terminal Value Formula:**
---------------------------

Terminal value is calculated to capture the value of a business beyond the explicit forecast period. There are two primary methods to calculate terminal value:

1.  **The Terminal Multiple Method**: This approach uses an appropriate multiple (e.g., EV/EBITDA) to estimate the terminal value based on market valuations at the end of the projection period. The formula is:

**TV = LTM Terminal Multiple × Statistic for the Last 12 Months**

Where the multiple is typically based on public company trading multiples or precedent transactions,  depending on the exit strategy and market conditions.

2.  **The Perpetuity Growth Method**: This method assumes the business will generate free cash flows (FCF) indefinitely, growing at a stable rate. The formula is:  
    

TV = (FCFn × (1 + g)) / (WACC − g)  

Where FCFn is the final year’s free cash flow, g is the perpetuity growth rate, and WACC is the weighted average cost of capital.  

Both methods estimate the future value of the company beyond the forecast period, contributing significantly to the overall enterprise value in a DCF analysis.  

**What is the formula for the perpetuity growth method?**
---------------------------------------------------------

The perpetuity growth method calculates terminal value by assuming that a company’s free cash flows (FCF) will grow at a constant rate indefinitely. The formula used is:  

This method is valuable when a company is expected to maintain steady operations and growth. While it can be challenging to accurately estimate the perpetuity growth rate, this approach provides a useful perspective for long-term business valuation. It’s important to validate these assumptions to ensure the terminal value is realistic.

**Cross-Checking Terminal Value for Accuracy**
----------------------------------------------

While the TV may be calculated using either one of these methods, it is extremely important to cross-check the resulting valuation using the other method. For this purpose, it is important to calculate the perpetuity growth rate implied by the terminal value calculated using the terminal multiple method, or calculate the terminal multiple implied by the terminal value calculated using the perpetuity growth method.

For example, the perpetuity growth rate implied by a terminal EBITDA-based TV may be calculated by using the formula:

|     |     |     |
| --- | --- | --- |
| Implied g | \=  | TV × WACC − FCFn |
| TV + FCFn |

Likewise, a multiple implied (e.g. [EBITDA](https://macabacus.com/terms/ebitda)
) by the TV calculated using the perpetual growth method can be calculated as follows:

|     |     |     |
| --- | --- | --- |
| Implied terminal EBITDA multiple | \=  | TV  |
| EBITDAn |

**Ensuring Robust Terminal Value Calculations**
-----------------------------------------------

Cross-checking terminal value using both the terminal multiple method and the perpetuity growth method is a best practice that adds reliability to your DCF analysis. This dual validation ensures that your assumptions about growth rates and multiples are aligned with realistic expectations, minimizing the risk of valuation errors. By carefully verifying the implied values from both methods, you can produce a more accurate and defensible valuation, providing greater confidence in your financial model.

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