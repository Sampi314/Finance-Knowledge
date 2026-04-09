# Bond Duration Calculator - Macaulay & Modified | Ryan O'Connell

**Source:** https://ryanoconnellfinance.com/calculators/bond-duration-calculator

---

Bond Duration Calculator
========================

Calculate Macaulay Duration, Modified Duration, and DV01 for Fixed Income Securities

CFA-aligned calculations with detailed cash flow breakdown and sensitivity analysis

Embed This Calculator

Bond Parameters
---------------

Face Value (Par)

$ 

Coupon Rate

 %

Yield to Maturity

 %

Years to Maturity 

Payment Frequency Annual (1 payment/year) Semi-Annual (2 payments/year) Quarterly (4 payments/year) Monthly (12 payments/year)

**High Yield:** Calculations proceed but may represent distressed securities.

### Quick Examples

Load a preset to explore different bond characteristics:

Zero-Coupon Treasury Note IG Corporate High-Yield Premium Bond

### Assumptions

*   Settlement at coupon date (no accrued interest)
*   Yield compounded at payment frequency
*   Equal period lengths assumed
*   Negative yields not supported

### Duration Metrics

Macaulay Duration **\--** years

Modified Duration **\--**

Effective Duration **\--**

Bond Price **\--**

DV01 **\--**

Convexity **\--**

### Interest Rate Sensitivity

Estimated price change if yield moves:

\-100 bps \--

\-50 bps \--

\-25 bps \--

Current \--

+25 bps \--

+50 bps \--

+100 bps \--

### Visualization

Cash Flow Timeline Duration Sensitivity

Enter bond parameters to see the visualization

Duration: \-- years. A 1% yield increase would decrease price by approximately \--%.

### Cash Flow Breakdown

\-- periods

| Period | Time (Years) | Cash Flow | Discount Factor | Present Value | Weight | Weighted Time |
| --- | --- | --- | --- | --- | --- | --- |
| Total |     | \-- | \-- | \-- | 100% | \-- |

Understanding Bond Duration
---------------------------

### Video Explanation

Video: Bond Duration Explained

### What is Bond Duration?

Bond duration measures the sensitivity of a bond's price to changes in interest rates. It represents the weighted average time until you receive the bond's cash flows, where each cash flow is weighted by its present value as a proportion of the bond's total price.

Duration is one of the most important concepts in fixed income investing because it helps investors understand and manage interest rate risk. A higher duration means greater price sensitivity to interest rate changes.

#### Video: Bond Duration and Bond Convexity Explained

### Macaulay Duration

**Macaulay Duration** is measured in years and represents the weighted average time to receive the bond's cash flows. It was developed by Frederick Macaulay in 1938 and answers the question: "On average, how long do I have to wait to receive my money back?"

DMac = Σ(t × PVt) / Price

For example, a 10-year bond paying a 5% coupon has a Macaulay Duration of about 8 years because you receive coupon payments throughout the life of the bond, not just at maturity.

### Modified Duration

**Modified Duration** adjusts Macaulay Duration to directly measure price sensitivity. It tells you the approximate percentage price change for a 1% change in yield. This is the most commonly used duration measure for interest rate risk management.

DMod = DMac / (1 + y/m)

Where y is the yield to maturity and m is the number of payments per year. For example, if a bond has a modified duration of 7, a 1% increase in interest rates would cause approximately a 7% decrease in the bond's price.

### Effective Duration

**Effective Duration** measures price sensitivity empirically by actually calculating how the bond price changes when yields are shocked up and down. Unlike Modified Duration (which is derived analytically from Macaulay Duration), Effective Duration uses numerical methods.

DEff = (P\- - P+) / (2 × P0 × Δy)

Where P\- is the price when yield decreases, P+ is the price when yield increases, P0 is the current price, and Δy is the yield shock (typically 25 basis points).

**Why use Effective Duration?** For plain vanilla bonds, Effective Duration equals Modified Duration. However, for bonds with embedded options (callable bonds, mortgage-backed securities), the cash flows change when rates change, making Modified Duration inaccurate. Effective Duration captures these effects.

#### Video: Calculating Macaulay, Modified, and Effective Duration in Excel

### Understanding Convexity

**Convexity** measures the curvature of the price-yield relationship. While duration provides a linear approximation of price changes, the actual relationship between bond prices and yields is curved. This curvature is convexity.

Convexity = \[Σ t(t+1) × PVt\] / \[Price × (1+y/m)² × m²\]

**Why convexity matters:**

*   **Duration underestimates gains:** When yields fall significantly, the actual price increase is larger than duration alone predicts
*   **Duration overestimates losses:** When yields rise significantly, the actual price decrease is smaller than duration alone predicts
*   **Positive convexity is good:** It means you gain more when rates fall than you lose when rates rise by the same amount

