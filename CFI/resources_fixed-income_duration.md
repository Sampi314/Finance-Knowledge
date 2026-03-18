# Duration - Definition, Finance, Types, Formulas

**Source:** https://corporatefinanceinstitute.com/resources/fixed-income/duration

---

Table of Contents

*   [What is Duration?](https://corporatefinanceinstitute.com/resources/fixed-income/duration#what-is-duration)
    
*   ["Pure" Duration](https://corporatefinanceinstitute.com/resources/fixed-income/duration#pure-duration)
    

*   [The See-Saw and Fulcrum](https://corporatefinanceinstitute.com/resources/fixed-income/duration#the-see-saw-and-fulcrum)
    
*   [Macaulay Duration](https://corporatefinanceinstitute.com/resources/fixed-income/duration#macaulay-duration)
    
*   [Sample Calculation](https://corporatefinanceinstitute.com/resources/fixed-income/duration#sample-calculation)
    

*   [Calculating Duration Using Microsoft Excel](https://corporatefinanceinstitute.com/resources/fixed-income/duration#calculating-duration-using-microsoft-excel)
    
*   [Duration Characteristics](https://corporatefinanceinstitute.com/resources/fixed-income/duration#duration-characteristics)
    
*   [Types of Duration Measures](https://corporatefinanceinstitute.com/resources/fixed-income/duration#types-of-duration-measures)
    
*   [Effective Duration vs Modified Duration](https://corporatefinanceinstitute.com/resources/fixed-income/duration#effective-duration-vs-modified-duration)
    
*   [Portfolio Duration](https://corporatefinanceinstitute.com/resources/fixed-income/duration#portfolio-duration)
    

*   [Related Readings](https://corporatefinanceinstitute.com/resources/fixed-income/duration#related-readings)
    

Duration
========

A tool used in assessing the price volatility of a fixed-income security

Written by [Andrew Loo](https://corporatefinanceinstitute.com/author/andrew-loo/)

Reviewed by [Jeff Schmidt](https://corporatefinanceinstitute.com/author/jeffrey-schmidt/)

Published February 18, 2020

Read Time 13 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

**What is Duration?**
---------------------

Duration is one of the fundamental characteristics of a fixed income security (e.g., a [bond](https://corporatefinanceinstitute.com/resources/fixed-income/bonds/)
), alongside maturity, yield, [coupon](https://corporatefinanceinstitute.com/resources/fixed-income/coupon-rate/)
, and call features. It is the most commonly used tool in the bond markets as an assessment of the interest rate sensitivity of a fixed income security.

Since the [interest rate](https://corporatefinanceinstitute.com/resources/commercial-lending/interest-rate/)
 is one of the most significant drivers of a bond’s value, duration measures how much changes in the yield-to-maturity (YTM) of the instrument will ultimately impact the bond’s price.

A fixed income security with a greater duration indicates a higher sensitivity to interest rates and thus, the greater the interest rate risk it has. And as the price of most fixed income securities have an inverse relationship with yields, a security with a greater duration will have more interest rate risk than a security with a shorter duration.

However, in the markets, duration can also be understood to be a measure of how much a bond price will move given changes in the yield-to-maturity. This interpretation is more correctly called “dollar duration” but market participants stubbornly tend to use this duration definition the most.

Duration is commonly used in the portfolio and [risk management](https://corporatefinanceinstitute.com/resources/career-map/sell-side/risk-management/risk-management/)
 of fixed income instruments. Using interest rate forecasts, a portfolio manager can change a portfolio’s composition to align its duration with the expected movement of interest rates.

### Key Highlights

*   Duration is a way of measuring the interest rate risk of an individual or portfolio of fixed income securities.
*   Pure, or Macaulay duration, is calculated by discounting all cash flows of a bond using the proper interest rate and then time weighting each of the cash flows.
*   There are many other types of duration measures used by market practitioners to estimate the impact of interest rate changes to bond prices.

“Pure” Duration
---------------

The term duration is mathematically defined as the sum of the weighted average time of each of the cash flows that make up a bond. In other words, “pure” duration (denoted in years) is how long it will take for an investor to receive the bond’s present value based on the expected future cash flows of the bonds.

### The See-Saw and Fulcrum

![Duration Definition](https://cdn.corporatefinanceinstitute.com/assets/duration-1.png)

In the figure above, we have a simplified diagram of a five-year fixed-rate, annual-pay coupon bond. Each of the bars represents interest cash flows, or coupons, and a final cash flow consisting of the principal and the final interest payment.

If you imagine this entire cash flow diagram being put on a see-saw, duration is the point where the cash flow balances, also known as a fulcrum. This is the point of time represented by the orange triangle above measured in years.

### Macaulay Duration

This definition of “pure” duration was introduced by Canadian economist [Frederick Macaulay](https://www.nber.org/people/frederick_macaulay)
. It is a measure of the time required for an investor to be repaid the bond’s present value by the bond’s total cash flows. The Macaulay duration is measured in units of time (e.g., years).

The formula for the calculation of Macaulay duration (DMac) is expressed in the following way:

![Macaulay Duration - Formula](https://cdn.corporatefinanceinstitute.com/assets/duration-1-1.png)

### Sample Calculation

Using the formula above, let’s calculate the Macaulay duration for a hypothetical three-year bond. This bond has a 5% coupon that is paid at the end of each year. We begin by calculating the present values of the cash flows from each of the three years.

By adding up the [present values](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/)
 of each of the three years, we get to a sum of $102.78, which is the bond’s price.

![Macaulay Duration - Sample Calculation](https://cdn.corporatefinanceinstitute.com/assets/duration-2.png)

Next, we give a time weight to each of the present values by multiplying the PVCFt by the time period (i.e., 1 for the first year’s cash flows, 2 for the second year’s cash flows, and 3 for the last year’s cash flows).

Lastly, we take each of the PVCFt amounts and divide by the product of the payment frequency and bond price (or PVTCF). This gives us a weighted time figure for each of the years. Combining all the weighted times for each of the three years in our example gives us a Macauley duration of 2.8614 years for our hypothetical bond.

Calculating Duration Using Microsoft Excel
------------------------------------------

Now if this calculation becomes too unwieldy to do manually, there is an easier way of calculating duration by using Microsoft Excel. The formula is:

**\=DURATION(settlement, maturity, coupon, yld, frequency, \[basis\])**

The [DURATION function](https://support.microsoft.com/en-us/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038)
 uses the following arguments:

1.  **Settlement** (required argument) – This is the settlement date of a given security. Depending on the bond market, it is generally the trade day plus one business day or three business days (T+1 or T+3).
2.  **Maturity** (required argument) – This is the date when the security expires, also known as the maturity date.
3.  **Coupon** (required argument) – The stated coupon of the bond in annual terms.
4.  **Yld** (required argument) – The security’s annual yield to maturity.
5.  **Frequency** (required argument) – This is the number of coupon payments per year. The argument can take a value of 1 (annual payment), 2 (semi-annual payments), or 4 (quarterly payments).
6.  **Basis** (optional argument) – It specifies the day count basis to be used. It uses one of the following values:
7.  | Basis | Day Count basis |
    | --- | --- |
    | 0 or omitted | US(NASD) 30/360 |
    | 1   | Actual/actual |
    | 2   | Actual/360 |
    | 3   | Actual/365 |
    | 4   | European 30/360 |
    
    The function will default to zero when omitted. It indicates that the days in the month are counted using the US 30-day method with a 360-day year. When we enter 1 as the basis, the function uses the actual number of days in the month and year. Whereas, when we enter 2, it will count the actual days in the month with a 360-day year, while 3 will assume a 365-day year. When we enter 4 as the basis, it is the same as 1, except that it uses the European 30-day method. 

If we use our hypothetical three-year, fixed-rate coupon bond from earlier, the DURATION function on Microsoft Excel gives us the same result as we manually calculated: 2.8614 years.

![](https://cdn.corporatefinanceinstitute.com/assets/duration-4.png)

Duration Characteristics
------------------------

Let’s dive a bit deeper into the characteristics of Macaulay duration by continuing with our see-saw/fulcrum analogy:

#### 1\. Duration is not the same as maturity

As you can see in the figure above, the duration of a bond is not the same as its maturity. As a matter of fact, for coupon-paying bonds, the duration of that bond will always be shorter than the term to maturity of that bond.

So, what about a [zero-coupon bond](https://corporatefinanceinstitute.com/resources/fixed-income/zero-coupon-bond/)
? As this type of bond is sold at a discount to par, and matures at par, a zero-coupon bond has no coupon payments along the way. Hence, if we picture the see-saw, the duration for a zero-coupon bond would be equal to its term to maturity, as we see in the illustration below.

![Duration of a Zero-Coupon Bond](https://cdn.corporatefinanceinstitute.com/assets/duration-5.png)

#### 2\. Term to maturity impact on duration measures

Using our see-saw, let’s think about how a longer term to maturity impacts duration. In the following diagram, we have a five-year and an eight-year, fixed-rate, annual-pay coupon bond that pays the same coupon rate.

![Term to Maturity Impact on Duration Measures](https://cdn.corporatefinanceinstitute.com/assets/duration-6.png)

Not surprisingly, a bond with a longer remaining term to maturity will have a longer duration. This makes intuitive sense using our see-saw as a longer bond would require moving the fulcrum further to the right, increasing the Macaulay duration.

Therefore, for a given interest rate increase, it can be expected that the bond with the longer term to maturity will have a larger interest rate risk than a shorter bond with the same coupon.

#### 3\. Impact of coupons on duration measures

If we look at coupon payments of a fixed-rate bond, we can also see how two similar bonds with different coupon rates can have different duration measures.

![Impact of Coupons on Duration Measures](https://cdn.corporatefinanceinstitute.com/assets/duration-7.png)

In our example above, using our analogy, you may be able to see that the bond on the bottom with the higher coupon rate will have a shorter duration as more of the weight sits on the left hand side of the see-saw. Comparing this with the bond on the top with smaller coupon payments, you will see that the fulcrum is further out to the right hand side, meaning a longer duration.

#### 4\. How yields impact Macaulay Duration

Lastly, we want to think about the relationship between Macaulay duration and yield to maturity. If we consider that the cash flows in our Macaulay duration calculation were discounted back to present value using the yield to maturity, it would reason that an increase in yield to maturity means that the cash flows further out are worth less, so Macaulay duration is shorter.

This means that yield to maturity and Macaulay duration have an inverse relationship.

**Types of Duration Measures**
------------------------------

Our discussion on “pure” or Macaulay duration measures is very much a theoretical construct. In capital markets, a duration measure that gives the weighted average time for all the cash flows, measured in years, isn’t really all that helpful when we are thinking about the interest rate sensitivity of a bond’s price.

#### **Modified Duration**

Therefore, market participants came up with a more practical duration measure, called modified duration. Relative to the Macaulay duration, the modified duration metric is a slightly more precise measure of price sensitivity.

The modified duration measure takes duration one step further and gives the **percentage change** in the bond’s price per basis point. Unlike the Macaulay duration, modified duration is measured in percentages.

The formula for the modified duration is as follows:

![Modified Duration - Formula](https://cdn.corporatefinanceinstitute.com/assets/duration-8.png)

By dividing pure or Macaulay duration by (1+YTM/f), we have modified the duration measure to something that makes a bit more practical sense. In our three year bond example, the Macaulay duration was 2.8614 years, but the modified duration is 2.7513%. This means that a 1% change in yield to maturity will mean a 2.7513% fall in the price of the bond.

#### Dollar Duration (“Risk”)

For those who work on Wall Street trading desks though, the concept of modified duration was still not direct enough. Modified duration tells you the percentage change in price, but traders are interested in knowing how much the dollar price changes as yields move.

This was the genesis for dollar duration. Dollar duration measures the change in bond prices for a given change in yield to maturity. So, a trader who knows the dollar duration of a bond can easily calculate how much his or her position will change in price given a change in yield.

The conversion from modified duration to dollar duration follows this formula:

![Dollar Duration - Formula](https://cdn.corporatefinanceinstitute.com/assets/duration-9.png)

By taking our modified duration measure and multiplying that by the dollar price of our bond and then by a factor of 0.01, we arrive at a duration measure which gives an actual price change for a bond given a 100 basis point (or 1%) change in yield, which is clearly denoted in dollar terms.

Following on with our three-year bond example, the dollar duration works out to be $2.8278 dollars. This is interpreted to mean for a 100 basis point increase in the yield to maturity of our three-year bullet, annual-pay bond, the price will **fall** by $2.8278, making it much easier to work with. As a matter of fact, dollar duration is also sometimes simply referred to as “risk.”

It is also worth pointing out that even though two bonds may have the same modified duration, they may have different dollar duration measures if the prices of the bonds are not the same. A bond with a higher trading price will have a higher dollar duration than a bond with the same modified duration that trades at a lower price.

Both modified and dollar duration, therefore, are metrics for how sensitive a bond’s price is to movements in its yield. The price of a longer modified or dollar duration fixed-income instrument will move more significantly to a change in yield as compared to the price of a shorter modified or dollar duration instrument.

#### Other Measures of Yield Sensitivity

There are other variations of dollar duration that market participants tend to use.

#### Dollar Value of a Basis Point (AKA Price Value of Basis Point)

The dollar value of a basis point, known as DV01, is one hundredth the value of dollar duration. It is calculated by taking modified duration multiplied by the dollar price of the bond and then multiplying by a factor of 0.0001 in order to convert it to a basis point measure.

![Dollar Value of a Basis Point](https://cdn.corporatefinanceinstitute.com/assets/duration-10.png)

This is useful for market practitioners to get an idea of a change in bond price for movements in yield in 1 basis point increments. On trading floors, you will also hear DV01 called PVBP (the Price Value of a Basis Point).

#### Yield Value Change of a 0.01% Price Move

This measure, abbreviated as YV0.01, is the opposite way of looking at DV01. This duration measure is less commonly used but essentially indicates how much a 0.01% price move in a bond will impact the yield of that instrument.

#### Yield Value Change of a 1/32nd Price Move

Even more specific is the yield value change of a 1/32nd move in price, known as YV32 for short. In certain fixed income market, such as US government bonds and US mortgage-backed securities markets, the price is quoted in 1/32nds. This measure is meant to simplify the understanding of the impact to a bond’s yield for a 1/32nd (or a “tick”) move in the price of the bond.

**Effective Duration vs Modified Duration**
-------------------------------------------

Effective duration is a useful measure of the duration for bonds with embedded options (e.g., callable bonds). A bond with an embedded option tends to behave differently from an option-free bond when yields move as the bond may be either called or put if the embedded option is in-the-money. This means that the price change for a given change in yield is not constant.

As such, unlike the modified duration and Macaulay duration, effective duration looks at the actual change in duration for an upwards and downwards change in yield to maturity for an instrument.

The effective duration is calculated using the following formula:

![Effective Duration - Formula](https://cdn.corporatefinanceinstitute.com/assets/duration-11.png)

Where:

*   **Price (Y**↓**)**  – The bond’s price if yields fall by 1 basis point.
*   **Price (Y↑)**  – The bond’s price if yields rise by 1 basis point.
*   **Dollar Price** – The present value of all cash flows of the bond.
*   **ΔY** – The yield change.

Additionally, effective duration may also be useful when looking at option-free bonds in instances of large yield moves, as duration is not a constant figure due to the concept of [convexity](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/negative-convexity/)
.

![Convexity](https://cdn.corporatefinanceinstitute.com/assets/duration-12.png)

Convexity can be either negative or positive:

#### 1\. Positive convexity

This occurs when the duration and the yield of a bond decrease or increase together, thus, they are positively correlated. The yield curve for bonds with positive convexities usually follows an upward movement.

#### 2\. Negative convexity

This occurs when there is an inverse relationship between the yield and the duration. It means that with a decline in duration, there is an increase in yield. Therefore, they are negatively correlated. The yield curve for a bond with a [negative convexity](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/negative-convexity/)
 usually follows a downward movement.

In any event, where we have large movements in yield, it is important to consider that since duration is not a static measure, we should look at effective duration as opposed to modified duration.

However, duration only reveals one side of a fixed income security. A full analysis of the fixed income asset must be done using all available characteristics.

CFI’s [**Fixed Income Fundamentals Course**](https://corporatefinanceinstitute.com/course/introduction-to-fixed-income/)
 covers the essential topics for fixed-income valuation.

Portfolio Duration
------------------

One interesting thing about duration is that it is additive. By that, it means that the duration of individual securities in a portfolio can be combined into a duration for that entire portfolio.

There are generally two methods for calculating the duration of a bond portfolio:

1.  Weighted average of time until you receive the aggregate cash flows; and
2.  Weighted average of the individual bond durations which comprise the portfolio.

While the first approach is the more theoretically correct approach, it is harder to implement in practice. Therefore, the second approach below is the more commonly method used by fixed income portfolio managers.

![Portfolio Duration - Formula](https://cdn.corporatefinanceinstitute.com/assets/duration-13.png)

Where:

*   **Wi** – Market value of bond _i_ as a proportion of the market value of the entire bond portfolio
*   **DMaci**  – The Macaulay duration of bond _i_
*   **n** – The number of all bonds in the portfolio

However, this approach is far from perfect as it assumes that any yield changes are a parallel shift across the entire [yield curve](https://corporatefinanceinstitute.com/resources/fixed-income/yield-curve/)
 (for example, yields in the one-year part of the curve move up the same number of basis points as the two-, three-, five- and 10-year parts of the curve) when, in reality, changes in interest rates are seldom uniform across the curve.

### **Related Readings**

Thank you for reading CFI’s guide on Duration. To keep advancing your career, the additional CFI resources below will be useful:

[Bond Pricing](https://corporatefinanceinstitute.com/resources/fixed-income/bond-pricing/)

[Debt Capital Markets](https://corporatefinanceinstitute.com/resources/career-map/sell-side/investment-banking/dcm/)

[Equity Risk Premium](https://corporatefinanceinstitute.com/resources/valuation/equity-risk-premium/)

[Fixed Income Trading](https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-trading/)

[**See all fixed income resources**](https://corporatefinanceinstitute.com/topic/fixed-income/)

Get Certified for Capital Markets (CMSA®)

From equities and fixed income to derivatives, the CMSA certification bridges the gap from where you are now to where you want to be — a world-class capital markets analyst.

[Learn MoreLearn More](https://corporatefinanceinstitute.com/certifications/capital-markets-securities-analyst-cmsa/)

*   Share this article
*   [![Share on LinkedIn](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Fduration%2F&summary=Duration "Share on LinkedIn")
    
*   [![Share on Facebook](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Fduration%2F "Share on Facebook")
    
*   [![Share on Twitter](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://twitter.com/intent/tweet?text=Duration&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Fduration%2F "Share on Twitter")
    
*   [![Share on WhatsApp](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Fduration%2F&summary=Duration "Share on WhatsApp")
    
*   [![Copy link](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/resources/fixed-income/duration/ "Copy link")
    

[Corporate Finance Institute](https://corporatefinanceinstitute.com/)

[Back to Website](https://corporatefinanceinstitute.com/)

0 search results for ‘’

People also search for: excel power bi esg accounting balance sheet fmva real estate

Explore Our Certifications

[Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

[Commercial Banking & Credit Analyst (CBCA)®](https://corporatefinanceinstitute.com/certifications/commercial-banking-credit-analyst-certification-cbca/)

[Capital Markets & Securities Analyst (CMSA)®](https://corporatefinanceinstitute.com/certifications/capital-markets-securities-analyst-cmsa/)

[Certified Business Intelligence & Data Analyst (BIDA)®](https://corporatefinanceinstitute.com/certifications/business-intelligence-data-analyst-bida/)

[Financial Planning & Wealth Management Professional (FPWMP)®](https://corporatefinanceinstitute.com/certifications/financial-planning-and-wealth-management-fpwm-program/)

[FinTech Industry Professional (FTIP)®](https://corporatefinanceinstitute.com/certifications/fintech-industry-professional/)

Resources

[Mastering Excel Shortcuts for PC and Mac Work Smarter in Excel with Keyboard Shortcuts If you're still reaching for the mouse every few seconds, it's time to level up. The best Excel keyboard...](https://corporatefinanceinstitute.com/resources/excel/excel-shortcuts-pc-mac/)

[Financial Modeling Guidelines CFI’s free Financial Modeling Guidelines is a thorough and complete resource covering model design, model building blocks, and common tips, tricks,...](https://corporatefinanceinstitute.com/resources/financial-modeling/free-financial-modeling-guide/)

[SQL Data Types What are SQL Data Types? The Structured Query Language (SQL) comprises several different data types that allow it to store different types of information...](https://corporatefinanceinstitute.com/resources/data-science/sql-data-types/)

[Structured Query Language (SQL) What is Structured Query Language (SQL)? Structured Query Language (known as SQL) is a programming language used to interact with a database....](https://corporatefinanceinstitute.com/resources/data-science/structured-query-language-sql/)

[See All Resources See All](https://corporatefinanceinstitute.com/resources/)

Popular Courses

 [![Excel Fundamentals - Formulas for Finance](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)