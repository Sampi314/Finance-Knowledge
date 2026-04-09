# Fixed Income Interest Rate Risk - Impact of bond features and convexity

**Source:** https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-interest-rate-risk

---

Fixed Income Interest Rate Risk
===============================

fixed income asset losing value due to a change in interest rates

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published January 13, 2020

Read Time 4 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

What is Fixed Income Interest Rate Risk?
----------------------------------------

Fixed income interest rate risk is the [risk of a fixed income asset](https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-risks/)
 losing value due to a change in interest rates. Since bonds and interest rates have an inverse relationship, as interest rates rise, the value/price of [bonds](https://corporatefinanceinstitute.com/resources/fixed-income/bonds/)
 falls. Interest rate risk can be measured by the full valuation approach or the duration/convexity approach. This article will focus on the convexity approach.

![Fixed income interest rate risk illustration - bull and bear](https://cdn.corporatefinanceinstitute.com/assets/Income-rate-risk-1024x496.jpg)

### What affects interest rate risk?

[Interest rate](https://corporatefinanceinstitute.com/resources/commercial-lending/interest-rate/)
 risk affects bonds differently based on the features that the bonds possess. Some of these features include maturity date, coupon rate, and embedded options

#### Maturity

Bonds with a longer maturity rate are more susceptible to changing interest rates. If a 20-year bond has a yield of 4%, it would lose value if the interest rate rises to 5%. This is because investors have more incentive to buy the 5% bond. Thus, the 4% yield bond will need to have a lower price to give investors a reason to buy it.

The price has to decrease by a large amount, as it accounts for 20 years of lower [coupon rates](https://corporatefinanceinstitute.com/resources/fixed-income/coupon-rate/)
. However, if the bond matures in two years, the price will stay relatively the same. This is because the price decrease only accounts for two years of interest payments with a lower coupon rate.

#### Coupon rate

The next feature of a bond that determines the impact of interest rates is the coupon rate. The yield to maturity – [YTM](https://corporatefinanceinstitute.com/resources/fixed-income/yield-to-maturity-ytm/)
 – of the old bond must be the same as the YTM of the newer bond offering a higher interest rate.

Imagine one bond with a 2% coupon rate and one with a 4% coupon rate. The face value of the 2% bond will have to drop to match up appropriately with the 4% bond.

#### Embedded options

Lastly, [embedded options](https://en.wikipedia.org/wiki/Embedded_option)
 react to interest rates differently depending on the [option](https://corporatefinanceinstitute.com/resources/derivatives/options-calls-and-puts/)
.  For example, when the interest rate increases, the price for a [callable bond](https://corporatefinanceinstitute.com/resources/fixed-income/callable-bond/)
 and option-free bond will both decrease. However, the price of the callable bond will not fall as much, by comparison.

The equation for the price of a callable bond is:

Price of callable bond = price of option-free bond – the price of an embedded call option

*   option-free bond:  $50
*   embedded call option: $20
*   Price of callable bond: $30

If the interest rate rises, then the price of the option-free bond will drop. But the drop is offset by the drop in the embedded call option.

*   option-free bond: $50-$10= $40
*   embedded call option: $20-$5 = $15
*   price of callable bond: $25

As shown by the example above, the price of the option-free bond dropped by $10. However, the embedded call option only dropped by $5. This is because the $5 decrease in the call option offset the change. The value of the callable bond is not as exposed to interest rate risk.

### Measuring interest rate risk

Interest rate risk can be measured by [duration](https://corporatefinanceinstitute.com/resources/fixed-income/duration/)
 and convexity. Duration measures the approximate sensitivity of the value of the bond to the change in interest rate. Convexity is another measure of the change in price. An important note is that this measure is not the same as the convex shape of the price/yield relationship.

#### Convexity

As the [price/yield relationship](https://corporatefinanceinstitute.com/resources/fixed-income/yield-curve/)
 is curved, the duration measure is not accurate. Duration only measures the linear relationship between the price and the yield of the bond, and does not consider the curved shape. Simply put, as the yield on a bond changes, so does the duration. Thus, measuring the impact of convexity is important for understanding interest rate risk.

For bonds with a more convex price/yield curve, the interest rate increase has less effect on the price. On the other hand, as the interest rate decreases, the bond price increases more for bonds with a more convex shape.

The formula for the convexity measure is:

*   Convexity Measure = (V\+ \+ V– – 2V0) / (2V0(Δy)2)

Where:

*   V0 \= initial price
*   V\+ \= price if yields increase by Δy
*   V– \= price if yields decrease by Δy
*   Δy = change in yield

The convexity measure produces a number that is not simple to interpret. Thus, the convexity adjustment is used to estimate the percentage of price change.

The formula for the convexity adjustment is:

*   Convexity Adjustment = convexity measure x (Δy)2 x 100

The convexity adjustment is a percentage that remains the same regardless of whether the change in yield is an increase or decrease. To get the estimated percentage price change, add the convexity adjustment to the estimated change using duration. If the number is 31%, then that means the price will increase by approximately 31%.

### Why it matters

By understanding the impact of interest rates, investors can make more knowledgable decisions on the purchase of fixed income securities. This gives investors a better idea as to what type of bonds they would like in their portfolio.

An investor with a greater risk tolerance can purchase a bond with a high estimated percentage price change while a risk-averse investor can choose one with lower duration and convexity.

### Additional Resources

Thank you for reading CFI’s article on fixed income interest rate risk. To keep learning and advancing your career, we recommend these additional CFI resources:

*   [Fixed Income Risk](https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-risks/)
    
*   [Floating Rate Note](https://corporatefinanceinstitute.com/resources/fixed-income/floating-rate-note/)
    
*   [Fixed Income Bond Terms](https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-bond-terms/)
    
*   [Fixed Income Trading](https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-trading/)
    
*   **[See all fixed income resources](https://corporatefinanceinstitute.com/topic/fixed-income/)
    **

Get Certified for Capital Markets (CMSA®)

From equities and fixed income to derivatives, the CMSA certification bridges the gap from where you are now to where you want to be — a world-class capital markets analyst.

[Learn MoreLearn More](https://corporatefinanceinstitute.com/certifications/capital-markets-securities-analyst-cmsa/)

*   Share this article
*   [![Share on LinkedIn](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Ffixed-income-interest-rate-risk%2F&summary=Fixed+Income+Interest+Rate+Risk "Share on LinkedIn")
    
*   [![Share on Facebook](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Ffixed-income-interest-rate-risk%2F "Share on Facebook")
    
*   [![Share on Twitter](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://twitter.com/intent/tweet?text=Fixed+Income+Interest+Rate+Risk&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Ffixed-income-interest-rate-risk%2F "Share on Twitter")
    
*   [![Share on WhatsApp](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffixed-income%2Ffixed-income-interest-rate-risk%2F&summary=Fixed+Income+Interest+Rate+Risk "Share on WhatsApp")
    
*   [![Copy link](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/resources/fixed-income/fixed-income-interest-rate-risk/ "Copy link")
    

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