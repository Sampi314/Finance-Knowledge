# What is Beta in Finance? Formula & Examples

**Source:** https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide

---

Table of Contents

*   [What is Beta in Finance?](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#what-is-beta-in-finance)
    
*   [Examples of Beta in Action](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#examples-of-beta-in-action)
    
*   [Beta Formula & How to Calculate Beta](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#beta-formula-how-to-calculate-beta)
    
*   [Download the Free Template](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#download-the-free-template)
    
*   [What are Equity Beta and Asset Beta?](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#what-are-equity-beta-and-asset-beta)
    
*   [Levered Beta vs Unlevered Beta](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#levered-beta-vs-unlevered-beta)
    

*   [Calculation of Levered Beta](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#calculation-of-levered-beta)
    

*   [Interpreting Beta](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#interpreting-beta)
    
*   [Why Beta Matters](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#why-beta-matters)
    

*   [Limitations of Beta](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#limitations-of-beta)
    

*   [Additional Resources](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/#additional-resources)
    

Beta
====

Beta is a financial metric used to evaluate a stock’s volatility and risk relative to the broader market — essential for understanding investment performance.

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Reviewed by [Jeff Schmidt](https://corporatefinanceinstitute.com/author/jeffrey-schmidt/)

Updated March 12, 2026

Read Time 6 minutes

What is Beta in Finance?
------------------------

The beta (β) of an investment security (i.e., a stock) is a measurement of its volatility of returns relative to the entire market. It is used as a measure of risk and is an integral part of the Capital Asset Pricing Model ([CAPM](https://corporatefinanceinstitute.com/resources/valuation/what-is-capm-formula/)
). A company with a higher beta has greater risk and also greater expected returns.

In finance, beta refers to a security’s sensitivity to systematic risk, or market risk. It tells us how much a stock’s price is likely to move in response to market changes. Beta is typically benchmarked against a broad market index, like the [S&P 500](https://corporatefinanceinstitute.com/resources/equities/sp-500-index/)
.

The beta coefficient can be interpreted as follows:

*   **β = 1:** exactly as volatile as the market
*   **β > 1:** more volatile than the market (higher risk and potential return)
*   **β < 1 (but > 0):** less volatile than the market
*   **β = 0:** uncorrelated to the market
*   **β < 0:** negatively correlated to the market

Here is a chart illustrating the data points from the β calculator (below):

![Scatter plot showing stock returns against market returns with a beta of 1.21. The upward-sloping trendline illustrates a positive correlation, indicating higher stock volatility relative to the market.](https://cdn.corporatefinanceinstitute.com/assets/beta-chart-example.png)

_Note: Beta measures only market-related risk, not total volatility. A stock can have high total volatility but a low beta if its price swings are largely unrelated to the market._

Examples of Beta in Action
--------------------------

**High β** – A company with a β that’s greater than 1 is more volatile than the market. For example, a high-risk technology company with a β of 1.75 would have returned 175% of what the market returned in a given period (typically measured weekly).

**Low β** – A company with a β that’s lower than 1 is less volatile than the whole market. As an example, consider an electric utility company with a β of 0.45, which would have returned only 45% of what the market returned in a given period.

**Negative β** – A company with a negative β is negatively correlated to the returns of the market. For example, a gold company with a β of -0.2, which would have returned -2% when the market was up 10%.

Beta Formula & How to Calculate Beta
------------------------------------

Beta can be calculated using historical price data and regression analysis, or with Excel’s SLOPE function. Here is the general beta equation:

#### **Beta = Covariance (Re, Rm) / Variance (Rm)**

Where:

*   **Re** = Return of the asset
*   **Rm** = Return of the market

Below is an Excel β calculator that you can download and use to calculate β on your own in Excel using the SLOPE function.

**Steps to Calculate Beta in Excel:**

1.  Obtain the weekly prices of the stock.
2.  Obtain the weekly prices of the market index (i.e., S&P 500 Index).
3.  Calculate the weekly returns of the stock.
4.  Calculate the weekly returns of the market index.
5.  Use the SLOPE function and select the weekly returns of the market and the stock, each as their own series:

a. =SLOPE(stock returns, market returns)

Congrats! The output from the SLOPE function is the β.

![Screenshot of an Excel-based beta calculator comparing the daily closing prices for the index and an individual stock to calculate beta. Final beta value is calculated as 0.9085. The beta values are visualized in a scatter plot.](https://cdn.corporatefinanceinstitute.com/assets/what-is-beta-1-2048x1152.png)

Download the Free Template
--------------------------

Want to try it yourself? Download CFI’s free beta calculator template.

   Download Now

What are Equity Beta and Asset Beta?
------------------------------------

Levered beta, also known as equity beta or stock beta, is the volatility of returns for a stock, taking into account the impact of the company’s leverage from its capital structure. It compares the volatility (risk) of a levered company to the risk of the market.

Levered beta includes both [business risk](https://corporatefinanceinstitute.com/resources/career-map/sell-side/risk-management/what-is-systemic-risk/)
 and the risk that comes from taking on [debt](https://corporatefinanceinstitute.com/resources/fixed-income/market-value-of-debt/)
. It is also commonly referred to as “equity beta” because it is the volatility of an equity based on its [capital structure](https://corporatefinanceinstitute.com/resources/accounting/capital-structure-overview/)
.

Asset beta, or [unlevered beta](https://corporatefinanceinstitute.com/resources/valuation/unlevered-beta-asset-beta/)
, on the other hand, shows the risk of an unlevered company relative to the market. It includes business risk but does not include leverage risk.

![Formula for calculating levered or equity beta: Levered Beta = Unlevered Beta × [1 + (1 – Tax Rate) × (Debt / Equity)].](https://cdn.corporatefinanceinstitute.com/assets/levered-beta.png)

Levered Beta vs Unlevered Beta
------------------------------

Levered beta (equity beta) is a measurement that compares the volatility of returns of a company’s stock against that of the broader market. In other words, it is a measure of risk, and it includes the impact of a company’s capital structure and leverage. Equity beta allows investors to assess how sensitive a security might be to macro-market risks. For example, a company with a β of 1.5 denotes returns that are 150% as volatile as the market it is being compared to.

When you look up a company’s beta on [Bloomberg](https://www.bloomberg.com/)
, the default number you see is levered, and it reflects the debt of that company. Since each company’s capital structure is different, an analyst will often want to look at how “risky” the assets of a company are, regardless of the percentage of its debt or equity funding.

The higher a company’s debt or leverage, the more of its earnings that are committed to servicing the debt. As a company adds more debt, the uncertainty of the company’s future earnings also rises. It increases the risk associated with the company’s stock, but it is not a result of the market or industry risk. Therefore, by removing the financial leverage (debt impact), the unlevered beta can capture the risk of the company’s assets only.

### Calculation of Levered Beta

There are two ways to estimate the levered beta of a stock. The first, and simplest, way is to use the company’s historical β or just select the company’s beta from Bloomberg. The second, and more popular, way is to make a new estimate for β using public company comparables. To use the comparables approach, the β of comparable companies is taken from Bloomberg and the unlevered beta for each company is calculated.

#### Unlevered β = Levered β / ((1 + (1 – Tax Rate) \* (Debt / Equity))

Levered beta includes both business risk and the risk that comes from taking on debt. However, since different firms have different capital structures, unlevered beta is calculated to remove additional risk from debt in order to view pure business risk. The average of the unlevered betas is then calculated and re-levered based on the capital structure of the company that is being valued.

#### Levered Beta = Unlevered Beta \* ((1 + (1 – Tax Rate) \* (Debt / Equity))

**Note:** In most cases, the firm’s current capital structure is used when β is re-levered. However, if there is information that the firm’s capital structure might change in the future, then β would be re-levered using the firm’s target capital structure.

Interpreting Beta
-----------------

A security’s β should only be used when its high R-squared value is higher than the benchmark. The R-squared value measures the percentage of variation in the share price of a security that can be explained by movements in the benchmark index. For example, a gold ETF will show a low β and R-squared in relation to a benchmark equity index, as gold is negatively correlated with equities.

*   A β of 1 means the stock moves in line with the market.
*   A β greater than 1 means the stock is more volatile than the market.
*   A β less than 1 indicates less volatility than the market.
*   A negative β implies an inverse relationship with the market — rare, but sometimes seen with gold or hedge-focused assets.

For example, the β of most technology companies tends to be higher than 1. Also, a company with a β of 1.30 is theoretically 30% more volatile than the market. Similarly, a company with a β of 0.79 is theoretically 21% less volatile than the market.

For a company with a negative β, it means that it moves in the opposite direction of the market. Theoretically, this is possible; however, it is extremely rare to find a stock with a negative β.

Why Beta Matters
----------------

Understanding beta helps investors:

*   Assess systematic risk
*   Build diversified portfolios
*   Match investments to risk tolerance
*   Make informed investment decisions
*   Compare individual stocks to market volatility
*   Identify high- or low-risk securities for their strategy

Beta is especially valuable for comparing a stock’s volatility to the broader market and estimating future performance under different economic scenarios. Whether you’re evaluating long-term investments, balancing portfolio risk, or analyzing the performance of sector-specific assets, beta provides insight into how a security might behave in various market conditions.

### Limitations of Beta

While beta is a powerful tool, it has some limitations:

*   Based on historical data, which may not predict future movements
*   Doesn’t capture unsystematic (company-specific) risk
*   Can be misleading if the R-squared value is low
*   Doesn’t account for changes in capital structure

Beta should be used in combination with other financial metrics and qualitative factors to provide a robust basis for investment analysis.

Connect what you just learned to a clear career path with CFI’s role‑based courses and certification programs.

[Advance Your Career](https://corporatefinanceinstitute.com/pricing/)

Additional Resources
--------------------

Thank you for reading CFI’s guide to beta (β) of an investment security. To continue learning and advancing your career, these additional resources will be helpful:

*   [Types of Valuation Multiples](https://corporatefinanceinstitute.com/resources/valuation/types-of-valuation-multiples/)
    
*   [Multi-Factor Model](https://corporatefinanceinstitute.com/resources/data-science/multi-factor-model/)
    
*   [Leverage Ratios](https://corporatefinanceinstitute.com/resources/accounting/leverage-ratios/)
    
*   [Non-Marginable Securities](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/non-marginable-securities/)
    
*   [Valuation Methods](https://corporatefinanceinstitute.com/resources/valuation/valuation/)
    

[**See all Capital Markets resources**](https://corporatefinanceinstitute.com/resources/?topics=131719)

**[See all Valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
**

Get Certified for Capital Markets (CMSA®)

From equities and fixed income to derivatives, the CMSA certification bridges the gap from where you are now to where you want to be — a world-class capital markets analyst.

[Learn More](https://corporatefinanceinstitute.com/certifications/capital-markets-securities-analyst-cmsa/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fwhat-is-beta-guide%2F&summary=Beta "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fwhat-is-beta-guide%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)](https://twitter.com/intent/tweet?text=Beta&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fwhat-is-beta-guide%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fwhat-is-beta-guide%2F&summary=Beta "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/what-is-beta-guide/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)