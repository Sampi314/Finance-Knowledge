# Enterprise and Equity Values - Examples, Templates

**Source:** https://macabacus.com/valuation/dcf-enterprise-equity-values

---

Enterprise and Equity Values
============================

Calculating Enterprise Value
----------------------------

The enterprise value (EV) of the business is calculated by discounting the unlevered free cash flows (UFCFs) projected over the projection period and the [terminal value](https://macabacus.com/valuation/dcf-terminal-value)
 calculated at the end of the projection period to their present values using the chosen discount rate (WACC).

![](https://macabacus.com/assets/2025/10/lseg-promotion.png)

Webinar: The AI Edge in Investment Banking
------------------------------------------

**Presented By LSEG & Macabacus:** Learn practical insights about AI’s influence on the future of banking.

Thursday, Oct 30th at 10AM EDT / 2PM GMT.

[View Resource](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV  | \=  | FCF1 | +   | FCF2 | +   | …   | +   | FCFn | +   | TV  |
| (1+r)1 | (1+r)2 | (1+r)n | (1+r)n |

In Excel, EV = NPV(r, array of FCFs for years 1 through n) + TV/(1+r)n.

Where:

|     |     |     |
| --- | --- | --- |
| FCFn | \=  | Unlevered FCF occurring at the end of interval n |
| TV  | \=  | Terminal Value |
| r   | \=  | Weighted-average cost of capital (WACC) |

Always calculate the EV for a range of terminal multiples and perpetuity growth rates to illustrate the sensitivity of the [DCF analysis](https://macabacus.com/excel/templates/discounted-cash-flow)
 to these critical inputs.

Mid-Year vs. End-Period Convention
----------------------------------

The calculation of EV is affected by the assumptions regarding the timing of the cash flows within a projection interval. The mid-period convention assumes that the UFCFs occur at the middle of each projection interval, while the end-period convention assumes all UFCFs occur at the end of each interval. In practice, the end-period convention is often used because it is more conservative (the UFCFs are discounted at a time more distant from the present).

The EV formula above assumes an end-period convention. EV based on the mid-year convention is calculated using the following formula:

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV  | \=  | FCF1 | +   | FCF2 | +   | …   | +   | FCFn | +   | TV  |
| (1+r)0.5 | (1+r)1.5 | (1+r)n−0.5 | (1+r)n |

Where:

|     |     |     |
| --- | --- | --- |
| FCFn | \=  | Unlevered FCF occurring in the middle of interval n |

Alternatively, to arrive at the present value of the UFCFs using the mid-period convention, the present value of UFCFs based on the end-period convention must be moved forward by half a year in time by multiplying it by (1+r)0.5 as follows:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| EV (mid-period  <br>convention) | \=  | PV of UFCFs (end-period convention) × (1+r)0.5 | +   | TV  |
| (1+r)n |

Note that the NPV function in Excel uses an end-period convention.

Calculating Equity Value
------------------------

Equity value is calculated by simply subtracting net debt from the computed EV. While considering which balance sheet items should be included in the calculation of net debt, one must consider whether or not the income/expenses associated with a particular asset/liability were included in the calculation of EBIT to arrive at UFCF. Generally, if the expense associated with a liability is included in the calculation of EBIT, the liability should not be included in net debt. Likewise, if the income attributable to an asset has been included in the calculation of EBIT, the asset should not be included in the calculation of net debt.

Net debt is not dependent on the assumptions used in the DCF valuation, so you can subtract the constant net debt value from the range of EVs calculated as described above to arrive at a range of equity values. As an additional step, divide the equity value by the current diluted shares outstanding to arrive at a theoretical range of share prices based on the DCF valuation.

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