# Corporate Bond Valuation - Definition, Calculation, Formula

**Source:** https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation

---

Corporate Bond Valuation
========================

The process of determining a corporate bond’s fair value based on the present value of the bond’s coupon payments and the repayment of the principal

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published April 3, 2020

Read Time 4 minutes

What is Corporate Bond Valuation?
---------------------------------

Corporate bond valuation is the process of determining a corporate bond’s fair value based on the present value of the bond’s coupon payments and the repayment of the principal. Corporate bond valuation also accounts for the probability of the bond defaulting and not paying back the principal in full.

![Corporate Bond Valuation](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation.jpeg)

### What are Corporate Bonds?

Corporate bonds are bonds issued by [corporations](https://corporatefinanceinstitute.com/resources/accounting/what-is-corporation-overview/)
 to finance various activities, including operations, expansion, or M&A. Corporate bonds generally offer higher yields than government bonds because they usually come with a higher probability of default, making them riskier. Additionally, there are different types of corporate bonds that range in levels of risk and yield.

The valuation of corporate bonds is similar to that of any risky asset; it is dependent on the present value of future expected cash flows, discounted at a risk-adjusted rate (similar to a [DCF](https://corporatefinanceinstitute.com/resources/valuation/dcf-formula-guide/)
). However, the probability of default for the bond and the payout ratio if the bond defaults (ratio of face value received if bond defaults) must be factored into the valuation.

### How to Value a Corporate Bond (Probability Tree Method)

A common way to visualize the valuation of corporate bonds is through a probability tree.

![Corporate Bond Valuation - Probability Tree](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation1.png)

Consider the following example of a corporate bond:

*   3-year maturity
*   $1,000 face value
*   5% coupon rate ($50 coupon payments paid annually)
*   60 payout ratio ($600 default payout)
*   10 probability of default
*   5% risk-adjusted discount rate

![Corporate Bond Valuation - Sample Calculation](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation8.png)

The first step in valuing the bond is to find the expected value at each period. It is done by adding the product of the default payout and the [probability of default](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/probability-of-default/)
 (P) with the product of the promised payment (coupon payments and repayment of principal) and the probability of not defaulting (1-P).

![Corporate Bond Valuation - Step 1](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation3.png)

![Corporate Bond Valuation - Step 2](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation4.png)

After the expected values are calculated, they are discounted back to period 0 at a risk-adjusted discount rate (d) to calculate the bond’s price.

![Bond Price - Sample Calculation](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation5.png)

Where:

*   **d** = risk-adjusted discount rate

### Corporate Bond’s Yield

Corporate bonds tend to yield more than government bonds. The reason is that they carry more default risk. For a safe government bond, such as [U.S. Treasury Bills](https://corporatefinanceinstitute.com/resources/fixed-income/treasury-bills-t-bills/)
, the yield is comprised of the Federal Fund’s rate, an interest rate risk premium, and an inflation risk premium. However, for a corporate bond, investors also demand compensation for the risk of the corporation defaulting.

Some government bonds come offer default premiums; however, a U.S. treasury typically does not. Thus, a corporate bond’s yield also accounts for the default risk of the company. It is important to understand why the “tree method” to find a corporate bond’s price includes a calculation for the risk of the bond defaulting.

### How to Calculate a Corporate Bond’s Yield

After calculating the corporate bond’s price through the “tree method,” a final step can be taken to calculate the bond’s yield. To calculate the yield, set the bond’s price equal to the promised payments of the bond (coupon payments), divide it by one plus a rate, and solve for the rate. The rate will be the yield.

![Bond Yield - Sample Calculation](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation6.png)

An alternative way to solve a bond’s yield is by using the “Rate” function in Excel. Five inputs are needed to use the “Rate” function; time left until the bond matures in terms of the coupon payment periodicity (i.e., if coupons are paid annually, how many years until the bond matures), the value of the coupon payment, the price of the bond (as calculated with the “tree method”), the face value of the bond, and whether coupon payments are made at the beginning or end of a period.

![RATE Function (Excel)](https://cdn.corporatefinanceinstitute.com/assets/corporate-bond-valuation7.png)

### More Resources

Thank you for reading CFI’s guide to Corporate Bond Valuation. To keep learning and developing your knowledge base, please explore the additional relevant resources below:

*   [Cost of Debt](https://corporatefinanceinstitute.com/resources/valuation/cost-of-debt/)
    
*   [Default Risk Premium](https://corporatefinanceinstitute.com/resources/fixed-income/default-risk-premium/)
    
*   [Par Value](https://corporatefinanceinstitute.com/resources/accounting/par-value-overview/)
    
*   [Fixed Income Fundamentals Course](https://corporatefinanceinstitute.com/course/introduction-to-fixed-income/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

![](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)

**Get In-Demand Finance Certifications**

[Learn More](https://corporatefinanceinstitute.com/pricing/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcorporate-bond-valuation%2F&summary=Corporate+Bond+Valuation "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcorporate-bond-valuation%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)](https://twitter.com/intent/tweet?text=Corporate+Bond+Valuation&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcorporate-bond-valuation%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcorporate-bond-valuation%2F&summary=Corporate+Bond+Valuation "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/corporate-bond-valuation/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)