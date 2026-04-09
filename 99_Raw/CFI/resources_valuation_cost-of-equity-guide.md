# Cost of Equity - Formula, Guide, How to Calculate Cost of Equity

**Source:** https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide

---

Table of Contents

*   [What is Cost of Equity?](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#what-is-cost-of-equity)
    

*   [How to Calculate Cost of Equity](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#how-to-calculate-cost-of-equity)
    
*   [Dividend Capitalization Model Example](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#dividend-capitalization-model-example)
    
*   [Cost of Equity Example in Excel (CAPM Approach)](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#cost-of-equity-example-in-excel-capm-approach)
    
*   [Download CFI's Free Cost of Equity Calculator](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#download-cfis-free-cost-of-equity-calculator)
    
*   [Cost of Equity vs Cost of Debt](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#cost-of-equity-vs-cost-of-debt)
    
*   [Cost of Equity vs WACC](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#cost-of-equity-vs-wacc)
    
*   [Cost of Equity in Financial Modeling](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#cost-of-equity-in-financial-modeling)
    
*   [Additional Resources](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/#additional-resources)
    

Cost of Equity
==============

The rate of return a shareholder requires for investing equity

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published March 29, 2020

Read Time 5 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

What is Cost of Equity?
-----------------------

Cost of Equity is the rate of return a company pays out to equity investors. A firm uses cost of equity to assess the relative attractiveness of investments, including both internal projects and external acquisition opportunities. Companies typically use a combination of equity and debt financing, with equity capital being more expensive.

![Cost of Equity - Conceptual business illustration with the words cost of equity](https://cdn.corporatefinanceinstitute.com/assets/cost-of-equity.jpeg)

### How to Calculate Cost of Equity

The cost of equity can be calculated by using the [CAPM (Capital Asset Pricing Model)](https://corporatefinanceinstitute.com/resources/valuation/what-is-capm-formula/)
 or Dividend Capitalization Model (for companies that pay out dividends).

#### CAPM (Capital Asset Pricing Model)

CAPM takes into account the riskiness of an investment relative to the market. The model is less exact due to the estimates made in the calculation (because it uses historical information).

CAPM Formula:

**E(Ri) = Rf +** **β****i** **\* \[E(Rm) – Rf\]**

Where:

*   E(Ri) = Expected return on asset i
*   Rf = Risk-free rate of return
*   βi = Beta of asset i
*   E(Rm) = Expected market return

##### Risk-Free Rate of Return

The return expected from a risk-free investment (if computing the expected return for a US company, the [10-year Treasury note](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield)
 could be used).

##### Beta

The measure of systematic risk (the volatility) of the asset relative to the market. Beta can be found online or calculated by using regression: dividing the covariance of the asset and market’s returns by the variance of the market.

**βi < 1**: Asset i is less volatile (relative to the market)

**βi = 1**: Asset i’s volatility is the same rate as the market

**βi > 1**: Asset i is more volatile (relative to the market)

##### Expected Market Return

This value is typically the average return of the market (which the underlying security is a part of) over a specified period of time (five to ten years is an appropriate range).

#### Dividend Capitalization Model

The Dividend Capitalization Model only applies to companies that pay dividends, and it also assumes that the dividends will grow at a constant rate. The model does not account for investment risk to the extent that CAPM does (since CAPM requires beta).

Dividend Capitalization Formula:

**Re = (D1 / P0) + g**

Where:

*   Re = Cost of Equity
*   D1 = Dividends/share next year
*   P0 \= Current share price
*   g = Dividend growth rate

##### Dividends/Share Next Year

Companies usually announce dividends far in advance of the distribution. The information can be found in company filings (annual and quarterly reports or through press releases). If the information cannot be located, an assumption can be made (using historical information to dictate whether the next year’s dividend will be similar).

##### Current Share Price

The share price of a company can be found by searching the ticker or company name on the exchange that the stock is being traded on, or by simply using a credible search engine.

##### Dividend Growth Rate

The Dividend Growth Rate can be obtained by calculating the growth (each year) of the company’s past dividends and then taking the average of the values.

The growth rate for each year can be found by using the following equation:

**Dividend Growth = (Dt/Dt-1) – 1**

Where:

*   Dt = Dividend payment of year t
*   Dt-1 = Dividend payment of year t-1 (one year before year t)

##### Example

Below are the dividend amounts paid every year by a company that has been operating for five years.

![Cost of Equity - Sample Dividend Table](https://cdn.corporatefinanceinstitute.com/assets/cost-of-equity.png)

The average of the growth rates is 2.41%.

### Dividend Capitalization Model Example

XYZ Co. is currently being traded at $5 per share and just announced a dividend of $0.50 per share, which will be paid out next year. Using historical information, an analyst estimated the dividend growth rate of XYZ Co. to be 2%. What is the cost of equity?

*   D1 = $0.50
*   P0 \= $5
*   g = 2%

**Re = ($0.50/$5) + 2%**

**Re = 12%**

The cost of equity for XYZ Co. is 12%.

### Cost of Equity Example in Excel (CAPM Approach)

Step 1: Find the RFR (risk-free rate) of the market

Step 2: Compute or locate the beta of each company

Step 3: Calculate the ERP (Equity Risk Premium)

**ERP = E(Rm) – Rf**

Where:

*   E(Rm) = Expected market return
*   Rf = Risk-free rate of return

Step 4: Use the CAPM formula to calculate the cost of equity.

**E(Ri) = Rf +** **β****i****\*ERP**

Where:

*   E(Ri) = Expected return on asset i
*   Rf = Risk free rate of return
*   βi = Beta of asset i
*   ERP (Equity Risk Premium) = E(Rm) – Rf

[![Screenshot of Cost of Equity Calculator Template in Excel](https://cdn.corporatefinanceinstitute.com/assets/cost-of-equity-calculator.png)](https://corporatefinanceinstitute.com/assets/Cost-of-Equity-Calculator.xlsx)

![Cost of Equity Formula - Sample Calculation](https://cdn.corporatefinanceinstitute.com/assets/cost-of-equity2.png)

The company with the highest beta sees the highest cost of equity and vice versa. It makes sense because investors must be compensated with a higher return for the risk of more volatility (a higher beta).

### Download CFI’s Free Cost of Equity Calculator

Complete the form below to download CFI’s free Cost of Equity Calculator now!  

   Download Now

### Cost of Equity vs Cost of Debt

The cost of equity is often higher than the cost of debt. Equity investors are compensated more generously because equity is riskier than debt, given that:

*   Debtholders are paid before equity investors (absolute priority rule).
*   Debtholders are guaranteed payments, while equity investors are not.
*   Debt is often secured by specific assets of the firm, while equity is not.
*   In exchange for taking less risk, debtholders have a lower expected rate of return.

### Cost of Equity vs WACC

The cost of equity applies only to equity investments, whereas the [Weighted Average Cost of Capital (WACC)](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
 accounts for both equity and debt investments.

Cost of equity can be used to determine the relative cost of an investment if the firm doesn’t possess debt (i.e., the firm only raises money through issuing stock).

The WACC is used instead for a firm with debt. The value will always be cheaper because it takes a weighted average of the equity and debt rates (and debt financing is cheaper).

### Cost of Equity in Financial Modeling

WACC is typically used as a discount rate for [unlevered free cash flow](https://corporatefinanceinstitute.com/resources/financial-modeling/unlevered-free-cash-flow/)
 (FCFF). Since WACC accounts for the cost of equity and cost of debt, the value can be used to discount the FCFF, which is the entire free cash flow available to the firm. It is important to discount it at the rate it costs to finance (WACC).

Cost of equity can be used as a discount rate if you use levered free cash flow (FCFE). The cost of equity represents the cost to raise capital from equity investors, and since FCFE is the cash available to equity investors, it is the appropriate rate to discount FCFE by.

### Additional Resources

CFI is a global provider of [financial modeling certification programs](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 for aspiring financial analysts working in investment banking, equity research, corporate development, and FP&A. To continue advancing your career, these additional CFI resources will be helpful:

*   [CCPPO Shares](https://corporatefinanceinstitute.com/resources/equities/ccppo-shares/)
    
*   [Return on Equity](https://corporatefinanceinstitute.com/resources/accounting/what-is-return-on-equity-roe/)
    
*   [Enterprise Value](https://corporatefinanceinstitute.com/resources/valuation/what-is-enterprise-value-ev/)
    
*   [Market Capitalization](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/resources/knowledge/finance/what-is-market-capitalization/)
    
*   [Cost of Equity Calculator](https://corporatefinanceinstitute.com/resources/financial-modeling/cost-of-equity-calculator/)
    
*   **[See all equities resources](https://corporatefinanceinstitute.com/topic/equities/)
    **
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcost-of-equity-guide%2F&summary=Cost+of+Equity "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcost-of-equity-guide%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)](https://twitter.com/intent/tweet?text=Cost+of+Equity&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcost-of-equity-guide%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcost-of-equity-guide%2F&summary=Cost+of+Equity "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/cost-of-equity-guide/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)