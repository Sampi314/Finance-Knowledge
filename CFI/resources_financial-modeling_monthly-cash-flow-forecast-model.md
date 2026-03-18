# Monthly Cash Flow Forecast Model - Example, How to Use

**Source:** https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model

---

Table of Contents

*   [Monthly Cash Flow Forecast Model](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model#monthly-cash-flow-forecast-model)
    

*   [Inputs and Assumptions](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model#inputs-and-assumptions)
    
*   [Processing](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model#processing)
    
*   [Outputs](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model#outputs)
    
*   [Categories of Cash Flow Forecast](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model#categories-of-cash-flow-forecast)
    
*   [Related resources](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model#related-resources)
    

Monthly Cash Flow Forecast Model
================================

Inputs, assumptions, processing, and outputs in a cash flow forecast model

Written by [CFI Team](https://corporatefinanceinstitute.com/about-cfi/)

Published April 1, 2020

Read Time 4 minutes

Over 2.8 million + professionals use CFI to learn accounting, financial analysis, modeling and more. Unlock the essentials of corporate finance with our free resources and get an exclusive sneak peek at the first module of each course. [Start Free Start Free](https://learn.corporatefinanceinstitute.com/auth/registration)

Monthly Cash Flow Forecast Model
--------------------------------

With a rolling monthly cash flow forecast, the number of periods in the forecast remains constant (e.g., 12 months, 18 months, etc.).  The forecast is rolled forward every time there is a month of historical data to input.  [Rolling forecasts](https://corporatefinanceinstitute.com/resources/accounting/rolling-forecast/)
 work best when key [cash flow drivers](https://corporatefinanceinstitute.com/resources/valuation/cash-flow-drivers/)
 are modeled explicitly and directly drive forecast cash flow inputs.  We’ll look at the structure of a robust and flexible monthly cash flow forecast model for a retail store business in the following sections.

### Inputs and Assumptions

Here are five important points to creating a strong input section for a cash flow forecast model:

![Example of Monthly Cash Flow Model Assumptions](https://cdn.corporatefinanceinstitute.com/assets/monthly-cash-flow-model-assumptions-1024x416.png)

Image Source: CFI’s [FP&A Monthly Cash Flow Course](https://corporatefinanceinstitute.com/course/fpa-rolling-12-month-cash-flow-forecast-course/)
.

##### 1\. Key cash flow drivers should be modeled explicitly.

In our example, a retail store business should start with the number of stores it plans to operate each month, then build up from there, based on the number of square feet and sales per square foot.  This will help the business to compute its [revenue](https://corporatefinanceinstitute.com/resources/accounting/sales-revenue/)
.

##### 2\. Inputs should only need to be input once.

It is important to group all inputs in the assumptions section so users can easily find, add, and modify them.

##### 3\. Inputs should be organized logically.

This helps users of the model to quickly understand and update the model when they first jump into it.

##### 4\. All model inputs should be of the same color.

Using identical colors for inputs allows users to easily distinguish between inputs and other calculated outputs.  Most financial models use a blue font or yellow shading for inputs, and black font for [formulas](https://corporatefinanceinstitute.com/resources/excel/basic-excel-formulas-beginners/)
.

##### 5\. Document your sources for model inputs where possible.

Make notes and comments in cells using keyboard shortcut SHIFT + F2 to indicate where you pull the assumptions from.

### Processing

The processing section of a cash flow forecast model is located on the right-hand side of the historical results.  All cells in this section should be in formulas.

![Example of processing section of a cash flow forecast model](https://cdn.corporatefinanceinstitute.com/assets/monthly-cash-flow-model-income-statement-1024x296.png)

Image Source: CFI’s [FP&A Monthly Forecasting Course](https://corporatefinanceinstitute.com/course/fpa-rolling-12-month-cash-flow-forecast-course/)
.

##### 1\. Model calculations and processing should be transparent and easy-to-follow.

Use step-by-step calculations that are short in length. If the formulas are becoming too long, it is always a good practice to break them down into simple steps to allow efficient auditing and updates.

##### 2\. Hard-coded calculations should be avoided.

Everything to the right of the historical results should not be [hard-coded](https://en.wikipedia.org/wiki/Hard_coding)
.  All calculations should draw on explicit input drivers.

##### 3\. Put complicated calculations and processing on a separate worksheet.

Keep only the final figures on the output worksheets, and separate long and complicated formulas and calculations on another section of the model or worksheet.

##### 4\. Document how and why complicated calculations are structured.

This allows easy usability and audit-ability and brings confidence to the general process. All formulas should be transparent, clear, and well-documented so people can easily understand how the model works.

### Outputs

The output section contains all the important figures we would like to get out of a cash flow forecast model.

![Example of output section of a cash flow forecast model, with charts and graphs](https://cdn.corporatefinanceinstitute.com/assets/monthly-cash-flow-model-output-1024x438.png)

Image Source: CFI’s [FP&A Monthly Financial Modeling Course](https://corporatefinanceinstitute.com/course/fpa-rolling-12-month-cash-flow-forecast-course/)
.

##### 1\. Models outputs should be easy to find and understand.

##### 2\. Model outputs should be grouped logically in one area.

Outputs are typically placed at the bottom of the cash flow model and grouped together using the Grouping function in Excel.

##### 3\. Model outputs should be formula-driven with no hard-coding.

##### 4\. Outputs should provide key results to aid decision-making.

Charts and graphs summarize the health of the business, point out any issues that need to be considered or addressed, and make it easy for executive management to understand what is going to happen over the period of the forecast and, thus, make important decisions.

### Categories of Cash Flow Forecast

A rolling monthly cash flow forecast can be derived from a balance sheet and income statement driven by explicit inputs.  There are three categories of cash flow forecast:

![Cash Flow Forecast Model in Excel](https://cdn.corporatefinanceinstitute.com/assets/monthly-cash-flow-financial-model-1024x425.png)

#### Operating cash flows forecast

1.  Starting with [net income](https://corporatefinanceinstitute.com/resources/accounting/what-is-net-income/)
     from the income statement, add back any non-cash expenses that are included in the income statement such as depreciation from the PP&E breakdown.
2.  Adjust for changes in operating assets and liabilities (or working capital). Examples of working capital are trade and other receivables, inventories, and trade and other payables.
3.  Forecast working capital using working capital ratios such as receivable days, inventory days, and payable days. For a monthly cash flow forecast, the following ratios should be used:

Monthly accounts receivable = Receivable days 30 \* Sales

Monthly accounts payable = Payable days 30 \* Cost of sales

Monthly inventory = Inventory days 30 \* Cost of sales

#### Investing cash flows forecast

1.  Cash outflows include money invested in [property, plant, and equipment (PP&E)](https://corporatefinanceinstitute.com/resources/accounting/ppe-property-plant-equipment/)
     in the form of capital expenditures or acquisitions of new businesses.
2.  Cash inflows include proceeds from disposals of PP&E or businesses.

#### Financing cash flows forecast

1.  Cash inflows include cash raised by issuing equity or debt.
2.  Cash outflows include cash used to repurchase or repay equity or debt, and dividends paid out.

### Related resources

CFI is the official global provider of the [Financial Modeling and Valuation Analyst (FMVA)® designation](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
. To help you advance your career, check out the additional CFI resources below:

*   [Financial Modeling Best Practices](https://corporatefinanceinstitute.com/resources/financial-modeling/free-financial-modeling-guide/)
    
*   [Data Sources in Financial Modeling](https://corporatefinanceinstitute.com/resources/financial-modeling/data-sources-in-financial-modeling/)
    
*   [Statement of Cash Flows](https://corporatefinanceinstitute.com/resources/accounting/statement-of-cash-flows/)
    
*   [The Ultimate Cash Flow Guide](https://corporatefinanceinstitute.com/resources/valuation/cash-flow-guide-ebitda-cf-fcf-fcff/)
    
*   **[See all financial modeling resources](https://corporatefinanceinstitute.com/topic/financial-modeling/)
    **

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn MoreLearn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fmonthly-cash-flow-forecast-model%2F&summary=Monthly+Cash+Flow+Forecast+Model "Share on LinkedIn")
    
*   [![Share on Facebook](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fmonthly-cash-flow-forecast-model%2F "Share on Facebook")
    
*   [![Share on Twitter](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://twitter.com/intent/tweet?text=Monthly+Cash+Flow+Forecast+Model&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fmonthly-cash-flow-forecast-model%2F "Share on Twitter")
    
*   [![Share on WhatsApp](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Ffinancial-modeling%2Fmonthly-cash-flow-forecast-model%2F&summary=Monthly+Cash+Flow+Forecast+Model "Share on WhatsApp")
    
*   [![Copy link](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 32 32" xml:space="preserve"></svg>)](https://corporatefinanceinstitute.com/resources/financial-modeling/monthly-cash-flow-forecast-model/ "Copy link")
    

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