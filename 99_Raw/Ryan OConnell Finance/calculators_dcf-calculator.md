# DCF Calculator | Free Discounted Cash Flow Valuation Tool | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/dcf-calculator

---

DCF Valuation Calculator
========================

Discounted Cash Flow Analysis Tool

Project free cash flows, calculate terminal value, and estimate implied share price

Embed This Calculator

DCF Parameters
--------------

Number of Projection Years ? 1 year 2 years 3 years 4 years 5 years 6 years 7 years 8 years 9 years 10 years 11 years 12 years 13 years 14 years 15 years 16 years 17 years 18 years 19 years 20 years

Typical range: 5-10 years

Projected Free Cash Flows (FCFF) ?

Values in $ millions

Discount Rate (WACC) ?

 %

Weighted average cost of capital

Terminal Growth Rate ?

 %

Should not exceed long-term GDP growth (~2-3%)

Total Debt ?

$  M

Total interest-bearing debt ($ millions)

Cash & Equivalents ?

$  M

Cash and short-term investments ($ millions)

Shares Outstanding ?

 M

Diluted shares outstanding (millions)

Reset to Defaults

##### DCF Valuation Formula

EV = Σ FCFFt / (1+WACC)t + TV / (1+WACC)n

**EV** = Enterprise Value | **FCFF** = Free Cash Flow to Firm | **WACC** = Discount Rate | **TV** = Terminal Value | **n** = Projection Years

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Valuation Results

PV of Projected FCFs \--

Terminal Value \--

PV of Terminal Value \--

Enterprise Value \--

Equity Value \--

Implied Share Price \--

TV as % of EV \--

### Step-by-Step Calculation

EV = Σ FCFFt / (1+WACC)t + TV / (1+WACC)n

Discounted Cash Flow Valuation (Berk Chapter 10)

##### Model Assumptions

*   Cash flows represent Free Cash Flow to the Firm (FCFF), discounted at WACC
*   Terminal value uses the Gordon Growth Model (perpetuity with constant growth)
*   WACC is constant across all projection years
*   Free cash flows occur at end of each year (no mid-year convention)
*   Terminal growth rate should not exceed long-term GDP growth (~2-3%)
*   Equity bridge is simplified — excludes preferred stock, minority interest, leases, and other non-operating assets
*   All inputs (cash flows, WACC, terminal growth) must be on the same nominal/real basis
*   Debt and cash values are at book value

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding Discounted Cash Flow (DCF) Valuation
--------------------------------------------------

### What Is a DCF Analysis?

A discounted cash flow (DCF) analysis is a fundamental valuation method that estimates the intrinsic value of a company based on its expected future free cash flows to the firm (FCFF). By discounting these cash flows at the weighted average cost of capital (WACC), the model determines what those future cash flows are worth in today's dollars. This approach, detailed in Berk Chapter 10, is the cornerstone of corporate valuation in investment banking and equity research.

### The Equity Bridge: From Enterprise Value to Share Price

Enterprise value (EV) represents the total value of a company's operations. To determine what equity holders actually own, we apply the equity bridge: **Equity Value = EV - Total Debt + Cash**. This simplified bridge removes the claims of debt holders and adds back liquid assets. Dividing equity value by diluted shares outstanding gives the implied share price. Note that a full banking-style bridge would also adjust for preferred stock, minority interests, and other items.

### Terminal Value and the Gordon Growth Model

Since we cannot project cash flows indefinitely, the terminal value captures all value beyond the projection period. Using the Gordon Growth Model: **TV = FCFFn × (1 + g) / (WACC - g)**. The terminal growth rate (g) should reflect sustainable long-term growth, typically matching GDP growth of 2-3%. Terminal value often represents 60-80% of total enterprise value, making the growth rate and WACC assumptions critical to the final valuation.

### FCFF vs. FCFE: Choosing the Right Cash Flow

This calculator uses Free Cash Flow to the Firm (FCFF), which represents cash available to all capital providers (debt and equity holders). FCFF is discounted at WACC to determine enterprise value. The alternative approach uses Free Cash Flow to Equity (FCFE), discounted at the cost of equity to arrive at equity value directly. The FCFF/WACC approach is most common in practice because it separates operating performance from capital structure decisions.

### Understanding WACC (Weighted Average Cost of Capital)

The weighted average cost of capital (WACC) is the discount rate used in DCF analysis to convert future cash flows to present value. It represents the blended return required by all capital providers - both debt and equity holders - weighted by their proportion of the company's capital structure.

