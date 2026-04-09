# Development Feasibility Calculator | Residual Land Value & Dev Yield | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/development-feasibility-calculator

---

Development Feasibility Calculator
==================================

Residual Land Value, Development Yield & Project NPV

Static feasibility screen for CRE ground-up development — no phasing or dynamic cash flows

Embed This Calculator

Development Inputs
------------------

Land Cost ?

$ 

Site acquisition cost

Hard Construction Costs ?

$ 

Direct construction costs (include contingency)

Soft Costs ?

$ 

Design, permits, legal, insurance, developer fee

Construction Period ?

 months

Duration of construction phase

Lease-Up Period ?

 months

Time to stabilized occupancy

Construction Finance Rate ?

 %

Annual rate on construction loan

Construction Loan LTC ?

 %

% of (Hard + Soft) financed

Stabilized NOI ?

$  /yr

Annual NOI at stabilized occupancy

Exit Cap Rate ?

 %

Cap rate for completed property

Developer Profit Target ?

 %

Target margin on cost excl. land (for residual test)

Development Discount Rate ?

 %

OCC for development (typically 15-20%)

Reset to Defaults

### Model Assumptions

*   Construction interest uses 50% draw factor (average outstanding balance, simple interest, no compounding)
*   Loan base = LTC% × (Hard + Soft) only — land typically funded by equity
*   Completed value = Stabilized NOI / Exit Cap Rate (direct capitalization)
*   All costs assumed at t=0 (simplified); completed value discounted from stabilization date
*   No TI, leasing commissions, or lease-up carry modeled separately
*   No phasing, option value, or dynamic construction cash flows

_For educational purposes. Not financial advice. Market conventions simplified._

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Feasibility Results

#### Value & Cost Summary

Completed Property Value \-

Total Hard + Soft Costs \-

Construction Loan Amount \-

Estimated Construction Interest \-

Total Cost (excl. land) \-

Total Cost (incl. land) \-

#### Land Feasibility

Residual Land Value \-

Land Affordable? \-

#### Development Returns

Development Spread (profit on cost) \-

Development Yield (yield on cost) \-

Developer Profit / (Loss) \-

#### Time & NPV

Time to Stabilization \-

PV of Completed Value \-

NPV (simplified — costs at t=0) \-

### Formula Breakdown

NPV = PV(Completed Value) − Total Development Cost

Where Completed Value = Stabilized NOI / Exit Cap Rate

Understanding Real Estate Development Feasibility
-------------------------------------------------

### What is Residual Land Value?

**Residual land value** is the maximum a developer can pay for a site and still achieve their target profit margin. It answers the fundamental development question: _"Given what I can build here and what it will cost, how much can I afford to pay for the land?"_

