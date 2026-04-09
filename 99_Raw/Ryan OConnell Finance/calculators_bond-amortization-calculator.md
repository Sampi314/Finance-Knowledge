# Bond Amortization Schedule Calculator: Effective Interest Method & Carrying Value | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/bond-amortization-calculator

---

Bond Amortization Schedule Calculator
=====================================

Effective Interest Method for Issuers

Generate a complete amortization schedule with carrying value, interest expense, and period-by-period amortization

Embed This Calculator

Bond Parameters
---------------

Face Value ?

$ 

Par value repaid at maturity

Annual Coupon Rate ?

 %

Enter as percentage (e.g., 6 for 6%)

Annual Market Rate ?

 %

Market yield at issuance

Term to Maturity ?

 years

Bond maturity in years

Payment Frequency ? Annual (1/year) Semi-Annual (2/year) Quarterly (4/year) Monthly (12/year)

Coupon payment frequency

Reset to Defaults

##### Effective Interest Method

Interest Expense = CV × r

**CV** = Carrying Value | **r** = Market Rate per Period

* * *

Amortization = |Interest Exp − Cash Payment|

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Bond Summary

Issue Price $864,097 Issued at Discount

Premium / Discount \-$135,903

Total Coupon Payments $600,000

Total Interest Expense $735,903

Principal at Maturity $1,000,000

Total Cash Outflow $1,600,000

Number of Periods 20

### Amortization Schedule

| Period | Beginning CV | Interest Expense | Cash Payment | Amortization | Ending CV |
| --- | --- | --- | --- | --- | --- |

### Carrying Value Over Time

### Interest Expense vs Cash Payment

### Formula Breakdown

Issue Price = PV(Coupons) + PV(Face Value)

### Model Assumptions

*   Uses the **effective interest method** (required by U.S. GAAP; IFRS also requires it).
*   Straight-line amortization is not shown; it is only permitted when the difference from the effective interest method is not material.
*   Bonds are assumed to be **issued on a coupon date** (no accrued interest calculation).
*   Final period adjusted for rounding to ensure carrying value equals face value at maturity.
*   No transaction costs, underwriting fees, or bond issuance costs included.
*   For educational purposes. Not financial advice. Market conventions simplified.

Understanding Bond Amortization
-------------------------------

### What is Bond Amortization?

When a company issues bonds, the bonds may sell at a **premium** (above face value) or a **discount** (below face value) depending on the relationship between the stated coupon rate and the prevailing market interest rate. The difference between the issue price and face value must be amortized over the bond's life using the **effective interest method**.

Key Relationships

**Discount:** Coupon Rate < Market Rate → Issue Price < Face Value  
**Premium:** Coupon Rate > Market Rate → Issue Price > Face Value  
**Par:** Coupon Rate = Market Rate → Issue Price = Face Value

### The Effective Interest Method

#### Interest Expense

**Carrying Value × Market Rate per Period**  
Changes each period as the carrying value adjusts. Represents the true economic cost of borrowing.

#### Cash Payment

**Face Value × Coupon Rate per Period**  
Constant each period. The actual cash paid to bondholders based on the stated coupon rate.

### How Carrying Value Converges

The difference between interest expense and cash payment is the **amortization** for each period. For discount bonds, interest expense exceeds cash payment, so carrying value _increases_ each period. For premium bonds, cash payment exceeds interest expense, so carrying value _decreases_ each period. By maturity, carrying value equals face value exactly.

**Accounting Standard:** U.S. GAAP (ASC 835-30) and IFRS (IFRS 9) require the effective interest method. The straight-line method is only acceptable under U.S. GAAP when results are not materially different.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/bond-amortization-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is a bond amortization schedule?

A bond amortization schedule is a table that shows how a bond's carrying value (book value) changes over its life from the issue price to the face value at maturity. Each row shows the interest expense, cash payment, and amortization for one period. The schedule is used by bond issuers to record journal entries under the effective interest method required by GAAP.

### What is the effective interest method?

The effective interest method calculates interest expense each period as the bond's carrying value multiplied by the market interest rate at issuance. This produces a constant percentage return on the carrying value, unlike the straight-line method which allocates equal amortization each period. U.S. GAAP and IFRS require the effective interest method; straight-line amortization is only permitted when the difference is not material.

### What is the difference between bonds issued at a premium and at a discount?

A bond is issued at a **discount** when the coupon rate is lower than the market rate — investors pay less than face value because the stated interest is below market. A bond is issued at a **premium** when the coupon rate exceeds the market rate — investors pay more than face value because the stated interest is above market. At maturity, both converge to face value through the amortization process.

### How does carrying value change over time?

For a discount bond, the carrying value starts below face value and increases each period as amortization is added. For a premium bond, the carrying value starts above face value and decreases each period as amortization is subtracted. In both cases, the carrying value converges to the face value by the maturity date.

### Why does the final period have a rounding adjustment?

When calculating each period's interest expense and amortization using floating-point arithmetic, small rounding differences accumulate over the life of the bond. To ensure the carrying value equals the face value exactly at maturity (as required by accounting standards), the final period's amortization is adjusted to absorb any cumulative rounding difference. This is standard accounting practice.

### How is this calculator different from a bond pricing calculator or YTM calculator?

This calculator focuses on the **issuer's accounting perspective** — generating the amortization schedule that shows how carrying value, interest expense, and amortization change each period over the bond's life. A bond pricing calculator computes the market value of a bond from an **investor's perspective** using current market yields. A YTM calculator solves for the yield to maturity given a bond's current price. For investor-side calculations, see our [Bond Pricing Calculator](https://ryanoconnellfinance.com/calculators/bond-pricing-calculator/)
 and [YTM Calculator](https://ryanoconnellfinance.com/calculators/yield-to-maturity-calculator/)
.

##### Disclaimer

This calculator is for educational purposes only and uses the effective interest method per U.S. GAAP. Actual bond accounting may involve additional complexities such as bond issuance costs, accrued interest for between-date issuances, and impairment considerations. Consult a qualified accountant for specific accounting decisions. This tool should not be used as the sole basis for financial reporting.

Related Calculators
-------------------

[![Professional finance illustration representing Inventory Valuation Calculator: FIFO, LIFO & Weighted Average Cost Comparison](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Inventory Valuation Calculator: FIFO, LIFO & Weighted Average Cost Comparison\
\
Compare FIFO, LIFO, and weighted average inventory methods.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/inventory-valuation-calculator/)

[![Professional finance illustration representing Depreciation Calculator: Straight-Line, DDB, SYD & Units of Production](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Depreciation Calculator: Straight-Line, DDB, SYD & Units of Production\
\
Calculate depreciation using straight-line, declining balance, and more.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/depreciation-calculator/)

[![Professional finance illustration representing Bad Debt Expense & Allowance Calculator: Aging Schedule Method](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bad Debt Expense & Allowance Calculator: Aging Schedule Method\
\
Estimate bad debt expense using allowance and direct write-off methods.\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bad-debt-expense-calculator/)

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