#### Video: Weighted Average Cost of Capital (WACC) Explained

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/dcf-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a discounted cash flow (DCF) analysis and how does it work?

A DCF analysis estimates the intrinsic value of a company by projecting its future free cash flows to the firm (FCFF) and discounting them back to present value using the weighted average cost of capital (WACC). The model adds a terminal value to capture cash flows beyond the projection period, then subtracts debt and adds cash to arrive at equity value. Dividing by shares outstanding gives the implied share price. DCF is widely used in investment banking, equity research, and corporate finance because it values a company based on its fundamental cash-generating ability rather than market sentiment.

### How do you calculate terminal value in a DCF model?

Terminal value captures the value of all free cash flows to the firm (FCFF) beyond the explicit projection period. The most common approach is the Gordon Growth Model: **TV = FCFFn × (1 + g) / (WACC - g)**, where FCFFn is the final projected free cash flow, g is the perpetual growth rate, and WACC is the discount rate. The terminal growth rate should not exceed long-term GDP growth (typically 2-3%) because no company can grow faster than the economy indefinitely. An alternative method uses exit multiples (e.g., EV/EBITDA), but this calculator uses the Gordon Growth approach per Berk Chapter 10.

### Why is the terminal value often the largest component of enterprise value?

Terminal value frequently represents 60-80% of total enterprise value because it captures an infinite stream of cash flows beyond the projection period. A short projection period (e.g., 5 years) means most of the company's value lies in the terminal value. This is why DCF results are highly sensitive to the terminal growth rate and discount rate assumptions. Analysts can reduce terminal value dominance by extending the projection period (e.g., 10-15 years) or using more conservative growth assumptions. When TV exceeds 80% of EV, results should be interpreted with extra caution.

### What discount rate should I use in a DCF analysis?

The appropriate discount rate for a firm-value DCF model is the weighted average cost of capital (WACC), which blends the cost of equity and the after-tax cost of debt weighted by the company's capital structure. WACC typically ranges from 6-12% for established companies and can exceed 15% for high-risk ventures. The cost of equity is commonly estimated using CAPM: **Ke = Rf + β × (Rm - Rf)**. A higher WACC reduces the present value of future cash flows, resulting in a lower valuation. Use our [WACC Calculator](https://ryanoconnellfinance.com/calculators/wacc-calculator/)
 for a detailed WACC computation.

### How do you convert enterprise value to equity value per share?

Enterprise value (EV) represents the total value of a company's operations. To convert to equity value: **Equity Value = EV - Total Debt + Cash & Equivalents**. This simplified equity bridge removes the claims of debt holders and adds back liquid assets available to equity holders. It excludes items like preferred stock, minority interest, and other non-operating assets by design. Dividing equity value by diluted shares outstanding gives the implied share price. If the implied price exceeds the current market price, the stock may be undervalued; if below, it may be overvalued.

### What is the difference between FCFF and FCFE in a DCF model?

Free Cash Flow to the Firm (FCFF) represents cash available to all capital providers (debt and equity holders) and is discounted at WACC to determine enterprise value. Free Cash Flow to Equity (FCFE) represents cash available only to equity holders (after debt payments) and is discounted at the cost of equity to determine equity value directly. This calculator uses the FCFF/WACC approach, which is the most common in practice because it separates operating performance from capital structure decisions. Use our [FCF Calculator](https://ryanoconnellfinance.com/calculators/fcf-calculator/)
 to compute FCFF from income statement items.

##### Disclaimer

This calculator is for educational purposes only and uses a simplified DCF model based on Berk Chapter 10. Actual valuations require detailed financial modeling, sensitivity analysis, and professional judgment. The equity bridge excludes preferred stock, minority interest, and other non-operating items. This tool should not be used for investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing NPV Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### NPV Calculator\
\
Calculate net present value for investment projects with irregular cash flows. Evaluate capital budgeting decisions...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/npv-calculator/)

[![Professional finance illustration representing WACC Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### WACC Calculator\
\
Calculate weighted average cost of capital combining equity and debt financing costs. Determine the hurdle...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/wacc-calculator/)

[![Professional finance illustration representing Gordon Growth Model Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Gordon Growth Model Calculator\
\
Value stocks using the Gordon Growth Model (constant dividend growth). Calculate intrinsic value based on...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/gordon-growth-model-calculator/)

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