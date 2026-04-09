# Bond Immunization Calculator | Duration Matching Analysis | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/bond-immunization-calculator

---

Bond Immunization Calculator
============================

Duration Matching Analysis Tool

Check if your bond immunizes a future liability through duration matching and stress-test under yield curve shifts

Embed This Calculator

Enter Values
------------

Liability

Amount ?

$ 

Future payment obligation

Horizon ?

 years

Years until liability is due

Bond

Yield to Maturity ?

 %

Current market yield

Coupon Rate ?

 %

Annual coupon rate of the bond

Maturity ?

 years

Years to bond maturity

Face Value ?

$ 

Par value of the bond

Payment Frequency ? Annual Semi-Annual

Coupon payment frequency

Reset

### Quick Reference

Bond Price

P = Σ C/(1+y)t + F/(1+y)n

Macaulay Duration

D = \[Σ t×C/(1+y)t + n×F/(1+y)n\] / P / freq

Immunization Condition

Macaulay Duration = Investment Horizon

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Immunization Status

\--

Bond Price \--

Macaulay Duration \--

PV of Liability \--

Bonds Required \--

Target Accumulated Value \--

Duration - Horizon \--

### Formula Breakdown

Immunization: Macaulay Duration = Liability Horizon

Step-by-step computation of bond metrics

### Yield Shift Scenarios

| Yield Shift | New Yield | Accumulated Value | Surplus / Deficit |
| --- | --- | --- | --- |

### Immunization Effectiveness

##### Model Assumptions

*   Yield curve is flat (single yield for all maturities)
*   Only parallel yield curve shifts are modeled (not twists or butterfly shifts)
*   Coupons are reinvested at the new yield after the shift
*   No credit risk or default modeled
*   Single-liability immunization only (for multiple liabilities, see textbook Section 4.1.2)

_For educational purposes. Not financial advice. Market conventions simplified._

### Immunization Interpretation

| Status | Condition | Meaning |
| --- | --- | --- |
| Immunized | \|Duration - Horizon\| ≤ 0.1 years | Duration closely matches horizon; portfolio is immunized against parallel shifts |
| Close | \|Duration - Horizon\| ≤ 0.5 years | Duration is near horizon; partial protection exists but rebalancing is recommended |
| Not Immunized | \|Duration - Horizon\| > 0.5 years | Significant duration mismatch; portfolio is exposed to interest rate risk |

Understanding Bond Immunization
-------------------------------

### What is Bond Immunization?

**Bond immunization** is a fixed-income strategy that matches a bond portfolio's Macaulay duration to the investment horizon so that the portfolio's accumulated value at the horizon date is protected against parallel interest rate changes. When rates rise, reinvestment income increases but the bond's market price falls; when rates fall, the opposite occurs. Duration matching ensures these effects offset each other.

Immunization Conditions

**1.** Macaulay Duration = Investment Horizon  
**2.** PV(Portfolio) ≥ PV(Liability)  
**3.** Minimize portfolio dispersion (convexity)  
Classical single-liability immunization (MTMP Ch. 6)

### Price Risk vs. Reinvestment Risk

#### Rates Rise

**Bond price falls** (price risk), but **coupon reinvestment earns more** (reinvestment gain). If duration = horizon, the two effects cancel.

#### Rates Fall

**Bond price rises** (price gain), but **coupon reinvestment earns less** (reinvestment risk). Duration matching offsets these effects.

### When to Use This Calculator vs. Bond Duration Calculator

The [Bond Duration Calculator](https://ryanoconnellfinance.com/calculators/bond-duration-calculator/)
 computes Macaulay and Modified duration for a single bond as standalone metrics. This calculator uses duration as one input to a larger **immunization analysis** — checking whether a bond's duration matches a liability horizon, computing how many bonds are needed, and stress-testing the surplus/deficit under yield curve shifts.

**Key Insight:** Immunization is not a set-and-forget strategy. As time passes and yields change, the bond's duration shifts, requiring periodic rebalancing to maintain the duration match.

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/bond-immunization-calculator-excel/)

