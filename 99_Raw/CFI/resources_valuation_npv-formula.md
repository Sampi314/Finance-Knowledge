# NPV Formula - Learn How Net Present Value Really Works, Examples

**Source:** https://corporatefinanceinstitute.com/resources/valuation/npv-formula

---

Table of Contents

*   [What is the NPV Formula?](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#what-is-the-npv-formula)
    

*   [NPV for a Series of Cash Flows](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#npv-for-a-series-of-cash-flows)
    
*   [What is the Math Behind the NPV Formula?](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#what-is-the-math-behind-the-npv-formula)
    
*   [How to Use the NPV Formula in Excel](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#how-to-use-the-npv-formula-in-excel)
    
*   [Video Explanation of the NPV Formula](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#video-explanation-of-the-npv-formula)
    
*   [DCF Modeling](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#dcf-modeling)
    
*   [More Helpful Resources](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/#more-helpful-resources)
    

NPV Formula
===========

Learn how Net Present Value works

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published December 21, 2018

Read Time 3 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

What is the NPV Formula?
------------------------

The NPV formula is a way of calculating the Net Present Value (NPV) of a series of cash flows based on a specified discount rate.  The NPV formula can be very useful for financial analysis and [financial modeling](https://corporatefinanceinstitute.com/collections/financial-modeling/)
 when determining the value of an investment (a company, a project, a cost-saving initiative, etc.).

Below is an illustration of the NPV formula for a single [cash flow](https://corporatefinanceinstitute.com/resources/accounting/cash-flow/)
.

#### Present Value = Cash Flow / (1+i)n

Where:

*   i = Discount rate
*   n = Period number

[![NPV Formula - Single Cash Flow](https://cdn.corporatefinanceinstitute.com/assets/npv-formula.png)](https://corporatefinanceinstitute.com/course/corporate-finance-fundamentals/)

Screenshot of CFI’s [Corporate Finance 101 Course](https://corporatefinanceinstitute.com/course/corporate-finance-fundamentals/)
.

### NPV for a Series of Cash Flows

In most cases, a financial analyst needs to calculate the net present value of a [series of cash flows](https://corporatefinanceinstitute.com/resources/financial-modeling/forecasting-cash-flow/)
, not just one individual cash flow.  The formula works in the same way, however, each cash flow has to be discounted individually, and then all of them are added together.

Here is an illustration of a series of cash flows being discounted:

[![NPV Formula for a Series of Cash Flows](https://cdn.corporatefinanceinstitute.com/assets/NPV-for-series-of-cash-flows.jpg)](https://corporatefinanceinstitute.com/course/corporate-finance-fundamentals/)

Source: CFI’s [Free Corporate Finance Course](https://corporatefinanceinstitute.com/course/corporate-finance-fundamentals/)
.

### **What is the Math Behind the NPV Formula?**

Here is the mathematical formula for calculating the present value of an individual cash flow.

#### **NPV = F / \[ (1 + i)^n \]**

Where:

*   **PV** = **P**resent **V**alue
*   **F** = **F**uture payment (cash flow)
*   **i** = Discount rate (or **i**nterest rate)
*   **n** = the **n**umber of periods in the future the cash flow is

### How to Use the NPV Formula in Excel

Most financial analysts never calculate the net present value by hand or with a calculator; instead, they use Excel.

#### **\=NPV(discount rate, series of cash flow)**

Example of how to use the NPV function:

1.  Set a discount rate in a cell.
2.  Establish a series of cash flows (must be in consecutive cells).
3.  Type “=NPV(“  and select the discount rate “,” then select the cash flow cells and “)”. (See screenshots below).

Congratulations, you have now calculated net present value in Excel!

[Download the free template](https://corporatefinanceinstitute.com/assets/NPV-fuction.xlsx)
.

![Screenshot of NPV Function in Excel](https://cdn.corporatefinanceinstitute.com/assets/npv-formula-excel-1.png)

![NPV Calculation in Excel](https://cdn.corporatefinanceinstitute.com/assets/npv-formula-result.png)

Source: CFI’s [Free Excel Crash Course](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)
.

If you need to be very precise in your calculation, it’s **highly recommended to use [XNPV](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/resources/excel/study/xnpv-function-in-excel/)
 instead of the regular function**.

To find out why, **read CFI’s [guide to XNPV vs NPV in Excel](https://corporatefinanceinstitute.com/resources/excel/xnpv-function-in-excel/)**.

### Video Explanation of the NPV Formula

Below is a short video explanation of how the formula works, including a detailed example with an illustration of how future cash flows become discounted back to the present.

### DCF Modeling

The main use of the NPV formula is in Discounted Cash Flow (DCF) modeling in Excel.  In [DCF models](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/)
 an analyst will forecast a company’s [three financial statements](https://corporatefinanceinstitute.com/resources/accounting/three-financial-statements/)
 into the future and calculate the company’s [Free Cash Flow to the Firm](https://corporatefinanceinstitute.com/resources/valuation/cash-flow-guide-ebitda-cf-fcf-fcff/)
 (FCFF).

Additionally, a [terminal value](https://corporatefinanceinstitute.com/resources/valuation/terminal-value/)
 is calculated at the end of the forecast period. Each of the cash flows in the forecast and terminal value is then discounted back to the present using a [hurdle rate](https://corporatefinanceinstitute.com/resources/valuation/hurdle-rate-definition/)
 of the firm’s weighted average cost of capital ([WACC](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
).

Below is an example of a DCF model from one of CFI’s [financial modeling courses](https://corporatefinanceinstitute.com/collections/financial-modeling/)
.

[![DCF Modeling Example - Net Present Value (NPV)](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](https://corporatefinanceinstitute.com/collections/financial-modeling/)

Screenshot: CFI [financial modeling courses](https://corporatefinanceinstitute.com/collections/financial-modeling/)
.

### More Helpful Resources

Thank you for reading this guide to calculating net present value.  CFI’s mission is to help anyone become a world-class financial analyst.  To keep learning and advancing your career, these additional financial resources will be a big help:

*   [Walk Me Through a DCF Model](https://corporatefinanceinstitute.com/resources/career/walk-me-through-a-dcf/)
    
*   [Valuation Methods](https://corporatefinanceinstitute.com/resources/valuation/valuation/)
    
*   [DCF Modeling Guide](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/)
    
*   [Vertex42® Excel Templates](https://corporatefinanceinstitute.com/resources/excel/vertex42-excel-templates/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

### Analyst Certification FMVA® Program

Below is a break down of [subject weightings](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 in the FMVA® financial analyst program. As you can see there is a heavy focus on financial modeling, finance, Excel, business valuation, budgeting/forecasting, PowerPoint presentations, accounting and business strategy.

[![Financial Analyst certification curriculum](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

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
    

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fnpv-formula%2F&summary=NPV+Formula "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fnpv-formula%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](https://twitter.com/intent/tweet?text=NPV+Formula&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fnpv-formula%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fnpv-formula%2F&summary=NPV+Formula "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/npv-formula/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)