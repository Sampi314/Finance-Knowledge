# Capital Structure Calculator | WACC, Tax Shield & Leverage | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/capital-structure-calculator

---

Capital Structure & Leverage Calculator
=======================================

WACC, Tax Shield & Modigliani-Miller Analysis

Analyze how debt-equity mix affects firm value and cost of capital

Embed This Calculator

Capital Structure Inputs
------------------------

Equity Value (E) ?

$ 

Market value of equity ($)

Debt Value (D) ?

$ 

Market value of debt ($)

Cost of Equity (re) ?

 %

Required return on equity (%)

Cost of Debt (rd) ?

 %

Pre-tax cost of debt (%)

Tax Rate (T) ?

 %

Corporate marginal tax rate (%)

Unlevered Firm Value (VU) Optional ?

$ 

Leave blank to derive as E + D − T×D

Unlevered Beta (βU) Optional ?

Leave blank to skip levered beta output

Reset to Defaults

##### Key Formulas

VL = VU + T × D

**VL** = Levered firm value | **VU** = Unlevered firm value | **T** = Tax rate | **D** = Debt

* * *

WACC = (E/V) × re + (D/V) × rd × (1 − T)

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Capital Structure Results

Weighted Average Cost of Capital (WACC) 9.0000%

D/E Ratio 0.67

D/V Ratio 40.00%

E/V Ratio 60.00%

Unlevered Cost (ru) 9.6000%

After-Tax Cost of Debt 4.5000%

PV of Tax Shield $100,000,000

VU (derived) $900,000,000

VL (Levered) $1,000,000,000

Observed Firm Value (E + D) $1,000,000,000

Levered Beta (βL) 1.5000

### Formula Breakdown

M&M Proposition I: VL = VU + T × D

Step-by-step calculation with your inputs

### Model Assumptions

*   Market values used for D and E (not book values)
*   M&M Proposition I with corporate taxes: VL = VU + T × D
*   Permanent debt assumption for tax shield (PV of perpetual shields = T×D)
*   No financial distress costs or agency costs modeled
*   Cost of debt is pre-tax; after-tax cost = rd × (1 − T)
*   Hamada equation assumes debt is risk-free (βdebt = 0)
*   Static capital structure — no changes during the period
*   Only debt and common equity — no preferred stock, excess cash, leases, or minority interests
*   Levered beta is shown for educational illustration; it is not fed back into the cost of equity input

_These are companion textbook relationships from Berk Ch. 16, not one internally unified valuation engine. The tax-adjusted WACC and VL = VU + T×D are justified under different financing-policy setups._

_For educational purposes. Not financial advice. Market conventions simplified._

* * *

