# Sortino Ratio - Overview, How To Calculate, When To Use

**Source:** https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2

---

Table of Contents

*   [What is the Sortino Ratio?](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#what-is-the-sortino-ratio)
    

*   [Understanding the Sortino Ratio](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#understanding-the-sortino-ratio)
    
*   [How to Calculate the Sortino Ratio](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#how-to-calculate-the-sortino-ratio)
    
*   [When to Use the Sortino Ratio](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#when-to-use-the-sortino-ratio)
    
*   [Key Considerations](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#key-considerations)
    
*   [Wrap Up](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#wrap-up)
    
*   [Related Readings](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/#related-readings)
    

Sortino Ratio
=============

A risk-adjustment metric used to determine the additional return for each unit of downside risk

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published October 19, 2020

Read Time 4 minutes

What is the Sortino Ratio?
--------------------------

The Sortino ratio is a risk-adjustment metric used to determine the additional return for each unit of downside risk. It is computed by first finding the difference between an investment’s average return rate and the [risk-free rate](https://corporatefinanceinstitute.com/resources/valuation/risk-free-rate/)
. The result is then divided by the standard deviation of negative returns. Ideally, a high Sortino ratio is preferred, as it indicates that an investor will earn a higher return for each unit of a [downside risk](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/downside-risk/)
.

![Sortino Ratio](https://cdn.corporatefinanceinstitute.com/assets/sortino-ratio1.png)

### **Summary**

*   **The Sortino ratio is used to determine the risk-adjusted return on investment.**
*   **It is a refinement of the Sharpe ratio but only penalizes the returns, which have downside risks.**
*   **To measure the Sortino ratio, start by finding the difference between the weighted mean of return and the risk-free return rate. Next, find the quotient between this difference and the standard deviation of downside risks.**

### Understanding the Sortino Ratio

If you’re looking to invest, you should not concentrate on only the [rate of return](https://corporatefinanceinstitute.com/resources/valuation/rate-of-return-guide/)
. It would be better if you also considered the associated level of risk. Risk refers to the likelihood that an asset’s or security’s financial performance will differ from what is expected.

A downside risk is a potential loss from your investment. Conversely, a potential financial gain is known as an upside risk.

Unfortunately, many performance metrics fail to account for the variation in the risk of an investment. They merely calculate their rates of return. But not so with the Sortino ratio. The indicator examines changes in the risk-free rate; hence, enabling investors to make more informed decisions.

The Sortino ratio is an improvement of the [Sharpe ratio](https://corporatefinanceinstitute.com/resources/career-map/sell-side/risk-management/sharpe-ratio-definition-formula/)
, another metric that helps individuals gauge the performance of an investment when it has been adjusted for risk. What sets the Sortino ratio apart is that it acknowledges the difference between upside and downward risks. More specifically, it provides an accurate rate of return, given the likelihood of downside risk, while the Sharpe ratio treats both upside and downside risks equally.

### How to Calculate the Sortino Ratio

The formula for calculating the Sortino ratio is:

##### Sortino Ratio = (Average Realized Return – Expected Rate of Return) / Downside Risk Deviation

The average realized return refers to the weighted mean return of all the investments in an individual’s portfolio. On the other hand, the expected rate of return (required return rate), or risk-free rate, is the return on long-term government securities.

For our example, we will use:

#### S = (R – T) / DR

Where:

*   **S** – Sortino ratio
*   **R** – Average realized return
*   **T** – Required rate of return
*   **DR** – Target downside deviation

Assume we’re given the following annual return rates: 4%, 10%, 15%, 20%, -5%, -2%, -6%, 8%, 23%, and 13%.

1\. The annual average return rate is **8%** = (4% + 10% + 15% + 20% + -5% + -2% + -6% + 8% + 23% + 13%) / 10

2\. Let’s say the target or required rate of return is **7%.** The additional return will then be 1% (8% – 7%). The value will make up the numerator in our equation.

3\. Next, find the standard deviation of downward risks (those with a negative value). We will not consider those with positive returns as their deviations are zero.

Thus, square the downside deviations, then find their average as follows:

(-5%)² = 0.0025

(-2%)² = 0.0004

(-6%)² = 0.0036

Average = (0.0025 + 0.0004 + 0.0036) / 10 = **0.00065**

5\. For the final outcome, find the standard deviation by getting the square root of the result:

√0.00065 = **0.0255**

It gives us:

R = 8%

T = 7%

DR = 0.0255

6\. Finally, compute the Sortino ratio as shown:

**S = (R – T) / DR**

R – T = 1% or 0.01

**S = 0.01 / 0.0255 = 0.392**

As a rule of thumb, a Sortino ratio of 2 and above is considered ideal. Thus, this investment’s 0.392 rate is unacceptable.

### When to Use the Sortino Ratio

Compared to the Sharpe ratio, the Sortino ratio is a superior metric, as it only accounts for the downside variability of risks. Such an analysis makes sense, as it enables investors to assess downside risks, which is what they should worry about. Upward risks (i.e., when an investment generates an unexpected financial gain) isn’t really a cause for concern.

By comparison, the Sharpe ratio treats upside and downside risks in the same way. It means that even those investments that produce gains are penalized, which should not be the case.

Therefore, the Sortino ratio should be used to assess the performance of high volatility assets, such as shares. In comparison, the Sharpe ratio is more suitable for analyzing low volatility assets, such as bonds.

### Key Considerations

While the Sortino ratio is an excellent metric for comparing investments, there are a couple of things you should take into account. One is the timeframe. It would help if you considered investments made over several years or at least those made during a complete [business cycle](https://corporatefinanceinstitute.com/resources/economics/business-cycle/)
.

Doing so allows you to account for both positive and negative stock returns. If you were to record only the positive stock returns, it would not be a true reflection of an investment.

The second factor entails the liquidity of the assets. A portfolio can be construed to show that it is less risky, but it may be because the underlying assets being held are illiquid.

For example, the prices of investments held in [privately-owned companies](https://www.forbes.com/lists/largest-private-companies/)
 rarely change; hence they are illiquid. If they are incorporated in the Sortino ratio, it will seem as if the risk-adjusted returns are favorable, yet they aren’t.

### Wrap Up

The Sortino ratio is almost identical to the Sharpe ratio, but it differs in one way. The Sharpe ratio accounts for risk-adjustments in investments with both positive and negative returns.

In contrast, the Sortino ratio examines risk-adjusted returns, but it only considers the downside risks. In such a way, the Sortino ratio is seen as a better indicator of risk-adjusted returns since it doesn’t consider upside risks, which aren’t a cause for concern to investors.

### Related Readings

Thank you for reading CFI’s guide on Sortino Ratio. To keep advancing your career, the additional resources below will be useful:

*   [Downside Risk](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/downside-risk/)
    
*   [Effective Yield](https://corporatefinanceinstitute.com/resources/fixed-income/effective-yield/)
    
*   [Risk-Adjusted Return Ratios](https://corporatefinanceinstitute.com/resources/wealth-management/risk-adjusted-return-ratios/)
    
*   [Treasury Bills (T-Bills)](https://corporatefinanceinstitute.com/resources/fixed-income/treasury-bills-t-bills/)
    
*   **[See all wealth management resources](https://corporatefinanceinstitute.com/topic/wealth-management/)
    **
*   **[See all capital markets resources](https://corporatefinanceinstitute.com/topic/capital-markets/)
    **

Get Certified for Financial Planning & Wealth Management Professional (FPWMP®)

Learn financial analysis & planning, portfolio management, and risk assessment.

[Learn More](https://corporatefinanceinstitute.com/certifications/financial-planning-and-wealth-management-fpwm-program/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fwealth-management%2Fsortino-ratio-2%2F&summary=Sortino+Ratio "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fwealth-management%2Fsortino-ratio-2%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)](https://twitter.com/intent/tweet?text=Sortino+Ratio&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fwealth-management%2Fsortino-ratio-2%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fwealth-management%2Fsortino-ratio-2%2F&summary=Sortino+Ratio "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/wealth-management/sortino-ratio-2/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)