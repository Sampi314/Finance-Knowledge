# LBO Sensitivity Analysis Calculator: Entry & Exit Multiple IRR/MOIC Grid | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/entry-exit-multiple-calculator

---

LBO Sensitivity Analysis Calculator
===================================

Entry & Exit Multiple IRR/MOIC Grid

Visualize how LBO returns change across 25 entry/exit multiple scenarios

Embed This Calculator

LBO Parameters
--------------

Entry EBITDA ?

$  M

LTM EBITDA at acquisition ($M)

Base EV/EBITDA Multiple ?

 x

Grid shows \[Center-2x\] to \[Center+2x\]

Leverage (% of EV) ?

 %

Typical PE range: 50-70%

EBITDA CAGR ?

 %

Annual EBITDA growth rate

Hold Period ?

 years

Typical PE range: 3-7 years

Reset to Defaults

##### LBO Returns Formula

IRR = MOIC(1/n) - 1

**MOIC** = Exit Equity / Equity Invested  
**Exit Equity** = Exit EV - Debt at Exit  
**Debt at Exit** = Entry Debt x 0.80n

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Sensitivity Grid

Show MOIC

Lower entry = better

Higher exit = better

| Entry Exit | 7.0x | 8.0x | 9.0x | 10.0x | 11.0x |
| --- | --- | --- | --- | --- | --- |

Legend (IRR):

≥20%

15-20%

<15%

Diagonal (no expansion)

### Cell Details

Hover over a cell to see detailed breakdown

Entry Multiple \--

Exit Multiple \--

* * *

Entry EV \--

Entry Debt \--

Equity Invested \--

* * *

Exit EBITDA \--

Exit EV \--

Debt at Exit \--

* * *

Exit Equity \--

MOIC \--

IRR \--

### Model Assumptions

*   Debt paydown: ~20% annual reduction (Debt x 0.80n)
*   No taxes modeled (pre-tax returns)
*   EBITDA CAGR applies uniformly across hold period
*   Single terminal cash flow (no interim distributions)
*   Multiple range: +/-2x around center in 1.0x steps

Understanding LBO Sensitivity Analysis
--------------------------------------

### What is LBO Sensitivity Analysis?

**LBO sensitivity analysis** examines how leveraged buyout returns vary across different entry and exit multiple assumptions. Since entry price and exit valuation are two of the biggest drivers of PE returns, this analysis helps investors understand their deal's risk/reward profile.

Core LBO Return Drivers

**1\. Multiple Expansion:** Exit Multiple > Entry Multiple  
**2\. EBITDA Growth:** Exit EBITDA > Entry EBITDA  
**3\. Debt Paydown:** Equity grows as debt is repaid

### How to Use This Calculator

The 5x5 grid shows IRR (or MOIC) for 25 different entry/exit multiple combinations:

*   **Rows:** Entry multiples from \[Center-2x\] to \[Center+2x\]
*   **Columns:** Exit multiples from \[Center-2x\] to \[Center+2x\]
*   **Diagonal:** No multiple expansion (entry = exit)
*   **Above diagonal:** Multiple expansion (exit > entry)
*   **Below diagonal:** Multiple compression (exit < entry)

**Pro Tip:** PE firms typically target 20%+ IRR. Use the green/yellow/red color coding to quickly identify viable scenarios.

### Entry Price Discipline

Notice how returns improve dramatically as you move up the rows (lower entry multiples). This illustrates why entry price discipline is critical in private equity:

*   A 1x lower entry multiple can add 5-10% to IRR
*   High entry multiples require aggressive exit assumptions to hit targets
*   The diagonal shows what returns look like without relying on multiple expansion

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/entry-exit-multiple-calculator-excel/)

Frequently Asked Questions
--------------------------

### What does the diagonal represent in the sensitivity table?

The diagonal shows scenarios where entry multiple equals exit multiple, meaning no multiple expansion or compression. This is the baseline case showing returns driven purely by EBITDA growth and debt paydown. It's a useful benchmark for understanding how much of your return depends on multiple expansion versus operational improvement.

### How do I read this LBO sensitivity table?

Rows represent entry multiples (what you pay), columns represent exit multiples (what you sell for). Each cell shows the IRR or MOIC for that combination. Green cells indicate attractive returns (≥20% IRR), yellow is moderate (15-20%), red is below target (<15%). The best outcomes are in the top-right (low entry, high exit) and worst in bottom-left (high entry, low exit).

### Why do LBO returns improve with lower entry multiples?

Lower entry multiples mean you pay less for the same EBITDA, requiring less equity investment. Holding the exit multiple constant, less invested equity produces higher MOIC and IRR. This is why PE firms focus heavily on entry price discipline. A company bought at 7x EBITDA will generate significantly better returns than the same company bought at 10x, all else equal.

### What is the 20% annual debt paydown assumption?

This simplified model assumes the remaining debt balance decreases by 20% each year (Debt x 0.80n). Real LBOs use detailed amortization schedules based on mandatory principal payments and cash sweeps. This approximation captures the key driver: debt paydown increases equity value at exit by reducing the claim against enterprise value.

### When would I see negative or underwater returns?

When Exit Equity is less than Equity Invested (MOIC < 1.0x), you have a loss. This happens with high entry multiples, low exit multiples, high leverage, and/or negative EBITDA growth. Extreme cases show "Underwater" when Exit Equity is negative (debt exceeds exit enterprise value). These scenarios highlight the downside risk of aggressive LBO structures.

### How does this differ from the LBO Returns Calculator?

The LBO Returns Calculator computes a single scenario with specific entry and exit multiples. This Sensitivity Calculator shows 25 scenarios at once, helping you understand how returns change across a range of assumptions. This view is essential for deal negotiation (knowing your walk-away price), risk assessment (seeing downside scenarios), and investment committee presentations.

### Why are all diagonal cells the same?

Because leverage is defined as a percentage of EV (not a fixed dollar amount), and debt paydown is proportional to initial debt, the ratio relationships are preserved. On the diagonal (entry = exit multiple), the MOIC and IRR depend only on EBITDA growth and debt paydown, not on the absolute multiple level. This mathematical property makes the diagonal a clean benchmark for operational value creation.

##### Disclaimer

This calculator is for educational purposes only. Real LBO analysis involves detailed cash flow projections, working capital adjustments, tax effects, management incentives, and complex debt structures. This simplified model uses a ~20% annual debt paydown approximation. Results should not be used for investment decisions without proper due diligence.

Related Calculators
-------------------

[![LBO returns calculator showing IRR and MOIC based on entry, exit, and holding period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### LBO Returns Calculator (IRR & MOIC)\
\
Calculate leveraged buyout returns including IRR and MOIC. Analyze how leverage, EBITDA growth, and exit...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/lbo-returns-calculator/)

[![Private equity return metrics DPI TVPI RVPI diagram](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Private Equity Returns Calculator (DPI/TVPI/RVPI)\
\
Calculate PE fund multiples: DPI, RVPI, and TVPI.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/private-equity-returns-calculator/)

[![Professional finance illustration representing IRR Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### IRR Calculator\
\
Calculate the internal rate of return for investment projects. Find the discount rate that makes...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/irr-calculator/)

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