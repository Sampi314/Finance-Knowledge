# Crossover Rate

**Source:** https://corporatefinanceinstitute.com/resources/valuation/crossover-rate

---

Table of Contents

*   [What is the Crossover Rate?](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#what-is-the-crossover-rate)
    

*   [Crossover Rate Formula](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#crossover-rate-formula)
    
*   [Alternative Method of Calculating Crossover Rate](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#alternative-method-of-calculating-crossover-rate)
    
*   [Numerical Example](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#numerical-example)
    
*   [Graphical Solution to the Numerical Problem](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#graphical-solution-to-the-numerical-problem)
    
*   [Download the Free Template](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#download-the-free-template)
    
*   [Related Reading](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/#related-reading)
    

Crossover Rate
==============

Discount rate for equal NPVs

Written by [Tim Vipond, FMVA](https://corporatefinanceinstitute.com/author/tim-vipond/)

Published April 21, 2018

Read Time 4 minutes

What is the Crossover Rate?
---------------------------

Crossover Rate is the rate of return (alternatively called the [weighted average cost of capital](https://corporatefinanceinstitute.com/resources/valuation/what-is-wacc-formula/)
) at which the [Net Present Values](https://corporatefinanceinstitute.com/resources/valuation/dcf-analysis-infographic/)
 (NPV) of two projects are equal. It represents the rate of return at which the net present value profile of one project intersects the net present value profile of another project.

In capital budgeting analysis exercises, the crossover rate is used to show when one investment project becomes superior to another as a result of a change in the rate of return (cost of capital).

### Crossover Rate Formula

Consider the following example. An investor is faced with 2 investment projects: Project ABC and Project XYZ. Project ABC has an initial investment of A0 and will generate a steady stream of income over a 3-year period. The [cash flows](https://corporatefinanceinstitute.com/resources/valuation/cash-flow-guide-ebitda-cf-fcf-fcff/)
 from Project ABC at the end of the first, second, and third years are denoted by C1, C2, and C3, respectively. Thus, the Net Present Value of Project ABC is as follows:

![NPV of ABC](https://cdn.corporatefinanceinstitute.com/assets/NPV-of-ABC.png)

Project XYZ has an initial investment of X0 and will generate a steady stream of income over a 2-year period. The cash flows from Project XYZ at the end of the first and second years are denoted by Z1 and Z2, respectively. Thus, the Net Present Value of Project XYZ is as follows:

![NPV of XYZ](https://cdn.corporatefinanceinstitute.com/assets/NPV-of-XYZ.png)

The crossover rate is defined as the rate of return at which the NPVABC = NPVXYZ. Since C1, C2, C3, A0, Z1, Z2, and X0 are all known, we can solve for the crossover rate.

### Alternative Method of Calculating Crossover Rate

1.  Determine the [cash flow streams](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/resources/knowledge/valuation/cash-flow-guide-ebitda-cf-fcf-fcff/)
     of the two projects.
2.  Find the difference in the initial investments between the two projects.
3.  Find the difference in the cash flow in each period between the two projects. (After a project ends, it generates zero cash flow in all subsequent periods).
4.  Develop an [IRR](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)
     equation by equating the net present value equation of the resulting differential cash flows to zero.
5.  Solve the equation for r.

### Numerical Example

Let us continue with the example above. An investor is faced with 2 investment projects: Project ABC and Project XYZ. The first project, Project ABC costs $5 million and will result in a cash flow of $6 million at the end of the first year, $4 million at the end of the second year, and $2 million at the end of the third year. The second project, Project XYZ costs $8 million but will generate a cash flow of $25 million at the end of the second year.

![crossover rate formula](https://cdn.corporatefinanceinstitute.com/assets/crossover-rate-formula.png)

For simplicity let 1+r = v. Therefore, the above equation reduces to the following:

We can solve the above equation using the [cubic formula](https://corporatefinanceinstitute.com/course/financial-math-corporate-finance/)
. Because it is a cubic equation, it will have 3 roots that satisfy it. For the above equation v= -3.85, 1.76, and 0.098. Therefore, 1+r = -3.85, 1.76, or 0.098. Since the rate of return can never be negative, we can ignore the first and the third root. Therefore 1+r = 1.76 or r=0.76 or 76%.

### Graphical Solution to the Numerical Problem

We can arrive at the above solution using software such as [Microsoft Excel](https://corporatefinanceinstitute.com/topic/excel/)
 and plot the [NPV](https://corporatefinanceinstitute.com/resources/knowledge/valuation/npv-formula/)
 profiles of the two different projects and observe their point of intersection.

|     |     |     |
| --- | --- | --- |
| **r** | **NPVABC** | **NPVXYZ** |
| 0.05 | 6.070078825 | 14.67573696 |
| 0.1 | 5.26296018 | 12.66115702 |
| 0.15 | 4.556998438 | 10.90359168 |
| 0.2 | 3.935185185 | 9.361111111 |
| 0.25 | 3.384 | 8   |
| 0.3 | 2.892580792 | 6.792899408 |
| 0.35 | 2.452116039 | 5.717421125 |
| 0.4 | 2.055393586 | 4.755102041 |
| 0.45 | 1.69646152 | 3.890606421 |
| 0.5 | 1.37037037 | 3.111111111 |
| 0.55 | 1.07297506 | 2.405827263 |
| 0.6 | 0.80078125 | 1.765625 |
| 0.65 | 0.550825055 | 1.182736455 |
| 0.7 | 0.320578058 | 0.650519031 |
| 0.75 | 0.10787172 | 0.163265306 |
| 0.8 | \-0.089163237 | \-0.283950617 |
| 0.85 | \-0.272145776 | \-0.695398101 |
| 0.9 | \-0.442484327 | \-1.074792244 |
| 0.95 | \-0.601409329 | \-1.425378041 |

![crossover rate graph](https://cdn.corporatefinanceinstitute.com/assets/Crossover-rate.png)

From the above graph, we can see that the two [NPV](https://corporatefinanceinstitute.com/resources/knowledge/valuation/npv-formula/)
 profiles intersect with each other at around r=0.76 or 76%, which is the same answer that we got when we solved the cubic equation. Thus, if the rate of return or cost of capital is less than 0.76, Project XYZ is superior to Project ABC. However, if the rate of return is more than 0.76, Project ABC is superior to Project XYZ.

### Download the Free Template

### Crossover Rate Template

Download the free Excel template now to advance your finance knowledge!

*   First Name\*
    
*   Email\*
    

           

Δ

### Related Reading

Thanks for reading CFI’s guide to the crossover rate. To keep advancing your career, the additional CFI resources below will be useful:

*   [Crossover Rate Template](https://corporatefinanceinstitute.com/resources/financial-modeling/crossover-rate-template/)
    
*   [DCF Modeling Guide](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/)
    
*   [IRR Guide](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)
    
*   [XNPV Function](https://corporatefinanceinstitute.com/resources/excel/xnpv-function-in-excel/)
    
*   **[See all valuation resources](https://corporatefinanceinstitute.com/topic/valuation/)
    **

### Analyst Certification FMVA® Program

Below is a break down of [subject weightings](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)
 in the FMVA® financial analyst program. As you can see there is a heavy focus on financial modeling, finance, Excel, business valuation, budgeting/forecasting, PowerPoint presentations, accounting and business strategy.

[![Financial Analyst certification curriculum](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

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
*   [![Share on LinkedIn](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcrossover-rate%2F&summary=Crossover+Rate "Share on LinkedIn")
    
*   [![Share on Facebook](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcrossover-rate%2F "Share on Facebook")
    
*   [![Share on Twitter](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)](https://twitter.com/intent/tweet?text=Crossover+Rate&url=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcrossover-rate%2F "Share on Twitter")
    
*   [![Share on WhatsApp](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)](https://wa.me/?text=https%3A%2F%2Fcorporatefinanceinstitute.com%2Fresources%2Fvaluation%2Fcrossover-rate%2F&summary=Crossover+Rate "Share on WhatsApp")
    
*   [![Copy link](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/ "Copy link")
    

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

 [![Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/resources/valuation/crossover-rate/)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)