**When to use this vs. WACC Calculator:** Use this calculator to analyze how debt/equity mix affects firm value and cost of capital via M&M. For standalone WACC estimation with flexible weight inputs, use the [WACC Calculator](https://ryanoconnellfinance.com/calculators/wacc-calculator/)
.

Understanding Capital Structure & Leverage
------------------------------------------

### What is Capital Structure?

**Capital structure** refers to how a firm finances its operations through a mix of debt and equity. The capital structure decision is one of the most important in corporate finance because it directly affects the firm's cost of capital (WACC), risk profile, and total value.

Modigliani-Miller Proposition I (with Taxes)

VL = VU + T × D  
Levered firm value = Unlevered value + PV of tax shields

### The Trade-Off Theory

#### Benefits of Debt

**Interest tax shield**  
Interest payments are tax-deductible, creating value equal to T × D for permanent debt. This reduces the effective cost of debt capital.

#### Costs of Debt

**Financial distress risk**  
Excessive leverage increases bankruptcy probability and agency costs (not modeled in M&M). These costs offset tax benefits at high D/E ratios.

### How Leverage Affects WACC

In the M&M framework with taxes, adding debt reduces WACC because:

*   **Debt is cheaper than equity** (rd < re) due to lower risk and priority in liquidation
*   **Tax deductibility** further reduces the effective cost: after-tax cost = rd × (1 − T)
*   **But cost of equity rises** with leverage as equity holders bear more financial risk (M&M Proposition II)

In the no-tax benchmark, these effects exactly offset and WACC remains constant regardless of leverage.

### Key Relationships

*   **WACC:** (E/V) × re + (D/V) × rd × (1 − T)
*   **Unlevered cost of capital:** ru = (E/V) × re + (D/V) × rd (pre-tax WACC)
*   **M&M Prop II (with taxes):** re = ru + (D/E) × (ru − rd) × (1 − T)
*   **Hamada equation:** βL = βU × \[1 + (1 − T) × (D/E)\]

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/capital-structure-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is capital structure and why does it matter?

Capital structure refers to the mix of debt and equity financing a firm uses to fund its operations and investments. It matters because it affects the firm's weighted average cost of capital (WACC), financial risk, and ultimately firm value. In a world without taxes (Modigliani-Miller Proposition I), capital structure wouldn't affect firm value. However, with corporate taxes, debt creates value through interest tax shields — making the optimal capital structure a key financial decision.

### How does leverage affect a company's WACC?

Leverage has two competing effects on WACC. First, debt is typically cheaper than equity (lower rd than re) due to lower risk and the tax deductibility of interest. Second, higher debt increases the financial risk borne by equity holders, raising the cost of equity. In the no-tax M&M benchmark, leverage does not reduce WACC because the higher cost of equity exactly offsets the cheaper debt. With taxes, the net effect depends on the tax rate — higher taxes amplify debt's benefit via a larger tax shield. At optimal leverage, WACC is minimized; excessive leverage triggers distress costs (not modeled here) that can increase overall cost of capital.

### What is the Modigliani-Miller theorem?

Modigliani-Miller (M&M) Proposition I states that in perfect capital markets without taxes, a firm's value is independent of its capital structure. With corporate taxes, M&M Proposition I becomes VL = VU + T×D — levered firm value equals unlevered value plus the present value of interest tax shields. Proposition II shows how the cost of equity rises linearly with leverage to compensate equity holders for increased financial risk. These propositions form the foundation of modern capital structure theory.

### What is the interest tax shield and how does it create value?

The interest tax shield is the tax savings from deducting interest expense. When a firm borrows D at cost rd, it pays interest of D×rd annually, which reduces taxable income. The annual tax savings equal T×D×rd. The present value of these perpetual savings (assuming permanent debt) is T×D. This represents the additional value that debt financing creates for the firm compared to an all-equity structure.

### How do you calculate levered beta from unlevered beta?

The Hamada equation (which assumes debt beta equals zero) relates levered and unlevered beta: βL = βU × \[1 + (1 − T) × (D/E)\]. Unlevered beta (βU) measures the firm's operating or asset risk — the systematic risk of the business without any debt. Levered beta (βL) captures both operating risk and financial risk from leverage. Higher D/E ratios amplify equity beta, and lower tax rates increase the amplification effect. This relationship is used to estimate a company's cost of equity via CAPM after adjusting for its capital structure.

### What are the limitations of this capital structure model?

This model applies M&M Proposition I with taxes, assuming debt is risk-free and taxes are the only market imperfection. Key limitations: (1) Financial distress costs — bankruptcy and agency costs reduce benefits of high leverage; (2) Debt is not risk-free — credit risk raises the true cost of debt; (3) Tax rates vary by jurisdiction and investor type; (4) The model is static — real firms adjust leverage dynamically; (5) Agency conflicts between debt and equity holders are not captured; (6) The Hamada equation assumes zero debt beta. Only debt and common equity are modeled — no preferred stock, excess cash, leases, or minority interests. For comprehensive analysis, use alongside other valuation and risk tools.

##### Disclaimer

This calculator is for educational purposes only and applies Modigliani-Miller Proposition I with corporate taxes under simplifying assumptions (permanent debt, no distress costs, risk-free debt). Real-world capital structure decisions involve additional factors including financial distress costs, agency costs, information asymmetry, and market conditions. This tool should not be used for investment or financing decisions.

Related Calculators
-------------------

[![Professional finance illustration representing DCF Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### DCF Calculator\
\
Discounted cash flow valuation with terminal value.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/dcf-calculator/)

[![Professional finance illustration representing Free Cash Flow (FCF) Calculator: FCFF & EBITDA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Free Cash Flow (FCF) Calculator: FCFF & EBITDA\
\
Calculate free cash flow to the firm from financial statements.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/fcf-calculator/)

[![Professional finance illustration representing WACC Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### WACC Calculator\
\
Calculate weighted average cost of capital combining equity and debt financing costs. Determine the hurdle...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/wacc-calculator/)

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