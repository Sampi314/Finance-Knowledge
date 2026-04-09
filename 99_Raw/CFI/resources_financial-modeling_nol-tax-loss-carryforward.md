# Net Operating Loss (NOL) - Tax Carryforward Rules

**Source:** https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward

---

Table of Contents

*   [What is an NOL/Tax Loss Carryforward?](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#what-is-an-nol-tax-loss-carryforward)
    
*   [What is the Purpose of an NOL/Tax Loss Carryforward?](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#what-is-the-purpose-of-an-nol-tax-loss-carryforward)
    

*   [Example if firms could NOT carry forward losses](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#example-if-firms-could-not-carry-forward-losses)
    

*   [Building a Tax Loss Carryforward Schedule](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#building-a-tax-loss-carryforward-schedule)
    

*   [Steps to create a tax loss carryforward schedule in Excel](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#steps-to-create-a-tax-loss-carryforward-schedule-in-excel)
    
*   [Example tax loss carryforward](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#example-tax-loss-carryforward)
    

*   [Treatment of NOLs in an Acquisition](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#treatment-of-nols-in-an-acquisition)
    

*   [Basics of IRC 382](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#basics-of-irc-382)
    
*   [Limitations of IRC 382](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#limitations-of-irc-382)
    
*   [Additional Resources](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward#additional-resources)
    

NOL Tax Loss Carryforward
=========================

Using prior losses to lower future taxes

Written by [Tim Vipond, FMVA](https://corporatefinanceinstitute.com/author/tim-vipond/)

Published April 2, 2020

Read Time 4 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

What is an NOL/Tax Loss Carryforward?
-------------------------------------

A net operating loss (NOL) or tax loss carryforward is a tax provision that allows firms to carry forward losses from prior years to offset future profits, and, therefore, lower future [income taxes](https://corporatefinanceinstitute.com/resources/accounting/accounting-for-income-taxes/)
. The way a tax loss carryforward works is that a schedule is generated to track all cumulative losses, which are then applied in future years to reduce profits until the balance in the TLCF is zero. An NOL carryforward schedule is commonly used in [financial modeling](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-financial-modeling/)
.

![Tax Loss Carryforward - Image of Tax Time written on pink sticker note over tax forms](https://cdn.corporatefinanceinstitute.com/assets/tax-loss.jpg)

### Key Highlights

*   **A net operating loss (NOL) or tax loss carryforward is a tax provision that allows firms to carry forward losses from prior years to offset future profits, and, therefore, lower future income taxes.**
*   **Tax loss carryforwards exist so that the total lifetime taxes for a firm will, in theory, be the same no matter how their profits and losses are spread out.**
*   **Typically, when an acquisition is structured as a stock acquisition, the acquiring company obtains the ability to use the target’s NOLs going forward. However, there may be limits placed on the usage of these acquired NOLs. For example, in the United States, the usage of acquired NOLs is governed by Internal Revenue Code (IRC) Section 382.**

What is the Purpose of an NOL/Tax Loss Carryforward?
----------------------------------------------------

Tax loss carryforwards exist so that the total lifetime taxes for a firm will, in theory, be the same no matter how their profits and losses are spread out.

### Example if firms could NOT carry forward losses

A company that had a loss of $10 million in 2018 and a profit of $10 million in 2019 with a 30% tax rate would pay zero tax in 2018 and $3 million in 2019. Its total profit before tax in 2018 and 2019 combined was zero, yet it paid $3 million in taxes.

Compare that to a different company that also had $0 of profit in 2018 and $0 of profit in 2019. This company would pay zero taxes and had a total pre-tax profit of $0.

So why would the first company pay $3 million in taxes while the second company paid none? The first company is much worse off due to the distribution and timing of its profits.

To address this issue, tax loss carryforwards were created.

Building a Tax Loss Carryforward Schedule
-----------------------------------------

The easiest way to keep track of a TLCF schedule is to create a model in Excel. In the screenshot below, you can see how a financial analyst creates the schedule.

![](https://cdn.corporatefinanceinstitute.com/assets/NOL-Steps.png)

### Steps to create a tax loss carryforward schedule in Excel

1.  Calculate the firm’s [Earnings Before Tax](https://corporatefinanceinstitute.com/resources/accounting/earnings-before-tax-ebt/)
     (EBT) for each year
2.  Create a line that’s the opening balance of carryforward losses
3.  Create a line that’s equal to the current period loss, if any
4.  Create a subtotal line
5.  Create a line to calculate the loss used in the period with a formula stating that “if the current period has taxable income, reduce it by the lesser of the taxable income in the period and the remaining balance in the TLCF.
6.  Create a closing balance line equal to the subtotal less any loss used in the period
7.  Next period’s opening balance equals the last period’s closing balance

### Example tax loss carryforward

Below is a screenshot of a tax loss carryforward schedule built in Excel. This is taken from CFI’s [e-commerce/startup financial modeling course](https://corporatefinanceinstitute.com/course/ecommerce-startup-financial-model-valuation/)
, in which a company has the ability to carry forward losses due to the significant losses expected to be incurred by the business in its first few years of operation.

![](https://cdn.corporatefinanceinstitute.com/assets/eCommerce-Screenshot.png)

The best way to learn how to build a TLCF schedule is by practicing. By using the example provided, you can see how it was designed and test yourself to create your own in Excel. If you want a completed example to work with, check out CFI’s [financial modeling templates](https://corporatefinanceinstitute.com/resources/financial-modeling/nopat-template/)
 library of completed models from beginner to advanced.

Treatment of NOLs in an Acquisition
-----------------------------------

Typically, when an acquisition is structured as a [stock acquisition](https://corporatefinanceinstitute.com/resources/valuation/stock-acquisition/)
, the acquiring company obtains the ability to use the target’s NOLs going forward. However, there may be limits placed on the usage of these acquired NOLs. For example, in the United States, the usage of acquired NOLs is governed by Internal Revenue Code (IRC) Section 382.

### Basics of IRC 382

There are two main components of Section 382 — limitation and ownership change. An ownership change occurs when one or more 5% shareholders increase their ownership, in aggregate, by more than 50% over a testing period. Obviously, an acquisition will trigger a change in ownership.

### Limitations of IRC 382

After the acquisition, the acquiring company may deduct the acquired NOLs against its taxable income after calculating the Section 382 base limitation. The formula used in calculating the base limitation amount is:

**Fair Market Value of the Target Corporation Stock x Federal Long-Term Tax Exempt Rate = Base Limitation Amount**

When calculating the base limitation amount, the fair market value depends on potential adjustments as set forth in Internal Revenue Service (IRS) regulations. The IRS publishes the federal long-term tax-exempt rate monthly.

The base limitation formula drastically limits the usage of acquired NOLs.

Learn more by reading a helpful [guide on Internal Revenue Code 382](https://www.law.cornell.edu/uscode/text/26/382)
 from Cornell Law School.

Always consult a professional tax advisor before filing any tax forms.

### Additional Resources

*   [Deferred Tax Liability](https://corporatefinanceinstitute.com/resources/accounting/deferred-tax-liability-asset/)
    
*   [Tax Havens](https://corporatefinanceinstitute.com/resources/economics/what-is-tax-haven/)
    
*   [Tax Shields](https://corporatefinanceinstitute.com/resources/valuation/tax-shield/)
    
*   **[See all financial modeling resources](https://corporatefinanceinstitute.com/topic/financial-modeling/)
    **
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

### Analyst Certification FMVA® Program

Below is a break down of [subject weightings](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 in the FMVA® financial analyst program. As you can see there is a heavy focus on financial modeling, finance, Excel, business valuation, budgeting/forecasting, PowerPoint presentations, accounting and business strategy.

[![Financial Analyst certification curriculum](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

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
    

### Accounting Crash Courses

Learn accounting fundamentals and how to read financial statements with CFI’s [online accounting classes](https://corporatefinanceinstitute.com/collections/accounting/)
.  
These courses will give you the confidence to perform world-class financial analyst work. Start now!

[![Accounting courses online](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 202.781 25.5938" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/collections/accounting/)

Boost your confidence and master accounting skills effortlessly with CFI’s expert-led courses! Choose CFI for unparalleled industry expertise and hands-on learning that prepares you for real-world success.

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn MoreLearn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fnol-tax-loss-carryforward%2F&summary=NOL+Tax+Loss+Carryforward "Share on LinkedIn")
    
*   [![Share on Facebook](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fnol-tax-loss-carryforward%2F "Share on Facebook")
    
*   [![Share on Twitter](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://twitter.com/intent/tweet?text=NOL+Tax+Loss+Carryforward&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fnol-tax-loss-carryforward%2F "Share on Twitter")
    
*   [![Share on WhatsApp](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fnol-tax-loss-carryforward%2F&summary=NOL+Tax+Loss+Carryforward "Share on WhatsApp")
    
*   [![Copy link](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/resources/financial-modeling/nol-tax-loss-carryforward/ "Copy link")
    

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