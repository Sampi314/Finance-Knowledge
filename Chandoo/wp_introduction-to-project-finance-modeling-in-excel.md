# Project Finance Modeling in Excel - Detailed Tutorial & Download

**Source:** https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel

---

*   [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Introduction to Project Finance Modeling in Excel
=================================================

*   Last updated on July 28, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post written by **Paramdeep** from Pristine__. Chandoo.org runs Financial Modeling School program in partnership with Pristine Careers. Visit [Financial Modeling School](http://chandoo.org/wp/financial-modeling/)
 to join our training program._

**Greetings!**

It’s been long time since we interacted on Chandoo.org. Actually I was very busy teaching the 105 awesome students for [financial modeling in Excel](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
. We all worked together to create some easy and some complex financial models. I found the journey to be quite exciting and enriching (From the feedback that I got, my students too didn’t find it bad either 😉 )

During the interaction, I found that **a lot of students were looking for financial modeling around the project financing as well**. So we thought why not introduce financial modeling for project finance.

**In this post I will speak about some of the key aspects of a project finance model and why it can be different from modeling a normal company.**

![Introduction to Project Finance Modeling using MS Excel - Chandoo.org](https://chandoo.org/img/fm/introduction-to-project-finance-modeling-using-excel.png)

What is so Special About Project Finance?
-----------------------------------------

An organization is an on-going entity – the basic assumption being that it would continue business for time immemorial. Project finance is different. It exists for a limited duration (though that duration is usually long – 20 to 30 Years!) and the project is structured in a special purpose vehicle (SPV). The SPV exists for a specific period of time and after the purpose of the project is solved, the SPV is dissolved. That means that the horizon of analysis is NOT time immemorial but a known time frame for which the SPV is formed.

The other typical difference is that these are long gestation projects, with almost no cash flow in the beginning and a lot of parties involved. This basic difference in the structure creates a lot of issues, Principal – Agency problem because of large number of parties, everybody trying to maximize their returns in a short time, propensity to wait decreases significantly and the initial project gestation period is critical to success of project.

_**Summarizing, Project Finance is the financing of**_

*   Often long-term, industrial projects
*   Increasingly those which provide public services or infrastructure
*   Based upon complex financial and contractual structures commonly involving many legal entities

_**Two main types of Project Financing**_

*   Greenfield – a fresh start
*   Brownfield – expansion of an existing project

### Key Aspects of Project Finance

I will highlight some of the other key aspects of Project finance.

*   **Separate Entity (Parent) and SPV Status** – Risk of the transaction is generally measured by the creditworthiness of the project itself rather than that of its owners (Sponsors).
*   **Project Finance debt is often termed as “non-recourse”**– That means the financial institutions cannot go to the parent level to get their money back. The money has to be generated at the SPV level. Typically these loans are secured by the project assets and the core project contracts.
*   **Timing of Cash Flow**: The cash flows from the project comes only after the project is fully complete (takes more than a single financial year for completion) and are usually the sole means of repayment of the borrowed funds
*   **Multiple parties involved**
    *   Sponsors
    *   Contractors
    *   Suppliers
    *   Governments
    *   Global financiers
*   **Long Gestation:** From inception of an idea to Financial Close, a Project Finance deal can take years to negotiate
*   **Identifying Risks:** The success of the project depends a lot on identifying risks, allocating them appropriately and ensuring that the responsible parties are adequately incentivized to manage their risks efficiently
    *   Construction time, costs & specification
    *   Operational cost, reliability
    *   Supply reliability, quality, cost
    *   Off-take volume, price
    *   Political environment, war, local hostility, currency in-convertibility
    *   Socio-environmental responsibilities

Modeling a Key Risk – Delay in Project Implementation
-----------------------------------------------------

**Because of the structure of the project one of the key risks in the project is the risk of delay**. Delay in project can significantly reduce the IRR ([what is it?](http://en.wikipedia.org/wiki/Internal_rate_of_return)
) of the project and completely take it off track! There are multiple ways in which projects can be delayed and each would have its own repercussions on the return. These can be (The list is not exhaustive):

*   There is an implementation risk (Delay because you could not execute the project in time)
*   Delay in start of project (Could be because of regulatory approvals – Regulatory Risk)
*   Delay in project because no funds were available (or delay in arranging the funds)
*   Delay in collection of revenues (You built at the right time, but could not sell – Selling risk)

Typically each of these delays would have different affect on the cash flows. For example, if you are implementing a real estate residential project and you are not able to sell the homes – you have incurred all your cash outflows and your inflows are delayed. This would spell doom for the returns. On the other hand, if there is a delay in staring the implementation because of non acquisition of land, typically your cash outflow is not there so the affect would not be that large.

### Why are delays more relevant for certain kind of investments?

Typically for long gestation projects – Roads, Real Estate, Power, Telecom, etc. there is a huge upfront investment. Even if there is a small delay in getting back the cash flows, it makes your project financials look very bad.

The Case of ABC Housing Co.
---------------------------

**ABC housing company is planning to start the project on 1 Jan 2002 and is expecting to complete the construction over a period of 3 years.** The construction cost is expected to be USD 1000 Mn. It is expecting to hold the property for a period of 5 years, in which it would get a lease rental of USD 100 Mn each year. After 5 years, it would sell the property at a value of USD 2000 Mn.

![Initial Setup - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-1.png)

### Modeling delays in Excel – Playing around with the date function

If you are planning to incorporate delays in your model, date function comes in very handy. For example, if you are expecting the construction period of 1 year, you can just put this as a parameter in your date (for years) and change his to see, if the construction period increases, what would be the effect on the project IRR.

The simple concept I have used here is to make the counter as a counter from the start date. The EOMONTH function calculates the end of month date of the particular month for which the date is given.

Now, I want to see if this is a construction year of not, I can just compare the number of years!

![Modeling Project Delays in Excel using EOMONTH Formula - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-2.png)

### Some assumptions to start with

I am assuming that once the project starts, the cost incurred during the construction period would be uniform. So if the construction is completed over a period of 3 years, each year 33% of the cost is incurred and if it is completed over 5 years, then 20% of the cost is incurred each year.

To model this in excel, I compare the current year with the time period when the construction started and allocate the cost.

![Modeling Project Delays in Excel using EOMONTH Formula - 2 - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-3.png)

Similarly for Leasing I assume that it gets leased out one year after the construction period and after the leasing is complete, ABC is able to sell the property at the desired price

### Calculating the Cash

There are two ways in which you generate cash – by lease and sale of property. The cash is consumed by your Capital expenditure.  Assuming there are no taxes, cash generated is just a combination of all these.

![Calculating Project Cash flows - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-4.png)

### Calculating the Return

As discussed last time, Internal Rate of Return (IRR) is an important aspect that all investors look at. Once we have the cash, we can simply ask excel to calculate the IRR for us. But in this case, since we have the exact year of cash with us, we will not use simple IRR function, but the XIRR function in Excel. This would take into account that all cash flows might not be at the year end.

![Calculating IRR for a Project - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-5.png)

### Scenario Analysis

Now that we have the model with us, we can change the construction period and see its effect on the IRR. If we want to do a complete scenario analysis, we can used Data Tables in Excel to generate a complete scenario analaysis.

Related Tip: [Learn how to work with Data Tables & Monte-carlo Simulations in Excel](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)

To create the data table, the structure of the table should look like:

![Project Scenario Analysis using Excel Data Tables - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-6.png)

Where 1, 2, 3 .. etc are the years of construction and the cell is linked to the IRR that we had calculated earlier.

Then select the data tables option within the data tab > What if Analaysis

![Create a data table in Excel - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-7.png)

Select the changing cell as the years of construction (In this case the change is in a column)

![Modeling project delays using data tables - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-8.png)

You can see that there is a significant change in the IRR of the project with a change in construction period.

![IRR calculations for various delay scenarios - Project finance modeling in Excel](https://chandoo.org/img/fm/introduction-to-project-finance-9.png)

So if you construction period is delayed from 3 years to 5 years, your IRR would change from 15.6% to 13.1% (and hence the investor interest would simply die out!!).

Templates to download
---------------------

I have created a template for you, where the subheadings are given and you have to link the model to get the cash numbers!

**[You can download the same from here](https://img.chandoo.org/d/Incorporating-Delays-Participant-Copy.xlsx)** \[[mirror](http://cid-b663e096d6c08c74.office.live.com/view.aspx/Public/fm/Incorporating-Delays-Participant-Copy.xlsx)\
\].

You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can [download this filled template](https://img.chandoo.org/d/Incorporating-Delays-Solution-Key.xlsx)
 \[[mirror](http://cid-b663e096d6c08c74.office.live.com/view.aspx/Public/fm/Incorporating-Delays-Solution-Key.xlsx)\
\] and check, if the information you recorded, matches mine or not! 🙂

I am just doing that for the single sheet model and recommend that you do the same for multi-sheet model as a homework problem. If you face any issue, post your excel with the exact problem and we can discuss the way to move forward.  
[![Project Finance Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/project-finance-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "Project Finance Modeling using Excel - Online Classes by Chandoo.org & Pristine")

### Next Steps

This series gives you a flavor of how financial modeling is done and an idea about specific nuances in modeling for long gestation projects. In the next part of this, we will learn how the interest payments of a project should be modeled.

### Join our Financial Modeling & Project Finance Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**

For any queries regarding the cash impact or financial modeling, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [7 Comments](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/#respond)
    
*   Tagged under [data tables](https://chandoo.org/wp/tag/data-tables/)
    , [date and time](https://chandoo.org/wp/tag/date-and-time/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [eomonth](https://chandoo.org/wp/tag/eomonth/)
    , [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [IRR](https://chandoo.org/wp/tag/irr/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [project finance](https://chandoo.org/wp/tag/project-finance/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [xirr()](https://chandoo.org/wp/tag/xirr/)
    
*   Category: [Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousMake Awesome Data Entry Forms by using Conditional Formatting + Data Validation](https://chandoo.org/wp/data-entry-forms-with-conditional-formatting-and-validation/)

[NextSimple Excel Formula to Calculate All-time High, Trailing 12 Month High Values \[Quick Tip\]Next](https://chandoo.org/wp/excel-formula-to-calculate-all-time-high-and-trailing-12-month-high/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/introduction-to-project-finance-modeling-in-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