# Bond Pricing Calculator: Clean Price, Dirty Price & Accrued Interest | Ryan O'Connell, CFA

**Source:** https://ryanoconnellfinance.com/calculators/bond-pricing-calculator

---

Bond Pricing Calculator
=======================

Clean Price, Dirty Price & Accrued Interest

Calculate bond prices from yield to maturity with premium/discount analysis

Embed This Calculator

Enter Values
------------

Face Value (Par) ?

$ 

Par value of the bond

Annual Coupon Rate ?

 %

Annual coupon as % of face value (0 for zero-coupon)

Yield to Maturity (YTM) ?

 %

Enter as percentage (e.g., 4 for 4%)

Years to Maturity ?

 years

Time until bond matures

Coupon Frequency ? Semi-Annual Annual

 Include Accrued Interest ?

Settlement between coupon dates

Days Since Last Coupon ?

 days

Days elapsed since last coupon payment

Days in Coupon Period ?

 days

Total days in the current coupon period

Reset to Defaults

##### Bond Pricing Formula

P = C/m × 1 − (1+y/m)−ny/m + F × (1+y/m)−n

**P** = Price | **C** = Annual coupon | **F** = Face value | **y** = YTM | **m** = Frequency | **n** = Total periods

![Ryan O'Connell, CFA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Calculator by [Ryan O'Connell, CFA](https://ryanoconnellfinance.com/meet-ryan-oconnell-cfa/)

### Bond Pricing Result

Clean Price \--

Dirty Price \--

Accrued Interest \--

Premium / Discount \--

Premium / Discount % \--

Per-Period Coupon \--

Number of Periods \--

Per-Period Yield \--

Undiscounted Total Cash Flows \--

### Formula Breakdown

P = C/m × \[(1 − (1+y/m)−n) / (y/m)\] + F / (1+y/m)n

Present value of coupon annuity + Present value of face value

### Bond Status Interpretation

| Status | Condition | Meaning |
| --- | --- | --- |
| Premium | Price > Face Value | Coupon rate exceeds market yield |
| Par | Price ≈ Face Value | Coupon rate equals market yield |
| Discount | Price < Face Value | Market yield exceeds coupon rate |

##### Model Assumptions

*   Fixed-rate coupon bond (not floating-rate or inflation-linked)
*   Periodic compounding matching payment frequency (not continuous)
*   Flat yield curve — single YTM rate discounts all cash flows
*   Accrued interest uses actual/actual day count convention (simplified)
*   Between-coupon pricing uses the simplified additive approach (Clean + AI) — educational approximation per BKM
*   No embedded options (not callable, putable, or convertible)
*   Non-negative yields assumed

_For educational purposes. Not financial advice. Market conventions simplified._

Understanding Bond Pricing
--------------------------

### Video Explanation

Video: Bond Pricing Explained

### What is Bond Pricing?

**Bond pricing** determines the fair value of a fixed-income security by calculating the present value of its future cash flows. These cash flows consist of periodic coupon payments and the face value (par) returned at maturity, all discounted at the bond's yield to maturity (YTM).

Bond Pricing Equation

**P = C/m × \[(1 − (1+y/m)−n) / (y/m)\] + F / (1+y/m)n**  
PV of Coupon Annuity + PV of Face Value

### Clean Price vs. Dirty Price

#### Clean Price

**Quoted market price**  
Excludes accrued interest. Used for price comparison and avoiding jumps on coupon dates.

#### Dirty Price

**Settlement price**  
Clean price + accrued interest. The actual amount the buyer pays at settlement.

### Price-Yield Relationship

Bond prices and yields move in opposite directions. When market interest rates rise, existing bonds with lower fixed coupons become less attractive, so their prices fall. When rates fall, existing higher-coupon bonds become more valuable.

*   **Premium bond (Price > Par):** Coupon rate > market yield — investors pay extra for above-market income.
*   **Par bond (Price = Par):** Coupon rate = market yield — fairly priced at face value.
*   **Discount bond (Price < Par):** Coupon rate < market yield — price compensates for below-market income.

**BKM Key Insight:** This convex price-yield relationship means that rate decreases produce larger price gains than equivalent rate increases produce losses — a property exploited in [bond convexity](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/)
 analysis.

### When to Use This Calculator vs. YTM Calculator

Use the **Bond Pricing Calculator** when you know the YTM and want to find the bond's price. Use the **Yield to Maturity Calculator** when you know the market price and want to find the yield. They are inverse operations — together they form a complete fixed income toolkit.

### Related Topics

*   [Bond Pricing & Yield to Maturity](https://ryanoconnellfinance.com/bond-pricing-yield-to-maturity/)
    
*   [Clean Price vs. Dirty Price](https://ryanoconnellfinance.com/clean-price-vs-dirty-price/)
    
*   [Bond Duration Calculator](https://ryanoconnellfinance.com/calculators/bond-duration-calculator/)
    
*   [Bond Convexity Calculator](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/)
    
*   [Interest Rate Risk](https://ryanoconnellfinance.com/interest-rate-risk/)
    

**Download This Calculator as an Excel Template** Interactive model with editable formulas — customize, save, and share.

[Get Excel Template](https://ryanoconnellfinance.com/product/bond-pricing-calculator-excel/)

Frequently Asked Questions
--------------------------

### How do you calculate the price of a bond?

A bond's price equals the present value of all its future cash flows — the stream of coupon payments plus the face value returned at maturity. Each cash flow is discounted at the yield to maturity (YTM). For a semi-annual coupon bond: P = Σ\[C/2 / (1 + y/2)t\] + F / (1 + y/2)2n, where C is the annual coupon, y is the YTM, and n is years to maturity.

### What is the difference between clean price and dirty price?

The clean price is the bond's quoted market price, excluding accrued interest. The dirty price (also called the invoice or settlement price) is what the buyer actually pays — it equals the clean price plus accrued interest since the last coupon date. Bond markets quote clean prices to avoid jumps on coupon dates, but settlement occurs at the dirty price. This calculator uses the simplified additive approach (Dirty = Clean + AI), consistent with BKM's educational treatment.

### What is accrued interest on a bond?

Accrued interest is the portion of the next coupon payment that has been earned but not yet paid since the last coupon date. It is calculated as: AI = (Coupon per period) × (Days since last coupon / Days in coupon period). The buyer compensates the seller for this earned interest at settlement.

### Why do bond prices move inversely to interest rates?

When market interest rates rise, the discount rate applied to a bond's fixed cash flows increases, reducing their present value — so the bond's price falls. Conversely, when rates fall, the present value of those same fixed cash flows increases, pushing the bond's price up. This inverse relationship is fundamental to fixed income investing.

### What is a premium bond vs. a discount bond?

A premium bond trades above its face value because its coupon rate exceeds the current market yield — investors pay extra for the higher coupon income. A discount bond trades below face value because its coupon rate is below the market yield. At maturity, both converge to face value (par), so premium bonds experience price depreciation and discount bonds experience price appreciation over time.

### How does coupon frequency affect bond pricing?

Coupon frequency affects bond pricing through the compounding convention. A 10% annual YTM applied semi-annually uses 5% per period, giving an effective annual rate of 10.25%. When comparing bonds with different frequencies, the yield basis must be consistent. Most U.S. bonds pay semi-annually, so yields are quoted on a semi-annual bond-equivalent basis.

##### Disclaimer

This calculator is for educational purposes only and uses simplified conventions (flat yield curve, actual/actual day count, additive accrued interest). Actual bond pricing may differ due to day count conventions (30/360, ACT/365), settlement rules, and market-specific practices. This tool should not be used for trading decisions.

Related Calculators
-------------------

[![Professional finance illustration representing Bond Convexity Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Convexity Calculator\
\
Calculate bond convexity, modified duration, and estimate price changes for interest rate shifts. Analyze the...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-convexity-calculator/)

[![Professional finance illustration representing Forward Rates Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Forward Rates Calculator\
\
Calculate forward interest rates from the spot rate curve. Extract implied future rates using the...\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/forward-rates-calculator/)

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