# Annuity & Perpetuity Calculator | PV, FV & Payment Solver | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/annuity-calculator

---

Annuity & Perpetuity Calculator
===============================

PV, FV & Payment Solver

Calculate present value, future value, or solve for payment, rate, and periods

Embed This Calculator

Enter Values
------------

Cash Flow Type ? Ordinary Annuity Annuity Due Perpetuity Growing Perpetuity Growing Annuity

Solve For ? Present Value

Payment Amount (PMT) ?

$ 

Periodic payment amount

Interest Rate (r) ?

 %

Enter as percentage (e.g., 10 for 10%)

Number of Periods (n) ?

 periods

Number of payment periods

Present Value (PV) ?

$ 

Known present value of the cash flow stream

Future Value (FV) ?

$ 

Known future value of the cash flow stream

Growth Rate (g) ?

 %

Per-period payment growth rate

Reset to Defaults

##### Key Formulas

PV = PMT × \[(1 − (1+r)−n) / r\]

Perpetuity: PV = PMT / r

Growing Perpetuity: PV = PMT / (r − g)

Growing Annuity: PV = PMT × \[1−((1+g)/(1+r))n\] / (r−g)

**PMT** = Payment | **r** = Rate | **n** = Periods | **g** = Growth rate

##### Model Assumptions

*   PMT is the level payment amount (first payment at end of period for ordinary, beginning for due)
*   r, g, and n must be on the same period basis (no automatic compounding conversion)
*   Constant discount rate across all periods
*   Payments occur at equal intervals
*   No taxes or transaction fees
*   Growing perpetuity requires g < r for convergence

_For educational purposes. Not financial advice. Market conventions simplified._

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Calculation Results

Present Value (PV) \--

Future Value (FV) \--

Payment (PMT) \--

Interest Rate \--

Number of Periods \--

Total Payments \--

Total Interest \--

### Formula Breakdown

Understanding Annuities & Perpetuities
--------------------------------------

### What Are Annuities and Perpetuities?

An **annuity** is a series of equal payments made at regular intervals for a fixed number of periods. A **perpetuity** is an annuity that continues forever. These are fundamental concepts in finance used to value bonds, mortgages, pensions, and many other financial instruments.

### Types of Cash Flow Streams

#### Ordinary Annuity

**Payments at end of period**  
Bond coupons, mortgage payments, loan repayments. PV = PMT × \[(1−(1+r)−n)/r\]

#### Annuity Due

**Payments at beginning of period**  
Rent, insurance premiums, lease payments. PV is (1+r) times higher than ordinary.

### Perpetuities and Growth

A **perpetuity** pays a constant amount forever: PV = PMT/r. A **growing perpetuity** increases payments at rate g each period: PV = PMT/(r−g). This is the foundation of the Gordon Growth Model used in stock valuation.

**Key Insight:** As the number of periods grows very large, the present value of an annuity approaches the present value of a perpetuity. This is why very long annuities (n > 500) produce values close to PMT/r.

### Practical Applications

*   **Mortgages:** Solve for PMT given the loan amount (PV), rate, and term
*   **Retirement planning:** Calculate PV of future pension payments
*   **Bond valuation:** PV of coupon stream (annuity) plus PV of face value
*   **Stock valuation:** Growing perpetuity (Gordon Growth Model) for dividend stocks
*   **Savings goals:** Solve for PMT needed to reach a future value target

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/annuity-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is the difference between an ordinary annuity and an annuity due?

An ordinary annuity makes payments at the end of each period (e.g., bond coupons), while an annuity due makes payments at the beginning (e.g., rent, insurance premiums). Both the present value and future value of an annuity due are exactly (1+r) times higher than the ordinary annuity equivalent, because each payment is received one period sooner.

### How do you calculate the present value of a perpetuity?

The present value of a perpetuity is PV = C/r, where C is the next-period payment and r is the per-period discount rate. The infinite series of discounted cash flows converges to this expression when r is greater than zero. This assumes C is the payment received one period from now.

### What is a growing perpetuity and when is it used in finance?

A growing perpetuity is a stream of cash flows where the first payment grows at a constant rate g forever. Its present value is PV = C/(r−g), valid only when g is less than r. It is widely used in stock valuation via the Gordon Growth Model, real estate valuation, and estimating terminal values in DCF analysis. Preferred stock dividends are often modeled as perpetuities.

### How does the discount rate affect the present value of an annuity?

A higher discount rate reduces the present value because future cash flows are discounted more heavily. The relationship is non-linear, meaning small rate changes have larger effects on longer annuities. At a zero discount rate, the present value of a level annuity simply equals the sum of all payments (PMT × n).

### What are real-world examples of annuities and perpetuities?

Common annuities include mortgage payments, car loans, pension payouts, bond coupon payments, and lease payments. Perpetuities are modeled by preferred stock dividends, certain endowment structures, and the retired British consol bonds. Growing perpetuities model dividend streams that increase over time.

##### Disclaimer

This calculator is for educational purposes only and assumes constant payments, rates, and intervals. Real-world annuities may involve variable rates, fees, taxes, and other complexities. Results should not be used for financial decisions without professional consultation.

Related Calculators
-------------------

[![Professional finance illustration representing DCF Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### DCF Calculator\
\
Perform discounted cash flow valuation analysis.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/dcf-calculator/)

[![Professional finance illustration representing Gordon Growth Model Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Gordon Growth Model Calculator\
\
Value stocks using the Gordon Growth Model (constant dividend growth). Calculate intrinsic value based on...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/gordon-growth-model-calculator/)

[![Professional finance illustration representing TVM Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### TVM Calculator\
\
Solve any time value of money problem: present value, future value, payment, interest rate, or...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/tvm-calculator/)

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