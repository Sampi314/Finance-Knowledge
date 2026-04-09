# Bond Convexity Calculator: Duration-Adjusted Price Sensitivity Analysis

**Source:** https://ryanoconnellfinance.com/calculators/bond-convexity-calculator

---

Bond Convexity Calculator
=========================

Duration-Adjusted Price Sensitivity Analysis

Compare duration-only vs. duration-plus-convexity estimates for yield change scenarios

Embed This Calculator

Bond Parameters
---------------

Face Value ?

$ 

Annual Coupon Rate ?

 %

Yield to Maturity (YTM) ?

 %

Years to Maturity ?

 years

Payment Frequency ? Annual Semi-Annual

Yield Change Scenario ?

 bps

+100 bps = yields rise 1%. Quick presets:

[\-200](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [\-100](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [\-50](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [\-25](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [+25](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [+50](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [+100](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)
 [+200](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/#)

Reset to Defaults

##### Convexity Price Estimate

ΔP/P ≈ -Dmod × Δy + ½ × C × (Δy)²

**Dmod** = Modified duration | **C** = Convexity | **Δy** = Yield change

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Convexity Analysis

Convexity (years²) —

Bond Price —

Macaulay Duration —

Modified Duration —

##### Price Change Estimates

Duration-Only ΔP/P —

Dur+Conv ΔP/P —

Convexity Adj. —

##### Exact vs. Estimated Prices

| Method | Estimated Price | Error vs Exact |
| --- | --- | --- |
| **Exact Repricing** | —   | —   |
| Duration-Only | —   | —   |
| Duration + Convexity | —   | —   |

### Formula Breakdown

##### Model Assumptions

*   Fixed coupon bond (not floating rate or inflation-linked)
*   Clean price calculation (excludes accrued interest)
*   Periodic compounding matching payment frequency
*   Flat yield curve (single YTM applies to all cash flows)
*   No embedded options (not callable or putable)

_For educational purposes. Not financial advice. Market conventions simplified._

What is Bond Convexity?
-----------------------

Bond convexity measures the **curvature** of the relationship between bond prices and yields. While duration provides a linear (first-order) approximation of how bond prices change when yields move, convexity captures the non-linear component that becomes increasingly important for larger yield shifts.

Mathematically, convexity is the second derivative of the bond price with respect to yield, scaled by the bond price. It is measured in units of years squared (years²).

C = (1/P) × ∑ CFk × tk × (tk + 1/m) / (1 + y/m)k+2

### Video Explanation

Video: Bond Convexity Explained

### Duration vs. Convexity

##### Duration (First-Order)

*   Linear approximation of price sensitivity
*   Accurate for small yield changes (<50 bps)
*   Always underestimates the true price for option-free bonds
*   ΔP/P ≈ -Dmod × Δy

##### Convexity (Second-Order)

*   Curvature correction to the duration estimate
*   Essential for large yield changes (>50 bps)
*   Always positive for option-free bonds (beneficial)
*   Correction: + ½ × C × (Δy)²

### When Does Convexity Matter?

The convexity adjustment is proportional to (Δy)², so it grows quadratically with yield changes. For a 50 basis point shift, the adjustment is 4 times larger than for a 25 basis point shift. This means:

*   **Small yield changes (<25 bps)**: Duration alone is usually sufficient
*   **Moderate changes (25–100 bps)**: Convexity noticeably improves accuracy
*   **Large changes (>100 bps)**: Convexity is essential; duration alone can produce significant errors

Bonds with higher convexity (longer maturity, lower coupon) benefit more from the convexity correction, and also provide a portfolio advantage: they gain more when yields fall than they lose when yields rise by the same amount.

**Key Insight:** For option-free bonds, positive convexity is always desirable. A bond with higher convexity outperforms a bond with lower convexity (but same duration) in any interest rate environment with large yield movements.

Frequently Asked Questions
--------------------------

### What is bond convexity?

Bond convexity measures the curvature of the relationship between bond prices and yields. It is the second derivative of the bond price with respect to yield, divided by the bond price. Convexity captures the non-linear price sensitivity that duration (a first-order measure) misses, making it essential for accurately estimating price changes when yields move significantly. Convexity is measured in units of years squared.

### What is the difference between duration and convexity?

Duration is a first-order (linear) measure of bond price sensitivity to yield changes, while convexity is a second-order (curvature) correction. Duration alone assumes the price-yield relationship is a straight line, which is only accurate for very small yield changes. Convexity accounts for the fact that this relationship is actually curved, improving price change estimates especially for large yield movements (typically above 50 basis points).

### Why is convexity important for bond portfolios?

Convexity is important because bonds with higher convexity benefit more from interest rate volatility. A bond with positive convexity gains more when yields fall than it loses when yields rise by the same amount. Portfolio managers use convexity to construct portfolios that are better protected against large interest rate movements and to identify bonds that offer superior risk-return profiles.

### How does convexity improve price change estimates?

The duration-only estimate is: ΔP/P = -Dmod × Δy. Adding the convexity adjustment gives: ΔP/P = -Dmod × Δy + ½ × C × (Δy)². The convexity term (always positive for option-free bonds) corrects the duration estimate, reducing the approximation error. For a 100 basis point yield change on a typical 10-year bond, convexity can improve the estimate by 0.1% to 0.5% of the bond price.

### Do all bonds have positive convexity?

No. Standard option-free bonds (fixed coupon, non-callable) always have positive convexity. However, callable bonds can exhibit negative convexity when yields fall near or below the call price, because the issuer is likely to call the bond, capping its price appreciation. Mortgage-backed securities (MBS) also commonly display negative convexity due to prepayment risk. This calculator assumes option-free bonds with positive convexity.

### What is the convexity of a zero-coupon bond?

A zero-coupon bond has the highest convexity among bonds of the same maturity and yield. Its Macaulay duration equals its maturity (since all cash flow occurs at maturity), and its convexity equals T × (T + 1/m) / (1 + y/m)², where T is the maturity in years, m is the compounding frequency, and y is the yield. For example, a 10-year zero-coupon bond with a 5% semi-annual yield has convexity of approximately 99.94 years squared. Set the coupon rate to 0% in the calculator above to explore zero-coupon bond convexity.

##### Disclaimer

This calculator is for educational purposes only and assumes option-free fixed coupon bonds with clean pricing (no accrued interest). Actual bond pricing involves additional factors including accrued interest, day count conventions, credit spreads, and embedded options. The duration and convexity approximations are most accurate for small-to-moderate yield changes. This tool should not be used for trading decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Forward Rates Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Rates Calculator\
\
Calculate forward interest rates from the spot rate curve. Extract implied future rates using the...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-rates-calculator/)

[![Professional finance illustration representing Interest Rate Swap Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Interest Rate Swap Calculator\
\
Price plain vanilla interest rate swaps and calculate fixed swap rates. Determine the present value...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/interest-rate-swap-calculator/)

[![Professional finance illustration representing Bond Duration Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Duration Calculator\
\
Calculate Macaulay duration, modified duration, and estimate bond price sensitivity to interest rate changes. Essential...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-duration-calculator/)

Course by Ryan O'Connell, CFA, FRM

### Fixed Income Investing Course

Master fixed income investing from fundamentals to advanced strategies. Covers bond pricing, duration, convexity, yield curves, and interest rate risk management.

*   Bond pricing, duration & convexity deep dives
*   Yield curve analysis and term structure models
*   Interest rate risk management techniques
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