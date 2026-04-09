# Intrinsic Value - Learn How to Calculate Intrinsic Value of a Business

**Source:** https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide

---

Table of Contents

*   [What is Intrinsic Value?](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#what-is-intrinsic-value)
    
*   [Background](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#background)
    
*   [Intrinsic Value Formula](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#intrinsic-value-formula)
    
*   [Risk Adjusting the Intrinsic Value](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#risk-adjusting-the-intrinsic-value)
    

*   [Discount Rate](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#discount-rate)
    
*   [Certainty Factor](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#certainty-factor)
    

*   [Calculating Intrinsic Value in Excel](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#calculating-intrinsic-value-in-excel)
    

*   [1\. Discount Rate](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#1-discount-rate)
    
*   [2\. Certainty Factor](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#2-certainty-factor)
    

*   [Challenges with Intrinsic Value](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#challenges-with-intrinsic-value)
    
*   [Download the Free Template](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#download-the-free-template)
    
*   [Other Forms of Valuation](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#other-forms-of-valuation)
    

*   [1\. Technical Analysis](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#1-technical-analysis)
    
*   [2\. Relative Valuation](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#2-relative-valuation)
    
*   [3\. Cost Approach](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#3-cost-approach)
    

*   [Video Explanation of Intrinsic Value](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#video-explanation-of-intrinsic-value)
    
*   [Additional Resources](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/#additional-resources)
    

Intrinsic Value
===============

The price a rational investor is willing to pay for an investment, given its level of risk

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published January 22, 2018

Read Time 5 minutes

What is Intrinsic Value?
------------------------

The intrinsic value of a business (or any investment security) is the present value of all expected future [cash flows](https://corporatefinanceinstitute.com/resources/accounting/statement-of-cash-flows/)
, discounted at the appropriate discount rate. Unlike relative forms of valuation that look at [comparable companies](https://corporatefinanceinstitute.com/resources/valuation/comparable-company-analysis/)
, intrinsic valuation looks only at the inherent value of a business on its own.

![Intrinsic Value Definition](https://cdn.corporatefinanceinstitute.com/assets/intrinsic-value2.png)

Another way to define intrinsic value is simply, “The price a rational investor is willing to pay for an investment, given its level of risk.”

Background
----------

Benjamin Graham and Warrant Buffett are widely considered the forefathers of value investing, which is based on the intrinsic valuation method. Graham’s book, [The Intelligent Investor](https://en.wikipedia.org/wiki/The_Intelligent_Investor)
, laid the groundwork for Warren Buffett and the entire school of thought on the topic.

The term intrinsic means _the essential nature of something_. Synonyms include innate, inherent, native, natural, deep-rooted, etc.

Intrinsic Value Formula
-----------------------

There are different variations of the intrinsic value formula, but the most “standard” approach is similar to the [net present value](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/)
 formula.

![Intrinsic Value Formula](https://cdn.corporatefinanceinstitute.com/assets/intrinsic-value-formula.png)

Where:

**NPV** = Net Present Value

**FV_j_** = Net cash flow for the _j_ th period (for the initial “Present” cash flow, _j =_ 0

_**i**_ \= annual interest rate

_**n**_ \= number of periods included

Variations include multi-stage growth models and assigning a probability or level of certainty to the cash flows and playing around with the discount rate.

Risk Adjusting the Intrinsic Value
----------------------------------

The task of risk adjusting the cash flows is very subjective and a combination of both art and science.

There are two main methods:

1.  **Discount rate** – Using a discount rate that includes a risk premium in it to adequately discount the cash flows
2.  **Certainty factor** – Using a factor on a scale of 0-100% certainty of the cash flows in the forecast materializing (This approach is believed to be used by Warren Buffett. Learn more by reading [Buffett’s annual letters to shareholders](https://www.berkshirehathaway.com/letters/letters.html)
    )

### Discount Rate

In the discount rate approach, a financial analyst will typically use a company’s [weighted average cost of capital (WACC)](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
. The formula for WACC includes the risk-free rate (usually a government bond yield) plus a premium based on the volatility of the stock multiplied by an equity risk premium. Learn all about the [WACC formula here](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
.

The rationale behind this approach is that if a stock is more volatile, it’s a riskier investment. Therefore, a higher discount rate is used, which has the effect of reducing the value of cash flow that would be received further in the future (because of the greater uncertainty).

### Certainty Factor

A certainty factor, or probability, can be assigned to each individual cash flow or multiplied against the entire [net present value (NPV)](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/)
 of the business as a means of discounting the investment. In this approach, only the risk-free rate is used as the discount rate since the cash flows are already risk-adjusted.

For example, the cash flow from a US Treasury note comes with a 100% certainty attached to it, so the discount rate is equal to yield, say 2.5% in this example. Compare that to the cash flow from a very high-growth and high-risk technology company. A 50% probability factor is assigned to the cash flow from the tech company and the same 2.5% discount rate is used.

At the end of the day, both methods are attempting to do the same thing – to discount an investment based on the level of risk inherent in it.

Calculating Intrinsic Value in Excel
------------------------------------

Below we will provide examples of how to calculate the intrinsic value in Excel using the two methods described above.

### 1\. Discount Rate

In the screenshot below, you can see how this approach is taken in Excel. The risk-adjusted discount rate for this investment is determined to be 10.0% based on its historic price volatility. In this method, there is no certainty or probability factor assigned to each [cash flow](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/resources/knowledge/valuation/cash-flow-guide-ebitda-cf-fcf-fcff/)
, since the discount rate does all the risk adjusting.

![Intrinsic Value with Discount Rate](https://cdn.corporatefinanceinstitute.com/assets/intrinsic-value4.png)

As you will see, for an investment that pays $10,000 at the end of each year for 10 years with a 10% discount rate, the intrinsic value is $61,446.

To learn more about DCF models, check out [CFI’s online financial modeling courses](https://corporatefinanceinstitute.com/collections/financial-modeling/)
.

### 2\. Certainty Factor

In the second screenshot below, you can see how this alternative approach is taken in Excel. This time, an [analyst](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 uses only the risk-free rate of 2.5% as the discount rate. There is, however, an additional adjustment factor of 70% applied to each cash flow. The way to think about this is, “there is a 70% chance of receiving $10,000 each year”, _or_, “there is a 100% chance of receiving $7,021 each year.”

![Intrinsic Value with Certainty Factor](https://cdn.corporatefinanceinstitute.com/assets/intrinsic-value3.png)

As you can see, for this same investment that pays $10,000 at the end of each year for 10 years with a 70% confidence factor and 2.5% discount rate, the intrinsic value is $61,446 (the same as method #1).

Challenges with Intrinsic Value
-------------------------------

The trouble with calculating intrinsic value is it’s a very subjective exercise. There are so many assumptions that must be made, and the final [net present value](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/)
 is very sensitive to changes in those assumptions.

Each of the assumptions in the WACC ([beta](https://corporatefinanceinstitute.com/resources/data-science/beta-coefficient/)
, [market risk premium](https://corporatefinanceinstitute.com/resources/valuation/market-risk-premium/)
) can be calculated in different ways, while the assumption around a confidence/probability factor is entirely subjective.

Essentially, when it comes to predicting the future, it is by definition, uncertain. For this reason, all of the most successful investors in the world can look at the same information about a company and arrive at totally different figures for its intrinsic value.

Download the Free Template
--------------------------

### Intrinsic Value Template

Download the free Excel template now to advance your finance knowledge!

*   First Name\*
    
*   Email\*
    

           

Δ

Other Forms of Valuation
------------------------

Intrinsic valuation is often used for long-term investment strategies, but there are many other approaches to valuation and investing. Alternatives include technical analysis, relative valuation, and cost approach.

### 1\. Technical Analysis

[Technical analysis](https://corporatefinanceinstitute.com/resources/career-map/sell-side/capital-markets/technical-analysis/)
 involves looking at charts and evaluating various indicators that may signal a stock is going to go up or down in the short to medium term. Examples include candlestick charts, momentum and moving averages, relative strength, and more.

### 2\. Relative Valuation

Relative valuation looks at what other investors are willing to pay for a similar investment and assumes that they would pay a comparable price for the company in question. The two most common examples of this are [comparable company analysis](https://corporatefinanceinstitute.com/resources/valuation/comparable-company-analysis/)
 (“Comps”) and [precedent transaction analysis](https://corporatefinanceinstitute.com/resources/valuation/precedent-transaction-analysis/)
 (“Precedents”).

### 3\. Cost Approach

In the cost approach, an investor looks at what the cost to build or create something would be and assumes that is what it’s worth. They may look at what it costs others to build a similar business and take into account how costs have changed since then (inflation, deflation, input costs, etc.).

Video Explanation of Intrinsic Value
------------------------------------

Watch this short video to quickly understand the main concepts covered in this guide, including what intrinsic value is, the formula, how to risk adjust the intrinsic value, and how to perform the calculation in Excel.

Additional Resources
--------------------

Thank you for reading this guide to intrinsic value. Hopefully, by now, you’ve gained a better understanding of how investors determine what an investment is worth to them. These additional resources will be helpful:

*   [The Analyst Trifecta](https://corporatefinanceinstitute.com/resources/financial-modeling/analyst-trifecta-ebook-pdf/)
    
*   [Valuation Infographic](https://corporatefinanceinstitute.com/resources/valuation/valuation-infographic/)
    
*   [Financial Modeling Guide](https://corporatefinanceinstitute.com/resources/financial-modeling/free-financial-modeling-guide/)
    
*   [All Valuation Articles](https://corporatefinanceinstitute.com/topic/valuation/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

### Analyst Certification FMVA® Program

Below is a break down of [subject weightings](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 in the FMVA® financial analyst program. As you can see there is a heavy focus on financial modeling, finance, Excel, business valuation, budgeting/forecasting, PowerPoint presentations, accounting and business strategy.

[![Financial Analyst certification curriculum](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

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
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fintrinsic-value-guide%2F&summary=Intrinsic+Value "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fintrinsic-value-guide%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)](https://twitter.com/intent/tweet?text=Intrinsic+Value&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fintrinsic-value-guide%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fintrinsic-value-guide%2F&summary=Intrinsic+Value "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/intrinsic-value-guide/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)