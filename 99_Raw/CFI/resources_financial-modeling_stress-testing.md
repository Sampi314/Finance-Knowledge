# Stress Test – Overview, Modeling, Main Purpose

**Source:** https://corporatefinanceinstitute.com/resources/financial-modeling/stress-testing

---

Stress Test – Financial Modeling
================================

Finding the flaws in a financial model

Written by [Jeff Schmidt](https://corporatefinanceinstitute.com/author/jeffrey-schmidt/)

Published April 12, 2020

Read Time 3 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

Why Stress Test a Financial Model?
----------------------------------

The last key step in preparing a financial model is stress testing it. The ability to stress test a [financial model](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-financial-modeling/)
 and find any flaws within it is a useful skill in improving the quality of a financial model. Stress testing also ensures no errors will occur in the future when the model has been handed off to the final user.

This final step is one that is often overlooked, even though stress testing a financial model prevents dissatisfied clients, managers, and executives.

### How to stress test in financial modeling?

One of the easiest methods of stress testing is to test the formula logic built into the calculations of the financial model. A simple sanity test will reveal whether the resulting values make sense. A more robust extension of this test is to fill the formula down or to the right into adjacent cells, and see whether the change properly flows through. Does the filled down formula result in appropriate values? If not, that may mean that there is an overlooked reference within the formula that must be adjusted. As shown in the image below, one of the lines in the statement is not referencing correctly. Stress testing reveals these errors.

![stress test errors](https://cdn.corporatefinanceinstitute.com/assets/stress-testing-errors.png)

Because a financial model relies on the use of assumptions to calculate projected values, it becomes prudent to also stress test the formulas surrounding the assumptions. Test all probable and possible values of the assumptions and see if that crashes the formula. Decrease the assumption, increase it, flip its sign, or make it zero, and see whether the formulas still calculate properly. If, in any case, the formula errors or becomes nonsensical, a further look into the formula logic may be required for that specific assumption.

If multiple users operate within the financial model, check the output values against their copy or version of the model. Are the assumptions similar and do the results match exactly? This is also a good time to ensure that [proper formatting](https://corporatefinanceinstitute.com/resources/knowledge/modeling/financial-model-formatting/)
 has carried over into the new iterations of the model.

### Error checking

Because of the structured nature of the [core statements,](https://corporatefinanceinstitute.com/resources/accounting/three-financial-statements/)
 it is not too difficult to ensure the data and calculations are correct. Below are just a few types of checks that can be placed within an Excel model to ensure that values are adding up correctly.

*   Does the [balance sheet](https://corporatefinanceinstitute.com/resources/accounting/balance-sheet/)
     add up? Do Assets minus Liabilities minus Equity equal zero?
    
*   Does the change to [retained earnings](https://corporatefinanceinstitute.com/resources/accounting/retained-earnings-guide/)
     in the current period equal [net income](https://corporatefinanceinstitute.com/resources/accounting/what-is-net-income/)
     minus dividends?
    
*   Does the ending [cash balance](https://corporatefinanceinstitute.com/resources/accounting/cash-equivalents/)
     in the [cash flow equal](https://corporatefinanceinstitute.com/resources/accounting/cash-flow/)
     the cash balance in the balance sheet?
    
*   Do ending values in the supporting schedules match their corresponding values in the core statements?
    
*   One master error checks to determine whether all of the above are resulting correctly.
    

Placing these checks within a financial model enables the user to ensure calculations are being done correctly, and that no formula logic has been made erroneously. The more checks in place, the more secure the financial model is from errors appearing.

### Read more about financial modeling!

See the following free CFI resources to learn more.

*   [Net working capital](https://corporatefinanceinstitute.com/resources/knowledge/finance/what-is-net-working-capital/)
    
*   [Debt Schedule](https://corporatefinanceinstitute.com/resources/financial-modeling/debt-schedule/)
    
*   [Depreciation Schedule](https://corporatefinanceinstitute.com/resources/financial-modeling/depreciation-schedule/)
    
*   [What Makes a Good Financial Model?](https://corporatefinanceinstitute.com/resources/financial-modeling/free-financial-modeling-guide/)
    
*   **[See all financial modeling resources](https://corporatefinanceinstitute.com/topic/financial-modeling/)
    **
*   **[See all capital markets resources](https://corporatefinanceinstitute.com/topic/capital-markets/)
    **

### Analyst Certification FMVA® Program

Below is a break down of [subject weightings](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 in the FMVA® financial analyst program. As you can see there is a heavy focus on financial modeling, finance, Excel, business valuation, budgeting/forecasting, PowerPoint presentations, accounting and business strategy.

[![Financial Analyst certification curriculum](https://corporatefinanceinstitute.com/resources/financial-modeling/stress-testing)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

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
    

### Excel Tutorial

To master the art of Excel, check out CFI’s [Excel Crash Course](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
, which teaches you how to become an Excel power user. Learn the most important formulas, functions, and shortcuts to become confident in your financial analysis.

[![Excel Course](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 111.156 25.5938" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

Launch [CFI’s Excel Crash Course](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
 now to take your career to the next level and move up the ladder!

*   Share this article
*   [![Share on LinkedIn](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fstress-testing%2F&summary=Stress+Test+%E2%80%93+Financial+Modeling "Share on LinkedIn")
    
*   [![Share on Facebook](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fstress-testing%2F "Share on Facebook")
    
*   [![Share on Twitter](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://twitter.com/intent/tweet?text=Stress+Test+%E2%80%93+Financial+Modeling&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fstress-testing%2F "Share on Twitter")
    
*   [![Share on WhatsApp](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fstress-testing%2F&summary=Stress+Test+%E2%80%93+Financial+Modeling "Share on WhatsApp")
    
*   [![Copy link](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/resources/financial-modeling/stress-testing/ "Copy link")
    

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

![](https://bat.bing.com/action/0?ti=26068827&tm=gtm002&Ver=2&mid=00a74099-9cf4-4e9b-a510-97e1cab60161&bo=2&sid=b889e5b022bd11f1a408affc7db738c0&vid=b889fca022bd11f1a5fb21a70e0c05a2&vids=1&msclkid=N&pi=0&lg=en-US&sw=1280&sh=800&sc=24&nwd=1&tl=Stress%20Test%20%E2%80%93%20Overview,%20Modeling,%20Main%20Purpose&p=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fstress-testing%2F&r=&lt=2816&evt=pageLoad&sv=2&asc=G&cdb=AQcT&rn=24921)

![](https://www.ojrq.net/p/?return=&cid=23723&tpsync=no&auth=)