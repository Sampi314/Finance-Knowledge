# CRE Pro Forma Calculator | DCF, NPV & IRR for Commercial Real Estate | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/cre-proforma-calculator

---

CRE Pro Forma Calculator
========================

DCF Valuation, NPV & IRR

Project year-by-year cash flows for commercial real estate (unlevered, property-level analysis)

Embed This Calculator

Investment Inputs
-----------------

Purchase Price ?

$ 

Total property acquisition price

Year 1 NOI ?

$ 

First-year net operating income

NOI Growth Rate ?

 %/yr

Annual NOI growth assumption

Annual CapEx ?

$ 

First-year recurring capital reserves

CapEx Growth Rate ?

 %/yr

Annual CapEx growth rate

Holding Period ?

 years

Expected investment duration

Exit Cap Rate ?

 %

Cap rate applied to NOI at sale

Selling Costs ?

 %

Transaction costs at sale

Discount Rate ?

 %

Unlevered property-level OCC

Reset to Defaults

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Investment Valuation

Going-In Cap 7.00%

DCF Value $10,249,882

NPV $249,882 Positive

IRR 8.35% Strong

Terminal NOI (Yr n+1) $853,296

Gross Reversion $12,189,944

Net Reversion $11,946,145

PV Operating CFs $4,716,505

PV Reversion $5,533,377

Holding Period 10 years

DCF Property Value $10,249,882

### Year-by-Year Pro Forma

|     |     |     |     |     |
| --- | --- | --- | --- | --- |Year-by-year pre-financing before-tax cash flow projections
| Year | NOI | CapEx | PBTCF | PV of PBTCF |
| --- | --- | --- | --- | --- |

### Formula Breakdown

DCF Value = PV(PBTCF) + PV(Net Reversion)

IRR = rate where −Purchase + Σ\[PBTCFt/(1+IRR)t\] + NetRev/(1+IRR)n = 0

##### Model Assumptions

