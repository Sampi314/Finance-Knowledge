# Canadian Equity Risk Premium - How to Calculate Canada's ERP

**Source:** https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium

---

Table of Contents

*   [What is Equity Risk Premium?](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/#what-is-equity-risk-premium)
    

*   [Forecasting the Canadian Equity Risk Premium](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/#forecasting-the-canadian-equity-risk-premium)
    
*   [Related Readings](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/#related-readings)
    

Canadian Equity Risk Premium
============================

The excess return that investing in a Canadian bond provides over a risk-free rate

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published March 15, 2018

Read Time 5 minutes

What is Equity Risk Premium?
----------------------------

Equity Risk Premium is defined as the excess return that investing in [equities](https://corporatefinanceinstitute.com/resources/equities/what-is-a-stock/)
 provides over a risk-free rate. The variable is a central component in almost every [risk-reward model](https://corporatefinanceinstitute.com/resources/financial-modeling/types-of-financial-models/)
 used in finance today, but the way that it is measured may not be appropriate for forward-looking analysis. This guide will look at the Canadian equity risk premium.

We can deconstruct the equity risk premium (the expected return on the [S&P/TSX Composite Index](https://en.wikipedia.org/wiki/S%26P/TSX_Composite_Index)
 less the expected return on a riskless bond) in order to estimate the components:

![](https://cdn.corporatefinanceinstitute.com/assets/equity-risk-premium.png)

E(rb) is the expected return on a Government of Canada bond with a maturity of 1 year (alternatively, any maturity equal to the forecast horizon appropriate for the security you wish to value) and E(rs) is the expected return on the S&P TSX Composite index. The expected return can be expressed by the following equation:

![](https://cdn.corporatefinanceinstitute.com/assets/expected-return.png)

Where:

*   D1 = Total dividends paid on the index
*   R1 = Total amount spent on stock repurchases in the index
*   MVE0 = Total market value of the index’s equity at the start of the period
*   MVE1 = Total market value of the index’s equity at the end of the period

We can further define _R1_ _\=_ Δ(_S_) \* _k,_ where:

*   Δ(_S_) = _S1 – S_0
*   k = price at which shares are repurchased (assume 2% premium)
*   S0 = number of shares outstanding at the start of the period
*   S1 = number of shares outstanding at the end of the period

Reorganizing the formula above by expanding the denominator, we can break down the expected return on the S&P/TSX Composite Index into two components:

![](https://cdn.corporatefinanceinstitute.com/assets/expected-return-SP-TSX-Composite-Index.png)

The income return consists of the dividend yield and the repurchase adjustment:

![](https://cdn.corporatefinanceinstitute.com/assets/income-return.png)

Using data from [Bloomberg](https://corporatefinanceinstitute.com/resources/?topics=111064)
, the annual dividend yield (calculated as a geometric average of monthly recorded yields) is approximately 3.5%, and the repurchase adjustment (assumed with a 2% repurchase premium) is negligible at slightly higher than 0.1%.

The annual capital gains return as of the year ended 2017 is 8.5%**.** The number can be found by taking a normal return on the S&P/TSX composite index over the year. The return is consistent with the Bloomberg S&P/TSX Composite index price return.

Adding these components together, we get a YTD total return of approximately 12%. The number is consistent with the Bloomberg S&P/TSX Composite Index total return (including dividends).

![Bloomberg S&P/TSX Composite Index total return ](https://cdn.corporatefinanceinstitute.com/assets/canadian-equity-risk-premium4.png)

The trend-line in the chart above illustrates the point that the average expected return on the S&P/TSX Composite Index has been declining. The average total return on the TSX Composite can be a proxy for the health of the Canadian economy. With a trend of declining expected returns, we can conclude that it is becoming increasingly challenging to find above-average returns in the Canadian equity market.

This phenomenon can be explained by any number of factors. Since we are analyzing the Canadian equity market, we know that the Canadian dollar is highly correlated with the price of oil. From the start of 2014 to the end of 2015, the crude oil price per barrel fell from a high of US$109.78 per barrel to a low of US$29.64 per barrel. Furthermore, the Canadian household’s debt to disposable income ratio rose from approximately 140% to 175% over the past 10 years, which may have contributed to the pressure on the overall Canadian economy.

### Forecasting the Canadian Equity Risk Premium

From the above analysis, we note that the key component in expected returns is the capital gain return. By replacing P0 = E0 x p0 (where p0 = P0/E0, i.e., the current trailing P/E ratio) and P1 = E1 x p1 (where p1 = P1/E1, i.e., the end-of-period P/E ratio), we can express the capital gain return in terms of earnings growth and as a function of the current and end-of-period P/E ratios:

![](https://cdn.corporatefinanceinstitute.com/assets/capital-gain-return.png)

Where:

*   g = Expected real growth in earnings (1.1% – proxy: GDP growth – Q2/2017)
*   i = Expected inflation (1.8% – Q2/2017)
*   rp = Re-pricing effect = p1/p0 -1 (10-year average annual change = 1.2%, Source: Bloomberg)

Therefore:

![](https://cdn.corporatefinanceinstitute.com/assets/capital-gain-return-earnings-growth.png)

Where d1/P0 = $424.31(1+0.0025)/$16,150 = 2.6% (growing at 0.25% CAGR since October 2002) and ra = repurchase adjustment = ![Repurchase Adjustment](https://cdn.corporatefinanceinstitute.com/assets/canadian-equity-risk-premium7.png), which we can assume to be negligible at a 2% premium. With a short-term GOC bond yield (1-3 of 1.5%, we can estimate the near-term ERP for the Canadian Equity Market by simply adding the terms of the ERP equation:

**Canadian ERP = 2.6% + 1.1% + 1.8% + 1.2% _–_ 1.5% = 5.2%**

The above method can be applied to any major stock market index to solve for the intrinsic equity risk premium for benchmarking expected equity returns over a risk-free rate.

### Related Readings

Thank you for reading this guide to the Canadian equity risk premium. CFI is the official provider of the [Financial Modeling & Valuation Analyst (FMVA)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 certification program for financial analysts. To continue advancing your career, these additional resources will be helpful:

*   [Bond Pricing](https://corporatefinanceinstitute.com/resources/fixed-income/bond-pricing/)
    
*   [Capital Asset Pricing Model (CAPM)](https://corporatefinanceinstitute.com/resources/valuation/what-is-capm-formula/)
    
*   [Cost of Debt](https://corporatefinanceinstitute.com/resources/valuation/cost-of-debt/)
    
*   [Debt Capital Markets](https://corporatefinanceinstitute.com/resources/career-map/sell-side/investment-banking/dcm/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcanadian-equity-risk-premium%2F&summary=Canadian+Equity+Risk+Premium "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcanadian-equity-risk-premium%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)](https://twitter.com/intent/tweet?text=Canadian+Equity+Risk+Premium&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcanadian-equity-risk-premium%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcanadian-equity-risk-premium%2F&summary=Canadian+Equity+Risk+Premium "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/canadian-equity-risk-premium/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)