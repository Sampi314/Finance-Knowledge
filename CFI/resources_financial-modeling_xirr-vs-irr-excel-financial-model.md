# XIRR vs IRR - Why You Must Use XIRR in Excel Financial Modeling

**Source:** https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model

---

Table of Contents

*   [What is XIRR vs IRR in Excel?](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#what-is-xirr-vs-irr-in-excel)
    

*   [What is Internal Rate of Return (IRR)?](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#what-is-internal-rate-of-return-irr)
    
*   [What is IRR in Excel?](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#what-is-irr-in-excel)
    
*   [What is XIRR in Excel?](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#what-is-xirr-in-excel)
    
*   [Example of XIRR vs IRR Calculation](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#example-of-xirr-vs-irr-calculation)
    
*   [Download the Free Template](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#download-the-free-template)
    
*   [Additional Resources](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model#additional-resources)
    

XIRR vs IRR
===========

Why you should always use XIRR instead of IRR in financial modeling

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published April 7, 2020

Read Time 3 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

What is XIRR vs IRR in Excel?
-----------------------------

In financial modeling and valuation, it’s critical to understand why to use XIRR vs IRR.  Using the simple =[IRR function in Excel](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
 can be misleading, as it assumes all the time periods in a series of cash flows are equal.  This is frequently not the case, especially if you have an initial investment up front, and which is almost never on December 31.

**XIRR gives you the flexibility to assign specific dates to each individual cash flow, making it a much more accurate calculation.**

![XIRR vs IRR in Excel](https://cdn.corporatefinanceinstitute.com/assets/xirr-vs-irr.png)

### What is Internal Rate of Return (IRR)?

The Internal Rate of Return is the discount rate that sets the [Net Present Value (NPV)](https://corporatefinanceinstitute.com/collections/)
 of all future cash flows of an investment to zero. If the NPV of an investment is zero, that doesn’t mean it’s a good or bad investment, it just means you will earn the IRR (discount rate) as your rate of return.

### What is IRR in Excel?

If you use the [\=IRR() formula in Excel,](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
 then you are using equal time periods between each cell (cash flow). This makes it challenging when you expect to enter an investment in the middle of a year. For this reason (as outlined below), always use XIRR instead.

### What is XIRR in Excel?

If you use the [\=XIRR() formula in Excel,](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
 then you have complete flexibility over the time periods of the cash flows. In order to do this, enter two series in your formula:

*   The series of cash flows
*   The corresponding dates of each of the cash flows

### Example of XIRR vs IRR Calculation

Below is an example of regular IRR versus XIRR with a series of six cash flows. With regular IRR, it assumes all cash flows occur on Dec 31, but with [XIRR,](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
 we can tell Excel that the first cash flow is in the middle of the year. This has a substantial impact on the internal rate of return calculation.

![Example of XIRR vs IRR Calculation in Excel](https://cdn.corporatefinanceinstitute.com/assets/xirr-vs-irr.png)

As you can see in the result below, using XIRR vs IRR produces 16.25% as compared to 13.45%, which is a material difference!

![XIRR vs IRR Calculation Results](https://cdn.corporatefinanceinstitute.com/assets/irr-and-xirr.png)

### Download the Free Template

Our free [XIRR vs IRR Template](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-template/)
 allows you to differentiate between the use of IRR and XIRR functions to compute the internal rate of return.  

   Download NowDownload Now

### Additional Resources

Thank you for reading this guide to XIRR vs IRR in Excel. To keep learning and advancing your career, we highly recommend the additional CFI resources below:

*   [XIRR vs IRR Template](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-template/)
    
*   [DCF Modeling Guide](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/)
    
*   [What is Sensitivity Analysis?](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-sensitivity-analysis/)
    
*   **[See all Excel resources](https://corporatefinanceinstitute.com/topic/excel/)
    **
*   **[See all financial modeling resources](https://corporatefinanceinstitute.com/topic/financial-modeling/)
    **

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn MoreLearn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fxirr-vs-irr-excel-financial-model%2F&summary=XIRR+vs+IRR "Share on LinkedIn")
    
*   [![Share on Facebook](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fxirr-vs-irr-excel-financial-model%2F "Share on Facebook")
    
*   [![Share on Twitter](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://twitter.com/intent/tweet?text=XIRR+vs+IRR&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fxirr-vs-irr-excel-financial-model%2F "Share on Twitter")
    
*   [![Share on WhatsApp](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fxirr-vs-irr-excel-financial-model%2F&summary=XIRR+vs+IRR "Share on WhatsApp")
    
*   [![Copy link](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model/ "Copy link")
    

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

![](https://bat.bing.com/action/0?ti=26068827&tm=gtm002&Ver=2&mid=d40bd091-f920-41df-b11d-ad9d7d8140df&bo=2&sid=e708c21022bd11f1ac6f9ff9d6dc07e4&vid=e70913b022bd11f185c7818b4bbf98ee&vids=1&msclkid=N&pi=0&lg=en-US&sw=1280&sh=800&sc=24&nwd=1&tl=XIRR%20vs%20IRR%20-%20Why%20You%20Must%20Use%20XIRR%20in%20Excel%20Financial%20Modeling&p=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fxirr-vs-irr-excel-financial-model%2F&r=&lt=3394&evt=pageLoad&sv=2&asc=G&cdb=AQcD&rn=445109)

![](https://www.ojrq.net/p/?return=&cid=23723&tpsync=no&auth=)