# Internal Rate of Return (IRR) - Calculator & Formula

**Source:** https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr

---

Table of Contents

*   [What is the Internal Rate of Return (IRR)?](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#what-is-the-internal-rate-of-return-irr)
    
*   [What is the IRR Formula?](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#what-is-the-irr-formula)
    

*   [Practical Example](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#practical-example)
    

*   [IRR Calculator](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#irr-calculator)
    
*   [What is the Internal Rate of Return Used For?](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#what-is-the-internal-rate-of-return-used-for)
    
*   [What IRR Really Means (Another Example)](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#what-irr-really-means-another-example)
    
*   [Disadvantages of IRR](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#disadvantages-of-irr)
     
*   [Additional Resources](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/#additional-resources)
    

Internal Rate of Return (IRR)
=============================

An Analyst's Guide to IRR

Written by [Tim Vipond, FMVA](https://corporatefinanceinstitute.com/author/tim-vipond/)

Published February 27, 2020

Read Time 5 minutes

What is the Internal Rate of Return (IRR)?
------------------------------------------

The Internal Rate of Return (IRR) is the discount rate that makes the [net present value (NPV)](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/)
 of a project zero. In other words, it is the expected compound annual rate of return that will be earned on a project or investment.

When calculating IRR, expected cash flows for a project or investment are given and the NPV equals zero. Put another way, the initial cash investment for the beginning period will be equal to the present value of the _future_ [cash flows](https://corporatefinanceinstitute.com/resources/accounting/cash-flow/)
 of that investment. (Cost paid = present value of future cash flows, and hence, the _net_ present value = 0).

Once the internal rate of return is determined, it is typically compared to a company’s [hurdle rate](https://corporatefinanceinstitute.com/resources/valuation/hurdle-rate-definition/)
 or cost of capital. If the IRR is greater than or equal to the cost of capital, the company would accept the project as a good investment. (That is, of course, assuming this is the sole basis for the decision.

In the example below, an initial investment of $50 has a 22% IRR. That is equal to earning a 22% compound annual growth rate.

![Example of Calculating Internal Rate of Return (IRR), from an initial investment of USD50 and an IRR of 22%](https://cdn.corporatefinanceinstitute.com/assets/internal-rate-of-return-irr-example.png)

In reality, there are many other quantitative and qualitative factors that are considered in an investment decision.) If the IRR is lower than the hurdle rate, then it would be rejected.

What is the IRR Formula?
------------------------

The IRR formula is as follows: 

![Breakdown of Internal Rate of Return (IRR) Formula](https://cdn.corporatefinanceinstitute.com/assets/Screen-Shot-2017-07-16-at-11.27.16-PM.png)

Calculating the internal rate of return can be done in three ways:

1.  Using the IRR or [XIRR](https://corporatefinanceinstitute.com/resources/excel/xirr-function/)
     function in Excel or other spreadsheet programs (see example below)
2.  Using a financial calculator
3.  Using an iterative process where the analyst tries different discount rates until the NPV equals zero ([Goal Seek](https://corporatefinanceinstitute.com/resources/excel/goal-seek-excel-guide/)
     in Excel can be used to do this)

### Practical Example

Here is an example of how to calculate the Internal Rate of Return.

A company is deciding whether to purchase new equipment that costs $500,000. Management estimates the life of the new asset to be four years and expects it to generate an additional $160,000 of annual [profits](https://corporatefinanceinstitute.com/resources/accounting/profit/)
. In the fifth year, the company plans to sell the equipment for its salvage value of $50,000.

Meanwhile, another similar investment option can generate a 10% return. This is higher than the company’s current hurdle rate of 8%. The goal is to make sure the company is making the best use of its cash.

To make a decision, the IRR for investing in the new [equipment](https://corporatefinanceinstitute.com/resources/knowledge/accounting/ppe-property-plant-equipment/)
 is calculated below.

Excel was used to calculate the IRR of 13%, using the function, =_IRR()_. From a financial standpoint, the company should make the purchase because the IRR is both greater than the hurdle rate and the IRR for the alternative investment.

![Example of how to calculate the Internal Rate of Return in Excel](https://cdn.corporatefinanceinstitute.com/assets/IRR.png)

**IRR Calculator**
------------------

Enter your name and email in the form below and download the free calculator/template now!  

   Download Now

What is the Internal Rate of Return Used For?
---------------------------------------------

Companies take on various projects to increase their revenues or cut down costs. A great new business idea may require, for example, investing in the development of a new product.

In capital budgeting, senior leaders like to know the estimated return on such investments. The internal rate of return is one method that allows them to compare and rank projects based on their projected yield. The investment with the highest internal rate of return is usually preferred.

Internal Rate of Return is widely used in analyzing investments for private equity and venture capital, which involves multiple cash investments over the life of a business and a cash flow at the end through an IPO or [sale of the business](https://corporatefinanceinstitute.com/resources/valuation/sale-purchase-agreement/)
.

Thorough investment analysis requires an analyst to examine both the net present value (NPV) and the internal rate of return, along with other indicators, such as the [payback period,](https://corporatefinanceinstitute.com/resources/financial-modeling/payback-period/)
 in order to select the right investment.  Since it’s possible for a very small investment to have a very high rate of return, investors and managers sometimes choose a lower _percentage return_ but higher _absolute dollar value_ opportunity.

Also, it’s important to have a good understanding of your own risk tolerance, a company’s investment needs, [risk aversion,](https://corporatefinanceinstitute.com/resources/wealth-management/risk-averse-definition/)
 and other available options.

What IRR Really Means (Another Example)
---------------------------------------

Let’s look at an example of a financial model in Excel to see what the internal rate of return number really means.

If an investor paid $463,846 (which is the negative cash flow shown in cell C178) for a series of positive cash flows as shown in cells D178 to J178, the IRR they would receive is 10%. This means the net present value of all these cash flows (including the negative outflow) is zero and that only the 10% rate of return is earned.

If the investors paid _less than_ $463,846 for all the same additional cash flows, then their IRR would be _higher than 10%._ Conversely, if they paid _more than_ $463,846, then their IRR would be _lower than 10%_.

![Example of a financial model in Excel showing how to calculate IRR ](https://cdn.corporatefinanceinstitute.com/assets/irr-calculation.png)

The above screenshot is from CFI’s [M&A Modeling Course](https://corporatefinanceinstitute.com/collections/advanced-financial-modeling-mergers-acquisitions/)
.

Disadvantages of IRR 
---------------------

Unlike net present value, the internal rate of return doesn’t give you the return on the initial investment in terms of real dollars. For example, knowing an IRR of 30% alone doesn’t tell you if it’s 30% of $10,000 or 30% of $1,000,000.

Using IRR exclusively can lead you to make poor investment decisions, especially if comparing two projects with different durations.

Let’s say a company’s hurdle rate is 12%, and one-year project A has an IRR of 25%, whereas five-year project B has an IRR of 15%. If the decision is solely based on IRR, this will lead to unwisely choosing project A over B.

Another very important point about the internal rate of return is that **it assumes all positive cash flows of a project will be reinvested at the same rate as the project** instead of the [company’s cost of capital.](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
 Therefore, the internal rate of return may not accurately reflect the profitability and cost of a project.

A smart financial analyst will alternatively use the modified internal rate of return (MIRR) to arrive at a more accurate measure.

Connect what you just learned to a clear career path with CFI’s role‑based courses and certification programs.

[Advance Your Career](https://corporatefinanceinstitute.com/pricing/)

Additional Resources
--------------------

Thank you for reading CFI’s explanation of the Internal Rate of Return metric. CFI is the official global provider of the [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 designation. To learn more and help advance your career, see the following free CFI resources:

*   [XIRR vs. IRR](https://corporatefinanceinstitute.com/resources/financial-modeling/xirr-vs-irr-excel-financial-model/)
    
*   [EVA: Economic Value Added](https://corporatefinanceinstitute.com/resources/valuation/economic-value-added-eva/)
    
*   [Weighted Average Cost of Capital (WACC)](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
    
*   [Crossover Rate](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)
    

**[See all Valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
**

Get Certified for Financial Modeling (FMVA)®

Gain in-demand industry knowledge and hands-on practice that will help you stand out from the competition and become a world-class financial analyst.

[Learn More](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

*   Share this article
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Finternal-rate-return-irr%2F&summary=Internal+Rate+of+Return+%28IRR%29 "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Finternal-rate-return-irr%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)](https://twitter.com/intent/tweet?text=Internal+Rate+of+Return+%28IRR%29&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Finternal-rate-return-irr%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Finternal-rate-return-irr%2F&summary=Internal+Rate+of+Return+%28IRR%29 "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)