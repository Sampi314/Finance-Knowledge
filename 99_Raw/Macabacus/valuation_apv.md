# Adjusted Present Value (APV) - Examples, Templates & Formula

**Source:** https://macabacus.com/valuation/apv

---

Adjusted Present Value
======================

The adjusted present value (“APV”) analysis is similar to the DCF analysis, except that the APV does not attempt to capture taxes and other financing effects in a WACC or adjusted discount rate. Recall from our [discussion of DCF](https://macabacus.com/valuation/dcf-wacc)
 that the WACC used in the DCF analysis is calculated as a blend of the cost of debt and the cost of equity, thereby capturing the effects of taxes and financing. APV, on the other hand, seeks to value these effects separately.

APV = base-case NPV + sum of PVs of financing side effects

The APV method is not used as frequently in practice as is the DCF analysis, but more in academic circles. However, the APV is often considered to yield a more accurate valuation.

![](https://macabacus.com/assets/2025/10/lseg-promotion.png)

Webinar: The AI Edge in Investment Banking
------------------------------------------

**Presented By LSEG & Macabacus:** Learn practical insights about AI’s influence on the future of banking.

Thursday, Oct 30th at 10AM EDT / 2PM GMT.

[View Resource](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Interest Tax Shields
--------------------

The most important financing side effect is the interest tax shield (“ITS”). When a company has debt, the interest it pays on that debt that is tax-deductible, creating interest tax shields that have value. In the DCF analysis, the ITS are baked in by including the tax-effected cost of debt in the WACC used to discount free cash flows (“FCF”). For APV purposes, the ITS in a given year is calculated as:

ITS = Interest Expense × Tax Rate

If the projected taxes to be paid exceed the ITS generated in a given year, the entire ITS is consumed in that year and no ITS carryforward is accumulated. However, if the company has more ITS in a given year than taxes paid:

*   The excess ITS can be carried back up to 3 years to offset taxable income in those years.
*   If you cannot exhaust the ITS on current or past taxes, you must carry the unused ITS forward for up to 15 years to offset future taxes, and can begin using the unused portion once you reach a year in which the all-equity tax bill exceeds the new ITS generated.

Therefore, the actual ITS used in a given year equals the minimum of the calculated ITS and the projected taxes before the ITS is applied.

ITS Used = min(ITS, Taxes)

When calculating APV, the present values of the interest tax shields actually used in each projected year, along with the present value of the [terminal value](https://macabacus.com/valuation/dcf-terminal-value)
 (“TV”) of the ITS, are added to the present values of future free cash flows. The discount rate used in calculating present values is the same as that used in discounting free cash flows (the CAPM rate), since the ITS only have value if there is sufficient taxable income to use them. The terminal value of the ITS is calculated as:

TV ITS = t × DebtN × Re × (1 + g) / (Re − g)2

where t = tax rate, DebtN = terminal year debt balance, Re = required return on equity, and g = terminal growth rate.

### Exhibit A – Interest Tax Shields

The following example shows how the APV analysis values interest tax shields. Note that the rate used to discount the free cash flows and ITS is the CAPM rate, rather than the WACC used in a DCF analysis.

Download Template
-----------------

[Interest Tax Shields](https://macabacus.com/assets/2023/02/apv1.xls)

**[Try Macabacus for free](https://macabacus.com/start-trial)
** to accelerate financial modeling in Excel.

Exhibit B – Tax-Loss Carryforwards
----------------------------------

When a company has negative taxable income, a tax-loss carryforward (“TLC”) is generated. The TLC may then be used to reduce taxable income in subsequent years.

### Exhibit B – Tax-Loss Carryforward

The following example shows how the APV analysis values tax-loss carryforwards. Note that the TLC only has value when it can actually be used. The present value of the TLC would be added to the PV of free cash flows, along with any other items like ITS, to yield the APV.

Download Template
-----------------

[Tax-Loss Carryforwards](https://macabacus.com/assets/2023/02/apv2.xls)

**[Try Macabacus for free](https://macabacus.com/start-trial)
** to accelerate financial modeling in Excel.

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