The complete price change formula incorporating both duration and convexity is:

% Price Change ≈ -DMod × Δy + ½ × Convexity × (Δy)²

The Duration Sensitivity chart above illustrates this relationship: the curved blue line shows actual prices (including convexity), while the straight dashed line shows the duration-only approximation.

#### Video: Calculate Bond Convexity and Duration in Excel

### How to Use This Calculator

1.  **Enter bond parameters** - Input the face value, coupon rate, yield to maturity, years to maturity, and payment frequency
2.  **Review key metrics** - See the calculated Macaulay Duration, Modified Duration, Effective Duration, DV01, and Convexity
3.  **Analyze sensitivity** - The sensitivity table shows estimated price changes for various yield movements
4.  **Explore the chart** - The Duration Sensitivity chart shows the price-yield relationship and demonstrates convexity visually
5.  **Explore cash flows** - The breakdown table shows each payment's present value and weight
6.  **Use presets** - Try the example bonds to see how different characteristics affect duration and convexity

### Why Duration and Convexity Matter

*   **Interest Rate Risk:** Duration quantifies how much your bond portfolio will change in value when rates move; convexity refines this estimate for larger rate changes
*   **Portfolio Immunization:** Match portfolio duration to your investment horizon to minimize interest rate risk
*   **Hedging:** Use duration and convexity to calculate hedge ratios for interest rate derivatives
*   **Bond Selection:** Given two bonds with equal duration, prefer the one with higher convexity (all else equal)
*   **Comparison:** Compare bonds with different coupons and maturities on an equal basis

### Duration and Convexity Limitations

While duration and convexity are powerful tools, they have important limitations:

*   **Parallel shift assumption:** Duration assumes the entire yield curve shifts by the same amount, which rarely happens in practice
*   **Instantaneous change:** The formulas assume yields change instantaneously; in reality, changes occur over time
*   **No credit risk:** Duration doesn't account for the possibility of default
*   **Embedded options:** For callable or putable bonds, use Effective Duration instead of Modified Duration

**CFA Exam Tip:** For zero-coupon bonds, Macaulay Duration equals time to maturity. As coupon rates increase (holding maturity constant), duration decreases because you receive more cash flows earlier. Higher convexity is always desirable - it's the "free lunch" of fixed income investing.

Frequently Asked Questions
--------------------------

### What is Macaulay Duration?

Macaulay Duration measures the weighted average time until a bond's cash flows are received, expressed in years. It's calculated by weighting each cash flow by the present value of that cash flow, then dividing by the bond's current price. A 10-year bond with a 5% coupon typically has a Macaulay duration of about 8 years because you receive coupon payments before maturity.

### What is Modified Duration?

Modified Duration measures a bond's price sensitivity to interest rate changes. It's calculated by dividing Macaulay Duration by (1 + yield/frequency). For example, if a bond has a modified duration of 7, a 1% increase in interest rates would cause approximately a 7% decrease in the bond's price. This is the primary metric used for interest rate risk management.

### How do I calculate bond duration?

To calculate bond duration: 1) Determine all future cash flows (coupon payments and principal), 2) Calculate the present value of each cash flow, 3) Weight each present value by time to receipt, 4) Sum all weighted values and divide by the bond's price for Macaulay duration, 5) Divide by (1 + yield/frequency) for modified duration. Our calculator automates this entire process.

### What is a good bond duration?

There's no universally "good" duration - it depends on your investment goals and interest rate outlook. Shorter durations (1-3 years) suit investors expecting rising rates or needing liquidity. Longer durations (7+ years) benefit from rate declines but carry more risk. Match your bond duration to your investment horizon for immunization against interest rate risk.

### How does duration relate to interest rate risk?

Duration directly measures interest rate risk. The formula is: Percentage Price Change ≈ -Modified Duration × Change in Yield. A bond with duration of 5 will lose approximately 5% in value for every 1% increase in interest rates. Higher duration means higher interest rate sensitivity and greater price volatility.

### What is the difference between duration and maturity?

Maturity is simply when the bond's principal is repaid - it's a fixed date. Duration considers ALL cash flows (coupons and principal), weighted by when you receive them. A 10-year bond paying 8% annual coupons has a duration closer to 7 years because you receive substantial cash flows before maturity. Zero-coupon bonds are the only ones where duration equals maturity.

##### Important Disclaimer

This calculator is for educational purposes only. It assumes settlement at coupon dates, equal period lengths, and yield compounded at payment frequency. Actual bond prices may differ due to accrued interest, day count conventions, call features, credit risk, and other factors. This is not financial advice.

Related Calculators
-------------------

[![Professional finance illustration representing Bond Immunization Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20200'%3E%3C/svg%3E)\
\
### Bond Immunization Calculator\
\
Try Calculator →](https://ryanoconnellfinance.com/calculators/bond-immunization-calculator/)

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