Frequently Asked Questions
--------------------------

### What is bond immunization and how does it work?

Bond immunization is a strategy that matches a bond portfolio's Macaulay duration to the investment horizon so that the portfolio value at the horizon date is protected against parallel interest rate changes. When rates rise, reinvestment income increases but bond prices fall; when rates fall, the opposite occurs. Duration matching ensures these effects offset each other, locking in the target return regardless of rate movements.

### What are the conditions required for immunization?

Classical single-liability immunization requires three conditions: (1) the portfolio's Macaulay duration equals the liability horizon, (2) the present value of the portfolio equals or exceeds the present value of the liability, and (3) portfolio dispersion (convexity) is minimized to reduce structural risk from non-parallel yield curve shifts. This calculator checks the first two conditions and stress-tests the portfolio under parallel shifts.

### Why does duration matching protect against interest rate changes?

Duration matching works because it balances two opposing effects of interest rate changes: price risk and reinvestment risk. When a bond's Macaulay duration equals the investment horizon, the gain (or loss) from reinvesting coupons at the new rate exactly offsets the loss (or gain) in the bond's market price at the horizon date. This is why Macaulay duration, not Modified duration, is the relevant measure for immunization.

### What is contingent immunization?

Contingent immunization is a hybrid strategy that allows active management as long as the portfolio value stays above a safety net (the immunized floor). The manager actively trades bonds to try to outperform, but if active management erodes the surplus to zero, the manager switches to a fully immunized strategy to lock in the minimum acceptable return. It combines the upside potential of active management with the downside protection of immunization.

### What are the risks and limitations of immunization?

Key limitations include: immunization only protects against parallel yield curve shifts, not twists or butterfly shifts; it requires periodic rebalancing as duration changes over time; it assumes coupons can be reinvested at the prevailing yield; and it does not account for credit risk or default. Additionally, for large yield changes, the linear duration approximation becomes less accurate, and convexity effects become significant.

### How is immunization different from cash flow matching?

Cash flow matching (dedication) buys bonds whose coupon and principal payments exactly match each liability payment date, eliminating both price and reinvestment risk entirely. Immunization uses duration matching to protect against rate changes but does not require exact cash flow alignment. Cash flow matching is more conservative and eliminates reinvestment risk entirely, but it is typically more expensive and less flexible than immunization.

##### Disclaimer

This calculator is for educational purposes only. It assumes a flat yield curve with parallel shifts and does not model credit risk, liquidity risk, or non-parallel curve movements. Real-world immunization requires periodic rebalancing and consideration of multiple risk factors. This tool should not be used for investment decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Bond Pricing Calculator: Clean Price, Dirty Price, and Accrued Interest](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Pricing Calculator: Clean Price, Dirty Price, and Accrued Interest\
\
Calculate clean price, dirty price, and accrued interest for fixed-rate bonds. Supports annual and semi-annual...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-pricing-calculator/)

[![Professional finance illustration representing Yield to Maturity (YTM) Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Yield to Maturity (YTM) Calculator\
\
Calculate yield to maturity for coupon and zero-coupon bonds using iterative bisection. Analyze bond returns...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/yield-to-maturity-calculator/)

[![Professional finance illustration representing Bond Convexity Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Convexity Calculator\
\
Calculate bond convexity, modified duration, and estimate price changes for interest rate shifts. Analyze the...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Fixed Income Investing: Bond Fundamentals to Portfolio Management

Master fixed income from bond pricing fundamentals to portfolio immunization strategies. Covers yield curves, duration, convexity, credit analysis, and liability-driven investing.

*   Bond pricing, duration, and convexity deep dives
*   Immunization and cash flow matching strategies
*   Credit risk analysis and spread decomposition
*   Hands-on exercises with real bond market data

[View Course](https://ryanoconnellfinance.com/courses/fixed-income-investing/)

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