The calculation works backwards from the completed property value, subtracting all development costs (including the developer's required profit) to arrive at the amount left over for land acquisition. This "back-door" approach is standard in real estate development analysis (Geltner Ch. 28).

Key Formulas

**Completed Value** = Stabilized NOI / Exit Cap Rate  
**Residual Land** = Completed Value − \[Total Cost excl. Land × (1 + Profit Target%)\]  
**Dev Spread** = (Completed Value / Total Cost) − 1  
**Dev Yield** = Stabilized NOI / Total Cost  
**NPV** = PV(Completed Value) − Total Cost

### Development Spread & Yield Explained

**Development spread** (profit on cost) measures total return relative to investment: if the completed property is worth $42M and total costs are $28M, the spread is 50%. Developers typically target 15–25% to compensate for construction and lease-up risk.

**Development yield** (yield on cost) compares stabilized NOI to total cost. If your development yield exceeds market cap rates for comparable stabilized properties, you are effectively "creating" value by building rather than buying. For example, a 9% development yield vs. a 6% market cap implies significant value creation.

**Note:** Some practitioners define "development spread" as development yield minus exit cap rate. This calculator uses the profit-on-cost definition. Both are valid; check which convention your counterparty uses.

### Construction Interest Mechanics

Construction loans are drawn progressively as work is completed — the full balance is never outstanding from day one. This calculator uses a **50% draw factor** to approximate the average outstanding balance, assuming roughly linear draws with simple interest.

In practice, actual interest depends on the specific draw schedule, compounding frequency, and whether the lender charges an interest reserve. For detailed construction budgeting, use a monthly draw schedule rather than this screening approximation.

### NPV for Development Projects

Development NPV discounts the completed property value back to today at a **development discount rate** (typically 15–20%) and subtracts total costs. The discount rate is higher than a stabilized property's cap rate because development involves _operational leverage_: fixed construction costs amplify uncertainty in the final property value (Geltner Ch. 29).

**Simplification:** This calculator assumes all costs occur at t=0 and discounts the completed value from the stabilization date. A true development DCF would discount cost cash flows at the risk-free rate and property values at the stabilized OCC. This static screen is appropriate for initial feasibility — not for final investment committee approval.

### Feasible vs. Not Feasible

#### Feasible Project

Land cost below residual value, positive NPV, development yield exceeds market cap rate, spread above 15–20%. The project creates value and compensates for development risk.

#### Not Feasible

Land cost exceeds residual, negative NPV, thin spread, or yield below market cap rate. The developer is paying too much, building too expensively, or the market cannot support the required rents.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/development-feasibility-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is residual land value and how is it calculated?

Residual land value is the maximum a developer can pay for a site and still achieve their target profit margin. It equals the completed property value minus all development costs (hard costs, soft costs, and construction interest) multiplied by (1 + profit target percentage). If the actual land cost is below the residual, the project exceeds the developer's profit target. Profit-target conventions vary; this calculator uses a target margin on cost excluding land. This back-door approach to feasibility is standard in real estate development analysis (Geltner Ch. 28).

### What is a development spread and what does it tell you?

Development spread in this calculator measures profit on total cost: (Completed Value / Total Cost) - 1. A spread of 20% means the completed property is worth 20% more than total development costs. Developers typically target a minimum 15–25% spread to compensate for development risk. Spreads below 10% are generally considered thin relative to ground-up development risk. Note: some practitioners define "development spread" as the difference between development yield and exit cap rate; this calculator uses the profit-on-cost definition.

### What is development yield and how does it differ from cap rate?

Development yield (also called "yield on cost") equals Stabilized NOI divided by Total Development Cost. It answers: "What cap rate am I effectively creating by building rather than buying?" If your development yield exceeds the market cap rate for comparable stabilized properties, the development creates value. For example, if market cap rates are 6% but your development yield is 8.5%, you're building at a significant discount to market.

### Why is the development discount rate higher than a stabilized property's cap rate?

Development projects have operational leverage: construction costs are largely fixed commitments, while the completed property value is uncertain. This amplifies both upside and downside risk relative to buying an existing stabilized property. Per Geltner Ch. 29, the development phase opportunity cost of capital is typically 15–20%, compared to 8–10% for stabilized properties, because the developer's equity position has 2–3x the systematic risk of the underlying real estate asset.

### Why does this calculator use a 50% draw factor for construction interest?

Construction loans are drawn down progressively as work is completed — the full loan amount is not outstanding from day one. A 50% draw factor (multiplying the full loan by 0.5) approximates the average outstanding balance over the construction period, assuming roughly linear draws with simple interest and no compounding. This is a standard simplification in feasibility screening. Actual interest depends on the specific draw schedule, which varies by project.

### What does a negative NPV mean for a development project?

A negative NPV means the present value of the completed property (discounted at the development discount rate) is less than total development costs at time zero. This suggests the project does not generate sufficient return to compensate for development risk at the assumed discount rate. Note that this calculator uses simplified cash-flow timing (all costs at t=0). A negative NPV may indicate the land price is too high, the discount rate assumption is too aggressive, or that certain value-adds (rezoning, entitlements) haven't been captured in the NOI estimate.

##### Disclaimer

This calculator is for educational purposes only and provides a simplified static feasibility screen. It is not a substitute for a full development pro forma or discounted cash flow analysis. Actual development decisions should consider detailed construction budgets, phased draw schedules, lease-up carry costs, TI/LC allowances, entitlement risk, and local market conditions. Consult a qualified real estate professional or financial advisor for investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing CRE Pro Forma Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### CRE Pro Forma Calculator\
\
Free commercial real estate proforma calculator. Project year-by-year NOI and CapEx cash flows, compute DCF...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/cre-proforma-calculator/)

[![Professional finance illustration representing NPV Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### NPV Calculator\
\
Calculate net present value for investment projects with irregular cash flows. Evaluate capital budgeting decisions...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/npv-calculator/)

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