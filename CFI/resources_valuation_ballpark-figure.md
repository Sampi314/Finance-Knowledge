# Ballpark Figure - Overview, Examples, Sample Calculations

**Source:** https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure

---

Ballpark Figure
===============

A close estimate of the actual value of a variable

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published April 14, 2020

Read Time 7 minutes

What is a Ballpark Figure?
--------------------------

A ballpark figure is a close estimate of the actual value of a variable. It is typically computed using a simple approximation instead of going about the actual computation process, which is more complicated.

![Ballpark Figure](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure1.jpeg)

Ballpark figures provide a reasonable estimate when more sophisticated tools, such as [spreadsheets](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
, are not available. Many such approximations were widely used before computers became commonplace in the finance industry.

Despite the widespread use of computers nowadays, ballpark calculations remain in use. The simplicity of the estimation methods helps reduce the complexity of the calculation. It helps reduce the chances of introducing an error while doing decimal (floating point) operations, as well as a human error such as inputting an incorrect formula.

In the next sections, we will see examples of ballpark figures as used in different areas of finance, such as [time value of money](https://corporatefinanceinstitute.com/resources/valuation/time-value-of-money/)
, derivatives, real estate, and more.

### Ballpark Figure Examples

#### 1\. Time Value of Money

The most common example of using a ballpark figure comes from the very basics of finance – the [Rule of 72](https://corporatefinanceinstitute.com/resources/wealth-management/rule-of-72-double-investment/)
. The rule simply states that to calculate the amount of time it takes for an investment to double is given by the following simple formula:

![Ballpark Figure - Rule of 72](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)

Where:

*   **T** – Time to double an investment
*   **r** – Interest rate in decimal form (so r = 0.1 for 10%)

As the chart below illustrates, the rule of 72 is an excellent estimate when compared to the actual value computed using the [NPER function](https://corporatefinanceinstitute.com/resources/excel/nper-function/)
 in Excel.

![Rule of 72 vs. NPER Function](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure2.png)

It is important to note that the rule does apply if the investment includes intermediate payments, such as an annuity. It is because as payments increase, the time taken to double the investment falls very fast.

#### 2\. Bonds

Bonds come with all sorts of metrics associated with them. One such metric is the bond duration. The duration of a bond is the sensitivity of its price to change in the yield to maturity. For the scope of this article, we will only look at how it is computed using a formula compared to an estimate of the duration.

The following formula is used to compute the duration of a simple coupon bond:

![Simple Coupon Bond - Duration](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure3.png)

Where:

*   **y** – Yield to maturity of the bond
*   **c** – Coupon rate
*   **N** – Number of remaining coupons or periods
*   **t** – Days since the last coupon
*   **T** – Total days in a coupon period

The choice of t and T depends on the day count convention used in valuation. In short, it is very complicated with lots of moving parts. The ballpark estimate for the duration is given by a simpler procedure described below:

![Duration Simple Formula](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure4.png)

Where:

*   **MV(down)** – The market value of the bond calculated by decreasing the current yield by a small amount (∆y)
*   **MV(up)** – The market value of the bond calculated by increasing the current yield by a small amount (∆y)
*   **MV(initial)** – The market value of the bond calculated at the current yield
*   **∆y** – Small amount to change the yield by in order to do the above calculations

The calculation of market value can be done easily using the PV function in Excel, then plugging the values in the above formula. The figure below summarizes the two methods and their results.

![Bond Duration Analysis](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure5.png)

The calculation can be made more precise by reducing the value of ∆y as close to zero as possible or to a satisfactory degree of precision.

#### 3\. Equities

The most commonly used discount rate while valuing equities is the [Weighted Average Cost of Capital (WACC)](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
. The WACC includes many inputs, and some of the inputs are estimated rather than being explicitly calculated. Two such inputs are the beta and the equity risk premium (ERP), which is used to calculate the cost of equity.

There are many ways to determine beta. The explicit approach is to run a regression of stock returns against the market returns. However, it leads to discrepancies in the estimates of beta due to the data used (daily or weekly returns, length of history, etc.). To overcome such a problem, an average or median of comparable company betas from a reliable source is used to arrive at an estimate of the beta.

Similarly, for the ERP, a consensus estimate is used to do the calculations instead of doing the statistical work to compute it from raw data. For example, a number of about 5% is a common ballpark figure for the ERP.

The ideas above are illustrated in a well-cited survey, “[Best Practices in Estimating Cost of Capital](https://www.hbs.edu/faculty/Pages/item.aspx?num=50378)
.”

#### 4\. Derivatives

Derivatives are a broad discipline and offer many techniques to calculate different ballpark figures, some more complex than others. The two techniques listed below show how to calculate the price and implied volatility of close to- or at-the-money call options.

The price of a call option is given using the Black-Scholes formula. However, there is an easier way to calculate the price of the option when it is close-to-the-money. The approximation is based on the Black-Scholes framework, as described below:

![Call Price - Formula](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure6.png)

Where:

*   **S** – Price of the underlying
*   **σ** – Volatility of the underlying
*   **t** – Time to expiration

![Ballpark Option Price Analysis](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure7.png)

The [implied volatility](https://corporatefinanceinstitute.com/resources/derivatives/implied-volatility-iv/)
 of an option is the value of the volatility parameter implied by the market price of the option. It is important to note in valuing options that all inputs can be observed except volatility, which must be estimated. Hence, the difference between the model price (say from the Black-Scholes model) and the market price is attributable to volatility.

To calculate implied volatility, one needs to use a computer program that would do a trial and error search for the correct value of the implied volatility. However, it is possible to get a ballpark figure for implied volatility of close-to-the-money options using the following formula:

![Implied Volatility - Formula](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure8.png)

Where:

*   **C** – Price of at-the-money call
*   **S** – Price of the underlying
*   **t** – Time to expiration

![Ballpark Option Implied Volatility Analysis](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure9.png)

#### 5\. Real Estate

A similar concept to a ballpark figure is the concept of a back-of-the-envelope calculation. The back-of-the-envelope calculation is the simplified version of the actual calculation that gives a ballpark estimate of the required variable.

A common example of such a calculation is the estimation of the cap rate in the real estate sector. There are elaborate models to determine the cap rate of a property, but it can be estimated in a simple calculation described below:

![Ballpark Cap Rate](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure10.png)

  
In the above calculation, the cap rate is calculated as:

![Cap Rate - Formula](https://cdn.corporatefinanceinstitute.com/assets/ballpark-figure11.png)

The net operating income here is derived from basic assumptions and facts about the property. It is a simplistic representation of the more detailed models used in the industry.

### Related Readings

Thank you for reading CFI’s guide to Ballpark Figure. To keep advancing your career, the additional CFI resources below will be useful:

*   [Beta](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)
    
*   [Black-Scholes-Merton Model](https://corporatefinanceinstitute.com/resources/derivatives/black-scholes-merton-model/)
    
*   [Equity Risk Premium](https://corporatefinanceinstitute.com/resources/valuation/equity-risk-premium/)
    
*   [Real Estate Financial Modeling](https://corporatefinanceinstitute.com/course/real-estate-financial-modeling-excel/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

### Analyst Certification FMVA® Program

Below is a break down of [subject weightings](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 in the FMVA® financial analyst program. As you can see there is a heavy focus on financial modeling, finance, Excel, business valuation, budgeting/forecasting, PowerPoint presentations, accounting and business strategy.

[![Financial Analyst certification curriculum](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

A well rounded financial analyst possesses all of the above skills!

### Additional Questions & Answers

CFI is the global institution behind the financial modeling and valuation analyst [FMVA® Designation](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
. CFI is on a mission to enable anyone to be a great financial analyst and have a great career path. In order to help you advance your career, CFI has compiled many resources to assist you along the path.

In order to become a great financial analyst, here are some more [questions and answers](https://corporatefinanceinstitute.com/topic/financial-modeling/)
 for you to discover:

*   [What is Financial Modeling?](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-financial-modeling/)
    
*   [How Do You Build a DCF Model?](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/)
    
*   [What is Sensitivity Analysis?](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-sensitivity-analysis/)
    
*   [How Do You Value a Business?](https://corporatefinanceinstitute.com/resources/valuation/valuation/)
    

Get Certified for Business Intelligence (BIDA®)

Develop analytical superpowers by learning how to use programming and data analytics tools such as VBA, Python, Tableau, Power BI, Power Query, and more.

[Learn More](https://corporatefinanceinstitute.com/certifications/business-intelligence-data-analyst-bida/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fballpark-figure%2F&summary=Ballpark+Figure "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fballpark-figure%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)](https://twitter.com/intent/tweet?text=Ballpark+Figure&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fballpark-figure%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fballpark-figure%2F&summary=Ballpark+Figure "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/ballpark-figure/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)