*   Constant NOI growth rate applied uniformly (no lease-level modeling or tenant rollover)
*   Annual cash flows assumed at year-end (both PBTCF and sale proceeds at end of Year n)
*   Exit cap rate applied to Year n+1 NOI (first year of next owner per Geltner convention)
*   Single discount rate representing unlevered property OCC (no intralease/interlease risk decomposition)
*   CapEx represents normalized recurring capital reserves, growing at its own rate independent of NOI
*   No financing — property-level (unlevered) analysis only; for levered returns see [CRE Returns Calculator](https://ryanoconnellfinance.com/calculators/cre-returns-calculator/)
    
*   No income taxes — pre-tax cash flows
*   No vacancy modeling — Year 1 NOI is assumed net of vacancy; growth rate is net
*   Purchase price represents total acquisition basis (buyer transaction costs not modeled separately)

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding CRE Pro Forma Analysis
------------------------------------

### What is a Pro Forma?

A **real estate pro forma** is a forward-looking financial model that projects a property's income, expenses, and cash flows over a defined holding period. It forms the basis of DCF (discounted cash flow) valuation — the standard method for estimating the investment value of commercial real estate (Geltner Ch. 10-11).

Key Formulas

**PBTCF** = NOI − CapEx  
**DCF Value** = Σ\[PBTCFt / (1+r)t\] + Net Reversion / (1+r)n  
**NPV** = DCF Value − Purchase Price  
**IRR** = Rate where NPV = 0

### DCF Valuation

DCF valuation discounts all projected future cash flows back to the present at the investor's required rate of return (the **opportunity cost of capital**). The property's value has two components: the present value of operating cash flows during the holding period, and the present value of the net sale proceeds (reversion) at the end.

### Going-In vs. Exit Cap Rate

The **going-in cap rate** (Year 1 NOI / Purchase Price) reflects the yield at acquisition. The **exit cap rate** is an assumption about what buyers will pay at disposition — it is applied to the terminal NOI (Year n+1) to estimate the sale price. If exit cap < going-in cap, the model assumes cap rate compression (market appreciation beyond NOI growth). Most conservative underwriting assumes a slightly higher exit cap.

**Key insight (Geltner Ch. 10):** The terminal NOI uses Year n+1 — the first year of the next owner's cash flow — not the current owner's final year. This convention ensures the exit cap rate is applied to a forward-looking income figure, consistent with how market participants price properties.

### Practical Applications

*   **Acquisition Screening:** Compare DCF value to asking price — positive NPV indicates value creation
*   **Sensitivity Analysis:** Vary growth rate, exit cap, and discount rate to stress-test the deal
*   **Hold Period Optimization:** Find the holding period that maximizes IRR
*   **Unlevered vs. Levered:** Start with this unlevered analysis, then layer in financing using the [CRE Returns Calculator](https://ryanoconnellfinance.com/calculators/cre-returns-calculator/)
    

**Limitation:** This calculator uses simplified annual cash flows with constant NOI growth and independently growing CapEx. Professional underwriting models incorporate lease-by-lease analysis, detailed capital expenditure schedules, vacancy modeling, tenant improvements, and tax implications.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/cre-proforma-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a real estate pro forma?

A real estate pro forma is a financial projection that estimates a property's future income, expenses, and cash flows over a specified holding period. It includes year-by-year NOI projections, capital expenditure estimates, and a terminal sale (reversion) to evaluate the property's investment potential using metrics like DCF value, NPV, and IRR.

### How is DCF value calculated for commercial real estate?

DCF (discounted cash flow) value equals the present value of projected operating cash flows (PBTCF) plus the present value of the net sale proceeds (reversion) at the end of the holding period. Each year's cash flow is discounted back to today at the investor's required rate of return. **Formula: DCF Value = Σ\[PBTCFt / (1+r)t\] + Net Reversion / (1+r)n**.

### What is the difference between NPV and IRR in real estate?

NPV (Net Present Value) measures the dollar difference between the DCF value and the purchase price — positive NPV means the property is worth more than you're paying. IRR (Internal Rate of Return) is the discount rate that makes NPV exactly zero — it represents the annualized return the investment is expected to generate. Both should be used together: **NPV measures value creation in dollars, IRR measures return as a percentage**.

### What is the terminal capitalization rate (exit cap rate)?

The exit cap rate is applied to the property's projected NOI in the year after the holding period ends (Year n+1) to estimate the sale price. Per Geltner convention, this uses the next owner's first-year NOI, not the current owner's final-year NOI. The going-in cap rate uses Year 1 NOI / Purchase Price, while the exit cap rate is an assumption about future market conditions at sale. A lower exit cap rate implies a higher expected sale price.

### What is PBTCF (Pre-Financing Before-Tax Cash Flow)?

PBTCF is the property-level cash flow before any debt service payments or income taxes. It equals NOI minus capital expenditures (CapEx). PBTCF represents the cash flow available to the property owner before financing decisions and tax implications — making it the correct measure for unlevered property analysis.

### How does NOI growth rate affect property value?

Higher NOI growth increases both the operating cash flows during the holding period and the terminal NOI used to calculate the reversion (sale price). Since the exit cap rate is applied to Year n+1 NOI, even small differences in growth rate compound significantly over long holding periods. A 2% vs 3% growth rate over 10 years can change the reversion by 10%+ due to compounding.

### Should I discount NOI or PBTCF in a pro forma?

When recurring CapEx is modeled explicitly (as in this calculator), you should discount PBTCF (NOI minus CapEx), not raw NOI. Capital expenditures are real cash outflows that reduce the amount available to the investor. Discounting NOI without deducting CapEx would overstate the property's value. This calculator correctly uses PBTCF as the annual cash flow in both the DCF valuation and IRR calculation.

##### Disclaimer

This calculator is for educational purposes only. It uses simplified assumptions including constant NOI growth and independently growing CapEx. Actual CRE investment decisions should incorporate lease-by-lease analysis, detailed capital expenditure schedules, vacancy modeling, tax implications, and professional due diligence. Consult a qualified real estate professional or financial advisor for investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing DCF Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### DCF Calculator\
\
Calculate discounted cash flow value for any investment with projected future cash flows.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/dcf-calculator/)

[![Professional finance illustration representing NPV Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### NPV Calculator\
\
Calculate net present value for investment projects with irregular cash flows. Evaluate capital budgeting decisions...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/npv-calculator/)

[![Professional finance illustration representing Cap Rate Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Cap Rate Calculator\
\
Calculate the capitalization rate for real estate investments. Analyze property value and expected returns based...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/cap-rate-calculator/)

Contact Me
----------

Have a question or want to work together? Fill out the form below and we’ll get back to you as soon as possible.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20378'%3E%3C/svg%3E)

Contact Form Demo

First Name

Last Name

Email

Subject

Your Message

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy)
 and [Terms of Service](https://policies.google.com/terms)
 apply.

Submit Form